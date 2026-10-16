# chatgpt: unsupported-selected-model

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "unsupported-selected-model",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#28",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "The requested model is unavailable or rejects the selected effort.",
  "caseDefinition": {
    "id": "unsupported-selected-model",
    "sourcePaths": [
      "agents/poteto-agent.md",
      "agents/comment-sicko.md"
    ],
    "prompt": "The requested model is unavailable or rejects the selected effort.",
    "requirements": [
      "Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
      "Read portable role instructions; bind operations to observed session capabilities."
    ],
    "expectedFull": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
    "expectedReduced": "Authorized sequential role review preserves scope and reports reduced capability. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
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
    "caseId": "unsupported-selected-model",
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
      "attemptId": "grades-chatgpt-09-12.json#28",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 28,
      "host": "chatgpt",
      "caseId": "unsupported-selected-model",
      "status": "blocked",
      "grade": {
        "caseId": "unsupported-selected-model",
        "batch": "batch-12",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "No concrete rejected request/effort receipt or actual fallback; deliberate unsupported request correctly avoided. Conditional policy alone cannot exercise required rejection/fallback variants.",
        "actualResponse": "There is no concrete requested model/effort or rejected tool receipt in this case. I did not invent one or deliberately request an unsupported name. The current collaboration schema documents available overrides, but does not report actual worker models. A real rejection must retain exact request/error and supported effort source. If the exact selection is mandatory, its arm stays blocked; if inherited fallback is authorized, disclose the change before dispatch and keep the original rejection. Default portable request remains inherit-parent. No rejection or fallback actually occurred here. Missing agents/* sources and documented portable alternatives were read and preserved.",
        "variants": [
          {
            "name": "unsupported named model",
            "state": "blocked",
            "reason": "No concrete rejected request supplied; do not fabricate rejection"
          },
          {
            "name": "unsupported effort with known supported replacement",
            "state": "blocked",
            "reason": "No rejected effort/current selection supplied; no guessed compatibility"
          },
          {
            "name": "inherited fallback disclosure",
            "state": "attempted",
            "reason": "Policy described; no actual fallback or rewritten receipt claimed"
          },
          {
            "name": "mandatory exact selection",
            "state": "blocked",
            "reason": "Cannot satisfy unavailable exact choice; none supplied"
          },
          {
            "name": "portable role source reads",
            "state": "attempted",
            "reason": "Original paths missing, documented references/agent-prompts alternatives read"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "unsupported named model",
            "reason": "No concrete rejected request supplied; do not fabricate rejection"
          },
          {
            "variant": "unsupported effort with known supported replacement",
            "reason": "No rejected effort/current selection supplied; no guessed compatibility"
          },
          {
            "variant": "mandatory exact selection",
            "reason": "Cannot satisfy unavailable exact choice; none supplied"
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
        "fullExpected": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
        "reducedExpected": "Authorized sequential role review preserves scope and reports reduced capability. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
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
        "text": "There is no concrete requested model/effort or rejected tool receipt in this case. I did not invent one or deliberately request an unsupported name. The current collaboration schema documents available overrides, but does not report actual worker models. A real rejection must retain exact request/error and supported effort source. If the exact selection is mandatory, its arm stays blocked; if inherited fallback is authorized, disclose the change before dispatch and keep the original rejection. Default portable request remains inherit-parent. No rejection or fallback actually occurred here. Missing agents/* sources and documented portable alternatives were read and preserved.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/result.json",
          "sha256": "2434393dcbdbe3f627ed0cf60f532794104fdd19cbd387796afc502ef3935559",
          "bytes": 2565
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/case.json",
            "sha256": "9e29493d263a2a13c1cef9ffa74fbf3df58ee9721a5d9f99eaf5185dd305e77b",
            "bytes": 429
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/unsupported-selected-model/evidence/source-read-status.tsv",
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
