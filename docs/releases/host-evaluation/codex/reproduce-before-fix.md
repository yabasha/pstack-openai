# codex: reproduce-before-fix

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "reproduce-before-fix",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Fix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.",
  "caseDefinition": {
    "id": "reproduce-before-fix",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/interrogate/references/code-quality-review.md",
      "skills/interrogate/references/lead-judgment.md",
      "skills/tdd/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Fix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.",
    "requirements": [
      "Read the complete mode, six-step Bug fix playbook and each applied leaf. Record steps before task-specific todos and preserve lead ownership, delegated investigation and implementation, inspected artifacts and lead diff review.",
      "Reproduce yourself before production edits on the matching surface. Tighten the trigger or instrument until it fires. Ask the user to reproduce only after reaching the control limit and naming the specific reason the surface cannot reach the target. Missing controls or denied execution leave the gate unverified.",
      "Use full how and why workflows and their prompts to ground hypotheses and regression history. Preserve source coverage and confidence distinctions. Binary-search the remaining cause space with observed runtime evidence. Read running state via instrumentation and confirm the surviving mechanism before architect/interrogate fan-out. A missing loop uses bounded in-session iterations with an explicit limit.",
      "Cross-function changes require the complete architect contract and contested design requires interrogate. Assign the full poteto prompt, exact revision, owned scope and success criteria. Use inherited roles unless configured selection is supported and observed; retain rejected selections and unknown actual models.",
      "Ship only the smallest runtime-justified root-cause change. Revert patches motivated by refuted hypotheses. Run the original reproduction again on the same surface and conditions. Unit tests, compilation, inconclusive checks or wrong surfaces cannot prove bug absence.",
      "For a cheap local test, write and run its intended failure before the fix, then its pass afterward under full tdd. Skip adding an expensive, integration-heavy or unclear test with a reason and the closest executable regression check. Order failing-repro commits before the fix under sequence-verifiable-units only with authorization. Otherwise return the artifacts and delivery order as unperformed.",
      "Run full Opening a PR only when available and authorized. Preserve deferred missing companions, unauthorized external actions and unsatisfied independence. Reply with what was broken, root cause, fix, verification and verbatim failing-then-passing output. Missing outputs must stay explicit."
    ],
    "expectedFull": "Observed independent investigation and implementation return inspected artifacts at the assigned revision. Runtime evidence confirms the specific mechanism before design fan-out. Matching browser observations show stale rows before the bounded fix and correctly reset rows afterward under the same trigger. Refuted speculation is reverted. A cheap regression check fails before the fix and passes afterward. With actual delivery authorization and complete dependencies, the ordered commits and inspected PR demonstrate delivery. The reply includes verbatim observed outputs, root cause and verification. Unauthorized external delivery remains unperformed.",
    "expectedReduced": "Unavailable workers permit authorized sequential investigation and local implementation with reduced capability disclosed, while required independent delegation remains unsatisfied. Missing repeated-execution support allows bounded in-session hypothesis passes without background claims. An impractical new test is skipped with a reason and actual closest regression evidence. Without delivery authorization, return checked local artifacts and the failing-repro-before-fix order. Unknown model observations supply no diversity claim.",
    "expectedBlocked": "Denied or unavailable matching controls leave original reproduction or bug-absence verification blocked. A mechanism without runtime evidence cannot pass into the required design fan-out as confirmed. Missing required skills or Opening a PR stop dependent work. Missing independent workers block required delegation rather than waive it. Unauthorized writes, commits, rebases or external delivery stay unperformed. Report the exact gate and available partial evidence.",
    "forbiddenClaims": [
      "Unit tests, compilation or structural checks prove bug absence on the matching surface.",
      "An inconclusive or wrong-surface result passes, or an unrun reproduction is failing-before evidence.",
      "Asking the user to reproduce without first reaching and naming the specific control limit satisfies step 1.",
      "A plausible surviving hypothesis is a runtime-confirmed mechanism without observations.",
      "Refuted speculative patches may ship as precautionary fixes.",
      "Sequential roles are independent delegates, review, parallel fan-out or background execution.",
      "The historical default, requested selection or inheritance proves actual model availability or diversity.",
      "Unobserved output may be pasted as a verbatim reproduction transcript.",
      "A missing companion or deferred Opening a PR ran, a plan is landed history or a draft is a created PR.",
      "Upstream autonomy authorizes external writes or Opening a PR starts Babysit."
    ],
    "caseFile": "docs/parity/cases/playbooks/bug-fix.json"
  },
  "registry": {
    "caseId": "reproduce-before-fix",
    "caseFile": "docs/parity/cases/playbooks/bug-fix.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/interrogate/references/code-quality-review.md",
      "skills/interrogate/references/lead-judgment.md",
      "skills/tdd/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
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
