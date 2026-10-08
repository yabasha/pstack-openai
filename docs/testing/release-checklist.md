# Release candidate checklist

Version 0.1.0 targets frozen source `e808be2d2b03277fdb1422dd729936e6b775126d`, F3. Report ancestor `a5628dd849174f17b34d24ee7f1afb705cec77e9` contains the blocked-record relink. This checklist records development validation and remaining gates. It does not authorize installation or publication.

- [x] All 164 source dispositions are reviewed, covering 51 root skills, 24 principles, 113 support files and 23 playbooks.
- [x] Registry accounting covers 108 cases: 105 behavioral entries on each host and three structural-only entries.
- [x] Full F3 maintenance suite passed all 190 tests in 145.844 seconds, exit 0.
- [x] Package structural validation passed with exit 0.
- [x] Evidence validation against F3 passed with exit 0; all 210 records remain blocked.
- [x] Catalog consistency check passed with 51 skills and 24 principles; no catalog files were regenerated.
- [x] The actual F3 helper fixture passed bootstrap, 85 tests with 316 assertions, and strict watch-pr TypeScript checking.
- [x] Release CLI returned the expected exit 1, `releasable=false`, zero stale records and two missing-discovery blockers.
- [ ] Actual package discovery in Codex and personal ChatGPT. Both remain false.
- [ ] Supported behavior observed in each actual host. Full and reduced pass counts remain zero.
- [ ] Fresh task review and final whole-branch review completed.
- [ ] Separate authorization and observed completion for any installation, tag or release.

## Exact checks

The resumed F3 suite passed 190 tests in 145.844 seconds, with no failures or skips. This is a fresh integrated run after the reviewed correction.

The F2 maintenance suite ran 189 tests in 143.655 seconds: 187 passed and two failed, with exit 1. The dependency-case test expected not-run on both hosts while the registry recorded blocked. The dependency audit also retained an old README.md destination hash. Those failures stopped completion. A separately reviewed two-file correction updated only the audit destination hash and the dependency test. The test now requires blocked and rejects promotion of unavailable receipts to pass or reduced-pass. README and host evidence behavior were unchanged. The added regression increases the full suite to 190 tests. This operative correction required F3, relinking all 210 blocked records and repeating integrated validation. F1 and F2 history remains available; no host passes were transferred.

Run package commands from `/Users/digital-hawk/Herd/pstack-openai-port`. All Python execution uses Bun with installation disabled and Python bytecode writes disabled. These commands were executed against F3 operative bytes:

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","unittest","discover","-s","tests","-v"],{stdout:"inherit",stderr:"inherit",env:{...process.env,PYTHONDONTWRITEBYTECODE:"1"}});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","tools/validate_package.py","--root",".","--inventory","docs/parity/inventory.json"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","tools/validate_evidence.py","--root",".","--commit","e808be2d2b03277fdb1422dd729936e6b775126d"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","tools/build_catalog.py","--root",".","--check"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","tools/release_report.py","--root",".","--commit","e808be2d2b03277fdb1422dd729936e6b775126d","--version","0.1.0"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

The last command must currently exit 1. The report's `logicalEligibility=true` is preliminary accounting; `releasable=false` is the release decision. The host discovery blockers prevent the CLI from reaching its immutable-identity check, so its output alone does not validate the post-freeze marker. The separate marker check validates its strict schema, 217 existing allowed paths, unchanged inventory identity and every other frozen byte and mode. The unchanged identity_checks and rollback_tested_commit functions are also exercised in an isolated local Git fixture at /Users/digital-hawk/Herd/pstack-task29-f3-report-proof. That fixture uses the exact 720 candidate files and modes, a report commit whose parent is the report ancestor above, and proven F3 ancestry. Its commit is a local test artifact, not the operative report commit. Actual committed marker provenance must still be checked against the later reviewed operative commit before any release or rollback claim.

## Candidate helper verification

The F3 export at `/Users/digital-hawk/Herd/pstack-task29-f3-validation` supplies the actual tested source. Its scripts directory references the approved snapshot's existing node_modules only for reads. All 716 tracked F3 files remained byte- and mode-identical after tests. Dependency and task-owned cache bytes, modes and symlink targets also remained unchanged. No new dependencies were installed, and the operative checkout still has no scripts/node_modules.

From `/Users/digital-hawk/Herd/pstack-task29-f3-validation/skills/poteto-mode/scripts`:

```sh
bun --no-install -e 'import {ensureDependenciesInstalled} from "./bootstrap.ts"; ensureDependenciesInstalled(); console.log("bootstrap PASS");'
ORCH_TEST_ROOT=/Users/digital-hawk/Herd/pstack-task29-f3-orch-scratch bun --no-install test bootstrap.test.ts orch watch-pr
bun --no-install node_modules/typescript/bin/tsc --project watch-pr/tsconfig.json --noEmit --strict
```

All three commands exited 0. The suite passed 85 tests, zero failures, 316 assertions. The compiler emitted no diagnostics. Runtime and exact dependency pins, manifest/lock hashes, historical snapshot authorization and the preserved invalid Implementation unit 14 live-read incident are recorded in `docs/releases/0.1.0.md`. Those historical checks are distinct from this fresh candidate run.

## Review and recovery gates

The tested-package marker lists exact report files; it grants no directory-wide exemption. Changes to operative guidance, navigation, helpers, validators, registry or catalog require a fresh reviewed freeze and affected checks. Future report-only handoff updates must stay within the named `docs/releases/remaining-controller-report.md` path.

Maintenance tests cover isolated source/update/rollback fixtures and injected transports. No actual installed plugin was discovered, refreshed or rolled back. Rollback remains subject to immutable identity, exhaustive ownership, fresh approval digest and the recovery limits in `docs/maintenance/rollback.md`. That guide's release-tool-absent sentence describes its earlier checkpoint; the tool now exists. Final review must disposition the inherited documentation and patch-presentation minors without silently changing F3 instructions.
