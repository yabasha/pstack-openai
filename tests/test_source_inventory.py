import hashlib
import re
import tempfile
import unittest
from pathlib import Path

from tools.source_inventory import inspect_source

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/Users/digital-hawk/Herd/pstack-port-research/task-1-20261007/extracted/plugins-df581122cde17e6e27686b5a448bde23e4ad4318/pstack')
COMMIT = 'df581122cde17e6e27686b5a448bde23e4ad4318'


class SourceInventoryTests(unittest.TestCase):
    def test_exact_baseline(self):
        records = inspect_source(SOURCE, COMMIT)
        paths = {r['upstreamPath'] for r in records}
        spec = (ROOT / 'docs/superpowers/specs/2026-10-07-pstack-openai-design.md').read_text()
        a = spec.split('## Appendix A:')[1].split('## Appendix B:')[0]
        b = spec.split('## Appendix B:')[1].split('## Appendix C:')[0]
        expected = {f'skills/{name}/SKILL.md' for name in re.findall(r'^\| `([^`]+)`', a, re.M)}
        expected.update(re.findall(r'^- `([^`]+)`', b, re.M))
        self.assertEqual(paths, expected)
        self.assertEqual(len(records), 164)
        self.assertEqual(paths, set((ROOT / 'docs/parity/baseline-paths.txt').read_text().splitlines()))
        skills = [p for p in paths if re.fullmatch(r'skills/[^/]+/SKILL.md', p)]
        self.assertEqual(len(skills), 51)
        self.assertEqual(sum(p.split('/')[1].startswith('principle-') for p in skills), 24)
        self.assertEqual(sum(p.startswith('skills/poteto-mode/playbooks/') for p in paths), 23)
        self.assertEqual(sum(p.startswith('automations/benny/') and p.endswith('/SKILL.md') for p in paths), 3)

    def test_provenance_and_archive_boundary(self):
        for record in inspect_source(SOURCE, COMMIT):
            self.assertEqual(record['upstreamSha256'], hashlib.sha256((SOURCE / record['upstreamPath']).read_bytes()).hexdigest())
            self.assertEqual(record['upstreamCommit'], COMMIT)
            self.assertEqual(record['licenseProvenance']['copyright'], 'Copyright (c) 2026 Lauren Tan')
            self.assertEqual(record['adaptationStatus'], 'pending')
            for host in ('chatgpt', 'codex'):
                self.assertEqual(record['verification'][host], {'status': 'not-run', 'evidence': []})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'outside-link').symlink_to(SOURCE / 'LICENSE')
            with self.assertRaises(ValueError):
                inspect_source(root, COMMIT)
            (root / 'outside-link').unlink()
            (root / 'directory-link').symlink_to(SOURCE, target_is_directory=True)
            with self.assertRaises(ValueError):
                inspect_source(root, COMMIT)
        with self.assertRaises(ValueError):
            inspect_source(SOURCE / '..', COMMIT)


if __name__ == '__main__':
    unittest.main()
