"""Local decision-log contract tests; no remote sinks or private inputs."""
import os
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = ROOT / '.superpowers/sdd/2026-10-07-pstack-openai/task-16-fixtures'
HELPER = Path(os.environ.get('DECISION_LOG_HELPER', ROOT / 'skills/show-me-your-work/scripts/log.sh'))
HEADER = b'ts\tphase\tdecision\twhy\tevidence\tresult\n'

class DecisionLogTests(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.output = SCRATCH / (self._testMethodName + '.tsv')
        self.output.unlink(missing_ok=True)

    def call(self, output, cells=None):
        return subprocess.run(['bash', str(HELPER), str(output), *(cells or ['frame', 'chosen', 'reason', 'file:12', 'open'])], capture_output=True)

    def test_tab_and_newline_rejected(self):
        for separator in ['\t', '\n', '\r']:
            for column in range(5):
                cells = ['frame', 'chosen', 'reason', 'file:12', 'open']
                cells[column] += separator + 'extra'
                result = self.call(self.output, cells)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.output.exists())
                nested = SCRATCH / "invalid-parent" / "log.tsv"
                self.assertNotEqual(self.call(nested, cells).returncode, 0)
                self.assertFalse(nested.parent.exists())
                self.output.write_bytes(HEADER + b'previous row\n')
                before = self.output.read_bytes()
                self.assertNotEqual(self.call(self.output, cells).returncode, 0)
                self.assertEqual(self.output.read_bytes(), before)
                self.output.unlink()

    def test_missing_output_fails(self):
        self.assertNotEqual(self.call('').returncode, 0)
        self.assertNotEqual(subprocess.run(['bash', str(HELPER), 'frame', 'chosen', 'reason', 'file:12', 'open'], capture_output=True).returncode, 0)
        for separator in ['\t', '\n', '\r']:
            invalid = str(self.output) + separator + 'suffix'
            self.assertNotEqual(self.call(invalid).returncode, 0)
            self.assertFalse(Path(invalid).exists())

    def test_existing_log_is_preserved(self):
        before = HEADER + b'2026-01-01T00:00:00Z\told\tchosen\treason\tfile:1\topen\n'
        self.output.write_bytes(before)
        self.assertEqual(self.call(self.output).returncode, 0)
        after = self.output.read_bytes()
        self.assertTrue(after.startswith(before))
        self.assertEqual(len(after.splitlines()), 3)
        self.assertEqual(after.count(HEADER), 1)
        self.assertEqual(after.splitlines()[-1].split(b'\t')[1:], [b'frame', b'chosen', b'reason', b'file:12', b'open'])

    def test_new_log_and_formula_protection(self):
        self.assertEqual(self.call(self.output, ['=frame', '+chosen', '-reason', '@file:12', 'open']).returncode, 0)
        rows = self.output.read_bytes().splitlines()
        self.assertEqual(rows[0] + b'\n', HEADER)
        self.assertEqual(rows[1].split(b'\t')[1:], [b"'=frame", b"'+chosen", b"'-reason", b"'@file:12", b'open'])
        self.assertRegex(rows[1].split(b'\t')[0].decode(), r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')

if __name__ == '__main__':
    unittest.main()
