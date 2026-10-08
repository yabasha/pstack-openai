# principle-subtract-before-you-add

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-subtract-before-you-add.json](../catalog/skills/principle-subtract-before-you-add.json).

Skill: [skills/principle-subtract-before-you-add/SKILL.md](../../skills/principle-subtract-before-you-add/SKILL.md). Kind: principle.

## Purpose

Remove obsolete behavior and redundant complexity before adding its replacement, then build on the simpler base.

## Triggers

- Sequencing an addition, refactor or rewrite
- Removing dead code, redundant validators or stub references

## Required input

- Authorized task and inspected source
- Observed usage and specified requirements

## Output contract

- Removal before construction, simpler prompts and references, and observed implementation checks when available
- Ordered proposal with explicit limits when writes or execution are unavailable

## Ordinary example

Inspect callers of an obsolete handler, remove that handler and its redundant validator, then add the specified replacement without speculative guards.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [dead-path](../parity/cases/skills/principle-subtract-before-you-add.json)

Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.

Full capability expectation:

Inspect actual usage and requirements, remove obsolete behavior before constructing the replacement, and show the sequence and observed checks. Cut before polishing, preserve required behavior, avoid speculative edge cases, validators, parsers and guards, simplify redundant prompts, and delete empty references rather than leaving stubs. Leave the design simpler and more capable behind the same or smaller interface.

Reduced capability expectation:

With source available but writes or execution unavailable, provide an ordered removal and replacement proposal as reduced capability. State which edits and checks were not performed.

Blocked capability expectation:

If source or required usage evidence is unavailable, state the missing inputs and block claims that deletion is safe or completed. Do not invent obsolete paths or usage.

Required observations:

- Available source and observed usage
- Authorization and write capability for changes
- Execution capability for actual checks

Forbidden claims:

- Replacement constructed before obsolete behavior is removed
- Deletion is safe without inspecting usage and required behavior
- Unperformed edits or checks claimed complete
- Speculative guards added beyond the specification
- Host parity or metadata enforcement claimed from structural validation

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Removal requires source and usage evidence, authorization and writes; checks require observed execution.
- Missing writes or execution permit a reduced proposal; missing source blocks safety and completion claims.
- Invocation metadata is preserved without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-subtract-before-you-add/SKILL.md`

Destination: [skills/principle-subtract-before-you-add/SKILL.md](../../skills/principle-subtract-before-you-add/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `a983a50e732c1ed315eba7aaf47a61329e31c4794eb1ab9d25d9945265b31e03`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/dead-path.json](../parity/evidence/chatgpt/dead-path.json), [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/preserved-behavior.json](../parity/evidence/chatgpt/preserved-behavior.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/dead-path.json](../parity/evidence/codex/dead-path.json), [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/preserved-behavior.json](../parity/evidence/codex/preserved-behavior.json).
