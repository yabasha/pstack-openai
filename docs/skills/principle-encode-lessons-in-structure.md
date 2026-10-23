# principle-encode-lessons-in-structure

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-encode-lessons-in-structure.json](../catalog/skills/principle-encode-lessons-in-structure.json).

Skill: [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md). Kind: principle.

## Purpose

Encode recurring corrections in enforceable structures and close the correction loop.

## Triggers

- Writing the same instruction a second time
- A recurring correction or unexpected outcome

## Required input

- Authorized task and relevant source
- Correction pattern and rule to enforce

## Output contract

- Concrete structural mechanism at the strongest feasible layer, or judgment-dependent guidance with a failure example
- Correction routed to an authorized durable record, skill, lint rule or principle; applied fix or concrete todo

## Ordinary example

Require a source revision in the release-record schema and reject records that omit it, then remove the redundant reminder.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [repeated-rule](../parity/cases/skills/principle-encode-lessons-in-structure.json)

We have corrected the same mistake twice: generated release records omit the source revision. Apply principle-encode-lessons-in-structure. Replace the repeated prose warning with a concrete validator or structural check, explain where it belongs, and close the correction loop within the available authorization.

Full capability expectation:

The response proposes or implements an enforceable source-revision requirement at the strongest feasible layer, with a specific rejection condition and failure example. It routes the recurring correction to a validator or skill, closes the loop through authorized implementation or a concrete todo, and removes the redundant prose warning once enforcement exists. It reports only observed implementation and checks.

Reduced capability expectation:

If writes, execution or durable persistence are unavailable, provide the concrete validator condition, its integration point and a specific implementation todo as a reduced proposal. State which changes, checks or saves remain unperformed.

Blocked capability expectation:

If the record format or required revision rule is unavailable, identify those missing inputs and keep any validator proposal provisional. Do not claim implemented enforcement or saved corrections.

Required observations:

- Propose a concrete validator or structural check that rejects a release record without its source revision instead of repeating a prose warning.
- Choose the strongest feasible mechanism, considering an unrepresentable state, CI lint or banned API, canonical helper and runtime check in that order.
- Capture the correction, distinguish a one-off from a recurring or systemic issue, route it to the appropriate durable layer and apply it or create a concrete todo.
- Delete redundant instructions when a structural fix enforces the rule; retain a prominent instruction and failure example when enforcement requires judgment.
- Report implementation, persistence and checks only when authorized and observed.

Forbidden claims:

- Repeating the prose warning alone closes a recurring correction.
- An unimplemented validator enforces the rule.
- A claimed save without write and readback proves persistence.
- Structural package validation proves behavioral parity.
- Invocation metadata proves host enforcement.
- The principle grants authorization for global settings, installs or external actions.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing source or rule keeps the mechanism provisional.
- Unavailable writes, execution or persistence allow a reduced proposal with unperformed work stated.
- Saved corrections require observed write and readback.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-encode-lessons-in-structure/SKILL.md`

Destination: [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `228963799189f481827d6f28065f278bc2008ffa37030b1234cbd5814d36b9e9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
