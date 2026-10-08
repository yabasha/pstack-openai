# create-verification-skill

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/create-verification-skill.json](../catalog/skills/create-verification-skill.json).

Skill: [skills/create-verification-skill/SKILL.md](../../skills/create-verification-skill/SKILL.md). Kind: skill.

## Purpose

Generate a project-local verification skill grounded in the real app and prove one mapped user-facing feature.

## Triggers

- /create-verification-skill
- make a control skill for this repo
- project has no scripted way to prove UI/CLI/service behavior

## Required input

- Actual repository controls, startup instructions and existing harnesses
- Observed host discovery and authorized tool capabilities

## Output contract

- Project-local verify-<app> skill with YAML metadata
- Feature-map index and top 3-5 identifiable features
- Observed end-to-end proof with surviving evidence, or an explicit unrun draft

## Ordinary example

Inspect a notes app toolbar, keyboard shortcuts and CLI; generate its local verification skill and feature map, then exercise one feature and retain proof after cleanup.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [real-app-contract](../parity/cases/skills/create-verification-skill.json)

Create a verification skill for this repo. Inspect its real app controls and existing harness, seed a feature map, and prove one feature if authorized tools are available. Retain the Notes example contracts as examples only.

Full capability expectation:

Inspect real routes, controls, commands and startup before authoring. Generate registered YAML metadata and Launch, Doctor, Drive, Evidence, Cleanup and Helpers sections using actual controls; seed the top 3-5 identifiable features with the prescribed four headings and all user entry points. Launch, doctor, drive one mapped feature, capture action, resulting state and side effects, clean up each attempt, then confirm evidence survives. Report observed proof only and point to /maintain-verification-skill without scheduling.

Reduced capability expectation:

When repository controls can be inspected and writes are authorized but execution or app-driving is unavailable, author a draft grounded in those controls. Mark verification not-run, name missing capabilities and unproved entry points; do not present the draft as a verified deliverable. If project-local registration is unconfirmed, report a portable draft with registration unverified.

Blocked capability expectation:

If repository access or required authoring permission is unavailable, report the exact blocker and do not invent app controls or write files. If startup is broken, fix within authorization or report the precise failure before generation. Denied execution blocks proof and cannot count as a pass.

Required observations:

- Repository reads and authorized project-local writes
- Observed execution and app-driving tools for end-to-end proof
- Preserve all three feature-map examples and their exact commands
- Discover the active host project-local skill location and verify registration
- Follow the active workflow owner and permission boundaries

Forbidden claims:

- Notes example commands are real controls in an unrelated app
- An unexecuted generated skill is a verified deliverable
- A final screenshot alone proves the user action or side effects
- Skipped entry points are verified through another path
- A documented tool or project-local path proves discovery or successful execution
- Cleanup may delete evidence or kill processes by name
- Suggested cadence authorizes recurring scheduling

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [skills/maintain-verification-skill/SKILL.md](../../skills/maintain-verification-skill/SKILL.md)
- [skills/create-verification-skill/references/feature-map-example/README.md](../../skills/create-verification-skill/references/feature-map-example/README.md)
- [skills/create-verification-skill/references/feature-map-example/create-note.md](../../skills/create-verification-skill/references/feature-map-example/create-note.md)
- [skills/create-verification-skill/references/feature-map-example/search.md](../../skills/create-verification-skill/references/feature-map-example/search.md)

## Host limits

- Project-local registration requires observed host discovery; otherwise registration remains unverified.
- Execution or app-driving gaps leave verification not-run and the generated skill a draft.
- Dependency installation, listeners and external writes require applicable authorization.
- The maintenance leaf is present and reviewed; its live app verification still requires observed capabilities.
- Both hosts remain not-run; structural checks supply no behavioral proof.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/create-verification-skill/SKILL.md`

Destination: [skills/create-verification-skill/SKILL.md](../../skills/create-verification-skill/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `644f2551403c1bca01a2855b34611b6e7be0ce0dc5b204514c376c0f6a6e6ac4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/real-app-contract.json](../parity/evidence/chatgpt/real-app-contract.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/real-app-contract.json](../parity/evidence/codex/real-app-contract.json).

### `skills/create-verification-skill/references/feature-map-example/README.md`

Destination: [skills/create-verification-skill/references/feature-map-example/README.md](../../skills/create-verification-skill/references/feature-map-example/README.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `cb7bd782cf89968a4ba3d58a5151db837430db92d19a6f52a906973b77b516ba`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/real-app-contract.json](../parity/evidence/chatgpt/real-app-contract.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/real-app-contract.json](../parity/evidence/codex/real-app-contract.json).

### `skills/create-verification-skill/references/feature-map-example/create-note.md`

Destination: [skills/create-verification-skill/references/feature-map-example/create-note.md](../../skills/create-verification-skill/references/feature-map-example/create-note.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `644a44c74f35d38c2feb7cd05a0121fdebbb623e8dc376c185b565a581d1ccf7`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/real-app-contract.json](../parity/evidence/chatgpt/real-app-contract.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/real-app-contract.json](../parity/evidence/codex/real-app-contract.json).

### `skills/create-verification-skill/references/feature-map-example/search.md`

Destination: [skills/create-verification-skill/references/feature-map-example/search.md](../../skills/create-verification-skill/references/feature-map-example/search.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `6e87b9e7f2791a7776ba1bb83f371cd285c306c67f19d245cc4dd6ca3015c823`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/real-app-contract.json](../parity/evidence/chatgpt/real-app-contract.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/real-app-contract.json](../parity/evidence/codex/real-app-contract.json).
