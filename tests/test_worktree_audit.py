import importlib.util
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / 'skills/poteto-mode/scripts/worktree-audit.py'
SCRATCH = Path.home() / 'Herd/pstack-port-research/task-15-fixtures'


class WorktreeAuditTests(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=SCRATCH)
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / 'repo with spaces'
        self.repo.mkdir()
        self.git('init', '-b', 'base')
        self.git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '--allow-empty', '-m', 'fixture')
        spec = importlib.util.spec_from_file_location('worktree_audit', HELPER)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True, capture_output=True)

    def candidate(self, detached=False):
        path = Path(self.temp.name) / 'candidate with spaces'
        self.git('worktree', 'add', *(['--detach'] if detached else ['-b', 'topic']), str(path), 'base')
        return path

    def audit(self, base='base', history=None, prs=None):
        return self.module.audit_worktrees(self.repo, base, history, prs)

    def test_path_with_spaces(self):
        path = self.candidate()
        row = self.audit()[0]
        self.assertEqual(row['worktree'], str(path))
        self.assertIs(row['merged'], True)
        self.assertEqual(row['dirty'], 'clean')
        self.assertIsNone(row['pr'])
        self.assertIsNone(row['last_chat'])
        self.assertEqual(row['bucket'], 'hold-unknown')

    def test_detached_head(self):
        self.candidate(True)
        row = self.audit()[0]
        self.assertIsNone(row['branch'])
        self.assertEqual(row['remote'], 'detached')

    def test_missing_base(self):
        self.candidate()
        row = self.audit('missing')[0]
        self.assertIsNone(row['merged'])
        self.assertEqual(row['bucket'], 'hold-unknown')

    def test_dirty_untracked_work(self):
        path = self.candidate()
        (path / 'precious notes.txt').write_text('keep')
        row = self.audit(history={str(path): None}, prs=[])[0]
        self.assertEqual(row['dirty'], 'scratch:1')
        self.assertEqual(row['bucket'], 'hold-wip')
        self.assertTrue((path / 'precious notes.txt').exists())

    def test_no_network_or_history_probe(self):
        self.candidate()
        original = self.module.subprocess.run
        commands = []
        def spy(command, **kwargs):
            commands.append(command)
            self.assertEqual(command[0], 'git')
            self.assertFalse(set(command) & {'fetch', 'push', 'ls-remote', 'remote', 'remove', 'prune'})
            return original(command, **kwargs)
        with patch.object(self.module.subprocess, 'run', side_effect=spy):
            self.audit()
        self.assertTrue(commands)

    def test_cli_exports(self):
        path = self.candidate()
        history = Path(self.temp.name) / 'history.json'
        prs = Path(self.temp.name) / 'prs.json'
        history.write_text(json.dumps({str(path): None}))
        prs.write_text('[]')
        result = subprocess.run(['bash', str(HELPER.with_suffix('.sh')), '--repo', str(self.repo), '--base', 'base', '--history-map', str(history), '--pr-state', str(prs)], check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout)[0]['worktree'], str(path))

    def test_documented_bun_wrapper_preserves_arguments_and_worktrees(self):
        path = self.candidate()
        note = path / 'precious notes.txt'
        note.write_text('preserve this work\n')
        history = Path(self.temp.name) / 'authorized history export.json'
        prs = Path(self.temp.name) / 'authorized PR export.json'
        history.write_text(json.dumps({str(path): None}))
        prs.write_text('[]')
        before = {
            'worktrees': self.git('worktree', 'list', '--porcelain', '-z').stdout,
            'primary_status': self.git('status', '--porcelain=v1', '-z').stdout,
            'candidate_status': subprocess.run(
                ['git', '-C', str(path), 'status', '--porcelain=v1', '-z'],
                check=True, capture_output=True).stdout,
            'note': note.read_bytes(),
            'history': history.read_bytes(),
            'prs': prs.read_bytes(),
        }
        playbook = ROOT / 'skills/poteto-mode/playbooks/worktree-cleanup.md'
        documented = next(line.strip() for line in playbook.read_text().splitlines()
                          if line.strip().startswith('bun --no-install -e '))
        replacements = {
            '<repository-path>': str(self.repo),
            '<verified-local-base-ref>': self.git('rev-parse', 'base').stdout.decode().strip(),
            '<authorized-history-export.json>': str(history),
            '<authorized-pr-export.json>': str(prs),
        }
        command = [replacements.get(argument, argument) for argument in shlex.split(documented)]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = json.loads(result.stdout)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['worktree'], str(path))
        self.assertIs(rows[0]['merged'], True)
        self.assertEqual(rows[0]['bucket'], 'hold-wip')
        self.assertEqual(rows[0]['pr'], [])
        self.assertTrue(rows[0]['history_known'])
        self.assertEqual(self.git('worktree', 'list', '--porcelain', '-z').stdout, before['worktrees'])
        self.assertEqual(self.git('status', '--porcelain=v1', '-z').stdout, before['primary_status'])
        self.assertEqual(subprocess.run(
            ['git', '-C', str(path), 'status', '--porcelain=v1', '-z'],
            check=True, capture_output=True).stdout, before['candidate_status'])
        self.assertEqual(note.read_bytes(), before['note'])
        self.assertEqual(history.read_bytes(), before['history'])
        self.assertEqual(prs.read_bytes(), before['prs'])

    def test_explicit_merged_review(self):
        path = self.candidate()
        row = self.audit(history={str(path): None}, prs=[])[0]
        self.assertEqual(row['bucket'], 'review-merged')
        self.assertEqual(row['pr'], [])
        self.assertTrue(row['history_known'])

    def test_closed_pr_is_not_merge_evidence(self):
        path = self.candidate()
        subprocess.run(['git', '-C', str(path), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '--allow-empty', '-m', 'new'], check=True, capture_output=True)
        row = self.audit(history={str(path): None}, prs=[{'headRefName': 'topic', 'number': 1, 'state': 'CLOSED'}])[0]
        self.assertFalse(row['merged'])
        self.assertEqual(row['bucket'], 'review')

    def test_open_pr_and_recent_chat(self):
        import time
        path = self.candidate()
        history = {str(path): time.time() - 60}
        self.assertEqual(self.audit(history=history, prs=[])[0]['bucket'], 'verify-recent-chat')
        self.assertEqual(self.audit(history=history, prs=[{'headRefName': 'topic', 'number': 1, 'state': 'OPEN'}])[0]['bucket'], 'hold-open-pr')

    def test_invalid_export(self):
        self.candidate()
        for history, prs in [([], None), ({'x': 'y'}, None), (None, {}), (None, [{'state': 'CLOSED'}])]:
            with self.assertRaises(ValueError):
                self.audit(history=history, prs=prs)

    def test_newline_path(self):
        path = Path(self.temp.name) / 'candidate\nnewline'
        self.git('worktree', 'add', '-b', 'newline', str(path), 'base')
        self.assertEqual(self.audit()[0]['worktree'], str(path))

    def test_tracked_and_untracked(self):
        path = self.candidate()
        (path / 'tracked').write_text('initial')
        subprocess.run(['git', '-C', str(path), 'add', 'tracked'], check=True, capture_output=True)
        (path / 'untracked').write_text('keep')
        row = self.audit(history={str(path): None}, prs=[])[0]
        self.assertEqual(row['tracked_changes'], 1)
        self.assertEqual(row['untracked_changes'], 1)
        self.assertEqual(row['bucket'], 'hold-wip')

    def test_failed_local_fields_hold_unknown(self):
        path = self.candidate()
        self.git('config', 'branch.topic.remote', '.')
        self.git('config', 'branch.topic.merge', 'refs/heads/base')
        # A different tracking commit makes rev-list evidence material.
        self.git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '--allow-empty', '-m', 'base update')
        original = self.module._git
        for command, field in [('log', 'age'), ('rev-list', 'remote')]:
            with self.subTest(command=command):
                def failing_git(repo, *args):
                    if args[0] == command:
                        return subprocess.CompletedProcess(['git', *args], 128, b'', b'fixture local read failure')
                    return original(repo, *args)
                with patch.object(self.module, '_git', side_effect=failing_git):
                    row = self.audit(history={str(path): None}, prs=[])[0]
                self.assertIsNone(row[field])
                self.assertIs(row['merged'], True)
                self.assertEqual(row['dirty'], 'clean')
                self.assertEqual(row['bucket'], 'hold-unknown')


if __name__ == '__main__':
    unittest.main()
