# codex: user-correction

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "user-correction",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-06.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Use /correct after I correct a repeated repository mistake. Inspect the available history and propose enforcement. Durable skill edits require my review and permission.",
  "caseDefinition": {
    "id": "user-correction",
    "sourcePaths": [
      "skills/correct/SKILL.md"
    ],
    "prompt": "Use /correct after I correct a repeated repository mistake. Inspect the available history and propose enforcement. Durable skill edits require my review and permission.",
    "requirements": [
      "Read recent commits, reverts, review comments, instruction files and workaround comments when available; declare gaps.",
      "Count a mistake class after two occurrences and prioritize architecture, types, lint or CI, behavior tests, then documentation for judgment calls.",
      "Prove new checks fail on real past mistakes and use the same local and CI command when authorized execution is available.",
      "Retain the rule/enforcement table, inline exceptions with reason, expiry and human approval, and the source reply contract.",
      "Require explicit review and permission before changing durable skills or agent instructions; commit and external actions require authorization."
    ],
    "expectedFull": "With authorized repository reads, writes and execution, fix the most frequent repeated classes, prove checks against real past mistakes, retain the rule table and report each class with evidence, selected level and why higher levels did not work. Obtain review and explicit permission for durable skill or instruction edits and authorization for each commit.",
    "expectedReduced": "If writes, execution or CI are unavailable or unauthorized, provide scoped findings and proposed enforcement, declare gaps, and retain the reply contract without claiming edits, failing checks, commits or CI success.",
    "expectedBlocked": "If repository evidence is unavailable, identify the missing access and request the relevant evidence. Do not invent repeated classes or edit durable skills.",
    "forbiddenClaims": [
      "A single occurrence proves a repeated class.",
      "Documentation alone prevents deterministic mistakes.",
      "Unobserved checks or CI passed.",
      "A correction authorizes durable skill edits, commits or external writes."
    ],
    "caseFile": "docs/parity/cases/skills/correct.json"
  },
  "registry": {
    "caseId": "user-correction",
    "caseFile": "docs/parity/cases/skills/correct.json",
    "sourcePaths": [
      "skills/correct/SKILL.md"
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
      "attemptId": "grades-native-06.json#0",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "user-correction",
      "status": "reduced-pass",
      "grade": {
        "caseId": "user-correction",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_6",
          "item_7",
          "item_18",
          "item_28"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Real historical replay/producer/CI integration absent."
        ],
        "review": "Uses synthetic repeated shipped corrections only, ranks structural status ownership before prose and runs prototype validator negative/positive checks. Real past Git/CI mistakes and authoritative producer absent; no durable edit without approval. Preserves enforcement table and concrete integration proposal.",
        "responseArtifact": "fixtures/batch-06/user-correction.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "With authorized repository reads, writes and execution, fix the most frequent repeated classes, prove checks against real past mistakes, retain the rule table and report each class with evidence, selected level and why higher levels did not work. Obtain review and explicit permission for durable skill or instruction edits and authorization for each commit.",
        "reducedExpected": "If writes, execution or CI are unavailable or unauthorized, provide scoped findings and proposed enforcement, declare gaps, and retain the reply contract without claiming edits, failing checks, commits or CI success.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-06.json",
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
        "text": "# user-correction\n\n## Supplied input\n\n> Use /correct after I correct a repeated repository mistake. Inspect the available history and propose enforcement. Durable skill edits require my review and permission.\n\nNamed source files and exact copied source bytes are retained in [user-correction/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/source-manifest.json) and [user-correction/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual response and evidence\n\nOne repeated class exists in supplied synthetic history, unsupported shipped claims. repeated-history.json events fixture-event-04 and fixture-event-06 explicitly record two occurrences. They meet the two-occurrence threshold only within synthetic input. The original history.json supplies a separate limited correction, not two independently verified real repository incidents.\n\nRecent commits and reverts are unavailable because there is no Git repository. git-history.txt and command-results.json retain failures. No live review comments, CI history, repository instruction file, or workaround comments for this class were supplied. The user-provided AGENTS instructions are available and preserve Bun and review-before-edit requirements. No live forge was contacted.\n\nChoose structured status ownership first. A single status producer should distinguish prepared, submitted and verified outcomes, with a receipt reference required for verified shipment. Free-text prose needs judgment beyond a schema. Type enforcement could prohibit construction of shipped state without a verified receipt in a typed producer, but no such application or typed producer is supplied. The disposable local check is a prototype mechanism, not a shipped architectural fix.\n\ncheck-status.mjs rejects shipped records without a receipt whose outcome is verified. It rejects both synthetic past occurrences with exit1 and accepts prepared with exit0. negative.json and positive.json preserve these inputs. additional-command-results.json preserves both exact command results. A caller can forge the receipt field, so this check does not establish independent receipt authenticity or constrain arbitrary prose. Actual real-past-mistake proof remains blocked by missing history.\n\n## Rule and enforcement proposal for review\n\n| Rule | Evidence | Selected level | Why a higher level is not yet demonstrated | Enforcement status |\n|---|---|---|---|---|\n| Shipment claims require an independently checked receipt | Synthetic events04 and06 | Single status owner, then typed status constructor; prototype runtime gate | No real status producer or types supplied | Local prototype only; integration unapproved |\n| Judgment claims distinguish proposal from observed outcome | Limited supplied correction | Documentation last for human interpretation | Schemas cannot establish truth of arbitrary prose | Proposed wording only |\n\nProposed AGENTS table row is the first row above. Proposed judgment sentence is \"Report prepared work as prepared; report shipment only with an independently checked receipt.\" Neither was applied. Durable instruction and skill changes require explicit review and permission, as correct/SKILL.md states, \"Before changing durable skills or agent instruction files, present the proposed edit for review and obtain explicit permission.\"\n\nProposed CI invocation is exactly the local command, bun user-correction/check-status.mjs <real-status-export.json>, once a real producer and CI scope are supplied. No CI run or integration occurred. Exceptions must sit on the offending line with reason, expiry date and human approval. No approved exception exists and no expiry was invented.\n\n## Variants and limits\n\nAvailable-history variant used supplied limited and repeated synthetic records. Missing-history variant is real, observed Git absence. Local negative/positive prototype checks ran. Real historical replay, CI parity, durable skill edit, AGENTS edit, commits and external actions remain unperformed. Source reply contract is preserved here through class, evidence, enforcement level and reason higher levels could not be demonstrated.\n",
        "artifact": {
          "path": "fixtures/batch-06/user-correction.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction.result.md",
          "sha256": "f97837f21679ecc15478490a36d00ee13d8f986203eaa52cf28e9defe32377f0",
          "bytes": 5857
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-06.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-06.events.jsonl",
            "sha256": "29e250d426d7f6e1853f71ccc210620bd85774dbbfaa2645ed41e80fe5d27d0b",
            "bytes": 497874,
            "eventReferences": [
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "27fa0bd0f51b5437f36dab3dcd17c394a5d7218d8024877877ebab356dce7f68"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a0641e13eefc8a0357d51bf1433e76171bd2477925c4fde93425fc8219847678",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "47752e596478dfe15ca960f407621e4b414297317af6fa359ed92ee8b7fbf796"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f92e8885378702b4bd7f8c8923b9d86fe857b3100ddd122500e258c0eea90617",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6eba47133a1cf683899747e15a84a0a81e82842f958a9258fbcce19951d11221"
              },
              {
                "eventId": "item_18",
                "line": 35,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "10d86c3726566e0f6a79e4f64f1b8f31f64c7752414b455c488854b4b5fbf77b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_28",
                "line": 52,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f95634a991bdf83a520d38029a33cffd5c0c1d25553b2c7b58c0de0780830db8"
              },
              {
                "eventId": "item_28",
                "line": 53,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "897622be432f98a936806993bfadfeaf44ae238d2155a8b6f7be5292d6d44677",
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
            "item_6",
            "item_7",
            "item_18",
            "item_28"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-06.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-06/user-correction/check-status.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/check-status.mjs",
      "sha256": "8302fd18867fcc30c8c47bef4795e2d737f4faebbee8250e6d4b229f2d192abe",
      "bytes": 316,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": "const path=process.argv[2];const records=await Bun.file(path).json();let errors=0;\nfor(const r of records)if(r.status==='shipped'&&(!r.receipt||r.receipt.outcome!=='verified')){console.error(`${r.id}: shipped requires an independently verified receipt; use draft or prepared`);errors++;}process.exitCode=errors?1:0;\n"
    },
    {
      "path": "fixtures/batch-06/user-correction/git-history.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/git-history.txt",
      "sha256": "d2b35cacadc66b7fad8dedd1be5244e17150a6625978c9330f831bd7a9cd6b1e",
      "bytes": 69,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": "fatal: not a git repository (or any of the parent directories): .git\n"
    },
    {
      "path": "fixtures/batch-06/user-correction/negative-output.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/negative-output.txt",
      "sha256": "32ee3ac5b10c69cf489154b2f2a69635b15118779009dd2a7584ccdea4b9cea1",
      "bytes": 184,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": "fixture-event-04: shipped requires an independently verified receipt; use draft or prepared\nfixture-event-06: shipped requires an independently verified receipt; use draft or prepared\n"
    },
    {
      "path": "fixtures/batch-06/user-correction/negative.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/negative.json",
      "sha256": "5ab10ea3c495249a18dc799b9d60f942eb93d987c17bcdf969b8a46ddea91783",
      "bytes": 92,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": "[{\"id\":\"fixture-event-04\",\"status\":\"shipped\"},{\"id\":\"fixture-event-06\",\"status\":\"shipped\"}]\n"
    },
    {
      "path": "fixtures/batch-06/user-correction/positive-output.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/positive-output.txt",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": ""
    },
    {
      "path": "fixtures/batch-06/user-correction/positive.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/positive.json",
      "sha256": "1e0ad9be840ea506c1f816db8dd09341bfd8036a6cc9ca1d62dce608c91804c9",
      "bytes": 37,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": "[{\"id\":\"draft\",\"status\":\"prepared\"}]\n"
    },
    {
      "path": "fixtures/batch-06/user-correction.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction.result.md",
      "sha256": "f97837f21679ecc15478490a36d00ee13d8f986203eaa52cf28e9defe32377f0",
      "bytes": 5857,
      "owners": [
        "grades-native-06.json#0"
      ],
      "text": "# user-correction\n\n## Supplied input\n\n> Use /correct after I correct a repeated repository mistake. Inspect the available history and propose enforcement. Durable skill edits require my review and permission.\n\nNamed source files and exact copied source bytes are retained in [user-correction/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/source-manifest.json) and [user-correction/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-correction/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual response and evidence\n\nOne repeated class exists in supplied synthetic history, unsupported shipped claims. repeated-history.json events fixture-event-04 and fixture-event-06 explicitly record two occurrences. They meet the two-occurrence threshold only within synthetic input. The original history.json supplies a separate limited correction, not two independently verified real repository incidents.\n\nRecent commits and reverts are unavailable because there is no Git repository. git-history.txt and command-results.json retain failures. No live review comments, CI history, repository instruction file, or workaround comments for this class were supplied. The user-provided AGENTS instructions are available and preserve Bun and review-before-edit requirements. No live forge was contacted.\n\nChoose structured status ownership first. A single status producer should distinguish prepared, submitted and verified outcomes, with a receipt reference required for verified shipment. Free-text prose needs judgment beyond a schema. Type enforcement could prohibit construction of shipped state without a verified receipt in a typed producer, but no such application or typed producer is supplied. The disposable local check is a prototype mechanism, not a shipped architectural fix.\n\ncheck-status.mjs rejects shipped records without a receipt whose outcome is verified. It rejects both synthetic past occurrences with exit1 and accepts prepared with exit0. negative.json and positive.json preserve these inputs. additional-command-results.json preserves both exact command results. A caller can forge the receipt field, so this check does not establish independent receipt authenticity or constrain arbitrary prose. Actual real-past-mistake proof remains blocked by missing history.\n\n## Rule and enforcement proposal for review\n\n| Rule | Evidence | Selected level | Why a higher level is not yet demonstrated | Enforcement status |\n|---|---|---|---|---|\n| Shipment claims require an independently checked receipt | Synthetic events04 and06 | Single status owner, then typed status constructor; prototype runtime gate | No real status producer or types supplied | Local prototype only; integration unapproved |\n| Judgment claims distinguish proposal from observed outcome | Limited supplied correction | Documentation last for human interpretation | Schemas cannot establish truth of arbitrary prose | Proposed wording only |\n\nProposed AGENTS table row is the first row above. Proposed judgment sentence is \"Report prepared work as prepared; report shipment only with an independently checked receipt.\" Neither was applied. Durable instruction and skill changes require explicit review and permission, as correct/SKILL.md states, \"Before changing durable skills or agent instruction files, present the proposed edit for review and obtain explicit permission.\"\n\nProposed CI invocation is exactly the local command, bun user-correction/check-status.mjs <real-status-export.json>, once a real producer and CI scope are supplied. No CI run or integration occurred. Exceptions must sit on the offending line with reason, expiry date and human approval. No approved exception exists and no expiry was invented.\n\n## Variants and limits\n\nAvailable-history variant used supplied limited and repeated synthetic records. Missing-history variant is real, observed Git absence. Local negative/positive prototype checks ran. Real historical replay, CI parity, durable skill edit, AGENTS edit, commits and external actions remain unperformed. Source reply contract is preserved here through class, evidence, enforcement level and reason higher levels could not be demonstrated.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/user-correction/history.json",
      "owner": "grades-native-06.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-06/user-correction/input.json",
      "owner": "grades-native-06.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-correction/repeated-history.json",
      "owner": "grades-native-06.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "fixtures/batch-06/user-correction/source-manifest.json",
      "owner": "grades-native-06.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-correction/source-reads.txt",
      "owner": "grades-native-06.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-correction/history.json",
      "owner": "grades-native-06.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-06/user-correction/input.json",
      "owner": "grades-native-06.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-correction/repeated-history.json",
      "owner": "grades-native-06.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "fixtures/batch-06/user-correction/source-manifest.json",
      "owner": "grades-native-06.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-correction/source-reads.txt",
      "owner": "grades-native-06.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
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
