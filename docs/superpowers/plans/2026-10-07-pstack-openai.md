# pstack OpenAI implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development, recommended, or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a shared personal ChatGPT and Codex plugin that accounts for all 51 upstream skills and their full workflow dependencies, with evidence for supported behavior and honest limits for unavailable execution.

**Architecture:** Extract the pinned pstack subtree into one package. Shared capability references bind workflow operations to tools available in each session. Runtime helpers remain optional, and a file inventory separates source review from host verification.

**Tech stack:** Markdown skills, root Agent Plugins JSON manifest, Python standard-library maintenance checks, and adapted upstream Bun, TypeScript, Node, and shell helpers where execution is supported. No new orchestration server, required MCP integration, or hooks.

**Spec:** [Approved design](../specs/2026-10-07-pstack-openai-design.md), recorded at documentation commit `726a90d1cae31056bbdd0116b2de332669fc45d4`. The user approved the written spec on October 7, 2026, in message `Sentinel_b63fed5d63a881919b3db34f2237f085`. That approval permits this plan, not implementation.

## Global constraints

- The repository is `/Users/digital-hawk/Herd/pstack-openai`.
- "Preserve the full pstack baseline before adding personal customizations."
- "The baseline includes all 51 root skills, all 24 principles, and the support files that make the workflows work."
- Canonical source is `cursor/plugins`, subtree `pstack/`, version `0.15.15`, commit `df581122cde17e6e27686b5a448bde23e4ad4318`.
- Comparison source is `FetchUpstream/pstack-plugin`, version `0.2.0`, commit `ba2205db1f83295154e31abc762f533954f581bb`. It is a 26-skill subset, not the baseline.
- "Full coverage means every upstream workflow has an accounted-for purpose, instructions, dependencies, and acceptance evidence."
- "A missing capability remains visible even when a useful reduced workflow exists."
- Root `plugin.json` uses `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` and `extensions.com.openai.interface`.
- "There is no default MCP server, app mapping, lifecycle hook, or compatibility overlay."
- "Sequential fallback" is labelled "reduced capability" and is never independent workers.
- "Local `.codex/agents/*.toml` configuration is not portable plugin configuration."
- "Broad autonomy language in upstream mode instructions does not override either" user authorization or host permissions.
- "Personal customization begins only after the entire baseline inventory has reviewed dispositions and each host has evidence for supported behavior or explicit blocks."
- Keep `Copyright (c) 2026 Lauren Tan`, the complete MIT permission notice, applicable comparison-port notices, and unofficial lineage.
- No remote creation, push, publishing, installation, credentials, network listener, global settings, or personal customization is an incidental step. Any required setup needs explicit user authorization before it happens.
- Apply pstack unslop to all generated prose. Preserve this approved spec, its baseline counts, and existing documentation history.

## Review focus

These five failure modes need explicit tests in the named tasks. They extend the spec's cases without changing its design.

- A reference escapes the package through `..` or a symlink. Reject the operative reference rather than reading an unrelated file. Task 3.
- A worker returns evidence for an earlier commit. Reject the result even if its summary says PASS. Tasks 4 and 27.
- A pause or retry repeats an external write. Check prior action identity and authorization before any retry. Tasks 4 and 20.
- A helper starts inside a read-only plugin cache. Use an explicit writable data path and never install into the cache. Tasks 12 and 13.
- A rollback combines old skills with a new inventory or user configuration. Restore an immutable package and its inventory together without touching user data. Tasks 26 and 29.

---

## Execution boundaries and task sizing

This plan is not an execution request. Review it and select an execution method first. Implementation starts by reading local instructions again and following Superpowers using-git-worktrees if an isolated worktree is selected. Keep worktrees, fixtures, and task outputs under `~/Herd`. Preserve unexpected user files and do not reset the checkout.

D1 adopts the approved spec's recommendation: retain the active workflow, otherwise use host defaults. When both pstack and Superpowers are explicitly requested, clarify orchestration ownership. D2 adopts full inventory and workflow coverage with per-host limits. D3 selects adapted ports for all existing helpers, with no automatic dependency installation. If later source review disproves feasibility, record the affected branch blocked and bring a concrete design change for review rather than deleting coverage.

The skills, helpers, and operational pack are parts of one package with shared parity contracts. They can be reviewed independently, but a release requires their combined inventory and caller checks. There is no second subsystem or separate product build hidden in this plan.

A leaf row in Tasks 6 through 11 is one small task, with its own test cycle, review, and commit. Do not combine an entire table into one giant skill rewrite. The same rule applies to each playbook row in Tasks 18 through 21. The task numbers identify families; append the row's name to the task ID in the execution record.

No checkbox below is complete yet. Planned test expectations are not observed runtime results.

## Files and contracts

The implementation adds these units. Existing upstream support paths are retained unless the destination map below names a move.

| Path | Responsibility |
| --- | --- |
| `plugin.json`, `LICENSE`, `NOTICE.md`, `UPSTREAM.md` | Package identity, license, and pinned lineage. |
| `skills/<name>/SKILL.md` and adjacent support files | One upstream workflow or principle per leaf, with its own references. |
| `references/host-capabilities.md`, `references/model-roles.md` | Session capability checks and supported model choices. |
| `references/orchestration-contract.md`, `references/workflow-ownership.md` | Assignment, result, retry, write ownership, and coordinator rules. |
| `references/agent-prompts/poteto-agent.md`, `references/agent-prompts/comment-sicko.md` | Portable role instructions, not host custom-agent configuration. |
| `automations/benny/` | Optional operational pack, outside registered root skills. |
| `docs/parity/inventory.json`, `docs/parity/inventory.schema.json` | One record per canonical source file. |
| `docs/parity/evidence.schema.json`, `docs/parity/cases/`, `docs/parity/evidence/` | Behavioral inputs, expected observations, and actual per-host results. |
| `docs/parity/baseline-paths.txt`, `docs/parity/adaptations/`, `docs/parity/support-map.md` | Exact source paths, per-task adaptation fragments, and reviewed support dispositions. |
| `tools/source_inventory.py`, `tools/validate_package.py`, `tools/validate_evidence.py` | Read-only source inventory, package checks, and evidence checks. |
| `tools/compare_upstream.py`, `tools/release_report.py` | Non-destructive update reports and release evidence summary. |
| `tests/` | Standard-library tests for maintenance tools and helper behavior. |
| `docs/testing/`, `docs/releases/`, `docs/maintenance/` | Host test procedure, release support claims, and rollback instructions. |

Use these interfaces consistently. They are development-time checks, not substitutes for actual host tools.

```python
# tools/source_inventory.py
inspect_source(root: Path, commit: str) -> list[dict]
# Records have upstreamPath, upstreamCommit, upstreamSha256, destinationPath,
# disposition, rationale, dependencies, licenseProvenance, adaptationStatus,
# and verification with separate chatgpt and codex status/evidence arrays.

# tools/validate_package.py
validate_package(root: Path, inventory: list[dict]) -> list[str]
# Empty list means structural checks passed, not behavioral parity.

# tools/validate_evidence.py
validate_evidence(record: dict, package_commit: str, root: Path) -> list[str]
# No execution, model selection, or worker independence is inferred here.

# tools/compare_upstream.py
compare_sources(old: list[dict], new: list[dict], adapted_root: Path) -> dict
# Return added, removed, changed, possibleRenames, and conflicts.

# tools/release_report.py
summarize_release(inventory: list[dict], evidence: list[dict], commit: str) -> dict
# Return workflowCoverage, byHost, blockers, staleEvidence, and releasable.
```

An inventory record's `disposition` is `runtime`, `reference-only`, `metadata-replaced`, or `relocated`. Adaptation status is exactly `pending`, `unchanged-reviewed`, `adapted-reviewed`, or `reference-only-reviewed`. Verification status is exactly `not-run`, `pass`, `reduced-pass`, `blocked`, or `fail`. Unknown values are errors. A reference-only disposition never proves the original runtime behavior.

