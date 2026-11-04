"""Generate offline GIFs for the installed game's visual documentation examples."""

import argparse
from collections import Counter
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from code_examples import collect
from media_assets import extract_media, verify_game


ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    temporary.replace(path)


def command(args, **kwargs):
    result = subprocess.run(args, capture_output=True, text=True, timeout=180, **kwargs)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout


def build_bridge(dotnet, managed, cache):
    env = dict(os.environ, DOTNET_CLI_TELEMETRY_OPTOUT='1', DOTNET_NOLOGO='1',
               DOTNET_CLI_HOME=str(cache / 'dotnet-home'), NUGET_PACKAGES=str(cache / 'nuget'))
    host = cache / 'bridge'
    host.mkdir(parents=True, exist_ok=True)
    command([dotnet, 'build', str(ROOT / 'game_bridge/Bridge.csproj'), '--nologo',
             '--output', str(host), '-p:GameManaged=' + str(managed),
             '-p:BaseIntermediateOutputPath=' + str(cache / 'obj') + os.sep], env=env)
    command([dotnet, str(host / 'TfwrBridge.dll'), 'prepare', str(managed),
             str(host / 'UnityEngine.CoreModule.offline')], env=env)
    for name in ['UnityEngine.CoreModule', 'Core']:
        (host / (name + '.offline')).replace(host / (name + '.dll'))
    return host / 'TfwrBridge.dll'


def inspect_gif(path):
    from PIL import Image

    with Image.open(path) as image:
        if image.format != 'GIF' or image.info.get('loop') != 0:
            raise ValueError('Expected a looping GIF')
        size, duration = image.size, 0
        for i in range(image.n_frames):
            image.seek(i)
            image.load()
            duration += image.info.get('duration', 0)
        if not 0 < duration <= 15050:
            raise ValueError('GIF duration is outside the recording limit')
        return {'width': size[0], 'height': size[1], 'duration': duration / 1000,
                'sha256': digest(path)}


def encode(frames, config, assets, target):
    from media_renderer import Renderer

    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=target.parent) as directory:
        temporary = Path(directory) / 'example.gif'
        renderer = Renderer(assets, config)
        try:
            with tempfile.TemporaryFile() as errors:
                process = subprocess.Popen([
                    'ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', '15',
                    '-i', 'pipe:0', '-filter_complex_threads', '1', '-filter_complex',
                    'split[a][b];[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer:bayer_scale=3',
                    '-loop', '0', str(temporary)], stdin=subprocess.PIPE, stderr=errors)
                try:
                    for frame in frames:
                        renderer.render(frame).save(process.stdin, format='PNG')
                    process.stdin.close()
                    if process.wait(timeout=60):
                        errors.seek(0)
                        raise RuntimeError(errors.read().decode())
                finally:
                    if process.poll() is None:
                        process.kill()
                        process.wait()
        finally:
            renderer.close()
        details = inspect_gif(temporary)
        if (details['width'], details['height']) != (
                config.get('image_size', {'x': 500})['x'], config.get('image_size', {'y': 300})['y']):
            raise ValueError('GIF dimensions do not match the example')
        temporary.replace(target)
        return details


