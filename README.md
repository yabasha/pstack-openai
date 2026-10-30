# pstack-openai

An unofficial port of Lauren Tan's pstack. Version 0.2.4 adapts the combined compiler, review and orchestration changes from upstream v0.15.36. Its inventory records 573 source files and 58 canonical roots, including one deferred reference. The runtime package retains 57 skills, 24 principles and 23 playbooks. Read [UPSTREAM.md](UPSTREAM.md), [NOTICE.md](NOTICE.md) and [LICENSE](LICENSE) for lineage and attribution.

The accepted 0.2.4 source baseline is upstream `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`, official version 0.15.36. The [source acceptance record](docs/releases/0.2.4.md) states the completed checks and remaining verification limits. Source acceptance, installed discovery and full workflow qualification are separate gates.

Upstream adds Claude Code packaging; this port retains its shared portable runtime and records the Claude adapter as a quoted reference only.

It also makes `/sharpen` return four framing answers and a rewritten prompt without executing its task. It adds create-formal-verification-skill and maintain-formal-verification-skill, including bounded claims, safe mutation trials and explicit testing fallbacks. Source validation and installed discovery are tracked separately from full workflow behavior. The [0.2.2 source validation record](docs/releases/0.2.2.md) identifies the reviewed snapshot, checks and remaining host limits. Earlier release records retain their historical scope. See [compatibility](docs/compatibility.md) before relying on a workflow.

