"""Shared, dependency-free parsing and identity for the game's example blocks."""

import hashlib
import json
import re
from pathlib import Path


BLOCKS = re.compile(r'\{\{codeexample[ \t]*\n(.*?)^\}\}[ \t]*(?=$|<)', re.M | re.S)


def parse_block(block):
    block = block.lstrip()
    config, end = json.JSONDecoder().raw_decode(block)
    if not isinstance(config, dict):
        raise ValueError('Interactive example settings must be an object')
    remainder = block[end:].strip('\n')
    sections = re.split(r'^#CODE[ \t]*(?:\n|$)', remainder, maxsplit=1, flags=re.M)
    if len(sections) != 2:
        raise ValueError('Interactive example is missing #CODE')
    setup, code = sections
    setup = re.sub(r'^#SETUP[ \t]*\n?', '', setup).strip('\n')
    return {'config': config, 'setup': setup, 'code': code.strip('\n')}


def identify(example, page, ordinal):
    payload = json.dumps(example, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
    stem = page.removeprefix('guides/').removesuffix('.md')
    return dict(example, id=f'{page}:{ordinal}', page=page, ordinal=ordinal,
                source_hash=hashlib.sha256(payload.encode()).hexdigest(),
                gif=f'assets/examples/{stem}-{ordinal:02}.gif')


def collect(text, page):
    result = [identify(parse_block(m[1]), page, i)
              for i, m in enumerate(BLOCKS.finditer(text), 1)]
    if '{{codeexample' in BLOCKS.sub('', text):
        raise ValueError('Unconverted interactive example')
    return result


def recordings(output, examples, game):
    report_path = output / 'tools/example_media.json'
    if not report_path.exists():
        return {}
    report = json.loads(report_path.read_text(encoding='utf-8'))
    roots = [('sources', game / 'TheFarmerWasReplaced_Data'),
             ('tools', Path(__file__).resolve().parent)]
    for category, root in roots:
        for name, expected in report[category].items():
            path = (root / name).resolve()
            if not path.is_relative_to(root.resolve()):
                raise ValueError('Unsafe media provenance path')
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                return {}
    by_id = {example['id']: example for example in examples}
    result = {}
    for entry in report['examples']:
        example = by_id.get(entry['id'])
        if example is None or entry['source_hash'] != example['source_hash']:
            continue
        result[example['id']] = entry
    return result


def animations(output, examples, game):
    result = {}
    by_id = {example['id']: example for example in examples}
    for entry in recordings(output, examples, game).values():
        example = by_id[entry['id']]
        if entry['status'] != 'generated' or not example['config'].get('show_image', True):
            continue
        if entry['gif'] != example['gif']:
            raise ValueError('Animation path does not match its example')
        path = (output / entry['gif']).resolve()
        if not path.is_relative_to(output.resolve()):
            raise ValueError('Unsafe animation path')
        if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']:
            result[example['id']] = entry
    return result


def plain_output(text):
    return re.sub(r'<noparse>(.*?)(?:</noparse>|$)|</?(?:font|color|b|i|size)(?:=[^>]+)?>',
                  lambda match: match[1] if match[1] is not None else '', text, flags=re.S)
