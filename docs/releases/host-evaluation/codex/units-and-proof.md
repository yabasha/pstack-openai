# codex: units-and-proof

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "units-and-proof",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Write a multi-phase pstack plan for a two-PR change. Name file ownership and dependencies, unit tests, live regression against trunk and head, interaction review media, and applicable performance evidence. Run the adapted pstack checker. Repeat with unavailable workers, controls, scheduling, remote setup, model selection and denied writes.",
  "caseDefinition": {
    "id": "units-and-proof",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/multi-phase-plan.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/scripts/check-plan.mjs",
      "skills/poteto-mode/playbooks/prototype.md",
      "skills/poteto-mode/playbooks/autopilot-full.md",
      "skills/poteto-mode/playbooks/autopilot-stack.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/references/bugbot-triage.md",
      "skills/swarm/SKILL.md",
      "skills/technical-writing/SKILL.md",
      "skills/unslop/SKILL.md",
      "skills/principle-never-block-on-the-human/SKILL.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/how/SKILL.md",
      "skills/interrogate/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/no-comments/SKILL.md"
    ],
    "prompt": "Write a multi-phase pstack plan for a two-PR change. Name file ownership and dependencies, unit tests, live regression against trunk and head, interaction review media, and applicable performance evidence. Run the adapted pstack checker. Repeat with unavailable workers, controls, scheduling, remote setup, model selection and denied writes.",
    "requirements": [
      "Preserve plan-only ownership, trivial-change skip, prototype evidence and explicit execution go.",
      "Keep all ordered program, PR sub-blocks, close and appendix sections.",
      "Declare all five capability bindings with evidence and actual worker capacity.",
      "Name per-PR files, dependencies, unit evidence, live artifacts and pass predicates.",
      "Retain the ten independent lane full expectation; explicit reduced or blocked limits preserve omitted scenarios.",
      "Performance uses comparable trunk/head metric, interleaved probe, baseline first and numeric fail rule, or justified non-applicability evidence.",
      "Preserve operator screenshot/video review for interactions and independent review requirements.",
      "Invoke Bun positional read-only checker on a pstack plan only and retain output and exit status.",
      "External setup, scheduling, PR operations and merge require actual separate authorization."
    ],
    "expectedFull": "An authorized saved pstack plan preserves all sections, ten independent live scenarios within observed capacity, per-PR units and evidence, applicable performance or justified non-applicability, operator interaction review and checker output with zero structural problems. Execution waits for explicit go.",
    "expectedReduced": "Authorized sequential exploration or reduced live capacity remains labelled reduced capability with reasons, evidence and omitted scenarios. Manual ticks replace unavailable scheduling without unattended claims. Denied writes return unsaved text. Independent verdict gates remain blocked. A structural checker pass proves format only.",
    "expectedBlocked": "Missing source contracts, unreadable plan, denied execution, unavailable live control or required independent review blocks the affected work. Preserve planned scenarios, disclose the missing dependency and the actual checker outcome. A structurally valid plan with blocked execution can pass; report checker failure only when the checker actually fails; do not fabricate artifacts or start execution.",
    "forbiddenClaims": [
      "Structural checker success proves implementation or host parity.",
      "Sequential role switching provides independent workers or review.",
      "Requested model proves observed model or diversity.",
      "A checked box without receipt proves live success.",
      "Unavailable scheduling proves unattended execution.",
      "Planning permission authorizes external setup, PR creation, push, messaging or merge."
    ],
    "caseFile": "docs/parity/cases/playbooks/multi-phase-plan.json"
  },
  "registry": {
    "caseId": "units-and-proof",
    "caseFile": "docs/parity/cases/playbooks/multi-phase-plan.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/multi-phase-plan.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/scripts/check-plan.mjs",
      "skills/poteto-mode/playbooks/prototype.md",
      "skills/poteto-mode/playbooks/autopilot-full.md",
      "skills/poteto-mode/playbooks/autopilot-stack.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/references/bugbot-triage.md",
      "skills/swarm/SKILL.md",
      "skills/technical-writing/SKILL.md",
      "skills/unslop/SKILL.md",
      "skills/principle-never-block-on-the-human/SKILL.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/how/SKILL.md",
      "skills/interrogate/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/no-comments/SKILL.md"
    ],
    "requiredHosts": [
      "chatgpt",
      "codex"
    ],
    "structuralOnly": false,
    "hostStatus": {
      "chatgpt": "blocked",
      "codex": "blocked"
    },
    "requiredObservations": {
      "pass": [
        "read",
        "inspect-result",
        "execution",
        "isolated-write"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
        "workers"
      ],
      "reduced-pass": [
        "direct",
        "sequential",
        "workers"
      ]
    },
    "requiredPermissions": {
      "pass": [
        "execution",
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [],
  "artifactProjections": [],
  "skippedManifest": [],
  "globalLimits": [
    "Only the supplied frozen f462 source is bound by this reviewed baseline; no later operative tree or current release acceptance is established.",
    "Cloud UI corroborates native dispatch/read/command activity in specified turns, not every exact argument, raw output, exit code or model-captured receipt. Early raw capture gaps and truncation remain explicit.",
    "The two invented cloud timestamps remain retained errors despite appended correction.",
    "Native event metadata proves retained trace identity and locators; per-case independent grade determines qualitative result. File counts, test selfgrades and proxy scripts never generate grades.",
    "Task Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
