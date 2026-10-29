# how

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/how.json](../catalog/skills/how.json).

Skill: [skills/how/SKILL.md](../../skills/how/SKILL.md). Kind: workflow.

## Purpose

Explain subsystem architecture and runtime flow for a senior engineer using inspected code.

## Triggers

- how does X work
- Code walkthrough before a change
- Placement, ownership and layering questions

## Required input

- Question and codebase
- Supplied execution path or subsystem scope
- Available read-only worker and source tools

## Output contract

- Overview, Key Concepts, How It Works, Where Things Live and Gotchas as applicable
- Actual files and functions, data flow, boundaries, diagrams when useful and explicit open questions

## Ordinary example

Trace an API request from its route through its service calls and storage layer, citing the files read.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [trace-path](../parity/cases/skills/how.json)

Explain how a supplied request execution path works, from entry point through its downstream calls. Cite actual files and disclose whether explorers ran independently.

Full capability expectation:

Choose the simple or complex path. Complex work uses 2 to 4 distinct read-only explorers and one explainer; simple work uses one read-only explainer. Cite actual read files, functions, data flow and relevant line numbers; reconcile conflicting findings against code and retain open questions.

Reduced capability expectation:

When workers are absent, disclose reduced capability and sequential exploration. Apply the same explorer and explainer roles in sequence, cite actual files along the supplied path, and retain unknown links without claiming independent workers.

Blocked capability expectation:

When required source cannot be read or permission is denied, identify the unavailable path and explain the resulting gap without inventing execution flow.

Required observations:

- Readable supplied codebase and execution path
- Observed worker operations for independent exploration and synthesis

Forbidden claims:

- Independent explorers without observed spawn and result inspection
- Runtime behavior inferred only from names
- Actual model selection or host pass without evidence
- Complete flow when source links remain untraced

## Dependencies

- [skills/how/references/explorer-prompt.md](../../skills/how/references/explorer-prompt.md)
- [skills/how/references/explainer-prompt.md](../../skills/how/references/explainer-prompt.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Absent workers require disclosed sequential exploration with reduced capability.
- Unavailable source leaves explicit gaps.
- Model selection follows observed session support; source-host defaults are not portable.
- Invocation metadata is preserved without claiming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/how/SKILL.md`

Destination: [skills/how/SKILL.md](../../skills/how/SKILL.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `08a00079bb15b4258874ac3ff62d4ca7e94350ffedb521d0fd296dc9dd21904e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/how/references/explainer-prompt.md`

Destination: [skills/how/references/explainer-prompt.md](../../skills/how/references/explainer-prompt.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ddb89cebefc24e2b54517a331aedfe045b6971e101f45c71b8cef4cccff45bff`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/how/references/explorer-prompt.md`

Destination: [skills/how/references/explorer-prompt.md](../../skills/how/references/explorer-prompt.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6300128385ee940fd42ecb84b0e623435440a2dc283eae54ee4a52ba56947ba1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
