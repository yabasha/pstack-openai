# Restore a reviewed package snapshot

Rollback restores an immutable package commit and its matching inventory into a clean, owned linked Git worktree under `~/Herd`. It leaves Git HEAD and the index unchanged. Review and commit the resulting diff separately. It never resets the original checkout or operates an installed host.

The package includes inventoried source adaptations and explicitly reviewed port-only files, such as tools, tests, references and documentation. A version 1 ownership document must classify every tracked path in the union of the current and release trees. List package files in `ownedPaths`. List each destination-only customization in `preservedPaths` with a review reason. No directory prefix establishes ownership. Omitted, duplicated, unknown or overlapping paths block the operation. Required inventory destinations, declared dependencies and update provenance cannot be excluded as personal files.

Rollback refuses protected secrets and host configuration paths in the owned list. The current bytes of preserved files survive even when the release commit contains older copies. Ignored files cannot be overwritten by a restored destination. Runtime state, external automations, user data and installed host settings are outside this operation.

## Preconditions and review

The coordinator supplies the linked worktree and its Git-admin `pstack-update-owner.json` marker, as documented by the update tool. The marker identifies the task owner, absolute worktree and current package commit. It asserts ownership; it does not authenticate human approval.

The target must be a full package commit already available locally and an ancestor of current HEAD. Branch names and missing commits fail. The release inventory must match its source manifest. The original canonical manifest must remain intact. A later source pin requires its separately reviewed, hash-bound acceptance receipt. An unaccepted later candidate is not a rollback release.

Passing observations name the frozen operative commit, which precedes the release commit containing their evidence. Such releases must contain `docs/parity/tested-package.json` with exactly `schemaVersion: 1`, `kind: pstack-tested-package`, `testedCommit` and `reportPaths`. The tested commit must be an ancestor of the release. The tool compares the immutable trees, including file modes. Source inventory identity, package version and all other operative bytes must match. Inventory verification may advance after testing.

List every evidence/report file changed after freezing in `reportPaths`. Only explicit JSON, Markdown or text files under `docs/parity/evidence/` or `docs/releases/`, the three exact planned reports `docs/testing/codex.md`, `docs/testing/chatgpt.md` and `docs/testing/release-checklist.md`, plus the validated `docs/parity/upstream-manifests/accepted.json` receipt, may differ. Every exception still requires an explicit `reportPaths` entry. Other `docs/testing/` files, setup guides, helper instructions and navigation are not report exceptions. Inventoried destinations and dependencies cannot be exempted. The provenance document itself may be added after the freeze. Every other tracked path must remain identical, even personal paths between the frozen and release commits. Current personal content after the release still uses the ownership preservation rules. Missing provenance, an unrelated ancestor, changed operative content or a mismatched observation version blocks restoration. Matching observations are validated against the proven tested commit, never the later report commit. Acceptance evidence must be nonempty as well as hash-matching.

Review runtime-state compatibility before writing the ownership document. The only supported declaration is `no-runtime-state-migrations`. This is a reviewer assertion that neither package needs runtime-state migration for this restoration. Unknown, incompatible or migration-required state blocks automatic rollback. The tool neither discovers external state nor runs migrations. Resolve such cases through a separately authorized procedure.

The document has exactly these fields, using actual full commit IDs and a complete path classification:

```json
{
  "schemaVersion": 1,
  "kind": "pstack-rollback-ownership",
  "release": "<previous-package-commit>",
  "packageCommit": "<current-package-commit>",
  "runtimeState": "no-runtime-state-migrations",
  "ownedPaths": ["<sorted-exact-package-paths>"],
  "preservedPaths": {
    "<destination-only-path>": "<reviewed reason to preserve current bytes>"
  }
}
```

This illustrates the shape; placeholder IDs and paths are not executable inputs. Compare both immutable Git trees when making the list. Include changed port-only helpers and every package support file. Treat uncertain ownership as a blocker. Store the reviewed document under `.upstream/rollback/ownership.json`, or outside the worktree, so the checkout stays clean.

## One update and recovery sequence

The commands below run from the package repository. Replace placeholders with reviewed real values. These are procedure examples, not permission to fetch, apply or roll back a live package. Each Python entry point runs through Bun with dependency installation disabled.

