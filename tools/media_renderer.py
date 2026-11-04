"""Render simulator snapshots using original meshes and a simpler lighting model."""

import json
import math
import os
from pathlib import Path
import re

os.environ.setdefault('PYOPENGL_PLATFORM', 'egl')

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pyrender
import trimesh


FLIP = np.diag([-1., 1., 1., 1.])


class Renderer:
    def __init__(self, cache, config):
        self.cache = cache
        self.config = config
        size = config.get('image_size', {'x': 500, 'y': 300})
        self.width, self.height = size['x'], size['y']
        if not (1 <= self.width <= 4096 and 1 <= self.height <= 4096):
            raise ValueError('Invalid example image dimensions')
        self.output_width = min(260, self.width // 3) if config.get('show_output', False) else 0
        self.renderer = pyrender.OffscreenRenderer(self.width - self.output_width, self.height)
        self.meshes = {}
        self.models = {}
        self.blocks = {}
        self.camera = json.loads((cache / 'camera.json').read_text())
        records = json.loads((cache / 'resources.json').read_text())
        self.names = {name: token for token, name in json.loads((cache / 'meshes.json').read_text()).items()}
        self.design = next(row['data']['farmRenderer'] for row in records if row['type'] == 'DesignConstants')
        self.grounds = {row['data']['objectName']: row['data'] for row in records
                        if row['type'] in {'GroundSO', 'MushroomGroundSO'}}
        try:
            self.font = ImageFont.truetype('DejaVuSans.ttf', 13)
        except OSError:
            self.font = ImageFont.load_default()

    def close(self):
        self.renderer.delete()

    def mesh(self, mesh_id):
        if mesh_id not in self.meshes:
            with np.load(self.cache / f'mesh-{mesh_id}.npz', allow_pickle=False) as data:
                vertices = data['vertices'].copy()
                vertices[:, 0] *= -1
                model = trimesh.Trimesh(vertices=vertices, faces=data['faces'][:, ::-1],
                                        vertex_colors=data['colors'], process=False)
            self.models[mesh_id] = model
            self.meshes[mesh_id] = pyrender.Mesh.from_trimesh(model, smooth=False)
        return self.meshes[mesh_id]

    def add_model(self, scene, mesh_id, pose):
        mesh = self.mesh(mesh_id)
        if not np.isfinite(pose).all():
            raise ValueError('Non-finite model transform')
        if np.any(np.linalg.norm(pose[:3, :3], axis=0) < 1e-9):
            # Pyrender cannot decompose zero scales; bake these growth/tail transforms.
            model = self.models[mesh_id]
            baked = trimesh.Trimesh(vertices=trimesh.transform_points(model.vertices, pose),
                                    faces=model.faces, vertex_colors=model.visual.vertex_colors,
                                    process=False)
            faces = baked.nondegenerate_faces()
            if faces.any():
                baked.update_faces(faces)
                scene.add(pyrender.Mesh.from_trimesh(baked, smooth=False))
        else:
            scene.add(mesh, pose=pose)

    def block(self, color):
        key = tuple(round(value, 4) for value in color)
        if key not in self.blocks:
            material = pyrender.MetallicRoughnessMaterial(
                baseColorFactor=color, metallicFactor=0, roughnessFactor=1)
            self.blocks[key] = pyrender.Mesh.from_trimesh(trimesh.creation.box(), material=material)
        return self.blocks[key]

    def camera_pose(self, frame):
        q = self.camera['rotation']
        rotation = trimesh.transformations.quaternion_matrix([q['w'], q['x'], q['y'], q['z']])
        pose = FLIP @ rotation @ np.diag([1., 1., -1., 1.])
        position = self.config.get('camera_position', {'x': 0, 'y': 0, 'z': 0})
        origin = self.camera['origin']
        pose[:3, 3] = np.array([-(position['x'] - origin['x']),
                                position['y'] - origin['y'], position['z'] - origin['z']])
        # Follow the drone underground without changing the source camera's framing.
        if frame['drones']:
            pose[2, 3] -= frame['drones'][0]['position'][2]
        return pose

    def render(self, frame):
        scene = pyrender.Scene(bg_color=[0.48, 0.61, 0.66, 1], ambient_light=[0.7, 0.7, 0.7])
        bottom = max(tile['depth'] for tile in frame['tiles']) + 1
        for tile in frame['tiles']:
            height = bottom - tile['depth']
            pose = np.diag([1., 1., float(height), 1.])
            pose[:3, 3] = [tile['x'], tile['y'], -tile['depth'] - height / 2]
            scene.add(self.block(tile['color']), pose=pose)
            for decoration in self.grounds[tile['ground']]['decorations']:
                if not decoration['top'] or decoration['probability'] < 1:
                    continue
                mesh_id = decoration['mesh']['m_PathID']
                if not mesh_id:
                    continue
                pose = trimesh.transformations.rotation_matrix(
                    math.radians(decoration['fixedRotation']), [0, 0, 1])
                pose[:3, 3] = [-tile['x'], tile['y'], -tile['depth']]
                scene.add(self.mesh(mesh_id), pose=FLIP @ pose @ FLIP)
        for model in frame['meshes'] + frame['drones']:
            pose = FLIP @ np.asarray(model['matrix']).reshape(4, 4) @ FLIP
            self.add_model(scene, model['id'], pose)
        for drone in frame['drones']:
            matrix = np.asarray(drone['matrix']).reshape(4, 4)
            self.add_model(scene, self.names['Drone'], FLIP @ matrix @ FLIP)
            for i in range(1, 5):
                offset = self.design['propellerOffset' + str(i)]
                spin = trimesh.transformations.rotation_matrix(frame['time'] * 50, [0, 0, 1])
                spin[:3, 3] = [offset['x'], offset['y'], offset['z']]
                self.add_model(scene, self.names['Propeller'], FLIP @ matrix @ spin @ FLIP)
            if drone['digging'] > 0:
                drill = trimesh.transformations.rotation_matrix(frame['time'] * 30, [0, 0, 1])
                drill[:3, 3] = [0, 0, -0.7]
                self.add_model(scene, self.names['Drill.008'], FLIP @ matrix @ drill @ FLIP)
        pose = self.camera_pose(frame)
        scene.add(pyrender.PerspectiveCamera(yfov=math.radians(self.camera['fov'])), pose=pose)
        scene.add(pyrender.DirectionalLight(color=[1, 1, 1], intensity=1.8), pose=pose)
        pixels, _ = self.renderer.render(scene, flags=pyrender.RenderFlags.SKIP_CULL_FACES)
        image = Image.new('RGB', (self.width, self.height), '#25292d')
        image.paste(Image.fromarray(pixels), (0, 0))
        draw = ImageDraw.Draw(image, 'RGBA')
        if self.config.get('show_inventory', True):
            items = [(name.replace('_', ' '), value) for name, value in frame['inventory'].items() if value]
            for i, (name, value) in enumerate(items):
                y = 9 + i * 19
                if y + 18 > self.height:
                    break
                label = f'{name}: {value:,.8g}'
                width = draw.textlength(label, font=self.font)
                draw.rectangle((7, y - 2, width + 19, y + 17), fill=(29, 36, 40, 190))
                draw.text((12, y), label, fill='white', font=self.font)
        if self.output_width:
            x = self.width - self.output_width + 10
            draw.text((x, 8), 'Output', fill='#a4b7c4', font=self.font)
            text = re.sub(r'</?(?:color|b|i|size)(?:=[^>]+)?>', '', frame['output'])
            width = max(1, (self.output_width - 20) // 8)
            lines = [part[start:start + width] for part in text.splitlines()
                     for start in range(0, max(1, len(part)), width)]
            lines = lines[-max(1, (self.height - 40) // 18):]
            for i, line in enumerate(lines):
                draw.text((x, 33 + 18 * i), line, fill='white', font=self.font)
        return image
