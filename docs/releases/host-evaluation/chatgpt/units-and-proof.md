# chatgpt: units-and-proof

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "units-and-proof",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#26",
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
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#26",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 26,
      "host": "chatgpt",
      "caseId": "units-and-proof",
      "status": "reduced-pass",
      "grade": {
        "caseId": "units-and-proof",
        "batch": "batch-12",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Actual saved twoPR plan with owned dependencies, explicit unchecked boxes/proposed2percent criterion and open10live scenarios. Bun checker127 means format not verified; no execution-go assumed.",
        "actualResponse": "Saved a two-PR planning draft at docs/plan.md for correct filtered CSV export. CSV-1 owns a serializer, literal behavior tests and benchmark probe; CSV-2 depends on CSV-1 and owns dashboard export integration, UI fixture and empty-state feedback. The plan keeps ordered program/PR/close/appendix sections, five capability bindings, every implementation and proof box unchecked, zero live lanes, and the full ten unexercised scenarios in risks. It requires comparable baseline-first interleaved timings and rejects invalid ratios or failed output/work checks. Planned numeric adoption threshold is a 2 percent regression limit, an explicit proposed criterion, not a measured result or approved product budget. Interaction change holds screenshot/video and operator review gates. Actual Bun positional check-plan invocation returned exit127 'bun: command not found', so format validation is unverified. No Node/Python fallback, checker success, implementation go, scheduler, remote setup, PR, commit or merge occurred. Exact task Git SHA, runnable controls and complete independent plan review remain open.",
        "variants": [
          {
            "name": "plan-only owner/two PR ownership and dependency",
            "state": "attempted",
            "reason": "Authored retained docs/plan.md, no implementation"
          },
          {
            "name": "trivial-change skip",
            "state": "attempted",
            "reason": "Not used because specified two-PR scope and separate integration/proof concerns"
          },
          {
            "name": "prototype prior evidence",
            "state": "blocked",
            "reason": "Bun absent; no prototype branch/SHA/screenshots claimed"
          },
          {
            "name": "five capability bindings and capacity",
            "state": "attempted",
            "reason": "Plan separates exposed workers from missing live control/setup permissions and unknown model identities"
          },
          {
            "name": "ordered sections/unit/live/perf review gates",
            "state": "attempted",
            "reason": "Draft retains blocks, all checks unchecked; checker not validated"
          },
          {
            "name": "full ten independent live lane expectation",
            "state": "blocked",
            "reason": "No matching app/driver and no ten-lane proof; ten omitted scenarios explicitly retained"
          },
          {
            "name": "baseline/trunk/head interleaved perf and numeric fail rule",
            "state": "blocked",
            "reason": "Method and proposed 2 percent threshold authored, no measured result/revision"
          },
          {
            "name": "interaction screenshots/video/operator review",
            "state": "blocked",
            "reason": "No actual render/driver/media or approval"
          },
          {
            "name": "Bun positional checker",
            "state": "attempted",
            "reason": "Actual command returned exit127, no script execution or format verdict"
          },
          {
            "name": "unavailable workers variant",
            "state": "attempted",
            "reason": "Plan labels reduced sequential review and independence gate unsatisfied"
          },
          {
            "name": "controls unavailable/denied variant",
            "state": "blocked",
            "reason": "Zero live lanes; no static screenshot substitute"
          },
          {
            "name": "scheduling/remote setup/model selection unavailable variants",
            "state": "attempted",
            "reason": "No enabling/scheduling, inherit request actual unknown"
          },
          {
            "name": "denied writes variant",
            "state": "attempted",
            "reason": "Would provide same plan inline, no durable-save claim; actual authorized sandbox draft retained"
          },
          {
            "name": "external PR/merge delivery and explicit execution go",
            "state": "blocked",
            "reason": "Planning only, no live writes or go supplied"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "prototype prior evidence",
            "reason": "Bun absent; no prototype branch/SHA/screenshots claimed"
          },
          {
            "variant": "full ten independent live lane expectation",
            "reason": "No matching app/driver and no ten-lane proof; ten omitted scenarios explicitly retained"
          },
          {
            "variant": "baseline/trunk/head interleaved perf and numeric fail rule",
            "reason": "Method and proposed 2 percent threshold authored, no measured result/revision"
          },
          {
            "variant": "interaction screenshots/video/operator review",
            "reason": "No actual render/driver/media or approval"
          },
          {
            "variant": "controls unavailable/denied variant",
            "reason": "Zero live lanes; no static screenshot substitute"
          },
          {
            "variant": "external PR/merge delivery and explicit execution go",
            "reason": "Planning only, no live writes or go supplied"
          }
        ],
        "limits": [
          "No Bun runtime available; no Node/Python substitute.",
          "All original named source read failures retained. Documented role alternatives explicitly separate.",
          "Task Git SHA unavailable and package freeze not independently verified host revision.",
          "No live external accounts/messages/trackers/PRs/schedules/credentials/settings.",
          "Initial raw host receipt export incomplete, some large outputs truncated; full source bytes retained but not claimed complete raw metadata.",
          "Earlier batch-00 Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "An authorized saved pstack plan preserves all sections, ten independent live scenarios within observed capacity, per-PR units and evidence, applicable performance or justified non-applicability, operator interaction review and checker output with zero structural problems. Execution waits for explicit go.",
        "reducedExpected": "Authorized sequential exploration or reduced live capacity remains labelled reduced capability with reasons, evidence and omitted scenarios. Manual ticks replace unavailable scheduling without unattended claims. Denied writes return unsaved text. Independent verdict gates remain blocked. A structural checker pass proves format only.",
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
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
        "text": "Saved a two-PR planning draft at docs/plan.md for correct filtered CSV export. CSV-1 owns a serializer, literal behavior tests and benchmark probe; CSV-2 depends on CSV-1 and owns dashboard export integration, UI fixture and empty-state feedback. The plan keeps ordered program/PR/close/appendix sections, five capability bindings, every implementation and proof box unchecked, zero live lanes, and the full ten unexercised scenarios in risks. It requires comparable baseline-first interleaved timings and rejects invalid ratios or failed output/work checks. Planned numeric adoption threshold is a 2 percent regression limit, an explicit proposed criterion, not a measured result or approved product budget. Interaction change holds screenshot/video and operator review gates. Actual Bun positional check-plan invocation returned exit127 'bun: command not found', so format validation is unverified. No Node/Python fallback, checker success, implementation go, scheduler, remote setup, PR, commit or merge occurred. Exact task Git SHA, runnable controls and complete independent plan review remain open.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/result.json",
          "sha256": "f4868a566a0b8161bc3fecd479c774f88d75008e2132e815676c5b9122db66c3",
          "bytes": 4820
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
            "sha256": "7055437f341d58caac31e043099641b2579ad0ed167b3da14a08a06a46c5e68d",
            "bytes": 25602
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/case.json",
            "sha256": "2602d8b7d3ba1ccbd43db37677f03eaa39ec5b02b69aa7a4f61755e89b9880de",
            "bytes": 2424
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/units-and-proof/evidence/source-read-status.tsv",
            "sha256": "eaca7efe8594a365a0f27915acd0cc491692499c531c6c2f6784d78641c8d57c",
            "bytes": 940
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
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
