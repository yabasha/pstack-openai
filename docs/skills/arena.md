# arena

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/arena.json](../catalog/skills/arena.json).

Skill: [skills/arena/SKILL.md](../../skills/arena/SKILL.md). Kind: workflow.

## Purpose

Compare isolated attempts at the same artifact, pick a maintainable base, graft the strongest rejected-candidate ideas coherently and verify the synthesis.

## Triggers

- /arena
- arena this
- throw it in the arena
- one attempt at a non-trivial artifact would lock in the wrong shape

## Required input

- Authorized artifact task and shared grounding
- Parent-only 3-6 criterion rubric
- Runner and cross-judge preferences, observed capabilities and isolated output paths

## Output contract

- One synthesized artifact
- Adjacent synthesis note with base, judge verdict, graft sources, rejections, dropouts and verification

## Ordinary example

Compare two cache API designs in isolated directories, judge completed candidates, select the cleaner boundary and adapt one useful idea from the other design.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [candidate-cross-review](../parity/cases/skills/arena.json)

Arena two designs for an authorized local cache API. Produce isolated artifacts and rationales, then have a fresh cross-judge review the completed candidates before parent selection and grafting. Exercise a candidate dropout and unavailable-worker branch.

Full capability expectation:

Two or more isolated candidates finish before a fresh readonly judge receives the rubric and labelled artifact paths. Parent reads and scores all candidates, compares rationales, selects a maintainable base, grafts coherently and verifies the synthesis with an adjacent evidence note.

Reduced capability expectation:

Without independent workers or a fresh judge, authorized sequential alternatives and parent comparison may produce a useful synthesis labelled reduced capability. Dropouts are recorded; one survivor is incomplete competition and does not prove competitive selection.

Blocked capability expectation:

Required independence, exact model choice, source reads, isolation or writes unavailable or denied blocks that gate. Zero surviving artifacts blocks synthesis. Missing required principle or contract blocks dependent execution.

Required observations:

- At least two isolated candidate artifacts and rationales complete before a fresh readonly cross-judge starts.
- Candidates receive the same task and grounding, but not the parent rubric. Parent derives 3-6 gradeable criteria.
- Judge scores by criterion and recommends a base; parent reads every candidate end to end and resolves disagreement before selection.
- Parent records base, hand-adapted grafts, rejections, convergence or reframing, dropouts and verification.
- Observe independent worker operations, result artifacts and permission-bound writes; record requested and actual models separately.
- One survivor means incomplete competition, never a full arena pass.

Forbidden claims:

- Sequential role switching proves independent candidates or independent review.
- Requested model names prove actual model diversity.
- A judge begins while candidates still write.
- One survivor establishes full competition.
- Structural validation or a case definition establishes host pass.
- The rubric is supplied to candidates.
- Upstream autonomy permits external writes or implicit setup.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [skills/principle-separate-before-serializing-shared-state/SKILL.md](../../skills/principle-separate-before-serializing-shared-state/SKILL.md)
- [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md)
- [skills/principle-redesign-from-first-principles/SKILL.md](../../skills/principle-redesign-from-first-principles/SKILL.md)
- [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md)
- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)

## Host limits

- Independent candidates and fresh judging require exposed authorized workers and inspected artifacts.
- Sequential alternatives are reduced capability; one survivor is incomplete competition.
- Requested models do not prove actual model diversity.
- Required missing capabilities or denied writes block their gates.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/arena/SKILL.md`

Destination: [skills/arena/SKILL.md](../../skills/arena/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `6e17736b5228b661569c3af054f8302c55cf9bf1649447652d53705cce38bed6`.

Disposition: `runtime`. Aggregate adaptation status: `pending`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
