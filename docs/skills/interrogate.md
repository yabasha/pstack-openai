# interrogate

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/interrogate.json](../catalog/skills/interrogate.json).

Skill: [skills/interrogate/SKILL.md](../../skills/interrogate/SKILL.md). Kind: workflow.

## Purpose

Adversarially review changes through competing reviewers and pragmatic lead judgment without automatically applying changes.

## Triggers

- interrogate
- adversarial review
- multi-model review
- challenge this
- stress test this code
- find blind spots
- tear this apart

## Required input

- Diff or files and surrounding context
- Stated intent paragraph
- Authorized reviewer selections and observed capabilities

## Output contract

- Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map
- Attributed findings with evidence, category and lead rationale
- Observed worker independence, model diversity and limits

## Ordinary example

Challenge a branch diff with identical reviewer prompts, then trace a disputed null-input finding to its caller before categorizing it.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [adversarial-review](../parity/cases/skills/interrogate.json)

Adversarially review the current changes against their stated intent. Challenge correctness and structural quality, then decide which findings warrant action.

Full capability expectation:

Authorized independent reviewers receive the same template and all rubric/code-quality lenses. The lead deduplicates findings, traces evidence and classifies every finding with attribution and rationale. The verdict includes Intent, Reviewers, Act On, Consider, Noted, Dismissed and Agreement Map, with observed model diversity or its explicit limit.

Reduced capability expectation:

When independent workers are unavailable, an authorized sequential review applies the complete rubric and lead judgment and labels reduced capability. It does not claim independent agreement or model diversity; unknown actual models remain unknown.

Blocked capability expectation:

Unavailable diff or context, or denied review capability, blocks grounded findings. Report the missing source or permission without inventing findings, reviewer execution or agreement.

Required observations:

- State intent and give every competing reviewer the identical diff, context, rubric and code-quality lens.
- Preserve all rubric lenses, evidence-based findings and pragmatic lead judgment across act on, consider, noted and dismissed categories.
- Report reviewer models, finding counts, independent consensus, lone findings and disagreements in the complete verdict format.
- Verify independent worker results and observed model diversity; disclose sequential review as reduced capability.
- Do not auto-apply changes or create external changes to fix rejected model defaults.

Forbidden claims:

- Sequential passes are independent reviewers.
- Requested model names prove actual model diversity.
- The rubric or code-quality lens can be omitted.
- A review authorizes automatic fixes or an external PR.
- Structural checks establish host behavioral parity.

## Dependencies

- [skills/interrogate/references/code-quality-review.md](../../skills/interrogate/references/code-quality-review.md)
- [skills/interrogate/references/reviewer-prompt.md](../../skills/interrogate/references/reviewer-prompt.md)
- [skills/interrogate/references/rubric.md](../../skills/interrogate/references/rubric.md)
- [skills/interrogate/references/lead-judgment.md](../../skills/interrogate/references/lead-judgment.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Independent reviewers require observed authorized spawn and result inspection.
- Unknown or identical observed models do not establish model diversity.
- Sequential review is reduced capability.
- Missing source or denied review blocks grounded findings.
- Invocation metadata is retained without claiming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/interrogate/SKILL.md`

Destination: [skills/interrogate/SKILL.md](../../skills/interrogate/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `a16dfe179005abc22a4651b82f25b0c8ab953284276efe4e6dc341958fb63647`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/interrogate/references/code-quality-review.md`

Destination: [skills/interrogate/references/code-quality-review.md](../../skills/interrogate/references/code-quality-review.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `79162fda183eafd40d51661fbb5e151c7ba250f89e506ba17f5bd135dcbd50a8`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

### `skills/interrogate/references/reviewer-prompt.md`

Destination: [skills/interrogate/references/reviewer-prompt.md](../../skills/interrogate/references/reviewer-prompt.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `f6005cc2b535006fca97a96c5bfda49df57312eedf1ffd8d1aaaf3eb33817c25`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/interrogate/references/rubric.md`

Destination: [skills/interrogate/references/rubric.md](../../skills/interrogate/references/rubric.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `0f9c6bdb0b96e26dbde5f6407f417e0c02f54080e7a1268d8994f3c3ec6c5ac0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/interrogate/references/lead-judgment.md`

Destination: [skills/interrogate/references/lead-judgment.md](../../skills/interrogate/references/lead-judgment.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `355f5195a76bc75a655125292369f2a8231a2b61fabe5188d8f1386060922b87`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.