1. Run `check` with an exact candidate source commit. It writes `.upstream/reviews/<candidate>/report.json`, source copies, manifests, notice differences and pending resolutions. Inspect every source change, conflict, caller, rename and deletion. Keep the bundle unchanged. To run `prepare` for the same candidate, deliberately move the check bundle to a retained sibling first; the tool refuses to overwrite it.

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","check","--candidate","<source-commit>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","prepare","--candidate","<source-commit>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

2. `prepare` adds exact-byte files under `drafts/` when the original adaptation permits a clean draft. `draft.patch` is a review aid and is never applied. Report and report-schema version 2 bind the accepted baseline. Pending resolutions remain version 1. Copy their decisions into the strict version 2 actionable format in `docs/maintenance/update-resolutions.example.json`. Preserve source artifacts and put manual resolutions under `resolved/`. Review exact hashes, rationale and dependent callers, including paired rename and explicit deletion decisions. Human approval must cover the exact resolution digest and owned worktree.

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","apply","--review","<review-directory>","--resolutions","<reviewed-json>","--worktree","<owned-worktree>","--owner","<task-owner>","--approve-resolutions-sha256","<approved-resolution-digest>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

3. Apply stages candidate files, inventory, version, lineage, notices, baseline path list and candidate manifest. The `<candidate>.apply.json` under `docs/parity/upstream-manifests/` records the review, invalidated sources and pending checks. It never advances `accepted.json`. Validate the staged package, run helper regressions and gather actual affected host observations before separate acceptance. Broken references, unsupported capability claims and invalid host evidence block acceptance. Both hosts remain `not-run` until observations establish otherwise. `release_report.py` is a later implementation unit and is not available at this checkpoint.

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.validate_package","--root","<owned-worktree>","--inventory","<owned-worktree>/docs/parity/inventory.json"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.validate_evidence","--root","<owned-worktree>","--commit","<tested-package-commit>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

4. A failed apply restores its own touched bytes after caught failures. A staged candidate that fails later validation remains unaccepted. Retain its diff and evidence for review. Rollback requires a clean committed current snapshot; authorize any local staging commit separately and do not label it a release. Refresh the owner marker to that current commit. Retain the prior working package commit. Review the exhaustive ownership document and runtime-state assertion.

5. Preview rollback without an approval flag. The tool validates the immutable release and outputs a JSON `plan` and `planSha256` on standard output. It writes no package files. Retain that output under `.upstream/rollback/preview.json`. The plan lists every owned path, before/after hashes and modes, preserved paths with reasons, current and target package digests, state assertion, ownership digest and both package identities. Human approval covers this exact plan and worktree.

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","rollback","--release","<previous-package-commit>","--worktree","<owned-worktree>","--owner","<task-owner>","--ownership","<ownership-json>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

6. Repeat with `--approve-plan-sha256 <approved-preview-digest>`. The tool recomputes the entire plan and rejects stale approval before writes. The result on standard output includes `actualPackageSha256`, which must match `releasePackageSha256`, plus the approval digest. Save this result outside the owned write set. Review the restoration diff before any separately authorized commit. Rollback does not accept, release, install or reload the package.

## Recovery limits

Preflight rejects dirty worktrees, missing releases, unsupported schemas, snapshot/inventory mismatches, unsafe paths, links, shared hardlinks and invalid release references. The snapshot validator uses the installed maintenance contracts; incompatible old schemas need a reviewed migration rather than an automatic restore. Passing inventory claims require matching host evidence. Historical unreferenced evidence makes no new support claim.

The transaction backs up every owned file's bytes and mode in memory before replacement and writes inventory last. Caught exceptions, including a caught interruption, restore the original owned files and remove directories created by that attempt. A post-write digest checks the actual restored package.

Recovery assumes the process can still write its backups. It does not cover power loss, an uncatchable process kill, storage failure during recovery or hostile concurrent filesystem replacement. Readers can observe intermediate file changes. Preserve immutable commits and review artifacts for manual recovery if those limits matter. No automatic destructive reset is available.

`tests/test_update_regression.py` rehearses a modified leaf, added skill, renamed reference, deleted support file and modified notice through injected source responses. It preserves the portable adaptation and newer private files, restores a changed port-only helper, and proves caught interruption recovery. These fixtures establish structural behavior only.
