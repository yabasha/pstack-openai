# blast-radius

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/blast-radius.json](../catalog/skills/blast-radius.json).

Skill: [skills/blast-radius/SKILL.md](../../skills/blast-radius/SKILL.md). Kind: workflow.

## Purpose

Find what a change can break outside the diff and prove the safety fact by running real code.

## Triggers

- blast radius of X
- what could this break
- Reviewing a small diff you do not trust

## Required input

- Diff and codebase
- Real dependent callers, pinned library source and local patches
- Available history, execution and arena review capabilities

## Output contract

- What it does; the one fact it is safe because of; risks; cleared; before you merge
- Safety-fact evidence level and runtime proof or explicit unproven status
- Caller citations, risk likelihood and cost, proof output and cheapest test

## Ordinary example

Review cache invalidation and trace a caller outside the diff through teardown timing, then run the real pinned library to test the safety fact.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [dependent-caller](../parity/cases/skills/blast-radius.json)

Review a cache invalidation diff. Trace a dependent caller outside the diff, including its pinned dependency and teardown timing, and prove or mark unproven the runtime consequence of the one fact the change relies on.

Full capability expectation:

Find a dependent caller outside the diff and connect the changed behavior to its runtime consequence with real file:line evidence. Run the real code and report the command, result and evidence level for the safety fact. Distinguish confirmed risks and cleared risks, then provide the cheapest pre-merge test. For a wide change, use authorized arena review and report observed worker and model limits.

Reduced capability expectation:

With source access but no authorized execution, trace the caller and explain the runtime consequence from source while marking the safety fact unproven and reporting where evidence stopped. Provide the proposed real-code test without claiming it ran. Missing arena workers or model diversity are disclosed as reduced capability.

Blocked capability expectation:

If the diff or relevant caller source cannot be inspected, state the missing input or denied capability and leave the runtime consequence and safety fact unproven. Request the needed source or permission without inventing callers, results or setup.

Required observations:

- Read the diff and a real dependent caller outside it, citing file:line and following runtime timing or shared data contracts beyond symbol search.
- Identify the one or two safety facts and report their evidence level, separating confirmed risks from checked and cleared risks.
- Run an authorized script or test against the real pinned code and paste its result, or mark the fact unproven when execution is denied or unavailable.
- Use the prescribed output sections and give risk likelihood, cost and a cheapest pre-merge check.
- For a wide change, check arena and observed worker/model capabilities; disclose any sequential reduced capability or unverified diversity.

Forbidden claims:

- Caller lists alone establish runtime safety.
- A hypothetical or mock-only result proves the actual pinned code.
- An unexecuted script or source-only argument is runtime proof.
- Requested model names establish observed model diversity or sequential review supplies independent workers.
- Unavailable or denied capabilities justify installation, publishing or external writes without authorization.

## Dependencies

- [skills/how/SKILL.md](../../skills/how/SKILL.md)
- [skills/why/SKILL.md](../../skills/why/SKILL.md)
- [skills/arena/SKILL.md](../../skills/arena/SKILL.md)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Unavailable diff or caller source blocks a grounded consequence assessment.
- Denied or unavailable execution leaves runtime proof unproven.
- Missing arena workers or model diversity requires disclosed reduced capability.
- Invocation metadata is preserved without claiming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/blast-radius/SKILL.md`

Destination: [skills/blast-radius/SKILL.md](../../skills/blast-radius/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `2e10745b97f5862323dcda3b29ca60d56b5c3c98e37020085d26b48efbe0a436`.

Disposition: `runtime`. Aggregate adaptation status: `pending`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
