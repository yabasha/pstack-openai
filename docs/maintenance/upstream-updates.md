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
3. Prepare supplies exact-byte drafts only where the original adaptation permits them. Report/schema version 2 binds accepted-baseline receipt and evidence digests. Pending resolutions use version 1. draft.patch is a review aid with explicit no-final-newline markers; exact drafts/resolved bytes and hashes govern apply. Never apply that patch mechanically.
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

Release report exits 0 only when root evidence gates establish readiness; exit 1 prints blockers. Full installed discovery requires an actual receipt with all actual runtime roots declared by destination paths, three Benny exclusions, installed identity, version, frozen SHA and three observed discovery operations. A validated sequential reduced-pass can carry complete discovery but never proves independent workers. Link checks and fixture positives are structural only.

7. Separate reviewed acceptance decides whether the candidate becomes the next baseline. Only after validation, evidence review and explicit acceptance authorization, record the strict accepted.json receipt with exact manifest/evidence digests and ancestor package identity. The receipt is a review assertion, not authenticated permission. No CLI or passing structural check automatically accepts. Keep the original canonical manifest. Then check/prepare the next candidate binds that receipt and its digests; unaccepted or tampered baselines stop before proposals.
8. If validation fails, retain the candidate and evidence as unaccepted. Use [rollback](rollback.md) after a separately authorized clean local snapshot commit. Review exhaustive package ownership, preserved personal paths and runtime-state compatibility. Preview the exact rollback plan, approve its digest and recompute before writes. No destructive reset, install or acceptance follows rollback.

## Freeze and observations

For a statechart change, run `bun --no-install test --timeout 120000 skills/statechart/scripts/test/` after reviewing the adapted helpers. This carries the upstream CI helper-test intent into the port's Bun workflow. Tests requiring Java/TLC must run with a reviewed local jar and Java runtime; skipped tests remain unverified. Renderer tests require separately reviewed local Pele 1.9.0, Mermaid 11.16.0 and jsdom 26.1.0; they never install packages. Missing dependencies are explicit skips. Inspect actual SVGs separately. Both-host completion also requires observed execution, image inspection, real-code reproduction and surviving artifacts under the [statechart execution contract](../../skills/statechart/references/execution.md).

Freeze operative bytes, catalog and navigation together. Later reports must identify that tested ancestor through the exact [tested-package marker contract](rollback.md). Named narrow report exceptions and inventory verification may differ; setup, helpers and navigation may not. Record an explicit second freeze after blocked host inventory merge/catalog regeneration, then fresh blocked discovery at that final SHA. Preserve both freeze identities and prior records in Git history. The final handoff must keep final navigation byte-identical or explicitly refreeze.

Expected visible result for `upstream-update-walkthrough` is an inspected source review, exact approved staged diff, validation results and separately reviewed acceptance before the next update. With no fetch/write authorization, an offline fixture rehearsal or read-only review is reduced capability. Missing inputs, conflicts, stale identities, denied setup or invalid host observations blocks the affected stage. Neither helper snapshots nor update fixtures establish a host pass.

## Reviewed package metadata closure

A complete package also requires `packageMetadata` in its version 2 resolutions. It contains `contentPath`, such as `resolved/package-metadata.json`, and `reviewedSha256`. The out-of-band resolution approval digest binds this reference, which binds every metadata file. Missing or incomplete closure stops before any package mutation. Inventory-only maintenance fixtures exercise a smaller development contract and are not proof of full-package updates.

The referenced JSON has exactly schemaVersion 1, kind `pstack-package-metadata`, inventory, fragmentOwners and files. Supply the complete reviewed candidate inventory with exact candidate source identities and destination mappings. Every host verification must be not-run with empty evidence. Dependencies, dispositions, rationale and license provenance require review. fragmentOwners maps every candidate source path to one `docs/parity/adaptations/<name>.json` owner. Added or removed workflows require explicit reviewed ownership, cases, catalog and dependency changes; apply does not invent them.

Each files entry has path, contentPath and sha256. Exact bytes live under resolved/; deliberate deletions use null contentPath and sha256. Allowed files are the registry, case definitions, catalog inputs and generated pages, dependency audit, remnant dispositions, support map and `docs/parity/baseline-policy.json`. Schemas, code, host evidence and acceptance receipts cannot enter this write set. At minimum supply the registry with all candidate hostStatus values not-run, dependencies and baseline policy. Include regenerated catalog pages and any changed case/catalog definitions or removed pages needed for closure.

