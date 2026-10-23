"""Structural upstream update checks. No downloaded code is executed."""
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from unittest.mock import patch

from tools.compare_upstream import compare_sources
from tools import sync_upstream as sync

HERD = Path.home() / 'Herd'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def row(path, data, commit='a' * 40):
    return {'upstreamPath': path, 'destinationPath': path,
            'upstreamCommit': commit, 'upstreamSha256': digest(data)}


class UpstreamCheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=HERD)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = 'skills/how/SKILL.md'
        self.file = self.root / self.path
        self.file.parent.mkdir(parents=True)
        self.file.write_bytes(b'local adaptation\n')

    def compare(self, old, new):
        before = self.file.read_bytes()
        result = compare_sources(old, new, self.root)
        self.assertEqual(before, self.file.read_bytes())
        return result

    def test_three_way_preserves_adaptation(self):
        result = self.compare([row(self.path, b'original')],
                              [row(self.path, b'candidate', 'b' * 40)])
        entry = result['changed'][0]
        self.assertEqual((entry['oldSha256'], entry['newSha256'], entry['adaptedSha256']),
                         (digest(b'original'), digest(b'candidate'), digest(b'local adaptation\n')))
        self.assertEqual(result['conflicts'], [entry])

    def test_added_skill_report(self):
        result = self.compare([], [row('skills/new/SKILL.md', b'new')])
        self.assertEqual(result['added'][0]['path'], 'skills/new/SKILL.md')
        self.assertEqual(result['skills']['added'], ['skills/new/SKILL.md'])

    def test_rename_requires_resolution(self):
        result = self.compare([row(self.path, b'same')], [row('skills/new/SKILL.md', b'same')])
        self.assertEqual(result['possibleRenames'], [{'oldPath': self.path, 'newPath': 'skills/new/SKILL.md', 'sha256': digest(b'same')}])
        self.assertFalse(result['acceptanceReady'])

    def test_deletion_blocks_acceptance(self):
        result = self.compare([row(self.path, b'old')], [])
        self.assertFalse(result['acceptanceReady'])
        self.assertEqual(result['removed'][0]['resolution'], 'required')

    def test_changed_license_report(self):
        result = self.compare([row('LICENSE', b'old terms')], [row('LICENSE', b'new terms')])
        self.assertEqual(result['noticeChanges'][0]['newSha256'], digest(b'new terms'))

    def test_rejects_unsafe_identity_and_symlink(self):
        for path in ('../escape', '/absolute', 'skills//leaf', '.env', '.git/config'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                compare_sources([], [row(path, b'bad')], self.root)
        self.file.unlink()
        self.file.symlink_to(self.root / 'outside')
        with self.assertRaises(ValueError):
            compare_sources([row(self.path, b'old')], [], self.root)
        with self.assertRaises(ValueError):
            compare_sources([row('a', b'a'), row('a', b'b')], [], self.root)

    def test_rejects_moving_ref_before_fetch(self):
        with patch.object(sync, 'load_sources') as load:
            with self.assertRaises(ValueError):
                sync.build_review(self.root, 'main', 'check')
            load.assert_not_called()


def archive_bytes(files, revision):
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode='w:gz') as archive:
        for path, data in files.items():
            member = tarfile.TarInfo(f'plugins-{revision}/pstack/{path}')
            member.size = len(data)
            archive.addfile(member, io.BytesIO(data))
    return output.getvalue()


class PublicSourceContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=HERD)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.package = Path(__file__).resolve().parents[1]
        self.candidate = 'b' * 40
        self.tree_sha = 'c' * 40
        # Small deterministic baseline fixture retains the required 164-file contract.
        self.original = {f'docs/file-{i}.md': f'file {i}\n'.encode() for i in range(162)}
        self.original['LICENSE'] = b'MIT fixture notice\n'
        self.leaf = 'skills/how/SKILL.md'
        self.original[self.leaf] = b'---\nname: how\ndescription: Explain a codebase\n---\n# How\nRead the source and explain its flow.\n'
        self.proposed = dict(self.original)
        self.proposed[self.leaf] += b'Name the callers.\n'
        self.proposed['docs/file-0.md'] += b'candidate\n'
        self.proposed['LICENSE'] += b'Changed fixture notice.\n'
        self.proposed['skills/new/SKILL.md'] = b'---\nname: new\n---\n# New\n'
        self.baseline_archive = archive_bytes(self.original, sync.BASELINE)
        self.baseline_hash = digest(self.baseline_archive)
        old = [row(path, data, sync.BASELINE) for path, data in sorted(self.original.items())]
        for path, data in self.original.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        (self.root / self.leaf).write_bytes(b'portable adapted instructions\n')
        manifest = dict(schemaVersion=1, repository='https://github.com/cursor/plugins', subtree='pstack/',
                        commit=sync.BASELINE, archiveSha256=self.baseline_hash, files=old)
        manifest_path = self.root / f'docs/parity/upstream-manifests/{sync.BASELINE}.json'
        manifest_path.parent.mkdir(parents=True)
        manifest_path.write_text(json.dumps(manifest))
        (self.root / 'docs/parity/inventory.json').write_text(json.dumps(old))
        for path in ('.env', '.codex/settings.json', 'UPSTREAM.md', 'personal.md'):
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b'protected fixture\n')
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        subprocess.run(['git', '-C', str(self.root), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(self.root), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'fixture'], check=True)
        self.responses = {
            sync.ARCHIVE + sync.BASELINE: self.baseline_archive,
            sync.ARCHIVE + self.candidate: archive_bytes(self.proposed, self.candidate),
            sync.API + '/commits/' + self.candidate: json.dumps({'sha': self.candidate, 'commit': {'tree': {'sha': self.tree_sha}}}).encode(),
            sync.API + '/compare/' + sync.BASELINE + '...' + self.candidate: json.dumps({'merge_base_commit': {'sha': sync.BASELINE}, 'base_commit': {'sha': sync.BASELINE}, 'status': 'ahead'}).encode(),
            sync.API + '/git/trees/' + self.tree_sha + '?recursive=1': json.dumps({'sha': self.tree_sha, 'truncated': False, 'tree': [
                {'path': 'pstack/' + path, 'type': 'blob', 'mode': '100644', 'sha': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()} for path, data in self.proposed.items()]}).encode()}

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): digest(path.read_bytes()) for path in self.root.rglob('*')
                if path.is_file() and '.upstream' not in path.relative_to(self.root).parts}

    def run_review(self, command):
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            return sync.build_review(self.root, self.candidate, command, self.responses.__getitem__)

    def test_check_and_prepare_preserve_package_and_pin(self):
        for command in ('check', 'prepare'):
            with self.subTest(command=command):
                before = self.snapshot()
                bundle = self.run_review(command)
                self.assertEqual(before, self.snapshot())
                self.assertEqual(len(bundle['files']['changed']), 3)
                review = self.root / '.upstream/reviews' / self.candidate
                self.assertEqual(json.loads((review / 'report.json').read_text()), bundle)
                for path, expected in bundle['artifactHashes'].items():
                    self.assertEqual(digest((review / path).read_bytes()), expected)
                self.assertFalse((review / 'drafts' / self.leaf).exists())
                self.assertEqual((review / 'conflicts' / (self.leaf + '.json')).is_file(), True)
                if command == 'prepare':
                    self.assertEqual((review / 'drafts/docs/file-0.md').read_bytes(), self.proposed['docs/file-0.md'])
                    self.assertIn(b'+candidate', (review / 'draft.patch').read_bytes())
                with self.assertRaises(ValueError):
                    self.run_review(command)
                shutil.rmtree(review)

    def test_new_portable_manifest_does_not_overwrite_adapted_identity(self):
        source = '.cursor-plugin/plugin.json'
        original = dict(self.original)
        del original['docs/file-161.md']
        original[source] = b'{"name":"pstack","version":"0.15.15"}\n'
        proposed = dict(self.proposed)
        del proposed['docs/file-161.md']
        proposed[source] = b'{"name":"pstack","version":"0.15.25"}\n'
        proposed['plugin.json'] = b'{"name":"pstack","version":"0.15.25"}\n'
        baseline_archive = archive_bytes(original, sync.BASELINE)
        self.baseline_hash = digest(baseline_archive)
        old = [row(path, data, sync.BASELINE) for path, data in sorted(original.items())]
        for record in old:
            if record['upstreamPath'] == source:
                record['destinationPath'] = 'plugin.json'
        manifest_path = self.root / f'docs/parity/upstream-manifests/{sync.BASELINE}.json'
        manifest = json.loads(manifest_path.read_text())
        manifest.update(archiveSha256=self.baseline_hash, files=old)
        manifest_path.write_text(json.dumps(manifest))
        (self.root / 'docs/parity/inventory.json').write_text(json.dumps(old))
        portable = b'{"name":"pstack-openai","version":"0.1.0"}\n'
        (self.root / 'plugin.json').write_bytes(portable)
        self.responses[sync.ARCHIVE + sync.BASELINE] = baseline_archive
        self.responses[sync.ARCHIVE + self.candidate] = archive_bytes(proposed, self.candidate)
        tree_key = sync.API + '/git/trees/' + self.tree_sha + '?recursive=1'
        tree = json.loads(self.responses[tree_key])
        tree['tree'] = [
            {'path': 'pstack/' + path, 'type': 'blob', 'mode': '100644',
             'sha': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}
            for path, data in proposed.items()]
        self.responses[tree_key] = json.dumps(tree).encode()
        bundle = self.run_review('prepare')
        added = next(entry for entry in bundle['files']['added'] if entry['path'] == 'plugin.json')
        self.assertEqual(added['destinationPath'], 'references/upstream-metadata/plugin.json')
        self.assertEqual((self.root / 'plugin.json').read_bytes(), portable)
        destinations = [entry['destinationPath'] for category in ('added', 'removed', 'changed', 'unchanged')
                        for entry in bundle['files'][category]]
        self.assertEqual(len(destinations), len(set(destinations)))

    def test_rejects_source_tampering_and_divergence_before_write(self):
        cases = [sync.ARCHIVE + sync.BASELINE, sync.ARCHIVE + self.candidate,
                 sync.API + '/commits/' + self.candidate,
                 sync.API + '/compare/' + sync.BASELINE + '...' + self.candidate,
                 sync.API + '/git/trees/' + self.tree_sha + '?recursive=1']
        for key in cases:
            saved = self.responses[key]
            self.responses[key] = b'{}' if key.startswith(sync.API) else archive_bytes({'LICENSE': b'tampered'}, self.candidate)
            with self.subTest(key=key), self.assertRaises((ValueError, KeyError)):
                self.run_review('check')
            self.assertFalse((self.root / '.upstream').exists())
            self.responses[key] = saved

    def test_rejects_output_symlink_before_fetch(self):
        (self.root / '.upstream').symlink_to(self.root / 'elsewhere')
        with self.assertRaises(ValueError):
            self.run_review('check')

    def test_license_deletion_remains_a_review_blocker(self):
        proposed = dict(self.proposed)
        del proposed['LICENSE']
        self.responses[sync.ARCHIVE + self.candidate] = archive_bytes(proposed, self.candidate)
        key = sync.API + '/git/trees/' + self.tree_sha + '?recursive=1'
        tree = json.loads(self.responses[key])
        tree['tree'] = [entry for entry in tree['tree'] if entry['path'] != 'pstack/LICENSE']
        self.responses[key] = json.dumps(tree).encode()
        bundle = self.run_review('check')
        self.assertEqual(bundle['files']['removed'][0]['path'], 'LICENSE')
        self.assertIsNone(bundle['files']['noticeChanges'][0]['newSha256'])
        self.assertFalse(bundle['files']['acceptanceReady'])

    def test_archive_rejects_links_traversal_and_duplicate_members(self):
        for kind in ('link', 'traversal', 'duplicate'):
            output = io.BytesIO()
            with tarfile.open(fileobj=output, mode='w:gz') as archive:
                member = tarfile.TarInfo(f'plugins-{self.candidate}/pstack/LICENSE')
                if kind == 'link':
                    member.type = tarfile.SYMTYPE
                    member.linkname = '/tmp/escape'
                elif kind == 'traversal':
                    member.name = f'plugins-{self.candidate}/pstack/../LICENSE'
                archive.addfile(member)
                if kind == 'duplicate':
                    archive.addfile(member)
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                sync.unpack_archive(output.getvalue(), self.candidate)

    def test_real_shaped_canonical_leaf_candidate(self):
        archive = HERD / 'pstack-port-research/task-1-20261007/upstream.tar.gz'
        if not archive.exists():
            self.skipTest('Retained canonical archive is unavailable; synthetic contract still runs')
        original = sync.unpack_archive(archive.read_bytes(), sync.BASELINE)
        proposed = dict(original)
        proposed[self.leaf] += b'\nFixture candidate: name each caller in the explanation.\n'
        responses = dict(self.responses)
        responses[sync.ARCHIVE + sync.BASELINE] = archive.read_bytes()
        responses[sync.ARCHIVE + self.candidate] = archive_bytes(proposed, self.candidate)
        responses[sync.API + '/git/trees/' + self.tree_sha + '?recursive=1'] = json.dumps({'sha': self.tree_sha, 'truncated': False, 'tree': [
            {'path': 'pstack/' + path, 'type': 'blob', 'mode': '100644', 'sha': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()} for path, data in proposed.items()]}).encode()
        canonical_root = self.root / 'canonical-source-contract'
        canonical_manifest = canonical_root / f'docs/parity/upstream-manifests/{sync.BASELINE}.json'
        canonical_manifest.parent.mkdir(parents=True)
        shutil.copy2(self.package / f'docs/parity/upstream-manifests/{sync.BASELINE}.json', canonical_manifest)
        old, new, _, _, identity = sync.load_sources(canonical_root, self.candidate, responses.__getitem__)
        result = compare_sources(old, new, self.package)
        self.assertEqual([entry['path'] for entry in result['changed']], [self.leaf])
        self.assertEqual(result['changed'][0]['oldSha256'], digest(original[self.leaf]))
        self.assertEqual(result['changed'][0]['newSha256'], digest(proposed[self.leaf]))
        self.assertEqual(result['changed'][0]['adaptedSha256'], digest((self.package / self.leaf).read_bytes()))
        self.assertEqual(identity['baselineArchiveSha256'], sync.ARCHIVE_SHA256)

    def test_canonical_manifest_matches_approved_archive(self):
        manifest = json.loads((self.package / f'docs/parity/upstream-manifests/{sync.BASELINE}.json').read_text())
        self.assertEqual(len(manifest['files']), 164)
        self.assertEqual(len({r['upstreamPath'] for r in manifest['files']}), 164)
        # Optional retained research evidence is verified when available, never fetched.
        archive = HERD / 'pstack-port-research/task-1-20261007/upstream.tar.gz'
        if archive.exists():
            self.assertEqual(digest(archive.read_bytes()), sync.ARCHIVE_SHA256)
            source = sync.unpack_archive(archive.read_bytes(), sync.BASELINE)
            self.assertEqual({r['upstreamPath']: r['upstreamSha256'] for r in manifest['files']},
                             {path: digest(data) for path, data in source.items()})


if __name__ == '__main__':
    unittest.main()

class PatchPresentationTests(unittest.TestCase):
    def test_final_newline_markers_preserve_line_boundaries(self):
        from tools.sync_upstream import draft_patch
        self.assertEqual(draft_patch(b'old',b'new','x'), '--- a/x\n+++ b/x\n@@ -1 +1 @@\n-old\n\\ No newline at end of file\n+new\n\\ No newline at end of file\n')
        self.assertIn('+new\n',draft_patch(b'old\n',b'new\n','x'))
