"""Export the installed English documentation; Python 3.10+, standard library only."""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit

from packaged_assets import extract
from code_examples import BLOCKS, animations, collect, identify, parse_block


STRING_FILES = ('code_tooltips', 'unlock_tooltips', 'object_tooltips',
                'item_tooltips', 'hat_tooltips', 'leaderboard_tooltips')
IMAGE_NAMES = {'PlayButton', 'Breakpoints', 'ImportsInOnePicture',
               'LeaderboardSetup', 'UndergroundLeaderboardSetup'}
IMAGE_LABELS = {'PlayButton': 'The editor play and pause buttons',
                'Breakpoints': 'Setting a breakpoint in the editor',
                'ImportsInOnePicture': 'Two modules sharing a variable through an import',
                'LeaderboardSetup': 'Leaderboard simulation setup',
                'UndergroundLeaderboardSetup': 'Underground leaderboard simulation setup'}
LINK = re.compile(r'(!?)\[([^\]]*)\]\(([^)]+)\)')
FENCES = re.compile(r'(^```[^\n]*\n.*?^```[ \t]*$)', re.M | re.S)


def entries(text):
    matches = list(re.finditer(r'^@([\w]+)\s*=[ \t]*', text, re.M))
    result = {}
    for i, match in enumerate(matches):
        key = match[1]
        if key in result:
            raise ValueError(f'Duplicate source key: {key}')
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result[key] = text[match.end():end].strip()
    return result


def outside_fences(text, transform):
    return ''.join(part if i % 2 else transform(part)
                   for i, part in enumerate(FENCES.split(text)))


def fenced(text, language='python'):
    if '```' in text:
        raise ValueError('Unexpected nested fence in source example')
    return f'\n```{language}\n{text.strip(chr(10))}\n```\n'


def multiline_code(text):
    return outside_fences(text, lambda part: re.sub(
        r'(?<!`)`([^`]+)`(?!`)', lambda m: fenced(m[1]) if '\n' in m[1] else m[0], part))


def generic_data_locations(text):
    return re.sub(
        r'(?m)^The persistent data folder is located at:\n(?:[ \t]*\n|-[^\n]*(?:\n|$))+',
        'The persistent data directory is written as `<game-data>/` in this reference.\n'
        'Its actual location depends on the platform and launcher.\n\n', text)


def examples(text, animations=None):
    count = 0
    def convert(match):
        nonlocal count
        count += 1
        example = parse_block(match[1])
        config, setup, code = (example[key] for key in ('config', 'setup', 'code'))
        relevant = {key: value for key, value in config.items()
                    if key not in {'camera_position', 'show_image', 'image_size', 'show_code',
                                   'show_inventory', 'show_output', 'collapsing', 'autoplay'}}
        result = '\n'
        if relevant:
            result += '**Example conditions**\n' + fenced(
                json.dumps(relevant, ensure_ascii=False, indent=2), 'json') + '\n'
        if setup.strip():
            result += '**Example setup**\n' + fenced(setup) + '\n'
        result += '**Example code**\n' + fenced(code) + '\n'
        if animations and count in animations:
            result += ('<details>\n<summary>Animated example</summary>\n\n'
                       f'![Animated example {count}]({animations[count]})\n\n'
                       '*Offline recreation using extracted game models; simplified visuals. '
                       'Clips are limited to 15 seconds.*\n\n'
                       '</details>\n')
        return result
    result = BLOCKS.sub(convert, text)
    if '{{codeexample' in result:
        raise ValueError('Unconverted interactive example')
    return result, count


def title(name):
    return name.replace('_', ' ').title()


def number(value):
    if isinstance(value, bool):
        return 'Yes' if value else 'No'
    return f'{value:,.8g}'


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def table(rows):
    return '\n| Property | Stored value |\n| --- | --- |\n' + ''.join(
        f'| {cell(key)} | {cell(value)} |\n' for key, value in rows) + '\n'


def item_block(block):
    values = block['serializeList']
    return ', '.join(f"{number(item['nr'])} × {title(item['name'])}" for item in values) or 'None'