Baseline policy declares schemaVersion 1, upstreamCommit, reviewRationale and exact sorted sourcePaths, rootSkills, principles, playbooks and bennySkills arrays. Its membership and source hashes must match the candidate manifest and inventory. It declares reviewed scope, not behavioral readiness. The accepted 0.2.3 source has 184 source files, 57 root skills, 24 principles and 23 playbooks. The original 164-file, 51-root manifest is retained as historical provenance. Future reviewed membership changes do not edit that historical canonical manifest.

Apply checks a complete projected package before mutation, including fragment ownership, source membership, case/catalog coverage, regenerated pages, dependency hashes and references. It writes the active fragments and aggregate in the same caught-failure transaction and retains prior fragments in `<candidate>.previous-fragments.json`. Existing host records keep their old identities and cannot transfer. Candidate registry and inventory become untested. Acceptance remains the separate authorized receipt in step 7 after the actual checks and evidence review. Structural closure does not make the candidate releasable.

The shape below is illustrative; replace the abbreviated inventory and file list with the complete reviewed package data. The [resolution example](update-resolutions.example.json) shows the enclosing digest reference.

```json
{
  "schemaVersion": 1,
  "kind": "pstack-package-metadata",
  "inventory": ["<complete reviewed inventory row objects>"],
  "fragmentOwners": {
    "skills/how/SKILL.md": "docs/parity/adaptations/skill-how.json"
  },
  "files": [
    {
      "path": "docs/parity/case-registry.json",
      "contentPath": "resolved/metadata/docs/parity/case-registry.json",
      "sha256": "<sha256 of exact reviewed bytes>"
    }
  ]
}
```

Compute each file digest after writing its final reviewed bytes, then hash the metadata bundle and place that digest in packageMetadata. Finally hash the full resolutions file for the existing apply approval command in step 5. For example, this read-only command prints a file digest without installing dependencies:

```sh
bun --no-install -e 'const {createHash}=await import("node:crypto"); const bytes=await Bun.file(process.argv[1]).arrayBuffer(); console.log(createHash("sha256").update(new Uint8Array(bytes)).digest("hex"))' /absolute/path/to/review/resolved/package-metadata.json
```

No automatic draft is an approved metadata bundle. Missing new cases, removed case scopes, catalog membership, dependency callers or regenerated outputs fail the projected closure check before writes.

## Non-mutating combined preview

Prepare a combined update from the accepted source receipt, never by accepting an intermediate staged candidate to unlock the tool. Port-owned prerequisite tooling and execution contracts may be committed separately in the isolated implementation worktree. Keep its source inventory and accepted receipt unchanged. Bind prepare to that exact prerequisite commit and retain the separate prerequisite diff.

Before approval, use the preview command with the exact review, reviewed resolutions and ownership marker. It shares the apply preflight and metadata validation, but requires no approval and never writes the implementation package. Supply a new real output directory outside existing repositories and the review tree, with an existing task-owned parent. The command refuses existing outputs and ancestor overlap. Its package projection omits the future apply receipt. The separate preview plan and planned transaction record are proposals, never execution or acceptance evidence.

```sh
bun --no-install -e 'const r=Bun.spawnSync(["python3","-B","-m","tools.sync_upstream","preview","--review","<review>","--resolutions","<reviewed-json>","--worktree","<owned-worktree>","--owner","<task-owner>","--output","<new-external-output>"],{stdout:"inherit",stderr:"inherit"});process.exit(r.exitCode)'
```

Review the prerequisite and complete projected diff, validate the projection, then obtain approval of the reported exact resolution digest and implementation worktree before formal apply. Preview never authorizes apply, setup, baseline acceptance, integration, installation or refresh. Apply rejects any resolution change between approval validation and plan construction.

A version 2 reviewed resolution may declare reviewedMode as 100644 or 100755 for a retained file, and null only for deletion. The digest binds that permission mode as well as the content. Retain-adaptation preserves the original mode. Preview and apply share the same mode interpretation and preview verifies byte and mode readback. Without an explicit mode, existing permissions are preserved and new files default to 0644. Review new executable helpers explicitly; otherwise replay fixtures and command launchers may fail before reaching their intended phase. Apply failure recovery restores the prior bytes and permissions.
