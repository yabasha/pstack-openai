import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate_evidence import validate_evidence


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'result.txt').write_text('observed')
        self.record = dict(caseId='absent-workers', sourcePaths=['pstack/commands/poteto.md'],
            packageVersion='0.15.15', packageCommit='a'*40, host='codex', hostMode='test',
            date='2026-10-07', documentedCapabilities=[], exposedTools=['observed.spawn'],
            successfulOperations=[dict(operation='spawn', tool='observed.spawn', evidence='result.txt')],
            permissions=dict(execution='granted', writes='granted', externalActions='denied'),
            input='fixture', observedOutput='fixture observation', artifacts=['result.txt'],
            status='pass', limits=[], execution='workers', models=dict(requested='unknown', actual='unknown'),
            priorActionIdentities=[])

    def check(self):
        return validate_evidence(self.record, 'a'*40, self.root)

    def test_stale_commit_rejected(self):
        self.record['packageCommit'] = 'b'*40
        self.assertTrue(self.check())

    def test_missing_artifact_rejected(self):
        self.record['artifacts'] = ['missing.txt']
        self.assertTrue(self.check())

    def test_reduced_is_not_full(self):
        self.record['execution'] = 'sequential'
        self.assertTrue(self.check())
        self.record['status'] = 'reduced-pass'
        self.assertEqual([], self.check())

    def test_claimed_worker_without_operation(self):
        self.record['successfulOperations'] = []
        self.assertTrue(self.check())

    def test_blocked_denial_preserved(self):
        self.record.update(status='blocked', execution='unavailable', artifacts=[], successfulOperations=[])
        self.record['permissions']['execution'] = 'denied'
        self.assertEqual([], self.check())

    def test_pass_requires_permissions_and_artifacts(self):
        self.record['permissions']['writes'] = 'unknown'
        self.assertTrue(self.check())
        self.record['permissions']['writes'] = 'granted'
        self.record['artifacts'] = []
        self.assertTrue(self.check())

    def test_unexposed_tool_and_escaping_artifact_rejected(self):
        self.record['successfulOperations'][0]['tool'] = 'imaginary.spawn'
        self.record['artifacts'] = ['../outside']
        self.assertTrue(self.check())

    def test_valid_worker_fixture(self):
        self.assertEqual([], self.check())

    def test_malformed_record_rejected(self):
        self.record['exposedTools'] = None
        self.assertTrue(self.check())

    def test_registry_rejects_wrong_scope_and_structural_host_claim(self):
        directory = self.root / 'docs/parity'
        directory.mkdir(parents=True)
        entry = dict(caseId='absent-workers', sourcePaths=['other'], requiredHosts=['codex'], structuralOnly=False)
        path = directory / 'case-registry.json'
        path.write_text(json.dumps(dict(entries=[entry])))
        self.assertTrue(self.check())
        entry['sourcePaths'] = self.record['sourcePaths']
        entry['structuralOnly'] = True
        path.write_text(json.dumps(dict(entries=[entry])))
        self.assertTrue(self.check())

    def test_external_write_requires_prior_identity(self):
        self.record['successfulOperations'].append(dict(operation='external-write',tool='observed.spawn',evidence='result.txt'))
        self.assertTrue(self.check())
        self.record['permissions']['externalActions'] = 'granted'
        self.record['priorActionIdentities'] = ['action-1']
        self.assertEqual([], self.check())

    def test_cli_invalid_and_valid(self):
        evidence = self.root / 'docs/parity/evidence'
        evidence.mkdir(parents=True)
        record_path = evidence / 'fixture.json'
        record_path.write_text(json.dumps(self.record))
        command = [sys.executable, '-B', str(Path(__file__).resolve().parents[1] / 'tools/validate_evidence.py'),
                   '--root', str(self.root), '--commit', 'a'*40]
        good = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, good.returncode, good.stdout)
        self.record['packageCommit'] = 'b'*40
        record_path.write_text(json.dumps(self.record))
        bad = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad.returncode)
        self.assertIn('packageCommit', bad.stdout)
