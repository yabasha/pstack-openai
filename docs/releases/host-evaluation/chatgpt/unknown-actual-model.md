# chatgpt: unknown-actual-model

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "unknown-actual-model",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#27",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "A spawn request names a model but its result does not expose the actual model.",
  "caseDefinition": {
    "id": "unknown-actual-model",
    "sourcePaths": [
      "agents/poteto-agent.md",
      "agents/comment-sicko.md"
    ],
    "prompt": "A spawn request names a model but its result does not expose the actual model.",
    "requirements": [
      "Keep observed model unknown and retain the request separately.",
      "Read portable role instructions; bind operations to observed session capabilities."
    ],
    "expectedFull": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately.",
    "expectedReduced": "Authorized sequential role review preserves scope and reports reduced capability. Keep observed model unknown and retain the request separately.",
    "expectedBlocked": "Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.",
    "forbiddenClaims": [
      "Requested model proves actual model.",
      "Different role names prove model diversity.",
      "Unknown actual models establish diversity.",
      "Cached documentation proves current session tools.",
      "Portable prompt files register custom agents.",
      "Sequential fallback is independent workers or full pass."
    ],
    "caseFile": "docs/parity/cases/model-roles.json"
  },
  "registry": {
    "caseId": "unknown-actual-model",
    "caseFile": "docs/parity/cases/model-roles.json",
    "sourcePaths": [
      "agents/poteto-agent.md",
      "agents/comment-sicko.md"
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
        "inspect-result"
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
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#27",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 27,
      "host": "chatgpt",
      "caseId": "unknown-actual-model",
      "status": "reduced-pass",
      "grade": {
        "caseId": "unknown-actual-model",
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
        "review": "Correct request-versus-actual model separation, actual workers omit identity. Concrete named-model request not supplied so conditional policy only; portable fallback reads not registration.",
        "actualResponse": "A requested model identifies the request only. A spawn result with no actual-model field leaves actual model and effort unknown, even if the request was accepted. The actual native workers observed in this evaluation expose worker identities but not model identities; their default request is inherit-parent. This fixture does not supply a concrete named-model request/receipt, so I cannot claim a named selection happened. Preserve requestedModel separately from actualModel='unknown' and do not infer diversity. Original agents/poteto-agent.md and agents/comment-sicko.md reads failed; documented references/agent-prompts equivalents were read instead.",
        "variants": [
          {
            "name": "portable role original paths",
            "state": "attempted",
            "reason": "Missing path errors and documented alternate source copies retained"
          },
          {
            "name": "named-model request with unobserved actual",
            "state": "attempted",
            "reason": "Applied request/observation distinction without inventing a named request"
          },
          {
            "name": "actual model identity and diversity",
            "state": "blocked",
            "reason": "No actual-model/effort result field or observed family"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "actual model identity and diversity",
            "reason": "No actual-model/effort result field or observed family"
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
        "fullExpected": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately.",
        "reducedExpected": "Authorized sequential role review preserves scope and reports reduced capability. Keep observed model unknown and retain the request separately.",
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
        "text": "A requested model identifies the request only. A spawn result with no actual-model field leaves actual model and effort unknown, even if the request was accepted. The actual native workers observed in this evaluation expose worker identities but not model identities; their default request is inherit-parent. This fixture does not supply a concrete named-model request/receipt, so I cannot claim a named selection happened. Preserve requestedModel separately from actualModel='unknown' and do not infer diversity. Original agents/poteto-agent.md and agents/comment-sicko.md reads failed; documented references/agent-prompts equivalents were read instead.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/result.json",
          "sha256": "5230094b53fbc9670a5285514368c1f51be1f60355c4abc36c1db8bd263a085f",
          "bytes": 2191
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/case.json",
            "sha256": "f10c45605cc796a721207fbdf2db2c47d99ee0739b99457eff1fbf9b90f29391",
            "bytes": 397
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unknown-actual-model/evidence/source-read-status.tsv",
            "sha256": "304d170a37e6a7406e09e117ca8b822bfacabf79016397b43b98f3f2a51bceb7",
            "bytes": 51
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
