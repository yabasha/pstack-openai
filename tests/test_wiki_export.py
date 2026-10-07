"""Offline export checks against the actual canonical documentation."""
import hashlib
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.export_wiki import export_wiki

ROOT = Path(__file__).resolve().parents[1]
HERD = ROOT.parent


class WikiExportTests(unittest.TestCase):
    def fixture(self):
        context = tempfile.TemporaryDirectory(prefix='task23d-wiki-', dir=HERD)
        self.addCleanup(context.cleanup)
        return Path(context.name)

    def test_wiki_catalog_complete(self):
        output = self.fixture()
        pages = export_wiki(ROOT, output)
        leaves = list((ROOT / 'docs/skills').glob('*.md'))
        leaves = [p for p in leaves if p.name != 'README.md']
        self.assertEqual(len(leaves), 51)
        self.assertEqual(sum(p.stem.startswith('principle-') for p in leaves), 24)
        for source in leaves + [ROOT / 'docs/setup/chatgpt.md', ROOT / 'docs/setup/codex.md']:
            self.assertTrue(any(source.relative_to(ROOT).as_posix() in p.read_text() for p in pages if p.suffix == '.md'))
        home = (output / 'Home.md').read_text()
        self.assertIn('0.1.0', home)
        self.assertRegex(home, r'Package commit: `[a-f0-9]{40}`')

    def test_wiki_links_resolve(self):
        output = self.fixture()
        export_wiki(ROOT, output)
        for page in output.glob('*.md'):
            text = re.sub(r'```.*?```', '', page.read_text(), flags=re.S)
            text = re.sub(r'`[^`\n]+`', '', text)
            for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)', text):
                if ':' in target or target.startswith('#'):
                    continue
                path = target.split('#')[0]
                self.assertTrue((output / path).exists() or (output / (path + '.md')).exists(), (page.name, target))
        for overview in ('docs/skills/README.md', 'docs/principles/README.md', 'docs/guide/README.md'):
            source = (ROOT / overview).read_text()
            exported = next(p.read_text() for p in output.glob('*.md') if f'Source: `{overview}`' in p.read_text())
            for label in re.findall(r'\[([^\]]+)\]\(', source):
                self.assertIn(f'[{label}](', exported)

    def test_existing_output_not_overwritten(self):
        output = self.fixture()
        keep = output / 'keep.txt'
        keep.write_text('owned by somebody else')
        with self.assertRaises(ValueError):
            export_wiki(ROOT, output)
        self.assertEqual(keep.read_text(), 'owned by somebody else')
        with self.assertRaises(ValueError):
            export_wiki(ROOT, ROOT / 'docs')
        link = self.fixture() / 'linked'
        link.symlink_to(self.fixture(), target_is_directory=True)
        with self.assertRaises(ValueError):
            export_wiki(ROOT, link)

    def test_no_network_or_settings_changes(self):
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts}
        with patch('socket.socket', side_effect=AssertionError('network forbidden')):
            export_wiki(ROOT, self.fixture())
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in before})


if __name__ == '__main__':
    unittest.main()
