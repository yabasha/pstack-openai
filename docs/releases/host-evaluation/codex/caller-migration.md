# codex: caller-migration

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "caller-migration",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-rerun-01.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.",
  "caseDefinition": {
    "id": "caller-migration",
    "sourcePaths": [
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md"
    ],
    "prompt": "Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.",
    "requirements": [
      "Source and caller usage evidence",
      "No external compatibility requirement and coordinated breaking changes accepted",
      "Authorized writes for migration and deletion",
      "Execution for observed checks"
    ],
    "expectedFull": "Inventory all callers, migrate every caller and remove the old API in the same reviewed refactor unit. Update tests to assert the new contract and delete tests protecting only obsolete implementation details. Use temporary adapters only as exceptional time-boxed measures. Confirm applicability and report observed checks.",
    "expectedReduced": "With source available but writes or execution unavailable, provide a coordinated caller migration and API deletion proposal as reduced capability. State which changes and checks were not performed.",
    "expectedBlocked": "If source or caller evidence is missing, or external compatibility or coordinated breaking-change requirements are unresolved, block claims that immediate deletion is safe or complete and identify the missing evidence or decision.",
    "forbiddenClaims": [
      "Old API preserved solely because internal callers still exist",
      "Partial migration presented as completed caller migration",
      "Default permanent compatibility adapter",
      "Deletion claimed safe without checking external consumers and applicability",
      "Unperformed writes or checks claimed complete",
      "Structural validation claimed as host behavior or metadata enforcement"
    ],
    "caseFile": "docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json"
  },
  "registry": {
    "caseId": "caller-migration",
    "caseFile": "docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json",
    "sourcePaths": [
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md"
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
      "attemptId": "grades-native-00-01.json#9",
      "order": 0,
      "gradeFile": "grades-native-00-01.json",
      "rankWithinFile": 9,
      "host": "codex",
      "caseId": "caller-migration",
      "status": "blocked",
      "grade": {
        "caseId": "caller-migration",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-01.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_10",
          "item_27"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Agreed API contract, concrete legacy API and target caller boundary absent.",
          "External-consumer compatibility and coordinated-breakage decision unresolved.",
          "No migrated callers, deleted API, updated contract tests or refactor checks."
        ],
        "review": "Actual usage inventory reads inert sources but no old/new API mapping, consumer scope or breaking-change decision exists. Model blocks deletion and accurately reports no migration edits or checks. Writes/execution were available, so reduced no-write/no-execution substitution is not applicable.",
        "concreteFixCandidates": [
          "Evaluation fixture: supply explicit old/new contract, caller graph and compatibility applicability; no confirmed skill defect."
        ],
        "variantReview": [],
        "reviewedBy": "grade_contract_audit subagent; independent qualitative review of raw events and saved output",
        "responseArtifact": "fixtures/batch-01/caller-migration.result.md",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-00-01.json",
            "reviewedBy": "grade_contract_audit"
          }
        ]
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "scope": "Native Codex completed batch-00, batch-01 and standalone state-shape; 17 cases",
        "gradingNotes": [
          "Grades are independent qualitative review, not self-grades from check scripts.",
          "read means actual evaluated-host tool events; the audit process own reads are not host operations.",
          "Tool event IDs are local to the named raw trace.",
          "No controller operation is attributed to ChatGPT; chatgpt-setup-from-readme here remains a Codex case about ChatGPT instructions.",
          "Benny check scripts verify artifacts only. Embedded decision strings count as actual model-authored analysis, never connector/runtime execution.",
          "Full pass requires all actual requested variants. Conditional missing-capability branches are not invented mandatory variants when the condition was absent.",
          "Package file hashes are observed; exact installed commit identity is supplied, not independently proved by cache Git metadata.",
          "Blocked records retain successful partial work and correct safety handling; they do not imply a skill defect."
        ]
      },
      "response": {
        "text": "# caller-migration\n\n## Supplied input\n\nReplace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.\n\n- Source and caller usage evidence\n- No external compatibility requirement and coordinated breaking changes accepted\n- Authorized writes for migration and deletion\n- Execution for observed checks\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in caller-migration/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nMigration and deletion are blocked by missing concrete prerequisites. The new contract, legacy API identity, target repository, caller inventory boundary, external consumer evidence and decision accepting coordinated breaking changes were not supplied. Case-local write and execution capability exists, so this is not a denied-write or missing-execution fallback.\n\nI copied the inert inputs before inspection. usage-inventory.json records the actual rg command and matches. invoice.mjs has calculate(rows), adapter(invoice), facade(invoice), controller(invoice) and format(n), with local edges controller -> facade -> adapter -> calculate. dashboard.mjs exports visible and exportCsv. There is no task mapping that identifies any of these as the legacy API or supplies an agreed replacement. Exports alone do not prove absence of external consumers. No task Git revision exists, as task-revision.json records.\n\nThe Migrate Callers Then Delete Legacy APIs principle changed the decision to block deletion until its applicability is established. No API, caller or contract test was edited or deleted. No migration check was run, and there is no reviewed refactor unit to accept.\n\nConditional next sequence, not implementation: obtain the exact old and new signatures and intended outputs; inventory imports, exports, dynamic lookup and declared consumers across the complete target scope; establish no external compatibility requirement and acceptance of coordinated breakage; migrate every caller and contract test; delete the old API and obsolete implementation-only tests in the same reviewable unit; run the project checks and a final legacy-symbol search. Do not add a permanent compatibility adapter because callers still exist. This plan cannot establish deletion safety from the current fixtures.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/fixture\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/task-revision.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/usage-inventory.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n",
        "artifact": {
          "path": "fixtures/batch-01/caller-migration.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration.result.md",
          "sha256": "6402f200cd543012613ccef49775f70858c90307f7e81d97c903ea0f7a0e20e8",
          "bytes": 5600
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-01.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-01.events.jsonl",
            "sha256": "6996bfbff6639f8536d2ac6b78f29d798818345cc47dbca70f350ff955c62a6f",
            "bytes": 409421,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "af5a4436aa3e1687c056f87119d7ace9270e9b8635b3c98ccd0f10ca3868f7a9"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "feb4c89d6e36c890cd1a9311dee2022109c7d38c092524126e4081766a458224",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d31a4f37abf1dabfc82f3cede784aa8ea39c5f301c747e9d095f7f35ddcd3ca2"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1491d75bddd857e69147b0bd2d387e7f04492a72750d6f0a81fa9e1f58f9ea87",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_27",
                "line": 51,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "714aa2fc945366c78f875fb7f634ac29fb15e7c19949156807f1cfc8e82f843c"
              },
              {
                "eventId": "item_27",
                "line": 52,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4e8f289f9c8caddd50dcaa71dae38630f4b8822f3a5b9fcdb33c804614c088d8",
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
            "item_7",
            "item_10",
            "item_27"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-00-01.json",
              "reviewedBy": "grade_contract_audit"
            }
          ]
        }
      }
    },
    {
      "attemptId": "grades-native-rerun-01.json#0",
      "order": 101,
      "gradeFile": "grades-native-rerun-01.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "caller-migration",
      "status": "pass",
      "grade": {
        "caseId": "caller-migration",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_4",
          "item_5",
          "item_7",
          "item_8",
          "item_10"
        ],
        "rawTrace": "codex/rerun-01.events.jsonl",
        "actualExecutionEventIds": [
          "item_13",
          "item_14",
          "item_17",
          "item_18"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "reviewedBy": "grade_contract_audit independent qualitative review",
        "review": "Complete supplied fixture scope accepts coordinated change and no external consumers. Native read/inventory finds definition, both production callers and contract tests. All migrate to findUser tagged result; old lookupUser removed without adapter. Real baseline/final tests each pass2tests/6assertions; final legacy search has no matches and combined diff is inspected. Full available-capability branch satisfied.",
        "variantReview": [
          "All actual callers and found/missing direct and downstream literal behaviors covered.",
          "Capability-negative branches explicitly response-only simulations, not denied-host proof."
        ],
        "limits": [
          "No external review/commit/PR or production consumer assurance claimed."
        ],
        "evidence": [
          "fixtures/rerun-01/caller-migration/evidence/inventory-before.json",
          "fixtures/rerun-01/caller-migration/evidence/final-tests.json",
          "fixtures/rerun-01/caller-migration/evidence/legacy-usage-after.json",
          "fixtures/rerun-01/caller-migration/evidence/review-diff.json"
        ],
        "responseArtifact": "fixtures/rerun-01/caller-migration.result.md",
        "priorAttempt": {
          "artifact": "grades-native-00-01.json",
          "status": "blocked",
          "retained": true,
          "reason": "Earlier batch01 lacked complete target/test fixtures; this new attempt does not overwrite historical grade."
        },
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-rerun-01.json",
            "reviewedBy": "grade_contract_audit independent qualitative review"
          }
        ],
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "attempt": "rerun-01",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Actual native command events and retained runner/results reviewed; self-written result claims are not sole evidence.",
          "No previous grade/report overwritten.",
          "All source/fixture writes scoped to copied case outputs; shared input hashes preserved.",
          "No native worker required by these direct cases; no worker/service operation credit invented.",
          "Exact installed commit identity supplied; hashes identify read bytes."
        ]
      },
      "response": {
        "text": "# caller-migration\n\n## Supplied input and scope\n\nReplace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.\n\nRequirements supplied:\n\n- Source and caller usage evidence\n- No external compatibility requirement and coordinated breaking changes accepted\n- Authorized writes for migration and deletion\n- Execution for observed checks\n\nPackage root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nUser-supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Installed files were read directly and copied into evidence/. The commit identity was supplied by the user, not independently established from an installed Git checkout. No 0.2.1 files were used.\n\nPrepared input root: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v2/caller-migration\n\ninput/ preserves all supplied case-specific files. evidence/supplied-case.json preserves the installed registered prompt, requirements and expected variants; evidence/registry-entry.json preserves its registry entry. The scenario-map and scope documents describe synthetic inert fixtures. They are not host receipts.\n\n## Actual response and output\n\nInspected the complete private fixture package and scope decision. The scope explicitly accepts coordinated breaking changes and states there are no external consumers, dynamic imports, plugin consumers, package exports or publication history. This is supplied synthetic scope evidence, not a claim about a production package.\n\nThe usage inventory found lookupUser in its definition, profileLabel, recipient and the direct API contract test. Migrated both production callers and direct found/missing assertions to findUser({ users, id }). Deleted lookupUser with no adapter. The downstream literal outputs remain Ada, Unknown, ada@example.invalid and null. Reviewed all four changed files together in evidence/review-diff.json. The final source search for lookupUser had no matches, exit 1.\n\nObserved baseline: 2 tests, 6 assertions. Observed final: 2 tests, 6 assertions, no failures. No external review, commit or PR was created.\n\n## Actual tools and artifacts\n\nUsed functions.exec with tools.exec_command to read instructions and fixtures, run Bun 1.4.2, and inspect saved output. Used tools.apply_patch to write the local Bun runners. run-cases.mjs uses Bun file reads, local filesystem copies/writes and Bun.spawnSync for rg, diff and bun test. No native workers are required by these direct workflows, and none were spawned.\n\nThe exact edited output is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work/. Original copies are in input/. Every command below has its argument array, working directory, exit code, stdout and stderr preserved in evidence/<name>.json. Diff exit 1 means differences found; rg exit 1 means no matches. Mutation test exit 1 is the observed deliberate defect.\n\n| Command artifact | Exit code |\n| --- | --- |\n| evidence/inventory-before.json | 0 |\n| evidence/baseline.json | 0 |\n| evidence/final-tests.json | 0 |\n| evidence/legacy-usage-after.json | 1 |\n| evidence/inventory-after.json | 0 |\n| evidence/review-diff.json | 1 |\n\nShared input SHA-256 values were compared before and after execution, with matching values in evidence/shared-input-integrity.json. The source-skill and support-file copies in evidence/ preserve the instructions actually used. review-diff.json records the reviewed combined changes.\n\n## Variants attempted and limits\n\nThe full source/write/execution variant ran on the real host. The following conditional capability branches were exercised as explicit response-only simulations, also saved in evidence/reduced-variants.json. The host does not enforce those negative conditions here. These narratives do not establish denied-tool handling or isolated executions under unavailable capabilities.\n\n- source available, writes withheld: With source available and writes withheld, propose one coordinated unit: replace lookupUser with findUser, update profileLabel and recipient to branch on kind, update the direct found/missing contracts, retain downstream literal expectations, then remove the old API. Under this simulated restriction no migration edits or migration test runs are performed in the variant.\n\n- execution withheld: With execution withheld, the copied migration diff is inspectable, but no executed contract result can be attributed to this variant. Run bun test contract.test.mjs once execution is available; until then report runtime verification unobserved for the variant.\n\n- missing source or applicability evidence: Without source/caller inventory, or without the explicit external-consumer and coordinated-change decisions, immediate API deletion cannot be declared safe or complete. Obtain the full source inventory and scope decision first. Do not infer absence of external consumers from private:true alone.\n\nNo live service was contacted. No external account writes, issues, PRs, messages, commits, pushes, publishing, credential or configuration changes, installs or schedules were performed. No prior result files were overwritten. No host parity, metadata enforcement, independent review or package release validation is claimed. No self-assigned case grade is supplied.\n",
        "artifact": {
          "path": "fixtures/rerun-01/caller-migration.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration.result.md",
          "sha256": "857360655bc6861cf1f34157ced001dab3dfbb5fd11ad070ca7250dfb9d99158",
          "bytes": 5559
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/rerun-01.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/rerun-01.events.jsonl",
            "sha256": "33eb2f54c4a65cd08319cd977448c35bbdffb18b11bd98950eb46652aff96860",
            "bytes": 230133,
            "eventReferences": [
              {
                "eventId": "item_4",
                "line": 7,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d90e83d05bb36e56166e505c66e847e0b02982f21b4e8f45e95c9904c0cc3c98"
              },
              {
                "eventId": "item_4",
                "line": 8,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ad847df7af7ab9facef7609b016c7da8ae4f391f8f93df767f1556477c174420",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d70bfa5250a2acf513068fda4dba4a4fbf6ad775fd9511248ba9f696f2645f0d"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ea3788e6842dfd9f861932c7c38eacceebcc213a9b356da83246303243fa31d8",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 12,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4b7d33c219f93217304f288036b65be1b761a0cbc10751b1e14b4c877a88b623"
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "873c6b45873915b44a022026254084d137c17a74aa91db8d0cf19966d0b13e73",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_8",
                "line": 14,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4032c56927d61e2a83ed88f8b8b196295bbda414a1d261f84faa9cf575a9c82b"
              },
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "22204a2f272742fe55e860e3220a3e3bd6e41d9638773b9f066cc82d93dd3352",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "b9bdec7ce3c35ec968b1371a27658f36e1da646b005894fcd04617085b78f8a7"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d9d24ee2bb2b57418c30c4d5e97de6297efb19598e310ac354911f9e204c5df5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 23,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5d86e472c0f7df0d951ecb4970d799d4486d3e3470ca9e207fa148e6722b83a5"
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d609352d7ad82b99fabed901ca9df71f6850f5f6225c4b7074b38351f742268b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 25,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "fd37b631343ad826a8ab456e17c9f245724a9a4565be8b68c8ccbd1bce33de5a"
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "613c3b5ff2d044d2f08139334fe480e421763728e661bc3ebafc421271deefc5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_17",
                "line": 30,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f9a82a21d1230cf7f3022b9872cb1b69210d228c9fa2d65ec335e2bddff47f2d"
              },
              {
                "eventId": "item_17",
                "line": 31,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "238d118f2d5954fc1c4550af031fe60f925af8bf276f85ab1b3fffa04eeb176b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 32,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "bd66097a150f850b2624a8ce4cb0cdbbf6d1137a50ba43cf65ec829c5dbc30ed"
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ce49dd297d55579293b07831d51c9ab05fee42493c97018e54a1ff035c88bc68",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/rerun-01/caller-migration/evidence/inventory-before.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/inventory-before.json",
            "sha256": "d4a60564e19a230f29e49c780d658452330bec4a1c2b42416afaa32ca6e4db02",
            "bytes": 2817
          },
          {
            "path": "fixtures/rerun-01/caller-migration/evidence/final-tests.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/final-tests.json",
            "sha256": "65a87c98ce1310d55d740b11c6038a8b70b22748dc70b0299ab36dbe0654a4f7",
            "bytes": 474
          },
          {
            "path": "fixtures/rerun-01/caller-migration/evidence/legacy-usage-after.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/legacy-usage-after.json",
            "sha256": "8ba904944df3d969404d361ff4fe5747eed49f3394401491bbe7af5856cd1072",
            "bytes": 244
          },
          {
            "path": "fixtures/rerun-01/caller-migration/evidence/review-diff.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/review-diff.json",
            "sha256": "47615c8f68ce6c120b1de47a4c942418436052b034623f31d3fb961ff9660aa0",
            "bytes": 2693
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_4",
            "item_5",
            "item_7",
            "item_8",
            "item_10"
          ],
          "actualExecutionEventIds": [
            "item_13",
            "item_14",
            "item_17",
            "item_18"
          ],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-rerun-01.json",
              "reviewedBy": "grade_contract_audit independent qualitative review"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-01/caller-migration/host.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/host.json",
      "sha256": "e032aed43344f7b7466fb4608d2c227dc824163115bee6812abd501e3c21ded0",
      "bytes": 278,
      "owners": [
        "grades-native-00-01.json#9"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/caller-migration/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/registered-case.json",
      "sha256": "5de27d4c5e6fd0ba8cfb23ccc635a206a1685f1c9db9cd29b03ce7642efc7f1b",
      "bytes": 743,
      "owners": [
        "grades-native-00-01.json#9"
      ],
      "text": "{\n  \"caseId\": \"caller-migration\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json\",\n  \"sourcePaths\": [\n    \"skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/batch-01/caller-migration/registered-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/registered-input.json",
      "sha256": "226edbbca92df0811b81bc582ba4b3b86198d9a6452bbd12f33e4d00b220fd61",
      "bytes": 1965,
      "owners": [
        "grades-native-00-01.json#9"
      ],
      "text": "{\n  \"id\": \"caller-migration\",\n  \"sourcePaths\": [\n    \"skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\"\n  ],\n  \"prompt\": \"Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.\",\n  \"requirements\": [\n    \"Source and caller usage evidence\",\n    \"No external compatibility requirement and coordinated breaking changes accepted\",\n    \"Authorized writes for migration and deletion\",\n    \"Execution for observed checks\"\n  ],\n  \"expectedFull\": \"Inventory all callers, migrate every caller and remove the old API in the same reviewed refactor unit. Update tests to assert the new contract and delete tests protecting only obsolete implementation details. Use temporary adapters only as exceptional time-boxed measures. Confirm applicability and report observed checks.\",\n  \"expectedReduced\": \"With source available but writes or execution unavailable, provide a coordinated caller migration and API deletion proposal as reduced capability. State which changes and checks were not performed.\",\n  \"expectedBlocked\": \"If source or caller evidence is missing, or external compatibility or coordinated breaking-change requirements are unresolved, block claims that immediate deletion is safe or complete and identify the missing evidence or decision.\",\n  \"forbiddenClaims\": [\n    \"Old API preserved solely because internal callers still exist\",\n    \"Partial migration presented as completed caller migration\",\n    \"Default permanent compatibility adapter\",\n    \"Deletion claimed safe without checking external consumers and applicability\",\n    \"Unperformed writes or checks claimed complete\",\n    \"Structural validation claimed as host behavior or metadata enforcement\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-01/caller-migration/task-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/task-revision.json",
      "sha256": "69a4bfd3c72868a54dfa2058b3c46147677ee8e3cc8bbcff25e9940383d8697c",
      "bytes": 355,
      "owners": [
        "grades-native-00-01.json#9"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/caller-migration/usage-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/usage-inventory.json",
      "sha256": "1ce68fd2e1e15592c9dffbe6618542c54f0046fb7970a000e4a8e867064a421f",
      "bytes": 1347,
      "owners": [
        "grades-native-00-01.json#9"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"rg\",\n    \"-n\",\n    \"--glob\",\n    \"*\",\n    \"export |import |slugify|legacy|obsolete|validator|contract|benny|ownerClaim|existingPr\",\n    \"fixture\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration\",\n  \"exitCode\": 0,\n  \"stdout\": \"fixture/forge.json:37:  \\\"benny\\\": {\\nfixture/forge.json:40:    \\\"marker\\\": \\\"[benny:bug]\\\",\\nfixture/forge.json:42:    \\\"existingPr\\\": \\\"fixture-pr-1\\\",\\nfixture/forge.json:46:    \\\"ownerClaim\\\": {\\nfixture/dashboard.mjs:1:export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nfixture/dashboard.mjs:2:export function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\nfixture/invoice.mjs:1:export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nfixture/invoice.mjs:2:export function adapter(invoice){return calculate(invoice.rows)}\\nfixture/invoice.mjs:3:export function facade(invoice){return adapter(invoice)}\\nfixture/invoice.mjs:4:export function controller(invoice){return {total:facade(invoice)}}\\nfixture/invoice.mjs:5:export function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/caller-migration.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration.result.md",
      "sha256": "6402f200cd543012613ccef49775f70858c90307f7e81d97c903ea0f7a0e20e8",
      "bytes": 5600,
      "owners": [
        "grades-native-00-01.json#9"
      ],
      "text": "# caller-migration\n\n## Supplied input\n\nReplace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.\n\n- Source and caller usage evidence\n- No external compatibility requirement and coordinated breaking changes accepted\n- Authorized writes for migration and deletion\n- Execution for observed checks\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in caller-migration/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nMigration and deletion are blocked by missing concrete prerequisites. The new contract, legacy API identity, target repository, caller inventory boundary, external consumer evidence and decision accepting coordinated breaking changes were not supplied. Case-local write and execution capability exists, so this is not a denied-write or missing-execution fallback.\n\nI copied the inert inputs before inspection. usage-inventory.json records the actual rg command and matches. invoice.mjs has calculate(rows), adapter(invoice), facade(invoice), controller(invoice) and format(n), with local edges controller -> facade -> adapter -> calculate. dashboard.mjs exports visible and exportCsv. There is no task mapping that identifies any of these as the legacy API or supplies an agreed replacement. Exports alone do not prove absence of external consumers. No task Git revision exists, as task-revision.json records.\n\nThe Migrate Callers Then Delete Legacy APIs principle changed the decision to block deletion until its applicability is established. No API, caller or contract test was edited or deleted. No migration check was run, and there is no reviewed refactor unit to accept.\n\nConditional next sequence, not implementation: obtain the exact old and new signatures and intended outputs; inventory imports, exports, dynamic lookup and declared consumers across the complete target scope; establish no external compatibility requirement and acceptance of coordinated breakage; migrate every caller and contract test; delete the old API and obsolete implementation-only tests in the same reviewable unit; run the project checks and a final legacy-symbol search. Do not add a permanent compatibility adapter because callers still exist. This plan cannot establish deletion safety from the current fixtures.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/fixture\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/task-revision.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/caller-migration/usage-inventory.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/baseline.json",
      "sha256": "fff267bce626f22784815b44ee809c8764bad587f8f20675aedd7e67c80cd0bc",
      "bytes": 479,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"cmd\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) original API found and missing contracts [0.73ms]\\n(pass) all downstream user-visible behavior is preserved [0.04ms]\\n\\n 2 pass\\n 0 fail\\n 6 expect() calls\\nRan 2 tests across 1 file. [8.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/capability-bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/capability-bindings.json",
      "sha256": "8b31dfa1c4425694892cfdb73c67fb4ee51bd29c64de2b06e5c1f954a5c982bb",
      "bytes": 1500,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"evidence/inventory-before.json\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"isolated-write\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"work/\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"evidence/baseline.json\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"persistence\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"work/\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": null,\n    \"exposed\": null,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Forbidden by user; not attempted. Connector availability was not probed.\"\n  }\n]"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/final-tests.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/final-tests.json",
      "sha256": "65a87c98ce1310d55d740b11c6038a8b70b22748dc70b0299ab36dbe0654a4f7",
      "bytes": 474,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"cmd\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) new API found and missing contracts [0.12ms]\\n(pass) all downstream user-visible behavior is preserved [0.04ms]\\n\\n 2 pass\\n 0 fail\\n 6 expect() calls\\nRan 2 tests across 1 file. [7.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/inventory-after.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/inventory-after.json",
      "sha256": "8e997988a623a634a9c3999fab438df28e83e6e3b1387e332ee42d3700f7265f",
      "bytes": 1411,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"cmd\": [\n    \"rg\",\n    \"-n\",\n    \"findUser|profileLabel|recipient\",\n    \"--glob\",\n    \"*.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"contract.test.mjs:2:import { findUser } from './api.mjs';\\ncontract.test.mjs:3:import { profileLabel } from './profile.mjs';\\ncontract.test.mjs:4:import { recipient } from './notification.mjs';\\ncontract.test.mjs:7:  expect(findUser({ users, id: 'u1' })).toEqual({ kind: 'found', user: { id: 'u1', name: 'Ada', email: 'ada@example.invalid' } });\\ncontract.test.mjs:8:  expect(findUser({ users, id: 'absent' })).toEqual({ kind: 'missing' });\\ncontract.test.mjs:11:  expect(profileLabel(users, 'u1')).toBe('Ada');\\ncontract.test.mjs:12:  expect(profileLabel(users, 'absent')).toBe('Unknown');\\ncontract.test.mjs:13:  expect(recipient(users, 'u1')).toBe('ada@example.invalid');\\ncontract.test.mjs:14:  expect(recipient(users, 'absent')).toBeNull();\\nnotification.mjs:1:import { findUser } from './api.mjs';\\nnotification.mjs:2:export function recipient(users, id) {\\nnotification.mjs:3:  const result = findUser({ users, id });\\nprofile.mjs:1:import { findUser } from './api.mjs';\\nprofile.mjs:2:export function profileLabel(users, id) {\\nprofile.mjs:3:  const result = findUser({ users, id });\\napi.mjs:1:export function findUser({ users, id }) {\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/inventory-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/inventory-before.json",
      "sha256": "d4a60564e19a230f29e49c780d658452330bec4a1c2b42416afaa32ca6e4db02",
      "bytes": 2817,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"cmd\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"--glob\",\n    \"*.mjs\",\n    \"--glob\",\n    \"*.md\",\n    \"--glob\",\n    \"package.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"package.json:1:{\\\"name\\\":\\\"synthetic-private-user-module\\\",\\\"private\\\":true,\\\"type\\\":\\\"module\\\"}\\napi.mjs:1:export function lookupUser(users, id) { return users.find(user => user.id === id) ?? null; }\\nnotification.mjs:1:import { lookupUser } from './api.mjs';\\nnotification.mjs:2:export function recipient(users, id) { return lookupUser(users, id)?.email ?? null; }\\nprofile.mjs:1:import { lookupUser } from './api.mjs';\\nprofile.mjs:2:export function profileLabel(users, id) { const user = lookupUser(users, id); return user ? user.name : 'Unknown'; }\\ncontract.test.mjs:1:import { test, expect } from 'bun:test';\\ncontract.test.mjs:2:import { lookupUser } from './api.mjs';\\ncontract.test.mjs:3:import { profileLabel } from './profile.mjs';\\ncontract.test.mjs:4:import { recipient } from './notification.mjs';\\ncontract.test.mjs:5:const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\\ncontract.test.mjs:6:test('original API found and missing contracts', () => {\\ncontract.test.mjs:7:  expect(lookupUser(users, 'u1')).toEqual({ id: 'u1', name: 'Ada', email: 'ada@example.invalid' });\\ncontract.test.mjs:8:  expect(lookupUser(users, 'absent')).toBeNull();\\ncontract.test.mjs:9:});\\ncontract.test.mjs:10:test('all downstream user-visible behavior is preserved', () => {\\ncontract.test.mjs:11:  expect(profileLabel(users, 'u1')).toBe('Ada');\\ncontract.test.mjs:12:  expect(profileLabel(users, 'absent')).toBe('Unknown');\\ncontract.test.mjs:13:  expect(recipient(users, 'u1')).toBe('ada@example.invalid');\\ncontract.test.mjs:14:  expect(recipient(users, 'absent')).toBeNull();\\ncontract.test.mjs:15:});\\nscope.md:1:# Agreed internal API migration\\nscope.md:3:This complete private synthetic package has no publication history, dynamic imports, plugin consumers, package exports or external compatibility obligations. All source and test consumers are supplied here. Coordinated breaking changes in the case-owned copy are accepted. This scope decision does not authorize edits to the shared fixture or an unrelated real repository.\\nscope.md:5:New contract: findUser({ users, id }) returns { kind: 'found', user } for a matching row, otherwise { kind: 'missing' }. Preserve profileLabel and recipient literal outputs in contract.test.mjs. Inventory all source/test usages, migrate every caller and direct API contract assertion, then delete lookupUser in one unit. Do not retain an adapter or obsolete null-return API tests. Run the contract with Bun during the actual case; preparation has not run it.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/legacy-usage-after.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/legacy-usage-after.json",
      "sha256": "8ba904944df3d969404d361ff4fe5747eed49f3394401491bbe7af5856cd1072",
      "bytes": 244,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"cmd\": [\n    \"rg\",\n    \"-n\",\n    \"lookupUser\",\n    \"--glob\",\n    \"*.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/reduced-variants.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/reduced-variants.json",
      "sha256": "7583fbb527ba5a87848573b8dc85b46e735074b369d94b42f217321b1eb8d0bd",
      "bytes": 1477,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "[\n  {\n    \"variant\": \"source available, writes withheld\",\n    \"enforcement\": \"simulated by deliberately not performing edits in this narrative branch; host writes are available\",\n    \"actualResponse\": \"With source available and writes withheld, propose one coordinated unit: replace lookupUser with findUser, update profileLabel and recipient to branch on kind, update the direct found/missing contracts, retain downstream literal expectations, then remove the old API. Under this simulated restriction no migration edits or migration test runs are performed in the variant.\"\n  },\n  {\n    \"variant\": \"execution withheld\",\n    \"enforcement\": \"simulated narrative branch; host execution is available\",\n    \"actualResponse\": \"With execution withheld, the copied migration diff is inspectable, but no executed contract result can be attributed to this variant. Run bun test contract.test.mjs once execution is available; until then report runtime verification unobserved for the variant.\"\n  },\n  {\n    \"variant\": \"missing source or applicability evidence\",\n    \"enforcement\": \"simulated narrative branch; prepared source and scope are actually available\",\n    \"actualResponse\": \"Without source/caller inventory, or without the explicit external-consumer and coordinated-change decisions, immediate API deletion cannot be declared safe or complete. Obtain the full source inventory and scope decision first. Do not infer absence of external consumers from private:true alone.\"\n  }\n]"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/registry-entry.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/registry-entry.json",
      "sha256": "8be46c18d30128bc7291c6d216f86b01cb89c172bf92d08d1671445275187b50",
      "bytes": 742,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"caseId\": \"caller-migration\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json\",\n  \"sourcePaths\": [\n    \"skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/review-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/review-diff.json",
      "sha256": "47615c8f68ce6c120b1de47a4c942418436052b034623f31d3fb961ff9660aa0",
      "bytes": 2693,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"cmd\": [\n    \"diff\",\n    \"-ru\",\n    \"../input\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru ../input/api.mjs ./api.mjs\\n--- ../input/api.mjs\\t2026-10-16 10:49:12\\n+++ ./api.mjs\\t2026-10-16 10:51:18\\n@@ -1 +1,4 @@\\n-export function lookupUser(users, id) { return users.find(user => user.id === id) ?? null; }\\n+export function findUser({ users, id }) {\\n+  const user = users.find(user => user.id === id);\\n+  return user ? { kind: 'found', user } : { kind: 'missing' };\\n+}\\ndiff -ru ../input/contract.test.mjs ./contract.test.mjs\\n--- ../input/contract.test.mjs\\t2026-10-16 10:49:12\\n+++ ./contract.test.mjs\\t2026-10-16 10:51:18\\n@@ -1,11 +1,11 @@\\n import { test, expect } from 'bun:test';\\n-import { lookupUser } from './api.mjs';\\n+import { findUser } from './api.mjs';\\n import { profileLabel } from './profile.mjs';\\n import { recipient } from './notification.mjs';\\n const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\\n-test('original API found and missing contracts', () => {\\n-  expect(lookupUser(users, 'u1')).toEqual({ id: 'u1', name: 'Ada', email: 'ada@example.invalid' });\\n-  expect(lookupUser(users, 'absent')).toBeNull();\\n+test('new API found and missing contracts', () => {\\n+  expect(findUser({ users, id: 'u1' })).toEqual({ kind: 'found', user: { id: 'u1', name: 'Ada', email: 'ada@example.invalid' } });\\n+  expect(findUser({ users, id: 'absent' })).toEqual({ kind: 'missing' });\\n });\\n test('all downstream user-visible behavior is preserved', () => {\\n   expect(profileLabel(users, 'u1')).toBe('Ada');\\ndiff -ru ../input/notification.mjs ./notification.mjs\\n--- ../input/notification.mjs\\t2026-10-16 10:49:12\\n+++ ./notification.mjs\\t2026-10-16 10:51:18\\n@@ -1,2 +1,5 @@\\n-import { lookupUser } from './api.mjs';\\n-export function recipient(users, id) { return lookupUser(users, id)?.email ?? null; }\\n+import { findUser } from './api.mjs';\\n+export function recipient(users, id) {\\n+  const result = findUser({ users, id });\\n+  return result.kind === 'found' ? result.user.email : null;\\n+}\\ndiff -ru ../input/profile.mjs ./profile.mjs\\n--- ../input/profile.mjs\\t2026-10-16 10:49:12\\n+++ ./profile.mjs\\t2026-10-16 10:51:18\\n@@ -1,2 +1,5 @@\\n-import { lookupUser } from './api.mjs';\\n-export function profileLabel(users, id) { const user = lookupUser(users, id); return user ? user.name : 'Unknown'; }\\n+import { findUser } from './api.mjs';\\n+export function profileLabel(users, id) {\\n+  const result = findUser({ users, id });\\n+  return result.kind === 'found' ? result.user.name : 'Unknown';\\n+}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/shared-input-integrity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/shared-input-integrity.json",
      "sha256": "6658184ce353f566cca15ab0edb0e00ed56025358745087d6831a4e88b52f6f4",
      "bytes": 1225,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"caller-migration/profile.mjs\": {\n    \"before\": \"2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465\",\n    \"after\": \"2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465\"\n  },\n  \"caller-migration/scope.md\": {\n    \"before\": \"ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed\",\n    \"after\": \"ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed\"\n  },\n  \"caller-migration/api.mjs\": {\n    \"before\": \"822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7\",\n    \"after\": \"822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7\"\n  },\n  \"caller-migration/notification.mjs\": {\n    \"before\": \"ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee\",\n    \"after\": \"ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee\"\n  },\n  \"caller-migration/contract.test.mjs\": {\n    \"before\": \"5574d0adbf1362444a5d8e0b275a4d52cfed5c79dc3822f4560d6b24928e35a5\",\n    \"after\": \"5574d0adbf1362444a5d8e0b275a4d52cfed5c79dc3822f4560d6b24928e35a5\"\n  },\n  \"caller-migration/package.json\": {\n    \"before\": \"23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0\",\n    \"after\": \"23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0\"\n  }\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/supplied-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/evidence/supplied-case.json",
      "sha256": "665fecee2989595117b22fb918e9f8f612be45d18a02f5e1d1eafea7ecdf3459",
      "bytes": 1964,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "{\n  \"id\": \"caller-migration\",\n  \"sourcePaths\": [\n    \"skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\"\n  ],\n  \"prompt\": \"Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.\",\n  \"requirements\": [\n    \"Source and caller usage evidence\",\n    \"No external compatibility requirement and coordinated breaking changes accepted\",\n    \"Authorized writes for migration and deletion\",\n    \"Execution for observed checks\"\n  ],\n  \"expectedFull\": \"Inventory all callers, migrate every caller and remove the old API in the same reviewed refactor unit. Update tests to assert the new contract and delete tests protecting only obsolete implementation details. Use temporary adapters only as exceptional time-boxed measures. Confirm applicability and report observed checks.\",\n  \"expectedReduced\": \"With source available but writes or execution unavailable, provide a coordinated caller migration and API deletion proposal as reduced capability. State which changes and checks were not performed.\",\n  \"expectedBlocked\": \"If source or caller evidence is missing, or external compatibility or coordinated breaking-change requirements are unresolved, block claims that immediate deletion is safe or complete and identify the missing evidence or decision.\",\n  \"forbiddenClaims\": [\n    \"Old API preserved solely because internal callers still exist\",\n    \"Partial migration presented as completed caller migration\",\n    \"Default permanent compatibility adapter\",\n    \"Deletion claimed safe without checking external consumers and applicability\",\n    \"Unperformed writes or checks claimed complete\",\n    \"Structural validation claimed as host behavior or metadata enforcement\"\n  ]\n}"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/api.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work/api.mjs",
      "sha256": "943675826fa84d6a33954c4128a754d3c2711197184138fdffe921ec7aceb576",
      "bytes": 158,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "export function findUser({ users, id }) {\n  const user = users.find(user => user.id === id);\n  return user ? { kind: 'found', user } : { kind: 'missing' };\n}\n"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/contract.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work/contract.test.mjs",
      "sha256": "4dc5e4b4d331ae8b27334f21839392132a40b35127a099c238e57f3bf69a896e",
      "bytes": 794,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { findUser } from './api.mjs';\nimport { profileLabel } from './profile.mjs';\nimport { recipient } from './notification.mjs';\nconst users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\ntest('new API found and missing contracts', () => {\n  expect(findUser({ users, id: 'u1' })).toEqual({ kind: 'found', user: { id: 'u1', name: 'Ada', email: 'ada@example.invalid' } });\n  expect(findUser({ users, id: 'absent' })).toEqual({ kind: 'missing' });\n});\ntest('all downstream user-visible behavior is preserved', () => {\n  expect(profileLabel(users, 'u1')).toBe('Ada');\n  expect(profileLabel(users, 'absent')).toBe('Unknown');\n  expect(recipient(users, 'u1')).toBe('ada@example.invalid');\n  expect(recipient(users, 'absent')).toBeNull();\n});\n"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/notification.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work/notification.mjs",
      "sha256": "013f24fb2266188e87205088e5ba4ff672958414c377b21deb3435eb10837614",
      "bytes": 182,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "import { findUser } from './api.mjs';\nexport function recipient(users, id) {\n  const result = findUser({ users, id });\n  return result.kind === 'found' ? result.user.email : null;\n}\n"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/profile.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work/profile.mjs",
      "sha256": "c5514fa479b90c4a781e2f9ca790d980b584d68838640d720961d99c80ecfaf5",
      "bytes": 189,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "import { findUser } from './api.mjs';\nexport function profileLabel(users, id) {\n  const result = findUser({ users, id });\n  return result.kind === 'found' ? result.user.name : 'Unknown';\n}\n"
    },
    {
      "path": "fixtures/rerun-01/caller-migration.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration.result.md",
      "sha256": "857360655bc6861cf1f34157ced001dab3dfbb5fd11ad070ca7250dfb9d99158",
      "bytes": 5559,
      "owners": [
        "grades-native-rerun-01.json#0"
      ],
      "text": "# caller-migration\n\n## Supplied input and scope\n\nReplace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.\n\nRequirements supplied:\n\n- Source and caller usage evidence\n- No external compatibility requirement and coordinated breaking changes accepted\n- Authorized writes for migration and deletion\n- Execution for observed checks\n\nPackage root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nUser-supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Installed files were read directly and copied into evidence/. The commit identity was supplied by the user, not independently established from an installed Git checkout. No 0.2.1 files were used.\n\nPrepared input root: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v2/caller-migration\n\ninput/ preserves all supplied case-specific files. evidence/supplied-case.json preserves the installed registered prompt, requirements and expected variants; evidence/registry-entry.json preserves its registry entry. The scenario-map and scope documents describe synthetic inert fixtures. They are not host receipts.\n\n## Actual response and output\n\nInspected the complete private fixture package and scope decision. The scope explicitly accepts coordinated breaking changes and states there are no external consumers, dynamic imports, plugin consumers, package exports or publication history. This is supplied synthetic scope evidence, not a claim about a production package.\n\nThe usage inventory found lookupUser in its definition, profileLabel, recipient and the direct API contract test. Migrated both production callers and direct found/missing assertions to findUser({ users, id }). Deleted lookupUser with no adapter. The downstream literal outputs remain Ada, Unknown, ada@example.invalid and null. Reviewed all four changed files together in evidence/review-diff.json. The final source search for lookupUser had no matches, exit 1.\n\nObserved baseline: 2 tests, 6 assertions. Observed final: 2 tests, 6 assertions, no failures. No external review, commit or PR was created.\n\n## Actual tools and artifacts\n\nUsed functions.exec with tools.exec_command to read instructions and fixtures, run Bun 1.4.2, and inspect saved output. Used tools.apply_patch to write the local Bun runners. run-cases.mjs uses Bun file reads, local filesystem copies/writes and Bun.spawnSync for rg, diff and bun test. No native workers are required by these direct workflows, and none were spawned.\n\nThe exact edited output is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/caller-migration/work/. Original copies are in input/. Every command below has its argument array, working directory, exit code, stdout and stderr preserved in evidence/<name>.json. Diff exit 1 means differences found; rg exit 1 means no matches. Mutation test exit 1 is the observed deliberate defect.\n\n| Command artifact | Exit code |\n| --- | --- |\n| evidence/inventory-before.json | 0 |\n| evidence/baseline.json | 0 |\n| evidence/final-tests.json | 0 |\n| evidence/legacy-usage-after.json | 1 |\n| evidence/inventory-after.json | 0 |\n| evidence/review-diff.json | 1 |\n\nShared input SHA-256 values were compared before and after execution, with matching values in evidence/shared-input-integrity.json. The source-skill and support-file copies in evidence/ preserve the instructions actually used. review-diff.json records the reviewed combined changes.\n\n## Variants attempted and limits\n\nThe full source/write/execution variant ran on the real host. The following conditional capability branches were exercised as explicit response-only simulations, also saved in evidence/reduced-variants.json. The host does not enforce those negative conditions here. These narratives do not establish denied-tool handling or isolated executions under unavailable capabilities.\n\n- source available, writes withheld: With source available and writes withheld, propose one coordinated unit: replace lookupUser with findUser, update profileLabel and recipient to branch on kind, update the direct found/missing contracts, retain downstream literal expectations, then remove the old API. Under this simulated restriction no migration edits or migration test runs are performed in the variant.\n\n- execution withheld: With execution withheld, the copied migration diff is inspectable, but no executed contract result can be attributed to this variant. Run bun test contract.test.mjs once execution is available; until then report runtime verification unobserved for the variant.\n\n- missing source or applicability evidence: Without source/caller inventory, or without the explicit external-consumer and coordinated-change decisions, immediate API deletion cannot be declared safe or complete. Obtain the full source inventory and scope decision first. Do not infer absence of external consumers from private:true alone.\n\nNo live service was contacted. No external account writes, issues, PRs, messages, commits, pushes, publishing, credential or configuration changes, installs or schedules were performed. No prior result files were overwritten. No host parity, metadata enforcement, independent review or package release validation is claimed. No self-assigned case grade is supplied.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-01/caller-migration/fixture/README.md",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/dashboard.mjs",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/forge.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/history.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/invoice.mjs",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/orders.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/runtime.mjs",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-01/caller-migration/input.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/caller-migration/source",
      "owner": "grades-native-00-01.json#9",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/caller-migration/source-manifest.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/README.md",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/dashboard.mjs",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/forge.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/history.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/invoice.mjs",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/orders.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-01/caller-migration/fixture/runtime.mjs",
      "owner": "grades-native-00-01.json#9",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-01/caller-migration/input.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/caller-migration/source",
      "owner": "grades-native-00-01.json#9",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/caller-migration/source-manifest.json",
      "owner": "grades-native-00-01.json#9",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/references__host-capabilities.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/scenario-map.json",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/skills__principle-migrate-callers-then-delete-legacy-apis__SKILL.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/skills__unslop__SKILL.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/input",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/package.json",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/package.json",
      "sha256": "23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0",
      "bytes": 72
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/scope.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/scope.md",
      "sha256": "ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed",
      "bytes": 866
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/references__host-capabilities.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/scenario-map.json",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/skills__principle-migrate-callers-then-delete-legacy-apis__SKILL.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/evidence/skills__unslop__SKILL.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/input",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/package.json",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/package.json",
      "sha256": "23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0",
      "bytes": 72
    },
    {
      "path": "fixtures/rerun-01/caller-migration/work/scope.md",
      "owner": "grades-native-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/scope.md",
      "sha256": "ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed",
      "bytes": 866
    }
  ],
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
