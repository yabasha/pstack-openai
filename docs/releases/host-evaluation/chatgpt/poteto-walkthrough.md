# chatgpt: poteto-walkthrough

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "poteto-walkthrough",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#10",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Start with a read-only architecture question and an explicit active controller. Follow README to Poteto mode and select Investigation.",
  "caseDefinition": {
    "id": "poteto-walkthrough",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md"
    ],
    "prompt": "Start with a read-only architecture question and an explicit active controller. Follow README to Poteto mode and select Investigation.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/workflows/poteto-mode.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.",
      "Resolve controller ownership before work. Read the full mode, Investigation playbook, routed how contracts and every applied principle leaf. Copy exact steps or explicit skips; preserve the read-only checkpoint and Investigation no-PR exception."
    ],
    "expectedFull": "The active owner produces a cited read-only architecture explanation using inspected read-only worker results, with the Investigation checkpoint and actual capability limits. Principles named in the answer were read in full. No implementation, PR or babysit starts.",
    "expectedReduced": "A reduced foreground run can preserve routing, the checkpoint and an inspected local artifact. Missing independent workers, controls or persistence stays explicit; no unattended completion is claimed.",
    "expectedBlocked": "Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.",
    "forbiddenClaims": [
      "Links or direct source reads prove installed discovery.",
      "Sequential roles are independent workers.",
      "An isolated helper snapshot proves this candidate or host passed.",
      "A resolution file, owner marker or upstream autonomy grants approval.",
      "Apply automatically accepts an update or refreshes a host."
    ],
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json"
  },
  "registry": {
    "caseId": "poteto-walkthrough",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md"
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
      "attemptId": "grades-chatgpt-09-12.json#10",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 10,
      "host": "chatgpt",
      "caseId": "poteto-walkthrough",
      "status": "reduced-pass",
      "grade": {
        "caseId": "poteto-walkthrough",
        "batch": "batch-10",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Source navigation/Investigation checkpoint and ownership handling useful. Related trace-path explanation explicitly not own method; exact registered discovery/controller-conflict inputs unobserved.",
        "actualResponse": "Explicit pstack invocation owns this evaluation. The case names an active controller but does not supply its identity; I do not silently replace a different controller. README links docs/workflows/poteto-mode.md and that full destination, mode, Investigation, how and required prompt/capability contracts were read. For this read-only question, Investigation is the selected route. Throughput checkpoint: n/a, read-only investigation. Relevant fixture architecture has controller wrapping facade return, facade forwarding invoice to adapter, adapter extracting rows, and calculator replacing shared cachedTotal; the separate trace-path independent explainer artifact grounds that description but does not substitute for this case's own registered discovery proof. Local navigation/source reads succeeded. SourceFreeze f4623636a287bea2aa79c4b2234a53d20a5f193c remains supplied metadata, actual installed Git HEAD unknown. No settings, install, code, PR or babysit action. The source-specific controller-conflict branch is held until an explicit competing controller identity is supplied.",
        "variants": [
          {
            "name": "README to full workflow/mode/Investigation/how contracts",
            "state": "attempted",
            "reason": "Actual local read receipts retained"
          },
          {
            "name": "active controller ownership",
            "state": "attempted",
            "reason": "Explicit pstack request owns current evaluation; unspecified competing controller remains unknown"
          },
          {
            "name": "exact steps and read-only checkpoint",
            "state": "attempted",
            "reason": "Full Investigation text retained; no PR exception applied"
          },
          {
            "name": "independent explanation",
            "state": "blocked",
            "reason": "No separate independent task assignment for this case; related trace-path report not counted as own operation"
          },
          {
            "name": "installed UI discovery and exact Git revision",
            "state": "blocked",
            "reason": "No host menu-registration observation or installed Git HEAD"
          },
          {
            "name": "dual-controller conflict",
            "state": "blocked",
            "reason": "No concrete competing active controller supplied"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "independent explanation",
            "reason": "No separate independent task assignment for this case; related trace-path report not counted as own operation"
          },
          {
            "variant": "installed UI discovery and exact Git revision",
            "reason": "No host menu-registration observation or installed Git HEAD"
          },
          {
            "variant": "dual-controller conflict",
            "reason": "No concrete competing active controller supplied"
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
        "fullExpected": "The active owner produces a cited read-only architecture explanation using inspected read-only worker results, with the Investigation checkpoint and actual capability limits. Principles named in the answer were read in full. No implementation, PR or babysit starts.",
        "reducedExpected": "A reduced foreground run can preserve routing, the checkpoint and an inspected local artifact. Missing independent workers, controls or persistence stays explicit; no unattended completion is claimed.",
        "concreteFixCandidates": [],
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
        "text": "Explicit pstack invocation owns this evaluation. The case names an active controller but does not supply its identity; I do not silently replace a different controller. README links docs/workflows/poteto-mode.md and that full destination, mode, Investigation, how and required prompt/capability contracts were read. For this read-only question, Investigation is the selected route. Throughput checkpoint: n/a, read-only investigation. Relevant fixture architecture has controller wrapping facade return, facade forwarding invoice to adapter, adapter extracting rows, and calculator replacing shared cachedTotal; the separate trace-path independent explainer artifact grounds that description but does not substitute for this case's own registered discovery proof. Local navigation/source reads succeeded. SourceFreeze f4623636a287bea2aa79c4b2234a53d20a5f193c remains supplied metadata, actual installed Git HEAD unknown. No settings, install, code, PR or babysit action. The source-specific controller-conflict branch is held until an explicit competing controller identity is supplied.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/result.json",
          "sha256": "34ab42af544b79609f2f5ac68051f26935a7356d38517bf537e54714edf0d141",
          "bytes": 2956
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/case.json",
            "sha256": "a299dbfc6ee730f264a7218a548c56fbc22d2a6ccc0e0ec3f0938c38acfa2889",
            "bytes": 1030
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/poteto-walkthrough/evidence/source-read-status.tsv",
            "sha256": "66c862003c8e637328ab402bd0d45180498802c44fa12a06a82826c21ac0c1fa",
            "bytes": 30
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
    "Input Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
