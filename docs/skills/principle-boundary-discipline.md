# principle-boundary-discipline

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-boundary-discipline.json](../catalog/skills/principle-boundary-discipline.json).

Skill: [skills/principle-boundary-discipline/SKILL.md](../../skills/principle-boundary-discipline/SKILL.md). Kind: principle.

## Purpose

Concentrate validation, type narrowing and error handling at system boundaries; trust internal types and keep business logic in pure functions.

## Triggers

- Wiring validation, error handling or framework adapters

## Required input

- Relevant source and external input contracts
- Authorized task and available capabilities

## Output contract

- Boundary validation and typed internal error propagation with pure business logic; observed implementation and checks when available

## Ordinary example

Validate an incoming order quantity in an HTTP adapter, pass a typed order to pure pricing logic and remove redundant internal quantity checks.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [invalid-input](../parity/cases/skills/principle-boundary-discipline.json)

Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.

Full capability expectation:

The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.

Reduced capability expectation:

If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed.

Blocked capability expectation:

If relevant source or the input contract is unavailable, identify the missing information and keep any proposal provisional. Do not claim that boundary validation or guard removal was verified.

Required observations:

- Validate external input at its boundary without duplicating internal guards.
- Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.
- Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.
- Report implementation and checks only when writes and execution are authorized and observed.

Forbidden claims:

- Structural checks prove behavioral parity.
- Unavailable writes or execution succeeded.
- Internal validation is required after the boundary has validated typed data.
- Invocation metadata proves host enforcement.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing source or input contracts keep proposals provisional.
- Unavailable writes or execution allow a reduced proposal with unperformed checks stated.
- Invocation metadata does not prove host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-boundary-discipline/SKILL.md`

Destination: [skills/principle-boundary-discipline/SKILL.md](../../skills/principle-boundary-discipline/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `62ac2862c2caa22dd14531f51c9c6bb445ceb198ca98a687e25b4d47c1f10a28`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
