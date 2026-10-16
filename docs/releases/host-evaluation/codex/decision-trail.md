# codex: decision-trail

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "decision-trail",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-07.json#7",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Keep an auditable local decision trail for a multi-phase run. Append a correction to a wrong claim, audit only this run against available history, and obtain cross-model review before handing back. Do not log secrets or claim unobserved completion.",
  "caseDefinition": {
    "id": "decision-trail",
    "sourcePaths": [
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/show-me-your-work/scripts/log.sh"
    ],
    "prompt": "Keep an auditable local decision trail for a multi-phase run. Append a correction to a wrong claim, audit only this run against available history, and obtain cross-model review before handing back. Do not log secrets or claim unobserved completion.",
    "requirements": [
      "Authorized local persistence and readback",
      "Accessible history for this run",
      "task 16 logging helper or equally safe TSV append",
      "Authorized independent reviewer with observed different model family for full review"
    ],
    "expectedFull": "Save and read back one canonical six-column TSV with sanitized single-line cells and formula-prefix protection. Preserve run start boundaries and append-only corrections. Resolve evidence, audit this run against its transcript, and obtain independent different-family review. End every trail-producing reply with Attention, observed reviewer model and row-specific flags or No flags. Exclude secrets and unobserved results.",
    "expectedReduced": "When history or different-family review is unavailable, preserve the local trail and report the precise audit or review gap in Attention. Sequential self-review is reduced capability and never substitutes for independent cross-model review. If durable writes are unavailable, provide an unsaved in-chat handoff only when authorized and disclose that no durable trail was saved.",
    "expectedBlocked": "Denied persistence blocks a claimed saved trail. Missing helper blocks helper execution unless an authorized equivalent preserves sanitization. Missing transcript or observed different-family reviewer blocks the corresponding full audit or cross-model claim. Report denied or unavailable capabilities without invented success.",
    "forbiddenClaims": [
      "Secrets or private unrelated transcripts in the trail",
      "Saved trail without write and readback",
      "Edited or deleted prior rows",
      "Independent cross-model review from self-review or unknown model family",
      "Tests green, completed work or evidence resolution without observation",
      "Commit, publication or external writes without explicit authorization"
    ],
    "caseFile": "docs/parity/cases/skills/show-me-your-work.json"
  },
  "registry": {
    "caseId": "decision-trail",
    "caseFile": "docs/parity/cases/skills/show-me-your-work.json",
    "sourcePaths": [
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/show-me-your-work/scripts/log.sh"
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
        "inspect-result",
        "isolated-write"
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
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-07.json#7",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 7,
      "host": "codex",
      "caseId": "decision-trail",
      "status": "reduced-pass",
      "grade": {
        "caseId": "decision-trail",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_13",
          "item_21",
          "item_38"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Full transcript audit and observed different-family review unverified."
        ],
        "review": "Actual installed append-only log helper writes/readbacks canonical trail, intentional wrong claim preserved and superseded, real negative baseline evidence cited. Independent artifact review narrows weak pointers via appended correction. Complete transcript and verified different-family reviewer absent; Attention correctly says unknown.",
        "responseArtifact": "fixtures/batch-07/decision-trail.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Save and read back one canonical six-column TSV with sanitized single-line cells and formula-prefix protection. Preserve run start boundaries and append-only corrections. Resolve evidence, audit this run against its transcript, and obtain independent different-family review. End every trail-producing reply with Attention, observed reviewer model and row-specific flags or No flags. Exclude secrets and unobserved results.",
        "reducedExpected": "When history or different-family review is unavailable, preserve the local trail and report the precise audit or review gap in Attention. Sequential self-review is reduced capability and never substitutes for independent cross-model review. If durable writes are unavailable, provide an unsaved in-chat handoff only when authorized and disclose that no durable trail was saved.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-07.json",
            "reviewedBy": "grade_contract_audit independent reviewer"
          }
        ]
      },
      "topLevelContext": {
        "limits": [
          "Root command JSONL and retained child-produced artifacts inspected. Worker summary transcriptions are not signed raw method receipts.",
          "Inherited-context thread-store failure followed fresh-context success must not be described as absent worker tools.",
          "TaskGit SHA missing in these baseline fixtures remains distinct from package source freeze.",
          "No actual PR/service/scheduler behavior credited from local replay programs.",
          "No exitreceipt needed to infer batch completion here: actual native turn.completed and final response exist; paused outer orchestrator not counted as case failure."
        ]
      },
      "response": {
        "text": "# decision-trail\n\n## Supplied input\n\nKeep an auditable local decision trail for a multi-phase run. Append a correction to a wrong claim, audit only this run against available history, and obtain cross-model review before handing back. Do not log secrets or claim unobserved completion.\n\nPackage source freeze supplied by the user: f4623636a287bea2aa79c4b2234a53d20a5f193c. Only installed 0.1.0 source was read. Named sources are preserved in this case's source-read.txt and source-files.json. The package and task fixture are not Git repositories here. The freeze is not a verified task revision. No service, commit, push, PR, dependency installation, configuration change or schedule was performed.\n\n## Actual response and actions\n\nCreated decision-trail/decision.tsv using the installed log.sh through Bun.spawnSync. Preserved the initial deliberately wrong exercise claim, appended its correction, and read back the unchanged prior row and new rows into decision-readback.txt. The correction says the export baseline gate failed with exit 1. It points to the actual baseline-command.txt. No baseline-green or optimization-complete claim survives the correction.\n\nActual invocation arguments and exit statuses are in performance-command-results.json. The run audit is scoped to current-turn tool output and generated artifacts. synthetic-history.json was copied from the prepared shared input; it contains a proposal-versus-shipped correction and no external actions. It was not used as evidence of this run's prior history. No global or unrelated private transcript search occurred.\n\nThe log uses the source TSV columns and append-only helper. No secret-bearing values were supplied. Local .gitignore includes decision.tsv, though no Git repository exists here. Persistence is demonstrated by helper exit 0 and direct saved-byte readback. The log proves recorded decisions, not continuity or unattended execution.\n\n## Variants and limits\n\nThe explicit wrong-claim correction exercise was executed. History access is partial: visible conversation and tool results exist, but no complete machine-readable transcript export is exposed. Fresh independent readonly worker /root/trail_review returned an artifact-level review, preserved in decision-trail/review.md. Two weak evidence pointers were narrowed by append-only corrections, not edited away. Actual model/family was unexposed. Full cross-model review cannot be claimed from a requested model alone.\n\n## Attention\n\nreviewed by unknown\n\nThe independent artifact review found weak pointers in original rows 3 and 4. New rows narrow those claims. Complete transcript audit and verified different-model-family review remain open. The false claim in row 2 is intentionally retained and superseded by row 3, not deleted.\n",
        "artifact": {
          "path": "fixtures/batch-07/decision-trail.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail.result.md",
          "sha256": "943b78efbb9dba9c5aa3ac87688487ab74d7ede782c536739aea2955be84a302",
          "bytes": 2771
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-07.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-07.events.jsonl",
            "sha256": "26078a6d01730e84b6d57421e843541eb5b82f4c8b0cdd0b167ecf6636bbc630",
            "bytes": 636607,
            "eventReferences": [
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c39ca46f7c09559ae3206965b3361defa4b87d3cc7d481e755062b699459248d"
              },
              {
                "eventId": "item_13",
                "line": 26,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0ae80e5985a1a4aeeadd411872884cecff4e25247358cfdc041ecb343c06c551",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "00a1d39e50791c9041a79d7bf1869f42b2f40cae2ee8b09fd8abc7fd74d1463e"
              },
              {
                "eventId": "item_21",
                "line": 41,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c0af66489d0de4494f6f77cf94b6baf4d506b70b81dd58439764e409bef9e1c1",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_38",
                "line": 70,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c0353cb9b1890b86ebe3510a1ec49051ec8c8700db539a343e165e033cded6a0"
              },
              {
                "eventId": "item_38",
                "line": 71,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0897e4d615564eef78bb6dd7e03bfd5683ed2557ac2b7d95d74fbad7c7bccea5",
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
            "item_13",
            "item_21",
            "item_38"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-07.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-07/decision-trail/.gitignore",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/.gitignore",
      "sha256": "8fadd16cc626b1932746f316f5b38b206875fd9602b24f2164e8b3df6f8e0102",
      "bytes": 13,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "decision.tsv\n"
    },
    {
      "path": "fixtures/batch-07/decision-trail/audit-scope.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/audit-scope.md",
      "sha256": "a72a7d14d3670c7dca3f580ab9b6db67536bff66989ca6359a5ed31552f80215",
      "bytes": 1088,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "This artifact records the parent audit scope, not a recovered transcript. The current conversation exposes its tool outputs to the parent, but no complete export of this run's transcript was supplied. No private-history search was attempted. The prepared synthetic-history.json is marked inert fixture-only and excluded as evidence of this conversation.\n\nObserved artifact audit: decision.tsv and decision-readback.txt matched before this follow-up. performance-command-results.json records real helper invocations and baseline/profiler command outputs. bounded-improvement/baseline-command.txt proves gate exit 1. The zero-iteration account is a scoped parent report in bounded-improvement.result.md, not independently proven by that single baseline file. No full transcript audit or exhaustive absence proof is claimed.\n\nThe reviewer result is review.md. Its evidence-pointer flags are retained and narrowed by append-only correction rows. The original false-claim row remains visible as an exercise. Requested different model selection is not observed different model-family evidence.\n"
    },
    {
      "path": "fixtures/batch-07/decision-trail/decision-readback.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/decision-readback.txt",
      "sha256": "f3af4f6c407c2c7c338c46c3c3269822b1e658dc22091ddd3b2a164f78c83854",
      "bytes": 1369,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:59:24Z\texercise\tDeliberately record wrong claim that baseline gate was green\tRequested correction exercise; this claim is false\t../bounded-improvement/baseline-command.txt\tWRONG CLAIM FOR TEST\n2026-10-16T07:59:24Z\tcorrection\tSupersede prior row: baseline gate failed with exit 1\tThe actual command output contradicts the prior exercise claim\t../bounded-improvement/baseline-command.txt\tRED; no optimization loop completed\n2026-10-16T07:59:24Z\taudit\tAudit only current-run local artifacts and visible tool history\tShared history.json is synthetic and not this conversation transcript\t../bounded-improvement/baseline-command.txt\tpartial audit; machine-readable full transcript unavailable\n2026-10-16T08:05:25Z\tcorrection\tNarrow row 3 evidence to failed baseline gate only\tA single baseline command cannot prove no other loop ran\taudit-scope.md\tRED gate independently shown; zero iterations is scoped parent report\n2026-10-16T08:05:25Z\tcorrection\tSupersede row 4 complete-scope implication with artifact-only audit\tNo complete transcript export is exposed; reviewer found weak pointer\treview.md\tpartial artifact audit only\n2026-10-16T08:05:25Z\treview\tRetain independent reviewer flags and unknown actual model\tA requested model does not prove its actual family\treview.md\tdifferent-model-family review remains unverified\n"
    },
    {
      "path": "fixtures/batch-07/decision-trail/decision.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/decision.tsv",
      "sha256": "f3af4f6c407c2c7c338c46c3c3269822b1e658dc22091ddd3b2a164f78c83854",
      "bytes": 1369,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:59:24Z\texercise\tDeliberately record wrong claim that baseline gate was green\tRequested correction exercise; this claim is false\t../bounded-improvement/baseline-command.txt\tWRONG CLAIM FOR TEST\n2026-10-16T07:59:24Z\tcorrection\tSupersede prior row: baseline gate failed with exit 1\tThe actual command output contradicts the prior exercise claim\t../bounded-improvement/baseline-command.txt\tRED; no optimization loop completed\n2026-10-16T07:59:24Z\taudit\tAudit only current-run local artifacts and visible tool history\tShared history.json is synthetic and not this conversation transcript\t../bounded-improvement/baseline-command.txt\tpartial audit; machine-readable full transcript unavailable\n2026-10-16T08:05:25Z\tcorrection\tNarrow row 3 evidence to failed baseline gate only\tA single baseline command cannot prove no other loop ran\taudit-scope.md\tRED gate independently shown; zero iterations is scoped parent report\n2026-10-16T08:05:25Z\tcorrection\tSupersede row 4 complete-scope implication with artifact-only audit\tNo complete transcript export is exposed; reviewer found weak pointer\treview.md\tpartial artifact audit only\n2026-10-16T08:05:25Z\treview\tRetain independent reviewer flags and unknown actual model\tA requested model does not prove its actual family\treview.md\tdifferent-model-family review remains unverified\n"
    },
    {
      "path": "fixtures/batch-07/decision-trail/final-log-commands.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/final-log-commands.json",
      "sha256": "95c574f1be6afe51d7bc1a37907cbe712942067b9995eab8f47b6469f2619a69",
      "bytes": 1736,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "[\n  {\n    \"argv\": [\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/decision.tsv\",\n      \"correction\",\n      \"Narrow row 3 evidence to failed baseline gate only\",\n      \"A single baseline command cannot prove no other loop ran\",\n      \"audit-scope.md\",\n      \"RED gate independently shown; zero iterations is scoped parent report\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/decision.tsv\",\n      \"correction\",\n      \"Supersede row 4 complete-scope implication with artifact-only audit\",\n      \"No complete transcript export is exposed; reviewer found weak pointer\",\n      \"review.md\",\n      \"partial artifact audit only\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/decision.tsv\",\n      \"review\",\n      \"Retain independent reviewer flags and unknown actual model\",\n      \"A requested model does not prove its actual family\",\n      \"review.md\",\n      \"different-model-family review remains unverified\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-07/decision-trail/finalize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/finalize.mjs",
      "sha256": "73f2882e72feecaaaa5811d1a3102d170a849fcce53b588f1967e6660e9a5d39",
      "bytes": 2156,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "import {readFileSync,writeFileSync} from 'node:fs';\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst root=process.cwd();const receipts=[];\nfor(const [phase,decision,why,evidence,result] of [\n['correction','Narrow row 3 evidence to failed baseline gate only','A single baseline command cannot prove no other loop ran','audit-scope.md','RED gate independently shown; zero iterations is scoped parent report'],\n['correction','Supersede row 4 complete-scope implication with artifact-only audit','No complete transcript export is exposed; reviewer found weak pointer','review.md','partial artifact audit only'],\n['review','Retain independent reviewer flags and unknown actual model','A requested model does not prove its actual family','review.md','different-model-family review remains unverified']]){\nconst argv=['bash',pkg+'/skills/show-me-your-work/scripts/log.sh',root+'/decision-trail/decision.tsv',phase,decision,why,evidence,result];const r=Bun.spawnSync(argv);receipts.push({argv,exitCode:r.exitCode,stdout:r.stdout.toString(),stderr:r.stderr.toString()});}\nwriteFileSync('decision-trail/final-log-commands.json',JSON.stringify(receipts,null,2));writeFileSync('decision-trail/decision-readback.txt',readFileSync('decision-trail/decision.tsv'));\nconst path='decision-trail.result.md';let report=readFileSync(path,'utf8').replace('Independent reviewer requested separately; observed results and model-family limits are recorded in review.md when available.','Fresh independent readonly worker /root/trail_review returned an artifact-level review, preserved in decision-trail/review.md. Two weak evidence pointers were narrowed by append-only corrections, not edited away. Actual model/family was unexposed.');report=report.replace('Complete transcript audit and verified different-model-family review remain open.','The independent artifact review found weak pointers in original rows 3 and 4. New rows narrow those claims. Complete transcript audit and verified different-model-family review remain open.');writeFileSync(path,report);\nconsole.log(readFileSync('decision-trail/decision.tsv','utf8'));\n"
    },
    {
      "path": "fixtures/batch-07/decision-trail/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/review.md",
      "sha256": "62cd97bdbe0c6f864398cee3fb5d5771e13f28fcdc3669f71b67616ff0de2f51",
      "bytes": 780,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "Fresh readonly reviewer /root/trail_review, assignment trail-review-1. Requested gpt-6-luna/high; actual model, effort and family are unexposed. This is observed independent artifact review, not verified cross-model review.\n\nThe reviewer read the trail, readback, reports, actual baseline evidence, command records and scripts. It found two gaps. Row 4 points only to baseline-command.txt, which cannot prove transcript access or audit scope. Row 3 points to the same command, which proves a red gate but cannot by itself prove no optimization loop completed. The reviewer found the deliberately wrong row 2 properly superseded and readback identical. Full transcript and exact task Git SHA remain unavailable. The parent appended narrower corrections rather than rewriting rows.\n"
    },
    {
      "path": "fixtures/batch-07/decision-trail/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail/source-files.json",
      "sha256": "b2849a82106c1db4c1d141fe9d07a156828f356fdc93cc972927c3a8aee01b95",
      "bytes": 153,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "[\n  \"skills/show-me-your-work/SKILL.md\",\n  \"skills/show-me-your-work/references/decision-log-template.tsv\",\n  \"skills/show-me-your-work/scripts/log.sh\"\n]"
    },
    {
      "path": "fixtures/batch-07/decision-trail.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/decision-trail.result.md",
      "sha256": "943b78efbb9dba9c5aa3ac87688487ab74d7ede782c536739aea2955be84a302",
      "bytes": 2771,
      "owners": [
        "grades-native-07.json#7"
      ],
      "text": "# decision-trail\n\n## Supplied input\n\nKeep an auditable local decision trail for a multi-phase run. Append a correction to a wrong claim, audit only this run against available history, and obtain cross-model review before handing back. Do not log secrets or claim unobserved completion.\n\nPackage source freeze supplied by the user: f4623636a287bea2aa79c4b2234a53d20a5f193c. Only installed 0.1.0 source was read. Named sources are preserved in this case's source-read.txt and source-files.json. The package and task fixture are not Git repositories here. The freeze is not a verified task revision. No service, commit, push, PR, dependency installation, configuration change or schedule was performed.\n\n## Actual response and actions\n\nCreated decision-trail/decision.tsv using the installed log.sh through Bun.spawnSync. Preserved the initial deliberately wrong exercise claim, appended its correction, and read back the unchanged prior row and new rows into decision-readback.txt. The correction says the export baseline gate failed with exit 1. It points to the actual baseline-command.txt. No baseline-green or optimization-complete claim survives the correction.\n\nActual invocation arguments and exit statuses are in performance-command-results.json. The run audit is scoped to current-turn tool output and generated artifacts. synthetic-history.json was copied from the prepared shared input; it contains a proposal-versus-shipped correction and no external actions. It was not used as evidence of this run's prior history. No global or unrelated private transcript search occurred.\n\nThe log uses the source TSV columns and append-only helper. No secret-bearing values were supplied. Local .gitignore includes decision.tsv, though no Git repository exists here. Persistence is demonstrated by helper exit 0 and direct saved-byte readback. The log proves recorded decisions, not continuity or unattended execution.\n\n## Variants and limits\n\nThe explicit wrong-claim correction exercise was executed. History access is partial: visible conversation and tool results exist, but no complete machine-readable transcript export is exposed. Fresh independent readonly worker /root/trail_review returned an artifact-level review, preserved in decision-trail/review.md. Two weak evidence pointers were narrowed by append-only corrections, not edited away. Actual model/family was unexposed. Full cross-model review cannot be claimed from a requested model alone.\n\n## Attention\n\nreviewed by unknown\n\nThe independent artifact review found weak pointers in original rows 3 and 4. New rows narrow those claims. Complete transcript audit and verified different-model-family review remain open. The false claim in row 2 is intentionally retained and superseded by row 3, not deleted.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/decision-trail/source-read.txt",
      "owner": "grades-native-07.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/decision-trail/synthetic-history.json",
      "owner": "grades-native-07.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-07/decision-trail/source-read.txt",
      "owner": "grades-native-07.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/decision-trail/synthetic-history.json",
      "owner": "grades-native-07.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    }
  ],
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
