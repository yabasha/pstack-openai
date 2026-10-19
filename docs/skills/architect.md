# architect

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/architect.json](../catalog/skills/architect.json).

Skill: [skills/architect/SKILL.md](../../skills/architect/SKILL.md). Kind: workflow.

## Purpose

Sketch caller usage, types, signatures and module boundaries before implementation, compare whole-shape alternatives and redesign when repeated implementation friction invalidates the sketch.

## Triggers

- /architect
- architect this
- design this
- non-trivial work where coding first would lock in the wrong shape

## Required input

- Design task and authorized subsystem source reads
- Grounding artifacts, runner preferences and observed capabilities
- Implementation scope and optional checkpoint request

## Output contract

- At least two structurally distinct design candidates and synthesized sketch
- Caller-first usage, ownership, module map and complete rationale
- Authorized implementation, surfaced deviations and renewed design when required

## Ordinary example

Design a stateful cache boundary, compare two ownership models, derive types from caller usage and implement the selected sketch within authorized scope.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [boundary-design](../parity/cases/skills/architect.json)

Architect a supplied stateful subsystem change. Compare at least two structurally distinct designs, show caller usage before types, ownership and rationale. Then implement within my authorized scope; with unavailable workers label sequential alternatives.

Full capability expectation:

Observed authorized independent runners produce two structurally distinct candidates using the runner prompt. Synthesis compares depth and all red flags, records state ownership, selected base, grafts and rejections. Caller usage precedes types and the complete rationale accompanies the sketch. Implementation follows the sketch within authorization; explicit checkpoint pauses before implementation.

Reduced capability expectation:

Without workers, label sequential alternatives as reduced capability, use the complete arena workflow and runner discipline for two distinct alternatives and preserve comparison, ownership and full rationale. Missing direct invocation uses disclosed complete-workflow execution. Unverified or identical observed models cannot support model diversity. Denied writes permit a read-only sketch with an explicit implementation block.

Blocked capability expectation:

Missing required workflow or authorized source reads block grounded design. Missing exact required model selection or implementation permission remains explicit; do not claim a runner, checkpoint approval or implementation succeeded.

Required observations:

- Ground with how and why when ownership or layering changes; skip only genuine greenfield.
- Use arena to compare at least two whole-shape candidates, screen all eight design red flags and judge interface depth.
- Preserve caller-first usage, type sketch, module ownership and every rationale-template section, including synthesis and rejected alternatives.
- Honor opt-in checkpoint, authorized implementation, deviation signals and scrap/reground/re-explore cycle.
- Observe independent workers and actual model diversity or disclose their limits; preserve model selection rejections and aliases.

Forbidden claims:

- Sequential alternatives described as independent workers.
- Requested models or upstream defaults described as observed model diversity.
- Unsupported runner aliases or tool names claimed usable.
- Invented grounding, rationale, approvals or implementation success.
- Structural checks described as host behavioral pass.

## Dependencies

- [skills/how/SKILL.md](../../skills/how/SKILL.md)
- [skills/why/SKILL.md](../../skills/why/SKILL.md)
- [skills/arena/SKILL.md](../../skills/arena/SKILL.md)
- [skills/interrogate/SKILL.md](../../skills/interrogate/SKILL.md)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [skills/architect/references/design-red-flags.md](../../skills/architect/references/design-red-flags.md)
- [skills/architect/references/rationale-template.md](../../skills/architect/references/rationale-template.md)
- [skills/architect/references/runner-prompt.md](../../skills/architect/references/runner-prompt.md)
- [skills/principle-exhaust-the-design-space/SKILL.md](../../skills/principle-exhaust-the-design-space/SKILL.md)
- [skills/principle-foundational-thinking/SKILL.md](../../skills/principle-foundational-thinking/SKILL.md)
- [skills/principle-outcome-oriented-execution/SKILL.md](../../skills/principle-outcome-oriented-execution/SKILL.md)
- [skills/principle-redesign-from-first-principles/SKILL.md](../../skills/principle-redesign-from-first-principles/SKILL.md)
- [skills/principle-fix-root-causes/SKILL.md](../../skills/principle-fix-root-causes/SKILL.md)
- [skills/principle-subtract-before-you-add/SKILL.md](../../skills/principle-subtract-before-you-add/SKILL.md)
- [skills/principle-separate-before-serializing-shared-state/SKILL.md](../../skills/principle-separate-before-serializing-shared-state/SKILL.md)
- [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md)
- [skills/principle-boundary-discipline/SKILL.md](../../skills/principle-boundary-discipline/SKILL.md)
- [skills/principle-make-operations-idempotent/SKILL.md](../../skills/principle-make-operations-idempotent/SKILL.md)
- [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md)
- [skills/principle-minimize-reader-load/SKILL.md](../../skills/principle-minimize-reader-load/SKILL.md)

## Host limits

- Unavailable workers require labelled sequential alternatives as reduced capability.
- Model aliases are preferences; requested or unknown models do not prove diversity.
- Missing invocation uses disclosed complete-workflow execution; missing required workflows block.
- Source reads, isolated writes, worktrees, commits and implementation require authorization and exposed capabilities.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/architect/SKILL.md`

Destination: [skills/architect/SKILL.md](../../skills/architect/SKILL.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `31f8e97a52bfa5432edd61f68ade2a8632ef0bacbc2d2a6802d7a0e6821944ac`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/architect/references/design-red-flags.md`

Destination: [skills/architect/references/design-red-flags.md](../../skills/architect/references/design-red-flags.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `d0e639e4cc588ec865f930d3a4111faad60987ae36925917e319d7ceca7c69ce`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/architect/references/rationale-template.md`

Destination: [skills/architect/references/rationale-template.md](../../skills/architect/references/rationale-template.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `0cedfccdc7b47fc881febd5a8293eecbc542c20f8df825639904a8102d2eb5d3`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/architect/references/runner-prompt.md`

Destination: [skills/architect/references/runner-prompt.md](../../skills/architect/references/runner-prompt.md).

Upstream commit: `d457567332aa6989e753ea289f30ea2bfbc80bc0`. SHA-256: `21dd5314aab778c5007228027a4591d97693fbec6ab86524037772b63f40948e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
