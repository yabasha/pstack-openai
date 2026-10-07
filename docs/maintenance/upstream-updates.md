# Upstream update walkthrough

Start from a clean, owned disposable linked worktree beneath `~/Herd`, the current package commit and an exact lowercase 40-character candidate source SHA. [README](../../README.md) links this procedure. The [CLI](../../tools/sync_upstream.py) implements check, prepare, apply and rollback. It has no accept command. Never execute fetched upstream code during review.

## Accepted baseline and source review

The original canonical manifest for `df581122cde17e6e27686b5a448bde23e4ad4318` remains retained and hash-verified. Later check/prepare selects a separately accepted source baseline through `docs/parity/upstream-manifests/accepted.json`. Its strict receipt has schemaVersion 1, kind pstack-accepted-baseline, commit, manifestPath, manifestSha256, packageCommit, evidencePath and evidenceSha256. Evidence must be nonempty and hash-matching. The package commit must be locally available, an ancestor and contain that exact manifest. A staged but unaccepted source pin blocks another update. Apply never writes this receipt.

1. Obtain exact permission for public source fetch before check or prepare. The fetcher contacts only `https://api.github.com/repos/cursor/plugins` and `https://codeload.github.com/cursor/plugins`. It verifies descendant identity, archive digest, complete tree and subtree blob hashes. It rejects unsafe archive members. Run from the package root through Bun:

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","check","--candidate","<exact-source-sha>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","prepare","--candidate","<exact-source-sha>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

2. Check writes a new `.upstream/reviews/<candidate>/` bundle. Open summary.md and report.json, source copies, complete manifests, file/skill changes, notice changes, conflicts, possible renames and callers. Existing bundles are never overwritten. To prepare the same candidate, intentionally move the check bundle to a retained sibling first, or run prepare directly.
3. Prepare supplies exact-byte drafts only where the original adaptation permits them. Report/schema version 2 binds accepted-baseline receipt and evidence digests. Pending resolutions use version 1. draft.patch is a review aid; its inherited no-final-newline limitation means exact drafts/resolved bytes and hashes govern apply. Never apply that patch mechanically.
4. Preserve every original bundle artifact. Copy decisions into the strict version 2 [actionable resolution format](update-resolutions.example.json). Bind reviewSha256, higher candidateVersion, every changed file's disposition, contentPath and reviewedSha256, rationale and dependent callers. Put manual bytes under resolved/. Explicit deletion uses null content/hash. Review both paired rename decisions and all notices. Empty caller lists establish no coverage.

## Exact approved apply and validation

The coordinator creates an isolated linked worktree and its Git-admin `pstack-update-owner.json` marker. It has exactly schemaVersion 1, owner, absolute real worktree and packageCommit. HEAD must match that base and the checkout must be clean except allowed review files. A marker asserts ownership and does not authenticate human approval. Never mark the original repository or claim broad directory ownership.

5. Obtain explicit approval of the exact resolution digest and worktree before apply. The tool validates schemas, immutable review artifacts, accepted baseline, owned destinations, current hashes, complete decisions and callers before writes.

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","apply","--review","<retained-review-directory>","--resolutions","<reviewed-json>","--worktree","<owned-worktree>","--owner","<task-owner>","--approve-resolutions-sha256","<approved-resolution-digest>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

Apply changes the candidate's reviewed files, inventory, version, lineage, notices, baseline paths and candidate manifest. It records `<candidate>.apply.json` and invalidates affected observations. It does not advance accepted.json, install dependencies, reload a host or make a release. Caught failures restore its touched bytes. Power loss, uncatchable kill or hostile concurrent replacement requires manual recovery from retained immutable artifacts.

6. Validate references and schemas, run affected helper regressions in their exact authorized copy and gather fresh affected host observations. Missing tools or permission remains blocked. Use the real version and frozen tested SHA, not a later report commit:

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.validate_package","--root","<owned-worktree>","--inventory","<owned-worktree>/docs/parity/inventory.json"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.validate_evidence","--root","<owned-worktree>","--commit","<tested-package-sha>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.release_report","--root","<owned-worktree>","--commit","<tested-package-sha>","--version","<actual-package-version>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

Release report exits 0 only when root evidence gates establish readiness; exit 1 prints blockers. Full installed discovery requires an actual receipt with all 51 roots, three Benny exclusions, installed identity, version, frozen SHA and three observed discovery operations. A validated sequential reduced-pass can carry complete discovery but never proves independent workers. Link checks and fixture positives are structural only.

7. Separate reviewed acceptance decides whether the candidate becomes the next baseline. Only after validation, evidence review and explicit acceptance authorization, record the strict accepted.json receipt with exact manifest/evidence digests and ancestor package identity. The receipt is a review assertion, not authenticated permission. No CLI or passing structural check automatically accepts. Keep the original canonical manifest. Then check/prepare the next candidate binds that receipt and its digests; unaccepted or tampered baselines stop before proposals.
8. If validation fails, retain the candidate and evidence as unaccepted. Use [rollback](rollback.md) after a separately authorized clean local snapshot commit. Review exhaustive package ownership, preserved personal paths and runtime-state compatibility. Preview the exact rollback plan, approve its digest and recompute before writes. No destructive reset, install or acceptance follows rollback.

## Freeze and observations

Freeze operative bytes, catalog and navigation together. Later reports must identify that tested ancestor through the exact [tested-package marker contract](rollback.md). Named narrow report exceptions and inventory verification may differ; setup, helpers and navigation may not. Record an explicit second freeze after blocked host inventory merge/catalog regeneration, then fresh blocked discovery at that final SHA. Preserve both freeze identities and prior records in Git history. The final handoff must keep final navigation byte-identical or explicitly refreeze.

Expected visible result for `upstream-update-walkthrough` is an inspected source review, exact approved staged diff, validation results and separately reviewed acceptance before the next update. With no fetch/write authorization, an offline fixture rehearsal or read-only review is reduced capability. Missing inputs, conflicts, stale identities, denied setup or invalid host observations blocks the affected stage. Neither helper snapshots nor update fixtures establish a host pass.
