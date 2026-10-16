# figure-it-out

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/figure-it-out.json](../catalog/skills/figure-it-out.json).

Skill: [skills/figure-it-out/SKILL.md](../../skills/figure-it-out/SKILL.md). Kind: workflow.

## Purpose

Design and execute an auditable playbook when no narrower workflow fits, with task-scaled rigor and hypothesis loops.

## Triggers

- /figure-it-out
- figure it out
- A large migration
- No narrower playbook applies

## Required input

- task scope and accessible grounding evidence
- Falsifiable definition of done, authorized scope and available capabilities

## Output contract

- Designed playbook before code and rigor rationale
- Decision trail recorded as units land
- Verified results against the predicate and open limits

## Ordinary example

Use /figure-it-out for a large migration, capture the old behavior, verify atomic units and record an inconclusive measurement as an open limit.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [uncertain-result](../parity/cases/skills/figure-it-out.json)

Figure it out: design and carry out an auditable migration playbook. The initial measurement is ambiguous and the deployment evidence is inaccessible. Investigate accessible evidence and report what remains uncertain.

Full capability expectation:

Frames a falsifiable predicate, quantifies scope, chooses rigor and checkpoint, designs phases before code, captures baseline, investigates accessible evidence through hypothesis/change/measurement loops, records decisions as units land, and hands back the playbook, rigor rationale, trail path, verified results and concrete inaccessible-evidence limit. Uses INCONCLUSIVE for unresolved observations.

Reduced capability expectation:

Uses authorized accessible artifacts and sequential work when independent workers are unavailable, labels reduced capability, preserves the five phases and reports missing execution or persistence as concrete limits. No inaccessible result is fabricated.

Blocked capability expectation:

States which required evidence or operation is inaccessible or denied, reports NOT VERIFIED or INCONCLUSIVE, and supplies the designed workflow and open questions without inventing execution or a saved trail.

Required observations:

- Accessible source and artifacts
- Authorized artifact inspection and execution for verification
- Decision-trail persistence; independent workers only when exposed and authorized

Forbidden claims:

- Inconclusive evidence is a pass
- Unavailable deployment evidence proves migration success
- Sequential work establishes independent workers
- A trail was saved without observed persistence
- Workflow autonomy authorizes external actions

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [skills/poteto-mode/SKILL.md](../../skills/poteto-mode/SKILL.md)
- [skills/architect/SKILL.md](../../skills/architect/SKILL.md)
- [skills/arena/SKILL.md](../../skills/arena/SKILL.md)
- [skills/show-me-your-work/SKILL.md](../../skills/show-me-your-work/SKILL.md)
- [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md)
- [skills/principle-never-block-on-the-human/SKILL.md](../../skills/principle-never-block-on-the-human/SKILL.md)
- [skills/principle-foundational-thinking/SKILL.md](../../skills/principle-foundational-thinking/SKILL.md)
- [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md)
- [skills/principle-separate-before-serializing-shared-state/SKILL.md](../../skills/principle-separate-before-serializing-shared-state/SKILL.md)
- [skills/principle-sequence-verifiable-units/SKILL.md](../../skills/principle-sequence-verifiable-units/SKILL.md)
- [skills/principle-encode-lessons-in-structure/SKILL.md](../../skills/principle-encode-lessons-in-structure/SKILL.md)

## Host limits

- Missing inspection or execution leaves results NOT VERIFIED or INCONCLUSIVE
- Unavailable independent workers permit explicitly reduced sequential work
- Unavailable persistence prevents a durable-trail claim
- Missing supporting skills remain explicit dependencies
- Authorization bounds commits, external actions and setup
- Host behavior is not-run; invocation metadata enforcement is not assumed

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/figure-it-out/SKILL.md`

Destination: [skills/figure-it-out/SKILL.md](../../skills/figure-it-out/SKILL.md).

Upstream commit: `99743e9c151c8537cbbf1f98bb38f34ef3368453`. SHA-256: `bdb23cdbd82a1e6af094b495691c832a6f7f3ab9706ba9edbeb664ef51a726e1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
