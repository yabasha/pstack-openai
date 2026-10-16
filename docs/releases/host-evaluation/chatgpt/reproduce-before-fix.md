# chatgpt: reproduce-before-fix

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "reproduce-before-fix",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#15",
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
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#15",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 15,
      "host": "chatgpt",
      "caseId": "reproduce-before-fix",
      "status": "blocked",
      "grade": {
        "caseId": "reproduce-before-fix",
        "batch": "batch-10",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Read-only evidence cannot replace observed reproduction/fix/regression. Bun absent; no actual local implementation/proof credited from proposed order.",
        "actualResponse": "The required browser reproduction gate is unverified. The supplied dashboard module exposes visible(orders,status) and exportCsv only; it has no search-input handler, rendered search field, browser harness or launch contract. There is no observed clear-search symptom or failing-before transcript. Therefore I did not patch filtering, blame cache, instrument a nonexistent app, or claim a cache hypothesis was refuted by runtime evidence. Full how/why contracts were read; source observations cannot establish the missing browser mechanism. Bun absence also blocks any cheap local regression execution. The original matching-surface post-fix trigger cannot run because no fix or runnable surface exists. Ordered delivery remains repro artifact, confirmed mechanism, minimal fix, same-trigger check, then separately authorized commit/PR. Nothing shipped.",
        "variants": [
          {
            "name": "matching browser failing-before reproduction",
            "state": "blocked",
            "reason": "No search handler/rendered app/harness and missing matching control companion"
          },
          {
            "name": "binary-search cache hypothesis/instrumentation",
            "state": "blocked",
            "reason": "No reproducible runtime mechanism; no speculative patch to revert"
          },
          {
            "name": "delegated investigation/code change/architect",
            "state": "blocked",
            "reason": "Runtime reproduction and mechanism gates unmet; exact task Git revision absent"
          },
          {
            "name": "passing-after same trigger",
            "state": "blocked",
            "reason": "No fix or runnable browser surface"
          },
          {
            "name": "cheap local test/cheap test absent variant",
            "state": "blocked",
            "reason": "Bun absent; no browser search test target supplied"
          },
          {
            "name": "workers unavailable variant",
            "state": "attempted",
            "reason": "Would retain sequential reduced source review, never claim required delegation"
          },
          {
            "name": "browser denied variant",
            "state": "blocked",
            "reason": "No browser proof permitted or possible in variant"
          },
          {
            "name": "Opening a PR and delivery commits",
            "state": "blocked",
            "reason": "External writes forbidden; no verification evidence"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "matching browser failing-before reproduction",
            "reason": "No search handler/rendered app/harness and missing matching control companion"
          },
          {
            "variant": "binary-search cache hypothesis/instrumentation",
            "reason": "No reproducible runtime mechanism; no speculative patch to revert"
          },
          {
            "variant": "delegated investigation/code change/architect",
            "reason": "Runtime reproduction and mechanism gates unmet; exact task Git revision absent"
          },
          {
            "variant": "passing-after same trigger",
            "reason": "No fix or runnable browser surface"
          },
          {
            "variant": "cheap local test/cheap test absent variant",
            "reason": "Bun absent; no browser search test target supplied"
          },
          {
            "variant": "browser denied variant",
            "reason": "No browser proof permitted or possible in variant"
          },
          {
            "variant": "Opening a PR and delivery commits",
            "reason": "External writes forbidden; no verification evidence"
          }
        ],
        "limits": [
          "Bun unavailable; no Node/Python substitute.",
          "Supplied freeze is not verified installed/task Git HEAD.",
          "No live accounts/services/writes/settings/schedules.",
          "Some initial tool raw metadata omitted from local export and some large outputs truncated, explicitly not reconstructed.",
          "Prior Node/Python deviation retained, not repeated.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Observed independent investigation and implementation return inspected artifacts at the assigned revision. Runtime evidence confirms the specific mechanism before design fan-out. Matching browser observations show stale rows before the bounded fix and correctly reset rows afterward under the same trigger. Refuted speculation is reverted. A cheap regression check fails before the fix and passes afterward. With actual delivery authorization and complete dependencies, the ordered commits and inspected PR demonstrate delivery. The reply includes verbatim observed outputs, root cause and verification. Unauthorized external delivery remains unperformed.",
        "reducedExpected": "Unavailable workers permit authorized sequential investigation and local implementation with reduced capability disclosed, while required independent delegation remains unsatisfied. Missing repeated-execution support allows bounded in-session hypothesis passes without background claims. An impractical new test is skipped with a reason and actual closest regression evidence. Without delivery authorization, return checked local artifacts and the failing-repro-before-fix order. Unknown model observations supply no diversity claim.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "reviewedBy": "grade_contract_audit"
          },
          {
            "observation": "review-outcome",
            "evidence": "grades-chatgpt-09-12.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ]
      },
      "topLevelContext": {
        "scope": "Actual ChatGPT Work remaining batches09..12,30cases",
        "gradingNotes": [
          "Independent outcome review of retained actual responses/variants/source artifacts, not exported selfgrades.",
          "Native UI aggregate reads/commands/worker activity supplied by parent; exact model-captured logs treated with explicit provenance gaps.",
          "No proxy programs/fixture verdicts count as actual service or worker results.",
          "Missing taskGit and unavailable Bun remain required-method blockers; tools themselves not declared absent.",
          "All named requested variants must be addressed before full. No full awarded in this set.",
          "Old original source path failures retained; documented fallback source reads not automatically rejected.",
          "history-evidence is included because actual cloud batch09 contains it; do not count duplicate historical case twice when aggregating target coverage."
        ]
      },
      "response": {
        "text": "The required browser reproduction gate is unverified. The supplied dashboard module exposes visible(orders,status) and exportCsv only; it has no search-input handler, rendered search field, browser harness or launch contract. There is no observed clear-search symptom or failing-before transcript. Therefore I did not patch filtering, blame cache, instrument a nonexistent app, or claim a cache hypothesis was refuted by runtime evidence. Full how/why contracts were read; source observations cannot establish the missing browser mechanism. Bun absence also blocks any cheap local regression execution. The original matching-surface post-fix trigger cannot run because no fix or runnable surface exists. Ordered delivery remains repro artifact, confirmed mechanism, minimal fix, same-trigger check, then separately authorized commit/PR. Nothing shipped.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/result.json",
          "sha256": "193b3ebcdef5b3c78f1f8505cb618bb07e3c6d2f29030d04210031f6b8e42dfd",
          "bytes": 3024
        },
        "extraction": "Actual response field when present; otherwise complete retained JSON"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "sha256": "667b5681288f125d3857df0388ae65288954542d8545c2b44a420635baa66c49",
            "bytes": 430462
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "sha256": "573460e5da46c0ef316385566ec2c9a9e86bc65be4ba7bf24d3449eec1bce3f4",
            "bytes": 24603
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/case.json",
            "sha256": "2fa1c4029652ab7a9a7e6a7ddb933f48ef271b5b6b71dbbd3dc57a0679a91301",
            "bytes": 4502
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/reproduce-before-fix/evidence/source-read-status.tsv",
            "sha256": "56e701fe8423e10262f24e2b7d97a6837c9cbcd773acd29d1c81d211d723ea2b",
            "bytes": 1292
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
              "reviewedBy": "grade_contract_audit"
            },
            {
              "observation": "review-outcome",
              "evidence": "grades-chatgpt-09-12.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
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
