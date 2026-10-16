# codex: uncertain-result

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "uncertain-result",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-05.json#6",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Figure it out: design and carry out an auditable migration playbook. The initial measurement is ambiguous and the deployment evidence is inaccessible. Investigate accessible evidence and report what remains uncertain.",
  "caseDefinition": {
    "id": "uncertain-result",
    "sourcePaths": [
      "skills/figure-it-out/SKILL.md"
    ],
    "prompt": "Figure it out: design and carry out an auditable migration playbook. The initial measurement is ambiguous and the deployment evidence is inaccessible. Investigate accessible evidence and report what remains uncertain.",
    "requirements": [
      "Accessible source and artifacts",
      "Authorized artifact inspection and execution for verification",
      "Decision-trail persistence; independent workers only when exposed and authorized"
    ],
    "expectedFull": "Frames a falsifiable predicate, quantifies scope, chooses rigor and checkpoint, designs phases before code, captures baseline, investigates accessible evidence through hypothesis/change/measurement loops, records decisions as units land, and hands back the playbook, rigor rationale, trail path, verified results and concrete inaccessible-evidence limit. Uses INCONCLUSIVE for unresolved observations.",
    "expectedReduced": "Uses authorized accessible artifacts and sequential work when independent workers are unavailable, labels reduced capability, preserves the five phases and reports missing execution or persistence as concrete limits. No inaccessible result is fabricated.",
    "expectedBlocked": "States which required evidence or operation is inaccessible or denied, reports NOT VERIFIED or INCONCLUSIVE, and supplies the designed workflow and open questions without inventing execution or a saved trail.",
    "forbiddenClaims": [
      "Inconclusive evidence is a pass",
      "Unavailable deployment evidence proves migration success",
      "Sequential work establishes independent workers",
      "A trail was saved without observed persistence",
      "Workflow autonomy authorizes external actions"
    ],
    "caseFile": "docs/parity/cases/skills/figure-it-out.json"
  },
  "registry": {
    "caseId": "uncertain-result",
    "caseFile": "docs/parity/cases/skills/figure-it-out.json",
    "sourcePaths": [
      "skills/figure-it-out/SKILL.md"
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
      "attemptId": "grades-native-05.json#6",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 6,
      "host": "codex",
      "caseId": "uncertain-result",
      "status": "reduced-pass",
      "grade": {
        "caseId": "uncertain-result",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-05.events.jsonl",
        "actualReadEventIds": [
          "item_9",
          "item_16",
          "item_17",
          "item_23",
          "item_28"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome",
          "execution",
          "persistence"
        ],
        "missing": [
          "Independent required trail review and full transcript audit unobserved; assignment prerequisites absent."
        ],
        "review": "Actually designs phases before source edits, captures baseline, migrates tagged API and all callers, executes checks, records decisions using installed log helper and inspects saved trail. Corrected full execution/persistence/grants are substantively met. Independent required trail review/transcript audit remains blocked by missing taskSHA/transcript, with no worker attempted; measurement and deployment correctly INCONCLUSIVE.",
        "responseArtifact": "fixtures/batch-05/uncertain-result.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-05.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Frames a falsifiable predicate, quantifies scope, chooses rigor and checkpoint, designs phases before code, captures baseline, investigates accessible evidence through hypothesis/change/measurement loops, records decisions as units land, and hands back the playbook, rigor rationale, trail path, verified results and concrete inaccessible-evidence limit. Uses INCONCLUSIVE for unresolved observations.",
        "reducedExpected": "Uses authorized accessible artifacts and sequential work when independent workers are unavailable, labels reduced capability, preserves the five phases and reports missing execution or persistence as concrete limits. No inaccessible result is fabricated.",
        "permissionReview": {
          "execution": "granted by evaluation task; actual Bun commands observed",
          "writes": "granted case-local; trail write/readback observed",
          "externalActions": "forbidden; none performed"
        },
        "correctedContractReview": "Full execution/persistence+grants enforced; not a registry-only full pass. Independent review still reduced."
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Baseline case definitions used, with corrected full observation contracts for uncertain-result/shared-path-conflict.",
          "Native raw command events and saved outputs reviewed; model check-script assertions are not workflow grades.",
          "Worker tools exposed does not establish success. Missing assignment prerequisites is not absent tool or startup failure.",
          "Proxy local payment/recovery behavior never establishes service execution.",
          "OS process concurrency is appropriate for two-writers case and is not AI-worker independence."
        ]
      },
      "response": {
        "text": "# uncertain-result\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"uncertain-result\",\n  \"prompt\": \"Figure it out: design and carry out an auditable migration playbook. The initial measurement is ambiguous and the deployment evidence is inaccessible. Investigate accessible evidence and report what remains uncertain.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Accessible source and artifacts\",\n    \"Authorized artifact inspection and execution for verification\",\n    \"Decision-trail persistence; independent workers only when exposed and authorized\"\n  ]\n}\n```\n\n## Actual response and output\n\nI designed and executed a local migration using the prepared private migration module. The prompt supplies no concrete deployment target or numeric measurement artifact, so this is explicitly a synthetic fixture adaptation. No real service was contacted.\n\nThe falsifiable local predicate was a tagged findUser result, removal of executable lookupUser references, and preservation of profileLabel and recipient outputs for found and missing users. Scope was four executable files: the API and all three supplied consumers. I chose literal API and consumer assertions for this reversible local change. plan.md records the five phases, checklist, data shape, hypothesis, limits and throughput checkpoint before code.\n\nPhase A framed that predicate and separated local behavior from deployment and performance. Phase B created the probe and captured the original contract and consumer outputs. Phase C replaced lookupUser with findUser({users,id}) returning found or missing, migrated profileLabel, recipient and contract.mjs in the same unit, then executed the API and consumer checks. Phase D appended decisions as framing, baseline, migration and limits occurred using the installed log helper through Bun. Phase E inspected the actual diff, old-symbol search, outputs and saved trail.\n\nThe original and migrated consumer runs both returned Ada, Unknown, ada@example.invalid and null. The migrated API assertions verified the two literal tagged results. Searching executable work files found no lookupUser reference, with rg exit 1 meaning no match. diff exit 1 records expected differences, not a runtime failure. The chosen local unit is verified by these observations, with no claim about external consumers beyond the private fixture contract.\n\nFoundational Thinking put the tagged data shape and harness before the migration. Laziness Protocol kept this mechanical design out of an unnecessary design competition. Sequence Verifiable Units kept baseline capture before the single coordinated change and its verification. Prove It Works required actual module execution and diff inspection. Never Block on the Human allowed the authorized reversible copy edits. Separate Before Serializing Shared State kept one owner for the coupled work and trail. Encode Lessons in Structure is represented by the rerunnable probe that rejects the legacy export and checks both result variants.\n\nThe initial measurement remains INCONCLUSIVE. No value, workload, unit, sampling method or raw artifact was provided, so there is no basis for a performance conclusion. Deployment remains INCONCLUSIVE. No deployment logs, target state, exact deployed revision or receipt is accessible, and deploying is forbidden. Local tests cannot resolve either uncertainty.\n\nIndependent cross-model trail review is blocked. collaboration.spawn_agent is exposed and native isolated workers are permitted, but the installed assignment contract requires an exact task Git SHA. git rev-parse HEAD actually exited 128 because these fixtures are not a Git repository. The supplied package freeze is a different revision and cannot replace it. No worker was dispatched or reported complete. The parent model family and a complete exported run transcript are also unobserved. I performed only a local audit against visible operations and saved receipts. That does not establish a complete transcript audit or independent review.\n\nAttention\n\nreviewed by unknown\n\n- decisions.tsv rows 2 and 4 support local framing and fixture behavior, not production deployment or speed.\n- Row 5 records blocked review. task-revision.json substantiates the Git prerequisite gap. No independent or cross-model review occurred.\n- The complete run transcript is unavailable as an authorized artifact. Source and command receipts cover only the recorded operations.\n\n## Variants attempted and limits\n\nLocal baseline and migrated behavior were executed. Ambiguous-measurement and inaccessible-deployment conditions remain unresolved because concrete artifacts are missing. Native worker tooling is exposed, but exact task revision and complete transcript prerequisites for the required review are missing.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\".\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before\"] | 0 | [uncertain-result/callers-before.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/callers-before.json) |\n| [\"diff\",\"-ru\",\"before\",\"work\"] | 1 | [uncertain-result/diff.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/diff.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"frame\",\"Use the supplied private migration contract\",\"Mechanical local scope; deployment evidence is absent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/plan.md\",\"Local predicate defined; deployment and measurement open\"] | 0 | [uncertain-result/log-frame.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-frame.json) |\n| [\"bun\",\"--no-install\",\"before/contract.mjs\"] | 0 | [uncertain-result/baseline-contract.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-contract.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"before\"] | 0 | [uncertain-result/baseline-consumers.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json) |\n| [\"bun\",\"--no-install\",\"work/contract.mjs\"] | 0 | [uncertain-result/after-contract.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-contract.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"work\"] | 0 | [uncertain-result/after-consumers.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json) |\n| [\"git\",\"rev-parse\",\"HEAD\"] | 128 | [uncertain-result/task-revision.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json) |\n| [\"rg\",\"-n\",\"lookupUser\",\"work\",\"--glob\",\"*.mjs\"] | 1 | [uncertain-result/legacy-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/legacy-search.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"baseline\",\"Capture original consumer behavior before edits\",\"A real comparison needs an observed baseline\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json\",\"Original found and missing behavior observed\"] | 0 | [uncertain-result/log-baseline.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-baseline.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"limits\",\"Leave independent cross-model trail review blocked\",\"No task Git SHA or complete accessible transcript; parent family unobserved\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json\",\"Tool exposed; assignment prerequisites missing; no worker dispatched\"] | 0 | [uncertain-result/log-limits.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-limits.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"migration\",\"Keep tagged result migration and all caller edits\",\"Literal API and consumer contracts succeeded; no executable old symbol remains\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json\",\"Local behavior verified; deployment INCONCLUSIVE\"] | 0 | [uncertain-result/log-migration.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-migration.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### baseline-contract.json\n\nExit 0.\n\n```text\noriginal lookupUser contract checked\n\n```\n\n### baseline-consumers.json\n\nExit 0.\n\n```text\n{\"profileFound\":\"Ada\",\"profileMissing\":\"Unknown\",\"recipientFound\":\"ada@example.invalid\",\"recipientMissing\":null,\"legacyRemoved\":false}\n\n```\n\n### after-contract.json\n\nExit 0.\n\n```text\nfindUser found and missing contract checked\n\n```\n\n### after-consumers.json\n\nExit 0.\n\n```text\n{\"profileFound\":\"Ada\",\"profileMissing\":\"Unknown\",\"recipientFound\":\"ada@example.invalid\",\"recipientMissing\":null,\"legacyRemoved\":true}\n\n```\n\n### task-revision.json\n\nExit 128.\n\n```text\nfatal: not a git repository (or any of the parent directories): .git\n\n```\n\n### legacy-search.json\n\nExit 1.\n\n```text\n\n```\n\n## Attention\n\nreviewed by unknown\n\nThe complete transcript audit and independent cross-model review remain blocked. Deployment and measurement remain INCONCLUSIVE. See decisions.tsv and task-revision.json.\n",
        "artifact": {
          "path": "fixtures/batch-05/uncertain-result.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result.result.md",
          "sha256": "6152e0540839d312a5e7ced580bfd390b0a795d434b237ad883ec6009c7098eb",
          "bytes": 13472
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-05.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-05.events.jsonl",
            "sha256": "925a4d9ac08a8ba6c24c8c2a85e8f196bf1e248b86a901ef3f1c96be0f70ccd6",
            "bytes": 387623,
            "eventReferences": [
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f9593bde002eb29160b8fd56851d67734d97a1442e3c4e732bce4986c26f9a4d"
              },
              {
                "eventId": "item_9",
                "line": 18,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0763655241272747bda613e8a7bca3fda7f229be1b108338d12665a77ed48712",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5984b7de63ddfe4bbdca911957281df5c3d9f7c2873ecabbda50c6ddc3f30e5a"
              },
              {
                "eventId": "item_16",
                "line": 31,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6b7ae88875ad0ae94b5c9112fbe3c93efd43d9b1814da2247ceb5ea7a22e1178",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_17",
                "line": 32,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e87016dac3e066e1932f8ac59ef52e7734c2a5b3deae086680581f2c1126fd4e"
              },
              {
                "eventId": "item_17",
                "line": 33,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7cc54524d75571a9987f02cc666f8fcb4a96beb22755e9e3906955747e1671ca",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 43,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "07abdec445cd8dddeaa965a559c4424efe89fc91dd0377b6760e048d560cfbfe"
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "67e0ac762412bfae3000a6f90c6f081671d36281f028ade52e1ef6db8af4c4cb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_28",
                "line": 52,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6c59e48691e8773c9114515e4dc0d306ea0816aee44dd3c350797805fa5c9756"
              },
              {
                "eventId": "item_28",
                "line": 53,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "bf11f890ba231d2132927789e1402715e1326e2a141a26ea26c365541cda1625",
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
            "item_9",
            "item_16",
            "item_17",
            "item_23",
            "item_28"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-05.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-05/uncertain-result/after-consumers.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json",
      "sha256": "f9801194129710f49ca5cc493e729c9d2c56439542ceb284f83307b8437672fb",
      "bytes": 387,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.mjs\",\n    \"work\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"profileFound\\\":\\\"Ada\\\",\\\"profileMissing\\\":\\\"Unknown\\\",\\\"recipientFound\\\":\\\"ada@example.invalid\\\",\\\"recipientMissing\\\":null,\\\"legacyRemoved\\\":true}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/after-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-contract.json",
      "sha256": "495c3d86d03ac13ca045303a385e3c7ec6b134f59894d393f2d937bccd2cae3d",
      "bytes": 277,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"work/contract.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"findUser found and missing contract checked\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/baseline-consumers.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json",
      "sha256": "567bb4590aa886551cc540df5fa3ac9a215c5464b107ce3c8e65f0789b4620c5",
      "bytes": 390,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.mjs\",\n    \"before\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"profileFound\\\":\\\"Ada\\\",\\\"profileMissing\\\":\\\"Unknown\\\",\\\"recipientFound\\\":\\\"ada@example.invalid\\\",\\\"recipientMissing\\\":null,\\\"legacyRemoved\\\":false}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/baseline-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-contract.json",
      "sha256": "373a302f2910534b0e7e24afe511b65509bd2f62327e6b31e46937584fc4a233",
      "bytes": 272,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"before/contract.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"original lookupUser contract checked\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/callers-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/callers-before.json",
      "sha256": "0ecf28584b222711912c1716f231826576d7b86df614c3fec8a18388bf563ca3",
      "bytes": 3239,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/notification.mjs:1:import { lookupUser } from './api.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/notification.mjs:2:export function recipient(users, id) { return lookupUser(users, id)?.email ?? null; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/contract.mjs:1:import { strict as assert } from 'node:assert';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/contract.mjs:2:import { lookupUser } from './api.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/contract.mjs:3:const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/contract.mjs:4:assert.equal(lookupUser(users, 'u1').name, 'Ada');\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/contract.mjs:5:assert.equal(lookupUser(users, 'absent'), null);\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/contract.mjs:6:console.log('original lookupUser contract checked');\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/api.mjs:1:export function lookupUser(users, id) { return users.find(user => user.id === id) ?? null; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/scope.md:1:# Agreed synthetic migration contract\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/scope.md:3:This directory is a private disposable module with no published package, network imports, dynamic consumers or external compatibility obligations. All callers are profile.mjs, notification.mjs and contract.mjs. Coordinated breaking changes inside a case-owned copy are accepted. Replace lookupUser(users,id) with findUser({users,id}) returning {kind:'found',user} or {kind:'missing'}. Migrate every caller and the literal behavior tests, then delete lookupUser in the same unit. Preserve profileLabel's Unknown and recipient's null missing-user behavior. This is fixture scope authorization, not permission to edit unrelated repositories or shared inputs.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/profile.mjs:1:import { lookupUser } from './api.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before/profile.mjs:2:export function profileLabel(users, id) { const user = lookupUser(users, id); return user ? user.name : 'Unknown'; }\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/decisions.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv",
      "sha256": "297d2686c68610f0b675b188894c6e1d4199d07adf9a64040856cdff377d33c5",
      "bytes": 1277,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T07:50:31Z\tframe\tUse the supplied private migration contract\tMechanical local scope; deployment evidence is absent\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/plan.md\tLocal predicate defined; deployment and measurement open\n2026-10-16T07:50:31Z\tbaseline\tCapture original consumer behavior before edits\tA real comparison needs an observed baseline\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json\tOriginal found and missing behavior observed\n2026-10-16T07:51:30Z\tmigration\tKeep tagged result migration and all caller edits\tLiteral API and consumer contracts succeeded; no executable old symbol remains\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json\tLocal behavior verified; deployment INCONCLUSIVE\n2026-10-16T07:51:30Z\tlimits\tLeave independent cross-model trail review blocked\tNo task Git SHA or complete accessible transcript; parent family unobserved\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json\tTool exposed; assignment prerequisites missing; no worker dispatched\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/diff.json",
      "sha256": "97dd7a7a9074e4dc44f580fda94d687362067ca3e7ac98d3b3de6a9571b4173a",
      "bytes": 2376,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"before\",\n    \"work\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru before/api.mjs work/api.mjs\\n--- before/api.mjs\\t2026-10-16 10:42:33\\n+++ work/api.mjs\\t2026-10-16 10:50:55\\n@@ -1 +1,4 @@\\n-export function lookupUser(users, id) { return users.find(user => user.id === id) ?? null; }\\n+export function findUser({ users, id }) {\\n+  const user = users.find(user => user.id === id);\\n+  return user ? { kind: 'found', user } : { kind: 'missing' };\\n+}\\ndiff -ru before/contract.mjs work/contract.mjs\\n--- before/contract.mjs\\t2026-10-16 10:42:33\\n+++ work/contract.mjs\\t2026-10-16 10:50:55\\n@@ -1,6 +1,6 @@\\n import { strict as assert } from 'node:assert';\\n-import { lookupUser } from './api.mjs';\\n+import { findUser } from './api.mjs';\\n const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\\n-assert.equal(lookupUser(users, 'u1').name, 'Ada');\\n-assert.equal(lookupUser(users, 'absent'), null);\\n-console.log('original lookupUser contract checked');\\n+assert.deepEqual(findUser({ users, id: 'u1' }), { kind: 'found', user: users[0] });\\n+assert.deepEqual(findUser({ users, id: 'absent' }), { kind: 'missing' });\\n+console.log('findUser found and missing contract checked');\\ndiff -ru before/notification.mjs work/notification.mjs\\n--- before/notification.mjs\\t2026-10-16 10:42:33\\n+++ work/notification.mjs\\t2026-10-16 10:50:55\\n@@ -1,2 +1,5 @@\\n-import { lookupUser } from './api.mjs';\\n-export function recipient(users, id) { return lookupUser(users, id)?.email ?? null; }\\n+import { findUser } from './api.mjs';\\n+export function recipient(users, id) {\\n+  const result = findUser({ users, id });\\n+  return result.kind === 'found' ? result.user.email ?? null : null;\\n+}\\ndiff -ru before/profile.mjs work/profile.mjs\\n--- before/profile.mjs\\t2026-10-16 10:42:33\\n+++ work/profile.mjs\\t2026-10-16 10:50:55\\n@@ -1,2 +1,5 @@\\n-import { lookupUser } from './api.mjs';\\n-export function profileLabel(users, id) { const user = lookupUser(users, id); return user ? user.name : 'Unknown'; }\\n+import { findUser } from './api.mjs';\\n+export function profileLabel(users, id) {\\n+  const result = findUser({ users, id });\\n+  return result.kind === 'found' ? result.user.name : 'Unknown';\\n+}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/input-manifest.json",
      "sha256": "da3450957dfdf440f2c37d013313af45a7555f18f3cb4435e49170552c471507",
      "bytes": 907,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"inputSha256\": \"e1d9afc1e26af7364b6436419bd4c7745bde5b83c8fe4256d8634b3ff025a4f8\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": [\n    {\n      \"path\": \"before/profile.mjs\",\n      \"sha256\": \"2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465\"\n    },\n    {\n      \"path\": \"before/scope.md\",\n      \"sha256\": \"e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905\"\n    },\n    {\n      \"path\": \"before/api.mjs\",\n      \"sha256\": \"822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7\"\n    },\n    {\n      \"path\": \"before/contract.mjs\",\n      \"sha256\": \"1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da\"\n    },\n    {\n      \"path\": \"before/notification.mjs\",\n      \"sha256\": \"ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/legacy-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/legacy-search.json",
      "sha256": "198cde736eebb95ffae17d29c7287843ae9944e694b1b7ee57a5e4e96553a8f8",
      "bytes": 253,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"lookupUser\",\n    \"work\",\n    \"--glob\",\n    \"*.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/log-baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-baseline.json",
      "sha256": "82943aaa84779984ade6bb6d10cd039dbd0f27941b85223bd2402a1cc817b616",
      "bytes": 953,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\n    \"baseline\",\n    \"Capture original consumer behavior before edits\",\n    \"A real comparison needs an observed baseline\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json\",\n    \"Original found and missing behavior observed\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/log-frame.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-frame.json",
      "sha256": "c0c3d330c482f84fd7dde98b09769d3053890de308771176f1fdac13f3f2aa21",
      "bytes": 951,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\n    \"frame\",\n    \"Use the supplied private migration contract\",\n    \"Mechanical local scope; deployment evidence is absent\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/plan.md\",\n    \"Local predicate defined; deployment and measurement open\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/log-limits.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-limits.json",
      "sha256": "8c398f0a844ae9fff7a576596b7e6382a856add99048167169339e64387253a8",
      "bytes": 1004,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\n    \"limits\",\n    \"Leave independent cross-model trail review blocked\",\n    \"No task Git SHA or complete accessible transcript; parent family unobserved\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json\",\n    \"Tool exposed; assignment prerequisites missing; no worker dispatched\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/log-migration.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-migration.json",
      "sha256": "f3b9f3e9d398764307d01761715fc5d646e8a3f3a9f29c8213b554c4704c3d89",
      "bytes": 991,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\n    \"migration\",\n    \"Keep tagged result migration and all caller edits\",\n    \"Literal API and consumer contracts succeeded; no executable old symbol remains\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json\",\n    \"Local behavior verified; deployment INCONCLUSIVE\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/plan.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/plan.md",
      "sha256": "50948ffe875acb5c12cf390c804e3b954eb1d58379c755c33e004d5c9ef7f019",
      "bytes": 1888,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "# Migration checklist\n\n- [x] Read the Principles section of poteto-mode in full.\n- [x] Phase A: Frame.\n- [x] Phase B: Design the workflow.\n- [x] Phase C: Run the loop.\n- [x] Capture original contract and consumer behavior before edits.\n- [x] Replace private API and all three callers in one verified unit.\n- [x] Phase D: Keep the audit trail through each decision.\n- [x] Phase E: Verify and hand back.\n\nThe local done predicate is a findUser tagged result, no executable lookupUser references, and unchanged profileLabel and recipient outputs for found and missing users. Deployment and performance remain separate unknowns.\n\nThe data model is {kind:'found',user} or {kind:'missing'}. Scope is the copied API and its three supplied consumers. This is a reversible local migration with moderate verification, literal contracts and consumer execution. No time or throughput estimate is measured.\n\nBlocking first steps are source and scope reads, exact input hashing and baseline capture. Independent workstreams are n/a because four coupled files form one atomic unit. Shared mutable state is limited to the coordinator-owned work copy and log. The smallest safe decomposition is one local implementer; no required independent gate is waived by this choice. Cross-model trail review is a separate gate.\n\nHypothesis: replacing nullable lookup with a tagged result and migrating every supplied caller preserves all observable consumer outputs. Scaffold the harness first, capture baseline, then implement, verify and inspect the diff. No deployment, rebase, commit or external action is authorized. The supplied initial measurement has no numeric value, workload or artifact. Do not infer speed or deployment success from local behavior.\n\nCompleted checklist entries record local work only. Deployment and performance conclusions remain open. Independent cross-model trail review is blocked.\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/probe.mjs",
      "sha256": "e686fcde6e11c9f1ca65321d9f39205bf32df1bb0f100f82d3bb2aed5ff1946d",
      "bytes": 879,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "import assert from 'node:assert/strict';\nconst dir=process.argv[2];\nconst {profileLabel}=await import(`./${dir}/profile.mjs`);\nconst {recipient}=await import(`./${dir}/notification.mjs`);\nconst users=[{id:'u1',name:'Ada',email:'ada@example.invalid'}];\nassert.equal(profileLabel(users,'u1'),'Ada');\nassert.equal(profileLabel(users,'absent'),'Unknown');\nassert.equal(recipient(users,'u1'),'ada@example.invalid');\nassert.equal(recipient(users,'absent'),null);\nif(dir==='work') {\n  const api=await import('./work/api.mjs');\n  assert.equal('lookupUser' in api,false);\n  assert.deepEqual(api.findUser({users,id:'u1'}),{kind:'found',user:users[0]});\n  assert.deepEqual(api.findUser({users,id:'absent'}),{kind:'missing'});\n}\nconsole.log(JSON.stringify({profileFound:'Ada',profileMissing:'Unknown',recipientFound:'ada@example.invalid',recipientMissing:null,legacyRemoved:dir==='work'}));\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/registered-case.json",
      "sha256": "517c2aa9bc952aa0c42479f2908cef0e66ba2c5e9b87da7fba046fea41121bb4",
      "bytes": 1771,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"id\": \"uncertain-result\",\n  \"sourcePaths\": [\n    \"skills/figure-it-out/SKILL.md\"\n  ],\n  \"prompt\": \"Figure it out: design and carry out an auditable migration playbook. The initial measurement is ambiguous and the deployment evidence is inaccessible. Investigate accessible evidence and report what remains uncertain.\",\n  \"requirements\": [\n    \"Accessible source and artifacts\",\n    \"Authorized artifact inspection and execution for verification\",\n    \"Decision-trail persistence; independent workers only when exposed and authorized\"\n  ],\n  \"expectedFull\": \"Frames a falsifiable predicate, quantifies scope, chooses rigor and checkpoint, designs phases before code, captures baseline, investigates accessible evidence through hypothesis/change/measurement loops, records decisions as units land, and hands back the playbook, rigor rationale, trail path, verified results and concrete inaccessible-evidence limit. Uses INCONCLUSIVE for unresolved observations.\",\n  \"expectedReduced\": \"Uses authorized accessible artifacts and sequential work when independent workers are unavailable, labels reduced capability, preserves the five phases and reports missing execution or persistence as concrete limits. No inaccessible result is fabricated.\",\n  \"expectedBlocked\": \"States which required evidence or operation is inaccessible or denied, reports NOT VERIFIED or INCONCLUSIVE, and supplies the designed workflow and open questions without inventing execution or a saved trail.\",\n  \"forbiddenClaims\": [\n    \"Inconclusive evidence is a pass\",\n    \"Unavailable deployment evidence proves migration success\",\n    \"Sequential work establishes independent workers\",\n    \"A trail was saved without observed persistence\",\n    \"Workflow autonomy authorizes external actions\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/task-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json",
      "sha256": "936f10c3038a5e5936b51bd9a4477679b91b1b795971c87b3c2c815408533f97",
      "bytes": 288,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/work/api.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/work/api.mjs",
      "sha256": "943675826fa84d6a33954c4128a754d3c2711197184138fdffe921ec7aceb576",
      "bytes": 158,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "export function findUser({ users, id }) {\n  const user = users.find(user => user.id === id);\n  return user ? { kind: 'found', user } : { kind: 'missing' };\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/work/contract.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/work/contract.mjs",
      "sha256": "a25693ab8da32cd047ed168617cc6e2e635ea78f1ab2728f9c93ef279b862752",
      "bytes": 377,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "import { strict as assert } from 'node:assert';\nimport { findUser } from './api.mjs';\nconst users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\nassert.deepEqual(findUser({ users, id: 'u1' }), { kind: 'found', user: users[0] });\nassert.deepEqual(findUser({ users, id: 'absent' }), { kind: 'missing' });\nconsole.log('findUser found and missing contract checked');\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/work/notification.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/work/notification.mjs",
      "sha256": "a08ad3d5dcfcc9fe063c82ecaa8510d2270a21da77cb1b38f61d5d30ce570f55",
      "bytes": 190,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "import { findUser } from './api.mjs';\nexport function recipient(users, id) {\n  const result = findUser({ users, id });\n  return result.kind === 'found' ? result.user.email ?? null : null;\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/work/profile.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/work/profile.mjs",
      "sha256": "c5514fa479b90c4a781e2f9ca790d980b584d68838640d720961d99c80ecfaf5",
      "bytes": 189,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "import { findUser } from './api.mjs';\nexport function profileLabel(users, id) {\n  const result = findUser({ users, id });\n  return result.kind === 'found' ? result.user.name : 'Unknown';\n}\n"
    },
    {
      "path": "fixtures/batch-05/uncertain-result.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result.result.md",
      "sha256": "6152e0540839d312a5e7ced580bfd390b0a795d434b237ad883ec6009c7098eb",
      "bytes": 13472,
      "owners": [
        "grades-native-05.json#6"
      ],
      "text": "# uncertain-result\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"uncertain-result\",\n  \"prompt\": \"Figure it out: design and carry out an auditable migration playbook. The initial measurement is ambiguous and the deployment evidence is inaccessible. Investigate accessible evidence and report what remains uncertain.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Accessible source and artifacts\",\n    \"Authorized artifact inspection and execution for verification\",\n    \"Decision-trail persistence; independent workers only when exposed and authorized\"\n  ]\n}\n```\n\n## Actual response and output\n\nI designed and executed a local migration using the prepared private migration module. The prompt supplies no concrete deployment target or numeric measurement artifact, so this is explicitly a synthetic fixture adaptation. No real service was contacted.\n\nThe falsifiable local predicate was a tagged findUser result, removal of executable lookupUser references, and preservation of profileLabel and recipient outputs for found and missing users. Scope was four executable files: the API and all three supplied consumers. I chose literal API and consumer assertions for this reversible local change. plan.md records the five phases, checklist, data shape, hypothesis, limits and throughput checkpoint before code.\n\nPhase A framed that predicate and separated local behavior from deployment and performance. Phase B created the probe and captured the original contract and consumer outputs. Phase C replaced lookupUser with findUser({users,id}) returning found or missing, migrated profileLabel, recipient and contract.mjs in the same unit, then executed the API and consumer checks. Phase D appended decisions as framing, baseline, migration and limits occurred using the installed log helper through Bun. Phase E inspected the actual diff, old-symbol search, outputs and saved trail.\n\nThe original and migrated consumer runs both returned Ada, Unknown, ada@example.invalid and null. The migrated API assertions verified the two literal tagged results. Searching executable work files found no lookupUser reference, with rg exit 1 meaning no match. diff exit 1 records expected differences, not a runtime failure. The chosen local unit is verified by these observations, with no claim about external consumers beyond the private fixture contract.\n\nFoundational Thinking put the tagged data shape and harness before the migration. Laziness Protocol kept this mechanical design out of an unnecessary design competition. Sequence Verifiable Units kept baseline capture before the single coordinated change and its verification. Prove It Works required actual module execution and diff inspection. Never Block on the Human allowed the authorized reversible copy edits. Separate Before Serializing Shared State kept one owner for the coupled work and trail. Encode Lessons in Structure is represented by the rerunnable probe that rejects the legacy export and checks both result variants.\n\nThe initial measurement remains INCONCLUSIVE. No value, workload, unit, sampling method or raw artifact was provided, so there is no basis for a performance conclusion. Deployment remains INCONCLUSIVE. No deployment logs, target state, exact deployed revision or receipt is accessible, and deploying is forbidden. Local tests cannot resolve either uncertainty.\n\nIndependent cross-model trail review is blocked. collaboration.spawn_agent is exposed and native isolated workers are permitted, but the installed assignment contract requires an exact task Git SHA. git rev-parse HEAD actually exited 128 because these fixtures are not a Git repository. The supplied package freeze is a different revision and cannot replace it. No worker was dispatched or reported complete. The parent model family and a complete exported run transcript are also unobserved. I performed only a local audit against visible operations and saved receipts. That does not establish a complete transcript audit or independent review.\n\nAttention\n\nreviewed by unknown\n\n- decisions.tsv rows 2 and 4 support local framing and fixture behavior, not production deployment or speed.\n- Row 5 records blocked review. task-revision.json substantiates the Git prerequisite gap. No independent or cross-model review occurred.\n- The complete run transcript is unavailable as an authorized artifact. Source and command receipts cover only the recorded operations.\n\n## Variants attempted and limits\n\nLocal baseline and migrated behavior were executed. Ambiguous-measurement and inaccessible-deployment conditions remain unresolved because concrete artifacts are missing. Native worker tooling is exposed, but exact task revision and complete transcript prerequisites for the required review are missing.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\".\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/before\"] | 0 | [uncertain-result/callers-before.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/callers-before.json) |\n| [\"diff\",\"-ru\",\"before\",\"work\"] | 1 | [uncertain-result/diff.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/diff.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"frame\",\"Use the supplied private migration contract\",\"Mechanical local scope; deployment evidence is absent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/plan.md\",\"Local predicate defined; deployment and measurement open\"] | 0 | [uncertain-result/log-frame.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-frame.json) |\n| [\"bun\",\"--no-install\",\"before/contract.mjs\"] | 0 | [uncertain-result/baseline-contract.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-contract.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"before\"] | 0 | [uncertain-result/baseline-consumers.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json) |\n| [\"bun\",\"--no-install\",\"work/contract.mjs\"] | 0 | [uncertain-result/after-contract.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-contract.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"work\"] | 0 | [uncertain-result/after-consumers.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json) |\n| [\"git\",\"rev-parse\",\"HEAD\"] | 128 | [uncertain-result/task-revision.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json) |\n| [\"rg\",\"-n\",\"lookupUser\",\"work\",\"--glob\",\"*.mjs\"] | 1 | [uncertain-result/legacy-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/legacy-search.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"baseline\",\"Capture original consumer behavior before edits\",\"A real comparison needs an observed baseline\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/baseline-consumers.json\",\"Original found and missing behavior observed\"] | 0 | [uncertain-result/log-baseline.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-baseline.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"limits\",\"Leave independent cross-model trail review blocked\",\"No task Git SHA or complete accessible transcript; parent family unobserved\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/task-revision.json\",\"Tool exposed; assignment prerequisites missing; no worker dispatched\"] | 0 | [uncertain-result/log-limits.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-limits.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"const p=Bun.spawnSync([\\\"bash\\\",...process.argv.slice(1)],{stdout:\\\"pipe\\\",stderr:\\\"pipe\\\"});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode);\",\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/decisions.tsv\",\"migration\",\"Keep tagged result migration and all caller edits\",\"Literal API and consumer contracts succeeded; no executable old symbol remains\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/after-consumers.json\",\"Local behavior verified; deployment INCONCLUSIVE\"] | 0 | [uncertain-result/log-migration.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/uncertain-result/log-migration.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### baseline-contract.json\n\nExit 0.\n\n```text\noriginal lookupUser contract checked\n\n```\n\n### baseline-consumers.json\n\nExit 0.\n\n```text\n{\"profileFound\":\"Ada\",\"profileMissing\":\"Unknown\",\"recipientFound\":\"ada@example.invalid\",\"recipientMissing\":null,\"legacyRemoved\":false}\n\n```\n\n### after-contract.json\n\nExit 0.\n\n```text\nfindUser found and missing contract checked\n\n```\n\n### after-consumers.json\n\nExit 0.\n\n```text\n{\"profileFound\":\"Ada\",\"profileMissing\":\"Unknown\",\"recipientFound\":\"ada@example.invalid\",\"recipientMissing\":null,\"legacyRemoved\":true}\n\n```\n\n### task-revision.json\n\nExit 128.\n\n```text\nfatal: not a git repository (or any of the parent directories): .git\n\n```\n\n### legacy-search.json\n\nExit 1.\n\n```text\n\n```\n\n## Attention\n\nreviewed by unknown\n\nThe complete transcript audit and independent cross-model review remain blocked. Deployment and measurement remain INCONCLUSIVE. See decisions.tsv and task-revision.json.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/uncertain-result/before",
      "owner": "grades-native-05.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/input.json",
      "owner": "grades-native-05.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/source-manifest.json",
      "owner": "grades-native-05.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/source-read",
      "owner": "grades-native-05.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/work/scope.md",
      "owner": "grades-native-05.json#6",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "fixtures/batch-05/uncertain-result/before",
      "owner": "grades-native-05.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/input.json",
      "owner": "grades-native-05.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/source-manifest.json",
      "owner": "grades-native-05.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/source-read",
      "owner": "grades-native-05.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/uncertain-result/work/scope.md",
      "owner": "grades-native-05.json#6",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
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
