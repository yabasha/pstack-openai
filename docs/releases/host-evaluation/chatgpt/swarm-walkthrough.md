# chatgpt: swarm-walkthrough

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "swarm-walkthrough",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#20",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Swarm and partition a three-file source review.",
  "caseDefinition": {
    "id": "swarm-walkthrough",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
    ],
    "prompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Swarm and partition a three-file source review.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/workflows/swarm.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.",
      "Declare partition/race/mixed shape, N and first pass/rank all/best-of when relevant before dispatch. Include full SHA and method; reject incomplete results, allow at most one inspected retry and retain uncovered slices as gaps."
    ],
    "expectedFull": "Three independent authorized slice results cover the three fixture files at the exact SHA and method. The coordinator inspects terminal artifacts and returns one consolidated table with evidenced issues and explicit gaps/dropouts. Cancellation requires observed stop, terminal inspection and quarantine.",
    "expectedReduced": "Sequential review of the declared three-file partition may return reduced findings with exact revisions, inspected artifacts and visible missing slices. It proves neither independent workers nor a race.",
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
    "caseId": "swarm-walkthrough",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
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
    "requiredMethod": "swarm-partition",
    "requiredSliceCount": 3
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#20",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 20,
      "host": "chatgpt",
      "caseId": "swarm-walkthrough",
      "status": "reduced-pass",
      "grade": {
        "caseId": "swarm-walkthrough",
        "batch": "batch-11",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Actual three independent source-reader identities and inspected slice reports support partition observations. No race requirement invented for partition-only. Sequential slot waves/taskGit absence/full receipt prevent full method.",
        "actualResponse": "Followed README to the actual full Swarm walkthrough and required capability/role/assignment contracts. Declared partition N3 over controller, facade and calculator before dispatch. Three fresh native identities read disjoint exact fixture files in sequential waves constrained by shared slots. Parent inspected all reports, source-copy identity and report digests. Controller wraps facade output, facade forwards to adapter, and calculator owns shared latest-result state. No defect is proven from controller/facade slices alone. Calculator cache scope is a static ownership observation, not a runtime test. All three source slices have retained independent observations; full revision-bound method acceptance is blocked because task Git SHA is missing. Attachment digest and supplied package freeze do not replace it. No race, failure injection or cancellation belongs to this partition-only walkthrough. Requested models inherited; actual identities unknown. Source reading does not prove installed menu discovery. A first guessed controller artifact filename failed, actual discovery found controller.mjs and byte comparison then returned exit0.",
        "variants": [
          {
            "name": "README navigation/full workflow and source contracts",
            "state": "attempted",
            "reason": "Actual local destinations and text read"
          },
          {
            "name": "three-file partition N3 independent identities",
            "state": "attempted",
            "reason": "Observed three native workers; three inspected source/result artifacts"
          },
          {
            "name": "simultaneous parallel dispatch",
            "state": "blocked",
            "reason": "Shared native capacity required sequential waves; independence does not prove simultaneous execution"
          },
          {
            "name": "exact full task SHA/method receipt acceptance",
            "state": "blocked",
            "reason": "No Git revision supplied; partial observation record explicitly not full method receipt"
          },
          {
            "name": "missing/incomplete result retry",
            "state": "blocked",
            "reason": "Required revision absent globally, cannot invent valid full acceptance; no actual retry performed"
          },
          {
            "name": "race/cancel/dropout exercises",
            "state": "not-applicable",
            "reason": "This walkthrough is partition-only; combined scenario handled separately and blocked there"
          },
          {
            "name": "installed host discovery/remote setup/model diversity",
            "state": "blocked",
            "reason": "No menu registration, remote bindings or actual-model identities observed"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "simultaneous parallel dispatch",
            "reason": "Shared native capacity required sequential waves; independence does not prove simultaneous execution"
          },
          {
            "variant": "exact full task SHA/method receipt acceptance",
            "reason": "No Git revision supplied; partial observation record explicitly not full method receipt"
          },
          {
            "variant": "missing/incomplete result retry",
            "reason": "Required revision absent globally, cannot invent valid full acceptance; no actual retry performed"
          },
          {
            "variant": "installed host discovery/remote setup/model diversity",
            "reason": "No menu registration, remote bindings or actual-model identities observed"
          }
        ],
        "limits": [
          "Bun absent; no runtime scripts executed.",
          "Full structured method contract remains blocked; no self-grade.",
          "Some early worker raw metadata only native transcript; retained repeated-read receipts do not repair original omission.",
          "No external services/account writes/settings/schedules.",
          "Prior Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Three independent authorized slice results cover the three fixture files at the exact SHA and method. The coordinator inspects terminal artifacts and returns one consolidated table with evidenced issues and explicit gaps/dropouts. Cancellation requires observed stop, terminal inspection and quarantine.",
        "reducedExpected": "Sequential review of the declared three-file partition may return reduced findings with exact revisions, inspected artifacts and visible missing slices. It proves neither independent workers nor a race.",
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
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
        "text": "Followed README to the actual full Swarm walkthrough and required capability/role/assignment contracts. Declared partition N3 over controller, facade and calculator before dispatch. Three fresh native identities read disjoint exact fixture files in sequential waves constrained by shared slots. Parent inspected all reports, source-copy identity and report digests. Controller wraps facade output, facade forwards to adapter, and calculator owns shared latest-result state. No defect is proven from controller/facade slices alone. Calculator cache scope is a static ownership observation, not a runtime test. All three source slices have retained independent observations; full revision-bound method acceptance is blocked because task Git SHA is missing. Attachment digest and supplied package freeze do not replace it. No race, failure injection or cancellation belongs to this partition-only walkthrough. Requested models inherited; actual identities unknown. Source reading does not prove installed menu discovery. A first guessed controller artifact filename failed, actual discovery found controller.mjs and byte comparison then returned exit0.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/result.json",
          "sha256": "863763b32a3a2f08fa50c2576a78a635a3288faa8bac45e782ece86a02b6d941",
          "bytes": 3503
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "sha256": "a0f4eb6e5baaded49263375472ed1d7b945b1aa4459538f99c6abf2f46b3ebf5",
            "bytes": 28398
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/case.json",
            "sha256": "e3eaba749aa0a79765207d04d1bcc312fa33c39b5c3e2f028f0627670216fe6f",
            "bytes": 1001
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/swarm-walkthrough/evidence/source-read-status.tsv",
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
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
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