Every evidence record contains `caseId`, `sourcePaths`, `packageVersion`, `packageCommit`, `host`, `hostMode`, `date`, `documentedCapabilities`, `exposedTools`, `successfulOperations`, `permissions`, `input`, `observedOutput`, `artifacts`, `status`, and `limits`. Host is `chatgpt` or `codex`. Models have requested and actual values only when observed, otherwise an explicit unknown. Missing artifacts or a mismatched commit cannot support pass. Denied or unavailable execution uses blocked. Successful sequential fallback uses reduced-pass. Static checks get their own structural result, never invented host pass records.

A case file contains `id`, `sourcePaths`, `prompt`, `requirements`, `expectedFull`, `expectedReduced`, `expectedBlocked`, and `forbiddenClaims`. Evidence links source files and case IDs so support files are checked through their callers.

## Dependency order and safe parallel work

Task 1 precedes everything. Tasks 2 and 3 can develop in isolated outputs after Task 1, with Task 3 accepting the Task 2 manifest before completion. Task 4 depends on Task 3. Task 5 depends on Task 4.

After Tasks 1 through 5 close, leaf rows in Tasks 6 through 11 can run in parallel on disjoint directories. Their briefs include the exact baseline SHA, capability references, and case schema. Each writes its inventory fragment to `docs/parity/adaptations/<task-id>.json`; only the coordinator merges fragments into the shared inventory. A worker never edits `README.md`, `plugin.json`, another skill, or the shared inventory without assigned ownership.

Tasks 12 through 17 own separate helper paths. Task 13 depends on Task 12; Task 14 depends on Task 12; Task 15 depends on Task 4; Tasks 16 and 17 depend on Task 3. Helpers can proceed alongside leaf work. Tasks 18 through 21 wait for the referenced leaves and helpers. Task 22 owns `automations/benny/` and can proceed after Tasks 4 and 11. Task 23 waits for all skill and playbook callers. Tasks 24 and 25 then close support and dependencies. Tasks 26A through 26C can develop their update tools independently after Task 3 but must test the integrated package before completion.

Freeze the runtime package files at an exact commit before host tests. Later evidence-only commits refer back to that tested commit; any changed operative skill, helper, manifest, or reference requires a new test commit and affected reruns. Task 27 is the Codex host gate. Task 28 is the ChatGPT host gate. They use the same frozen package commit and can run independently if both environments and authorization are available. Neither host's result validates the other. Tasks 23B and 23C follow leaf catalog fragments and Task 23. Task 23D follows the canonical documentation, with no remote or publication prerequisite. Task 29 follows all structural and host evidence. Task 30 updates the entry point only after Task 29's actual result.

Serial integration and fresh review happen between dependent tasks. No more workers run than the active host can support. Isolated writers are required for parallel changes; otherwise use serial execution. The recommended method is subagent-driven implementation with fresh per-task review and a final whole-branch review.

## Task 1: pinned source inventory and license provenance

Files: create `tools/source_inventory.py`, `tests/test_source_inventory.py`, `docs/parity/baseline-paths.txt`, `docs/parity/inventory.json`, `docs/parity/inventory.schema.json`, `LICENSE`, `NOTICE.md`, and `UPSTREAM.md`.

Interfaces: produce `inspect_source(root: Path, commit: str) -> list[dict]` and the inventory contract above. Consume the spec's appendices and source pins.

- [ ] Write `test_exact_baseline`, asserting 164 file records, 51 root skill files, 24 principle leaves, 23 poteto playbooks, and exactly three nested Benny skill files.
- [ ] Write `test_provenance_and_archive_boundary`, asserting SHA-256 per file, original MIT copyright, pending adaptation, and not-run host statuses. Reject symlinks and paths outside the extracted source root.
- [ ] Run `python3 -m unittest tests.test_source_inventory -v` and confirm the new module or implementation is missing before building it.
- [ ] Fetch exact-commit source archives into a task-owned research directory under `~/Herd`. Verify the spec's digests `7e76b77c76fca022e17483cdaba0f3efa583043d98ac604d59a20bc22bf5091f` and `4bbbb50a4f97abb85554610870cb7bac68bfb00c3e629813eb27b605f9b66812`. A digest mismatch stops import pending source review, not a silent replacement. Extract only safe paths and inspect source as data, never execute downloaded scripts.
- [ ] Implement `inspect_source` and CLI `python3 tools/source_inventory.py --source <extracted-pstack> --commit df581122cde17e6e27686b5a448bde23e4ad4318 --output docs/parity/inventory.json`. Record both sources and archive digests in `UPSTREAM.md`; write the full MIT license and notice without replacing Lauren Tan's authorship.
- [ ] Run the tests and compare `baseline-paths.txt` with all paths in the spec. Pass only with exact path-set equality. Commit this unit as `build: record pinned pstack baseline`.

## Task 2: shared package discovery

Files: create `plugin.json`, adapt `assets/logo.png`, and create `tests/test_manifest.py`.

Interfaces: consume the inventory and create one root manifest named `pstack-openai`, candidate version `0.1.0`, license MIT, and `extensions.com.openai.interface`. Use the original asset only with recorded provenance. No guessed public repository or website URL.