[Website and examples](https://pstack-openai.yabasha.chatgpt.site) · [Get started](docs/guide/01-setup.md) · [Choose a skill](docs/skills/README.md) · [Compatibility](docs/compatibility.md) · [Documentation](docs/guide/README.md)

- [Personal ChatGPT setup and blocked route](docs/setup/chatgpt.md).
- [Codex setup and unverified documented route](docs/setup/codex.md).
- [Choose a workflow](docs/workflows/choosing-a-workflow.md).
- [Workflow examples, simple to advanced](#workflow-examples).
- [57 runtime skills and one deferred source](docs/skills/README.md) and [all 24 principles](docs/principles/README.md).
- [Preserved guide](docs/guide/README.md).
- [Arena walkthrough](docs/workflows/arena.md), [Swarm walkthrough](docs/workflows/swarm.md) and [Poteto mode walkthrough](docs/workflows/poteto-mode.md).
- [Troubleshooting](docs/troubleshooting.md) and [host test matrix](docs/testing/host-matrix.md).
- [Helper dependency setup](docs/testing/helper-setup.md) and [optional Benny readiness](docs/testing/benny-readiness.md).
- [Upstream check, prepare, apply, validation and separate acceptance](docs/maintenance/upstream-updates.md).
- [Baseline gate and personal customization boundary](docs/maintenance/customization-boundary.md).
- [Conflict resolution format](docs/maintenance/update-resolutions.example.json) and [rollback](docs/maintenance/rollback.md).
- [Package validator](tools/validate_package.py), [evidence validator](tools/validate_evidence.py), [update CLI](tools/sync_upstream.py), [release report CLI](tools/release_report.py) and [catalog renderer](tools/build_catalog.py).
- [Acceptance cases](docs/parity/cases/documentation-walkthroughs.json), [inventory](docs/parity/inventory.json) and [case registry](docs/parity/case-registry.json).
- [Design](docs/superpowers/specs/2026-10-07-pstack-openai-design.md) and [implementation plan](docs/superpowers/plans/2026-10-07-pstack-openai.md).

## What it does

- Routes engineering tasks through a playbook with `poteto-mode`.
- Compares alternative implementations with `arena`, or divides independent work with `swarm` when the host supports workers.
- Explains code and design decisions with `how`, `why`, and `teach`.
- Reviews changes with `interrogate` and checks affected code with `blast-radius`.
- Adds verification workflows and removes formulaic wording with `unslop`.

Candidate navigation is frozen with operative content. The final handoff must keep these bytes unchanged or explicitly refreeze and relink fresh blocked observations. Evidence/report commits can follow the tested commit only under the exact [tested-package marker contract](docs/maintenance/rollback.md). After blocked host records enter the inventory and regenerate the catalog, an explicit second freeze is required. Fresh blocked discovery records must then name that final SHA. No behavioral pass transfers between freezes.

Use [`/statechart`](skills/statechart/SKILL.md) to check a TLA+ model and draw flat, parent or region charts using a reviewed view. The compiler retires automatic chart-to-spec conversion and integrated comparison flags. [Execution prerequisites](skills/statechart/references/execution.md) are explicit; unavailable tools leave verification blocked.

<!-- workflow-examples:start -->

## Workflow examples

Choose a scenario and send its prompts in order. Review each result before continuing. These examples describe intended outputs, not observed host results. Check [compatibility](docs/compatibility.md) for available tools and current verification limits.

Keep one controller responsible for the task. Workers, isolation, tool installation, external actions, and publication require the relevant host capabilities and authorization.

- [Simple](#simple-workflows): start a small project from scratch; add a small feature to an existing app; fix a reproducible bug.
- [Intermediate](#intermediate-workflows): start a project with a deliberate architecture; add a feature across UI and API boundaries; diagnose a bug that spans several components.
- [Advanced](#advanced-workflows): coordinate a migration with independent work; investigate a retry or concurrency failure; review a release before asking to publish.

### Simple workflows

#### Start a small project from scratch

Build a personal reading list with one working user journey before adding accounts or integrations.

Skills: [`sharpen`](skills/sharpen/SKILL.md), [`poteto-mode`](skills/poteto-mode/SKILL.md), [`principle-prove-it-works`](skills/principle-prove-it-works/SKILL.md).

**1. Sharpen the brief**

```text
Use sharpen on this brief: build a local reading-list app where I can add a URL, mark it read, and find it again. Keep the scope small. Leave framework and storage choices open. Return the four framing answers and a rewritten prompt, then stop.
```

Expected output: A clearer brief. Sharpen does not create files or execute the project.

**2. Build one complete journey**

```text
Use poteto-mode to implement the reading-list brief above in this empty project folder. Inspect available tools and agree any unresolved product choices first. Build add, list, mark-read, and search with browser-local storage. Keep this local. Use existing dependencies where possible; ask before installations or external actions.
```

Expected output: A local app with a small, usable scope and a record of implementation choices.

**3. Check the delivered app**

```text
Use principle-prove-it-works on the reading-list app. Add an item through the UI, mark it read, reload, and search for it. Check an empty list and invalid input. Report observed results and anything you could not run.
```

Expected output: Evidence for the actual user journey, including persistence after reload.

Principle in practice: Prove it works: finishing the code is followed by exercising what the user receives.

Completion check: The core journey works locally and its checks are recorded. Deployment is a separate authorized action.

#### Add a small feature to an existing app

Add a status filter to a task list without changing how tasks are stored.

Skills: [`how`](skills/how/SKILL.md), [`blast-radius`](skills/blast-radius/SKILL.md), [`principle-prove-it-works`](skills/principle-prove-it-works/SKILL.md).

**1. Find the current behavior**

```text
Use how to trace this task list from its route through data loading to rendering. Identify status values, existing filter behavior, and relevant checks. Keep this read-only and cite the source files.
```

Expected output: A short map of the code that owns the feature.

**2. Implement the bounded change**

```text
Add an All / Open / Done filter to the existing task list. Follow its current UI conventions and preserve storage and API contracts. Handle empty filtered results. Use blast-radius to inspect affected callers and run the existing focused checks.
```

Expected output: A focused change with caller impact and empty-state behavior checked.

Principle in practice: Subtract before you add: reuse the existing task status and filtering logic before introducing another representation.

Completion check: Each filter displays the right tasks, and clearing it restores the original list.

#### Fix a reproducible bug

A whitespace-only search hides every result instead of showing the full list.

Skills: [`tdd`](skills/tdd/SKILL.md), [`principle-fix-root-causes`](skills/principle-fix-root-causes/SKILL.md).

**1. Reproduce and fix**

```text
Use tdd to fix this bug: a search containing only spaces hides all items; it should behave like an empty search. Find the existing cheap local test target, demonstrate the failure before the fix, trace the input-handling cause, then make the smallest correction and rerun the check. If the test path is unavailable, state that limit instead of inventing a result.
```

Expected output: A failing-before and passing-after regression check, or an explicit account of the missing evidence.

**2. Check neighboring behavior**

```text
Use principle-fix-root-causes to review the search fix. Check empty input, leading and trailing spaces, a real query, and no matches. Confirm that normalization happens at the correct boundary and report the checks actually run.
```

Expected output: A verified correction with nearby behavior covered.

Principle in practice: Fix root causes: correct input handling where the bad state first enters the search flow.

Completion check: The original reproduction passes and normal search still works.

### Intermediate workflows

#### Start a project with a deliberate architecture

Create a small team issue tracker with clear ownership and a repeatable verification workflow.

Skills: [`sharpen`](skills/sharpen/SKILL.md), [`architect`](skills/architect/SKILL.md), [`poteto-mode`](skills/poteto-mode/SKILL.md), [`create-verification-skill`](skills/create-verification-skill/SKILL.md).

**1. Define a useful first release**

```text
Use sharpen on this project brief: a team issue tracker with project lists, issue creation, and status changes. Ask for evidence that the core journey works. Keep authentication provider, framework, hosting, and paid services as open choices. Rewrite the brief and stop.
```

Expected output: A bounded first-release brief and explicit unresolved product choices.

**2. Sketch the design before implementation**

```text
Use architect on the issue-tracker brief. Compare two ownership models for projects, issues, and memberships. Sketch caller usage, types, module boundaries, and allowed issue transitions. Read the available host contracts. Keep this design-only; do not install dependencies or implement yet.
```

Expected output: A concrete design with tradeoffs and an implementation boundary.

**3. Implement the selected slice**

```text
Use poteto-mode to implement the selected issue-tracker design. Start with create-project, create-issue, and change-status as one complete slice. Keep ownership and validation at explicit boundaries. Inspect existing tooling and obtain authorization before adding dependencies or services. Report deviations from the design.
```

Expected output: A working first slice with scoped changes and observed checks.

**4. Leave reusable checks**

```text
Use create-verification-skill for the issue tracker. Inspect the app's real commands and available browser/test tools. Define observable checks for issue creation, status changes, invalid input, and project separation. Run the supported checks and identify unavailable ones. Verify local skill discovery separately from writing the file.
```

Expected output: A project-local verification workflow tied to real entry points.

Principle in practice: Model the domain: represent issue states and membership rules explicitly before wiring screens together.

Completion check: The first slice is usable, its boundaries are reviewable, and another agent can rerun the documented checks.

#### Add a feature across UI and API boundaries

Add project-scoped CSV export without exposing another project's records.

Skills: [`how`](skills/how/SKILL.md), [`architect`](skills/architect/SKILL.md), [`blast-radius`](skills/blast-radius/SKILL.md), [`interrogate`](skills/interrogate/SKILL.md).

**1. Trace access before adding output**

```text
Use how to trace project membership checks, list queries, and file responses in this app. Find the existing authorization boundary and cite its callers. Keep this read-only.
```

Expected output: A map of the access rules the export must preserve.

**2. Design and implement within scope**

```text
Use architect to compare synchronous and queued CSV export for the actual data sizes and existing infrastructure. State the tradeoffs, then implement the simplest supported design for project-scoped issue export. Reuse current membership checks, validate inputs, and handle an empty export. Do not add services or paid dependencies without approval.
```

Expected output: An export implementation whose design matches observed needs.

**3. Review the boundary**

```text
Use blast-radius to trace the export change's callers and authorization assumptions. Use interrogate for an adversarial review of cross-project access and malformed inputs. Exercise the real API with allowed and denied project access. If independent reviewers are unavailable, disclose reduced capability and keep review claims bounded.
```

Expected output: Evidence for allowed exports and denied access, plus unresolved risks.

Principle in practice: Boundary discipline: enforce project access where data leaves the application, using the existing authorization contract.

Completion check: An authorized user can export their project's records; a user without access cannot.

#### Diagnose a bug that spans several components

An issue looks updated in the UI but returns to its old status after a refresh.

Skills: [`how`](skills/how/SKILL.md), [`poteto-mode`](skills/poteto-mode/SKILL.md), [`blast-radius`](skills/blast-radius/SKILL.md), [`show-me-your-work`](skills/show-me-your-work/SKILL.md).

**1. Trace the failed journey**

```text
Use how to trace a status change through the UI, request, validation, database update, and cache refresh. Reproduce the stale-status bug through actual entry points where authorized. Separate observed behavior from hypotheses and retain relevant evidence without secrets.
```

Expected output: A reproduction and a ranked account of where the state diverges.

**2. Fix the owning component**

```text
Use poteto-mode to fix the reproduced stale-status bug at its root cause. Use show-me-your-work to retain a local decision trail. Avoid compensating UI changes if persistence is wrong. Add a focused regression check when practical, run blast-radius on the affected callers, and verify the status after a reload.
```

Expected output: A scoped fix, an inspected user journey, and a reviewable local log.

Principle in practice: Attack the premise: if repeated fixes fail the same check, revisit the shared assumption before adding another patch.

Completion check: The updated status survives a reload, and the evidence identifies the component that caused the failure.

### Advanced workflows

#### Coordinate a migration with independent work

Move a legacy notification system behind one new interface while preserving existing callers.

Skills: [`architect`](skills/architect/SKILL.md), [`swarm`](skills/swarm/SKILL.md), [`blast-radius`](skills/blast-radius/SKILL.md), [`show-me-your-work`](skills/show-me-your-work/SKILL.md).

**1. Set ownership and migration order**

```text
Use architect to map notification callers and design the replacement interface from caller usage. Plan a migration that moves callers before deleting the old API. Identify independent slices, file ownership, integration order, and user-visible checks. Keep implementation paused until the design is reviewed.
```

Expected output: A caller map, selected design, and conflict-aware work plan.

**2. Execute isolated slices**

```text
Use swarm to implement the reviewed notification migration. Assign disjoint caller groups to isolated workers with explicit boundaries; keep one integration owner. Use show-me-your-work for decisions and inspect every worker's terminal result and artifact before integration. If workers or isolation are unavailable, disclose the limit and use a sequential plan without claiming independent execution.
```

Expected output: Integrated changes with actual worker receipts, or an explicitly sequential result.

**3. Remove the old path and verify**

```text
Use blast-radius to find remaining legacy notification callers. Remove the obsolete API only after callers have migrated. Run the checks that observe delivery, failure handling, and retries using isolated test data. Report any integration that could not be exercised.
```

Expected output: A coherent migration with the old path removed and remaining gaps stated.

Principle in practice: Separate before serializing shared state: give workers isolated outputs and one explicit integration point.

Completion check: Callers use the selected interface, obsolete code is removed, and supported journeys pass the recorded checks.

#### Investigate a retry or concurrency failure

Two retrying workers can process the same job and produce a duplicate result.

Skills: [`create-formal-verification-skill`](skills/create-formal-verification-skill/SKILL.md), [`statechart`](skills/statechart/SKILL.md), [`maintain-formal-verification-skill`](skills/maintain-formal-verification-skill/SKILL.md).

**1. Check one important property**

```text
Use create-formal-verification-skill to investigate duplicate job completion under retries. Start from the real claim, lock, and completion code. Choose a suitable verifier, state the property and bounds, and cite the code each model action represents. Use an already authorized local toolchain; do not install tools implicitly. Run deliberate broken-code trials only in an owned disposable copy. If no verifier can run, label any generated-input testing as a testing fallback, not formal proof.
```

Expected output: A bounded verification result or an explicit block, with a runnable local skill when supported.

**2. Explain the failure as a user story**

```text
Use statechart on the job-processing model. Show states in terms of what the operator sees, retain invariants and code-guard citations, and turn each counterexample into a numbered story. Use an authorized local renderer and inspect every SVG. Replay the story through the real application's entry points; distinguish modeled behavior from reproduced behavior. Do not fix product code in this step.
```

Expected output: Mermaid charts, compiler reports and separately rendered SVGs with model scope and reproduction status separated.

**3. Recheck after an authorized fix**

```text
After the job-processing fix is separately implemented and authorized, use maintain-formal-verification-skill to reconcile the verification with the changed code. Preserve the original property, inspect covered functions, rerun checks, demonstrate the check still detects a relevant broken variant in isolation, and advance the sync record only for code actually checked.
```

Expected output: Verification that describes the current implementation, with explicit bounds and remaining findings.

Principle in practice: Explain the number: a model pass covers its stated bounds and assumptions; it is not a claim that the whole production system is correct.

Completion check: The model and real-code evidence are separately reviewable. Missing tools, citations, rendering, or reproduction leave the dependent result incomplete.

#### Review a release before asking to publish

Assess an existing feature branch against its acceptance criteria and user journeys.

Skills: [`interrogate`](skills/interrogate/SKILL.md), [`blast-radius`](skills/blast-radius/SKILL.md), [`maintain-verification-skill`](skills/maintain-verification-skill/SKILL.md), [`technical-writing`](skills/technical-writing/SKILL.md).

**1. Challenge the completed change**

```text
Use interrogate and blast-radius to review this feature branch against the supplied acceptance criteria. Trace affected callers, challenge data and authorization assumptions, and distinguish confirmed defects from untested risks. Report actual reviewer independence and model identity only when observed.
```

Expected output: A prioritized review tied to code and acceptance criteria.

**2. Verify and prepare the handoff**

```text
Use maintain-verification-skill to check whether this project's verification workflow still matches its actual UI, API, and commands. Run the supported release checks. Use technical-writing to prepare release notes with changes, observed results, and unresolved gaps. Keep deployment and publication paused for explicit authorization.
```

Expected output: A release handoff that states what is checked and what remains open.

Principle in practice: Outcome-oriented execution: the release decision follows the requested behavior and evidence, rather than a completed checklist alone.

Completion check: The user can review the release evidence and make a concrete publication decision.

The [website workflow section](https://pstack-openai.yabasha.chatgpt.site/#workflows) uses the same [workflow source](docs/workflows/examples.json). Changes pushed to `main` automatically regenerate this README and the site feed through [GitHub Actions](.github/workflows/sync-workflows.yml). The site loads that feed on page load and checks every five minutes while open. It keeps its published snapshot if the feed is unavailable. For local edits, run `bun tools/render_workflow_examples.mjs`; use `bun tools/render_workflow_examples.mjs --check` to detect drift. See [automatic sync](docs/workflows/automatic-sync.md) for scope and recovery.

<!-- workflow-examples:end -->
