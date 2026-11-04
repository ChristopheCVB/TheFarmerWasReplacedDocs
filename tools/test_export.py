"""Small regression checks for text conversion, binary decoding, and the exported collection."""

import json
from pathlib import Path
import re
import struct
import unittest
import zlib

from export_docs import Exporter, entries, examples, generic_data_locations, multiline_code, validate
from packaged_assets import Reader, decode_value


class ConversionTests(unittest.TestCase):
    def test_entries_preserve_multiline_values(self):
        self.assertEqual(entries('@one = first\n\nsecond\n@two = last\n'),
                         {'one': 'first\n\nsecond', 'two': 'last'})
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            entries('@one = first\n@one = second')

    def test_example_preserves_setup_code_and_conditions(self):
        source = ('{{codeexample\n{"seed": 3, "show_image": true}\n'
                  '#SETUP\ntill()\n#CODE\nx = {"nested": {"a": 1}}\nprint(x)\n}}')
        text, count = examples(source)
        self.assertEqual(count, 1)
        self.assertIn('```python\ntill()\n```', text)
        self.assertIn('x = {"nested": {"a": 1}}', text)
        self.assertIn('"seed": 3', text)
        self.assertNotIn('show_image', text)

    def test_example_without_setup(self):
        text, count = examples('{{codeexample\n{}\n#CODE\njump()\n}}')
        self.assertEqual(count, 1)
        self.assertNotIn('Example setup', text)
        self.assertIn('jump()', text)

    def test_example_closing_next_to_unlock_tag(self):
        text, count = examples('{{codeexample\n{}\n#CODE\nx = (1, 2)\n}}</unlock>')
        self.assertEqual(count, 1)
        self.assertIn('</unlock>', text)

    def test_example_requires_code_marker(self):
        with self.assertRaisesRegex(ValueError, '#CODE'):
            examples('{{codeexample\n{}\n#SETUP\njump()\n}}')

    def test_multiline_code_preserves_existing_fences(self):
        text = 'Example:\n`if True:\n    harvest()`\n\n```python\nprint("`x`")\n```\n'
        result = multiline_code(text)
        self.assertIn('```python\nif True:\n    harvest()\n```', result)
        self.assertIn('```python\nprint("`x`")\n```', result)

    def test_inline_code_across_table_rows_stays_inline(self):
        text = '| Parent | `mining` |\n| Unlocks | `clay`, `rice` |\n\nSource: `resources.assets`.\n'
        self.assertEqual(multiline_code(text), text)

    def test_rewrite_keeps_code_literal_and_resolves_alias_routes(self):
        exporter = object.__new__(Exporter)
        exporter.all_strings = {'grass': 'Grass'}
        exporter.routes = {'objects/dynamite': 'objects/dynamite.md',
                           'grounds/dynamite': 'grounds/dynamite.md',
                           'unlocks/grass': 'unlocks/grass.md'}
        source = ('[{{@grass}}](unlocks/grass)\n[Entity](objects/dynamite)\n'
                  '[Ground](grounds/dynamite)\n\n```python\nprint("<unlock=x>{{literal}}")\n```')
        text = exporter.rewrite(source, 'guides/home.md')
        self.assertIn('[Grass](../unlocks/grass.md)', text)
        self.assertIn('[Entity](../objects/dynamite.md)', text)
        self.assertIn('[Ground](../grounds/dynamite.md)', text)
        self.assertIn('print("<unlock=x>{{literal}}")', text)
        with self.assertRaisesRegex(ValueError, 'Unresolved'):
            exporter.rewrite('[Missing](objects/does_not_exist)', 'guides/home.md')

    def test_binary_boundaries_and_booleans(self):
        self.assertEqual(Reader(b'\x03\0\0\0abc\0').string(), 'abc')
        with self.assertRaisesRegex(ValueError, 'string length'):
            Reader(b'\xff\xff\xff\x7f').string()
        with self.assertRaisesRegex(ValueError, 'boolean'):
            decode_value(Reader(b'\x02\0\0\0'), 'bool', {})

    def test_logical_data_paths_and_platform_list(self):
        source = ('Before.\n\nThe persistent data folder is located at:\n\n'
                  '- Windows: `<profile>/vendor/game`\n'
                  '- macOS: `<profile>/vendor/game`\n'
                  '- Linux: `<profile>/vendor/game`\n\nAfter.\n')
        result = generic_data_locations(source)
        self.assertIn('Before.', result)
        self.assertIn('After.', result)
        self.assertIn('`<game-data>/`', result)
        self.assertNotIn('<profile>', result)
        self.assertNotIn('- Windows:', result)
        exporter = object.__new__(Exporter)
        exporter.all_strings, exporter.routes = {}, {}
        for suffix in ['Saves', 'Backup', 'output.txt']:
            expected = suffix if '.' in suffix else suffix + '/'
            self.assertEqual(exporter.rewrite(f'[Location](persistent_data_path/{suffix})', 'guides/test.md'),
                             f'Location (`<game-data>/{expected}`)')