- [ ] Write `test_one_portable_manifest`, asserting the exact schema URL, identity, version, extension location, root skills convention, and root-relative contained asset reference.
- [ ] Write `test_no_incidental_integrations`, asserting no hooks, MCP server, app mapping, or compatibility overlay exists by default.
- [ ] Run `python3 -m unittest tests.test_manifest -v`, expecting failure before manifest creation.
- [ ] Create the manifest following the [current packaging documentation](https://developers.openai.com/plugins/build/plugins). Recheck the documented schema at execution time. Mark upstream `.cursor-plugin/plugin.json` metadata-replaced in this task's fragment, and preserve source metadata in `UPSTREAM.md`.
- [ ] Run the tests. Require all assertions to pass, then commit as `feat: define shared OpenAI plugin package`.

## Task 3: package and reference validation

Files: create `tools/validate_package.py`, `tests/test_validate_package.py`, `docs/parity/remnant-dispositions.json`, and `tests/__init__.py`.

Interfaces: produce `validate_package(root: Path, inventory: list[dict]) -> list[str]` and CLI `python3 tools/validate_package.py --root . --inventory docs/parity/inventory.json`. A nonempty error list exits 1. Broken JSON or invalid CLI usage exits 2. Add `--scope <upstream-path>` for an individual unit: check its case schema, destinations, and contained references. A dependency on an explicitly inventoried pending local source path is reported as deferred in scoped mode; an undeclared missing reference is an error. Scoped exit 0 means only that the unit has no structural errors, not that deferred dependencies or the full package passed. Unscoped acceptance rejects every deferred reference.

- [ ] Write tests `test_broken_reference`, `test_path_escape`, `test_symlink_escape`, `test_duplicate_root_skill`, and `test_benny_not_registered`. Each malformed fixture produces the exact offending path and a nonzero result.
- [ ] Write `test_deferred_reference_blocks_full_acceptance` and `test_cursor_remnant_needs_disposition`. Operative `Task`, `AskQuestion`, `.cursor` paths, Cursor model defaults, routine APIs, and cloud-only parameters need a reviewed binding or a narrowly scoped source-only explanation. Broad ignore patterns fail.
- [ ] Run `python3 -m unittest tests.test_validate_package -v`, expecting the missing validator to fail.
- [ ] Implement contained-path and Markdown local-reference checks, root discovery checks, inventory status validation, and a remnant report. Cross-package dependencies are explicit inventory dependencies, not broken local paths. Source-only code examples remain distinguishable from instructions.
- [ ] Run the tests and intentional broken-fixture CLI. Expect the broken fixture to exit 1 and the valid fixture to exit 0. Commit as `test: validate package paths and source remnants`.

## Task 4: capability and orchestration contracts

Files: create `references/host-capabilities.md`, `references/orchestration-contract.md`, `references/workflow-ownership.md`, `docs/parity/cases/contracts.json`, `docs/parity/evidence.schema.json`, `tools/validate_evidence.py`, and `tests/test_validate_evidence.py`.

Interfaces: produce the case and evidence records defined above. Assignments contain ID, scope, exact input revision, output owner, isolated output path, role, retry count, terminal status, and evidence links. A maximum of one retry applies to missing required SHA or method evidence.

- [ ] Write tests `test_stale_commit_rejected`, `test_missing_artifact_rejected`, `test_reduced_is_not_full`, and `test_claimed_worker_without_operation`. They reject unsupported pass records and preserve explicit reduced or blocked states.
- [ ] Run `python3 -m unittest tests.test_validate_evidence -v`, expecting missing implementation failure.
- [ ] Implement `validate_evidence` and its CLI `python3 tools/validate_evidence.py --root . --commit <tested-package-commit>`, which reads evidence records under the root, prints each error, and exits 1 on any invalid record or 0 on valid records. Document session discovery for spawn, follow-up, wait, result inspection, stop, file reads, isolated writes, history, execution, and persistence. Each binding records the tool actually exposed and whether it succeeded. No fixed invented tool names.
- [ ] Document immutable assignment IDs, coordinator-only integration, rejected stale revisions, isolated writers, stopped-worker artifacts, and idempotent external-action checks. Explicit pstack owns pstack, explicit Superpowers owns Superpowers, and ambiguity follows D1.
- [ ] Add `contracts` cases for absent workers, denied writes, two workers requesting one path, a cancelled worker, an interrupted external write, and unavailable persistence. Each has full, reduced, blocked, and forbidden-claim expectations.
- [ ] Run the unit tests, validate the case records, and commit as `feat: define capability and evidence contracts`. Host runtime statuses remain not-run.

## Task 5: model roles and portable agent prompts

Files: create `references/model-roles.md`, `references/agent-prompts/poteto-agent.md`, `references/agent-prompts/comment-sicko.md`, `docs/parity/cases/model-roles.json`, and `docs/parity/adaptations/05-model-roles.json`.

Interfaces: consume Task 4's capabilities. Produce role instructions and a role table using `inherit-parent` as the default, with requested model, observed model, supported effort, and fallback disclosure fields. Do not create `.codex/agents` configuration.

- [ ] Write the `model-roles` cases for an unsupported selected model, inherited identical models, unknown actual model, and missing model-enumeration tool. Expected output never implies diversity without evidence.
- [ ] Validate the cases with Task 3's structural checks before drafting prompts. Confirm the new role references are initially missing.
- [ ] Adapt both upstream agent prompts. Preserve full poteto-mode reading and scope-bound comment review. Use the [subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) as context, not proof that the current personal session has those tools.
- [ ] Validate the references and review prompts against the two original files. Commit as `feat: adapt role prompts and model selection`. Model and worker runtime claims remain unverified.

## Tasks 6 through 11: each skill gets its own reviewed port

Each row below is one task instance. Its files are `skills/<name>/SKILL.md`, every adjacent source support file from spec Appendix B, `docs/parity/cases/skills/<name>.json`, `docs/parity/adaptations/<name>.json`, and `docs/catalog/skills/<name>.json`. Each catalog record has name, kind, purpose, triggers, inputs, outputs, one ordinary example, dependencies, capability limits, source paths, and case IDs. It describes the reviewed leaf, not a promised runtime result. Task 16 owns `show-me-your-work/scripts/log.sh`; its caller is Task 11. The helper and playbook tasks own poteto-mode executable and playbook paths. Do not double-edit those paths from the leaf task.

Interfaces: consume Tasks 1 through 5, produce the case contract and one adaptation fragment per source file touched. Keep descriptions and invocation aliases faithful to upstream. Port the source leaf first, then use the comparison port only for a reviewed useful fallback. Each fragment identifies changed semantics and required capabilities. No personal preference additions.

Apply this five-step cycle separately to every row:

- [ ] Write its case file with the exact named behavioral assertion below, a missing-capability branch where applicable, and forbidden unsupported claims. Read the entire original skill and each cited support file first.
- [ ] Run `python3 tools/validate_package.py --root . --inventory docs/parity/inventory.json --scope skills/<name>/SKILL.md` to demonstrate the new case's required skill or reference is still absent or incomplete. Structural failure is the initial failing check; it is not a behavioral model test.
- [ ] Copy or adapt the leaf and its assigned support files. Bind execution and integration requirements to Task 4's contract. Preserve its purpose, output contract, review gates, and all relevant principle meanings. Run unslop.
- [ ] Run the same scoped package check and review the case's expected observations against source. Record deferred local dependencies explicitly; Task 24 must close them before package acceptance. A source review can set adapted-reviewed or unchanged-reviewed, but cannot set a host pass. Save host behavior for Tasks 27 and 28.
- [ ] Commit that leaf and its fragment as `feat: port <name>` after its own fresh review. Stop that leaf if a required source contract cannot be preserved.

### Task 6: principles about design and scope

Dependencies: Tasks 1 through 5. These rows can run independently.

| Leaf | Named case and required observation |
| --- | --- |
| `principle-laziness-protocol` | `smaller-solution`: remove an unnecessary abstraction while preserving required behavior. |
| `principle-foundational-thinking` | `shape-first`: identify core data and ownership before logic. |
| `principle-redesign-from-first-principles` | `new-requirement`: redesign the affected structure rather than stack a workaround. |
| `principle-attack-the-premise` | `repeated-failure`: question a shared premise after two fixes fail the same check. |
| `principle-subtract-before-you-add` | `dead-path`: remove obsolete behavior before adding the replacement. |
| `principle-minimize-reader-load` | `trace-load`: reduce indirection in a concrete hard-to-follow path. |
| `principle-outcome-oriented-execution` | `migration-end-state`: converge on the named target without keeping throwaway states. |
| `principle-experience-first` | `user-tradeoff`: choose the user outcome with a concrete reason rather than implementation convenience. |
| `principle-exhaust-the-design-space` | `alternatives`: compare distinct approaches. Without execution, label untested proposals. |
| `principle-build-the-lever` | `repeatable-change`: propose or build a rerunnable tool and distinguish proposed from executed proof. |

### Task 7: principles about boundaries and shared state

Dependencies: Tasks 1 through 5. These rows can run independently.

| Leaf | Named case and required observation |
| --- | --- |
| `principle-model-the-domain` | `state-shape`: express valid state transitions in a concrete domain structure. |
| `principle-boundary-discipline` | `invalid-input`: validate external input at its boundary without duplicating internal guards. |
| `principle-type-system-discipline` | `invalid-state`: make an invalid typed state unrepresentable or identify the actual language limit. |
| `principle-make-operations-idempotent` | `replay`: a retry converges without replaying an external side effect blindly. |
| `principle-migrate-callers-then-delete-legacy-apis` | `caller-migration`: update all callers and remove the old API in one reviewed unit. |
| `principle-separate-before-serializing-shared-state` | `two-writers`: isolate writable output before considering locking. |

### Task 8: principles about verification and delegation

Dependencies: Tasks 1 through 5. These rows can run independently.

| Leaf | Named case and required observation |
| --- | --- |
| `principle-prove-it-works` | `false-success`: reject completion without real artifact evidence. |
| `principle-fix-root-causes` | `symptom-repro`: reproduce and trace the cause before a fix. |
| `principle-sequence-verifiable-units` | `migration-units`: each ordered unit ends in a specific check. |
| `principle-test-behavior-not-implementation` | `empty-function`: a test fails when the function returns nothing. |
| `principle-explain-the-number` | `misleading-speedup`: identify the measured work, sample method, and limiting factor before a speed claim. |
| `principle-guard-the-context-window` | `large-corpus`: narrow or delegate accessible evidence without inventing workers. |
| `principle-never-block-on-the-human` | `reversible-step`: proceed on authorized reversible work while preserving explicit user review gates. |
| `principle-encode-lessons-in-structure` | `repeated-rule`: propose a concrete validator or structural check instead of repeating a prose warning. |

### Task 9: conversational and engineering leaves

Dependencies: Tasks 1 through 5, plus relevant principle leaf references before final review.

| Leaf | Named case and required observation |
| --- | --- |
| `bro` | `plain-restate`: restate the actual last message without adding claims. |
| `unslop` | `prose-rewrite`: remove the upstream pattern examples without changing meaning or adding facts. |
| `technical-writing` | `dense-doc`: preserve named symbols and clear document purpose while removing filler. |
| `typescript-best-practices` | `typed-boundary`: apply the source's concrete typing practices to provided TypeScript and retain its patterns reference. |
| `no-comments` | `legal-header`: retain license and justified public-contract comments while identifying unneeded narration. |
| `tdd` | `red-green`: show a real failing behavior test before the fix. Without execution, mark the proposed sequence unrun. |
| `benchmark-checklist` | `measurement-method`: require workload, sample count, revisions, and confound checks before claiming a measured improvement. |
| `correct` | `user-correction`: follow the source's correction scope and output contract without changing durable skills without permission. |
| `figure-it-out` | `uncertain-result`: investigate accessible evidence and state a concrete limit instead of fabricating a result. |

### Task 10: investigation and design leaves

Dependencies: Tasks 1 through 5 and relevant reviewed principle references.

| Leaf | Named case and required observation |
| --- | --- |
| `how` | `trace-path`: cite actual files along a supplied execution path. If workers are absent, disclose sequential exploration. |
| `why` | `history-evidence`: distinguish source history, shared-record evidence, and inference. Missing connectors are explicit gaps. |
| `teach` | `grounded-explanation`: explain a supplied subsystem using its real names and evidence. |
| `architect` | `boundary-design`: compare candidates and provide ownership and rationale. Without workers, label sequential alternatives. |
| `blast-radius` | `dependent-caller`: find a caller outside the diff and prove or mark unproven the runtime consequence. |
| `interrogate` | `adversarial-review`: preserve the rubric, competing reviewer roles, and lead judgment. Missing independent reviewers limits the claim. |

### Task 11: orchestration, history, and setup leaves

Dependencies: Tasks 1 through 5. `poteto-mode` final review also waits for all other leaves and Tasks 12 through 22.

| Leaf | Named case and required observation |
| --- | --- |
| `arena` | `candidate-cross-review`: two isolated candidates finish before a fresh cross-judge, then parent selection, grafts, and evidence. One survivor means incomplete competition. |
| `swarm` | `partition-and-race`: declare slice or race rule, preserve exact revision and method, retry invalid evidence once, and leave coverage gaps visible. |
| `poteto-mode` | `fresh-worker-mode`: fresh worker reads full mode and applied leaves, follows the chosen playbook, and returns its throughput checkpoint and evidence. |
| `poteto-help` | `route-recipe`: route a concrete request to an existing ported playbook without promising unavailable runtime behavior. |
| `setup-pstack` | `unknown-model`: default to inherited roles. Never write an unverified slug or personal host config as an incidental action. |
| `recall` | `scoped-history`: lock topic, workspace, and time range, use a complete supplied capsule first, and check current state independently. |
| `reflect` | `approval-before-edit`: preserve judgment, tooling, divergent, and synthesis lenses. Show accepted, rejected, and backlog before changes. |
| `automate-me` | `existing-personal-mode`: preserve existing preferences, mark evidence strength, show a draft, and avoid scheduling or remote creation. |
| `show-me-your-work` | `decision-trail`: save an auditable local trail without secrets or unsupported completion claims. |
| `create-verification-skill` | `real-app-contract`: retain the feature-map examples and author a draft tied to actual app controls, with unrun verification marked. |
| `maintain-verification-skill` | `stale-feature-map`: review a supplied changed app contract without silently weakening its proof. |
| `make-bot-ui` | `missing-webhook`: retain the workflow purpose but block execution until explicit provider, secret, and network setup is available. No mandatory credentials for other skills. |

## Task 12: explicit helper dependency checks

Files: adapt `skills/poteto-mode/scripts/bootstrap.ts`, `skills/poteto-mode/scripts/package.json`, and `skills/poteto-mode/scripts/bun.lock`; create `skills/poteto-mode/scripts/bootstrap.test.ts` and `docs/testing/helper-setup.md`.

Interfaces: retain `ensureDependenciesInstalled(): void` for current callers, but change it to a check-only function. Missing or mismatched dependencies produce a setup-required error and nonzero exit. It never installs, restarts, or writes to the package cache.

The [pinned bootstrap](https://raw.githubusercontent.com/cursor/plugins/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/scripts/bootstrap.ts) currently runs `bun install --frozen-lockfile`. The [pinned lockfile](https://raw.githubusercontent.com/cursor/plugins/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/scripts/bun.lock) resolves `commander` to `14.0.0`, `bun-types` to `1.3.14`, and `typescript` to `7.0.2`. Use those exact dependency versions as the initial port pins. Bun's supported runtime version must be recorded from a successful helper run, not inferred from the types package version.

- [ ] Write `missing_dependencies_do_not_install`, `mismatched_lock_does_not_restart`, and `read_only_package_does_not_write`. Each asserts no subprocess installation and no package-directory writes.
- [ ] On an already available Bun runtime, run `bun test skills/poteto-mode/scripts/bootstrap.test.ts`, expecting the old auto-install contract to fail the negative assertions. If Bun is unavailable, record blocked and do not install it implicitly.
- [ ] Replace auto-install behavior with dependency checks. Pin the manifest's two `latest` entries to the resolved versions. Only after separately authorized setup, regenerate and verify the lockfile in a task-owned writable working copy, not the installed plugin cache.
- [ ] Run the tests with the supported dependency copy and record exact runtime versions. Document one explicit setup procedure, its network and filesystem effects, and all blocked branches when skipped. Commit as `fix: require explicit helper setup`.

## Task 13: orchestration store and CLI

Files: adapt `skills/poteto-mode/scripts/orch/store.ts`, `skills/poteto-mode/scripts/orch/orch.ts`, and `skills/poteto-mode/scripts/orch/orch.test.ts`.

Interfaces: preserve the upstream exported store and command interfaces after source inspection. Keep `--store <dir>` and `ORCH_STORE` explicit. Store records are bookkeeping, not evidence that host workers exist or finished successfully.

- [ ] Extend the existing suite with `explicit_writable_store`, `two_isolated_assignments`, `stale_lock_requires_review`, `invalid_revision_cannot_pass`, and `crash_preserves_last_valid_record`. Assert observable files and CLI output, not internal method calls.
- [ ] Run `bun test skills/poteto-mode/scripts/orch`, expecting the new required behavior cases to fail before adaptation.
- [ ] Port store operations with task-owned writable paths and preserve upstream error, ordering, inbox, gate, frontier, and verdict contracts. Do not add a server or synthetic host spawn implementation. Never use force-lock takeover automatically.
- [ ] Run the complete existing and new suite. With a temporary owned store, check `bun skills/poteto-mode/scripts/orch/orch.ts --store <owned-dir> --json init` returns valid initialization JSON and leaves the package tree unchanged.
- [ ] Record the helper's limitations in its adaptation fragment and commit as `feat: port orchestration bookkeeping`.

## Task 14: GitHub watch helper with bounded effects

Files: adapt every file under `skills/poteto-mode/scripts/watch-pr/` listed in spec Appendix B. Keep the upstream CLI, types, policy, rendering, wrapper, and fixture helpers together.

Interfaces: retain the source's exported TypeScript functions and CLI options. Inject or fake the actual GitHub transport in tests. Require explicit repository and exact head revision before a pass or authorized mutation. Preserve finite polling and terminal error reporting.

- [ ] Extend `cli.test.ts`, `github.test.ts`, and `policy.test.ts` with `head_changes_invalidate_verdict`, `authentication_missing`, `poll_budget_exhausted`, `duplicate_action_not_replayed`, and `unauthorized_merge_not_attempted`.
- [ ] Run `bun test skills/poteto-mode/scripts/watch-pr`, expecting the new cases to fail before adaptation.
- [ ] Adapt only host, path, and permission assumptions. The core review policy keeps independent per-PR verdicts and contiguous verified stack behavior. CLI fakes must cover failures and empty responses. No live comment, push, merge, or credential setup is part of helper testing.
- [ ] Run the full suite and `bun run --cwd skills/poteto-mode/scripts typecheck`. Expect exit 0 with no type errors. Real GitHub behavior remains blocked until access and authorization exist.
- [ ] Commit as `feat: port bounded PR status tooling`.

## Task 15: worktree audit without private-history assumptions

Files: adapt `skills/poteto-mode/scripts/worktree-audit.sh`; create `skills/poteto-mode/scripts/worktree-audit.py` and `tests/test_worktree_audit.py`.

Interfaces: the shell wrapper calls the standard-library Python helper. CLI is `worktree-audit.sh --repo <path> --base <ref> [--history-map <json>] [--pr-state <json>]`. Both optional inputs are user-scoped exports with no secrets. Default behavior uses local Git state only. There is no fetch or guessed `main` branch.

- [ ] Write tests `path_with_spaces`, `detached_head`, `missing_base`, `dirty_untracked_work`, and `no_network_or_history_probe`. Assert the JSON report preserves complete paths, dirty state, and unknown values.
- [ ] Run `python3 -m unittest tests.test_worktree_audit -v`, expecting the new interface to be absent.
- [ ] Adapt the [source audit](https://raw.githubusercontent.com/cursor/plugins/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/scripts/worktree-audit.sh) to `git worktree list --porcelain -z` and explicit inputs. Implement `audit_worktrees(repo: Path, base: str, history_map: dict | None, pr_state: list | None) -> list[dict]`. No deletion, private transcript glob, fetch, or remote query occurs inside this audit.
- [ ] Run tests against temporary local repositories. Dirty or unknown worktrees are held for review, never declared disposable from age alone. Commit as `fix: scope worktree audit to explicit inputs`.

## Task 16: decision logs preserve evidence

Files: adapt `skills/show-me-your-work/scripts/log.sh` and `skills/show-me-your-work/references/decision-log-template.tsv`; create `tests/test_decision_log.py`.

Interfaces: preserve the source's documented log fields and positional contract, with an explicit owned output path. Keep decision and evidence links readable, and reject invalid record separators rather than corrupt TSV.

- [ ] Write `test_tab_and_newline_rejected`, `test_missing_output_fails`, and `test_existing_log_is_preserved`. Assert that invalid input writes nothing and valid append retains all previous rows.
- [ ] Run `python3 -m unittest tests.test_decision_log -v`, expecting the required cases to fail on the unchanged helper where applicable.
- [ ] Adapt path and validation behavior without logging secrets or adding a default remote sink. Align Task 11's caller instructions with the real contract.
- [ ] Run the tests and commit as `fix: preserve scoped decision logs`.

## Task 17: pstack plan checks stay separate from Superpowers

Files: adapt `skills/poteto-mode/scripts/check-plan.mjs`; create `tests/test_pstack_plan_check.py` and `docs/parity/cases/pstack-plan-format.json`.

Interfaces: retain positional plan-file input and exit 0 for valid pstack plans, 1 for plan errors, and 2 for usage or missing file. It validates pstack multi-phase plans only. It must not require this Superpowers implementation plan to follow pstack's plan template.

- [ ] Write fixture tests `valid_pstack_plan`, `no_capability_evidence`, `unsupported_ten_lane_claim`, `justified_perf_not_applicable`, and `superpowers_not_rewritten`. Assertions inspect the error and exit code.
- [ ] Run `python3 -m unittest tests.test_pstack_plan_check -v`, expecting new capability-aware cases to fail before adaptation.
- [ ] Adapt hard-coded Cursor model, loop, remote, and unconditional lane assumptions to declared capability and evidence requirements. Preserve ordered verifiable units and independent review requirements when available. Reduced or blocked live verification cannot become full success by checking a box. A justified non-applicable performance check is recorded separately.
- [ ] Run the fixtures with the available Node executable. Record its version only after success. Commit as `fix: validate capability-aware pstack plans`.

## Tasks 18 through 21: each poteto playbook gets a caller check

Each row is one task instance. Files are `skills/poteto-mode/playbooks/<name>.md`, `docs/parity/cases/playbooks/<name>.json`, and `docs/parity/adaptations/playbook-<name>.json`. Source path names are exact. Task 21 also owns `skills/poteto-mode/references/bugbot-triage.md`.

Interfaces: consume reviewed leaf skills and actual helper contracts. Produce a playbook case whose sourcePaths include its referenced prompts and helpers. Use inherited model roles unless selection is supported and observed.

Apply this cycle separately to each row:

- [ ] Read the complete original playbook and write the named caller case below, including missing capability and forbidden completion claims.
- [ ] Run scoped validation for `skills/poteto-mode/playbooks/<name>.md` and confirm its operative helper bindings or references are initially missing or still Cursor-specific.
- [ ] Adapt the playbook to the shared contract. Preserve its gates and expected artifact. Read-only tests use fixtures. External writes remain conditional on actual authorization.
- [ ] Run the same scoped structural check and review the complete scenario against the source. Record any deferred dependency for Task 24 to close. Save unresolved runtime limits in the adaptation fragment and leave host statuses not-run.
- [ ] Commit the reviewed playbook as `feat: port <name> playbook`.

### Task 18: building and investigation playbooks

Dependencies: Tasks 6 through 11 and any helper the specific playbook calls.

| Playbook | Named case and required observation |
| --- | --- |
| `feature` | `verifiable-feature`: checkpoint, implementation units, and evidence match the user outcome. |
| `refactoring` | `preserved-behavior`: behavior checks survive the structural change. |
| `bug-fix` | `reproduce-before-fix`: exact symptom exists before the bounded root-cause fix and is absent afterward. |
| `perf-issue` | `comparable-revisions`: workload and revision evidence support the performance claim. |
| `investigation` | `read-only-answer`: accessible sources support the answer without starting a product build. |
| `prototype` | `throwaway-probe`: a concrete question and bounded probe decide the choice. The prototype remains labelled throwaway. |
| `hillclimb` | `bounded-improvement`: each candidate uses the same valid metric and respects the stopping rule. |

### Task 19: proof and authoring playbooks

Dependencies: reviewed caller leaves and Tasks 13, 16, and 17 where used.

| Playbook | Named case and required observation |
| --- | --- |
| `eval` | `discriminating-eval`: the eval separates a known good and known bad output before trusting its score. |
| `runtime-forensics` | `accessible-trace`: trace actual runtime evidence and distinguish absent telemetry. |
| `trace-forensics` | `trace-provenance`: retain exact trace identity, order, and source links. |
| `visual-parity` | `real-render`: inspect actual rendered output. Missing controls block a visual pass. |
| `authoring-a-skill` | `supported-authoring`: use an available authoring workflow, inspect its validator, and leave unknown trigger performance unverified. |
| `multi-phase-plan` | `units-and-proof`: name files, dependencies, unit, live, and applicable performance evidence, then run the adapted pstack checker. |

### Task 20: coordination and continuation playbooks

Dependencies: Task 4, Task 11, and Tasks 12 through 17.

| Playbook | Named case and required observation |
| --- | --- |
| `orchestrate` | `unit-state`: isolated ownership, exact revisions, inbox drain, and gates match real worker results. |
| `autonomous-run` | `no-persistent-tool`: save a continuation brief rather than promise work after the turn. |
| `autopilot-full` | `authorized-program`: retain user review gates and real durable status without invented scheduling. |
| `autopilot-stack` | `stack-resume`: verify every resumed PR revision and prior action before another write. |
| `pause-safely` | `interrupted-action`: preserve worker outputs and side-effect identity. Unknown prior write completion blocks an automatic replay. |
| `session-pickup` | `resume-revision`: load scoped continuation state and compare it with actual live state before acting. |

### Task 21: PR handling and cleanup playbooks

Dependencies: Task 11 and Tasks 14 and 15. Read-only fixtures precede any live integration.

| Playbook | Named case and required observation |
| --- | --- |
| `opening-a-pr` | `draft-only-authorized`: prepare reviewable content and create a draft only with real authorization and access. |
| `babysit` | `bounded-poll`: declare mode, triage review evidence, stop at the budget, and disclose unknowns. |
| `shipping` | `contiguous-verified-stack`: exact revisions and independent per-PR verdicts govern the authorized merge sequence. |
| `worktree-cleanup` | `owned-safe-cleanup`: preserve dirty and unrelated worktrees. Removal follows recorded evidence and the applicable user gate. |

## Task 22: optional Benny operational pack

Files: adapt all 12 source files under `automations/benny/` from the spec; create `docs/parity/cases/benny.json`, `docs/parity/adaptations/benny.json`, and `docs/testing/benny-readiness.md`.

Interfaces: consume scoped channel, tracker, repository, control adapter, feature map, and authorized trigger capabilities. The pack is not part of `skills/`. User configuration and secrets live outside copied pack paths.

- [ ] Write `benny` cases for missing coordinates, missing adapter, existing fix ownership, an existing PR that already fixes the symptom, duplicate report, untrusted triage marker, and unsupported trigger. Expect blocked setup or verification of the existing fix rather than competing work.
- [ ] Validate cases and demonstrate unresolved Cursor setup instructions before adaptation.
- [ ] Adapt `FOR_AGENTS.md`, all three nested `SKILL.md` files, both templates, configuration example, README, and all nested references. Preserve exactly one source-thread reply, immutable coordinates, bounded repro and fix, and draft-only PR behavior. Remove automatic `.cursor/settings.json` writes and Cursor routine assumptions.
- [ ] Review harmless readiness checks for every required connector. Sending messages, filing tickets, creating automations, and creating PRs each need actual authorization. Missing setup affects only Benny. Confirm all three operational skills remain outside root discovery.
- [ ] Run package checks and commit as `feat: port optional Benny operational pack`. Live connector cases remain blocked or not-run until separately set up.

## Task 23: guides and user-visible capability limits

Files: adapt all 11 Markdown files and six images under `docs/guide/` from the spec; create `docs/testing/host-matrix.md` and `docs/parity/adaptations/guides.json`.

Interfaces: consume the actual reviewed skill and playbook paths. Produce one shared guide describing full, reduced, and blocked branches without separate host skill forks.

- [ ] Write `docs/parity/cases/guides.json` with cases for ordinary ChatGPT without execution, worker-enabled ChatGPT, local Codex, absent GitHub access, and optional setup skipped.
- [ ] Run validation and confirm operative Cursor links or unavailable features are caught.
- [ ] Adapt each guide to real capability discovery, explicit setup, current package paths, and the ownership rule. Retain image attribution and do not use a diagram to imply tools exist.
- [ ] Check every local link and example path. Read the setup and overnight guides with the missing-capability cases in view. Commit as `docs: explain shared workflows and host limits`.

## Task 23B: complete generated skill and principle catalog

Files: create `tools/build_catalog.py`, `tests/test_catalog.py`, `docs/catalog/schema.json`, `docs/skills/README.md`, `docs/principles/README.md`, and generated `docs/skills/<name>.md` for each of the 51 leaves. Consume `docs/catalog/skills/<name>.json` records produced by individual leaf tasks. Add no registered root skills.

Interfaces: `build_catalog(root: Path, inventory: list[dict], entries: list[dict]) -> dict[str, str]` returns destination Markdown paths and rendered contents. CLI `python3 tools/build_catalog.py --root . --check` compares rendered text with tracked output and exits 1 for drift. Without `--check`, it writes only generated catalog paths.

- [ ] Write `test_catalog_exact_name_sets`, `test_catalog_required_fields`, `test_catalog_stale_generation`, and `test_catalog_example_case_link`. Assert exactly 51 skills and 24 principles, all required fields, no extra skill, and at least one grounded example with a matching behavioral case per leaf.
- [ ] Run `python3 -m unittest tests.test_catalog -v`, expecting the new renderer to be absent.
- [ ] Implement generation from reviewed catalog entries and the parity inventory. Give each page its purpose, triggers, required input, output contract, example, dependencies, and full, reduced, or blocked host limits. Cite the upstream pin and tested release evidence. A not-run result remains visible.
- [ ] Generate the catalog, run `python3 tools/build_catalog.py --root . --check`, and validate all local links. Read every example against its owning skill case. Commit as `docs: generate complete skill and principle catalog`.

## Task 23C: README navigation, separate setup, and walkthroughs

Files: create `docs/setup/chatgpt.md`, `docs/setup/codex.md`, `docs/workflows/arena.md`, `docs/workflows/swarm.md`, `docs/workflows/poteto-mode.md`, `docs/workflows/choosing-a-workflow.md`, `docs/troubleshooting.md`, `docs/compatibility.md`, and `docs/parity/cases/documentation-walkthroughs.json`. Task 30 owns the final README links.

Interfaces: consume catalog pages, host contracts, update CLI, and real host test records. `docs/compatibility.md` is a release-specific summary generated or checked against evidence, not a list of assumed product capabilities.

- [ ] Define cases `chatgpt-setup-from-readme`, `codex-setup-from-readme`, `arena-walkthrough`, `swarm-walkthrough`, `poteto-walkthrough`, and `upstream-update-walkthrough`. Each specifies the user's starting state, exact documented action, visible expected result, and missing-capability alternative.
- [ ] Validate the cases before writing the pages. The initial absent destinations must fail navigation checks.
- [ ] Write separate host setup guides using the currently supported loading method, labelled unverified until Tasks 27 and 28 exercise it. Explain any explicit setup authorization, installed-copy identity, optional dependencies, and removal or refresh effects. Do not embed assumed local paths as universal ChatGPT steps.
- [ ] Write orchestration examples around disposable local artifacts, including candidate and judge phases, partitioning and gaps, mode routing, workflow ownership, and evidence-backed completion. Link the actual update check, prepare, apply, release validation, conflict, and rollback guide.
- [ ] Add troubleshooting for unavailable skills, missing workers or execution, stale caches, rejected model choices, broken references, missing integrations, update conflicts, and stale verification records. Link each symptom to a bounded check and an honest capability limit.
- [ ] Validate links, CLI usage examples, and catalog coverage. Tasks 27 and 28 must follow these instructions in fresh real host sessions and attach observed evidence. A host setup walkthrough not run remains blocked or not-run, never confirmed from a link check. Commit as `docs: write host setup and workflow walkthroughs`.

## Task 23D: optional GitHub Wiki export without publication

Files: create `tools/export_wiki.py`, `tests/test_wiki_export.py`, and `docs/maintenance/wiki-publication.md`.

Interfaces: `export_wiki(root: Path, output: Path) -> list[Path]` exports canonical docs to an explicitly task-owned empty directory. CLI `python3 tools/export_wiki.py --root . --output <owned-directory>` produces `Home.md`, skill and principle pages, workflow pages, setup pages, troubleshooting, maintenance, and compatibility pages. It never invokes GitHub, enables Wiki, or pushes.

- [ ] Write `test_wiki_catalog_complete`, `test_wiki_links_resolve`, `test_existing_output_not_overwritten`, and `test_no_network_or_settings_changes`. Assert all 51 pages, both host setup guides, and every overview link survive export.
- [ ] Run `python3 -m unittest tests.test_wiki_export -v`, expecting the exporter to be absent.
- [ ] Implement link conversion for GitHub Wiki page names while keeping the repository docs canonical. Include source package version and commit in the export. No hand-maintained second documentation tree.
- [ ] Run the export into an owned fixture directory and check links. Document publication as an optional later user-authorized operation after remote, visibility, Wiki availability, and desired content are reviewed. A private repo's Wiki availability must be checked rather than assumed. Commit as `docs: prepare optional Wiki export`.

## Task 24: complete 164-file support reconciliation

Files: create `docs/parity/support-map.md` and `tests/test_inventory_closed.py`; merge reviewed fragments into `docs/parity/inventory.json`; adapt `.gitignore` and update `NOTICE.md` and `UPSTREAM.md`.

Interfaces: consume all per-task fragments. Only the coordinator writes the aggregate inventory. New port-specific files get their own provenance section without changing the canonical 164-file count.

The source destination rules are fixed:

- Root skills and adjacent support files retain their paths, subject to the explicit helper and prompt tasks.
- `.cursor-plugin/plugin.json` is metadata-replaced by `plugin.json`.
- `agents/poteto-agent.md` and `agents/comment-sicko.md` relocate to `references/agent-prompts/`.
- Source `README.md` is metadata-replaced by the port entry point while preserving lineage.
- `.gitignore`, `LICENSE`, `assets/logo.png`, all guides, and the complete Benny pack stay accounted for.
- All upstream helpers are adapted runtime files under their source paths. New wrappers and maintenance tools are additional port files, not replacements that erase original records.

- [ ] Add `test_inventory_closed`, asserting one record per exact source path, no pending dispositions, no duplicate destination ownership, all required notices, and evidence or explicit limits for each caller.
- [ ] Run the package tests, expecting reconciliation gaps before the merge.
- [ ] Merge the reviewed fragments, fail on conflicting ownership, close every deferred local reference, and write the support map. Ignore `.upstream/`, task-owned temporary data, and dependency working copies. Do not ignore provenance or evidence.
- [ ] Run package validation. Structural closure can pass while host runtime verification remains not-run. Commit as `docs: close full upstream parity inventory`.

## Task 25: cross-package dependency readiness

Files: create `docs/parity/dependencies.json`, `docs/testing/dependency-readiness.md`, `docs/parity/cases/dependencies.json`, and `tests/test_dependencies.py`.

Interfaces: each dependency record names its caller, required proof, available binding or blocked reason, setup effects, and evidence. Skill names alone are not capabilities.

- [ ] Write `test_no_hidden_dependencies` and `test_missing_control_is_blocked`. Each operative `create-skill`, `deslop`, `control-cli`, `control-ui`, repository tool, and other discovered source dependency has a reviewed disposition.
- [ ] Run `python3 -m unittest tests.test_dependencies -v`, expecting incomplete dependency records to fail.
- [ ] Bind an authoring or control requirement only when an actual available tool or workflow can satisfy its proof. Otherwise mark that execution branch blocked. Document Bun, Node, Python, shell, Git, and integration requirements by branch. No hooks, custom agents, plugins, or credentials install by default.
- [ ] Run the tests and audit source dependency references against all 51 skills and 23 playbooks. Commit as `test: make optional dependency limits explicit`.

## Task 26A: repeatable upstream check and preparation

Files: create `tools/compare_upstream.py`, `tools/sync_upstream.py`, `tests/test_upstream_check.py`, `docs/maintenance/upstream-updates.md`, and `docs/parity/upstream-manifests/df581122cde17e6e27686b5a448bde23e4ad4318.json`.

Interfaces: `compare_sources(old: list[dict], new: list[dict], adapted_root: Path) -> dict` returns added, removed, changed, possibleRenames, and conflicts. The `sync_upstream.py` CLI manages review artifacts, never automatic semantic migration. Candidate commits must be exact 40-character revisions; a moving branch or tag cannot replace the recorded baseline.

- [ ] Write `test_three_way_preserves_adaptation`, `test_added_skill_report`, `test_rename_requires_resolution`, `test_deletion_blocks_acceptance`, and `test_changed_license_report`. Use small synthetic source trees plus one real-shaped upstream leaf edit. Expected results name exact old, new, and adapted hashes and leave working files unchanged.
- [ ] Run `python3 -m unittest tests.test_upstream_check -v`, expecting the new module to be absent.
- [ ] Implement `check --candidate <commit>` to download and inspect the exact candidate in `.upstream/`, verify lineage, and write a complete file and skill report. It fetches only public source data, not a Git remote or dependencies. `prepare --candidate <commit>` builds three-way comparisons of old upstream, candidate upstream, and the adapted package. Exact-byte clean merges can produce draft files, but all semantic adaptations still require review.
- [ ] Persist a review bundle under `.upstream/reviews/<commit>/` with report JSON, Markdown summary, original and candidate hashes, working-package base commit, draft patch, conflict files, and source notice differences. File identity guesses are possible renames, never accepted renames. Require an intentional disposition for every added, deleted, renamed, or changed source file.
- [ ] Run tests and check a representative candidate fixture. Assert both commands leave tracked package content, user customization files, secrets, settings, and the accepted upstream pin unchanged. Commit as `feat: prepare reviewable upstream updates`.

## Task 26B: apply reviewed updates in an isolated checkout

Files: extend `tools/sync_upstream.py`; create `tests/test_upstream_apply.py` and `docs/maintenance/update-resolutions.example.json`.

Interfaces: `apply --review <bundle> --resolutions <file> --worktree <owned-path>` only operates in an explicitly supplied clean task-owned implementation worktree under `~/Herd`. It refuses the user's original checkout or a path it does not own. Resolutions name source path, action, destination, reviewed content hash, rationale, and dependent caller checks. A resolution file documents review; it is not a substitute for actual user authorization.

- [ ] Write `test_stale_working_hash_rejected`, `test_unresolved_conflict_no_write`, `test_user_customization_untouched`, and `test_failure_mid_apply_restores_owned_checkout`. Inject failure between a skill write and inventory write, then assert package and pin return to their pre-apply contents and the review bundle survives.
- [ ] Run `python3 -m unittest tests.test_upstream_apply -v`, expecting the missing safe-apply contract to fail.
- [ ] Implement preflight checks against the bundle's original package commit and every original working-file hash. Apply only resolved files in the owned checkout, preserving destination-only files. Back up owned package paths and restore them on failure. Never reset unrelated files or rewrite user configuration. Retain the old source manifest and add the new one.
- [ ] Invalidate changed-file and dependent-caller evidence. Update `UPSTREAM.md`, hashes, notices, dispositions, and candidate release version together. Run structural checks, helper regression tests, and affected host cases before acceptance. A successful file merge alone cannot accept a new baseline or produce release pass.
- [ ] Run all update tests and commit as `feat: apply reviewed updates with failure recovery`. The user reviews the diff and actual evidence before a new release is accepted.

## Task 26C: upstream regression and rollback rehearsal

Files: create `tests/test_update_regression.py`, `docs/parity/cases/upstream-update.json`, and `docs/maintenance/rollback.md`; extend `tools/sync_upstream.py` with `rollback`.

Interfaces: `rollback --release <package-commit> --worktree <owned-path>` restores an immutable package snapshot and its matching inventory in a clean owned checkout. It validates the snapshot before replacement and never reverts external automations, user data, or installed host settings. Unknown or incompatible runtime-state migrations block automatic rollback.

- [ ] Write `test_update_breaks_reference`, `test_update_changes_capability_claim`, `test_rollback_package_and_inventory_match`, and `test_missing_previous_release_preserves_current`. Assert broken candidate references or evidence cannot be accepted and failed rollback leaves the current package intact.
- [ ] Run `python3 -m unittest tests.test_update_regression -v`, expecting the new rollback behavior to be missing.
- [ ] Implement rollback by the same preflight, owned-path, backup, and failure-restoration rules as apply. Record prior release identity, state compatibility, and actual package hash. Never use a destructive reset of the user checkout.
- [ ] Rehearse check, prepare, review, apply, failed validation, and rollback on a representative fixture containing a modified leaf, added skill, renamed reference, deleted support file, and modified notice. Preserve an OpenAI adaptation and a destination-only personal customization file throughout. Assert failed update and interrupted recovery retain both user content and the old working package.
- [ ] Commit as `test: prove upstream update and rollback recovery`. This proves fixture behavior, not unattended semantic migration or installed-host rollback.

### Update entry commands planned for users

These commands do not exist yet. They are the implementation target, not commands run during planning. Run them from the package repository after the plan is implemented and reviewed.

```sh
python3 tools/sync_upstream.py check --candidate <exact-upstream-commit>
python3 tools/sync_upstream.py prepare --candidate <exact-upstream-commit>
python3 tools/sync_upstream.py apply --review .upstream/reviews/<commit> --resolutions <reviewed-json> --worktree <owned-checkout>
python3 tools/validate_package.py --root <owned-checkout> --inventory <owned-checkout>/docs/parity/inventory.json
python3 tools/release_report.py --root <owned-checkout> --commit <tested-package-commit> --version <candidate-version>
python3 tools/sync_upstream.py rollback --release <previous-working-package-commit> --worktree <owned-checkout>
```

Check and prepare produce a reviewable report. Apply requires reviewed conflict resolutions and does not release anything. Release validation waits for compatibility and regression evidence. Rollback restores the package and inventory together. The guide must show one complete update example, explain every output path, and state which steps require human review. Conflicts, renames, and deletions never disappear into an automatic copy operation.

## Task 27: Codex behavioral verification

Files: create `docs/testing/codex.md` and actual records under `docs/parity/evidence/codex/`; update Codex statuses in `docs/parity/inventory.json` only from checked evidence.

Interfaces: consume the frozen candidate package commit, all cases, and Task 4's evidence contract. Setup or installation is a separate user-authorized step, not implied by implementing source files. Use the actual personal Codex environment only when it is available.

- [ ] Review the loading method with the user before installation or settings changes. If setup is unavailable or declined, mark discovery and dependent runtime cases blocked and retain the reason. Do not label direct file reads as installed-plugin discovery.
- [ ] In a fresh session, record the exposed capabilities and verify actual discovery of all 51 root skills and exclusion of the three operational Benny files. Follow `docs/setup/codex.md` from README in a fresh host walkthrough and save actual discovery and installed-copy evidence. Run every leaf case, all 23 playbook caller cases, documentation walkthrough cases, and contract cases in disposable owned fixtures with no real external writes.
- [ ] Exercise absent workers, unsupported model, worker dropout, stale SHA, lost evidence, denied execution, shared-output conflict, broken reference, missing optional integration, and both workflow ownership paths. Request actual workers only where the task and host permit them. Do not imitate failures by asserting a pass record without observation.
- [ ] Record each observed result with artifacts, successful operations, permissions, and limits. Validate evidence using `python3 tools/validate_evidence.py --root . --commit <tested-package-commit>`. Pass requires real artifact inspection; denied actions remain blocked.
- [ ] Review results against source and commit as `test: record Codex workflow evidence`. If any required branch cannot run, preserve explicit blocked status and report that limitation.

## Task 28: personal ChatGPT behavioral verification

Files: create `docs/testing/chatgpt.md` and actual records under `docs/parity/evidence/chatgpt/`; update ChatGPT statuses from checked evidence only.

Interfaces: consume the same tested package commit as Task 27. Distinguish ordinary conversation, worker-enabled mode, and any accessible execution environment. Do not transfer Codex passes into ChatGPT.

- [ ] Use a separately authorized supported personal-host loading method. If none is available, record blocked discovery. Do not claim every ChatGPT mode supports local plugins or custom agents.
- [ ] Follow `docs/setup/chatgpt.md` from README in a fresh host walkthrough and record the real result. Run all 51 leaf cases, 23 caller cases, and documentation walkthrough cases in the available ChatGPT mode. In ordinary conversation, confirm execution-dependent cases report unproven runtime or blocked and sequential lenses report reduced capability. Pure reasoning cases still need actual observed outputs.
- [ ] Where workers and execution are genuinely available, test arena competition and delayed cross-review, swarm partitioning and race rules, poteto coordination, cancellation, isolated artifacts, and missing model choices. Unavailable modes remain explicit blocks rather than fabricated coverage.
- [ ] Exercise history privacy, digest fallback, reflect approval, automate-me draft preservation, missing webhook setup, and unauthorized connector actions. No real message or credential operation is required for these negative tests.
- [ ] Save and validate evidence with Task 27's command and the same package commit. Commit as `test: record ChatGPT workflow evidence`. Make discovery and runtime limitations prominent in the host guide.

## Task 29: release validation and installed-copy rollback boundaries

Files: create `tools/release_report.py`, `tests/test_release_report.py`, `docs/releases/0.1.0.md`, and `docs/testing/release-checklist.md`; update candidate metadata only when validated.

Interfaces: `summarize_release(inventory: list[dict], evidence: list[dict], commit: str) -> dict` returns workflowCoverage, byHost, blockers, staleEvidence, and releasable. CLI `--root`, `--commit`, and `--version` prints the report, exits 0 for a candidate ready under its declared support policy, and exits 1 for unmet acceptance. It creates no remote, tag, upload, installation, or release automatically.

- [ ] Write `test_not_run_is_not_coverage`, `test_blocked_is_not_pass`, `test_mixed_package_versions_rejected`, and `test_stale_evidence_invalidated`. A summary must expose every limitation; it cannot collapse reduced-pass into full orchestration. `releasable` is true only when the source inventory has no pending or conflicting disposition, both hosts have observed package discovery, every required case has a validated result, no claimed supported branch is fail or not-run, and all unavailable branches are explicitly blocked. Declared reduced-pass and blocked optional execution remain visible and never count as full runtime parity.
- [ ] Run `python3 -m unittest tests.test_release_report -v`, expecting the missing summarizer to fail.
- [ ] Implement the report and run `python3 -m unittest discover -s tests -v`, all available helper suites, package validation, evidence validation, and update regression tests. Structural results and host behavior remain separate.
- [ ] Resolve all pending source dispositions and failed required cases. Full workflow coverage requires the 51 leaf and 23 playbook records, caller checks for all 113 support files, and observed supported behavior or explicit blocks in both hosts. If an entire host cannot be tested, report a candidate incomplete for host verification rather than calling it release-ready.
- [ ] Write release notes naming exact upstream lineage, package commit, port version, dependency versions actually tested, full or reduced host branches, unavailable features, and rollback limits. Verify any installed copy's version only with real access and separately authorized setup or refresh. No installed-copy rollback is claimed from a source fixture test.
- [ ] Obtain final whole-branch review of package, inventory, tests, capability claims, attribution, and update recovery. Commit as `docs: report validated port release candidate`. An immutable local tag or actual release needs a later explicit request.

## Task 30: entry point and next-stage handoff

Files: update `README.md`; create `docs/maintenance/customization-boundary.md`.

Interfaces: consume the actual release report. Do not generate a personal mode in this baseline implementation.

- [ ] Link both host setup guides, the complete skill and principle catalog, orchestration walkthroughs, workflow choice, troubleshooting, release compatibility, parity report, and the update entry workflow from README. Every command must correspond to an implemented CLI and explain whether it checks, prepares, applies, or validates a release.
- [ ] Document the full-baseline requirement before customization and the separate personal mode, provenance, and changelog boundary. Upstream updates never own personal settings, modes, or secrets.
- [ ] Run package link checks and `git diff --check`. Require a clean reviewed documentation diff with no unsupported runtime claims.
- [ ] Commit as `docs: publish port entry and maintenance workflow`. Return the tested package revision, full and reduced coverage, blocked branches, and any separately requested setup still needed. Do not push or install as a closing action.

## Acceptance and coverage map

| Approved design requirement | Owning tasks |
| --- | --- |
| Standalone shared package and modern manifest | 1, 2, 3 |
| Canonical source pins, comparison lineage, MIT and notices | 1, 24, 26A through 26C, 29 |
| All 51 skills and 24 principles | Each row in 6 through 11; 24, 27, 28 |
| All 113 support files and 23 playbooks | 5, 12 through 24 |
| Actual host capability bindings and model limits | 4, 5, 25, 27, 28 |
| Arena, swarm, poteto coordination, worker failure and isolated writes | 4, 11, 13, 18 through 21, 27, 28 |
| Scoped recall, reflect permission, automate-me draft | 11, 27, 28 |
| Optional make-bot-ui and Benny setup | 11, 22, 25, 27, 28 |
| Explicit ownership and ambiguity default | 4, 17, 27, 28 |
| Missing execution, persistence, connectors, or history | 4, 11, 20, 22, 25, 27, 28 |
| Broken references, remnants, and dependency closure | 3, 24, 25, 26C |
| Repeatable reviewed updates and failure recovery | 26A, 26B, 26C |
| Release, versioning, rollback, and evidence-backed completion | 26C, 27, 28, 29 |
| Baseline before personal customization | 24, 29, 30 |
| Complete README and optional Wiki documentation | 23, 23B, 23C, 23D, 27, 28, 30 |

## Plan self-review and remaining gates

Planning self-review completed on 2026-10-07. Automated name-set checks confirmed all 51 skills and all 23 playbooks with no missing or extra names. Local documentation links, balanced code fences, placeholders, unchecked-step state, and whitespace were checked. The original approved spec remains verbatim before labelled addenda. Manual review covered source-file ownership, dependencies, interfaces, command names, failure expectations, license lineage, scope, and unslop. It caught and fixed incomplete-package validation by adding scoped checks with visible deferred dependencies. Every spec acceptance case has an owning task, and static validation cannot produce a host behavior pass.

No implementation test, runtime helper, host installation, connector setup, upstream migration, or rollback has run during planning. The helper source and lockfile inspection only informs the planned ports. Revalidate host documentation and exposed tools at execution time.

There is no unresolved product decision blocking the plan. The reviewed spec's defaults govern ownership and capability limits; helper ports are selected with blocked branches if prerequisites are unavailable. Runtime setup, host loading access, model choices beyond inheritance, and optional integrations remain execution-time capability and permission checks. They are not promises of availability.

The user still needs to review this plan and choose execution. Subagent-driven execution is recommended because each leaf and playbook can be independently checked against source, while shared contracts and host claims need fresh review. Native execution is a lower-cost option with independent whole-branch review at the end. Neither method starts until selected after plan review.
