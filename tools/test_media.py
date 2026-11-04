"""Regression checks; installed-game integration is opt-in through TFWR_GAME_DIR."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from code_examples import animations, collect, identify, parse_block, plain_output, recordings
from export_docs import examples, Exporter


class ExampleTests(unittest.TestCase):
    source = ('{{codeexample\n{"show_image":true,"camera_position":{"x":0,"y":1.5,"z":4}}\n'
              '#SETUP\ndo_a_flip()\n#CODE\nx = {"a": {"b": 1}}\nharvest()\n}}')

    def test_shared_parser_retains_full_configuration(self):
        first = collect(self.source, 'guides/first.md')[0]
        self.assertEqual(first['config']['camera_position']['y'], 1.5)
        self.assertEqual(first['setup'], 'do_a_flip()')
        self.assertIn('x = {"a": {"b": 1}}', first['code'])
        self.assertEqual(first['gif'], 'assets/examples/first-01.gif')
        changed = identify(dict(config=first['config'], setup=first['setup'], code='harvest()'),
                           first['page'], 1)
        self.assertEqual(first['id'], changed['id'])
        self.assertNotEqual(first['source_hash'], changed['source_hash'])

    def test_parse_multiple_blocks_and_adjacent_unlock(self):
        entries = collect(self.source + '</unlock>\n' + self.source, 'guides/test.md')
        self.assertEqual([entry['ordinal'] for entry in entries], [1, 2])
        text, count = examples(self.source, {1: entries[0]['gif']})
        self.assertEqual(count, 1)
        self.assertIn('<details>\n<summary>Animated example</summary>', text)
        self.assertNotIn('<details open', text)
        self.assertIn('```python', text)

    def test_reject_invalid_configuration_and_missing_code(self):
        with self.assertRaisesRegex(ValueError, 'object'):
            parse_block('[]\n#CODE\nharvest()')
        with self.assertRaisesRegex(ValueError, '#CODE'):
            parse_block('{}\n#SETUP\nharvest()')

    def test_only_current_successful_media_is_selected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry = collect(self.source, 'guides/test.md')[0]
            gif = root / entry['gif']
            gif.parent.mkdir(parents=True)
            gif.write_bytes(b'GIF89a-test-content')
            generated = dict(entry, status='generated', sha256=hashlib.sha256(gif.read_bytes()).hexdigest())
            report = {'sources': {}, 'tools': {}, 'examples': [generated]}
            (root / 'tools').mkdir()
            path = root / 'tools/example_media.json'
            path.write_text(json.dumps(report))
            self.assertEqual(set(animations(root, [entry], root)), {entry['id']})
            changed = dict(entry, source_hash='changed')
            self.assertFalse(animations(root, [changed], root))
            gif.write_bytes(b'corrupted')
            self.assertFalse(animations(root, [entry], root))
            generated['gif'] = '../outside.gif'
            path.write_text(json.dumps(report))
            with self.assertRaisesRegex(ValueError, 'path'):
                animations(root, [entry], root)

    def test_output_panels_preserve_literal_text_and_disclose_limits(self):
        self.assertEqual(plain_output('<font=code><noparse><b>literal</b></noparse></font>'),
                         '<b>literal</b>')
        output = ('<color=red>Error:</color> func()\n^^^^^ \n<unlock=x>{{literal}}\n```\n[a](missing)'
                  '\n{{codeexample\n</pre><script>unsafe</script>')
        entry = {'output': plain_output(output), 'completed': False}
        text, _ = examples(self.source, {1: 'example.gif'}, {1: entry})
        self.assertLess(text.index('<summary>Animated example'), text.index('<summary>Example output'))
        self.assertIn('<pre>Error: func()\n^^^^^&#32;\n&lt;unlock=x&gt;{{literal}}\n```\n[a](missing)', text)
        self.assertIn('&lt;/pre&gt;&lt;script&gt;unsafe&lt;/script&gt;</pre>', text)
        self.assertNotIn('<script>', text)
        self.assertIn('capped at 30 seconds', text)
        exporter = object.__new__(Exporter)
        exporter.all_strings, exporter.routes = {}, {}
        exporter.animation_paths = {'example.gif'}
        self.assertIn('<pre>Error: func()', exporter.rewrite(text, 'guides/test.md'))
        silent, _ = examples(self.source, outputs={1: {'output': '', 'completed': True}})
        self.assertIn('*No output.*', silent)
        self.assertNotIn('capped', silent)
        self.assertNotIn('Example output</summary>', examples(self.source)[0])

    def test_recorded_output_requires_current_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry = collect(self.source, 'guides/test.md')[0]
            generated = dict(entry, status='generated', output='5', completed=True)
            (root / 'tools').mkdir()
            path = root / 'tools/example_media.json'
            report = {'sources': {}, 'tools': {}, 'examples': [generated]}
            path.write_text(json.dumps(report))
            self.assertEqual(recordings(root, [entry], root)[entry['id']]['output'], '5')
            self.assertFalse(recordings(root, [dict(entry, source_hash='changed')], root))
            report['sources']['missing'] = 'outdated'
            path.write_text(json.dumps(report))
            self.assertFalse(recordings(root, [entry], root))
            report['sources'] = {'../outside': 'unsafe'}
            path.write_text(json.dumps(report))
            with self.assertRaisesRegex(ValueError, 'provenance path'):
                recordings(root, [entry], root)

    def test_exporter_omits_failed_hidden_or_stale_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            game, output = root / 'game', root / 'export'
            english = game / 'TheFarmerWasReplaced_Data/StreamingAssets/Languages/EN'
            (english / 'docs').mkdir(parents=True)
            (english / 'Strings').mkdir()
            for name in ['code_tooltips', 'unlock_tooltips', 'object_tooltips',
                         'item_tooltips', 'hat_tooltips', 'leaderboard_tooltips']:
                (english / 'Strings' / (name + '.txt')).write_text('')
            (output / 'tools').mkdir(parents=True)
            for enabled, status, stale in [(True, 'generated', False), (True, 'failed', False),
                                           (False, 'generated', False), (True, 'generated', True)]:
                with self.subTest(enabled=enabled, status=status, stale=stale):
                    source = ('{{codeexample\n' + json.dumps({'show_image': False, 'show_output': enabled})
                              + '\n#CODE\nprint(5)\n}}')
                    (english / 'docs/test.md').write_text(source)
                    entry = collect(source, 'guides/test.md')[0]
                    recorded = dict(entry, status=status)
                    if status == 'generated':
                        recorded.update(output='5', completed=True)
                    if stale:
                        recorded['source_hash'] = 'old'
                    report = {'sources': {}, 'tools': {}, 'examples': [recorded]}
                    (output / 'tools/example_media.json').write_text(json.dumps(report))
                    exporter = Exporter(game, output)
                    exporter.prepare([])
                    self.assertEqual(bool(exporter.outputs), enabled and status == 'generated' and not stale)


@unittest.skipUnless(os.environ.get('TFWR_GAME_DIR'), 'Set TFWR_GAME_DIR for offline game checks')
class GameTests(unittest.TestCase):
    root = Path(__file__).resolve().parent.parent

    def run_example(self, example):
        game = Path(os.environ['TFWR_GAME_DIR'])
        dotnet = os.environ.get('TFWR_DOTNET', 'dotnet')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'request.json'
            path.write_text(json.dumps(example))
            result = subprocess.run([
                dotnet, str(self.root / '.media-cache/bridge/TfwrBridge.dll'), 'run',
                str(game / 'TheFarmerWasReplaced_Data/Managed'),
                str(self.root / '.media-cache/assets/resources.json'), str(path)],
                capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)

    def source(self, page, ordinal=1):
        path = Path(os.environ['TFWR_GAME_DIR']) / 'TheFarmerWasReplaced_Data/StreamingAssets/Languages/EN/docs' / page
        return collect(path.read_text(encoding='utf-8-sig'), 'guides/' + page)[ordinal - 1]

    def test_harvest_program_and_seeded_replay(self):
        example = self.source('first_program.md')
        first = self.run_example(example)
        self.assertTrue(first['completed'])
        self.assertEqual(first['frames'][-1]['inventory']['hay'], 2)
        self.assertEqual(first, self.run_example(example))

    def test_resource_scalars_match_the_independent_binary_reader(self):
        from packaged_assets import extract

        assets = json.loads((self.root / '.media-cache/assets/resources.json').read_text())
        by_id = {entry['id']: entry['data'] for entry in assets}
        with tempfile.TemporaryDirectory() as directory:
            records, _, _ = extract(Path(os.environ['TFWR_GAME_DIR']), Path(directory), set())
        for record in records:
            for key, value in record['values'].items():
                if isinstance(value, (str, int, float, bool)):
                    with self.subTest(record=record['name'], field=key):
                        self.assertEqual(by_id[record['path_id']][key], value)

    def test_farming_setup_movement_and_growth(self):
        example = self.source('unlocks/bamboo.md')
        result = self.run_example(example)
        self.assertTrue(result['completed'])
        self.assertTrue(any(tile['entity'] == 'bamboo' for frame in result['frames'] for tile in frame['tiles']))
        self.assertNotEqual(result['frames'][0]['drones'][0]['position'], result['frames'][-1]['drones'][0]['position'])

    def test_mining_yield_depth_and_reset(self):
        result = self.run_example(self.source('unlocks/mining.md'))
        self.assertTrue(result['completed'])
        self.assertEqual(result['frames'][-1]['inventory']['block'], 3)
        self.assertTrue(any(tile['depth'] >= 3 for frame in result['frames'] for tile in frame['tiles']))
        self.assertTrue(all(tile['depth'] == 0 for tile in result['frames'][-1]['tiles']))

    def test_cloned_mushroom_grounds_can_be_dug(self):
        result = self.run_example(self.source('unlocks/mushroom.md', 2))
        self.assertTrue(result['frames'])
        self.assertTrue(any(tile['ground'] == 'mushroom' for frame in result['frames'] for tile in frame['tiles']))

    @unittest.skipUnless(importlib.util.find_spec('pyrender'), 'Optional renderer packages are not installed')
    def test_zero_scale_growth_meshes_render(self):
        from media_renderer import Renderer
        import numpy as np

        example = self.source('unlocks/bamboo.md', 2)
        result = self.run_example(example)
        frame = next(frame for frame in result['frames'] if any(
            np.any(np.linalg.norm(np.asarray(mesh['matrix']).reshape(4, 4)[:3, :3], axis=0) < 1e-9)
            for mesh in frame['meshes']))
        renderer = Renderer(self.root / '.media-cache/assets', example['config'])
        try:
            self.assertEqual(renderer.render(frame).size, (800, 500))
        finally:
            renderer.close()

    def test_endless_loop_is_limited(self):
        example = self.source('first_program.md')
        example['setup'] = ''
        example['code'] = 'while True:\n\tdo_a_flip()'
        result = self.run_example(example)
        self.assertFalse(result['completed'])
        self.assertEqual(len(result['frames']), 450)

    def test_output_comes_from_the_interpreter(self):
        example = self.source('first_program.md')
        example['setup'] = ''
        example['code'] = 'print(2 + 3)'
        result = self.run_example(example)
        self.assertIn('5', result['frames'][-1]['output'])
        self.assertEqual(result['output'], result['frames'][-1]['output'])

    def test_output_only_result_and_silent_example(self):
        result = self.run_example(self.source('scripting/operators.md'))
        self.assertTrue(result['completed'])
        self.assertEqual(plain_output(result['output']), '5')
        self.assertEqual(result['frames'], [])
        silent = self.run_example(self.source('scripting/functions.md'))
        self.assertTrue(silent['completed'])
        self.assertEqual(silent['output'], '')

    def test_tutorial_runtime_error_has_native_diagnostic_and_carets(self):
        result = self.run_example(self.source('scripting/functions.md', 3))
        self.assertTrue(result['completed'])
        text = plain_output(result['output'])
        self.assertIn('Error: func has never been defined.', text)
        self.assertIn('func()\n^^^^^', text)
        self.assertEqual(result['frames'], [])

    def test_parse_error_is_captured_as_output(self):
        example = self.source('scripting/functions.md', 3)
        example['code'] = 'if True\n\tpass'
        result = self.run_example(example)
        self.assertTrue(result['completed'])
        self.assertIn('Error:', result['output'])
        self.assertIn('colon', plain_output(result['output']))
        self.assertIn('^', result['output'])

    def test_output_only_loop_keeps_partial_output_at_limit(self):
        example = self.source('scripting/functions.md', 3)
        example['code'] = 'print("started")\nwhile True:\n\tpass'
        result = self.run_example(example)
        self.assertFalse(result['completed'])
        self.assertIn('started', result['output'])
        self.assertEqual(result['frames'], [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
