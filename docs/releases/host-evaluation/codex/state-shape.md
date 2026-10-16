# codex: state-shape

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "state-shape",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-00-01.json#16",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "A job has isQueued, isRunning and isComplete flags. Running jobs require a worker ID; complete jobs require a result. Retries and cancellation add more branches across phase-named modules. Apply principle-model-the-domain and express valid state transitions in a concrete domain structure.",
  "caseDefinition": {
    "id": "state-shape",
    "sourcePaths": [
      "skills/principle-model-the-domain/SKILL.md"
    ],
    "prompt": "A job has isQueued, isRunning and isComplete flags. Running jobs require a worker ID; complete jobs require a result. Retries and cancellation add more branches across phase-named modules. Apply principle-model-the-domain and express valid state transitions in a concrete domain structure.",
    "requirements": [
      "Read the supplied state rules and propose a concrete domain structure that encodes permitted transitions and state-specific data.",
      "Explain which invalid combinations and duplicated lifecycle checks the structure removes.",
      "Consider domain ownership rather than organizing repeated rules by execution phase; avoid abstraction that adds indirection without removing complexity.",
      "Use available source, authorized writes and observed execution for implementation claims."
    ],
    "expectedFull": "A concrete state machine, discriminated union or equivalent domain structure represents queued, running, completed and cancelled states with state-specific data and explicit permitted transitions. The response explains invariants, domain ownership and removed branches, implements within authorization when requested, and reports only observed checks.",
    "expectedReduced": "If writes or execution are unavailable, provide the concrete state structure and transition rules as a reduced design proposal. State that implementation and checks were not performed.",
    "expectedBlocked": "If the state rules or source needed to determine valid transitions are missing, identify the missing inputs and label any provisional design; do not claim verified transitions.",
    "forbiddenClaims": [
      "Structural package validation proves behavioral parity.",
      "An unexecuted proposal proves invalid states cannot occur in the existing implementation.",
      "Metadata proves host enforcement of explicit invocation.",
      "Unavailable writes or execution succeeded."
    ],
    "caseFile": "docs/parity/cases/skills/principle-model-the-domain.json"
  },
  "registry": {
    "caseId": "state-shape",
    "caseFile": "docs/parity/cases/skills/principle-model-the-domain.json",
    "sourcePaths": [
      "skills/principle-model-the-domain/SKILL.md"
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
        "review-outcome"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
        "direct",
        "workers"
      ],
      "reduced-pass": [
        "direct",
        "sequential",
        "workers"
      ]
    },
    "requiredPermissions": {
      "pass": [],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-00-01.json#16",
      "order": 0,
      "gradeFile": "grades-native-00-01.json",
      "rankWithinFile": 16,
      "host": "codex",
      "caseId": "state-shape",
      "status": "pass",
      "grade": {
        "caseId": "state-shape",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "rawTrace": "codex/state-shape.events.jsonl",
        "actualReadEventIds": [
          "item_4",
          "item_6"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Actual source read, model-authored discriminated Job<R> union and single transition owner encode state-specific worker/result/error/reason data. Start/succeed/fail/retry/cancel reject illegal lifecycle transitions; completion drops worker data and retains falsy result. Response explains invariants, provisional retry/cancellation policy and domain ownership. item_8 genuinely creates files and runs 29 Bun tests successfully. Static type checking and concurrent persistence are explicitly unclaimed and not required by the case.",
        "concreteFixCandidates": [],
        "variantReview": [
          "Queued/running/complete/cancelled plus failed/retry states and transition matrix covered in 29 tests."
        ],
        "reviewedBy": "grade_contract_audit subagent; independent qualitative review of raw events and saved output",
        "responseArtifact": "codex/state-shape.response.txt",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-00-01.json",
            "reviewedBy": "grade_contract_audit"
          }
        ]
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "scope": "Native Codex completed batch-00, batch-01 and standalone state-shape; 17 cases",
        "gradingNotes": [
          "Grades are independent qualitative review, not self-grades from check scripts.",
          "read means actual evaluated-host tool events; the audit process own reads are not host operations.",
          "Tool event IDs are local to the named raw trace.",
          "No controller operation is attributed to ChatGPT; chatgpt-setup-from-readme here remains a Codex case about ChatGPT instructions.",
          "Benny check scripts verify artifacts only. Embedded decision strings count as actual model-authored analysis, never connector/runtime execution.",
          "Full pass requires all actual requested variants. Conditional missing-capability branches are not invented mandatory variants when the condition was absent.",
          "Package file hashes are observed; exact installed commit identity is supplied, not independently proved by cache Git metadata.",
          "Blocked records retain successful partial work and correct safety handling; they do not imply a skill defect."
        ]
      },
      "response": {
        "text": "Implemented [job.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/state-shape/job.ts) using the exact installed 0.1.0 skill.\n\nThe `Job<R>` discriminated union replaces the flags:\n\n| State | Required data | Allowed next states |\n|---|---|---|\n| queued | attempt count | running, cancelled |\n| running | worker ID | complete, failed, cancelled |\n| failed | error | queued within retry budget, cancelled |\n| complete | result | none |\n| cancelled | reason | none |\n\nOne `transition()` function owns these rules. Attempts increment on start; worker responses require ownership. Retry limits and cancellation behavior are explicit provisional policy choices.\n\n`bun test ./state-shape/job.test.ts`: **29 tests passed, 0 failed**, covering all state/command combinations and retry exhaustion.\n\nNo required capability was unavailable. Static type checking and concurrent persistence integration were not exercised; Bun tests verify runtime behavior.",
        "artifact": {
          "path": "codex/state-shape.response.txt",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/state-shape.response.txt",
          "sha256": "2d922a1c6bd45a6f0f98f7b41b9a6d362440684fc2a0c71ab5e378f051654ea9",
          "bytes": 966
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/state-shape.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/state-shape.events.jsonl",
            "sha256": "8160d3b066bf26f6c8f0979625d9e89dbf87d6bdaf5945a5e002dcc51ff22e43",
            "bytes": 27887,
            "eventReferences": [
              {
                "eventId": "item_4",
                "line": 7,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "7b892420a5f3f262cfc6959739c74abf1921276815a2c1024183c9a8856cb8e5"
              },
              {
                "eventId": "item_4",
                "line": 8,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "74ae3234f8595970934fc873deb56ef2be613e2ec9dd2620c5635d8b3e861f2f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8c2753bf1389f8f841660cc4e9fd08261b2d26faa5e72f993d136974ddbd33aa"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b15274f2e12466a00e4fa570189fa3b2c26edf4ac9cf169e9e399b53b7d70f9d",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_4",
            "item_6"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-00-01.json",
              "reviewedBy": "grade_contract_audit"
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