class Exporter:
    def __init__(self, game, output):
        self.game = game.resolve()
        self.output = output.resolve()
        self.source = self.game / 'TheFarmerWasReplaced_Data/StreamingAssets/Languages/EN'
        if not self.source.is_dir():
            raise ValueError('The game directory does not contain the English documentation')
        if self.output == self.game or self.output.is_relative_to(self.game / 'TheFarmerWasReplaced_Data'):
            raise ValueError('Output must be separate from the installed game data')
        self.strings = {name: entries((self.source / 'Strings' / (name + '.txt')).read_text(
            encoding='utf-8-sig')) for name in STRING_FILES}
        self.all_strings = {key: value for group in self.strings.values() for key, value in group.items()}
        self.coverage = defaultdict(list)
        self.pages = {}
        self.routes = {}
        self.gaps = []
        self.example_count = 0
        self.examples = []
        self.animation_paths = set()
        self.animations = {}

    def source_entry(self, key, page):
        if key not in self.all_strings:
            raise KeyError(key)
        if page not in self.coverage[key]:
            self.coverage[key].append(page)
        return self.all_strings[key]

    def add_page(self, path, text):
        if path in self.pages or not re.fullmatch(r'[A-Za-z0-9_./-]+\.md', path):
            raise ValueError(f'Duplicate or unsafe output page: {path}')
        self.pages[path] = text.strip() + '\n'

    def reference_page(self, record):
        category, name, values = record['category'], record['name'], record['values']
        page = f'{category}/{name}.md'
        heading = self.all_strings.get(name, title(name)) if category == 'unlocks' else title(name)
        if category == 'unlocks' and name in self.all_strings:
            self.source_entry(name, page)
        text = f'# {heading}\n\n'
        if values.get('dlc'):
            text += '> Underground/DLC content.\n\n'
        if values.get('hidden'):
            text += '> Hidden in the game’s normal selection interface.\n\n'
        if values.get('enabled') is False:
            text += '> Disabled in the packaged game data.\n\n'
        key = values.get('description')
        if category == 'hats':
            key = 'hat_descr_' + name
        if category == 'leaderboards':
            key = 'lb_descr_' + name
        if key and key in self.all_strings:
            text += self.source_entry(key, page) + '\n\n'
        else:
            note = f'{category}/{name}: no description is present in the selected English text resources.'
            self.gaps.append(note)
            text += '*No English description is packaged for this entry.*\n\n'
        if values.get('multiUnlockDescr') in self.all_strings:
            text += '## Upgrade description\n\n' + self.source_entry(values['multiUnlockDescr'], page) + '\n\n'
        if values.get('docs'):
            text += f"[Related guide]({values['docs']})\n\n"
        text += self.properties(category, values)
        text += ('\n> These are stored base settings. Actual costs, growth, yields, hardness, and other '
                 'behavior can depend on upgrades, depth, neighbors, or controller logic. '
                 'Stored upgrade lists and factors are exported without inventing a runtime formula.\n')
        text += f"\nSource: `resources.assets`, object `{record['path_id']}` (`{record['class']}`).\n"
        self.add_page(page, text)

    def properties(self, category, v):
        labels = {
            'objects': [('className', 'Behavior controller'), ('canBePlanted', 'Plantable'),
                        ('canBeOverplanted', 'Can be planted over'), ('canBeSwapped', 'Swappable'),
                        ('canHaveCompanion', 'Can have a companion'), ('canBeWeird', 'Can be infected'),
                        ('meanGrowTime', 'Mean base growth time (seconds)'),
                        ('growTimeDeviationPercent', 'Stored growth deviation fraction'),
                        ('dropItem', 'Base drop item'), ('dropAmount', 'Stored base drop amount'),
                        ('yieldUpgradeName', 'Yield upgrade')],
            'grounds': [('maxHardness', 'Stored maximum hardness'), ('stability', 'Stability'),
                        ('allowedToPlaceManually', 'Manually placeable'), ('isTillable', 'Tillable'),
                        ('isPushable', 'Pushable'), ('autodestroyWhenDugBeside', 'Destroyed when dug beside'),
                        ('yieldMultiplierForGrowables', 'Stored growable yield multiplier'),
                        ('dropItem', 'Base drop item'), ('dropAmount', 'Stored base drop amount'),
                        ('yieldUpgradeName', 'Yield upgrade'), ('controller', 'Behavior controller')],
            'hats': [('className', 'Behavior controller'), ('isGolden', 'Golden'),
                     ('preventWrapping', 'Prevents wrapping'), ('preventHover', 'Prevents hovering'),
                     ('rotateDroneToMove', 'Turns drone to face movement'), ('droneFlyHeight', 'Drone flight height')],
            'items': [('enabled', 'Enabled'), ('trackStats', 'Tracks rate statistics'),
                      ('trackTotalStats', 'Tracks total statistics')],
            'unlocks': [('parentUnlock', 'Parent unlock'), ('maxUnlockLevel', 'Stored maximum level'),
                        ('unlockedHat', 'Unlocked hat'), ('multiUnlockFactor', 'Stored upgrade cost factor'),
                        ('additivePercentStart', 'Stored additive percent start'),
                        ('additivePercentFactor', 'Stored additive percent factor'), ('enabled', 'Enabled')],
            'leaderboards': [('singleDrone', 'Single drone'), ('everythingUnlocked', 'Starts with everything unlocked'),
                             ('fullyGenerateUnderground', 'Fully generates underground')],
        }
        rows = []
        for key, label in labels[category]:
            if key in v and v[key] != '':
                val = number(v[key]) if isinstance(v[key], (int, float)) else f'`{v[key]}`'
                rows.append((label, val))
        if 'cost' in v:
            rows.append(('Stored base planting cost', item_block(v['cost'])))
        if 'placeableOn' in v:
            rows.append(('Can be planted on', ', '.join(title(x) for x in v['placeableOn']) or 'None'))
        if 'unlockCost' in v:
            rows.append(('Initial unlock cost', item_block(v['unlockCost'])))
            rows.extend((f'Stored upgrade cost {i + 1}', item_block(block))
                        for i, block in enumerate(v['multiUnlockCost']))
            req = v['additionalUnlockRequirement']
            if req['unlockName']:
                rows.append(('Additional requirement', f"{title(req['unlockName'])}, level {req['level']} or higher"))
            if v['unlocks']:
                rows.append(('Unlocks', ', '.join(f'`{x}`' for x in v['unlocks'])))
        if 'goalItems' in v:
            rows.extend([('Starting items', item_block(v['startItems'])), ('Goal items', item_block(v['goalItems']))])
        return '## Packaged gameplay settings\n' + table(rows)

    def prepare(self, records):
        guides = sorted((self.source / 'docs').rglob('*.md'))
        for source in guides:
            relative = source.relative_to(self.source).as_posix()
            destination = 'guides/' + source.relative_to(self.source / 'docs').as_posix()
            self.routes[relative] = destination
            self.examples.extend(collect(source.read_text(encoding='utf-8-sig'), destination))
        self.animations = animations(self.output, self.examples, self.game)
        self.animation_paths = {entry['gif'] for entry in self.animations.values()}
        for record in records:
            route = f"{record['category']}/{record['name']}"
            self.routes[route] = route + '.md'
            self.reference_page(record)
        for key in self.strings['code_tooltips']:
            name = key.removeprefix('code_tooltip_')
            page = f'code/{name}.md'
            self.routes['functions/' + name] = page
            self.add_page(page, f'# `{name}`\n\n' + self.source_entry(key, page)
                          + f'\n\nSource: `EN/Strings/code_tooltips.txt`, `{key}`.\n')
        # Retain descriptions for removed entries that have no packaged object anymore.
        for filename, prefix, category in [('item_tooltips', 'item_descr_', 'items'),
                                           ('object_tooltips', 'object_descr_', 'objects'),
                                           ('hat_tooltips', 'hat_descr_', 'hats'),
                                           ('unlock_tooltips', 'unlock_descr_', 'unlocks')]:
            for key in self.strings[filename]:
                if key.startswith(prefix) and key not in self.coverage:
                    name = key.removeprefix(prefix)
                    page = f'{category}/{name}.md'
                    if page in self.pages:
                        self.pages[page] += '\n## Additional source description\n\n' + self.source_entry(key, page) + '\n'
                    else:
                        self.add_page(page, f'# {title(name)}\n\n' + self.source_entry(key, page)
                                      + f'\n\nSource: `EN/Strings/{filename}.txt`, `{key}`. '
                                      'No separate matching asset was found.\n')
                        self.routes[f'{category}/{name}'] = page
        for source in guides:
            raw = source.read_text(encoding='utf-8-sig')
            path = self.routes[source.relative_to(self.source).as_posix()]
            media = {entry['ordinal']: entry['gif'] for entry in self.animations.values()
                     if entry['page'] == path}
            text, count = examples(generic_data_locations(raw), media)
            self.example_count += count
            self.add_page(path, text + f'\n\nSource: `EN/{source.relative_to(self.source).as_posix()}`.\n')
        templates = '# Tooltip templates and localized labels\n\n'
        templates += ('These supplementary source entries include labels and templates filled by the game. '
                      'Numbered placeholders are arguments; inventory, rates, costs, and requirements '
                      'are supplied at runtime. Literal templates are retained below.\n\n')
        for group in self.strings.values():
            for key in group:
                if key not in self.coverage:
                    templates += f'## {key}\n' + fenced(self.source_entry(key, 'reference/templates.md'), 'text') + '\n'
        self.add_page('reference/templates.md', templates)
        self.add_page('reference/gaps.md', '# Extraction limits and missing descriptions\n\n'
                      + '\n'.join('- ' + gap for gap in sorted(self.gaps))
                      + '\n\n- Live output, personal statistics, and live item blocks require a running game.\n'
                      '- Examples retain their code and starting conditions. Optional offline GIFs use '
                      'the game interpreter and extracted models with simplified visuals. '
                      'Unsupported examples are listed in `tools/example_media.json` when media has been generated.\n'
                      '- Standalone meshes, sounds, and unrelated artwork are excluded; '
                      'optional GIFs render extracted geometry.\n'
                      '- Static base settings do not reconstruct controller-specific or upgrade formulas.\n'
                      '- The exporter checks assembly hashes and Unity version to reject unsupported builds.\n')
        return guides

    def rewrite(self, text, page):
        def convert_link(match):
            image, label, target = match.groups()
            if urlsplit(target).scheme or target.startswith('#'):
                return match[0]
            if target.startswith('persistent_data_path/'):
                suffix = target.partition('/')[2]
                if suffix in {'Saves', 'Backup'}:
                    suffix += '/'
                return label + ' (`<game-data>/' + suffix + '`)'
            if image:
                if target in getattr(self, 'animation_paths', set()):
                    destination = target
                elif target in IMAGE_NAMES:
                    destination = f'assets/{target}.png'
                    label = IMAGE_LABELS[target]
                else:
                    raise ValueError(f'Unknown game image: {target}')
            elif target in self.routes:
                destination = self.routes[target]
            else:
                raise ValueError(f'Unresolved game link in {page}: {target}')
            relative = Path(os.path.relpath(destination, str(Path(page).parent))).as_posix()
            return f'{image}[{label}]({relative})'
        def transform(part):
            part = re.sub(r'\{\{@([\w]+)\}\}', lambda m: self.all_strings[m[1]], part)
            part = re.sub(r'<spoiler=([^>]+)>', lambda m: '\n\n**' + m[1].strip().capitalize() + '**\n\n', part)
            part = part.replace('</spoiler>', '\n\n')
            part = re.sub(r'</?(?:unlock(?:=[^>]+)?|dlc)>', '', part)
            part = re.sub(r'<columns>(.*?)</columns>', lambda m: '\n\n' + '\n'.join(
                '- ' + line.strip() for line in m[1].splitlines() if line.strip()) + '\n\n',
                part, flags=re.S)
            part = part.replace('<right>', ' | ')
            part = part.replace('{{output}}', '*Live output is available only in the running game.*')
            part = re.sub(r'\{\{itemblock ([^}]+)\}\}',
                          '*Live resource statistics are available only in the running game.*', part)
            return LINK.sub(convert_link, part)
        return outside_fences(multiline_code(text), transform)

    def write(self, guides, records, images, version):
        self.output.mkdir(parents=True, exist_ok=True)
        for category in ['code', 'unlocks', 'objects', 'grounds', 'items', 'hats', 'leaderboards']:
            pages = sorted(p for p in self.pages if p.startswith(category + '/'))
            self.add_page(category + '/index.md', '# ' + title(category) + '\n\n'
                          + '\n'.join(f'- [{Path(p).stem}](EXPORT:{p})' for p in pages))
        for page, text in list(self.pages.items()):
            if '/index.md' not in page:
                text = self.rewrite(text, page)
            else:
                text = text.replace('EXPORT:' + page.partition('/')[0] + '/', '')
            if not re.search(r'^# ', text, re.M):
                text = '# ' + title(Path(page).stem) + '\n\n' + text
            def spacing(part):
                part = re.sub(r'(?m)^(#{1,6} [^\n]+)\n(?=[^\n])', r'\1\n\n', part)
                part = re.sub(r'(?m)^---[ \t]*$', '\n---\n', part)
                return re.sub(r'\n{3,}', '\n\n', part)
            text = outside_fences(text, spacing).strip() + '\n'
            text = '[Documentation index](' + Path(os.path.relpath('README.md', str(Path(page).parent))).as_posix() + ')\n\n' + text
            self.pages[page] = text
        counts = Counter(record['category'] for record in records)
        readme = f'''# The Farmer Was Replaced — English Documentation

Complete installed English guides and gameplay reference, including Underground/DLC content.

- [In-game documentation home](guides/home.md)
- [Getting started](guides/getting_started.md)
- [Code reference](code/index.md)
- [Unlocks and upgrades](unlocks/index.md)
- [Entities](objects/index.md)
- [Grounds](grounds/index.md)
- [Items](items/index.md)
- [Hats](hats/index.md)
- [Leaderboards](leaderboards/index.md)
- [Supplementary templates and labels](reference/templates.md)
- [Extraction limits and missing descriptions](reference/gaps.md)
- [Exporter maintenance and validation](tools/README.md)

## Coverage

{len(guides)} guide pages; {len(self.strings['code_tooltips'])} code reference entries;
{sum(len(group) for group in self.strings.values())} source text entries;
{self.example_count} interactive examples converted to code and starting conditions;
{len(self.animations)} offline example GIFs;
{len(records)} packaged gameplay records; {len(images)} extracted illustrations.

Packaged records: {', '.join(f'{n} {category}' for category, n in sorted(counts.items()))}.

## Reading the reference

All unlock-gated content and hints are visible. Examples use the game's Python-like language.
Example conditions preserve gameplay configuration. Complete source examples, including visual
settings, are retained in the extraction manifest. Optional GIFs execute the game's interpreter
offline and render extracted models with simplified lighting and effects. Expand **Animated
example** beneath supported examples to view them. Clips show at most 15 seconds of execution.
Code and conditions remain available for all examples.
Media coverage and unsupported examples are recorded in `tools/example_media.json` when generated.

Reference tables contain stored base values, not unconditional promises about gameplay.
Upgrades, neighbors, depth, and controller logic can change actual values. Upgrade cost arrays
and factors are listed as stored; this export does not derive their runtime formula.
Source wording, including outdated entries and apparent mistakes, is preserved.
Templates retain literal source syntax inside fenced text blocks.

## Logical paths

`<game-data>/` means the game's persistent data directory. Its actual location depends
on the platform and launcher; it is a logical placeholder, not a literal filesystem path.

- `<game-data>/Saves/`: saves and in-game code files.
- `<game-data>/Backup/`: saved backups.
- `<game-data>/output.txt`: complete execution output.

## Sources

Source references are relative to the game installation. Unity version: `{version}`.
The extraction manifest retains the UTC export timestamp, source hashes, and entry coverage.

UI labels, settings, errors, warnings, news, audio, and unrelated artwork are excluded.
Live farm output and personal statistics require a running game; GIF output comes from offline examples.
'''
        maintenance = Path(__file__).with_name('README.md').read_text(encoding='utf-8')
        readme += '\n## All guides\n\n' + '\n'.join(
            f'- [{source.stem.replace("_", " ")}](guides/{source.relative_to(self.source / "docs").as_posix()})'
            for source in guides) + '\n'
        self.pages['README.md'] = readme
        self.pages['tools/README.md'] = maintenance
        for page, text in self.pages.items():
            path = self.output / page
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
        source_files = list(guides) + [self.source / 'Strings' / (name + '.txt') for name in STRING_FILES]
        data_root = self.game / 'TheFarmerWasReplaced_Data'
        source_files += [data_root / name for name in ['resources.assets', 'resources.assets.resS',
                         'globalgamemanagers.assets', 'Managed/Core.dll', 'Managed/Utils.dll']]
        manifest = {'unity_version': version, 'created_utc': datetime.now(timezone.utc).isoformat(),
                    'guide_count': len(guides), 'example_count': self.example_count,
                    'examples': self.examples, 'animations': list(self.animations.values()),
                    'string_counts': {name: len(values) for name, values in self.strings.items()},
                    'record_counts': dict(counts), 'images': images, 'gaps': sorted(self.gaps),
                    'source_entries': dict(sorted(self.coverage.items())),
                    'sources': {path.relative_to(self.game).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in source_files},
                    'pages': sorted(self.pages)}
        tools = self.output / 'tools'
        tools.mkdir(exist_ok=True)
        script_root = Path(__file__).resolve().parent
        for name in ['export_docs.py', 'packaged_assets.py', 'layouts.json', 'test_export.py',
                     'requirements.txt', 'code_examples.py', 'generate_examples.py',
                     'media_assets.py', 'media_renderer.py', 'requirements-media.txt', 'test_media.py',
                     'game_bridge/Bridge.csproj', 'game_bridge/Program.cs']:
            if (tools / name).resolve() != (script_root / name).resolve():
                (tools / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(script_root / name, tools / name)
        (tools / 'extraction_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        return manifest


def validate(output):
    manifest = json.loads((output / 'tools/extraction_manifest.json').read_text(encoding='utf-8'))
    expected_entries = sum(manifest['string_counts'].values())
    if len(manifest['source_entries']) != expected_entries:
        raise ValueError('Source entry coverage is incomplete')
    links = 0
    for page in manifest['pages']:
        path = output / page
        text = path.read_text(encoding='utf-8')
        prose = ''.join(FENCES.split(text)[::2])
        if re.search(r'<(?:/?(?:unlock|dlc|columns|spoiler)|right)\b|\{\{', prose):
            raise ValueError(f'Unconverted game syntax in {page}')
        for match in LINK.finditer(prose):
            target = match[3]
            if urlsplit(target).scheme:
                continue
            route, _, fragment = target.partition('#')
            resolved = (path.parent / unquote(route)).resolve() if route else path.resolve()
            if not resolved.is_relative_to(output.resolve()) or not resolved.is_file():
                raise ValueError(f'Broken local link in {page}: {target}')
            if fragment:
                headings = re.findall(r'^#+\s+(.+)$', resolved.read_text(encoding='utf-8'), re.M)
                anchors = {re.sub(r'[^\w -]', '', heading.lower()).replace(' ', '-') for heading in headings}
                if fragment not in anchors:
                    raise ValueError(f'Broken anchor in {page}: {target}')
            links += 1
        if len(re.findall(r'^```', text, re.M)) % 2:
            raise ValueError(f'Unbalanced code fences in {page}')
    for key, pages in manifest['source_entries'].items():
        if not pages or any(page not in manifest['pages'] for page in pages):
            raise ValueError(f'Missing output for source entry {key}')
    for image in manifest['images']:
        raw = (output / 'assets' / (image['name'] + '.png')).read_bytes()
        if raw[:8] != b'\x89PNG\r\n\x1a\n' or len(raw) < 40:
            raise ValueError(f'Invalid illustration: {image["name"]}')
    if 'examples' in manifest:
        all_examples = {entry['id']: entry for entry in manifest['examples']}
        if len(all_examples) != manifest['example_count']:
            raise ValueError('Example coverage is incomplete or contains duplicate IDs')
        for entry in all_examples.values():
            source = {key: entry[key] for key in ('config', 'setup', 'code')}
            expected = identify(source, entry['page'], entry['ordinal'])
            if any(entry[key] != expected[key] for key in ('id', 'source_hash', 'gif')):
                raise ValueError('Invalid example identity or source hash')
        for animation in manifest.get('animations', []):
            entry = all_examples.get(animation['id'])
            if (entry is None or animation['source_hash'] != entry['source_hash']
                    or animation['gif'] != entry['gif'] or animation['status'] != 'generated'
                    or not entry['config'].get('show_image', True)):
                raise ValueError('Animation does not match a visual source example')
            path = (output / animation['gif']).resolve()
            if not path.is_relative_to(output.resolve()):
                raise ValueError('Unsafe animation path')
            raw = path.read_bytes()
            size = entry['config'].get('image_size', {'x': 500, 'y': 300})
            if (raw[:6] not in (b'GIF87a', b'GIF89a') or len(raw) < 14 or raw[-1:] != b';'
                    or int.from_bytes(raw[6:8], 'little') != size['x']
                    or int.from_bytes(raw[8:10], 'little') != size['y']
                    or hashlib.sha256(raw).hexdigest() != animation['sha256']
                    or not 0 < animation['duration'] <= 15.05):
                raise ValueError(f'Invalid animation: {animation["id"]}')
    return {'pages': len(manifest['pages']), 'local_links': links,
            'source_entries': expected_entries, 'examples': manifest['example_count'],
            'animations': len(manifest.get('animations', [])),
            'images': len(manifest['images']), 'description_gaps': len(manifest['gaps'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game-dir', type=Path, help='Directory containing TheFarmerWasReplaced.exe')
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    if args.validate_only:
        print(json.dumps(validate(args.output), indent=2))
        return
    if args.game_dir is None:
        parser.error('--game-dir is required when exporting')
    exporter = Exporter(args.game_dir, args.output)
    records, images, version = extract(exporter.game, exporter.output, IMAGE_NAMES)
    guides = exporter.prepare(records)
    exporter.write(guides, records, images, version)
    print(json.dumps(validate(exporter.output), indent=2))


if __name__ == '__main__':
    main()
