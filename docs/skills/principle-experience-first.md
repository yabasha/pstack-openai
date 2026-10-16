# principle-experience-first

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-experience-first.json](../catalog/skills/principle-experience-first.json).

Skill: [skills/principle-experience-first/SKILL.md](../../skills/principle-experience-first/SKILL.md). Kind: principle.

## Purpose

Choose user delight over implementation convenience, justify scope and polish the central workflow.

## Triggers

- Product, UX or feature-scope tradeoffs

## Required input

- Authorized task
- User and central workflow context
- Available design or implementation source

## Output contract

- Concrete scope recommendation with reasons from the perspective of end users, API consumers and maintainers
- Authorized prototypes or edits and actual checks when tools permit

## Ordinary example

Choose three polished import controls over ten rough controls because users can finish and recover from the core import workflow with clear feedback.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [user-tradeoff](../parity/cases/skills/principle-experience-first.json)

Apply principle-experience-first to an import workflow. The team can ship ten controls with rough feedback or three polished controls covering the core import loop. Recommend a scope and explain the user outcome rather than implementation convenience. Consider end users, library consumers and future maintainers. Prototype only with authorized available tools.

Full capability expectation:

Choose three polished controls because they let users complete and recover from imports with clear feedback. Justify the controls against the core loop, consider API consumers and maintainers, and use an authorized throwaway prototype before production commitment. Explain relevant details and actual checks.

Reduced capability expectation:

With enough supplied context but unavailable prototype writes or execution, recommend the scope and describe a concrete prototype and feedback/error-state design. Label reduced capability and identify operations not performed.

Blocked capability expectation:

If essential user or workflow context is missing, identify the missing input before committing to a design. If prototype execution is denied or unavailable, record that operation as blocked without claiming a completed prototype.

Required observations:

- Choose the user outcome with a concrete reason rather than implementation convenience.
- Justify every feature, control and option; prefer fewer polished features and tighten the central workflow.
- Prototype before committing to design and address transitions, alignment, spacing, feedback and error states.
- Weigh end users, colleagues importing libraries or APIs, and future maintainers; explain impact from their perspective.
- Foundational thinking governs work sequence; experience governs the target.
- Discover tools and permissions before inspection, prototype writes or execution; report only observed operations.

Forbidden claims:

- Implementation convenience alone justifies worse user outcomes.
- More rough features necessarily provide a better experience.
- Library consumers or maintainers do not count as users.
- A prototype or test completed without observed authorized operations.
- Structural validation establishes host behavioral parity.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Prototype writes, edits and execution require available tools and permissions.
- Without writes or execution, provide a reduced recommendation and prototype plan; missing user context keeps designs provisional.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-experience-first/SKILL.md`

Destination: [skills/principle-experience-first/SKILL.md](../../skills/principle-experience-first/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `58903529d733b1c1a7c9ccf127d45ef3c7d0d9f0b81164a4dc6b80efe6f2912b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/user-tradeoff.json](../parity/evidence/chatgpt/user-tradeoff.json).
- codex: `not-run`. Tested release evidence: [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/user-tradeoff.json](../parity/evidence/codex/user-tradeoff.json).
