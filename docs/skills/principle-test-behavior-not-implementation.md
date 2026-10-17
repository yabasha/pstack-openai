# principle-test-behavior-not-implementation

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-test-behavior-not-implementation.json](../catalog/skills/principle-test-behavior-not-implementation.json).

Skill: [skills/principle-test-behavior-not-implementation/SKILL.md](../../skills/principle-test-behavior-not-implementation/SKILL.md). Kind: principle.

## Purpose

Keep tests that observe user-visible behavior and catch defects instead of asserting implementation details.

## Triggers

- When writing, changing or keeping a test

## Required input

- Test code, subject code and observable results
- Available file access, test execution and permissions

## Output contract

- Concrete-input assertions against literal output or observable effects
- Rewritten or deleted weak tests, with table relation and compile-time checks retained

## Ordinary example

Call slugify with Hello, World! and assert hello-world; confirm that an empty function fails the assertion when execution is available.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [empty-function](../parity/cases/skills/principle-test-behavior-not-implementation.json)

Review a slugify test that only checks its mock was called. Rewrite it to call slugify with Hello, World! and check its literal output. Replace slugify with a function that returns nothing and determine whether the test catches the defect. Also review absence-only assertions, self-referential expectations, constant pins and fixture-only assertions, while preserving table relation and compile-time checks.

Full capability expectation:

With authorized test access and execution, rewrite the assertion as expect(slugify("Hello, World!")).toBe("hello-world"). Run it against the working subject and against an empty function; the empty function fails. Identify and repair or delete the five weak test shapes while preserving the stated exceptions.

Reduced capability expectation:

If execution is unavailable, provide the rewritten test and explain why undefined differs from the literal expected output. State that the empty-function failure has not been observed.

Blocked capability expectation:

If the test or subject cannot be inspected, identify the missing access or permission and request the relevant code. Do not claim a rewrite or execution result.

Required observations:

- Call the subject inside the test body with concrete input and assert a literal observable output or effect.
- The rewritten test fails when the function returns nothing.
- For absence assertions, assert presence on another input in the same test; test the mechanism reading a constant instead of pinning it.
- For mocks, assert the received payload or resulting state; delete tests without a meaningful behavior assertion.
- Keep table relation tests and compile-time checks in *.test-d.ts files.

Forbidden claims:

- Mock call counts alone prove user-visible behavior.
- A test that still passes with an empty subject catches that defect.
- Static review or a proposed assertion proves a test ran and failed.
- Every table relation or compile-time test must be deleted.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing execution leaves the proposed empty-function check unverified.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-test-behavior-not-implementation/SKILL.md`

Destination: [skills/principle-test-behavior-not-implementation/SKILL.md](../../skills/principle-test-behavior-not-implementation/SKILL.md).

Upstream commit: `182f2ce414e83224915c190d2f63239c1608d0a5`. SHA-256: `f7223698623b6a26fea49c751e466b38e6691b1f32ce841d3983e7ffbe2b74a6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
