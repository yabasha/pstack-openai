# chatgpt: history-evidence

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "history-evidence",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Why does this retry threshold exist? The code history records a change, a shared ticket states a customer constraint, telemetry correlates with the release, and chat is unavailable. Distinguish the evidence from inference.",
  "caseDefinition": {
    "id": "history-evidence",
    "sourcePaths": [
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md"
    ],
    "prompt": "Why does this retry threshold exist? The code history records a change, a shared ticket states a customer constraint, telemetry correlates with the release, and chat is unavailable. Distinguish the evidence from inference.",
    "requirements": [
      "Anchor files, symbols, commit history and PR or ticket leads before investigation.",
      "Discover all seven evidence categories; record missing connectors and denied history as gaps.",
      "Use category investigators and a citation-checking synthesizer when independent workers are available; disclose sequential reduced capability otherwise.",
      "Preserve Direct, Supported, Inferred, Speculative and Unknown tiers, contradictions, exact queries and source citations.",
      "Keep source history, shared-record evidence and inference distinct; preserve source-specific search and privacy limits."
    ],
    "expectedFull": "Independent category investigators return searched queries, citations, contradictions and gaps. The synthesizer spot-checks citations and reports the eight source-defined sections, distinguishing the historical change from the ticket's stated motivation and telemetry inference; unavailable chat is an explicit gap.",
    "expectedReduced": "Without independent workers, sequential category passes and synthesis are labelled reduced capability. With missing connectors or gh, available history is inspected and each inaccessible source is named without invented rationale or complete-coverage claims.",
    "expectedBlocked": "If no authorized source or history reads are available, report the blocked investigation and exact access gaps rather than producing an evidence-backed rationale.",
    "forbiddenClaims": [
      "Code mechanics alone prove author intent.",
      "Missing connectors returned no relevant records.",
      "Sequential passes are independent investigators.",
      "Requested models prove actual model selection.",
      "Telemetry correlation proves causation.",
      "Structural validation proves host behavior.",
      "Read permission authorizes external writes or private-content redistribution."
    ],
    "caseFile": "docs/parity/cases/skills/why.json"
  },
  "registry": {
    "caseId": "history-evidence",
    "caseFile": "docs/parity/cases/skills/why.json",
    "sourcePaths": [
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md"
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
      "attemptId": "grades-chatgpt-09-12.json#0",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 0,
      "host": "chatgpt",
      "caseId": "history-evidence",
      "status": "reduced-pass",
      "grade": {
        "caseId": "history-evidence",
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
        "review": "Separates actual inert ticket narrative from unretrieved history/customer contract, rejects nonexistent telemetry correlation and preserves seven-source gaps. No independent category pipeline or live rationale conclusion credited.",
        "actualResponse": "The supplied ticket narrative explicitly requests three attempts for intermittent upstream failures. That is Direct evidence of what the fixture says, not a retrieved ticket or proven customer requirement. The code narrative says the threshold changed from 2 to 3 without a commit. This supports a possible link but cannot establish implementation history. Telemetry is explicitly not supplied, contradicting the prompt's claimed correlation. Inferred explanation: three attempts likely accommodate intermittent upstream failures. Speculative alternatives include convention or tuning; neither is evidenced. Unknown: actual target symbol/file, commits, PRs, author/date, telemetry, customer contract and chat. All seven categories were considered. Source history is absent from the inert fixture, tracker evidence is the supplied shared-records.json only, long-form docs and chat were not queried because live accounts are prohibited, infrastructure observability/error tracking/warehouse have no supplied records or exposed relevant bindings identified. No live search occurred. Confidence is limited to fixture narrative. Full category investigators/synthesizer pipeline is blocked by missing code anchor/history and relevant authorized service inputs; native workers exist and were not claimed missing.",
        "variants": [
          {
            "name": "supplied ticket/code record",
            "state": "attempted",
            "reason": "Read actual additional/history/shared-records.json; fixture records remain inert."
          },
          {
            "name": "telemetry correlation",
            "state": "blocked",
            "reason": "Fixture explicitly says telemetry not supplied."
          },
          {
            "name": "seven-category live investigation",
            "state": "blocked",
            "reason": "Live accounts forbidden; no target code/commit or authorized relevant service coordinates."
          },
          {
            "name": "independent category investigators and synthesizer",
            "state": "blocked",
            "reason": "No anchored task/history or authorized source-backed categories; no invented source queries."
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "telemetry correlation",
            "reason": "Fixture explicitly says telemetry not supplied."
          },
          {
            "variant": "seven-category live investigation",
            "reason": "Live accounts forbidden; no target code/commit or authorized relevant service coordinates."
          },
          {
            "variant": "independent category investigators and synthesizer",
            "reason": "No anchored task/history or authorized source-backed categories; no invented source queries."
          }
        ],
        "limits": [
          "No live service/account actions.",
          "Full task Git revision absent; attachment SHA is not a Git SHA.",
          "Earlier batch-00 Node/Python deviation remains recorded, not repeated here.",
          "Early exploratory raw tool JSON not all captured locally; host transcript contains outputs including disclosed truncation.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Independent category investigators return searched queries, citations, contradictions and gaps. The synthesizer spot-checks citations and reports the eight source-defined sections, distinguishing the historical change from the ticket's stated motivation and telemetry inference; unavailable chat is an explicit gap.",
        "reducedExpected": "Without independent workers, sequential category passes and synthesis are labelled reduced capability. With missing connectors or gh, available history is inspected and each inaccessible source is named without invented rationale or complete-coverage claims.",
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
        "text": "The supplied ticket narrative explicitly requests three attempts for intermittent upstream failures. That is Direct evidence of what the fixture says, not a retrieved ticket or proven customer requirement. The code narrative says the threshold changed from 2 to 3 without a commit. This supports a possible link but cannot establish implementation history. Telemetry is explicitly not supplied, contradicting the prompt's claimed correlation. Inferred explanation: three attempts likely accommodate intermittent upstream failures. Speculative alternatives include convention or tuning; neither is evidenced. Unknown: actual target symbol/file, commits, PRs, author/date, telemetry, customer contract and chat. All seven categories were considered. Source history is absent from the inert fixture, tracker evidence is the supplied shared-records.json only, long-form docs and chat were not queried because live accounts are prohibited, infrastructure observability/error tracking/warehouse have no supplied records or exposed relevant bindings identified. No live search occurred. Confidence is limited to fixture narrative. Full category investigators/synthesizer pipeline is blocked by missing code anchor/history and relevant authorized service inputs; native workers exist and were not claimed missing.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/result.json",
          "sha256": "198a0fd98d8c9acea89dd736bfd07c7c7ad7f74ba8f030067864bba97d0a9455",
          "bytes": 2864
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/case.json",
            "sha256": "70064378d3858dd587b1c4756acf49264ad4d4c8977289b75c118ae203b3417a",
            "bytes": 1546
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-09/cases/history-evidence/evidence/source-read-status.tsv",
            "sha256": "7c11b6ec40bc3cc75b15ea25f049d21cc8aece324da26d45bfe354cab81bab4d",
            "bytes": 559
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
    "Input Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
