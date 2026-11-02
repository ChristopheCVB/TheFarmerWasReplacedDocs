"""Read the documentation assets without loading or modifying the game."""

import hashlib
import json
from pathlib import Path
import struct
import zlib


class Reader:
    def __init__(self, data, offset=0):
        self.data = data
        self.offset = offset

    def read(self, fmt):
        result = struct.unpack_from('<' + fmt, self.data, self.offset)
        self.offset += struct.calcsize('<' + fmt)
        return result[0] if len(result) == 1 else result

    def align(self):
        self.offset = (self.offset + 3) // 4 * 4

    def string(self):
        size = self.read('i')
        if not 0 <= size <= len(self.data) - self.offset:
            raise ValueError('Invalid serialized string length')
        value = self.data[self.offset:self.offset + size].decode('utf-8')
        self.offset += size
        self.align()
        return value


def read_assets(path, version):
    data = path.read_bytes()
    if struct.unpack_from('>I', data, 8)[0] != 22:
        raise ValueError(f'Unsupported serialized asset format: {path}')
    start = struct.unpack_from('>q', data, 32)[0]
    end = data.index(b'\0', 48)
    if data[48:end].decode() != version:
        raise ValueError('Unity version changed; update the serialized layouts')
    reader = Reader(data, end + 5)
    if reader.read('B'):
        raise ValueError('Unexpected embedded type trees; update the asset reader')
    types = []
    for _ in range(reader.read('i')):
        class_id = reader.read('i')
        reader.offset += 3 + (16 if class_id == 114 else 0) + 16
        types.append(class_id)
    objects = {}
    for _ in range(reader.read('i')):
        reader.align()
        path_id, offset, size, type_id = reader.read('qqIi')
        if not (0 <= type_id < len(types) and 0 <= start + offset <= len(data) - size):
            raise ValueError('Invalid asset object bounds')
        objects[path_id] = (types[type_id], data[start + offset:start + offset + size])
    return objects


def decode_value(reader, kind, layouts):
    primitives = {'int': 'i', 'uint': 'I', 'float': 'f', 'double': 'd', 'long': 'q'}
    if kind in primitives:
        return reader.read(primitives[kind])
    if kind == 'string':
        return reader.string()
    if kind == 'bool':
        value = reader.read('B')
        if value not in (0, 1):
            raise ValueError('Invalid serialized boolean; field layout changed')
        reader.align()
        return bool(value)
    if kind in ('Mesh', 'Material', 'AudioClip'):
        file_id, path_id = reader.read('iq')
        return {'file_id': file_id, 'path_id': path_id}
    if kind in ('Vector3', 'Color'):
        return list(reader.read('fff' if kind == 'Vector3' else 'ffff'))
    if kind.endswith('[]') or kind.startswith('List`1<'):
        inner = kind[:-2] if kind.endswith('[]') else kind[7:-1]
        count = reader.read('i')
        if not 0 <= count <= 10000:
            raise ValueError('Invalid serialized array length')
        return [decode_value(reader, inner, layouts) for _ in range(count)]
    definition = layouts[kind]
    if definition['parent'] == 'Enum':
        return reader.read('i')
    values = {}
    for field, field_kind in definition['fields']:
        if field_kind == 'Gradient':
            # shortcut: visual ground decorations are omitted; extend if documentation needs them.
            break
        values[field] = decode_value(reader, field_kind, layouts)
    return values


def png_chunk(kind, payload):
    return struct.pack('>I', len(payload)) + kind + payload + struct.pack(
        '>I', zlib.crc32(kind + payload) & 0xffffffff)


def export_texture(data, root, target):
    reader = Reader(data)
    name = reader.string()
    reader.read('i')
    width, height, complete_size, stripped, fmt, mip_count = reader.read('6i')
    if not (fmt == 3 and mip_count == 1 and stripped == 0
            and 0 < width <= 10000 and 0 < height <= 10000
            and complete_size == width * height * 3):
        raise ValueError(f'Unsupported documentation texture format: {name}')
    # shortcut: this build stores these RGB24 textures in external streams; update on format changes.
    reader.offset += 64
    offset, size = reader.read('QI')
    resource = reader.string()
    if Path(resource).name != resource or reader.offset != len(data):
        raise ValueError('Unexpected texture stream layout')
    with (root / resource).open('rb') as stream:
        stream.seek(offset)
        pixels = stream.read(size)
    if len(pixels) != complete_size:
        raise ValueError(f'Incomplete documentation texture: {name}')
    row_size = width * 3
    rows = b''.join(b'\0' + pixels[y * row_size:(y + 1) * row_size]
                    for y in range(height - 1, -1, -1))
    target.write_bytes(b'\x89PNG\r\n\x1a\n'
                      + png_chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
                      + png_chunk(b'IDAT', zlib.compress(rows))
                      + png_chunk(b'IEND', b''))
    return {'name': name, 'width': width, 'height': height}


def extract(game, output, image_names):
    root = game / 'TheFarmerWasReplaced_Data'
    schema = json.loads(Path(__file__).with_name('layouts.json').read_text())
    for name, expected in schema['assemblies'].items():
        if hashlib.sha256((root / 'Managed' / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'{name} changed; regenerate layouts.json before exporting this build')
    globals_ = read_assets(root / 'globalgamemanagers.assets', schema['unity_version'])
    scripts = {}
    for path_id, (class_id, data) in globals_.items():
        if class_id == 115:
            reader = Reader(data)
            reader.string()
            reader.offset += 20
            scripts[path_id] = reader.string()
    objects = read_assets(root / 'resources.assets', schema['unity_version'])
    categories = {'EntitySO': ('objects', 'objectName'), 'GroundSO': ('grounds', 'objectName'),
                  'MushroomGroundSO': ('grounds', 'objectName'), 'ItemSO': ('items', 'itemName'),
                  'HatSO': ('hats', 'hatName'), 'UnlockSO': ('unlocks', 'unlockName'),
                  'LeaderboardSO': ('leaderboards', 'leaderboardName')}
    records, images = [], []
    (output / 'assets').mkdir(parents=True, exist_ok=True)
    for path_id, (class_id, data) in objects.items():
        if class_id == 28:
            name = Reader(data).string()
            if name in image_names:
                images.append(export_texture(data, root, output / 'assets' / (name + '.png')))
        if class_id != 114:
            continue
        reader = Reader(data, 16)
        script_file, script_id = reader.read('iq')
        if script_file != 1 or scripts.get(script_id) not in categories:
            continue
        kind = scripts[script_id]
        asset_name = reader.string()
        layout_kind = 'GroundSO' if kind == 'MushroomGroundSO' else kind
        values = decode_value(reader, layout_kind, schema['types'])
        if layout_kind != 'GroundSO' and reader.offset != len(data):
            raise ValueError(f'Unconsumed bytes in {kind} {asset_name}: {reader.offset}/{len(data)}')
        category, name_field = categories[kind]
        records.append({'category': category, 'name': values[name_field], 'class': kind,
                        'asset': asset_name, 'path_id': path_id, 'values': values})
    if {image['name'] for image in images} != set(image_names):
        raise ValueError('Missing documentation illustrations')
    return records, images, schema['unity_version']
