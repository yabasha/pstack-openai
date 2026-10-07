# principle-attack-the-premise

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-attack-the-premise.json](../catalog/skills/principle-attack-the-premise.json).

Skill: [skills/principle-attack-the-premise/SKILL.md](../../skills/principle-attack-the-premise/SKILL.md). Kind: principle.

## Purpose

Question a shared premise after repeated failed fixes, census actor imbalance and remove persistent role asymmetry.

## Triggers

- Two or more fixes sharing one premise fail the same gate

## Required input

- Failed fixes and shared premise
- Actor-level imbalance evidence across runs

## Output contract

- Written premise and rerunnable actor census
- Role-assignment diagnosis or evidence directing investigation elsewhere

## Ordinary example

After two balancing fixes fail, count which workers retain excess load across runs and trace the assignment that keeps selecting them.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [repeated-failure](../parity/cases/skills/principle-attack-the-premise.json)

Two fixes assume actor assignment is harmless, but both fail the same imbalance check. Before a third fix, apply Attack the Premise. Inspect actor counts across runs and consider both skewed and even census outcomes.

Full capability expectation:

Write the common premise before another fix. Create and run an actor census; inspect who holds the imbalance across runs. For persistent skew, trace role assignment and remove asymmetry by rotating, randomizing or moving the role. Reject compensations that preserve assignment and add recurring work. For an even census, retain evidence and investigate another cause. Distinguish this from redesign around a new requirement.

Reduced capability expectation:

With evidence available but writes or execution unavailable, state the premise and propose the rerunnable census with explicit limits. Stop before the next fix and do not claim a census exists or ran.

Blocked capability expectation:

If failed-check or actor evidence is unavailable, identify missing inputs and stop before diagnosing the assignment or implementing another fix.

Required observations:

- Read the shared premise and both failed checks.
- Inspect actor-level evidence and create a rerunnable census when writes and execution are authorized.

Forbidden claims:

- Two failed fixes prove the premise false without a census.
- A proposed census is an executed census.
- An even census supports blaming the premise.
- Compensation that retains assignment removes the asymmetry.
- Static review proves host behavior or metadata enforcement.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [skills/principle-build-the-lever/SKILL.md](../../skills/principle-build-the-lever/SKILL.md)
- [skills/principle-fix-root-causes/SKILL.md](../../skills/principle-fix-root-causes/SKILL.md)
- [skills/principle-laziness-protocol/SKILL.md](../../skills/principle-laziness-protocol/SKILL.md)
- [skills/principle-redesign-from-first-principles/SKILL.md](../../skills/principle-redesign-from-first-principles/SKILL.md)

## Host limits

- Census creation requires authorized writes and execution requires an available tool.
- Unavailable writes or execution allow a census proposal, with no claim it exists or ran.
- Missing actor or failed-check evidence blocks diagnosis.
- Invocation metadata enforcement and host behavior remain unverified.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-attack-the-premise/SKILL.md`

Destination: [skills/principle-attack-the-premise/SKILL.md](../../skills/principle-attack-the-premise/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `c87bd7536f772f8a403ad8155535ee17a1bbec9a353156693eb3bb1520c87ae3`.

Disposition: `runtime`. Aggregate adaptation status: `pending`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