def generate(game, output, dotnet):
    game, output = game.resolve(), output.resolve()
    if output == game or output.is_relative_to(game):
        raise ValueError('Output must be outside the game installation')
    root, unity_version = verify_game(game)
    cache = output / '.media-cache'
    cache.mkdir(parents=True, exist_ok=True)
    sources = {name: digest(root / name) for name in [
        'Managed/Core.dll', 'Managed/Utils.dll', 'Managed/UnityEngine.CoreModule.dll',
        'resources.assets', 'resources.assets.resS', 'globalgamemanagers.assets',
        'level0', 'sharedassets0.assets', 'sharedassets0.assets.resS']}
    tools = {path.relative_to(ROOT).as_posix(): digest(path) for path in [
        ROOT / 'code_examples.py', ROOT / 'generate_examples.py', ROOT / 'media_assets.py',
        ROOT / 'media_renderer.py', ROOT / 'requirements-media.txt',
        ROOT / 'layouts.json',
        ROOT / 'game_bridge/Bridge.csproj', ROOT / 'game_bridge/Program.cs']}
    packages = {name: version(name) for name in ['UnityPy', 'TypeTreeGeneratorAPI',
                                                'numpy', 'Pillow', 'pyrender']}
    inputs = {'sources': sources, 'tools': tools, 'packages': packages}
    stamp = cache / 'inputs.json'
    if not stamp.exists() or json.loads(stamp.read_text()) != inputs:
        print('Extracting simulator resources and original models...', flush=True)
        extract_media(game, cache / 'assets')
        print('Building the offline bridge...', flush=True)
        build_bridge(dotnet, root / 'Managed', cache)
        save_json(stamp, inputs)
    bridge = cache / 'bridge/TfwrBridge.dll'
    guides = root / 'StreamingAssets/Languages/EN/docs'
    candidates = [example for path in sorted(guides.rglob('*.md'))
                  for example in collect(path.read_text(encoding='utf-8-sig'),
                                         'guides/' + path.relative_to(guides).as_posix())
                  if example['config'].get('show_image', True)]
    report_path = output / 'tools/example_media.json'
    previous = json.loads(report_path.read_text()) if report_path.exists() else {'examples': []}
    old = {example['id']: example for example in previous['examples']}
    report = {'unity_version': unity_version, 'backend': 'managed-game-core',
              'fps': 15, 'maximum_duration': 15, **inputs, 'examples': []}
    for index, example in enumerate(candidates, 1):
        entry = {key: example[key] for key in ['id', 'page', 'ordinal', 'source_hash', 'gif']}
        entry['input_hash'] = fingerprint({'source': example['source_hash'], **inputs})
        prior = old.get(example['id'], {})
        target = output / example['gif']
        if (prior.get('status') == 'generated' and prior.get('input_hash') == entry['input_hash']
                and target.is_file() and digest(target) == prior.get('sha256')):
            entry = prior
        else:
            try:
                request = cache / 'request.json'
                save_json(request, example)
                result = json.loads(command([dotnet, str(bridge), 'run', str(root / 'Managed'),
                                             str(cache / 'assets/resources.json'), str(request)]))
                entry.update(encode(result['frames'], example['config'], cache / 'assets', target))
                entry.update(status='generated', seed=result['seed'], completed=result['completed'])
            except Exception as error:
                reason = str(error).splitlines()[0] or type(error).__name__
                method = re.search(r'^\s+at ([^\s(]+)\(', str(error), re.M)
                if method:
                    reason += ' (' + method[1] + ')'
                if isinstance(error, subprocess.TimeoutExpired):
                    reason = 'Simulator exceeded the 180-second wall-clock limit'
                # Keep machine-specific paths out of the public coverage report.
                reason = reason.replace(str(game), '<game>').replace(str(output), '<output>')
                entry.update(status='unsupported' if 'NotSupportedException' in reason
                             or 'SecurityException' in reason else 'failed', reason=reason[:300])
        report['examples'].append(entry)
        save_json(report_path, report)
        print(f'[{index}/{len(candidates)}] {example["id"]}: {entry["status"]}'
              + (': ' + entry['reason'] if 'reason' in entry else ''), flush=True)
    command([sys.executable, str(ROOT / 'export_docs.py'), '--game-dir', str(game), '--output', str(output)])
    print(json.dumps(dict(Counter(entry['status'] for entry in report['examples'])), indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT.parent)
    parser.add_argument('--dotnet', default='dotnet', help='Path to a .NET 8 SDK dotnet executable')
    args = parser.parse_args()
    if not shutil.which(args.dotnet) or not shutil.which('ffmpeg'):
        parser.error('The .NET 8 SDK and FFmpeg must be available')
    generate(args.game_dir, args.output, args.dotnet)


if __name__ == '__main__':
    main()
