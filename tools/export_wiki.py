"""Export canonical documentation into an explicitly owned empty offline directory."""
import argparse
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

HERD = Path('/Users/digital-hawk/Herd')
LINK = re.compile(r'(!?\[[^\]\n]*\]\()([^\s)]+)([^)]*\))')
CODE = re.compile(r'(```.*?```|~~~.*?~~~|`+[^`\n]*`+)', re.S)


def export_wiki(root: Path, output: Path) -> list[Path]:
    """Write a derived Wiki and linked local support without changing the package.

    The caller owns output by supplying an existing empty directory under Herd.
    Symlink paths and overlapping source/output trees are rejected before writes.
    """
    root = root.resolve(strict=True)
    output = output.absolute()
    if any(p.is_symlink() for p in (output, *output.parents)):
        raise ValueError('Output must not traverse symlinks')
    output = output.resolve(strict=True)
    if (not output.is_dir() or not output.is_relative_to(HERD) or
            output.is_relative_to(root) or root.is_relative_to(output) or any(output.iterdir())):
        raise ValueError('Output must be an explicitly owned empty directory under Herd, outside the source tree')
    version = json.loads((root / 'plugin.json').read_text())['version']
    commit = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'], check=True,
                            capture_output=True, text=True).stdout.strip()
    if not re.fullmatch(r'[a-f0-9]{40}', commit):
        raise ValueError('Cannot identify the actual source commit')
    selected = [root / 'docs/compatibility.md', root / 'docs/troubleshooting.md']
    for directory in ('skills', 'principles', 'setup', 'workflows', 'maintenance', 'guide', 'testing'):
        selected.extend(sorted((root / 'docs' / directory).glob('*.md')))
    leaves = [p for p in selected if p.parent == root / 'docs/skills' and p.name != 'README.md']
    if len(leaves) != 51 or sum(p.stem.startswith('principle-') for p in leaves) != 24:
        raise ValueError('Canonical catalog must contain 51 leaves and 24 principles')
    names = {}
    rendered = {}

    def register(path):
        relative = path.relative_to(root)
        if path.is_symlink() or any(p.is_symlink() for p in path.parents if p.is_relative_to(root)):
            raise ValueError(f'Symlink source: {relative}')
        name = '--'.join(relative.with_suffix('').parts) if path.suffix == '.md' else '--'.join(relative.parts)
        if name in names.values() and path not in names:
            raise ValueError(f'Wiki name collision: {relative}')
        names[path] = name
        return name

    pending = list(dict.fromkeys(selected))
    for path in pending:
        register(path)
    while pending:
        source = pending.pop(0)
        if source in rendered:
            continue
        if source.suffix != '.md':
            rendered[source] = source.read_bytes()
            continue
        def convert(match):
            target = match.group(2)
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith(('#', '//')):
                return match.group(0)
            path_text, separator, anchor = target.partition('#')
            candidate = (source.parent / unquote(path_text)).absolute()
            resolved = candidate.resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                if source in selected or not resolved.is_relative_to(root):
                    raise ValueError(f'Missing or unsafe documentation link: {source.relative_to(root)} -> {target}')
                return match.group(1)[match.group(1).find('[') + 1:-2] + f' (unresolved source support target: `{target}`)'
            # Check the lexical path as well as its resolved destination.
            if candidate.is_symlink() or any(p.is_symlink() for p in candidate.parents if p.is_relative_to(root)):
                raise ValueError(f'Symlink documentation link: {target}')
            if resolved.is_dir():
                name = register(resolved)
                entries = sorted(p for p in resolved.rglob("*") if p.is_file())
                lines = [f"# {resolved.name}", ""]
                for entry in entries:
                    lines.append(f"- [{entry.relative_to(resolved)}]({register(entry)})")
                    pending.append(entry)
                rendered[resolved] = ("\n".join(lines) + "\n").encode()
                return match.group(1) + name + match.group(3)
            name = register(resolved)
            if resolved not in rendered:
                pending.append(resolved)
            suffix = '.md' if match.group(1).startswith('!') and resolved.suffix == '.md' else ''
            return match.group(1) + name + suffix + (separator + anchor if separator else '') + match.group(3)
        tokens = re.compile(CODE.pattern + '|' + LINK.pattern, re.S)
        content = tokens.sub(lambda token: token.group(0) if token.group(1) is not None else convert(LINK.fullmatch(token.group(0))), source.read_text())
        rendered[source] = (content.rstrip() + f'\n\nSource: `{source.relative_to(root).as_posix()}`. Package version: `{version}`. Package commit: `{commit}`.\n').encode()
    home = ['# pstack documentation', '', f'Package version: `{version}`. Package commit: `{commit}`.', '',
            'This export is derived from the local canonical documentation. Structural export checks do not establish host support.', '']
    home += [f'- [{p.relative_to(root).as_posix()}]({names[p]})' for p in selected]
    payloads = {names[p] + ('.md' if p.suffix == '.md' or p.is_dir() else ''): data for p, data in rendered.items()}
    payloads['Home.md'] = ('\n'.join(home) + '\n').encode()
    written = []
    try:
        for name, data in sorted(payloads.items()):
            destination = output / name
            with destination.open('xb') as handle:
                written.append(destination)
                handle.write(data)
    except BaseException:
        # Remove only files this invocation created, never caller-owned contents.
        for destination in written:
            destination.unlink()
        raise
    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        paths = export_wiki(args.root, args.output)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        parser.error(str(error))
    print(f'Exported {len(paths)} files to {args.output.resolve()}')


if __name__ == '__main__':
    main()
