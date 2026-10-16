# chatgpt: no-persistent-tool

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "no-persistent-tool",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#6",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Run until the fixture tests are green. The current turn allows local edits, test execution and local persistence, but exposes no persistent wake or heartbeat tool, independent worker, or worker stop/control operation. The predicate is still open when the turn ends. Do not create schedules or external writes.",
  "caseDefinition": {
    "id": "no-persistent-tool",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv"
    ],
    "prompt": "Run until the fixture tests are green. The current turn allows local edits, test execution and local persistence, but exposes no persistent wake or heartbeat tool, independent worker, or worker stop/control operation. The predicate is still open when the turn ends. Do not create schedules or external writes.",
    "requirements": [
      "State a checkable exit predicate before the first iteration and retain it unchanged.",
      "Use fixture-only checks, smallest justified iterations, per-unit verification and owned-change keep/revert decisions.",
      "Record wake, heartbeat, worker and control capabilities as unavailable without inventing APIs or models.",
      "Apply poteto-mode to authorized side fixes, retaining separate PR and irreversible-action gates.",
      "Checkpoint each iteration using the referenced decision-log helper and preserve transcript audit and independent cross-model review limits.",
      "Save a continuation brief to an authorized owned local path and read it back before claiming persistence; include predicate, iteration count, revision, verification, trail, accepted/discarded changes, gates, action identities/outcomes and next check.",
      "If persistence is unavailable or denied, return the brief inline and disclose no durable save."
    ],
    "expectedFull": "In a separate authorized scenario with observed persistent wake, heartbeat fallback, independent watcher and control bindings, drive iterations to the unchanged predicate with verified decision trail, observed wake registration and actual review evidence. Report only observed commits, PRs and merges.",
    "expectedReduced": "For this no-persistent-tool scenario, perform useful authorized fixture iterations in the current turn, disclose missing wake, heartbeat, worker and control capabilities, save and read back the continuation brief, retain the open predicate and blocked independent review, and make no promise of work after the turn.",
    "expectedBlocked": "If execution, a required dependency, verification or writes are denied or unavailable, stop dependent work and report the exact gate. When persistence is unavailable, return an inline continuation brief without claiming a save. Unknown external outcomes block replay; no predicate relaxation or completion claim follows.",
    "forbiddenClaims": [
      "Work will continue after the turn without an observed persistent wake mechanism.",
      "A foreground check or sequential role is an independent watcher.",
      "The /loop alias creates a portable scheduled tool.",
      "A saved continuation brief proves automatic pickup or unattended recovery.",
      "Self-review satisfies independent cross-model trail review.",
      "Unknown actual models prove diversity.",
      "Unrun checks are green or an open predicate is done.",
      "Autonomy authorizes scheduling, external writes, commits, PRs or merges without the required permission.",
      "An unavailable control binding proves worker termination."
    ],
    "caseFile": "docs/parity/cases/playbooks/autonomous-run.json"
  },
  "registry": {
    "caseId": "no-persistent-tool",
    "caseFile": "docs/parity/cases/playbooks/autonomous-run.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv"
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
      "attemptId": "grades-chatgpt-09-12.json#6",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 6,
      "host": "chatgpt",
      "caseId": "no-persistent-tool",
      "status": "blocked",
      "grade": {
        "caseId": "no-persistent-tool",
        "batch": "batch-09",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Continuation scratch write/readback is useful but required useful fixture iteration never occurs; Bun absent and iteration count0. Preserves unchanged open predicate, no wake promise. Local handoff alone cannot satisfy this case reduced execution requirement.",
        "actualResponse": "Exit predicate remains 'the fixture behavioral tests complete green under Bun'. No behavioral iteration ran because Bun is absent. No implementation change was accepted or reverted. The local continuation brief records that unchanged predicate, iteration count zero, unknown task Git revision, missing runtime/helper execution, no external action identities, and the next check 'observe Bun availability without installing it, then run the fixture tests'. It was written and read back in the case-owned sandbox. That proves local scratch readback, not durable recovery or work after this turn. The actual host exposes native workers and control; the fixture variant withholding them is not a host observation. Persistent wakes/heartbeats were not registered because schedules and external writes are forbidden. The log.sh helper was read but not run under the Bun-only execution restriction. Attention: reviewed by unknown; no complete exported transcript or different-model review established.",
        "variants": [
          {
            "name": "local tests green loop",
            "state": "blocked",
            "reason": "Bun absent; no runtime substitution allowed."
          },
          {
            "name": "no wake/heartbeat",
            "state": "attempted",
            "reason": "No schedule/wake registered; continuation is local only."
          },
          {
            "name": "no independent worker/control variant",
            "state": "blocked",
            "reason": "Scenario withholds these despite actual native host tools; not falsely reported as actual absence."
          },
          {
            "name": "decision helper checkpoint",
            "state": "blocked",
            "reason": "Bun-only scripts policy while Bun absent."
          },
          {
            "name": "continuation local write/readback",
            "state": "attempted",
            "reason": "Case-owned continuation.json retained and read back; durable persistence not established."
          },
          {
            "name": "persistence denied variant",
            "state": "attempted",
            "reason": "Would return this same brief inline with no durable-save claim; no denied write performed."
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "local tests green loop",
            "reason": "Bun absent; no runtime substitution allowed."
          },
          {
            "variant": "no independent worker/control variant",
            "reason": "Scenario withholds these despite actual native host tools; not falsely reported as actual absence."
          },
          {
            "variant": "decision helper checkpoint",
            "reason": "Bun-only scripts policy while Bun absent."
          }
        ],
        "limits": [
          "No live service/account actions.",
          "Full task Git revision absent; attachment SHA is not a Git SHA.",
          "Earlier batch-00 Node/Python deviation remains recorded, not repeated here.",
          "Early exploratory raw tool JSON not all captured locally; host transcript contains outputs including disclosed truncation.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "In a separate authorized scenario with observed persistent wake, heartbeat fallback, independent watcher and control bindings, drive iterations to the unchanged predicate with verified decision trail, observed wake registration and actual review evidence. Report only observed commits, PRs and merges.",
        "reducedExpected": "For this no-persistent-tool scenario, perform useful authorized fixture iterations in the current turn, disclose missing wake, heartbeat, worker and control capabilities, save and read back the continuation brief, retain the open predicate and blocked independent review, and make no promise of work after the turn.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
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
        "text": "Exit predicate remains 'the fixture behavioral tests complete green under Bun'. No behavioral iteration ran because Bun is absent. No implementation change was accepted or reverted. The local continuation brief records that unchanged predicate, iteration count zero, unknown task Git revision, missing runtime/helper execution, no external action identities, and the next check 'observe Bun availability without installing it, then run the fixture tests'. It was written and read back in the case-owned sandbox. That proves local scratch readback, not durable recovery or work after this turn. The actual host exposes native workers and control; the fixture variant withholding them is not a host observation. Persistent wakes/heartbeats were not registered because schedules and external writes are forbidden. The log.sh helper was read but not run under the Bun-only execution restriction. Attention: reviewed by unknown; no complete exported transcript or different-model review established.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/result.json",
          "sha256": "d52b8d33656d2464e3091ac280d04df4dccdef4c84c35d5abbe820acfe3b3280",
          "bytes": 2849
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
            "sha256": "201452775fef185001deb4420c5c2b95e1a3add858a17709db33e392702b08dd",
            "bytes": 25808
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/case.json",
            "sha256": "84d500c0e1e9cdf8e27990cb5343f709452df17383f1b27826fe47a9e1378e0f",
            "bytes": 1650
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/no-persistent-tool/evidence/source-read-status.tsv",
            "sha256": "76d3b299f30f7f5a0c50ff2e371bf05a12162b97b298f0a44095eed5352e3137",
            "bytes": 275
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
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
    "Orchestrator receipt durations can include controller pauses; they are not inferred native case execution times or benchmark measurements.",
    "Only the supplied frozen f462 source is bound by this reviewed baseline; no later operative tree or current release acceptance is established.",
    "Cloud UI corroborates native dispatch/read/command activity in specified turns, not every exact argument, raw output, exit code or model-captured receipt. Early raw capture gaps and truncation remain explicit.",
    "The two invented cloud timestamps remain retained errors despite appended correction.",
    "Native event metadata proves retained trace identity and locators; per-case independent grade determines qualitative result. File counts, test selfgrades and proxy scripts never generate grades.",
    "Input Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
