# setup-pstack

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/setup-pstack.json](../catalog/skills/setup-pstack.json).

Skill: [skills/setup-pstack/SKILL.md](../../skills/setup-pstack/SKILL.md). Kind: workflow.

## Purpose

Configure pstack model choices per role and reasoning budget with confirmed availability and an explicit persistence gate.

## Triggers

- /setup-pstack
- configure pstack models
- pstack budget
- changing pstack's model choices

## Required input

- Available session models and supported efforts, current overrides, budget and role choices
- Explicit authorization and supported destination for a persistent override

## Output contract

- Reviewed complete role table with budget, retired roles and capability limits
- Verified persistent override only when authorized and supported; otherwise session-only proposal

## Ordinary example

Run /setup-pstack when model enumeration is unavailable; retain inherited choices, reject an unknown slug, and return a session-only table without writing personal configuration.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [unknown-model](../parity/cases/skills/setup-pstack.json)

Run /setup-pstack with no model enumeration, an unknown requested model slug, and no authorization to change personal host configuration.

Full capability expectation:

Recognize that enumeration is unavailable, reject the unknown slug, retain inherited choices for every role, and show the budget and complete role table for review. Do not write personal configuration because authorization is absent. Report model and persistence limits, keep actual model values unknown, and label the session-only result reduced capability; successful safety handling does not establish full persistent setup support.

Reduced capability expectation:

When enumeration or portable persistence is unavailable, keep every role inherited, show a session-only proposal and disclose reduced capability. Aliases count toward panel fan-out; no personal configuration is written.

Blocked capability expectation:

If the user requires the unknown slug or an unavailable or unauthorized persistent configuration, stop that selection or write, explain the missing capability, and retain inherited choices without claiming persistence.

Required observations:

- Discover exposed model and effort selection and authorized persistence capabilities.
- Default every role to inherit-parent when availability is unknown.
- Confirm the budget and every role before an explicitly authorized configuration write.

Forbidden claims:

- An unknown or documentation-example slug is available.
- A personal host configuration was written incidentally.
- A portable plugin installs an always-applied host rule.
- A requested model proves the actual model or model diversity.
- Structural validation establishes host behavior.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [skills/create-verification-skill/SKILL.md](../../skills/create-verification-skill/SKILL.md)

## Host limits

- Unknown availability defaults to inherited roles
- Persistent always-applied overrides require a verified host mechanism and explicit write authorization
- Requested models and budgets do not establish actual models, supported effort, diversity or worker independence
- The verification-skill leaf is present and reviewed; host behavior remains not-run

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/setup-pstack/SKILL.md`

Destination: [skills/setup-pstack/SKILL.md](../../skills/setup-pstack/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `d61b47256a18155a81c8e5ef95e3cc6569ce8c18317c35c4dd9c8015cf68cb59`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
