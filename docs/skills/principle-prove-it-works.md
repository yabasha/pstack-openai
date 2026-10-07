# principle-prove-it-works

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-prove-it-works.json](../catalog/skills/principle-prove-it-works.json).

Skill: [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md). Kind: principle.

## Purpose

Verify task outputs against the real artifact before declaring completion.

## Triggers

- After completing a task, before declaring done

## Required input

- task outputs and the real feature, process or stored value
- Available inspection and execution tools and permissions

## Output contract

- Direct observations and visible verification artifacts
- Explicit unverified outputs when direct checks are unavailable

## Ordinary example

After a feature compiles, run the feature and read its actual stored value before declaring it complete.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [false-success](../parity/cases/skills/principle-prove-it-works.json)

A worker says the feature is done because it compiles. A screenshot is cached, file timestamps are fresh and a derived status says the process is alive. Decide whether completion is supported and verify the actual feature, process and stored value before reporting success.

Full capability expectation:

With authorized artifact access and execution, directly inspect or run the feature, check process liveness and read the actual value. Reject compile-only and worker-reported success. Run and retain a deterministic check when possible, keep evidence visible to the human and commit the trail only for large or complex work that needs later audit.

Reduced capability expectation:

When only some checks are available, report the direct observations and their limits. Provide the remaining verification procedure or script without claiming it ran; keep the affected output unverified.

Blocked capability expectation:

If the required real artifact cannot be read or executed, identify the missing capability or permission and withhold completion for that output. Do not replace evidence with cached screenshots, timestamps, compilation or self-report.

Required observations:

- Reject completion without real artifact evidence.
- Inspect the real feature, process liveness and actual stored value instead of proxies or self-reports.
- When verification fails, examine the observation method before blaming the system.
- Use a deterministic repeatable check when possible and retain its visible output for reviewer reruns.
- Respect available tools and permissions; disclose any unperformed check.

Forbidden claims:

- Compilation alone proves the feature works.
- Worker self-report, fresh timestamps, cached screenshots or derived state prove completion.
- A proposed or unexecuted script counts as observed verification.
- Missing or denied tools can be bypassed or treated as a successful check.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [skills/show-me-your-work/SKILL.md](../../skills/show-me-your-work/SKILL.md)

## Host limits

- Unavailable or denied direct checks leave the affected outputs unverified.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-prove-it-works/SKILL.md`

Destination: [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `ec79a15025bac8d33d62011c54f3b612733fd2a024e623b531b3637aa75070e2`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
