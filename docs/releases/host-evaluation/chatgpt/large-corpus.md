# chatgpt: large-corpus

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "large-corpus",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-guard-the-context-window to an accessible large corpus with verbose command output, screenshots and long documents. Keep the main thread useful, plan bounded phases and use independent workers only when authorized and available. Report unavailable access or delegation honestly.",
  "caseDefinition": {
    "id": "large-corpus",
    "sourcePaths": [
      "skills/principle-guard-the-context-window/SKILL.md"
    ],
    "prompt": "Apply principle-guard-the-context-window to an accessible large corpus with verbose command output, screenshots and long documents. Keep the main thread useful, plan bounded phases and use independent workers only when authorized and available. Report unavailable access or delegation honestly.",
    "requirements": [
      "Isolate verbose outputs, screenshots and large documents; retain summaries in the main thread.",
      "Keep templates and references used on every invocation inline.",
      "Limit files per phase, set turn budgets and account for mechanism costs.",
      "Check current read and independent-worker capabilities and authorization before delegating; inspect actual worker results.",
      "If delegation is unavailable, narrow accessible evidence sequentially as reduced capability without inventing workers."
    ],
    "expectedFull": "Use authorized independent workers with observed identities and inspected results to summarize bulky accessible evidence. Keep summaries in the main thread, frequently used content inline and phases bounded by file limits, turn budgets and mechanism costs.",
    "expectedReduced": "When independent workers are unavailable or unauthorized but evidence is readable, label reduced capability, narrow the accessible corpus into bounded sequential phases and keep summaries in the main thread. State that no independent workers ran.",
    "expectedBlocked": "When required evidence cannot be accessed, identify the missing material and access limits; do not claim to have inspected or summarized it. Provide only a provisional bounded plan.",
    "forbiddenClaims": [
      "Workers exist or ran without observed authorized delegation.",
      "Sequential reading establishes independent-worker capability.",
      "Unread evidence was inspected or summarized.",
      "Case definitions or structural checks prove host behavior."
    ],
    "caseFile": "docs/parity/cases/skills/principle-guard-the-context-window.json"
  },
  "registry": {
    "caseId": "large-corpus",
    "caseFile": "docs/parity/cases/skills/principle-guard-the-context-window.json",
    "sourcePaths": [
      "skills/principle-guard-the-context-window/SKILL.md"
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
      "attemptId": "grades-chatgpt-09-12.json#2",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 2,
      "host": "chatgpt",
      "caseId": "large-corpus",
      "status": "reduced-pass",
      "grade": {
        "caseId": "large-corpus",
        "batch": "batch-09",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Actual native isolated corpus reader provides bounded counts/summary and parent artifact inspection; repeated fixture statements not treated as fact. Screenshots/long-doc variants absent and exact task revision missing prevent full method acceptance.",
        "actualResponse": "An independent native reader isolated the verbose corpus and returned a bounded summary. Parent inspected retained report and artifacts. The input contains 160 synthetic records, 46,932 bytes, IDs 1 through 160 unique. Forty repeat a cache disposal/invalidation timing caution; 120 repeat invoice formatting/empty/nonfinite statements. Those statements are unverified fixture claims. Three phases bounded the review to six distinct files under a 15-file budget. Frequently used capability/assignment guidance was kept with the source read artifacts. No screenshots or separate long documents were supplied. Attachment digest and observed corpus digest identify different scopes, not a content discrepancy. Native worker independence observed; parallel category decomposition not claimed. Exact Git assignment validation remains blocked. Raw corpus stayed out of the parent response.",
        "variants": [
          {
            "name": "verbose text corpus",
            "state": "attempted",
            "reason": "Observed native worker corpus_review plus parent report/artifact inspection."
          },
          {
            "name": "screenshots",
            "state": "blocked",
            "reason": "No screenshots supplied."
          },
          {
            "name": "long documents",
            "state": "blocked",
            "reason": "No separate long documents supplied in scoped corpus."
          },
          {
            "name": "missing delegation",
            "state": "attempted",
            "reason": "Counterfactual reduction is bounded sequential phases, not represented as an actual worker absence."
          },
          {
            "name": "exact task revision",
            "state": "blocked",
            "reason": "No full Git SHA; file and attachment digests retained separately."
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "screenshots",
            "reason": "No screenshots supplied."
          },
          {
            "variant": "long documents",
            "reason": "No separate long documents supplied in scoped corpus."
          },
          {
            "variant": "exact task revision",
            "reason": "No full Git SHA; file and attachment digests retained separately."
          }
        ],
        "limits": [
          "Bun absent; no runtime scripts executed.",
          "No live external operations.",
          "Early initial raw metadata export incomplete; source outputs and native transcript remain.",
          "Durable persistence not established.",
          "Earlier Node/Python deviation preserved, not repeated.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Use authorized independent workers with observed identities and inspected results to summarize bulky accessible evidence. Keep summaries in the main thread, frequently used content inline and phases bounded by file limits, turn budgets and mechanism costs.",
        "reducedExpected": "When independent workers are unavailable or unauthorized but evidence is readable, label reduced capability, narrow the accessible corpus into bounded sequential phases and keep summaries in the main thread. State that no independent workers ran.",
        "concreteFixCandidates": [],
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
        "text": "An independent native reader isolated the verbose corpus and returned a bounded summary. Parent inspected retained report and artifacts. The input contains 160 synthetic records, 46,932 bytes, IDs 1 through 160 unique. Forty repeat a cache disposal/invalidation timing caution; 120 repeat invoice formatting/empty/nonfinite statements. Those statements are unverified fixture claims. Three phases bounded the review to six distinct files under a 15-file budget. Frequently used capability/assignment guidance was kept with the source read artifacts. No screenshots or separate long documents were supplied. Attachment digest and observed corpus digest identify different scopes, not a content discrepancy. Native worker independence observed; parallel category decomposition not claimed. Exact Git assignment validation remains blocked. Raw corpus stayed out of the parent response.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/result.json",
          "sha256": "3b2bc04da1696f8ec26bf952110e640ca2294a33325d1a1b58b93b8b329514de",
          "bytes": 2370
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/case.json",
            "sha256": "33040919a7a21bb8c80153add768f750f25156e6be64c7d215fdfbd6592fab5d",
            "bytes": 950
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/large-corpus/evidence/source-read-status.tsv",
            "sha256": "1c2dcf649aa02d2c3b2e33627ff409a680591ff77d82a86845c554c9808cde2a",
            "bytes": 53
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
