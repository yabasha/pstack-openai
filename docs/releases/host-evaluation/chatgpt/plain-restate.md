# chatgpt: plain-restate

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "plain-restate",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-chatgpt-plain-restate.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Invoke bro.",
  "caseDefinition": {
    "id": "plain-restate",
    "sourcePaths": [
      "skills/bro/SKILL.md"
    ],
    "prompt": "Invoke bro.",
    "requirements": [
      "Before invocation, seed this exact sentence as the immediately preceding ASSISTANT turn: We should serialize mutations to the shared state to prevent concurrent writers from clobbering each other.",
      "Preserve a conversation artifact identifying the seeded assistant turn and its exact text; do not substitute an assertion about prior text inside the user invocation.",
      "Access to the actual previous assistant message.",
      "User invocation of bro; preserve disable-model-invocation metadata."
    ],
    "expectedFull": "Restates the actual immediately preceding assistant message in plain, coherent, concise language without adding claims. For the seeded assistant turn, explains that changes should happen one at a time so writers do not overwrite each other.",
    "expectedReduced": "If only an excerpt of the previous message is available, restates that excerpt and names the context limit without claiming it is the complete message.",
    "expectedBlocked": "If the previous assistant message is unavailable, says it cannot restate the message and requests the missing text without inventing its contents.",
    "forbiddenClaims": [
      "New facts, advice, promises, or outcomes absent from the previous message.",
      "Claims that unavailable conversation history was read.",
      "Claims of host behavioral verification from structural validation."
    ],
    "caseFile": "docs/parity/cases/skills/bro.json"
  },
  "registry": {
    "caseId": "plain-restate",
    "caseFile": "docs/parity/cases/skills/bro.json",
    "sourcePaths": [
      "skills/bro/SKILL.md"
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
        "supplied-input",
        "response",
        "review-outcome"
      ],
      "reduced-pass": [
        "supplied-input",
        "response",
        "review-outcome"
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
      "attemptId": "grades-chatgpt-plain-restate.json#0",
      "order": 0,
      "gradeFile": "grades-chatgpt-plain-restate.json",
      "rankWithinFile": 0,
      "host": "chatgpt",
      "caseId": "plain-restate",
      "status": "pass",
      "grade": {
        "schemaVersion": 1,
        "caseId": "plain-restate",
        "host": "chatgpt",
        "status": "pass",
        "execution": "direct",
        "threadId": "6ad1d8e7-7900-83eb-873c-11c8a5d75fa4",
        "requiredObservationsMet": [
          "supplied-input",
          "response",
          "review-outcome"
        ],
        "missing": [],
        "evidence": "chatgpt/plain-restate.thread.json",
        "seed": {
          "turnId": "a92fc00b-282b-404b-bc62-83468fb871b4",
          "messageId": "8da4ee20-d473-5e52-9587-82f4144fa48f",
          "text": "We should serialize mutations to the shared state to prevent concurrent writers from clobbering each other."
        },
        "invocation": {
          "type": "userMessage",
          "id": "e903b329-0006-479c-beab-ee3db16edcf9",
          "content": [
            {
              "type": "text",
              "text": "Invoke bro."
            }
          ]
        },
        "response": {
          "type": "agentMessage",
          "id": "0500e6de-5a3b-5300-9d67-f7fc78d13658",
          "text": "We should make changes to the shared data one at a time so they don’t overwrite each other."
        },
        "review": "Actual thread export preserves exact required assistant seed followed by user Invoke bro and concise equivalent shared-data one-at-a-time restatement. No jargon, new claim or promise. Parent independently observed same ordering in UI. Full native-text contract met.",
        "limits": [
          "Thread export omits tool calls, so specific skill read/source path is not independently proven here. Native-text case does not require invented read operation."
        ],
        "nativeObservations": [
          {
            "observation": "supplied-input",
            "evidence": "chatgpt/plain-restate.thread.json",
            "reviewedBy": "grade_contract_audit"
          },
          {
            "observation": "response",
            "evidence": "chatgpt/plain-restate.thread.json",
            "reviewedBy": "grade_contract_audit"
          },
          {
            "observation": "review-outcome",
            "evidence": "grades-chatgpt-plain-restate.json",
            "reviewedBy": "grade_contract_audit"
          }
        ]
      },
      "topLevelContext": {
        "limits": [
          "Thread export omits tool calls, so specific skill read/source path is not independently proven here. Native-text case does not require invented read operation."
        ]
      },
      "response": {
        "text": "We should make changes to the shared data one at a time so they don’t overwrite each other.",
        "artifact": {
          "path": "chatgpt/plain-restate.thread.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/plain-restate.thread.json",
          "sha256": "6a1f2b82e0546619a0e34481cb698e9cbd321507adbc32cf52a92d6a7b1910b3",
          "bytes": 2223
        },
        "extraction": "Exact response field retained by independent grade"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/plain-restate.thread.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/plain-restate.thread.json",
            "sha256": "6a1f2b82e0546619a0e34481cb698e9cbd321507adbc32cf52a92d6a7b1910b3",
            "bytes": 2223
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [
          {
            "path": "chatgpt/plain-restate.thread.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/plain-restate.thread.json",
            "sha256": "6a1f2b82e0546619a0e34481cb698e9cbd321507adbc32cf52a92d6a7b1910b3",
            "bytes": 2223
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "supplied-input",
              "evidence": "chatgpt/plain-restate.thread.json",
              "reviewedBy": "grade_contract_audit"
            },
            {
              "observation": "response",
              "evidence": "chatgpt/plain-restate.thread.json",
              "reviewedBy": "grade_contract_audit"
            },
            {
              "observation": "review-outcome",
              "evidence": "grades-chatgpt-plain-restate.json",
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
