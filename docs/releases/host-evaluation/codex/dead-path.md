# codex: dead-path

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "dead-path",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-rerun-01.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.",
  "caseDefinition": {
    "id": "dead-path",
    "sourcePaths": [
      "skills/principle-subtract-before-you-add/SKILL.md"
    ],
    "prompt": "Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.",
    "requirements": [
      "Available source and observed usage",
      "Authorization and write capability for changes",
      "Execution capability for actual checks"
    ],
    "expectedFull": "Inspect actual usage and requirements, remove obsolete behavior before constructing the replacement, and show the sequence and observed checks. Cut before polishing, preserve required behavior, avoid speculative edge cases, validators, parsers and guards, simplify redundant prompts, and delete empty references rather than leaving stubs. Leave the design simpler and more capable behind the same or smaller interface.",
    "expectedReduced": "With source available but writes or execution unavailable, provide an ordered removal and replacement proposal as reduced capability. State which edits and checks were not performed.",
    "expectedBlocked": "If source or required usage evidence is unavailable, state the missing inputs and block claims that deletion is safe or completed. Do not invent obsolete paths or usage.",
    "forbiddenClaims": [
      "Replacement constructed before obsolete behavior is removed",
      "Deletion is safe without inspecting usage and required behavior",
      "Unperformed edits or checks claimed complete",
      "Speculative guards added beyond the specification",
      "Host parity or metadata enforcement claimed from structural validation"
    ],
    "caseFile": "docs/parity/cases/skills/principle-subtract-before-you-add.json"
  },
  "registry": {
    "caseId": "dead-path",
    "caseFile": "docs/parity/cases/skills/principle-subtract-before-you-add.json",
    "sourcePaths": [
      "skills/principle-subtract-before-you-add/SKILL.md"
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
      "attemptId": "grades-native-00-01.json#12",
      "order": 0,
      "gradeFile": "grades-native-00-01.json",
      "rankWithinFile": 12,
      "host": "codex",
      "caseId": "dead-path",
      "status": "blocked",
      "grade": {
        "caseId": "dead-path",
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
          "Concrete obsolete behavior and safe deletion/usage evidence absent.",
          "Specified replacement and redundant prompt/reference inputs absent.",
          "No target removal/replacement or associated checks performed."
        ],
        "review": "No identified obsolete route, replacement specification, redundant validator, duplicate prompt or empty reference exists in the supplied inputs. Model inventories source and refuses speculative deletion. Available writes/execution do not make missing usage evidence safe.",
        "concreteFixCandidates": [
          "Evaluation fixture: provide named obsolete route, migrated callers, preserved behavior and replacement specification."
        ],
        "variantReview": [],
        "reviewedBy": "grade_contract_audit subagent; independent qualitative review of raw events and saved output",
        "responseArtifact": "fixtures/batch-01/dead-path.result.md",
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
        "text": "# dead-path\n\n## Supplied input\n\nReplace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\n\n- Available source and observed usage\n- Authorization and write capability for changes\n- Execution capability for actual checks\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in dead-path/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nRemoval and replacement are blocked. The supplied fixtures contain no identified obsolete request path, supported handler, redundant validator, duplicate prompt, empty reference or specified replacement behavior. The actual usage inventory is in usage-inventory.json. invoice.mjs's format guard is observable source, but nothing establishes that it is redundant or belongs to this case. I did not delete it.\n\nThe Subtract Before You Add principle changed the sequence to put evidence-backed deletion before replacement construction. Case-local writes and Bun execution are available and authorized. The missing inputs are task source, usage boundary and replacement specification. No target edit, deletion or replacement check occurred. A successful search command is source inventory only.\n\nConditional order, not completed work: identify the obsolete route and all callers, show that callers use the supported handler, and establish the required preserved behavior. Remove that obsolete path and its proven-redundant validator first. Simplify duplicate instructions and delete a reference only after comparing its entire content and inbound links. Check the supported handler and removed-symbol usage at that checkpoint. Then add only the specified replacement, run its behavior checks and nearby handler regressions, and inspect the final diff. The actual task cannot safely reach the first removal with the available inputs.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-subtract-before-you-add/SKILL.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/fixture\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/task-revision.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/usage-inventory.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n",
        "artifact": {
          "path": "fixtures/batch-01/dead-path.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path.result.md",
          "sha256": "13a5d14c15000224f222d5d454c68df1f54bb988031cdfb8078116959a66d257",
          "bytes": 5127
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
      "attemptId": "grades-native-rerun-01.json#1",
      "order": 101,
      "gradeFile": "grades-native-rerun-01.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "dead-path",
      "status": "pass",
      "grade": {
        "caseId": "dead-path",
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
        "review": "Complete input establishes only supportedRequest has production caller. Native runner removes obsoleteRequest and redundantValid and simplifies/deletes duplicate docs first, saves removal-stage snapshot and runs intermediate passing tests before optional note passthrough. Final literal omission/hello/empty-string acceptance passes2tests/5assertions; no new validator or speculative guard. Full requested subtraction-before-addition order observed.",
        "variantReview": [
          "Removal-only intermediate stage:1test/2assertions and no removed names.",
          "Replacement: undefined omitted, hello/empty preserved.",
          "Capability-negative narratives simulated."
        ],
        "limits": [
          "Synthetic complete scope, not external production usage."
        ],
        "evidence": [
          "fixtures/rerun-01/dead-path/evidence/removal-stage-tests.json",
          "fixtures/rerun-01/dead-path/evidence/removal-stage-search.json",
          "fixtures/rerun-01/dead-path/evidence/final-tests.json",
          "fixtures/rerun-01/dead-path/evidence/review-diff.json"
        ],
        "responseArtifact": "fixtures/rerun-01/dead-path.result.md",
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
        "text": "# dead-path\n\n## Supplied input and scope\n\nReplace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\n\nRequirements supplied:\n\n- Available source and observed usage\n- Authorization and write capability for changes\n- Execution capability for actual checks\n\nPackage root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nUser-supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Installed files were read directly and copied into evidence/. The commit identity was supplied by the user, not independently established from an installed Git checkout. No 0.2.1 files were used.\n\nPrepared input root: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v2/dead-path\n\ninput/ preserves all supplied case-specific files. evidence/supplied-case.json preserves the installed registered prompt, requirements and expected variants; evidence/registry-entry.json preserves its registry entry. The scenario-map and scope documents describe synthetic inert fixtures. They are not host receipts.\n\n## Actual response and output\n\nInspected handler.mjs, caller.mjs, contract.test.mjs, scope.md and both documentation files. The only production caller imports supportedRequest. obsoleteRequest is referenced only by its own definition, and redundantValid is used only by that function. The supplied complete synthetic scope declares the internal request boundary already validated and accepts removal.\n\nPerformed this order:\n\n1. Removed obsoleteRequest and redundantValid from the copied handler.\n2. Reduced instructions.md to one instruction and deleted duplicate-reference.md and its reference.\n3. Saved removal-stage/ before adding replacement behavior. Existing contract tests still passed, 1 test and 2 assertions. Source/documentation search for the removed names had no matches, exit 1.\n4. Added optional note passthrough to supportedRequest. Undefined omits the field; hello and the empty string retain their literal values. Added all three supplied acceptance cases as literal assertions. No new validator was added.\n5. Ran final contracts: 2 tests, 5 assertions, no failures. Reviewed evidence/review-diff.json. The public module now exports only supportedRequest; caller.mjs is unchanged.\n\n## Actual tools and artifacts\n\nUsed functions.exec with tools.exec_command to read instructions and fixtures, run Bun 1.4.2, and inspect saved output. Used tools.apply_patch to write the local Bun runners. run-cases.mjs uses Bun file reads, local filesystem copies/writes and Bun.spawnSync for rg, diff and bun test. No native workers are required by these direct workflows, and none were spawned.\n\nThe exact edited output is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work/. Original copies are in input/. Every command below has its argument array, working directory, exit code, stdout and stderr preserved in evidence/<name>.json. Diff exit 1 means differences found; rg exit 1 means no matches. Mutation test exit 1 is the observed deliberate defect.\n\n| Command artifact | Exit code |\n| --- | --- |\n| evidence/inventory-before.json | 0 |\n| evidence/baseline.json | 0 |\n| evidence/removal-stage-tests.json | 0 |\n| evidence/removal-stage-search.json | 1 |\n| evidence/final-tests.json | 0 |\n| evidence/review-diff.json | 1 |\n\nShared input SHA-256 values were compared before and after execution, with matching values in evidence/shared-input-integrity.json. The source-skill and support-file copies in evidence/ preserve the instructions actually used. review-diff.json records the reviewed combined changes.\n\n## Variants attempted and limits\n\nThe full source/write/execution variant ran on the real host. The following conditional capability branches were exercised as explicit response-only simulations, also saved in evidence/reduced-variants.json. The host does not enforce those negative conditions here. These narratives do not establish denied-tool handling or isolated executions under unavailable capabilities.\n\n- source available, writes withheld: With source available and writes withheld, propose: inventory all handlers and imports; remove obsoleteRequest and redundantValid; simplify the repeated instruction and delete duplicate-reference.md; only then add optional note passthrough and all literal acceptance cases. No removal or replacement is performed under this simulated restriction.\n\n- execution withheld: With execution withheld, inspect the ordered removal snapshot and final diff but report both intermediate and final test execution unobserved for this variant. Run bun test contract.test.mjs at each stage after execution becomes available.\n\n- missing source or applicability evidence: Without source or required usage evidence, do not label the path obsolete or deletion safe. Obtain handler, caller, contract and scope files before making removal claims.\n\nNo live service was contacted. No external account writes, issues, PRs, messages, commits, pushes, publishing, credential or configuration changes, installs or schedules were performed. No prior result files were overwritten. No host parity, metadata enforcement, independent review or package release validation is claimed. No self-assigned case grade is supplied.\n",
        "artifact": {
          "path": "fixtures/rerun-01/dead-path.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path.result.md",
          "sha256": "805ac944293977aef8f0f307cb008dba4635f0385806f634323e12fb93922a97",
          "bytes": 5595
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
            "path": "fixtures/rerun-01/dead-path/evidence/removal-stage-tests.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/removal-stage-tests.json",
            "sha256": "39f315b0dac09cd075477bd1fd1381ad80d1494c3a116cb4284fc7e7edef1477",
            "bytes": 433
          },
          {
            "path": "fixtures/rerun-01/dead-path/evidence/removal-stage-search.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/removal-stage-search.json",
            "sha256": "c1eee451c8f0d2482340eefffaeab06fb8316fe4a60c7ba1ce82ccddb83ac7fe",
            "bytes": 314
          },
          {
            "path": "fixtures/rerun-01/dead-path/evidence/final-tests.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/final-tests.json",
            "sha256": "e390eee72f3e0b20f6fa115d6a4ba90cbb742aa4631688274728d40a58ea0265",
            "bytes": 503
          },
          {
            "path": "fixtures/rerun-01/dead-path/evidence/review-diff.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/review-diff.json",
            "sha256": "10284bc1e00cf7bc8d864e026ce1230e2ed2d2489a807ca5d00ff3c513485b4e",
            "bytes": 2001
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
      "path": "fixtures/batch-01/dead-path/host.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/host.json",
      "sha256": "4ffb3e5dbe3cc866c6733a98c0e5ca0e43b4c450cc075f6e132cd6cb699cbe59",
      "bytes": 271,
      "owners": [
        "grades-native-00-01.json#12"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/dead-path/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/registered-case.json",
      "sha256": "a466f3bc94d1c643b1e431b4e165a5b915de0e9d32100b823a93100778079a96",
      "bytes": 704,
      "owners": [
        "grades-native-00-01.json#12"
      ],
      "text": "{\n  \"caseId\": \"dead-path\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-subtract-before-you-add.json\",\n  \"sourcePaths\": [\n    \"skills/principle-subtract-before-you-add/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/batch-01/dead-path/registered-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/registered-input.json",
      "sha256": "7dec771a53f14fd75c49722fbd4d6b2107880e8afb43b13150425e07e4f35050",
      "bytes": 1874,
      "owners": [
        "grades-native-00-01.json#12"
      ],
      "text": "{\n  \"id\": \"dead-path\",\n  \"sourcePaths\": [\n    \"skills/principle-subtract-before-you-add/SKILL.md\"\n  ],\n  \"prompt\": \"Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\",\n  \"requirements\": [\n    \"Available source and observed usage\",\n    \"Authorization and write capability for changes\",\n    \"Execution capability for actual checks\"\n  ],\n  \"expectedFull\": \"Inspect actual usage and requirements, remove obsolete behavior before constructing the replacement, and show the sequence and observed checks. Cut before polishing, preserve required behavior, avoid speculative edge cases, validators, parsers and guards, simplify redundant prompts, and delete empty references rather than leaving stubs. Leave the design simpler and more capable behind the same or smaller interface.\",\n  \"expectedReduced\": \"With source available but writes or execution unavailable, provide an ordered removal and replacement proposal as reduced capability. State which edits and checks were not performed.\",\n  \"expectedBlocked\": \"If source or required usage evidence is unavailable, state the missing inputs and block claims that deletion is safe or completed. Do not invent obsolete paths or usage.\",\n  \"forbiddenClaims\": [\n    \"Replacement constructed before obsolete behavior is removed\",\n    \"Deletion is safe without inspecting usage and required behavior\",\n    \"Unperformed edits or checks claimed complete\",\n    \"Speculative guards added beyond the specification\",\n    \"Host parity or metadata enforcement claimed from structural validation\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-01/dead-path/task-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/task-revision.json",
      "sha256": "16814affcfeca0121d5603178aeac8987d5536698e59a5cd39b7b124e1190c6b",
      "bytes": 348,
      "owners": [
        "grades-native-00-01.json#12"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/dead-path/usage-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/usage-inventory.json",
      "sha256": "b815ff02cb315ed6e3b05fade1542fc5f8a3cafe480cd8902a6e96e90d452300",
      "bytes": 1340,
      "owners": [
        "grades-native-00-01.json#12"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"rg\",\n    \"-n\",\n    \"--glob\",\n    \"*\",\n    \"export |import |slugify|legacy|obsolete|validator|contract|benny|ownerClaim|existingPr\",\n    \"fixture\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path\",\n  \"exitCode\": 0,\n  \"stdout\": \"fixture/forge.json:37:  \\\"benny\\\": {\\nfixture/forge.json:40:    \\\"marker\\\": \\\"[benny:bug]\\\",\\nfixture/forge.json:42:    \\\"existingPr\\\": \\\"fixture-pr-1\\\",\\nfixture/forge.json:46:    \\\"ownerClaim\\\": {\\nfixture/invoice.mjs:1:export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nfixture/invoice.mjs:2:export function adapter(invoice){return calculate(invoice.rows)}\\nfixture/invoice.mjs:3:export function facade(invoice){return adapter(invoice)}\\nfixture/invoice.mjs:4:export function controller(invoice){return {total:facade(invoice)}}\\nfixture/invoice.mjs:5:export function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\nfixture/dashboard.mjs:1:export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nfixture/dashboard.mjs:2:export function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/dead-path.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path.result.md",
      "sha256": "13a5d14c15000224f222d5d454c68df1f54bb988031cdfb8078116959a66d257",
      "bytes": 5127,
      "owners": [
        "grades-native-00-01.json#12"
      ],
      "text": "# dead-path\n\n## Supplied input\n\nReplace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\n\n- Available source and observed usage\n- Authorization and write capability for changes\n- Execution capability for actual checks\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in dead-path/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nRemoval and replacement are blocked. The supplied fixtures contain no identified obsolete request path, supported handler, redundant validator, duplicate prompt, empty reference or specified replacement behavior. The actual usage inventory is in usage-inventory.json. invoice.mjs's format guard is observable source, but nothing establishes that it is redundant or belongs to this case. I did not delete it.\n\nThe Subtract Before You Add principle changed the sequence to put evidence-backed deletion before replacement construction. Case-local writes and Bun execution are available and authorized. The missing inputs are task source, usage boundary and replacement specification. No target edit, deletion or replacement check occurred. A successful search command is source inventory only.\n\nConditional order, not completed work: identify the obsolete route and all callers, show that callers use the supported handler, and establish the required preserved behavior. Remove that obsolete path and its proven-redundant validator first. Simplify duplicate instructions and delete a reference only after comparing its entire content and inbound links. Check the supported handler and removed-symbol usage at that checkpoint. Then add only the specified replacement, run its behavior checks and nearby handler regressions, and inspect the final diff. The actual task cannot safely reach the first removal with the available inputs.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-subtract-before-you-add/SKILL.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/fixture\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/task-revision.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dead-path/usage-inventory.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/baseline.json",
      "sha256": "7fb88516e93714b41becbbe8c9c065ae3c0e59da7742d8a8fa751aad9fa87116",
      "bytes": 433,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"cmd\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) supported request and all production callers preserve existing output [0.07ms]\\n\\n 1 pass\\n 0 fail\\n 2 expect() calls\\nRan 1 test across 1 file. [5.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/capability-bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/capability-bindings.json",
      "sha256": "8b31dfa1c4425694892cfdb73c67fb4ee51bd29c64de2b06e5c1f954a5c982bb",
      "bytes": 1500,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"evidence/inventory-before.json\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"isolated-write\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"work/\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"evidence/baseline.json\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"persistence\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"work/\",\n    \"limits\": \"Observed direct filesystem and Bun operations in the authorized case directory; no independent worker operation required or invoked.\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": null,\n    \"exposed\": null,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Forbidden by user; not attempted. Connector availability was not probed.\"\n  }\n]"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/final-tests.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/final-tests.json",
      "sha256": "e390eee72f3e0b20f6fa115d6a4ba90cbb742aa4631688274728d40a58ea0265",
      "bytes": 503,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"cmd\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) supported request and all production callers preserve existing output [0.07ms]\\n(pass) optional note preserves literal values and omission [0.02ms]\\n\\n 2 pass\\n 0 fail\\n 5 expect() calls\\nRan 2 tests across 1 file. [6.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/inventory-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/inventory-before.json",
      "sha256": "a962b4cfa7c50f0da1cd1250acef2abc3d52fb708eb4ed8b6b0fcf3071521ecd",
      "bytes": 2510,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"cmd\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"--glob\",\n    \"*.mjs\",\n    \"--glob\",\n    \"*.md\",\n    \"--glob\",\n    \"package.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"instructions.md:1:Use the supported request handler. Use the supported request handler for requests. Read duplicate-reference.md for the same instruction.\\nduplicate-reference.md:1:Use the supported request handler.\\ncontract.test.mjs:1:import { test, expect } from 'bun:test';\\ncontract.test.mjs:2:import { supportedRequest } from './handler.mjs';\\ncontract.test.mjs:3:import { submit } from './caller.mjs';\\ncontract.test.mjs:4:test('supported request and all production callers preserve existing output', () => {\\ncontract.test.mjs:5:  expect(supportedRequest({ id: 'r1' })).toEqual({ id: 'r1', status: 'accepted' });\\ncontract.test.mjs:6:  expect(submit('r2')).toEqual({ id: 'r2', status: 'accepted' });\\ncontract.test.mjs:7:});\\ncaller.mjs:1:import { supportedRequest } from './handler.mjs';\\ncaller.mjs:2:export function submit(id) { return supportedRequest({ id }); }\\nscope.md:1:# Removal before replacement\\nscope.md:3:The complete synthetic source and contract-test consumers are supplied in this directory. No production caller uses obsoleteRequest. Its validator exists solely for that unused function. The supported handler accepts already-validated typed requests at a private internal boundary. No compatibility obligation remains for obsoleteRequest.\\nscope.md:5:First inspect usages and remove obsoleteRequest plus redundantValid. Then simplify instructions.md and delete the reference link and duplicate-reference.md, which adds no content. Only after that removal, extend supportedRequest to pass through optional request.note when provided. Preserve current id/status outputs and do not add speculative validation. Add the concrete acceptance cases from acceptance.json to the case-owned test suite and observe results. Keep shared inputs unchanged.\\nhandler.mjs:1:function redundantValid(request) { return request && typeof request === 'object' && typeof request.id === 'string'; }\\nhandler.mjs:2:export function obsoleteRequest(request) {\\nhandler.mjs:3:  if (!redundantValid(request)) throw new Error('invalid');\\nhandler.mjs:4:  return { id: request.id, obsolete: true };\\nhandler.mjs:5:}\\nhandler.mjs:6:export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/reduced-variants.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/reduced-variants.json",
      "sha256": "debf1edc6b728bf485a0b9aa0a978fa4a11e0e28f6e441937eff1d929723aec9",
      "bytes": 1305,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "[\n  {\n    \"variant\": \"source available, writes withheld\",\n    \"enforcement\": \"simulated by deliberately not performing edits in this narrative branch; host writes are available\",\n    \"actualResponse\": \"With source available and writes withheld, propose: inventory all handlers and imports; remove obsoleteRequest and redundantValid; simplify the repeated instruction and delete duplicate-reference.md; only then add optional note passthrough and all literal acceptance cases. No removal or replacement is performed under this simulated restriction.\"\n  },\n  {\n    \"variant\": \"execution withheld\",\n    \"enforcement\": \"simulated narrative branch; host execution is available\",\n    \"actualResponse\": \"With execution withheld, inspect the ordered removal snapshot and final diff but report both intermediate and final test execution unobserved for this variant. Run bun test contract.test.mjs at each stage after execution becomes available.\"\n  },\n  {\n    \"variant\": \"missing source or applicability evidence\",\n    \"enforcement\": \"simulated narrative branch; prepared source and scope are actually available\",\n    \"actualResponse\": \"Without source or required usage evidence, do not label the path obsolete or deletion safe. Obtain handler, caller, contract and scope files before making removal claims.\"\n  }\n]"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/registry-entry.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/registry-entry.json",
      "sha256": "04dcdea7b60702cba30f3cb656134083a83c7d491b2fca658792b993223bfe1b",
      "bytes": 703,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"caseId\": \"dead-path\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-subtract-before-you-add.json\",\n  \"sourcePaths\": [\n    \"skills/principle-subtract-before-you-add/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/removal-stage-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/removal-stage-search.json",
      "sha256": "c1eee451c8f0d2482340eefffaeab06fb8316fe4a60c7ba1ce82ccddb83ac7fe",
      "bytes": 314,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"cmd\": [\n    \"rg\",\n    \"-n\",\n    \"obsoleteRequest|redundantValid|duplicate-reference\",\n    \"--glob\",\n    \"*.mjs\",\n    \"--glob\",\n    \"instructions.md\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/removal-stage-tests.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/removal-stage-tests.json",
      "sha256": "39f315b0dac09cd075477bd1fd1381ad80d1494c3a116cb4284fc7e7edef1477",
      "bytes": 433,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"cmd\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) supported request and all production callers preserve existing output [0.06ms]\\n\\n 1 pass\\n 0 fail\\n 2 expect() calls\\nRan 1 test across 1 file. [5.00ms]\\n\"\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/review-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/review-diff.json",
      "sha256": "10284bc1e00cf7bc8d864e026ce1230e2ed2d2489a807ca5d00ff3c513485b4e",
      "bytes": 2001,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"cmd\": [\n    \"diff\",\n    \"-ru\",\n    \"../input\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru ../input/contract.test.mjs ./contract.test.mjs\\n--- ../input/contract.test.mjs\\t2026-10-16 10:49:12\\n+++ ./contract.test.mjs\\t2026-10-16 10:51:18\\n@@ -5,3 +5,9 @@\\n   expect(supportedRequest({ id: 'r1' })).toEqual({ id: 'r1', status: 'accepted' });\\n   expect(submit('r2')).toEqual({ id: 'r2', status: 'accepted' });\\n });\\n+\\n+test('optional note preserves literal values and omission', () => {\\n+  expect(supportedRequest({ id: 'r1' })).toEqual({ id: 'r1', status: 'accepted' });\\n+  expect(supportedRequest({ id: 'r1', note: 'hello' })).toEqual({ id: 'r1', status: 'accepted', note: 'hello' });\\n+  expect(supportedRequest({ id: 'r1', note: '' })).toEqual({ id: 'r1', status: 'accepted', note: '' });\\n+});\\nOnly in ../input: duplicate-reference.md\\ndiff -ru ../input/handler.mjs ./handler.mjs\\n--- ../input/handler.mjs\\t2026-10-16 10:49:12\\n+++ ./handler.mjs\\t2026-10-16 10:51:18\\n@@ -1,6 +1,3 @@\\n-function redundantValid(request) { return request && typeof request === 'object' && typeof request.id === 'string'; }\\n-export function obsoleteRequest(request) {\\n-  if (!redundantValid(request)) throw new Error('invalid');\\n-  return { id: request.id, obsolete: true };\\n+export function supportedRequest(request) {\\n+  return { id: request.id, status: 'accepted', ...(request.note !== undefined ? { note: request.note } : {}) };\\n }\\n-export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\\ndiff -ru ../input/instructions.md ./instructions.md\\n--- ../input/instructions.md\\t2026-10-16 10:49:12\\n+++ ./instructions.md\\t2026-10-16 10:51:18\\n@@ -1 +1 @@\\n-Use the supported request handler. Use the supported request handler for requests. Read duplicate-reference.md for the same instruction.\\n+Use the supported request handler.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/shared-input-integrity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/shared-input-integrity.json",
      "sha256": "e37866d02d387e5382512697cfe089114ea7f32d9f9bdef8853caf1bc9c8974d",
      "bytes": 1395,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"dead-path/acceptance.json\": {\n    \"before\": \"1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34\",\n    \"after\": \"1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34\"\n  },\n  \"dead-path/scope.md\": {\n    \"before\": \"d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528\",\n    \"after\": \"d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528\"\n  },\n  \"dead-path/contract.test.mjs\": {\n    \"before\": \"0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357\",\n    \"after\": \"0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357\"\n  },\n  \"dead-path/caller.mjs\": {\n    \"before\": \"1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931\",\n    \"after\": \"1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931\"\n  },\n  \"dead-path/handler.mjs\": {\n    \"before\": \"a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6\",\n    \"after\": \"a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6\"\n  },\n  \"dead-path/duplicate-reference.md\": {\n    \"before\": \"0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974\",\n    \"after\": \"0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974\"\n  },\n  \"dead-path/instructions.md\": {\n    \"before\": \"d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228\",\n    \"after\": \"d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228\"\n  }\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/supplied-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/evidence/supplied-case.json",
      "sha256": "60fab8bbb08f233aa3d3f2e9bdcb2d55ffd64004554a03c698b8380c1be19378",
      "bytes": 1873,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "{\n  \"id\": \"dead-path\",\n  \"sourcePaths\": [\n    \"skills/principle-subtract-before-you-add/SKILL.md\"\n  ],\n  \"prompt\": \"Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\",\n  \"requirements\": [\n    \"Available source and observed usage\",\n    \"Authorization and write capability for changes\",\n    \"Execution capability for actual checks\"\n  ],\n  \"expectedFull\": \"Inspect actual usage and requirements, remove obsolete behavior before constructing the replacement, and show the sequence and observed checks. Cut before polishing, preserve required behavior, avoid speculative edge cases, validators, parsers and guards, simplify redundant prompts, and delete empty references rather than leaving stubs. Leave the design simpler and more capable behind the same or smaller interface.\",\n  \"expectedReduced\": \"With source available but writes or execution unavailable, provide an ordered removal and replacement proposal as reduced capability. State which edits and checks were not performed.\",\n  \"expectedBlocked\": \"If source or required usage evidence is unavailable, state the missing inputs and block claims that deletion is safe or completed. Do not invent obsolete paths or usage.\",\n  \"forbiddenClaims\": [\n    \"Replacement constructed before obsolete behavior is removed\",\n    \"Deletion is safe without inspecting usage and required behavior\",\n    \"Unperformed edits or checks claimed complete\",\n    \"Speculative guards added beyond the specification\",\n    \"Host parity or metadata enforcement claimed from structural validation\"\n  ]\n}"
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/handler.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/removal-stage/handler.mjs",
      "sha256": "8e33a884b99b3be3c4d4c7f6c63e2c619b322d968b5f061bd155744b0b273db0",
      "bytes": 93,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\n"
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/contract.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work/contract.test.mjs",
      "sha256": "099c8db586d12197d2102bc31364acf1acb5faf2f602355b2523b53b2de96e8f",
      "bytes": 745,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { supportedRequest } from './handler.mjs';\nimport { submit } from './caller.mjs';\ntest('supported request and all production callers preserve existing output', () => {\n  expect(supportedRequest({ id: 'r1' })).toEqual({ id: 'r1', status: 'accepted' });\n  expect(submit('r2')).toEqual({ id: 'r2', status: 'accepted' });\n});\n\ntest('optional note preserves literal values and omission', () => {\n  expect(supportedRequest({ id: 'r1' })).toEqual({ id: 'r1', status: 'accepted' });\n  expect(supportedRequest({ id: 'r1', note: 'hello' })).toEqual({ id: 'r1', status: 'accepted', note: 'hello' });\n  expect(supportedRequest({ id: 'r1', note: '' })).toEqual({ id: 'r1', status: 'accepted', note: '' });\n});\n"
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/handler.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work/handler.mjs",
      "sha256": "dae0d0f662fd1d12fa639a7f52ac3a5af76dfc2d8518fbf8808aa87349b72fef",
      "bytes": 158,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "export function supportedRequest(request) {\n  return { id: request.id, status: 'accepted', ...(request.note !== undefined ? { note: request.note } : {}) };\n}\n"
    },
    {
      "path": "fixtures/rerun-01/dead-path.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path.result.md",
      "sha256": "805ac944293977aef8f0f307cb008dba4635f0385806f634323e12fb93922a97",
      "bytes": 5595,
      "owners": [
        "grades-native-rerun-01.json#1"
      ],
      "text": "# dead-path\n\n## Supplied input and scope\n\nReplace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\n\nRequirements supplied:\n\n- Available source and observed usage\n- Authorization and write capability for changes\n- Execution capability for actual checks\n\nPackage root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nUser-supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Installed files were read directly and copied into evidence/. The commit identity was supplied by the user, not independently established from an installed Git checkout. No 0.2.1 files were used.\n\nPrepared input root: /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v2/dead-path\n\ninput/ preserves all supplied case-specific files. evidence/supplied-case.json preserves the installed registered prompt, requirements and expected variants; evidence/registry-entry.json preserves its registry entry. The scenario-map and scope documents describe synthetic inert fixtures. They are not host receipts.\n\n## Actual response and output\n\nInspected handler.mjs, caller.mjs, contract.test.mjs, scope.md and both documentation files. The only production caller imports supportedRequest. obsoleteRequest is referenced only by its own definition, and redundantValid is used only by that function. The supplied complete synthetic scope declares the internal request boundary already validated and accepts removal.\n\nPerformed this order:\n\n1. Removed obsoleteRequest and redundantValid from the copied handler.\n2. Reduced instructions.md to one instruction and deleted duplicate-reference.md and its reference.\n3. Saved removal-stage/ before adding replacement behavior. Existing contract tests still passed, 1 test and 2 assertions. Source/documentation search for the removed names had no matches, exit 1.\n4. Added optional note passthrough to supportedRequest. Undefined omits the field; hello and the empty string retain their literal values. Added all three supplied acceptance cases as literal assertions. No new validator was added.\n5. Ran final contracts: 2 tests, 5 assertions, no failures. Reviewed evidence/review-diff.json. The public module now exports only supportedRequest; caller.mjs is unchanged.\n\n## Actual tools and artifacts\n\nUsed functions.exec with tools.exec_command to read instructions and fixtures, run Bun 1.4.2, and inspect saved output. Used tools.apply_patch to write the local Bun runners. run-cases.mjs uses Bun file reads, local filesystem copies/writes and Bun.spawnSync for rg, diff and bun test. No native workers are required by these direct workflows, and none were spawned.\n\nThe exact edited output is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-01/dead-path/work/. Original copies are in input/. Every command below has its argument array, working directory, exit code, stdout and stderr preserved in evidence/<name>.json. Diff exit 1 means differences found; rg exit 1 means no matches. Mutation test exit 1 is the observed deliberate defect.\n\n| Command artifact | Exit code |\n| --- | --- |\n| evidence/inventory-before.json | 0 |\n| evidence/baseline.json | 0 |\n| evidence/removal-stage-tests.json | 0 |\n| evidence/removal-stage-search.json | 1 |\n| evidence/final-tests.json | 0 |\n| evidence/review-diff.json | 1 |\n\nShared input SHA-256 values were compared before and after execution, with matching values in evidence/shared-input-integrity.json. The source-skill and support-file copies in evidence/ preserve the instructions actually used. review-diff.json records the reviewed combined changes.\n\n## Variants attempted and limits\n\nThe full source/write/execution variant ran on the real host. The following conditional capability branches were exercised as explicit response-only simulations, also saved in evidence/reduced-variants.json. The host does not enforce those negative conditions here. These narratives do not establish denied-tool handling or isolated executions under unavailable capabilities.\n\n- source available, writes withheld: With source available and writes withheld, propose: inventory all handlers and imports; remove obsoleteRequest and redundantValid; simplify the repeated instruction and delete duplicate-reference.md; only then add optional note passthrough and all literal acceptance cases. No removal or replacement is performed under this simulated restriction.\n\n- execution withheld: With execution withheld, inspect the ordered removal snapshot and final diff but report both intermediate and final test execution unobserved for this variant. Run bun test contract.test.mjs at each stage after execution becomes available.\n\n- missing source or applicability evidence: Without source or required usage evidence, do not label the path obsolete or deletion safe. Obtain handler, caller, contract and scope files before making removal claims.\n\nNo live service was contacted. No external account writes, issues, PRs, messages, commits, pushes, publishing, credential or configuration changes, installs or schedules were performed. No prior result files were overwritten. No host parity, metadata enforcement, independent review or package release validation is claimed. No self-assigned case grade is supplied.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-01/dead-path/fixture/README.md",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/dashboard.mjs",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/forge.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/history.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/invoice.mjs",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/orders.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/runtime.mjs",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-01/dead-path/input.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/dead-path/source",
      "owner": "grades-native-00-01.json#12",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/dead-path/source-manifest.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/README.md",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/dashboard.mjs",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/forge.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/history.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/invoice.mjs",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/orders.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-01/dead-path/fixture/runtime.mjs",
      "owner": "grades-native-00-01.json#12",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-01/dead-path/input.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/dead-path/source",
      "owner": "grades-native-00-01.json#12",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/dead-path/source-manifest.json",
      "owner": "grades-native-00-01.json#12",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/references__host-capabilities.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/scenario-map.json",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/skills__principle-subtract-before-you-add__SKILL.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/skills__unslop__SKILL.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/input",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/acceptance.json",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/caller.mjs",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/contract.test.mjs",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/contract.test.mjs",
      "sha256": "0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357",
      "bytes": 370
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/instructions.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/scope.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/acceptance.json",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/caller.mjs",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/instructions.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/scope.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/references__host-capabilities.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/scenario-map.json",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/skills__principle-subtract-before-you-add__SKILL.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/evidence/skills__unslop__SKILL.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-01/dead-path/input",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/acceptance.json",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/caller.mjs",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/contract.test.mjs",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/contract.test.mjs",
      "sha256": "0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357",
      "bytes": 370
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/instructions.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/rerun-01/dead-path/removal-stage/scope.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/acceptance.json",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/caller.mjs",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/instructions.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/rerun-01/dead-path/work/scope.md",
      "owner": "grades-native-rerun-01.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
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
