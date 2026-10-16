# chatgpt: real-app-contract

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "real-app-contract",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#12",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Create a verification skill for this repo. Inspect its real app controls and existing harness, seed a feature map, and prove one feature if authorized tools are available. Retain the Notes example contracts as examples only.",
  "caseDefinition": {
    "id": "real-app-contract",
    "sourcePaths": [
      "skills/create-verification-skill/SKILL.md",
      "skills/create-verification-skill/references/feature-map-example/README.md",
      "skills/create-verification-skill/references/feature-map-example/create-note.md",
      "skills/create-verification-skill/references/feature-map-example/search.md"
    ],
    "prompt": "Create a verification skill for this repo. Inspect its real app controls and existing harness, seed a feature map, and prove one feature if authorized tools are available. Retain the Notes example contracts as examples only.",
    "requirements": [
      "Repository reads and authorized project-local writes",
      "Observed execution and app-driving tools for end-to-end proof",
      "Preserve all three feature-map examples and their exact commands",
      "Discover the active host project-local skill location and verify registration",
      "Follow the active workflow owner and permission boundaries"
    ],
    "expectedFull": "Inspect real routes, controls, commands and startup before authoring. Generate registered YAML metadata and Launch, Doctor, Drive, Evidence, Cleanup and Helpers sections using actual controls; seed the top 3-5 identifiable features with the prescribed four headings and all user entry points. Launch, doctor, drive one mapped feature, capture action, resulting state and side effects, clean up each attempt, then confirm evidence survives. Report observed proof only and point to /maintain-verification-skill without scheduling.",
    "expectedReduced": "When repository controls can be inspected and writes are authorized but execution or app-driving is unavailable, author a draft grounded in those controls. Mark verification not-run, name missing capabilities and unproved entry points; do not present the draft as a verified deliverable. If project-local registration is unconfirmed, report a portable draft with registration unverified.",
    "expectedBlocked": "If repository access or required authoring permission is unavailable, report the exact blocker and do not invent app controls or write files. If startup is broken, fix within authorization or report the precise failure before generation. Denied execution blocks proof and cannot count as a pass.",
    "forbiddenClaims": [
      "Notes example commands are real controls in an unrelated app",
      "An unexecuted generated skill is a verified deliverable",
      "A final screenshot alone proves the user action or side effects",
      "Skipped entry points are verified through another path",
      "A documented tool or project-local path proves discovery or successful execution",
      "Cleanup may delete evidence or kill processes by name",
      "Suggested cadence authorizes recurring scheduling"
    ],
    "caseFile": "docs/parity/cases/skills/create-verification-skill.json"
  },
  "registry": {
    "caseId": "real-app-contract",
    "caseFile": "docs/parity/cases/skills/create-verification-skill.json",
    "sourcePaths": [
      "skills/create-verification-skill/SKILL.md",
      "skills/create-verification-skill/references/feature-map-example/README.md",
      "skills/create-verification-skill/references/feature-map-example/create-note.md",
      "skills/create-verification-skill/references/feature-map-example/search.md"
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
        "review-outcome",
        "execution",
        "isolated-write"
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
      "pass": [
        "execution",
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#12",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 12,
      "host": "chatgpt",
      "caseId": "real-app-contract",
      "status": "blocked",
      "grade": {
        "caseId": "real-app-contract",
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
        "review": "No runnable UI target/harness/verification skill; Notes examples are documentation only. Source inventory useful but cannot author meaningful executable app verification or produce feature cleanup proof.",
        "actualResponse": "The real supplied fixture contains JavaScript library modules and inert JSON, without a runnable UI package, actual app launch command, control harness or existing project-local verification skill. I read all three Notes feature-map examples and retained their exact commands in source copies; they are examples only and were never executed against this fixture. A meaningful portable verification draft can document library entry points visible/exportCsv and the CSV correctness targets, but cannot invent Launch/Doctor/selector commands or claim project registration. I therefore retain a source-grounded inventory and explicit missing run/drive contract, rather than a falsely executable skill. One end-to-end feature proof, post-cleanup artifact persistence and host project-local registration remain unverified. No listener or dependency setup occurred.",
        "variants": [
          {
            "name": "repo/app/harness interview",
            "state": "attempted",
            "reason": "Fixture file discovery and actual dashboard source reads"
          },
          {
            "name": "three Notes examples exact commands",
            "state": "attempted",
            "reason": "Complete source copies retained; examples not app instructions"
          },
          {
            "name": "project-local skill path and registration",
            "state": "blocked",
            "reason": "No actual host project convention/registration evidence"
          },
          {
            "name": "seed map and authored verified skill",
            "state": "blocked",
            "reason": "No runnable app/observed controls; cannot invent commands"
          },
          {
            "name": "one actual feature proof/cleanup",
            "state": "blocked",
            "reason": "Bun absent, launch/harness/control target absent"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "project-local skill path and registration",
            "reason": "No actual host project convention/registration evidence"
          },
          {
            "variant": "seed map and authored verified skill",
            "reason": "No runnable app/observed controls; cannot invent commands"
          },
          {
            "variant": "one actual feature proof/cleanup",
            "reason": "Bun absent, launch/harness/control target absent"
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
        "fullExpected": "Inspect real routes, controls, commands and startup before authoring. Generate registered YAML metadata and Launch, Doctor, Drive, Evidence, Cleanup and Helpers sections using actual controls; seed the top 3-5 identifiable features with the prescribed four headings and all user entry points. Launch, doctor, drive one mapped feature, capture action, resulting state and side effects, clean up each attempt, then confirm evidence survives. Report observed proof only and point to /maintain-verification-skill without scheduling.",
        "reducedExpected": "When repository controls can be inspected and writes are authorized but execution or app-driving is unavailable, author a draft grounded in those controls. Mark verification not-run, name missing capabilities and unproved entry points; do not present the draft as a verified deliverable. If project-local registration is unconfirmed, report a portable draft with registration unverified.",
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
        "text": "The real supplied fixture contains JavaScript library modules and inert JSON, without a runnable UI package, actual app launch command, control harness or existing project-local verification skill. I read all three Notes feature-map examples and retained their exact commands in source copies; they are examples only and were never executed against this fixture. A meaningful portable verification draft can document library entry points visible/exportCsv and the CSV correctness targets, but cannot invent Launch/Doctor/selector commands or claim project registration. I therefore retain a source-grounded inventory and explicit missing run/drive contract, rather than a falsely executable skill. One end-to-end feature proof, post-cleanup artifact persistence and host project-local registration remain unverified. No listener or dependency setup occurred.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/result.json",
          "sha256": "66c281fb448b8cb3fd8f21be70c7590d61d14a7462b73016661da454bdfdc654",
          "bytes": 2481
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/case.json",
            "sha256": "666ec2f57111404dc627951d008e6e69b9ac17d55b634c76a6d6d1ec7826087e",
            "bytes": 968
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/real-app-contract/evidence/source-read-status.tsv",
            "sha256": "0829bf3f0ffa58a17d083715a23dbe711e144cbd53597652d59091aff67913d9",
            "bytes": 277
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
