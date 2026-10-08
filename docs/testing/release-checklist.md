# Current F4 candidate and final fix status

The whole-branch review requested five Important corrections and identified 21 Minor findings. This single fix wave implements all 26 findings. The root's one scoped review of the entire fix range is still pending; no review approval or release is claimed.

The actual operative freeze is `d4c05c3e619a085c06d391f45299fe81d99cd7ce`, version 0.1.0. Canonical source remains `df581122cde17e6e27686b5a448bde23e4ad4318`: 164 files, 51 roots, 24 principles, 23 playbooks and 12 Benny files. All 210 host records remain blocked, unavailable and without successful operations. Each host has 105 validated blocked cases, zero passes, zero reduced passes and no observed package discovery. The release decision remains false.

The final source suite passed 207/207 maintenance tests in 161.799 seconds. Exact F4 source was exported to /Users/digital-hawk/Herd/pstack-final-f4-validation; all 726 tracked files retained exact bytes and modes. Bootstrap and strict TypeScript exited zero. The fake-only helper suite passed 92 tests with 346 assertions in 2 seconds. It used only the existing approved dependency snapshot /Users/digital-hawk/Herd/pstack-openai-helper-verification at historical identity `37b68c8e842b275f310ead112c0ecb7fa0ade308`, with Bun 1.4.2, commander 14.0.0, bun-types 1.3.14 and TypeScript 7.0.2. Manifest and lock bytes matched the approved snapshot; dependency/cache bytes, modes and symlink targets remained unchanged. No new dependency setup, installed host, live forge or external action was used.

The fixes distinguish full direct work from reduced sequential substitution, enforce method receipts, exhaust review-thread pages, retain UNKNOWN as unavailable, reject forge BLOCKED even with successful CI, and require reviewed full-package update metadata before writes. Automatic stack discovery explicitly blocks at its 300-open-PR cap. The full-package update fixture performs actual local apply, valid fragment closure, separate synthetic acceptance and next preparation. Fixture acceptance proves source tooling only. It does not establish actual-host acceptance or release readiness.

The first final-wave full run had 202/207 passes, two failures and three errors in 157.982 seconds. The next had 206/207 passes and one fixture error in 163.638 seconds. A stale already-loaded attempt was cancelled with SIGINT and supplies no completed-suite result. After exact fixture correction, the settled pre-refinement suite passed 207/207 in 157.677 seconds. Late case-bound Swarm, anchor and forge BLOCKED refinements prompted the final suite above. The initial working helper run passed 90 tests but failed strict TypeScript; explicit union narrowing corrected it. Earlier RED logs, the synthetic author correction, inert-review471-error scan and all failed attempts remain in the controller's working record. None is relabeled green.

The strict marker retains the same 217 explicit report paths and separate marker exception. Only existing reserved report data changed after F4. The final actual-HEAD identity and rollback-provenance proof is a required next check after committing these reports; this paragraph does not claim that future check has run. Installed-copy rollback, host discovery, worker/model behavior, persistent wake, integrations and external actions remain unverified.

See the [controller handoff](../releases/remaining-controller-report.md) for the full finding dispositions and root decisions.

# Preserved historical report through F3

Everything below records the earlier checkpoints and their then-pending findings. Current status is the F4 section above. Its original test results, incident history and lossless ruling appendix are retained verbatim.

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
