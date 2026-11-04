"""Optional extraction of the resources needed by the offline simulator and renderer."""

import hashlib
import json
from pathlib import Path

from packaged_assets import Reader, read_assets


def verify_game(game):
    schema = json.loads(Path(__file__).with_name('layouts.json').read_text())
    root = game / 'TheFarmerWasReplaced_Data'
    for name, expected in schema['assemblies'].items():
        if hashlib.sha256((root / 'Managed' / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'{name} changed; this game build is unsupported')
    read_assets(root / 'globalgamemanagers.assets', schema['unity_version'])
    return root, schema['unity_version']


def extract_media(game, cache):
    import numpy as np
    import UnityPy
    from UnityPy.helpers import TypeTreeHelper
    from UnityPy.helpers.MeshHelper import MeshHandler
    from UnityPy.helpers.TypeTreeGenerator import TypeTreeGenerator

    root, version = verify_game(game)
    cache.mkdir(parents=True, exist_ok=True)
    generator = TypeTreeGenerator(version)
    generator.load_local_game(str(game))
    # UnityPy's accelerated reader caches the uncorrected generated node layout.
    TypeTreeHelper.read_typetree_boost = False
    scripts = {}
    for pid, (kind, data) in read_assets(root / 'globalgamemanagers.assets', version).items():
        if kind == 115:
            reader = Reader(data)
            reader.string()
            reader.offset += 20
            name, namespace, assembly = reader.string(), reader.string(), reader.string()
            scripts[pid] = ((namespace + '.' if namespace else '') + name, assembly)

    def tree(assembly, name):
        node = generator.get_nodes_up(assembly, name)
        for field in node.traverse():
            # shortcut: TypeTreeGeneratorAPI 0.0.10 omits header alignment and labels
            # List<string> as string; remove these corrections when its layout is fixed.
            if field.m_Name == 'm_Enabled':
                field.m_MetaFlag = (field.m_MetaFlag or 0) | 0x4000
            if (field.m_Type == 'string' and field.m_Children
                    and field.m_Children[0].m_Children[-1].m_Type != 'char'):
                field.m_Type = 'vector'
        return node

    env = UnityPy.load(str(root / 'resources.assets'))
    objects = {obj.path_id: obj for obj in env.objects}
    scene = UnityPy.load(str(root / 'level0'))
    scene_objects = {obj.path_id: obj for obj in scene.objects}
    records = []
    selected = {'EntitySO', 'GroundSO', 'MushroomGroundSO', 'HatSO', 'ItemSO',
                'UnlockSO', 'LeaderboardSO', 'DroneSO', 'DesignConstants'}
    for filename, lookup in [('resources.assets', objects), ('level0', scene_objects)]:
        for pid, (kind, data) in read_assets(root / filename, version).items():
            if kind != 114:
                continue
            reader = Reader(data, 16)
            file_id, script_id = reader.read('iq')
            if file_id != 1:
                continue
            name, assembly = scripts.get(script_id, ('', ''))
            if name not in selected and 'Feature' not in name:
                continue
            if filename == 'level0' and name != 'DesignConstants':
                continue
            values = lookup[pid].parse_as_dict(tree(assembly, name))
            records.append({'id': pid if filename == 'resources.assets' else -pid,
                            'type': name, 'data': values})
    if sum(row['type'] == 'DesignConstants' for row in records) != 1:
        raise ValueError('Expected one scene configuration')

    shared = UnityPy.load(str(root / 'sharedassets0.assets'))
    palette_obj = next(obj for obj in shared.objects
                       if obj.type.name == 'Texture2D' and obj.peek_name() == 'ColorPalette2')
    palette = np.asarray(palette_obj.parse_as_object().image.convert('RGBA'))
    names = {}
    render_objects = [(str(obj.path_id), obj, True) for obj in objects.values()]
    render_objects += [('shared-' + str(obj.path_id), obj, False) for obj in shared.objects
                       if obj.type.name == 'Mesh' and obj.peek_name() in {'Drone', 'Propeller', 'Drill.008'}]
    for token, obj, local in render_objects:
        if obj.type.name not in {'Mesh', 'AudioClip', 'Material'}:
            continue
        name = obj.peek_name()
        if local:
            records.append({'id': obj.path_id, 'type': 'UnityEngine.' + obj.type.name,
                            'data': {'m_Name': name}})
        if obj.type.name != 'Mesh':
            continue
        handler = MeshHandler(obj.parse_as_object())
        handler.process()
        vertices = np.asarray(handler.m_Vertices, dtype=np.float32)
        faces = np.asarray([triangle for group in handler.get_triangles() for triangle in group],
                           dtype=np.uint32)
        if handler.m_Colors:
            colors = np.clip(np.asarray(handler.m_Colors) * 255, 0, 255).astype(np.uint8)
        elif handler.m_UV0:
            uv = np.asarray(handler.m_UV0)
            x = np.clip((uv[:, 0] * palette.shape[1]).astype(int), 0, palette.shape[1] - 1)
            y = np.clip(((1 - uv[:, 1]) * palette.shape[0]).astype(int), 0, palette.shape[0] - 1)
            colors = palette[y, x].copy()
        else:
            raise ValueError(f'Mesh has neither colors nor palette UVs: {name}')
        np.savez_compressed(cache / f'mesh-{token}.npz', vertices=vertices,
                            faces=faces, colors=colors)
        names[token] = name
    (cache / 'resources.json').write_text(json.dumps(records), encoding='utf-8')
    (cache / 'meshes.json').write_text(json.dumps(names), encoding='utf-8')

    camera_obj = next(obj for obj in scene.objects if obj.type.name == 'Camera'
                      and obj.parse_as_object().m_GameObject.deref().parse_as_object().m_Name == 'UIFarmCamera')
    camera = camera_obj.parse_as_dict()
    go = camera_obj.parse_as_object().m_GameObject.deref().parse_as_object()
    transform = next(component.component.deref().parse_as_dict() for component in go.m_Component
                     if component.component.deref().type.name == 'Transform')
    parent = scene_objects[transform['m_Father']['m_PathID']].parse_as_dict()
    camera_data = {'fov': camera['field of view'], 'rotation': transform['m_LocalRotation'],
                   'origin': parent['m_LocalPosition']}
    (cache / 'camera.json').write_text(json.dumps(camera_data), encoding='utf-8')
    return records
