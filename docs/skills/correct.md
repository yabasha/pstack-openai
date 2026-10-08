# correct

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/correct.json](../catalog/skills/correct.json).

Skill: [skills/correct/SKILL.md](../../skills/correct/SKILL.md). Kind: workflow.

## Purpose

Find repeated repository mistake classes and prevent recurrence through architecture, types, lint or CI, tests, then judgment rules.

## Triggers

- /correct
- An operator correction to a repeated repository mistake

## Required input

- Recent commits, reverts, review comments, agent instruction files and workaround comments
- Current correction and authorized repository scope

## Output contract

- Repository enforcement changes and real past-mistake checks when authorized
- Rule/enforcement table changes after review and explicit permission
- Each class with evidence, chosen enforcement level and why higher levels did not work

## Ordinary example

Use /correct to investigate two reverted changes that copied the same unsafe state owner, then propose one owner and prove the old mistake fails.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [user-correction](../parity/cases/skills/correct.json)

Use /correct after I correct a repeated repository mistake. Inspect the available history and propose enforcement. Durable skill edits require my review and permission.

Full capability expectation:

With authorized repository reads, writes and execution, fix the most frequent repeated classes, prove checks against real past mistakes, retain the rule table and report each class with evidence, selected level and why higher levels did not work. Obtain review and explicit permission for durable skill or instruction edits and authorization for each commit.

Reduced capability expectation:

If writes, execution or CI are unavailable or unauthorized, provide scoped findings and proposed enforcement, declare gaps, and retain the reply contract without claiming edits, failing checks, commits or CI success.

Blocked capability expectation:

If repository evidence is unavailable, identify the missing access and request the relevant evidence. Do not invent repeated classes or edit durable skills.

Required observations:

- Read recent commits, reverts, review comments, instruction files and workaround comments when available; declare gaps.
- Count a mistake class after two occurrences and prioritize architecture, types, lint or CI, behavior tests, then documentation for judgment calls.
- Prove new checks fail on real past mistakes and use the same local and CI command when authorized execution is available.
- Retain the rule/enforcement table, inline exceptions with reason, expiry and human approval, and the source reply contract.
- Require explicit review and permission before changing durable skills or agent instructions; commit and external actions require authorization.

Forbidden claims:

- A single occurrence proves a repeated class.
- Documentation alone prevents deterministic mistakes.
- Unobserved checks or CI passed.
- A correction authorizes durable skill edits, commits or external writes.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)

## Host limits

- Missing history limits class evidence
- Unavailable or unauthorized writes, execution or CI reduce the workflow to findings and proposals
- Durable skill and agent instruction edits require review and explicit permission; commits and external actions require authorization
- Host behavior has not been tested
- Preserve disable-model-invocation metadata without assuming host enforcement.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/correct/SKILL.md`

Destination: [skills/correct/SKILL.md](../../skills/correct/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `bf482bacc972b3f124a4af8bf9364b4b3e280cb5845e44c326ea4f4565e5c904`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `blocked`. Tested release evidence: [docs/parity/evidence/chatgpt/package-discovery.json](../parity/evidence/chatgpt/package-discovery.json), [docs/parity/evidence/chatgpt/user-correction.json](../parity/evidence/chatgpt/user-correction.json).
- codex: `blocked`. Tested release evidence: [docs/parity/evidence/codex/package-discovery.json](../parity/evidence/codex/package-discovery.json), [docs/parity/evidence/codex/user-correction.json](../parity/evidence/codex/user-correction.json).
