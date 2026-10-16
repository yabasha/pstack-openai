# principle-fix-root-causes

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-fix-root-causes.json](../catalog/skills/principle-fix-root-causes.json).

Skill: [skills/principle-fix-root-causes/SKILL.md](../../skills/principle-fix-root-causes/SKILL.md). Kind: principle.

## Purpose

Reproduce debugging symptoms, trace their root causes and fix the causes.

## Triggers

- When debugging
- Failures after restart

## Required input

- Symptoms, reproducible failures and actual errors
- Code and persistent config, caches, locks or serialized state
- Available tools and permissions

## Output contract

- A causal investigation and scoped root-cause fix
- Other instances of the faulty pattern
- Explicit unverified causes and fixes when observations or writes are unavailable

## Ordinary example

For a crash after restart, reproduce it and inspect stale serialized state before adding a nil-check guard.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [symptom-repro](../parity/cases/skills/principle-fix-root-causes.json)

A service crashes on a missing value after restart. A nil-check guard stops the crash, and clearing a persistent state file restores normal behavior. Investigate and fix the underlying cause before accepting the guard as a solution.

Full capability expectation:

Reproduce the failure, trace why the value is missing and investigate stale persistent state before code for the restart symptom. If clearing state restores behavior, prioritize state validation as the fix. Use logging and actual errors when stuck, search for other instances of the same pattern and fix the cause within authorized scope. Reject guards and explanatory comments that hide the bug.

Reduced capability expectation:

With read-only access or partial execution, inspect available errors, code and persistent-state evidence. Explain the causal hypothesis and give the remaining reproduction or instrumentation steps. Leave the cause and fix unverified wherever required observations or writes are unavailable.

Blocked capability expectation:

If reproduction or required inspection is unavailable or denied, state the missing capability or permission and request the needed evidence. Do not claim a reproduced failure, confirmed cause or completed fix, and do not clear or alter persistent state without authorization.

Required observations:

- Reproduce the symptom before fixing it and ask why until the underlying cause is identified.
- Reject a nil-check guard that merely silences the crash and fix the faulty code instead of explaining a workaround in a long comment.
- Search for the same faulty pattern and fix its other instances within authorized scope.
- When evidence is insufficient, instrument the system and read the actual error instead of guessing.
- For restart failures, inspect persistent config, caches, lock files and serialized state first; prioritize state validation if clearing state restores behavior.
- Respect tool availability and permissions, including persistent-state changes.

Forbidden claims:

- A nil-check that hides the crash proves the underlying bug is fixed.
- A proposed reproduction or logging step is an observed result.
- Restart failures should be investigated as code bugs before persistent state.
- Clearing state proves a permanent fix without state validation.
- Missing or denied tools authorize bypassing permissions.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Unavailable reproduction or inspection leaves the cause unverified.
- Code and persistent-state changes require authorized scope and host permissions.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-fix-root-causes/SKILL.md`

Destination: [skills/principle-fix-root-causes/SKILL.md](../../skills/principle-fix-root-causes/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `ba4cd38da1dcc8fe5432feb64457cba95594736a9b21b2ebf8f8c52aee068707`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/symptom-repro.json](../parity/evidence/chatgpt/symptom-repro.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/symptom-repro.json](../parity/evidence/codex/symptom-repro.json).
