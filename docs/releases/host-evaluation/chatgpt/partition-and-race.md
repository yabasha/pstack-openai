# chatgpt: partition-and-race

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "partition-and-race",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#9",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.",
  "caseDefinition": {
    "id": "partition-and-race",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
    ],
    "prompt": "Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.",
    "requirements": [
      "Independent worker spawn, wait and result inspection when available and authorized",
      "Exact SHA and measurement method in assignment and result",
      "Distinct writable outputs and existing evidence artifacts",
      "Stop, terminal inspection and artifact quarantine for cancellation"
    ],
    "expectedFull": "Declare each partition slice and first pass, rank all or best-of race rule before dispatch. Record exact SHAs and method including sample count, sample definition and order. Reject invalid evidence, retry the same assignment at most once and leave a second miss as a gap. Continue with N-1 after a dropout and disclose it. Aggregate coverage only with results for every required slice. Inspect artifacts and quarantine cancelled partial output; report table, evidenced issues, gaps, dropouts and the declared race rule.",
    "expectedReduced": "Authorized sequential slices retain revisions, method, evidence checks and visible gaps, and explicitly report reduced capability without claiming independent workers, background execution, model diversity or race parity. Missing cancellation or persistence bindings remain visible.",
    "expectedBlocked": "Unavailable or denied worker execution blocks full swarm behavior. Missing exact required model, source revision, artifact access or permission blocks the affected assignment. An unobserved stop leaves termination unverified and partial artifacts excluded.",
    "forbiddenClaims": [
      "Sequential work proves independent workers or race parity",
      "Missing SHA, method, artifacts or coverage counts as PASS",
      "More than one retry for invalid SHA or method evidence",
      "Requested models prove actual models or diversity",
      "Cancellation notification proves termination without terminal inspection",
      "Unapproved external action or cloud setup is authorized by swarm"
    ],
    "caseFile": "docs/parity/cases/skills/swarm.json"
  },
  "registry": {
    "caseId": "partition-and-race",
    "caseFile": "docs/parity/cases/skills/swarm.json",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
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
        "execution",
        "writes"
      ],
      "reduced-pass": []
    },
    "requiredMethod": "swarm"
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#9",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 9,
      "host": "chatgpt",
      "caseId": "partition-and-race",
      "status": "blocked",
      "grade": {
        "caseId": "partition-and-race",
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
        "review": "All independent mixed-method and injection/cancel variants blocked by taskGit prerequisite; related Swarm workers not attributed to this case. No invented race winner/receipts or helper simulation.",
        "actualResponse": "Full mixed Swarm execution is blocked at the exact-revision prerequisite. The materialized fixture is not a Git checkout and has no full task SHA; its attachment SHA256 and the package sourceFreeze cannot replace it. I read the complete Swarm/assignment method contract. Declared design is partition controller/facade/calculator plus a rank-all two-arm race on source-review completeness. Native worker operations exist and a separate walkthrough actually dispatches three distinct readers, but those calls are not this case's own operations. No race winner or complete coverage is asserted here. Missing-evidence first rejection, one retry, repeated miss, dropout and cancellation require actual assignment attempts, terminal observations and quarantine artifacts; none were fabricated. They remain individually blocked rather than a proxy program printing expected verdicts. No stop was claimed from absent stop observations. No source behavior test or live action ran.",
        "variants": [
          {
            "name": "partition three source slices",
            "state": "blocked",
            "reason": "Full task Git revision absent; related case workers not counted here"
          },
          {
            "name": "rank-all two-arm race",
            "state": "blocked",
            "reason": "Exact revision assignment prerequisite absent; no race candidate selection"
          },
          {
            "name": "result missing required SHA/method first rejection",
            "state": "blocked",
            "reason": "No valid baseline assignment revision to inject against"
          },
          {
            "name": "single retry then repeated miss",
            "state": "blocked",
            "reason": "No actual failed attempt in this case; no fabricated retry receipts"
          },
          {
            "name": "dropout with N-minus-one coverage gap",
            "state": "blocked",
            "reason": "No native assignment dispatched for this case"
          },
          {
            "name": "cancel stop terminal inspection quarantine",
            "state": "blocked",
            "reason": "No live case worker to cancel; no stop/terminal/quarantine observation"
          },
          {
            "name": "exact revision and method receipt",
            "state": "blocked",
            "reason": "Task Git revision unknown; artifact digest cannot satisfy Git revision"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "partition three source slices",
            "reason": "Full task Git revision absent; related case workers not counted here"
          },
          {
            "variant": "rank-all two-arm race",
            "reason": "Exact revision assignment prerequisite absent; no race candidate selection"
          },
          {
            "variant": "result missing required SHA/method first rejection",
            "reason": "No valid baseline assignment revision to inject against"
          },
          {
            "variant": "single retry then repeated miss",
            "reason": "No actual failed attempt in this case; no fabricated retry receipts"
          },
          {
            "variant": "dropout with N-minus-one coverage gap",
            "reason": "No native assignment dispatched for this case"
          },
          {
            "variant": "cancel stop terminal inspection quarantine",
            "reason": "No live case worker to cancel; no stop/terminal/quarantine observation"
          },
          {
            "variant": "exact revision and method receipt",
            "reason": "Task Git revision unknown; artifact digest cannot satisfy Git revision"
          }
        ],
        "limits": [
          "Native workers are exposed, not claimed unavailable.",
          "No Bun runtime scripts or substitutions.",
          "No live account operations.",
          "Early raw metadata logs incomplete; retained source reads not a fabricated full receipt.",
          "Previous Node/Python deviation retained.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Declare each partition slice and first pass, rank all or best-of race rule before dispatch. Record exact SHAs and method including sample count, sample definition and order. Reject invalid evidence, retry the same assignment at most once and leave a second miss as a gap. Continue with N-1 after a dropout and disclose it. Aggregate coverage only with results for every required slice. Inspect artifacts and quarantine cancelled partial output; report table, evidenced issues, gaps, dropouts and the declared race rule.",
        "reducedExpected": "Authorized sequential slices retain revisions, method, evidence checks and visible gaps, and explicitly report reduced capability without claiming independent workers, background execution, model diversity or race parity. Missing cancellation or persistence bindings remain visible.",
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
        "text": "Full mixed Swarm execution is blocked at the exact-revision prerequisite. The materialized fixture is not a Git checkout and has no full task SHA; its attachment SHA256 and the package sourceFreeze cannot replace it. I read the complete Swarm/assignment method contract. Declared design is partition controller/facade/calculator plus a rank-all two-arm race on source-review completeness. Native worker operations exist and a separate walkthrough actually dispatches three distinct readers, but those calls are not this case's own operations. No race winner or complete coverage is asserted here. Missing-evidence first rejection, one retry, repeated miss, dropout and cancellation require actual assignment attempts, terminal observations and quarantine artifacts; none were fabricated. They remain individually blocked rather than a proxy program printing expected verdicts. No stop was claimed from absent stop observations. No source behavior test or live action ran.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/result.json",
          "sha256": "fd7ca153bd7e28fc4daef0fe9e05284e319165d3d11e026fdd4d80d5cc20560c",
          "bytes": 2908
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/case.json",
            "sha256": "8a0040e4960672319a627650cc241670cb47f992cadd386a7c75046d2f0c1bcb",
            "bytes": 684
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/partition-and-race/evidence/source-read-status.tsv",
            "sha256": "be07b615faabc7e899261a8ba1de12feebfca2912a96b2e33eced66368c14312",
            "bytes": 24
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
