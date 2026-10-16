# chatgpt: alternatives

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "alternatives",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-chatgpt-00.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "A novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.",
  "caseDefinition": {
    "id": "alternatives",
    "sourcePaths": [
      "skills/principle-exhaust-the-design-space/SKILL.md"
    ],
    "prompt": "A novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.",
    "requirements": [
      "Identify a novel decision with multiple viable approaches",
      "Compare 2-3 distinct prototypes or sketches side by side",
      "Observe available write and execution tools and permissions before using them"
    ],
    "expectedFull": "Build 2-3 distinct prototypes or sketches, compare them side by side, and choose only after comparison. Report executed checks only when observed. Explain that minor variations of one approach do not count and that established patterns or a single viable approach do not require this exploration.",
    "expectedReduced": "Without execution, compare 2-3 distinct sketches or proposals and label them untested. State that runtime behavior and interaction feel remain unverified. Without writes, keep sketches in the response and disclose the limitation.",
    "expectedBlocked": "If required prototype construction or evaluation is denied or unavailable and sketches cannot answer the decision, report that step as blocked and identify the missing capability without claiming a completed comparison.",
    "forbiddenClaims": [
      "Execution or interaction testing occurred without observed results",
      "Minor variants count as distinct alternatives",
      "Prototype work authorizes publishing or external writes",
      "Static review establishes host parity"
    ],
    "caseFile": "docs/parity/cases/skills/principle-exhaust-the-design-space.json"
  },
  "registry": {
    "caseId": "alternatives",
    "caseFile": "docs/parity/cases/skills/principle-exhaust-the-design-space.json",
    "sourcePaths": [
      "skills/principle-exhaust-the-design-space/SKILL.md"
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
      "attemptId": "grades-chatgpt-00.json#0",
      "order": 0,
      "gradeFile": "grades-chatgpt-00.json",
      "rankWithinFile": 0,
      "host": "chatgpt",
      "caseId": "alternatives",
      "status": "pass",
      "grade": {
        "caseId": "alternatives",
        "host": "chatgpt",
        "status": "pass",
        "execution": "direct",
        "blockKind": null,
        "artifactOutcomeAssessment": "pass",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "requiredObservationsReportedButNotIndependentlyCorroborated": [
          "Exact file arguments, command stdout and exit statuses in exported model-authored log"
        ],
        "actualReadEventIds": [],
        "reportedReadLocators": [
          "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/4 (reported ec3413)",
          "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/5 (reported 7e9508)",
          "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/6 (reported fd04dd)",
          "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/7 (reported b871d0)"
        ],
        "review": "Archive contains three materially distinct side-by-side interaction sketches: per-row retry, bulk selection/review and search/command. Comparison includes costs and a provisional choice. Actual saved function/test source is inspectable. Reported Node three-test result exercises these local functions, not browser interaction; browser and usability limits are accurately retained. Expected full permits sketches, so absent browser execution alone is not an outcome failure. Runtime counts remain reported capture until independently corroborated.",
        "missing": [],
        "concreteFixCandidates": [],
        "exercisedVariants": [
          "three distinct HTML sketches created side by side",
          "single failed-job retry; running-job rejection; original state unchanged",
          "batch confirmation; cancellation preserves state; empty and duplicate selection rejection",
          "case-insensitive search; excludes running jobs; no matches",
          "Node syntax checks for implementation, tests, and extracted browser module"
        ],
        "unexercisedVariants": [
          "Actual browser rendering and module loading",
          "Real pointer/keyboard input, dialog focus, Escape, focus restoration, screen-reader behavior",
          "Hover, focus-visible, mobile layout, large lists, loading/error states",
          "Representative operator usability and interaction-feel comparison"
        ],
        "evidence": [
          "chatgpt/batch-00/batch-00-evaluation/batch-00.results.json",
          "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
          "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/sketches.html",
          "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/interaction.mjs",
          "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/interaction.test.mjs",
          "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/inspection.json",
          "chatgpt/batch-00/batch-00-evaluation/local-probes.json"
        ],
        "limits": [
          "Independent native UI corroborates read/skill-read/command activity. Exact arguments, raw outputs and claimed chunk IDs remain model-captured and not independently verified.",
          "Bun unavailable is reported; Node and Python were used despite user Bun preference. Preserve this deviation; do not claim Bun compliance.",
          "Installed package commit SHA is supplied, not independently verified by Git metadata.",
          "No external service/worker operation is credited from fixture data, metadata, proxy programs or artifact-check assertions."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
            "reviewedBy": "grade_contract_audit archive review"
          },
          {
            "observation": "review-outcome",
            "evidence": "grades-chatgpt-00.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Build 2-3 distinct prototypes or sketches, compare them side by side, and choose only after comparison. Report executed checks only when observed. Explain that minor variations of one approach do not count and that established patterns or a single viable approach do not require this exploration.",
        "reducedExpected": "Without execution, compare 2-3 distinct sketches or proposals and label them untested. State that runtime behavior and interaction feel remain unverified. Without writes, keep sketches in the response and disclose the limitation.",
        "nativeReadEvidence": "Independent parent-observed native UI labels corroborate real reads. Exact source attribution comes from captured archive and remains partly corroborated, not raw-event verified."
      },
      "topLevelContext": {
        "scope": "Exported ChatGPT Work batch00 artifact review with independently observed native UI activity",
        "gradingNotes": [
          "Parent independently observed native UI activity confirming actual file/skill reads and four commands; this permits read credit with explicit provenance limits.",
          "Exact source arguments, chunk IDs, command outputs and exit statuses in tool-log remain model-captured. Do not treat those strings as independent native trace IDs.",
          "Saved model responses and source artifacts support qualitative assessment. One full sketch outcome does not establish Bun compliance, browser execution or unrelated variants.",
          "Node/Python deviation remains a user-preference violation and limitation, not Bun execution or an automatic workflow failure.",
          "Reported local interaction/recovery test outputs do not establish target-app UI or tracker service behavior.",
          "Original skill resource read failure is preserved; filesystem fallback is separately reported."
        ]
      },
      "response": {
        "text": "{\n  \"id\": \"alternatives\",\n  \"response\": \"I chose the novel interaction of selecting failed jobs to retry. Three side-by-side working sketches are retained: A places a Retry button on each job row; B uses batch selection followed by a review dialog; C searches failed job IDs and exposes a targeted retry command. A is the provisional default for occasional retries because the target is visible beside the action. B suits frequent multi-job retries and adds an explicit review step. C suits operators who already know an ID, but needs discoverability and keyboard testing. These are distinct interaction structures, not styling variations. No production implementation choice is committed. Node executed the real local interaction-state functions; browser rendering and interaction feel remain untested.\",\n  \"outcome\": \"Local sketches and core-function probes completed; browser evaluation unperformed\",\n  \"comparison\": [\n    {\n      \"approach\": \"Inline action\",\n      \"strength\": \"Visible target and direct action\",\n      \"cost\": \"Repeated actions for many jobs\"\n    },\n    {\n      \"approach\": \"Selection and review\",\n      \"strength\": \"Batch scope visible before apply\",\n      \"cost\": \"Selection and dialog steps\"\n    },\n    {\n      \"approach\": \"Search and command\",\n      \"strength\": \"Targets known IDs without scanning\",\n      \"cost\": \"Search discovery and keyboard behavior unverified\"\n    }\n  ],\n  \"exercisedVariants\": [\n    \"three distinct HTML sketches created side by side\",\n    \"single failed-job retry; running-job rejection; original state unchanged\",\n    \"batch confirmation; cancellation preserves state; empty and duplicate selection rejection\",\n    \"case-insensitive search; excludes running jobs; no matches\",\n    \"Node syntax checks for implementation, tests, and extracted browser module\"\n  ],\n  \"unexercisedVariants\": [\n    \"Actual browser rendering and module loading\",\n    \"Real pointer/keyboard input, dialog focus, Escape, focus restoration, screen-reader behavior\",\n    \"Hover, focus-visible, mobile layout, large lists, loading/error states\",\n    \"Representative operator usability and interaction-feel comparison\"\n  ],\n  \"evidence\": [\n    \"cases/alternatives/sketches.html\",\n    \"cases/alternatives/interaction.mjs\",\n    \"cases/alternatives/interaction.test.mjs\",\n    \"cases/alternatives/inspection.json\",\n    \"local-probes.json\"\n  ]\n}\n",
        "artifact": {
          "path": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
          "sha256": "c4b5e1354d05a82ef23a0a3b327e73b968d2da076c4320bc49050fd0f479aa8c",
          "bytes": 2363
        },
        "extraction": "Complete retained response JSON"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/tool-log.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/tool-log.json",
            "sha256": "2db2dd5d3b0b1dab90d100335bf52686261dc850764cd4da279c32134ab93038",
            "bytes": 285204
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/batch-00.results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/batch-00.results.json",
            "sha256": "d301d3ac626147fdcbdd2ad770f42e221c1093e3f7d4cccb734aa6abd4cee76b",
            "bytes": 26252
          },
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
            "sha256": "c4b5e1354d05a82ef23a0a3b327e73b968d2da076c4320bc49050fd0f479aa8c",
            "bytes": 2363
          },
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/sketches.html",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/cases/alternatives/sketches.html",
            "sha256": "8245427b2b34a468da08e80cf7ca7e6997460a5cd15dd278c45758365faaf4f2",
            "bytes": 3556
          },
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/interaction.mjs",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/cases/alternatives/interaction.mjs",
            "sha256": "ee23852d00577bf5c5f386a70613003423939513b55763e2f7a39f3fe3605ffd",
            "bytes": 707
          },
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/interaction.test.mjs",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/cases/alternatives/interaction.test.mjs",
            "sha256": "795608276d2b6d3fd32a8e5b0a8d0ce0dcf4304d0b25c0c2da60a3dbd0660825",
            "bytes": 1110
          },
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/inspection.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/cases/alternatives/inspection.json",
            "sha256": "7781ec65c89f5db92e2440b2e29ce0b5198cd7949940a0d8113652590bbafddf",
            "bytes": 144
          },
          {
            "path": "chatgpt/batch-00/batch-00-evaluation/local-probes.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/batch-00/batch-00-evaluation/local-probes.json",
            "sha256": "5613176180361d09330343f548fd7759eec99306027d4650f65fca73aef5d9e7",
            "bytes": 8329
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [
            "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/4 (reported ec3413)",
            "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/5 (reported 7e9508)",
            "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/6 (reported fd04dd)",
            "chatgpt/batch-00/batch-00-evaluation/tool-log.json#/operations/7 (reported b871d0)"
          ],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/batch-00/batch-00-evaluation/cases/alternatives/response.json",
              "reviewedBy": "grade_contract_audit archive review"
            },
            {
              "observation": "review-outcome",
              "evidence": "grades-chatgpt-00.json",
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