class CollectionTests(unittest.TestCase):
    root = Path(__file__).resolve().parent.parent

    def test_collection_coverage_and_links(self):
        result = validate(self.root)
        manifest = json.loads((self.root / 'tools/extraction_manifest.json').read_text())
        self.assertEqual(result['source_entries'], sum(manifest['string_counts'].values()))
        self.assertGreater(result['pages'], manifest['guide_count'])
        self.assertEqual(result['images'], 5)

    def test_png_checksums_and_complete_pixels(self):
        for path in sorted((self.root / 'assets').glob('*.png')):
            with self.subTest(image=path.name):
                data = path.read_bytes()
                self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
                offset, compressed, width, height = 8, b'', 0, 0
                while offset < len(data):
                    size = struct.unpack_from('>I', data, offset)[0]
                    kind = data[offset + 4:offset + 8]
                    payload = data[offset + 8:offset + 8 + size]
                    crc = struct.unpack_from('>I', data, offset + 8 + size)[0]
                    self.assertEqual(crc, zlib.crc32(kind + payload) & 0xffffffff)
                    if kind == b'IHDR':
                        width, height = struct.unpack_from('>II', payload)
                    if kind == b'IDAT':
                        compressed += payload
                    offset += size + 12
                self.assertEqual(offset, len(data))
                self.assertEqual(len(zlib.decompress(compressed)), (width * 3 + 1) * height)

    def test_references_and_extracted_settings(self):
        for path in ['code/range.md', 'code/append.md', 'code/add.md', 'code/reset.md',
                     'objects/dynamite.md', 'grounds/dynamite.md']:
            self.assertTrue((self.root / path).is_file(), path)
        carrot = (self.root / 'objects/carrot.md').read_text()
        self.assertIn('| Mean base growth time (seconds) | 6 |', carrot)
        self.assertIn('1 × Wood, 1 × Hay', carrot)
        clay = (self.root / 'grounds/clay.md').read_text()
        self.assertIn('| Stability | 3 |', clay)

    def test_collection_uses_portable_paths(self):
        def strings(value):
            if isinstance(value, str):
                yield value
            elif isinstance(value, dict):
                for key, item in value.items():
                    yield key
                    yield from strings(item)
            elif isinstance(value, list):
                for item in value:
                    yield from strings(item)

        patterns = [r'(?<![\w])[A-Za-z]:[\\/][\w]', r'/mnt/[a-z]/', r'/home/[^/\s]+/',
                    r'(?i)AppData|LocalLow|%USERPROFILE%',
                    r'~/Library/', r'~/\.steam/']
        for path in self.root.rglob('*'):
            if any(part in {'.media-cache', '.venv', '.git'} for part in path.relative_to(self.root).parts):
                continue
            if path.is_file() and path.suffix in {'.md', '.json'}:
                text = path.read_text(encoding='utf-8')
                if path.suffix == '.json':
                    text = '\n'.join(strings(json.loads(text)))
                for pattern in patterns:
                    self.assertIsNone(re.search(pattern, text), f'{path.relative_to(self.root)}: {pattern}')
        manifest = json.loads((self.root / 'tools/extraction_manifest.json').read_text())
        self.assertIn('created_utc', manifest)
        self.assertIn('unity_version', manifest)
        for source in manifest['sources']:
            self.assertFalse(source.startswith('/'))
            self.assertNotIn('\\', source)
        self.assertTrue((self.root / 'tools/README.md').is_file())


if __name__ == '__main__':
    unittest.main(verbosity=2)
