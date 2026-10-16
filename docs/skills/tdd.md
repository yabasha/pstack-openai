# tdd

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/tdd.json](../catalog/skills/tdd.json).

Skill: [skills/tdd/SKILL.md](../../skills/tdd/SKILL.md). Kind: skill.

## Purpose

Make broken behavior executable before fixing a bug with a clear cheap test path, then prove the focused regression test passes.

## Triggers

- User explicitly asks for TDD, a failing test, or a regression test.
- A bug has an obvious cheap local test target; skip unclear, expensive, integration-heavy or unrequested test paths.

## Required input

- Intended and current bug behavior, affected code path, smallest reproduction, and available tests.
- Session file/write/execution capabilities and authorization.

## Output contract

- Focused regression test and smallest production fix when practical.
- Evidence report naming failing-before and passing-after checks, failure output, nearby validation, or why failure evidence could not be demonstrated.

## Ordinary example

For an incorrect empty-input result with an existing local unit test, add the intended-behavior assertion, run it and observe the failure, fix the implementation, then run the same test and report the passing result.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [red-green](../parity/cases/skills/tdd.json)

Fix a bug with an obvious cheap local regression target using TDD. Show a real failing behavior test before fixing production code. Repeat with execution unavailable.

Full capability expectation:

Write a focused intended-behavior test first, observe its failure for the intended reason before changing production code, apply the smallest fix, and observe the same test passing. Report commands, failure output, passing output, and nearby validation. Correct passing or unrelated-failing tests before implementation edits.

Reduced capability expectation:

If a new test is impractical, explain why and use the closest useful executable regression check. Preserve observed failure and passing evidence when available; explicitly state any missing failing-before evidence.

Blocked capability expectation:

If execution is unavailable or denied, mark the proposed failing-before and passing-after sequence unrun. Explain the missing capability and do not claim observed failure, success, or a demonstrated regression fix.

Required observations:

- An authorized code change and a clear cheap local test target.
- Available file access and execution with observed exit status and output for full evidence.

Forbidden claims:

- Claiming an unrun proposed sequence is red-green evidence.
- Calling a structural package check a failing behavior test.
- Changing assertions to match incorrect implementation or forcing expensive infrastructure.
- Assuming execution permission or automatic enforcement of invocation metadata.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Unavailable or denied execution leaves the proposed red-green sequence unrun.
- Impractical tests use the closest useful regression check; do not force broad setup or brittle mocks.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/tdd/SKILL.md`

Destination: [skills/tdd/SKILL.md](../../skills/tdd/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `eeb868e2dfebee528d730a67d7b17498fac4bb85dec2e38bc5c5176aca4d5d2f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/red-green.json](../parity/evidence/chatgpt/red-green.json), [docs/parity/evidence/chatgpt/reproduce-before-fix.json](../parity/evidence/chatgpt/reproduce-before-fix.json).
- codex: `not-run`. Tested release evidence: [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/red-green.json](../parity/evidence/codex/red-green.json), [docs/parity/evidence/codex/reproduce-before-fix.json](../parity/evidence/codex/reproduce-before-fix.json).
