"""Historical full-package migration fixture, never a host or live upstream run.

Canonical source bytes stay pinned to df581122cde17e6e27686b5a448bde23e4ad4318.
Package metadata comes from the distinct local PACKAGE_SNAPSHOT commit, so a
new active baseline cannot mix with that historical 164-file source archive.
Current imported tools still drive every transaction and validation assertion.
"""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from tests.test_upstream_check import archive_bytes, digest
from tests import test_upstream_apply as apply_fixtures
from tests.test_source_inventory import SOURCE
from tools import sync_upstream as sync
from tools.validate_package import validate_package

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_SNAPSHOT = '36547e7fec1b24b97e2c3391ea4758d8e9e6ad2b'


class FullPackageUpdateTests(unittest.TestCase):
    git_at = apply_fixtures.UpstreamApplyTests.git_at
    git = apply_fixtures.UpstreamApplyTests.git
    save_resolutions = apply_fixtures.UpstreamApplyTests.save_resolutions
    apply = apply_fixtures.UpstreamApplyTests.apply
    snapshot = apply_fixtures.UpstreamApplyTests.snapshot

    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix='pstack-full-update-',dir=Path.home()/'Herd')
        self.addCleanup(tmp.cleanup)
        self.container = Path(tmp.name)
        repo = self.container/'repository'; repo.mkdir()
        snapshot = subprocess.run(
            ['git', 'archive', '--format=tar', PACKAGE_SNAPSHOT], cwd=ROOT,
            capture_output=True)
        if snapshot.returncode:
            self.skipTest(f'Pinned local package snapshot {PACKAGE_SNAPSHOT} unavailable; no network lookup attempted.')
        subprocess.run(['tar', '-xf', '-', '-C', str(repo)],
                       input=snapshot.stdout, check=True)
        subprocess.run(['git','init','-q',str(repo)],check=True)
        self.root = repo
        self.git('add','.'); self.git('commit','-qm','complete synthetic package source')
        self.root = self.container/'owned'
        self.git_at(repo,'worktree','add','-q','--detach',str(self.root))
        self.original = {p.relative_to(SOURCE).as_posix():p.read_bytes() for p in SOURCE.rglob('*') if p.is_file()}
        self.baseline_archive = archive_bytes(self.original,sync.BASELINE)
        self.baseline_hash = digest(self.baseline_archive)
        manifest = self.root/f'docs/parity/upstream-manifests/{sync.BASELINE}.json'
        data = json.loads(manifest.read_text()); data['archiveSha256'] = self.baseline_hash
        manifest.write_text(json.dumps(data))
        self.git('add','.');self.git('commit','-qm','synthetic archive container identity')
        self.candidate = 'b'*40; self.leaf='skills/bro/SKILL.md'; self.owner='full-package-fixture'
        self.proposed = dict(self.original); self.proposed[self.leaf] += b'\nAdditional upstream fixture sentence.\n'
        self.prepare()

    def prepare(self):
        old = sync.BASELINE
        major, minor, patch_version = map(int, json.loads((self.root/'plugin.json').read_text())['version'].split('.'))
        self.candidate_version = f'{major}.{minor}.{patch_version + 1}'
        responses = {
            sync.ARCHIVE+old: self.baseline_archive,
            sync.ARCHIVE+self.candidate: archive_bytes(self.proposed,self.candidate),
            sync.API+'/commits/'+self.candidate: json.dumps({'sha':self.candidate,'commit':{'tree':{'sha':'c'*40}}}).encode(),
            sync.API+'/compare/'+old+'...'+self.candidate: json.dumps({'merge_base_commit':{'sha':old},'base_commit':{'sha':old},'status':'ahead'}).encode(),
            sync.API+'/git/trees/'+'c'*40+'?recursive=1': json.dumps({'sha':'c'*40,'truncated':False,'tree':[{'path':'pstack/'+p,'type':'blob','mode':'100644','sha':hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()} for p,d in self.proposed.items()]}).encode()}
        self.responses=responses
        with patch.object(sync,'ARCHIVE_SHA256',self.baseline_hash):
            self.bundle=sync.build_review(self.root,self.candidate,'prepare',responses.__getitem__)
        self.review=self.root/'.upstream/reviews'/self.candidate
        self.resolutions=dict(schemaVersion=2,kind=sync.RESOLUTION_KIND,candidate=self.candidate,packageCommit=self.bundle['packageCommit'],reviewSha256=digest((self.review/'report.json').read_bytes()),candidateVersion=self.candidate_version,entries=[])
        for e in self.bundle['files']['changed']+self.bundle['files']['added']+self.bundle['files']['removed']:
            content='resolved/'+e['destinationPath'] if e['newSha256'] else None
            if content:
                target=self.review/content;target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes((self.root/e['destinationPath']).read_bytes()+b'\nReviewed fixture sentence.\n' if e['oldSha256'] else self.proposed[e['path']])
            self.resolutions['entries'].append(dict(**e,disposition='adapt-manually' if e['oldSha256'] and e['newSha256'] else 'add-reviewed' if e['newSha256'] else 'delete-reviewed',rationale='Reviewed inert package update.',reviewedCallers=e['dependentCallers'],contentPath=content,reviewedSha256=digest((self.review/content).read_bytes()) if content else None))
        self.resolution_path=self.review/'approved.json';self.save_resolutions()
        admin=Path(self.git('rev-parse','--absolute-git-dir').strip())
        (admin/'pstack-update-owner.json').write_text(json.dumps(dict(schemaVersion=1,owner=self.owner,worktree=str(self.root),packageCommit=self.bundle['packageCommit'])))

    def test_missing_metadata_rejected_before_package_mutation(self):
        before=self.snapshot()
        with self.assertRaisesRegex(ValueError,'metadata closure'):
            self.apply()
        self.assertEqual(before,self.snapshot())

    def test_added_and_removed_workflows_require_reviewed_metadata(self):
        for label in ('added','removed'):
            self.candidate=('d' if label=='added' else 'e')*40
            self.proposed=dict(self.original)
            if label=='added': self.proposed['skills/new-workflow/SKILL.md']=b'---\nname: new-workflow\n---\nReviewed new workflow.\n'
            else: del self.proposed[self.leaf]
            self.prepare();before=self.snapshot()
            with self.assertRaisesRegex(ValueError,'metadata closure'): self.apply()
            self.assertEqual(before,self.snapshot())

    def metadata(self):
        from tools.baseline_policy import membership
        from tools.build_catalog import build_catalog
        inventory=json.loads((self.root/'docs/parity/inventory.json').read_text())
        entries={e['path']:e for e in self.resolutions['entries']}
        changed_bytes={e['destinationPath']:(self.review/e['contentPath']).read_bytes() for e in entries.values() if e['contentPath']}
        for row in inventory:
            row.update(upstreamCommit=self.candidate,upstreamSha256=digest(self.proposed[row['upstreamPath']]))
            row['verification']={h:{'status':'not-run','evidence':[]} for h in ('chatgpt','codex')}
            if row['upstreamPath'] in entries: row.update(rationale=entries[row['upstreamPath']]['rationale'],adaptationStatus='adapted-reviewed')
        owners={r['upstreamPath']:p.relative_to(self.root).as_posix() for p in (self.root/'docs/parity/adaptations').glob('*.json') for r in json.loads(p.read_text())}
        registry=json.loads((self.root/'docs/parity/case-registry.json').read_text())
        for e in registry['entries']:
            if not e['structuralOnly']: e['hostStatus']={h:'not-run' for h in ('chatgpt','codex')}
        policy=dict(schemaVersion=1,upstreamCommit=self.candidate,reviewRationale='Explicit synthetic review preserves current workflow membership.',**membership(inventory))
        plugin=json.loads((self.root/'plugin.json').read_text());plugin['version']=self.candidate_version
        changed_bytes['plugin.json']=sync.json_bytes(plugin)
        audit=json.loads((self.root/'docs/parity/dependencies.json').read_text());audit['sourceCommit']=self.candidate
        rows={r['upstreamPath']:r for r in inventory}
        for a in audit['sourceAudit']:
            r=rows[a['sourcePath']];a['sourceSha256']=r['upstreamSha256'];a['packageDependencies']=r['dependencies']
            a['destinationSha256']=digest(changed_bytes.get(r['destinationPath'],(self.root/r['destinationPath']).read_bytes()))
        files={'docs/parity/dependencies.json':sync.json_bytes(audit),'docs/parity/case-registry.json':sync.json_bytes(registry),'docs/parity/baseline-policy.json':sync.json_bytes(policy)}
        dispositions=json.loads((self.root/'docs/parity/remnant-dispositions.json').read_text())
        upstream=(self.root/'UPSTREAM.md').read_bytes()+(f'\n## Unaccepted candidate {self.candidate}\n\nCandidate version {self.candidate_version}. Archive SHA-256 {self.bundle["sourceIdentity"]["candidateArchiveSha256"]}. Review SHA-256 {self.resolutions["reviewSha256"]}.\nThe inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.\n').encode()
        for d in dispositions:
            if d['path']=='UPSTREAM.md': d['sha256']=digest(upstream)
        files['docs/parity/remnant-dispositions.json']=sync.json_bytes(dispositions)
        catalog=[json.loads(p.read_text()) for p in sorted((self.root/'docs/catalog/skills').glob('*.json'))]
        files.update({p:t.encode() for p,t in build_catalog(self.root,inventory,catalog).items()})
        bundle=dict(schemaVersion=1,kind='pstack-package-metadata',inventory=inventory,fragmentOwners=owners,files=[])
        for name,data in files.items():
            content='resolved/metadata/'+name;target=self.review/content;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
            bundle['files'].append(dict(path=name,contentPath=content,sha256=digest(data)))
        self.metadata_path=self.review/'resolved/package-metadata.json'
        self.metadata_path.write_bytes(sync.json_bytes(bundle))
        self.resolutions['packageMetadata']=dict(contentPath='resolved/package-metadata.json',reviewedSha256=digest(self.metadata_path.read_bytes()))
        self.save_resolutions()
        return bundle

    def test_changed_leaf_closes_fragments_invalidates_and_accepts_before_next_prepare(self):
        self.metadata()
        old_evidence={p:p.read_bytes() for p in (self.root/'docs/parity/evidence').rglob('*') if p.is_file()}
        state=self.apply()
        self.assertFalse(state['acceptanceReady']);self.assertFalse(state['releasable'])
        inventory=json.loads((self.root/'docs/parity/inventory.json').read_text())
        self.assertEqual([],validate_package(self.root,inventory))
        rows={r['upstreamPath']:r for r in inventory}
        fragments=[r for p in (self.root/'docs/parity/adaptations').glob('*.json') for r in json.loads(p.read_text())]
        self.assertEqual(164,len(fragments));self.assertEqual(rows,{r['upstreamPath']:r for r in fragments})
        self.assertTrue(all(v=={'status':'not-run','evidence':[]} for r in inventory for v in r['verification'].values()))
        self.assertTrue(all(p.read_bytes()==d for p,d in old_evidence.items()))
        self.assertTrue((self.root/f'docs/parity/upstream-manifests/{self.candidate}.previous-fragments.json').is_file())
        self.assertFalse((self.root/'docs/parity/upstream-manifests/accepted.json').exists())
        self.git('add','.');self.git('commit','-qm','synthetic tested full package update')
        package_commit=self.git('rev-parse','HEAD').strip()
        manifest=f'docs/parity/upstream-manifests/{self.candidate}.json';evidence='docs/parity/full-package-fixture-acceptance.txt'
        (self.root/evidence).write_text('SYNTHETIC separate acceptance of structurally tested update; host behavior remains untested.')
        receipt=dict(schemaVersion=1,kind='pstack-accepted-baseline',commit=self.candidate,manifestPath=manifest,manifestSha256=digest((self.root/manifest).read_bytes()),packageCommit=package_commit,evidencePath=evidence,evidenceSha256=digest((self.root/evidence).read_bytes()))
        (self.root/'docs/parity/upstream-manifests/accepted.json').write_bytes(sync.json_bytes(receipt))
        self.git('add','.');self.git('commit','-qm','separate synthetic baseline acceptance')
        previous=self.candidate;self.candidate='f'*40
        self.proposed[self.leaf]+=b'Next source update.\n'
        self.responses[sync.ARCHIVE+self.candidate]=archive_bytes(self.proposed,self.candidate)
        self.responses[sync.API+'/commits/'+self.candidate]=json.dumps({'sha':self.candidate,'commit':{'tree':{'sha':'c'*40}}}).encode()
        self.responses[sync.API+'/compare/'+previous+'...'+self.candidate]=json.dumps({'merge_base_commit':{'sha':previous},'base_commit':{'sha':previous},'status':'ahead'}).encode()
        self.responses[sync.API+'/git/trees/'+'c'*40+'?recursive=1']=json.dumps({'sha':'c'*40,'truncated':False,'tree':[{'path':'pstack/'+p,'type':'blob','mode':'100644','sha':hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()} for p,d in self.proposed.items()]}).encode()
        with patch.object(sync,'ARCHIVE_SHA256',self.baseline_hash):
            following=sync.build_review(self.root,self.candidate,'prepare',self.responses.__getitem__)
        self.assertEqual(previous,following['baseline']);self.assertEqual([self.leaf],[r['path'] for r in following['files']['changed']])

    def test_incomplete_metadata_and_caught_failure_preserve_whole_package(self):
        bundle=self.metadata(); before=self.snapshot()
        bundle['fragmentOwners'].pop(self.leaf)
        self.metadata_path.write_bytes(sync.json_bytes(bundle));self.resolutions['packageMetadata']['reviewedSha256']=digest(self.metadata_path.read_bytes());self.save_resolutions()
        with self.assertRaisesRegex(ValueError,'fragment owner'): self.apply()
        self.assertEqual(before,self.snapshot())
        self.metadata()
        def fail(stage): raise RuntimeError('inert transaction interruption')
        with self.assertRaises(RuntimeError): self.apply(failure_hook=fail)
        self.assertEqual(before,self.snapshot())
