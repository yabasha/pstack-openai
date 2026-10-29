# interrogate

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/interrogate.json](../catalog/skills/interrogate.json).

Skill: [skills/interrogate/SKILL.md](../../skills/interrogate/SKILL.md). Kind: workflow.

## Purpose

Try to break a reviewed change in isolated copies and retain only findings proven by a lead rerun.

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

- Intent, Reviewers, Findings and Dropped, plus capability limits
- Exact snapshot, command, environment, output and lead rerun evidence
- Explicit unverified observations in reduced static review

## Ordinary example

An adversary reproduces a wrong null-input result in an isolated snapshot; the lead reruns it and drops a second claim that passes.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [adversarial-review](../parity/cases/skills/interrogate.json)

Review a scoped dirty branch in isolated copies. An adversary supplies a real failing repro, another claim passes on rerun, and one claim cannot run. Repeat with denied writes and unavailable workers.

Full capability expectation:

Independent authorized adversaries reproduce against verified isolated snapshots. The lead reruns each command, retains only failures of the stated intent and reports Intent, Reviewers, Findings and Dropped with exact evidence.

Reduced capability expectation:

Sequential authorized reproduction or read-only static inspection is explicitly reduced. Unrun observations remain unverified. No verified findings does not prove no bugs.

Blocked capability expectation:

Missing scope, unsafe isolation, denied required execution or unavailable reproduction inputs block that gate. Preserve the original checkout and report the missing capability.

Required observations:

- Capture and verify the exact base plus scoped staged, unstaged and untracked bytes without changing the original checkout.
- Assign isolated authorized reproduction outputs and inspect terminal worker results; requested models never prove diversity.
- Require actual command, environment, exit code, expected and actual output plus a lead rerun before retaining a verified finding.
- Deduplicate verified failures by root cause and list dropped counts/reasons per adversary.
- Honor read-only requests with a reduced static review and unverified observations, never fabricated runs or automatic fixes.

Forbidden claims:

- Agreement or static citations establish a reproduced failure.
- A read-only request authorizes repro writes.
- Requested models prove actual diversity.
- Structural checks establish host behavior.
- Review authorizes automatic fixes or external changes.

## Dependencies

- [skills/arena/SKILL.md](../../skills/arena/SKILL.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Independent adversaries and writable repro isolation require observed authorized tools.
- Read-only review remains reduced and unrun suspicions are not verified findings.
- Unknown models do not establish diversity.
- The legacy reference files remain for staged-source accounting, not required rubric inputs.
- Neither host workflow has been observed for this overlay.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/interrogate/SKILL.md`

Destination: [skills/interrogate/SKILL.md](../../skills/interrogate/SKILL.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3f3c2e9b8cf6b180dba9f32a4aff85e5691b09805232468e37a0ba45437a9984`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
