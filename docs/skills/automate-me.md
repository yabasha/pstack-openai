# automate-me

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/automate-me.json](../catalog/skills/automate-me.json).

Skill: [skills/automate-me/SKILL.md](../../skills/automate-me/SKILL.md). Kind: skill.

## Purpose

Draft or revise a personal mode from scoped evidence and user preferences.

## Triggers

- /automate-me
- automate me
- create/update/refresh my -mode skill
- turn/capture my preferences or working style into a skill
- wanting agents to follow how the user works

## Required input

- Existing personal mode and last-edit boundary
- Authorized workspace-scoped history
- User answers and baseline acceptance evidence

## Output contract

- Evidence-strength findings
- Reviewable personal-mode draft and feedback revisions
- Explicit capability and authorization limits

## Ordinary example

After baseline acceptance, update an existing jay-mode from newer workspace history, retain uncontradicted preferences and show the draft before an authorized local edit.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [existing-personal-mode](../parity/cases/skills/automate-me.json)

Update my existing jay-mode skill. Preserve unchanged preferences, use only this workspace history, label evidence strength, and show me the draft before any write or shipping action. Do not schedule or create anything remotely.

Full capability expectation:

After the baseline prerequisite is met, preserve uncontradicted existing sections and category, mine only newer scoped history, cross-check independent slices, distinguish strong repeated evidence from weak lone signals and direct user statements, show a draft and incorporate feedback before authorized local edits. No scheduling or remote creation.

Reduced capability expectation:

After the baseline prerequisite is met, disclose unavailable workers, history or create-skill. Use authorized sequential mining or supplied scoped evidence and the bundled authoring playbook as reduced capability. Show a draft with evidence limits and preserve existing preferences. Do not claim independent mining or missing companions ran.

Blocked capability expectation:

If baseline acceptance is incomplete, explain the workflow without drafting or editing personal configuration. If existing mode, scoped history boundary, required authoring contract or write permission cannot be established, stop dependent work and identify the missing prerequisite. No scheduling, remote creation or unauthorized personal write.

Required observations:

- Read the existing mode and its last-edit boundary
- Baseline reviewed dispositions and per-host supported behavior evidence or explicit blocks precede personal-mode drafting or edits, separately from authorization
- Workspace-scoped history and explicit user answers
- Observed authoring, question, history and worker capabilities; declared missing companions

Forbidden claims:

- Structural checks prove host behavior
- Existing preferences replaced without contradiction or user approval
- Unrelated private workspace history mined
- Weak evidence presented as a repeated preference
- create-skill or independent workers ran when unavailable
- Scheduling, remote creation, commit, push or PR implied by draft approval
- Authorization alone satisfies the baseline prerequisite

## Dependencies

- [skills/unslop/SKILL.md](../../skills/unslop/SKILL.md)
- [skills/poteto-mode/SKILL.md](../../skills/poteto-mode/SKILL.md)
- [skills/poteto-mode/playbooks/authoring-a-skill.md](../../skills/poteto-mode/playbooks/authoring-a-skill.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)

## Host limits

- Personal drafting and edits wait for all reviewed baseline dispositions and per-host supported-behavior evidence or explicit blocks.
- create-skill and structured questions require observed exposed companions or a declared reduced fallback.
- Sequential mining does not prove independent workers. Missing scoped history limits evidence.
- Scheduling and remote creation are outside the flow. Commit, push and PR each need separate authorization.
- The authoring playbook is present and reviewed. Both hosts remain not-run; external authoring companions still require discovery.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/automate-me/SKILL.md`

Destination: [skills/automate-me/SKILL.md](../../skills/automate-me/SKILL.md).

Upstream commit: `e5136d82418d2db3165ea1050d17577cd618cc05`. SHA-256: `30b35f3628c4fd8c11af0ada06d14cdc3b28901810caca2480f627d4d21acfbe`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
