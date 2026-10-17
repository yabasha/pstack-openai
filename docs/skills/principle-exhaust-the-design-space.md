# principle-exhaust-the-design-space

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-exhaust-the-design-space.json](../catalog/skills/principle-exhaust-the-design-space.json).

Skill: [skills/principle-exhaust-the-design-space/SKILL.md](../../skills/principle-exhaust-the-design-space/SKILL.md). Kind: principle.

## Purpose

Explore distinct alternatives before choosing a novel interaction or architectural approach.

## Triggers

- Novel UI interactions without codebase precedent
- Architectural choices with multiple viable approaches
- Product decisions where experience depends on feel

## Required input

- Authorized task and constraints
- Codebase precedent
- Available prototype and evaluation tools

## Output contract

- 2-3 distinct prototypes or sketches compared side by side
- Choice after comparison, with observed checks and untested limits

## Ordinary example

Compare a command palette, a direct manipulation canvas and a guided form for a novel editing interaction before choosing its implementation.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [alternatives](../parity/cases/skills/principle-exhaust-the-design-space.json)

A novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.

Full capability expectation:

Build 2-3 distinct prototypes or sketches, compare them side by side, and choose only after comparison. Report executed checks only when observed. Explain that minor variations of one approach do not count and that established patterns or a single viable approach do not require this exploration.

Reduced capability expectation:

Without execution, compare 2-3 distinct sketches or proposals and label them untested. State that runtime behavior and interaction feel remain unverified. Without writes, keep sketches in the response and disclose the limitation.

Blocked capability expectation:

If required prototype construction or evaluation is denied or unavailable and sketches cannot answer the decision, report that step as blocked and identify the missing capability without claiming a completed comparison.

Required observations:

- Identify a novel decision with multiple viable approaches
- Compare 2-3 distinct prototypes or sketches side by side
- Observe available write and execution tools and permissions before using them

Forbidden claims:

- Execution or interaction testing occurred without observed results
- Minor variants count as distinct alternatives
- Prototype work authorizes publishing or external writes
- Static review establishes host parity

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Writes and execution require available tools and permissions.
- Without execution, label sketches or proposals untested; runtime behavior and interaction feel remain unverified.
- Required unavailable construction or evaluation remains blocked.
- Invocation metadata does not prove host enforcement. Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-exhaust-the-design-space/SKILL.md`

Destination: [skills/principle-exhaust-the-design-space/SKILL.md](../../skills/principle-exhaust-the-design-space/SKILL.md).

Upstream commit: `182f2ce414e83224915c190d2f63239c1608d0a5`. SHA-256: `2de83d99f93f60ec6313455b0bc9aa9f0bfb93dd59f414f403691322db00d4db`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
