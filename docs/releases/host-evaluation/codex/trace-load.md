# codex: trace-load

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "trace-load",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-rerun-03.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.",
  "caseDefinition": {
    "id": "trace-load",
    "sourcePaths": [
      "skills/principle-minimize-reader-load/SKILL.md"
    ],
    "prompt": "Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.",
    "requirements": [
      "Read source and callers; writes and execution require available tools and authorization.",
      "Inspect both layers to trace and state to hold.",
      "Preserve meaningful abstraction boundaries and invariants."
    ],
    "expectedFull": "Inspect the concrete path and caller evidence. Collapse unnecessary one-caller and pass-through layers, keep boundaries that hide meaningful decisions, derive total from rows in a pure function or smaller state scope, and name the invariant once at the boundary. Explain where total comes from and what can change it. Verify authorized edits with observed checks; treat the under-30-second reader test as a criterion unless actually measured.",
    "expectedReduced": "With readable source but unavailable or denied writes or execution, give a source-grounded ordered proposal that reduces trace layers and hidden state. State which edits or checks were not performed and preserve permission limits.",
    "expectedBlocked": "Without readable source or sufficient caller and state evidence, identify the missing access or evidence and stop concrete refactoring and completion claims.",
    "forbiddenClaims": [
      "A structural validator pass proves host behavior or a measured reader time.",
      "Fewer lines alone prove reduced reader load.",
      "All abstraction layers should be removed regardless of interface compression.",
      "Unavailable writes or execution succeeded.",
      "Preserved invocation metadata proves host enforcement."
    ],
    "caseFile": "docs/parity/cases/skills/principle-minimize-reader-load.json"
  },
  "registry": {
    "caseId": "trace-load",
    "caseFile": "docs/parity/cases/skills/principle-minimize-reader-load.json",
    "sourcePaths": [
      "skills/principle-minimize-reader-load/SKILL.md"
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
      "attemptId": "grades-native-05.json#2",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "trace-load",
      "status": "fail",
      "grade": {
        "caseId": "trace-load",
        "host": "codex",
        "status": "fail",
        "execution": "direct",
        "rawTrace": "codex/batch-05.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_9",
          "item_18"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Required pure total derivation or smaller state scope not implemented."
        ],
        "review": "Actual refactor removes two forwarding modules, preserves outputs and explains all total/cache mutations. However calculate still writes same module-global cachedTotal and no pure derivation or smaller state scope is implemented. This misses the expected-full hidden-state requirement with source/write/execution available. Honest disclosure prevents a fabricated result but does not satisfy required refactor.",
        "responseArtifact": "fixtures/batch-05/trace-load.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [
          "Evaluation execution: preserve inspectCachedTotal observable contract while extracting pure total derivation and making cache update boundary explicit, then rerun before/after behavior. Existing principle already requests reduced state burden."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-05.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Inspect the concrete path and caller evidence. Collapse unnecessary one-caller and pass-through layers, keep boundaries that hide meaningful decisions, derive total from rows in a pure function or smaller state scope, and name the invariant once at the boundary. Explain where total comes from and what can change it. Verify authorized edits with observed checks; treat the under-30-second reader test as a criterion unless actually measured.",
        "reducedExpected": "With readable source but unavailable or denied writes or execution, give a source-grounded ordered proposal that reduces trace layers and hidden state. State which edits or checks were not performed and preserve permission limits."
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
        "text": "# trace-load\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"trace-load\",\n  \"prompt\": \"Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Read source and callers; writes and execution require available tools and authorization.\",\n    \"Inspect both layers to trace and state to hold.\",\n    \"Preserve meaningful abstraction boundaries and invariants.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe copied controller now calls calculate(invoice.rows) directly. I removed facade.mjs and adapter.mjs after reading all supplied invoice sources and their imports. Both forwarding layers had one supplied caller and made no decisions. Calculator still owns numeric calculation; formatter and exporter contracts are unchanged.\n\nThe returned total is rows.reduce((total,row) => total + row.qty * row.unitPrice, 0). Changing a row's qty or unitPrice, adding or removing rows, or replacing rows changes the next calculation. Mutating rows alone does not change an already returned controller result or the cached number. Calling either calculate or invoiceController overwrites the cache. A fresh module instance starts its cache at zero. The existing result object contains a number snapshot, not a live binding. A caller can also mutate its own returned object, independently of the cache.\n\nMinimize Reader Load removed two trace layers. I retained cachedTotal because inspectCachedTotal exposes it, and the supplied decision record explicitly names its observable contract. The probe exercises that accessor after controller and direct calculator calls. Removing the cache would require a changed accessor contract or moving its ownership to an explicit instance; I did not silently remove the export. Thus hidden module state remains a documented limitation of this scoped refactor. No reader completion time was measured.\n\nBefore and after probes both returned totals 6, 9.25, 17 and 0 on the selected paths. They checked that earlier result snapshots stay unchanged, missing rows still throw, and formatter results remain 0.00, 1.00, -1.00 and 12.35. Empty formatting remains [], and NaN and Infinity still throw nonfinite. These are local fixture observations only.\n\n## Variants attempted and limits\n\nOriginal copied modules were executed before editing; migrated modules were executed after editing. Cache and display-contract behavior were checked. Source-unavailable and write-denied branches were unnecessary because those capabilities worked.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\".\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before\"] | 0 | [trace-load/callers-before.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/callers-before.json) |\n| [\"diff\",\"-ru\",\"before\",\"work\"] | 1 | [trace-load/diff.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/diff.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"work\"] | 0 | [trace-load/after.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/after.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"before\"] | 0 | [trace-load/baseline.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/baseline.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### after.json\n\nExit 0.\n\n```text\n{\"first\":{\"total\":6},\"afterMutation\":9.25,\"afterDirectCalculate\":17,\"empty\":0,\"formatted\":[\"0.00\",\"1.00\",\"-1.00\",\"12.35\"],\"nonfinite\":\"throws nonfinite\",\"missingRows\":\"TypeError\"}\n\n```\n\n### baseline.json\n\nExit 0.\n\n```text\n{\"first\":{\"total\":6},\"afterMutation\":9.25,\"afterDirectCalculate\":17,\"empty\":0,\"formatted\":[\"0.00\",\"1.00\",\"-1.00\",\"12.35\"],\"nonfinite\":\"throws nonfinite\",\"missingRows\":\"TypeError\"}\n\n```\n\n",
        "artifact": {
          "path": "fixtures/batch-05/trace-load.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load.result.md",
          "sha256": "cd2af3226b519e9dc50f6f4f0d7a8733e5986937c2af0c7178510638d4330527",
          "bytes": 6446
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
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "0e1c174a01a24d51c3dab280caceff344af0fefc6a644c6b97d10af9eeb71a02"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8a2b73027e46ae006ea751859775e7b3f6b53099dbe51f5b2d2e50874664d426",
                "commandResult": {
                  "exitCode": 0
                }
              },
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
                "eventId": "item_18",
                "line": 34,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "efa76720dfe3a51901c606b1ad43073218ec7b8edbbcce7870ba1d1e0affda10"
              },
              {
                "eventId": "item_18",
                "line": 35,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "daf33dfe6a92e6e8d9a399e9e75461540f72f6a3e3cc13a4a36b7a56511f7816",
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
            "item_5",
            "item_9",
            "item_18"
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
    },
    {
      "attemptId": "grades-native-rerun-03.json#0",
      "order": 103,
      "gradeFile": "grades-native-rerun-03.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "trace-load",
      "status": "pass",
      "grade": {
        "schemaVersion": 1,
        "caseId": "trace-load",
        "host": "codex",
        "attempt": "rerun-03",
        "status": "pass",
        "execution": "direct",
        "rawTrace": "codex/rerun-03.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_7",
          "item_8",
          "item_9",
          "item_20",
          "item_23"
        ],
        "actualExecutionEventIds": [
          "item_12",
          "item_14",
          "item_15",
          "item_16",
          "item_19"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Actual after source exports sumRows as a pure left-to-right Number reduction; calculate explicitly owns compatibility cache update. Controller directly calls calculate and forwarding modules are removed. Pure helper no-cache-mutation is genuinely asserted. Original and edited behavior each execute before/after with20recorded observations and byte-equivalent comparison exit0. Direct calculate, cached snapshot semantics, unchanged cache after exceptions, NaN/Infinity/coercion/sparse rows, existing formatter and CSV/public-symbol behavior preserved. Retaining inspectCachedTotal compatibility does not prevent satisfying pure derivation requirement. No measured reader-time claim.",
        "responseArtifact": "fixtures/rerun-03/trace-load.result.md",
        "evidence": [
          "fixtures/rerun-03/trace-load/after/calculator.mjs",
          "fixtures/rerun-03/trace-load/after/controller.mjs",
          "fixtures/rerun-03/trace-load/check.mjs",
          "fixtures/rerun-03/trace-load/evidence/baseline.json",
          "fixtures/rerun-03/trace-load/evidence/refactored.json",
          "fixtures/rerun-03/trace-load/evidence/compare.json",
          "fixtures/rerun-03/trace-load/evidence/audit.json",
          "fixtures/rerun-03/trace-load/evidence/patch.json"
        ],
        "variantReview": [
          "Original7-file source executed before edits.",
          "Single after implementation executed and compared.",
          "Pure-only-cache-removal/inline-controller alternatives rejected conceptually to preserve observable cache API, not claimed executed.",
          "Existing formatter alternatives belong to separate case, not falsely implemented here."
        ],
        "priorAttempt": {
          "artifact": "grades-native-05.json",
          "status": "fail",
          "retained": true,
          "reason": "Original attempt removed forwarding layers but did not implement required pure derivation/smaller state scope. New attempt corrects that omission."
        },
        "limits": [
          "Under30second reader test remains criterion, not measured.",
          "External unknown caller compatibility unproved; supplied complete fixture and consumers checked.",
          "Installed source version0.1.0 and read-byte hashes observed; source freeze remains supplied commit identity.",
          "No worker needed for direct refactor; no independent review/metadata enforcement claimed."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-rerun-03.json",
            "reviewedBy": "grade_contract_audit independent source/trace/outcome reviewer"
          }
        ],
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "attempt": "rerun-03",
        "limits": [
          "Under30second reader test remains criterion, not measured.",
          "External unknown caller compatibility unproved; supplied complete fixture and consumers checked.",
          "Installed source version0.1.0 and read-byte hashes observed; source freeze remains supplied commit identity.",
          "No worker needed for direct refactor; no independent review/metadata enforcement claimed."
        ]
      },
      "response": {
        "text": "# trace-load native execution record\n\n## Actual response\n\nThe original total comes from controller.mjs calling invoiceFacade(invoice), then invoiceAdapter(invoice), then calculate(invoice.rows). Each wrapper has one caller in the supplied invoice source. The facade forwards the invoice unchanged; the adapter selects rows. Neither hides a separate policy or implementation. The broader shared-fixture search is retained in evidence/callers.json. It also finds a separate shared/invoice.mjs fixture, which is not imported by this concrete path and was not edited.\n\nIn the case-owned after/ copy, the controller calls calculate(invoice.rows) directly. The facade and adapter files were removed. The controller still constructs { total }, and calculate remains the boundary for the observable calculator cache. sumRows is now a pure derivation. The one invariant comment at that derivation states that total is the left-to-right JavaScript Number sum of qty * unitPrice starting at 0. There is no rounding, decimal arithmetic replacement, finite-number validation, or coercion change here.\n\nChanges to qty, unitPrice, row membership, or row order can change the next result. JavaScript floating-point addition makes order relevant. A successful calculate call, including a controller call, replaces the module cache. Mutating rows alone does not refresh the cache or an already-returned total. An exception during reduction leaves the previous cache intact. NaN and Infinity propagate through calculation. Calling sumRows alone does not update the cache. No invoice.total input field is read or mutated.\n\nThe original path requires tracing four modules; the new path uses two modules. The extra pure function is next to calculate in calculator.mjs. The cache remains because inspectCachedTotal exposes it. Removing that state would change the supplied observable API. Readers still need to understand this one module-scoped value when using the inspection API. Fewer files are a structural observation, not a measured comprehension improvement.\n\nThe decision record describes a UI comparing two-decimal strings and the CSV consumer importing formatRows. The supplied exporter confirms the latter; no UI implementation or customer ticket was supplied. Formatter rounding, error behavior, names, public symbol strings, and the unrelated sort defect remain unchanged. The actual controller does not invoke the formatter, so the record's statement about formatter errors propagating through a controller cannot be exercised as a connected path in this source. Formatter errors were checked directly.\n\n## Variants and boundaries\n\n1. Original seven-file fixture, copied to before/ and executed before edits.\n2. One implemented refactor in after/: remove facade and adapter; retain calculate and inspectCachedTotal; extract pure sumRows. Executed and compared to baseline. No other implementation variant was attempted or failed.\n\nA pure-only calculator with a removed cache was considered and rejected because cache inspection is observable. Inlining calculation into the controller was rejected because direct calculate and inspection form a meaningful compatibility boundary. These were design alternatives, not executed variants.\n\nThe decision record's formatter alternatives A and B belong to a different refactor. Conceptually A removes hidden lastFormatted state and the fixed pass-through, while B adds instance ownership and lifecycle questions without a supplied need. Either would require its own equivalence checks. Neither was implemented here, and formatInvoice was not renamed.\n\n## Observed checks\n\nBaseline and edited runs each saved 20 observations. Their files compare byte-for-byte with diff exit 0. Checks cover empty and mixed rows, row mutation before recalculation, direct calculate, missing rows, null row, throwing getter, unchanged cache on errors, NaN, Infinity, binary floating arithmetic, existing numeric-string coercion, and sparse rows. The edited run additionally asserts pure sumRows leaves the cache untouched. This assertion succeeded but adds no synthetic baseline observation.\n\nBefore edits, observed display results were 0 -> \"0.00\", 1.005 -> \"1.00\", -1.005 -> \"-1.00\", and 12.345 -> \"12.35\". NaN and Infinity each threw Error('nonfinite'); empty formatRows returned []; empty export returned an empty string. Both runs exercised CSV output, exported symbol strings, and the existing lexical sort behavior. These are observed local Bun checks, not expectations copied into a completion receipt.\n\nThe audit confirmed that all seven before/ files still equal the read-only inputs, and that formatter.mjs, exporter.mjs, and decision.md also remain byte-identical in after/. Four retained installed package files match live installed source. SHA-256 values are in evidence/input-hashes.json. The patch command exits 1 because differences exist, which is the normal diff result. It is not a failed test.\n\n## Host, provenance and incomplete parts\n\nExecution used the actual exposed functions.exec wrapper and tools.exec_command binding on this host. Edits used tools.apply_patch and Bun filesystem operations within the authorized root. No worker was required or spawned. No external actions, installs, configuration changes, commits, pushes, schedules, or changes to shared input or installed package were performed.\n\nThe requested source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The exact installed path was read, and plugin.json reports version 0.1.0. Git revision discovery failed with exit 128 because the installed directory has no Git repository. Thus commit provenance remains user-supplied and is not independently verified. Snapshot hashes identify the bytes actually used. The skill's disable-model-invocation metadata is retained as source metadata, with no claim that this host enforces it.\n\nThe under-30-second reader test remains a criterion. No new reader was timed. No structural validator, release claim, grading label, or proxy success receipt was created. Behavioral checks cover the supplied fixture and selected cases; they do not establish unknown external caller compatibility. No independent outcome reviewer was invoked.\n\nThe writable root was empty at initial ls -la, so no previous incomplete output was present there to overwrite. No previous transcript or external retained output was located, modified, or used. This record does not claim to recover it.\n\n## Artifacts\n\nAll paths below are relative to /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/.\n\n- before/: all seven unchanged invoice inputs, including the actual decision.\n- after/: edited concrete implementation and unchanged display consumers.\n- installed-source/: exact requested skill, host capability guidance, case contract, and plugin manifest.\n- check.mjs: executed behavioral checks; run.mjs: captures exact command arguments, stdout, stderr and exit status.\n- audit.mjs: source preservation and hash checks; write-report.mjs: this report generator.\n- evidence/: raw command records, baseline and edited observations, patch output and input hashes.\n\n## Discovery and write log\n\nInitial read-only discovery used tools.exec_command before the persistent command recorder existed. The shell invocations read pwd, rg --files for AGENTS.md, trace-load and result files, ls -la of the root and shared invoice directory, all seven invoice files with cat, the exact installed SKILL.md, host-capabilities.md, unslop/SKILL.md, scenario-map.json, case JSON and plugin.json. All returned exit 0. The first rg produced no matches and the initial root listing contained only . and ... Ancestor AGENTS.md checks from / through the writable root and checks at shared/, additional/ and invoice/ printed no instruction files. Source contents are retained in before/ and installed-source/ and in the source-read command record below. The provided user AGENTS instructions governed the work.\n\nThe initial caller search and Bun version check returned matches and 1.4.2. The first git rev-parse failed with 'fatal: not a git repository (or any of the parent directories): .git'; the compound shell command returned 0 because its final bun --version succeeded. The isolated retry below records the actual Git exit 128. No failed freeze discovery is treated as verification.\n\nThe copy command ran via bun -e with node:fs/promises mkdir/cp. It copied the complete seven-file invoice directory into before/ and after/ before edits, then copied the four installed source files. Exit 0, output: 'Copied all 7 invoice inputs unchanged into before/ and after/; retained exact installed source and contract.' The later audit independently checked these copies. tools.apply_patch then created check.mjs and run.mjs, edited only after/controller.mjs and after/calculator.mjs, deleted only after/facade.mjs and after/adapter.mjs, and created audit.mjs and this report generator. Each apply_patch returned successfully with {}. No permission denial or alternate implementation retry occurred.\n\nThe following records contain the exact recorded command arguments, outputs and individual exit statuses. The source-read tool display was truncated, but its complete stdout is saved in evidence/source-read.json. Report generation is run as bun trace-load/write-report.mjs and prints its saved path; a final readback checks report persistence and lists artifacts.\n\n### after-observations.json\n\n```json\n[\n  {\n    \"label\": \"empty\",\n    \"total\": 0,\n    \"cache\": 0\n  },\n  {\n    \"label\": \"mixed rows\",\n    \"total\": 20,\n    \"cache\": 20\n  },\n  {\n    \"label\": \"before row mutation\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"mutation alone leaves cache unchanged\",\n    \"cache\": 6\n  },\n  {\n    \"label\": \"recalculation after mutation\",\n    \"total\": 12,\n    \"cache\": 12\n  },\n  {\n    \"label\": \"missing rows\",\n    \"error\": \"TypeError\",\n    \"message\": \"undefined is not an object (evaluating 'rows.reduce')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"null row\",\n    \"error\": \"TypeError\",\n    \"message\": \"null is not an object (evaluating 'row.qty')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"throwing getter\",\n    \"error\": \"Error\",\n    \"message\": \"row failure\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"NaN propagates\",\n    \"total\": \"NaN\",\n    \"cache\": \"NaN\"\n  },\n  {\n    \"label\": \"Infinity propagates\",\n    \"total\": \"Infinity\",\n    \"cache\": \"Infinity\"\n  },\n  {\n    \"label\": \"floating arithmetic\",\n    \"total\": 0.30000000000000004,\n    \"cache\": 0.30000000000000004\n  },\n  {\n    \"label\": \"existing coercion\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"sparse array\",\n    \"total\": 4,\n    \"cache\": 4\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 0,\n    \"result\": \"0.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 1.005,\n    \"result\": \"1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": -1.005,\n    \"result\": \"-1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 12.345,\n    \"result\": \"12.35\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"NaN\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"Infinity\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"display consumers\",\n    \"emptyRows\": [],\n    \"emptyExport\": \"\",\n    \"csv\": \"1.00\\n-1.00\",\n    \"symbols\": [\n      \"formatInvoice\",\n      \"formatRows\"\n    ],\n    \"unrelatedSort\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n```\n\n### audit.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"trace-load/audit.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"All 7 original invoice inputs match shared source; formatter, exporter and decision are unchanged in after/. All 4 retained installed files match their sources. SHA-256 manifest saved.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### baseline.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"trace-load/check.mjs\",\n    \"before\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"before: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; 20 observations saved.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### before-observations.json\n\n```json\n[\n  {\n    \"label\": \"empty\",\n    \"total\": 0,\n    \"cache\": 0\n  },\n  {\n    \"label\": \"mixed rows\",\n    \"total\": 20,\n    \"cache\": 20\n  },\n  {\n    \"label\": \"before row mutation\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"mutation alone leaves cache unchanged\",\n    \"cache\": 6\n  },\n  {\n    \"label\": \"recalculation after mutation\",\n    \"total\": 12,\n    \"cache\": 12\n  },\n  {\n    \"label\": \"missing rows\",\n    \"error\": \"TypeError\",\n    \"message\": \"undefined is not an object (evaluating 'rows.reduce')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"null row\",\n    \"error\": \"TypeError\",\n    \"message\": \"null is not an object (evaluating 'row.qty')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"throwing getter\",\n    \"error\": \"Error\",\n    \"message\": \"row failure\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"NaN propagates\",\n    \"total\": \"NaN\",\n    \"cache\": \"NaN\"\n  },\n  {\n    \"label\": \"Infinity propagates\",\n    \"total\": \"Infinity\",\n    \"cache\": \"Infinity\"\n  },\n  {\n    \"label\": \"floating arithmetic\",\n    \"total\": 0.30000000000000004,\n    \"cache\": 0.30000000000000004\n  },\n  {\n    \"label\": \"existing coercion\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"sparse array\",\n    \"total\": 4,\n    \"cache\": 4\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 0,\n    \"result\": \"0.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 1.005,\n    \"result\": \"1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": -1.005,\n    \"result\": \"-1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 12.345,\n    \"result\": \"12.35\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"NaN\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"Infinity\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"display consumers\",\n    \"emptyRows\": [],\n    \"emptyExport\": \"\",\n    \"csv\": \"1.00\\n-1.00\",\n    \"symbols\": [\n      \"formatInvoice\",\n      \"formatRows\"\n    ],\n    \"unrelatedSort\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n```\n\n### callers.json\n\n```json\n{\n  \"command\": [\n    \"rg\",\n    \"-n\",\n    \"invoiceController|invoiceFacade|invoiceAdapter|inspectCachedTotal|calculate\\\\(|calculator.mjs|facade.mjs|adapter.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/decision.md:7:Authorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs:1:import { invoiceFacade } from './facade.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs:2:export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs:1:import { invoiceAdapter } from './adapter.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs:2:export function invoiceFacade(invoice) { return invoiceAdapter(invoice); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs:1:import { calculate } from './calculator.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs:2:export function invoiceAdapter(invoice) { return calculate(invoice.rows); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs:2:export function calculate(rows) {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs:6:export function inspectCachedTotal() { return cachedTotal; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs:1:export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs:2:export function adapter(invoice){return calculate(invoice.rows)}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:15:      \\\"invoice/facade.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:16:      \\\"invoice/adapter.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:17:      \\\"invoice/calculator.mjs\\\"\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:21:      \\\"invoice/facade.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:22:      \\\"invoice/adapter.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:23:      \\\"invoice/calculator.mjs\\\"\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:27:      \\\"invoice/calculator.mjs\\\",\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### compare.json\n\n```json\n{\n  \"command\": [\n    \"diff\",\n    \"-u\",\n    \"trace-load/evidence/before-observations.json\",\n    \"trace-load/evidence/after-observations.json\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### freeze.json\n\n```json\n{\n  \"command\": [\n    \"git\",\n    \"-C\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n```\n\n### input-hashes.json\n\n```json\n[\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs\",\n    \"sha256\": \"1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/exporter.mjs\",\n    \"sha256\": \"b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs\",\n    \"sha256\": \"a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs\",\n    \"sha256\": \"6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs\",\n    \"sha256\": \"90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/decision.md\",\n    \"sha256\": \"324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/formatter.mjs\",\n    \"sha256\": \"405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-minimize-reader-load/SKILL.md\",\n    \"sha256\": \"8684154522048e9e5723f559a5ba9ecfcca87d551a76b9cd2ecd8668b48ccf90\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/host-capabilities.md\",\n    \"sha256\": \"f0f09ce28b6feca4d72694d5687204dc074aa58dade9a0ab59656da3bfa1bd20\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/parity/cases/skills/principle-minimize-reader-load.json\",\n    \"sha256\": \"37ec090c179ff6255160e73f18ed62730bfe9308c1c4a967ff57cfd8114858bc\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/plugin.json\",\n    \"sha256\": \"08119bdaf450eb34ad2a35c0685ac0d5795c45c4101b09bef41bc0ab8fe55cc7\"\n  }\n]\n```\n\n### patch.json\n\n```json\n{\n  \"command\": [\n    \"diff\",\n    \"-ru\",\n    \"trace-load/before\",\n    \"trace-load/after\"\n  ],\n  \"exitCode\": 1,\n  \"stdout\": \"Only in trace-load/before: adapter.mjs\\ndiff -ru trace-load/before/calculator.mjs trace-load/after/calculator.mjs\\n--- trace-load/before/calculator.mjs\\t2026-10-16 11:12:02\\n+++ trace-load/after/calculator.mjs\\t2026-10-16 11:12:49\\n@@ -1,6 +1,10 @@\\n let cachedTotal = 0;\\n+// Total is the left-to-right JavaScript Number sum of qty * unitPrice, starting at 0.\\n+export function sumRows(rows) {\\n+  return rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n+}\\n export function calculate(rows) {\\n-  cachedTotal = rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n+  cachedTotal = sumRows(rows);\\n   return cachedTotal;\\n }\\n export function inspectCachedTotal() { return cachedTotal; }\\ndiff -ru trace-load/before/controller.mjs trace-load/after/controller.mjs\\n--- trace-load/before/controller.mjs\\t2026-10-16 11:12:02\\n+++ trace-load/after/controller.mjs\\t2026-10-16 11:12:49\\n@@ -1,2 +1,2 @@\\n-import { invoiceFacade } from './facade.mjs';\\n-export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n+import { calculate } from './calculator.mjs';\\n+export function invoiceController(invoice) { return { total: calculate(invoice.rows) }; }\\nOnly in trace-load/before: facade.mjs\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### refactored.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"trace-load/check.mjs\",\n    \"after\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"after: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; 20 observations saved.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### runtime.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### source-read.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"-e\",\n    \"for (const path of [\\\"trace-load/installed-source/SKILL.md\\\",\\\"trace-load/installed-source/host-capabilities.md\\\",\\\"trace-load/installed-source/case.json\\\",...(await Array.fromAsync(new Bun.Glob(\\\"trace-load/before/*\\\").scan(\\\".\\\"))).sort()]) { console.log(JSON.stringify({path,content:await Bun.file(path).text()})); }\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"path\\\":\\\"trace-load/installed-source/SKILL.md\\\",\\\"content\\\":\\\"---\\\\nname: principle-minimize-reader-load\\\\ndescription: \\\\\\\"Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.\\\\\\\"\\\\ndisable-model-invocation: true\\\\n---\\\\n\\\\n# Minimize Reader Load\\\\n\\\\nMaintainability is the work a reader must do to understand code. Track two axes:\\\\n1. **Layers to trace.** How many indirections sit between the question and the answer.\\\\n2. **State to hold.** How much hidden or mutable context the reader must keep in their head.\\\\n\\\\n**Why:** Code is read far more than it is written. LOC, cyclomatic complexity, and \\\\\\\"clean architecture\\\\\\\" are proxies. Reader load is the thing that matters. The two axes are independent. A flat file with 50 globals can be as hard to reason about as a 6-layer adapter stack. Guard both. This is the human analog of [Guard the Context Window](../principle-guard-the-context-window/SKILL.md). Working memory is finite for readers too.\\\\n\\\\n**The pattern:**\\\\n- **Collapse layers** that cost more than they save: wrappers with one caller, adapters with no second implementation, speculative indirection that was never needed. Inline them.\\\\n- **Make adjacent layers change the abstraction.** A layer that repeats the same methods and arguments adds reader load without compression. Collapse pass-through layers.\\\\n- **Demand interface compression.** A broad interface that hides little complexity makes readers learn both the surface and the implementation. Prefer boundaries that hide meaningful decisions.\\\\n- **Shrink state scope:** prefer pure functions (returns over mutations), locals over fields, fields over module state, and module state over globals. Derive instead of sync.\\\\n- **Name the invariant at the boundary,** not in every consumer, so the reader learns it once.\\\\n- Before adding a layer or a piece of state, ask: does this reduce reader load somewhere else by at least as much?\\\\n\\\\n**The test:** Can a new reader answer \\\\\\\"where does X come from?\\\\\\\" and \\\\\\\"what can change X?\\\\\\\" in under 30 seconds? If not, cut layers or cut state.\\\\n\\\\n## Session capabilities and permissions\\\\n\\\\nUse [host capabilities](../../references/host-capabilities.md) to discover available read, write and execution tools. Inspect the concrete path, its callers and mutable state before deciding which layers to collapse. Make edits only within the authorized task and available write permissions. Run appropriate checks only through observed execution tools.\\\\n\\\\nWhen source is readable but writes or execution are denied or unavailable, give a source-grounded proposal and identify the edits or checks you could not perform. Without source or sufficient caller and state evidence, report the missing evidence and stop concrete refactoring claims. Do not claim a measured reader time without observation. Preserve invocation metadata without assuming the host enforces it.\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/installed-source/host-capabilities.md\\\",\\\"content\\\":\\\"# Discover capabilities in the current session\\\\n\\\\nRead the tools exposed to this session before assigning work. Cached official-subagents.txt is documentation context; it proves no operation succeeded. Local agent configuration is not portable plugin configuration.\\\\n\\\\nRecord each binding as `{operation, tool, exposed, succeeded, evidence, limits}`. `tool` is the exact exposed identifier or null when absent. `succeeded` is true only after observing a result. Keep failed and unavailable bindings. Successful bindings become `successfulOperations` in host evidence, with a root-relative evidence file. The operation labels below describe purposes, never callable APIs.\\\\n\\\\n| Operation | Discovery and observation required |\\\\n| --- | --- |\\\\n| spawn | Find an exposed independent-worker operation; retain returned worker identity and exact assigned revision. |\\\\n| follow-up | Find the operation that sends input to that worker; observe acceptance by the same identity. |\\\\n| wait | Find the operation that waits for worker state; retain terminal or interrupted state. |\\\\n| inspect-result | Read the worker result and its referenced artifacts; a wait notification alone is insufficient. |\\\\n| stop | Observe cancellation or termination through the exposed operation. |\\\\n| read | Observe the requested file content through the available file tool. |\\\\n| isolated-write | Observe a write within the worker's assigned path and permissions. |\\\\n| history | Observe available prior turns or records; declare gaps explicitly. |\\\\n| execution | Observe command execution with exit status and output. |\\\\n| persistence | Write and read an authorized durable record; a claimed save is insufficient. |\\\\n| external-write | Record explicit authorization and action identity; inspect the result before replay. |\\\\n| resolve-ownership | Observe distinct owned paths before contested writes. |\\\\n| inspect-terminal | Observe the worker's terminal state after stop. |\\\\n| quarantine-artifacts | Observe partial artifacts withheld from integration. |\\\\n| inspect-prior-action | Read the interrupted action identity and prior outcome. |\\\\n| inspect-destination | Observe the destination state for that action identity. |\\\\n| safe-recovery | Observe explicitly authorized idempotent recovery after identity and destination inspection. |\\\\n\\\\nNo default API names are assigned here. Tool names differ by host and session. An exposed tool may still be denied or fail. Record requested and actual models only when observed; otherwise use `unknown`. A requested model never proves the actual model.\\\\n\\\\nA denied or unavailable operation blocks the branch that requires it. Sequential substitution for required independent work is reduced capability and uses `reduced-pass`; ordinary direct completion can fully pass. Missing persistence limits session pickup even when current work succeeds. Preserve user authorization and host permission boundaries through every fallback.\\\\n\\\\nWorker passes require observed spawn and result inspection. Each registry entry declares `requiredObservations` for `pass` and `reduced-pass`; tool observations need exposed bindings and existing evidence artifacts; native text observations use the separate reviewed native record below. Full cancellation requires stop, terminal inspection and artifact quarantine. Full persistence requires durable write and readback. Full interrupted-action recovery requires prior identity inspection, destination inspection, safe recovery, explicit external permission and a recorded prior action identity even when no external-write observation is listed.\\\\n\\\\nPermission checks follow performed operations. Isolated writes and persistence require granted writes. External writes and safe recovery require granted external permission and prior identity. Authorized read-only reductions may retain denied writes; their limits must preserve denied or unavailable permissions. Required observations remain applicable to those reductions.\\\\n\\\\nHost evidence is stored as object or array JSON files under `docs/parity/evidence/`. Required fields are defined by `docs/parity/evidence.schema.json`. Artifacts and operation evidence must be existing files inside the tested root. Test fixtures belong in `tests/` and prove validator behavior only.\\\\n\\\\nRun `python3 tools/validate_evidence.py --root . --commit <tested-package-commit>` through Bun, for example `bun -e 'const p=Bun.spawnSync([\\\\\\\"python3\\\\\\\",\\\\\\\"-B\\\\\\\",\\\\\\\"tools/validate_evidence.py\\\\\\\",\\\\\\\"--root\\\\\\\",\\\\\\\".\\\\\\\",\\\\\\\"--commit\\\\\\\",process.argv[1]],{env:{...process.env,PYTHONDONTWRITEBYTECODE:\\\\\\\"1\\\\\\\"}});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode)' <tested-package-commit>`. It reads every JSON record below the evidence directory, prints each error, and exits 1 for invalid records or 0 for valid records. An empty directory has no invalid records and supplies no behavioral evidence.\\\\n\\\\nThe required registry file in `docs/parity/case-registry.json` declares applicability. Missing or non-file registry, unknown case, structural-only entry or unlisted host rejects behavioral validation. Maintenance fixtures use a temporary copy of this registry; they cannot bypass applicability. Required hosts must receive observed evidence or explicit blocked records before release claims. Structural checks have no required host and cannot populate host status. Later producers propose task-owned entries; only the coordinator integrates them. Source paths select callers through the task 3 case contract. Case definitions alone leave host statuses `not-run`.\\\\n\\\\n## Direct completion and recorded observations\\\\n\\\\n`direct` means the task is completed in the current context. Restatement, supplied-text writing and complete installed discovery can pass directly. `sequential` is reserved for replacing a required independent method with sequential work and remains reduced. A text response has no invented callable tool. Record supplied input, the actual response and qualitative outcome review as `nativeObservations`, each with its existing listed evidence artifact and named reviewer. Their labels are `supplied-input`, `response` and `review-outcome`. The reviewer assesses the case's expected outcome; validation checks evidence relationships and does not decide prose quality.\\\\n\\\\nEach registry entry declares allowed execution modes and required permissions for each status. A grant is required for the performed action: worker spawn, command execution and stop need execution; isolated output or persistence needs writes; external actions need their separate permission and prior identity. Read-only discovery does not inherit an execution grant requirement. Tool observations still name an actually exposed tool and existing evidence. Native observations cannot claim tool discovery, worker identity or saved writes.\\\\n\\\\nFull Arena and Swarm results additionally provide `inputRevision` and a listed `methodReceipt` artifact. An exposed `inspect-method` operation must reference that receipt. Assignment operations name `assignmentId` and the corresponding inspected output. See the [structured method contract](orchestration-contract.md). All positive maintenance fixtures are synthetic; none is an observed host result.\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/installed-source/case.json\\\",\\\"content\\\":\\\"{\\\\n  \\\\\\\"id\\\\\\\": \\\\\\\"trace-load\\\\\\\",\\\\n  \\\\\\\"sourcePaths\\\\\\\": [\\\\n    \\\\\\\"skills/principle-minimize-reader-load/SKILL.md\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"prompt\\\\\\\": \\\\\\\"Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.\\\\\\\",\\\\n  \\\\\\\"requirements\\\\\\\": [\\\\n    \\\\\\\"Read source and callers; writes and execution require available tools and authorization.\\\\\\\",\\\\n    \\\\\\\"Inspect both layers to trace and state to hold.\\\\\\\",\\\\n    \\\\\\\"Preserve meaningful abstraction boundaries and invariants.\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"expectedFull\\\\\\\": \\\\\\\"Inspect the concrete path and caller evidence. Collapse unnecessary one-caller and pass-through layers, keep boundaries that hide meaningful decisions, derive total from rows in a pure function or smaller state scope, and name the invariant once at the boundary. Explain where total comes from and what can change it. Verify authorized edits with observed checks; treat the under-30-second reader test as a criterion unless actually measured.\\\\\\\",\\\\n  \\\\\\\"expectedReduced\\\\\\\": \\\\\\\"With readable source but unavailable or denied writes or execution, give a source-grounded ordered proposal that reduces trace layers and hidden state. State which edits or checks were not performed and preserve permission limits.\\\\\\\",\\\\n  \\\\\\\"expectedBlocked\\\\\\\": \\\\\\\"Without readable source or sufficient caller and state evidence, identify the missing access or evidence and stop concrete refactoring and completion claims.\\\\\\\",\\\\n  \\\\\\\"forbiddenClaims\\\\\\\": [\\\\n    \\\\\\\"A structural validator pass proves host behavior or a measured reader time.\\\\\\\",\\\\n    \\\\\\\"Fewer lines alone prove reduced reader load.\\\\\\\",\\\\n    \\\\\\\"All abstraction layers should be removed regardless of interface compression.\\\\\\\",\\\\n    \\\\\\\"Unavailable writes or execution succeeded.\\\\\\\",\\\\n    \\\\\\\"Preserved invocation metadata proves host enforcement.\\\\\\\"\\\\n  ]\\\\n}\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/adapter.mjs\\\",\\\"content\\\":\\\"import { calculate } from './calculator.mjs';\\\\nexport function invoiceAdapter(invoice) { return calculate(invoice.rows); }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/calculator.mjs\\\",\\\"content\\\":\\\"let cachedTotal = 0;\\\\nexport function calculate(rows) {\\\\n  cachedTotal = rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\\\n  return cachedTotal;\\\\n}\\\\nexport function inspectCachedTotal() { return cachedTotal; }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/controller.mjs\\\",\\\"content\\\":\\\"import { invoiceFacade } from './facade.mjs';\\\\nexport function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/decision.md\\\",\\\"content\\\":\\\"# Synthetic invoice decision record\\\\n\\\\nDisplay contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\\\\n\\\\nFixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatInvoice and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\\\\n\\\\nAuthorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/exporter.mjs\\\",\\\"content\\\":\\\"import { formatRows } from './formatter.mjs';\\\\nexport function exportAmounts(rows) { return formatRows(rows).join('\\\\\\\\n'); }\\\\nexport const publicFixtureSymbols = ['formatInvoice', 'formatRows'];\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/facade.mjs\\\",\\\"content\\\":\\\"import { invoiceAdapter } from './adapter.mjs';\\\\nexport function invoiceFacade(invoice) { return invoiceAdapter(invoice); }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/formatter.mjs\\\",\\\"content\\\":\\\"let lastFormatted = '';\\\\nfunction fixed(value) { return value.toFixed(2); }\\\\nexport function formatInvoice(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  lastFormatted = fixed(value);\\\\n  return lastFormatted;\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n  \"stderr\": \"\"\n}\n```\n",
        "artifact": {
          "path": "fixtures/rerun-03/trace-load.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load.result.md",
          "sha256": "a345f9ffa2211092021c004e5d4f8a3ea7da3d813efc395f40a4dc7e30297285",
          "bytes": 38346
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/rerun-03.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/rerun-03.events.jsonl",
            "sha256": "a2c60b1162c35caa9df1bf28defc95bd626e05a916ea33d03adc1f9a109b1ba9",
            "bytes": 75725,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a6586bd375363848369f28fb4e2c2749f36cabb865a43b40f7407901e6b1672e"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c340eb3ed10b4f1c0292d6c4aca7d6ad20396b86f24f08555a09ddb38f238c21",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 12,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a89ca0172a7f56395bcb30aeedce1c316109ef6f36929615aae4ef1b703dc65b"
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "872c6d2fcc70a0d1eb052d1564b5fd9d11616d62050c8eb5a9d1a1295fdfa93d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_8",
                "line": 14,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "fd2057a024c462d5956efacff5b7ea7a2c86ec4bddecd0fe619f9519554bab87"
              },
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "48f706942f0e9ee59443a1c385388fae8f4f38984e67bc8d526b4dbc490ddb7d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 16,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "b885b8542cf060d4180ba5038f6b0b88b1841d1b45306694c72d2e25600d2450"
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8c4c85a6e630f22bc79729a3aafce1eff70630bc41300e337d859f2f1a1535f8",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e074a68ca651740809a8ad7bd00a72d1daf83aa67eeefe8907a5fb6e7f8d7165"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c4d6b4ded0e5f8c1643f5e9ad955fd0495bb255ffb7278b4652f2e235bb5e1e8",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 43,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f6aa8cc59d83c5f3f41e94a63ed9971a0cec03c7a089728c597cd5b49c081b93"
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "51dbd7838e08d6462421acbccc5443c207e1876c5fafe67cf50b12b75c7c2189",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "eba7bfeb7fc80118bbb43093a52c7503ee9f5e4ca633e18e4c5267d34e8ed425"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c14da738245affa17a4757fe741b194a62f866d4008d57f05b2728d5b88b9ba4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "30b559110a55d893f547f0eeed7befca78fdba8d0dd03029d5888a2b31a22674"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b3ae6e07ef05b52b61f8c6beb156011875f3fdf1cdaceb5d2c13d350008586b6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "40c939287328f36d30b9226d841ae975889f7a32bde68a8257f4ad3d3d37f721"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1a66696c00d6222f10e79995607fc91d57b73e7baaf8949d8452ca83a9ce5928",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d085d76ab68bd85d60bcdc599fe3ac9d067545db1559ae15c6e952c37cab25cb"
              },
              {
                "eventId": "item_16",
                "line": 31,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "47726da34750a35bc773531e3b14e2a483ae6801596e41f55968d8f5eccb55d8",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_19",
                "line": 35,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "691910bb88086a344c6197b7b5b09535dee70b4c03b5ba24c00fa26760bcd41b"
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6a8ac59682d6401015ffc6c3a42280a3eb77e31ddebb07edbffbabdccb4afa7e",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/rerun-03/trace-load/after/calculator.mjs",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/after/calculator.mjs",
            "sha256": "a4fb48ddc2f8cc25fb958924e5555becbe86480ba4273cbc17f8af14766e4c12",
            "bytes": 366
          },
          {
            "path": "fixtures/rerun-03/trace-load/after/controller.mjs",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/after/controller.mjs",
            "sha256": "2dddaf1a8727a248e1f233114eb0d241b6476aefa469ad3add9ece820ba6a3dd",
            "bytes": 136
          },
          {
            "path": "fixtures/rerun-03/trace-load/check.mjs",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/check.mjs",
            "sha256": "0d31f369e2f7b24dbd88e6d551978d5adef217fe303541185bd513c2f53a91d5",
            "bytes": 3645
          },
          {
            "path": "fixtures/rerun-03/trace-load/evidence/baseline.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/baseline.json",
            "sha256": "e6d9f2fc16d97b96cfb4f5e1a35d32608d0b1af8010e7bc907c3b5aa0440b0aa",
            "bytes": 250
          },
          {
            "path": "fixtures/rerun-03/trace-load/evidence/refactored.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/refactored.json",
            "sha256": "fab0dc94878faa63381ef99383e4f6d1a33ab156131ea117467242806dc97a49",
            "bytes": 248
          },
          {
            "path": "fixtures/rerun-03/trace-load/evidence/compare.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/compare.json",
            "sha256": "8e7161c8115facdcc4f668d8ccbfd38f336560a1823c1ad69236f6850b53cf23",
            "bytes": 196
          },
          {
            "path": "fixtures/rerun-03/trace-load/evidence/audit.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/audit.json",
            "sha256": "6921a94e213f7b1901590b0d32d9a936ea042535eec043526cd726ad40431cc8",
            "bytes": 296
          },
          {
            "path": "fixtures/rerun-03/trace-load/evidence/patch.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/patch.json",
            "sha256": "2f7f3ef2f2c28b44b8904aabefb9931b331ad93e40348a193a983cc86e62d39a",
            "bytes": 1389
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_7",
            "item_8",
            "item_9",
            "item_20",
            "item_23"
          ],
          "actualExecutionEventIds": [
            "item_12",
            "item_14",
            "item_15",
            "item_16",
            "item_19"
          ],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-rerun-03.json",
              "reviewedBy": "grade_contract_audit independent source/trace/outcome reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-05/trace-load/after.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/after.json",
      "sha256": "cd4f17e621c75c451f65ca5a5811be995944782b7b6b0b9f2aa8f2a888179bb3",
      "bytes": 439,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.mjs\",\n    \"work\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"first\\\":{\\\"total\\\":6},\\\"afterMutation\\\":9.25,\\\"afterDirectCalculate\\\":17,\\\"empty\\\":0,\\\"formatted\\\":[\\\"0.00\\\",\\\"1.00\\\",\\\"-1.00\\\",\\\"12.35\\\"],\\\"nonfinite\\\":\\\"throws nonfinite\\\",\\\"missingRows\\\":\\\"TypeError\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/baseline.json",
      "sha256": "cd8efab32fe8bb13c7dd78b05a56b278e57f78fb123aeb5d108af95b7b535b7e",
      "bytes": 441,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.mjs\",\n    \"before\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"first\\\":{\\\"total\\\":6},\\\"afterMutation\\\":9.25,\\\"afterDirectCalculate\\\":17,\\\"empty\\\":0,\\\"formatted\\\":[\\\"0.00\\\",\\\"1.00\\\",\\\"-1.00\\\",\\\"12.35\\\"],\\\"nonfinite\\\":\\\"throws nonfinite\\\",\\\"missingRows\\\":\\\"TypeError\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/callers-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/callers-before.json",
      "sha256": "c6b375d6bf1ba1bc943a75d2d6e8a07f6253eeb9d94baa5e462318485ae6efef",
      "bytes": 6055,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load\",\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:1:let lastFormatted = '';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:2:function fixed(value) { return value.toFixed(2); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:3:export function formatInvoice(value) {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:4:  if (!Number.isFinite(value)) throw new Error('nonfinite');\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:5:  lastFormatted = fixed(value);\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:6:  return lastFormatted;\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:7:}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:8:export function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:9:// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/formatter.mjs:10:export function sortAmounts(values) { return values.toSorted(); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/decision.md:1:# Synthetic invoice decision record\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/decision.md:3:Display contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/decision.md:5:Fixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatInvoice and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/decision.md:7:Authorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/controller.mjs:1:import { invoiceFacade } from './facade.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/controller.mjs:2:export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/facade.mjs:1:import { invoiceAdapter } from './adapter.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/facade.mjs:2:export function invoiceFacade(invoice) { return invoiceAdapter(invoice); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/exporter.mjs:1:import { formatRows } from './formatter.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/exporter.mjs:2:export function exportAmounts(rows) { return formatRows(rows).join('\\\\n'); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/exporter.mjs:3:export const publicFixtureSymbols = ['formatInvoice', 'formatRows'];\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/adapter.mjs:1:import { calculate } from './calculator.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/adapter.mjs:2:export function invoiceAdapter(invoice) { return calculate(invoice.rows); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/calculator.mjs:1:let cachedTotal = 0;\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/calculator.mjs:2:export function calculate(rows) {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/calculator.mjs:3:  cachedTotal = rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/calculator.mjs:4:  return cachedTotal;\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/calculator.mjs:5:}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before/calculator.mjs:6:export function inspectCachedTotal() { return cachedTotal; }\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/diff.json",
      "sha256": "1c4c1812b5e49b5245685a096b524538ddf0bd9c59424fde18d51c7a722bfe2a",
      "bytes": 718,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"before\",\n    \"work\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load\",\n  \"exitCode\": 1,\n  \"stdout\": \"Only in before: adapter.mjs\\ndiff -ru before/controller.mjs work/controller.mjs\\n--- before/controller.mjs\\t2026-10-16 10:42:33\\n+++ work/controller.mjs\\t2026-10-16 10:50:55\\n@@ -1,2 +1,2 @@\\n-import { invoiceFacade } from './facade.mjs';\\n-export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n+import { calculate } from './calculator.mjs';\\n+export function invoiceController(invoice) { return { total: calculate(invoice.rows) }; }\\nOnly in before: facade.mjs\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/input-manifest.json",
      "sha256": "3d896fe3f52e96ba3e79efb36eec68e8c5d37cd8b79a0c0334c5ec71a7557c17",
      "bytes": 1180,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "{\n  \"inputSha256\": \"a42c7288083c85ffeba946d2a4ba55175e6c668958f81ca1a5889ae27472997a\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": [\n    {\n      \"path\": \"before/calculator.mjs\",\n      \"sha256\": \"1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff\"\n    },\n    {\n      \"path\": \"before/exporter.mjs\",\n      \"sha256\": \"b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d\"\n    },\n    {\n      \"path\": \"before/adapter.mjs\",\n      \"sha256\": \"a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c\"\n    },\n    {\n      \"path\": \"before/facade.mjs\",\n      \"sha256\": \"6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d\"\n    },\n    {\n      \"path\": \"before/controller.mjs\",\n      \"sha256\": \"90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862\"\n    },\n    {\n      \"path\": \"before/decision.md\",\n      \"sha256\": \"324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee\"\n    },\n    {\n      \"path\": \"before/formatter.mjs\",\n      \"sha256\": \"405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/probe.mjs",
      "sha256": "9c481d3091d8c727f039a9f419b1c9411607dda4f66c069f7f976fb54b27fa29",
      "bytes": 1364,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "import assert from 'node:assert/strict';\nconst dir=process.argv[2];\nconst {invoiceController}=await import(`./${dir}/controller.mjs`);\nconst {calculate,inspectCachedTotal}=await import(`./${dir}/calculator.mjs`);\nconst {formatInvoice,formatRows}=await import(`./${dir}/formatter.mjs`);\nassert.equal(inspectCachedTotal(),0);\nconst invoice={rows:[{qty:2,unitPrice:3.25},{qty:1,unitPrice:-0.5}]};\nconst first=invoiceController(invoice);\nassert.deepEqual(first,{total:6});\nassert.equal(inspectCachedTotal(),6);\ninvoice.rows[0].qty=3;\nassert.equal(first.total,6);\nassert.equal(inspectCachedTotal(),6);\nassert.deepEqual(invoiceController(invoice),{total:9.25});\nassert.equal(inspectCachedTotal(),9.25);\nassert.equal(calculate([{qty:1,unitPrice:17}]),17);\nassert.equal(inspectCachedTotal(),17);\nassert.equal(first.total,6);\nassert.deepEqual(invoiceController({rows:[]}),{total:0});\nassert.equal(inspectCachedTotal(),0);\nconst formatted=[0,1.005,-1.005,12.345].map(formatInvoice);\nassert.deepEqual(formatted,['0.00','1.00','-1.00','12.35']);\nassert.deepEqual(formatRows([]),[]);\nfor(const n of [NaN,Infinity])assert.throws(()=>formatInvoice(n),{message:'nonfinite'});\nassert.throws(()=>invoiceController({}),TypeError);\nconsole.log(JSON.stringify({first,afterMutation:9.25,afterDirectCalculate:17,empty:0,formatted,nonfinite:'throws nonfinite',missingRows:'TypeError'}));\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/registered-case.json",
      "sha256": "37ec090c179ff6255160e73f18ed62730bfe9308c1c4a967ff57cfd8114858bc",
      "bytes": 1939,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "{\n  \"id\": \"trace-load\",\n  \"sourcePaths\": [\n    \"skills/principle-minimize-reader-load/SKILL.md\"\n  ],\n  \"prompt\": \"Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.\",\n  \"requirements\": [\n    \"Read source and callers; writes and execution require available tools and authorization.\",\n    \"Inspect both layers to trace and state to hold.\",\n    \"Preserve meaningful abstraction boundaries and invariants.\"\n  ],\n  \"expectedFull\": \"Inspect the concrete path and caller evidence. Collapse unnecessary one-caller and pass-through layers, keep boundaries that hide meaningful decisions, derive total from rows in a pure function or smaller state scope, and name the invariant once at the boundary. Explain where total comes from and what can change it. Verify authorized edits with observed checks; treat the under-30-second reader test as a criterion unless actually measured.\",\n  \"expectedReduced\": \"With readable source but unavailable or denied writes or execution, give a source-grounded ordered proposal that reduces trace layers and hidden state. State which edits or checks were not performed and preserve permission limits.\",\n  \"expectedBlocked\": \"Without readable source or sufficient caller and state evidence, identify the missing access or evidence and stop concrete refactoring and completion claims.\",\n  \"forbiddenClaims\": [\n    \"A structural validator pass proves host behavior or a measured reader time.\",\n    \"Fewer lines alone prove reduced reader load.\",\n    \"All abstraction layers should be removed regardless of interface compression.\",\n    \"Unavailable writes or execution succeeded.\",\n    \"Preserved invocation metadata proves host enforcement.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/trace-load/work/controller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/work/controller.mjs",
      "sha256": "2dddaf1a8727a248e1f233114eb0d241b6476aefa469ad3add9ece820ba6a3dd",
      "bytes": 136,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "import { calculate } from './calculator.mjs';\nexport function invoiceController(invoice) { return { total: calculate(invoice.rows) }; }\n"
    },
    {
      "path": "fixtures/batch-05/trace-load.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load.result.md",
      "sha256": "cd2af3226b519e9dc50f6f4f0d7a8733e5986937c2af0c7178510638d4330527",
      "bytes": 6446,
      "owners": [
        "grades-native-05.json#2"
      ],
      "text": "# trace-load\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"trace-load\",\n  \"prompt\": \"Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Read source and callers; writes and execution require available tools and authorization.\",\n    \"Inspect both layers to trace and state to hold.\",\n    \"Preserve meaningful abstraction boundaries and invariants.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe copied controller now calls calculate(invoice.rows) directly. I removed facade.mjs and adapter.mjs after reading all supplied invoice sources and their imports. Both forwarding layers had one supplied caller and made no decisions. Calculator still owns numeric calculation; formatter and exporter contracts are unchanged.\n\nThe returned total is rows.reduce((total,row) => total + row.qty * row.unitPrice, 0). Changing a row's qty or unitPrice, adding or removing rows, or replacing rows changes the next calculation. Mutating rows alone does not change an already returned controller result or the cached number. Calling either calculate or invoiceController overwrites the cache. A fresh module instance starts its cache at zero. The existing result object contains a number snapshot, not a live binding. A caller can also mutate its own returned object, independently of the cache.\n\nMinimize Reader Load removed two trace layers. I retained cachedTotal because inspectCachedTotal exposes it, and the supplied decision record explicitly names its observable contract. The probe exercises that accessor after controller and direct calculator calls. Removing the cache would require a changed accessor contract or moving its ownership to an explicit instance; I did not silently remove the export. Thus hidden module state remains a documented limitation of this scoped refactor. No reader completion time was measured.\n\nBefore and after probes both returned totals 6, 9.25, 17 and 0 on the selected paths. They checked that earlier result snapshots stay unchanged, missing rows still throw, and formatter results remain 0.00, 1.00, -1.00 and 12.35. Empty formatting remains [], and NaN and Infinity still throw nonfinite. These are local fixture observations only.\n\n## Variants attempted and limits\n\nOriginal copied modules were executed before editing; migrated modules were executed after editing. Cache and display-contract behavior were checked. Source-unavailable and write-denied branches were unnecessary because those capabilities worked.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\".\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/before\"] | 0 | [trace-load/callers-before.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/callers-before.json) |\n| [\"diff\",\"-ru\",\"before\",\"work\"] | 1 | [trace-load/diff.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/diff.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"work\"] | 0 | [trace-load/after.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/after.json) |\n| [\"bun\",\"--no-install\",\"probe.mjs\",\"before\"] | 0 | [trace-load/baseline.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/trace-load/baseline.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### after.json\n\nExit 0.\n\n```text\n{\"first\":{\"total\":6},\"afterMutation\":9.25,\"afterDirectCalculate\":17,\"empty\":0,\"formatted\":[\"0.00\",\"1.00\",\"-1.00\",\"12.35\"],\"nonfinite\":\"throws nonfinite\",\"missingRows\":\"TypeError\"}\n\n```\n\n### baseline.json\n\nExit 0.\n\n```text\n{\"first\":{\"total\":6},\"afterMutation\":9.25,\"afterDirectCalculate\":17,\"empty\":0,\"formatted\":[\"0.00\",\"1.00\",\"-1.00\",\"12.35\"],\"nonfinite\":\"throws nonfinite\",\"missingRows\":\"TypeError\"}\n\n```\n\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/calculator.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/after/calculator.mjs",
      "sha256": "a4fb48ddc2f8cc25fb958924e5555becbe86480ba4273cbc17f8af14766e4c12",
      "bytes": 366,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "let cachedTotal = 0;\n// Total is the left-to-right JavaScript Number sum of qty * unitPrice, starting at 0.\nexport function sumRows(rows) {\n  return rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\n}\nexport function calculate(rows) {\n  cachedTotal = sumRows(rows);\n  return cachedTotal;\n}\nexport function inspectCachedTotal() { return cachedTotal; }\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/controller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/after/controller.mjs",
      "sha256": "2dddaf1a8727a248e1f233114eb0d241b6476aefa469ad3add9ece820ba6a3dd",
      "bytes": 136,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "import { calculate } from './calculator.mjs';\nexport function invoiceController(invoice) { return { total: calculate(invoice.rows) }; }\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/audit.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/audit.mjs",
      "sha256": "635c5703b99e870f1e31f795595ca5be4f18847346f7efe2e358141f99348fae",
      "bytes": 1604,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "import { readFile, readdir, writeFile } from 'node:fs/promises';\nimport assert from 'node:assert/strict';\nconst shared = '/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice';\nconst installed = '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst hashes = [];\nfor (const name of await readdir(shared)) {\n  const source = await readFile(`${shared}/${name}`);\n  assert.deepEqual(await readFile(`trace-load/before/${name}`), source);\n  hashes.push({path: `${shared}/${name}`, sha256: new Bun.CryptoHasher('sha256').update(source).digest('hex')});\n  if (['formatter.mjs', 'exporter.mjs', 'decision.md'].includes(name)) assert.deepEqual(await readFile(`trace-load/after/${name}`), source);\n}\nfor (const [path, copy] of [\n  ['skills/principle-minimize-reader-load/SKILL.md', 'SKILL.md'],\n  ['references/host-capabilities.md', 'host-capabilities.md'],\n  ['docs/parity/cases/skills/principle-minimize-reader-load.json', 'case.json'],\n  ['plugin.json', 'plugin.json'],\n]) {\n  const source = await readFile(`${installed}/${path}`);\n  assert.deepEqual(await readFile(`trace-load/installed-source/${copy}`), source);\n  hashes.push({path: `${installed}/${path}`, sha256: new Bun.CryptoHasher('sha256').update(source).digest('hex')});\n}\nawait writeFile('trace-load/evidence/input-hashes.json', JSON.stringify(hashes, null, 2) + '\\n');\nconsole.log('All 7 original invoice inputs match shared source; formatter, exporter and decision are unchanged in after/. All 4 retained installed files match their sources. SHA-256 manifest saved.');\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/check.mjs",
      "sha256": "0d31f369e2f7b24dbd88e6d551978d5adef217fe303541185bd513c2f53a91d5",
      "bytes": 3645,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { writeFile } from 'node:fs/promises';\n\nconst variant = process.argv[2];\nassert.ok(['before', 'after'].includes(variant));\nconst { invoiceController } = await import(`./${variant}/controller.mjs`);\nconst { calculate, inspectCachedTotal } = await import(`./${variant}/calculator.mjs`);\nconst { formatInvoice, formatRows, sortAmounts } = await import(`./${variant}/formatter.mjs`);\nconst { exportAmounts, publicFixtureSymbols } = await import(`./${variant}/exporter.mjs`);\nconst encode = value => typeof value === 'number' && !Number.isFinite(value) ? String(value) : Object.is(value, -0) ? '-0' : value;\nconst observations = [];\nfunction total(label, rows, expected) {\n  const result = invoiceController({ rows });\n  assert.deepEqual(result, { total: expected });\n  assert.ok(Object.is(inspectCachedTotal(), expected));\n  observations.push({ label, total: encode(result.total), cache: encode(inspectCachedTotal()) });\n}\nassert.equal(inspectCachedTotal(), 0);\ntotal('empty', [], 0);\ntotal('mixed rows', [{qty: 2, unitPrice: 12.5}, {qty: -1, unitPrice: 5}], 20);\nconst rows = [{qty: 2, unitPrice: 3}];\ntotal('before row mutation', rows, 6);\nrows[0].qty = 4;\nassert.equal(inspectCachedTotal(), 6);\nobservations.push({ label: 'mutation alone leaves cache unchanged', cache: inspectCachedTotal() });\ntotal('recalculation after mutation', rows, 12);\nassert.equal(calculate([{qty: 3, unitPrice: 7}]), 21);\nassert.equal(inspectCachedTotal(), 21);\nfor (const [label, call] of [\n  ['missing rows', () => invoiceController({})],\n  ['null row', () => invoiceController({rows: [null]})],\n  ['throwing getter', () => calculate([{get qty() { throw new Error('row failure'); }}])],\n]) {\n  let error;\n  try { call(); } catch (caught) { error = caught; }\n  assert.ok(error);\n  assert.equal(inspectCachedTotal(), 21);\n  observations.push({label, error: error.name, message: error.message, cache: inspectCachedTotal()});\n}\ntotal('NaN propagates', [{qty: NaN, unitPrice: 1}], NaN);\ntotal('Infinity propagates', [{qty: 1, unitPrice: Infinity}], Infinity);\ntotal('floating arithmetic', [{qty: 3, unitPrice: 0.1}], 3 * 0.1);\ntotal('existing coercion', [{qty: '2', unitPrice: '3'}], 6);\ntotal('sparse array', [, {qty: 1, unitPrice: 4}], 4);\nfor (const value of [0, 1.005, -1.005, 12.345, NaN, Infinity]) {\n  let result;\n  try { result = formatInvoice(value); assert.equal(result, value.toFixed(2)); }\n  catch (error) { assert.equal(error.message, 'nonfinite'); result = { error: error.message }; }\n  observations.push({label: 'formatInvoice', input: encode(value), result});\n}\nassert.deepEqual(formatRows([]), []);\nassert.equal(exportAmounts([]), '');\nassert.deepEqual(publicFixtureSymbols, ['formatInvoice', 'formatRows']);\nassert.equal(exportAmounts([{total: 1.005}, {total: -1.005}]), '1.00\\n-1.00');\nassert.deepEqual(sortAmounts(['2', '10']), ['10', '2']);\nobservations.push({label: 'display consumers', emptyRows: formatRows([]), emptyExport: exportAmounts([]), csv: exportAmounts([{total: 1.005}, {total: -1.005}]), symbols: publicFixtureSymbols, unrelatedSort: sortAmounts(['2', '10'])});\nif (variant === 'after') {\n  const { sumRows } = await import('./after/calculator.mjs');\n  const prior = inspectCachedTotal();\n  assert.equal(sumRows([{qty: 10, unitPrice: 2}]), 20);\n  assert.equal(inspectCachedTotal(), prior);\n}\nawait writeFile(new URL(`./evidence/${variant}-observations.json`, import.meta.url), JSON.stringify(observations, null, 2) + '\\n');\nconsole.log(`${variant}: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; ${observations.length} observations saved.`);\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/after-observations.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/after-observations.json",
      "sha256": "4c9e0c1747a3db91a19b585c02f5049ba4b67901eaf364becd8218fd2b08a734",
      "bytes": 1974,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "[\n  {\n    \"label\": \"empty\",\n    \"total\": 0,\n    \"cache\": 0\n  },\n  {\n    \"label\": \"mixed rows\",\n    \"total\": 20,\n    \"cache\": 20\n  },\n  {\n    \"label\": \"before row mutation\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"mutation alone leaves cache unchanged\",\n    \"cache\": 6\n  },\n  {\n    \"label\": \"recalculation after mutation\",\n    \"total\": 12,\n    \"cache\": 12\n  },\n  {\n    \"label\": \"missing rows\",\n    \"error\": \"TypeError\",\n    \"message\": \"undefined is not an object (evaluating 'rows.reduce')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"null row\",\n    \"error\": \"TypeError\",\n    \"message\": \"null is not an object (evaluating 'row.qty')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"throwing getter\",\n    \"error\": \"Error\",\n    \"message\": \"row failure\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"NaN propagates\",\n    \"total\": \"NaN\",\n    \"cache\": \"NaN\"\n  },\n  {\n    \"label\": \"Infinity propagates\",\n    \"total\": \"Infinity\",\n    \"cache\": \"Infinity\"\n  },\n  {\n    \"label\": \"floating arithmetic\",\n    \"total\": 0.30000000000000004,\n    \"cache\": 0.30000000000000004\n  },\n  {\n    \"label\": \"existing coercion\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"sparse array\",\n    \"total\": 4,\n    \"cache\": 4\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 0,\n    \"result\": \"0.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 1.005,\n    \"result\": \"1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": -1.005,\n    \"result\": \"-1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 12.345,\n    \"result\": \"12.35\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"NaN\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"Infinity\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"display consumers\",\n    \"emptyRows\": [],\n    \"emptyExport\": \"\",\n    \"csv\": \"1.00\\n-1.00\",\n    \"symbols\": [\n      \"formatInvoice\",\n      \"formatRows\"\n    ],\n    \"unrelatedSort\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/audit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/audit.json",
      "sha256": "6921a94e213f7b1901590b0d32d9a936ea042535eec043526cd726ad40431cc8",
      "bytes": 296,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"trace-load/audit.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"All 7 original invoice inputs match shared source; formatter, exporter and decision are unchanged in after/. All 4 retained installed files match their sources. SHA-256 manifest saved.\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/baseline.json",
      "sha256": "e6d9f2fc16d97b96cfb4f5e1a35d32608d0b1af8010e7bc907c3b5aa0440b0aa",
      "bytes": 250,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"trace-load/check.mjs\",\n    \"before\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"before: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; 20 observations saved.\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/before-observations.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/before-observations.json",
      "sha256": "4c9e0c1747a3db91a19b585c02f5049ba4b67901eaf364becd8218fd2b08a734",
      "bytes": 1974,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "[\n  {\n    \"label\": \"empty\",\n    \"total\": 0,\n    \"cache\": 0\n  },\n  {\n    \"label\": \"mixed rows\",\n    \"total\": 20,\n    \"cache\": 20\n  },\n  {\n    \"label\": \"before row mutation\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"mutation alone leaves cache unchanged\",\n    \"cache\": 6\n  },\n  {\n    \"label\": \"recalculation after mutation\",\n    \"total\": 12,\n    \"cache\": 12\n  },\n  {\n    \"label\": \"missing rows\",\n    \"error\": \"TypeError\",\n    \"message\": \"undefined is not an object (evaluating 'rows.reduce')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"null row\",\n    \"error\": \"TypeError\",\n    \"message\": \"null is not an object (evaluating 'row.qty')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"throwing getter\",\n    \"error\": \"Error\",\n    \"message\": \"row failure\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"NaN propagates\",\n    \"total\": \"NaN\",\n    \"cache\": \"NaN\"\n  },\n  {\n    \"label\": \"Infinity propagates\",\n    \"total\": \"Infinity\",\n    \"cache\": \"Infinity\"\n  },\n  {\n    \"label\": \"floating arithmetic\",\n    \"total\": 0.30000000000000004,\n    \"cache\": 0.30000000000000004\n  },\n  {\n    \"label\": \"existing coercion\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"sparse array\",\n    \"total\": 4,\n    \"cache\": 4\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 0,\n    \"result\": \"0.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 1.005,\n    \"result\": \"1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": -1.005,\n    \"result\": \"-1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 12.345,\n    \"result\": \"12.35\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"NaN\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"Infinity\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"display consumers\",\n    \"emptyRows\": [],\n    \"emptyExport\": \"\",\n    \"csv\": \"1.00\\n-1.00\",\n    \"symbols\": [\n      \"formatInvoice\",\n      \"formatRows\"\n    ],\n    \"unrelatedSort\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/callers.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/callers.json",
      "sha256": "23d250533a3e27976210db6ae9638d89ba18671fdf57d9edbc2e93e4d2ba2dea",
      "bytes": 3419,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"rg\",\n    \"-n\",\n    \"invoiceController|invoiceFacade|invoiceAdapter|inspectCachedTotal|calculate\\\\(|calculator.mjs|facade.mjs|adapter.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/decision.md:7:Authorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs:1:import { invoiceFacade } from './facade.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs:2:export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs:1:import { invoiceAdapter } from './adapter.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs:2:export function invoiceFacade(invoice) { return invoiceAdapter(invoice); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs:1:import { calculate } from './calculator.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs:2:export function invoiceAdapter(invoice) { return calculate(invoice.rows); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs:2:export function calculate(rows) {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs:6:export function inspectCachedTotal() { return cachedTotal; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs:1:export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs:2:export function adapter(invoice){return calculate(invoice.rows)}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:15:      \\\"invoice/facade.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:16:      \\\"invoice/adapter.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:17:      \\\"invoice/calculator.mjs\\\"\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:21:      \\\"invoice/facade.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:22:      \\\"invoice/adapter.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:23:      \\\"invoice/calculator.mjs\\\"\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:27:      \\\"invoice/calculator.mjs\\\",\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/compare.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/compare.json",
      "sha256": "8e7161c8115facdcc4f668d8ccbfd38f336560a1823c1ad69236f6850b53cf23",
      "bytes": 196,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"diff\",\n    \"-u\",\n    \"trace-load/evidence/before-observations.json\",\n    \"trace-load/evidence/after-observations.json\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/freeze.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/freeze.json",
      "sha256": "fe9166135ab3d7d15866e87ab47db935f5c55b3694c92db85f517a9ffcfcc927",
      "bytes": 282,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"git\",\n    \"-C\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/input-hashes.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/input-hashes.json",
      "sha256": "bf3b10fea6d33a98f535b66254c2c4842dc3462cf071188437ea1652443b62ca",
      "bytes": 2402,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "[\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs\",\n    \"sha256\": \"1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/exporter.mjs\",\n    \"sha256\": \"b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs\",\n    \"sha256\": \"a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs\",\n    \"sha256\": \"6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs\",\n    \"sha256\": \"90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/decision.md\",\n    \"sha256\": \"324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/formatter.mjs\",\n    \"sha256\": \"405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-minimize-reader-load/SKILL.md\",\n    \"sha256\": \"8684154522048e9e5723f559a5ba9ecfcca87d551a76b9cd2ecd8668b48ccf90\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/host-capabilities.md\",\n    \"sha256\": \"f0f09ce28b6feca4d72694d5687204dc074aa58dade9a0ab59656da3bfa1bd20\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/parity/cases/skills/principle-minimize-reader-load.json\",\n    \"sha256\": \"37ec090c179ff6255160e73f18ed62730bfe9308c1c4a967ff57cfd8114858bc\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/plugin.json\",\n    \"sha256\": \"08119bdaf450eb34ad2a35c0685ac0d5795c45c4101b09bef41bc0ab8fe55cc7\"\n  }\n]\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/patch.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/patch.json",
      "sha256": "2f7f3ef2f2c28b44b8904aabefb9931b331ad93e40348a193a983cc86e62d39a",
      "bytes": 1389,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"diff\",\n    \"-ru\",\n    \"trace-load/before\",\n    \"trace-load/after\"\n  ],\n  \"exitCode\": 1,\n  \"stdout\": \"Only in trace-load/before: adapter.mjs\\ndiff -ru trace-load/before/calculator.mjs trace-load/after/calculator.mjs\\n--- trace-load/before/calculator.mjs\\t2026-10-16 11:12:02\\n+++ trace-load/after/calculator.mjs\\t2026-10-16 11:12:49\\n@@ -1,6 +1,10 @@\\n let cachedTotal = 0;\\n+// Total is the left-to-right JavaScript Number sum of qty * unitPrice, starting at 0.\\n+export function sumRows(rows) {\\n+  return rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n+}\\n export function calculate(rows) {\\n-  cachedTotal = rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n+  cachedTotal = sumRows(rows);\\n   return cachedTotal;\\n }\\n export function inspectCachedTotal() { return cachedTotal; }\\ndiff -ru trace-load/before/controller.mjs trace-load/after/controller.mjs\\n--- trace-load/before/controller.mjs\\t2026-10-16 11:12:02\\n+++ trace-load/after/controller.mjs\\t2026-10-16 11:12:49\\n@@ -1,2 +1,2 @@\\n-import { invoiceFacade } from './facade.mjs';\\n-export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n+import { calculate } from './calculator.mjs';\\n+export function invoiceController(invoice) { return { total: calculate(invoice.rows) }; }\\nOnly in trace-load/before: facade.mjs\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/refactored.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/refactored.json",
      "sha256": "fab0dc94878faa63381ef99383e4f6d1a33ab156131ea117467242806dc97a49",
      "bytes": 248,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"trace-load/check.mjs\",\n    \"after\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"after: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; 20 observations saved.\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/evidence/runtime.json",
      "sha256": "c31ac0e8bc33074a34ab0c28e25e750b1a5b71cfc1578eb64593b3f46b3e522f",
      "bytes": 106,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/run.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/run.mjs",
      "sha256": "18c83f8cb32b160f5db6f9799a0e8003e3eb0bd433e66198bf5de1c725ebe5d5",
      "bytes": 499,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "import { writeFile } from 'node:fs/promises';\nconst name = process.argv[2];\nconst command = process.argv.slice(3);\nconst result = Bun.spawnSync(command, {cwd: process.cwd(), stdout: 'pipe', stderr: 'pipe'});\nconst record = {command, exitCode: result.exitCode, stdout: result.stdout.toString(), stderr: result.stderr.toString()};\nawait writeFile(`trace-load/evidence/${name}.json`, JSON.stringify(record, null, 2) + '\\n');\nconsole.log(JSON.stringify(record, null, 2));\nprocess.exit(result.exitCode);\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load/write-report.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/write-report.mjs",
      "sha256": "32b3fdfd8e9d0355d7dbd98c779e869b2f1a5db799cb85e20e02f9e2e8691d9f",
      "bytes": 9821,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "import { readdir, readFile, writeFile } from 'node:fs/promises';\nconst report = `# trace-load native execution record\n\n## Actual response\n\nThe original total comes from controller.mjs calling invoiceFacade(invoice), then invoiceAdapter(invoice), then calculate(invoice.rows). Each wrapper has one caller in the supplied invoice source. The facade forwards the invoice unchanged; the adapter selects rows. Neither hides a separate policy or implementation. The broader shared-fixture search is retained in evidence/callers.json. It also finds a separate shared/invoice.mjs fixture, which is not imported by this concrete path and was not edited.\n\nIn the case-owned after/ copy, the controller calls calculate(invoice.rows) directly. The facade and adapter files were removed. The controller still constructs { total }, and calculate remains the boundary for the observable calculator cache. sumRows is now a pure derivation. The one invariant comment at that derivation states that total is the left-to-right JavaScript Number sum of qty * unitPrice starting at 0. There is no rounding, decimal arithmetic replacement, finite-number validation, or coercion change here.\n\nChanges to qty, unitPrice, row membership, or row order can change the next result. JavaScript floating-point addition makes order relevant. A successful calculate call, including a controller call, replaces the module cache. Mutating rows alone does not refresh the cache or an already-returned total. An exception during reduction leaves the previous cache intact. NaN and Infinity propagate through calculation. Calling sumRows alone does not update the cache. No invoice.total input field is read or mutated.\n\nThe original path requires tracing four modules; the new path uses two modules. The extra pure function is next to calculate in calculator.mjs. The cache remains because inspectCachedTotal exposes it. Removing that state would change the supplied observable API. Readers still need to understand this one module-scoped value when using the inspection API. Fewer files are a structural observation, not a measured comprehension improvement.\n\nThe decision record describes a UI comparing two-decimal strings and the CSV consumer importing formatRows. The supplied exporter confirms the latter; no UI implementation or customer ticket was supplied. Formatter rounding, error behavior, names, public symbol strings, and the unrelated sort defect remain unchanged. The actual controller does not invoke the formatter, so the record's statement about formatter errors propagating through a controller cannot be exercised as a connected path in this source. Formatter errors were checked directly.\n\n## Variants and boundaries\n\n1. Original seven-file fixture, copied to before/ and executed before edits.\n2. One implemented refactor in after/: remove facade and adapter; retain calculate and inspectCachedTotal; extract pure sumRows. Executed and compared to baseline. No other implementation variant was attempted or failed.\n\nA pure-only calculator with a removed cache was considered and rejected because cache inspection is observable. Inlining calculation into the controller was rejected because direct calculate and inspection form a meaningful compatibility boundary. These were design alternatives, not executed variants.\n\nThe decision record's formatter alternatives A and B belong to a different refactor. Conceptually A removes hidden lastFormatted state and the fixed pass-through, while B adds instance ownership and lifecycle questions without a supplied need. Either would require its own equivalence checks. Neither was implemented here, and formatInvoice was not renamed.\n\n## Observed checks\n\nBaseline and edited runs each saved 20 observations. Their files compare byte-for-byte with diff exit 0. Checks cover empty and mixed rows, row mutation before recalculation, direct calculate, missing rows, null row, throwing getter, unchanged cache on errors, NaN, Infinity, binary floating arithmetic, existing numeric-string coercion, and sparse rows. The edited run additionally asserts pure sumRows leaves the cache untouched. This assertion succeeded but adds no synthetic baseline observation.\n\nBefore edits, observed display results were 0 -> \"0.00\", 1.005 -> \"1.00\", -1.005 -> \"-1.00\", and 12.345 -> \"12.35\". NaN and Infinity each threw Error('nonfinite'); empty formatRows returned []; empty export returned an empty string. Both runs exercised CSV output, exported symbol strings, and the existing lexical sort behavior. These are observed local Bun checks, not expectations copied into a completion receipt.\n\nThe audit confirmed that all seven before/ files still equal the read-only inputs, and that formatter.mjs, exporter.mjs, and decision.md also remain byte-identical in after/. Four retained installed package files match live installed source. SHA-256 values are in evidence/input-hashes.json. The patch command exits 1 because differences exist, which is the normal diff result. It is not a failed test.\n\n## Host, provenance and incomplete parts\n\nExecution used the actual exposed functions.exec wrapper and tools.exec_command binding on this host. Edits used tools.apply_patch and Bun filesystem operations within the authorized root. No worker was required or spawned. No external actions, installs, configuration changes, commits, pushes, schedules, or changes to shared input or installed package were performed.\n\nThe requested source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The exact installed path was read, and plugin.json reports version 0.1.0. Git revision discovery failed with exit 128 because the installed directory has no Git repository. Thus commit provenance remains user-supplied and is not independently verified. Snapshot hashes identify the bytes actually used. The skill's disable-model-invocation metadata is retained as source metadata, with no claim that this host enforces it.\n\nThe under-30-second reader test remains a criterion. No new reader was timed. No structural validator, release claim, grading label, or proxy success receipt was created. Behavioral checks cover the supplied fixture and selected cases; they do not establish unknown external caller compatibility. No independent outcome reviewer was invoked.\n\nThe writable root was empty at initial ls -la, so no previous incomplete output was present there to overwrite. No previous transcript or external retained output was located, modified, or used. This record does not claim to recover it.\n\n## Artifacts\n\nAll paths below are relative to /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/.\n\n- before/: all seven unchanged invoice inputs, including the actual decision.\n- after/: edited concrete implementation and unchanged display consumers.\n- installed-source/: exact requested skill, host capability guidance, case contract, and plugin manifest.\n- check.mjs: executed behavioral checks; run.mjs: captures exact command arguments, stdout, stderr and exit status.\n- audit.mjs: source preservation and hash checks; write-report.mjs: this report generator.\n- evidence/: raw command records, baseline and edited observations, patch output and input hashes.\n\n## Discovery and write log\n\nInitial read-only discovery used tools.exec_command before the persistent command recorder existed. The shell invocations read pwd, rg --files for AGENTS.md, trace-load and result files, ls -la of the root and shared invoice directory, all seven invoice files with cat, the exact installed SKILL.md, host-capabilities.md, unslop/SKILL.md, scenario-map.json, case JSON and plugin.json. All returned exit 0. The first rg produced no matches and the initial root listing contained only . and ... Ancestor AGENTS.md checks from / through the writable root and checks at shared/, additional/ and invoice/ printed no instruction files. Source contents are retained in before/ and installed-source/ and in the source-read command record below. The provided user AGENTS instructions governed the work.\n\nThe initial caller search and Bun version check returned matches and 1.4.2. The first git rev-parse failed with 'fatal: not a git repository (or any of the parent directories): .git'; the compound shell command returned 0 because its final bun --version succeeded. The isolated retry below records the actual Git exit 128. No failed freeze discovery is treated as verification.\n\nThe copy command ran via bun -e with node:fs/promises mkdir/cp. It copied the complete seven-file invoice directory into before/ and after/ before edits, then copied the four installed source files. Exit 0, output: 'Copied all 7 invoice inputs unchanged into before/ and after/; retained exact installed source and contract.' The later audit independently checked these copies. tools.apply_patch then created check.mjs and run.mjs, edited only after/controller.mjs and after/calculator.mjs, deleted only after/facade.mjs and after/adapter.mjs, and created audit.mjs and this report generator. Each apply_patch returned successfully with {}. No permission denial or alternate implementation retry occurred.\n\nThe following records contain the exact recorded command arguments, outputs and individual exit statuses. The source-read tool display was truncated, but its complete stdout is saved in evidence/source-read.json. Report generation is run as bun trace-load/write-report.mjs and prints its saved path; a final readback checks report persistence and lists artifacts.\n`;\nlet output = report;\nfor (const name of (await readdir('trace-load/evidence')).sort()) {\n  output += `\\n### ${name}\\n\\n\\`\\`\\`json\\n${await readFile(`trace-load/evidence/${name}`, 'utf8')}\\`\\`\\`\\n`;\n}\nawait writeFile('trace-load.result.md', output);\nconsole.log('Saved trace-load.result.md with actual response and raw evidence records.');\n"
    },
    {
      "path": "fixtures/rerun-03/trace-load.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load.result.md",
      "sha256": "a345f9ffa2211092021c004e5d4f8a3ea7da3d813efc395f40a4dc7e30297285",
      "bytes": 38346,
      "owners": [
        "grades-native-rerun-03.json#0"
      ],
      "text": "# trace-load native execution record\n\n## Actual response\n\nThe original total comes from controller.mjs calling invoiceFacade(invoice), then invoiceAdapter(invoice), then calculate(invoice.rows). Each wrapper has one caller in the supplied invoice source. The facade forwards the invoice unchanged; the adapter selects rows. Neither hides a separate policy or implementation. The broader shared-fixture search is retained in evidence/callers.json. It also finds a separate shared/invoice.mjs fixture, which is not imported by this concrete path and was not edited.\n\nIn the case-owned after/ copy, the controller calls calculate(invoice.rows) directly. The facade and adapter files were removed. The controller still constructs { total }, and calculate remains the boundary for the observable calculator cache. sumRows is now a pure derivation. The one invariant comment at that derivation states that total is the left-to-right JavaScript Number sum of qty * unitPrice starting at 0. There is no rounding, decimal arithmetic replacement, finite-number validation, or coercion change here.\n\nChanges to qty, unitPrice, row membership, or row order can change the next result. JavaScript floating-point addition makes order relevant. A successful calculate call, including a controller call, replaces the module cache. Mutating rows alone does not refresh the cache or an already-returned total. An exception during reduction leaves the previous cache intact. NaN and Infinity propagate through calculation. Calling sumRows alone does not update the cache. No invoice.total input field is read or mutated.\n\nThe original path requires tracing four modules; the new path uses two modules. The extra pure function is next to calculate in calculator.mjs. The cache remains because inspectCachedTotal exposes it. Removing that state would change the supplied observable API. Readers still need to understand this one module-scoped value when using the inspection API. Fewer files are a structural observation, not a measured comprehension improvement.\n\nThe decision record describes a UI comparing two-decimal strings and the CSV consumer importing formatRows. The supplied exporter confirms the latter; no UI implementation or customer ticket was supplied. Formatter rounding, error behavior, names, public symbol strings, and the unrelated sort defect remain unchanged. The actual controller does not invoke the formatter, so the record's statement about formatter errors propagating through a controller cannot be exercised as a connected path in this source. Formatter errors were checked directly.\n\n## Variants and boundaries\n\n1. Original seven-file fixture, copied to before/ and executed before edits.\n2. One implemented refactor in after/: remove facade and adapter; retain calculate and inspectCachedTotal; extract pure sumRows. Executed and compared to baseline. No other implementation variant was attempted or failed.\n\nA pure-only calculator with a removed cache was considered and rejected because cache inspection is observable. Inlining calculation into the controller was rejected because direct calculate and inspection form a meaningful compatibility boundary. These were design alternatives, not executed variants.\n\nThe decision record's formatter alternatives A and B belong to a different refactor. Conceptually A removes hidden lastFormatted state and the fixed pass-through, while B adds instance ownership and lifecycle questions without a supplied need. Either would require its own equivalence checks. Neither was implemented here, and formatInvoice was not renamed.\n\n## Observed checks\n\nBaseline and edited runs each saved 20 observations. Their files compare byte-for-byte with diff exit 0. Checks cover empty and mixed rows, row mutation before recalculation, direct calculate, missing rows, null row, throwing getter, unchanged cache on errors, NaN, Infinity, binary floating arithmetic, existing numeric-string coercion, and sparse rows. The edited run additionally asserts pure sumRows leaves the cache untouched. This assertion succeeded but adds no synthetic baseline observation.\n\nBefore edits, observed display results were 0 -> \"0.00\", 1.005 -> \"1.00\", -1.005 -> \"-1.00\", and 12.345 -> \"12.35\". NaN and Infinity each threw Error('nonfinite'); empty formatRows returned []; empty export returned an empty string. Both runs exercised CSV output, exported symbol strings, and the existing lexical sort behavior. These are observed local Bun checks, not expectations copied into a completion receipt.\n\nThe audit confirmed that all seven before/ files still equal the read-only inputs, and that formatter.mjs, exporter.mjs, and decision.md also remain byte-identical in after/. Four retained installed package files match live installed source. SHA-256 values are in evidence/input-hashes.json. The patch command exits 1 because differences exist, which is the normal diff result. It is not a failed test.\n\n## Host, provenance and incomplete parts\n\nExecution used the actual exposed functions.exec wrapper and tools.exec_command binding on this host. Edits used tools.apply_patch and Bun filesystem operations within the authorized root. No worker was required or spawned. No external actions, installs, configuration changes, commits, pushes, schedules, or changes to shared input or installed package were performed.\n\nThe requested source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The exact installed path was read, and plugin.json reports version 0.1.0. Git revision discovery failed with exit 128 because the installed directory has no Git repository. Thus commit provenance remains user-supplied and is not independently verified. Snapshot hashes identify the bytes actually used. The skill's disable-model-invocation metadata is retained as source metadata, with no claim that this host enforces it.\n\nThe under-30-second reader test remains a criterion. No new reader was timed. No structural validator, release claim, grading label, or proxy success receipt was created. Behavioral checks cover the supplied fixture and selected cases; they do not establish unknown external caller compatibility. No independent outcome reviewer was invoked.\n\nThe writable root was empty at initial ls -la, so no previous incomplete output was present there to overwrite. No previous transcript or external retained output was located, modified, or used. This record does not claim to recover it.\n\n## Artifacts\n\nAll paths below are relative to /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-03/trace-load/.\n\n- before/: all seven unchanged invoice inputs, including the actual decision.\n- after/: edited concrete implementation and unchanged display consumers.\n- installed-source/: exact requested skill, host capability guidance, case contract, and plugin manifest.\n- check.mjs: executed behavioral checks; run.mjs: captures exact command arguments, stdout, stderr and exit status.\n- audit.mjs: source preservation and hash checks; write-report.mjs: this report generator.\n- evidence/: raw command records, baseline and edited observations, patch output and input hashes.\n\n## Discovery and write log\n\nInitial read-only discovery used tools.exec_command before the persistent command recorder existed. The shell invocations read pwd, rg --files for AGENTS.md, trace-load and result files, ls -la of the root and shared invoice directory, all seven invoice files with cat, the exact installed SKILL.md, host-capabilities.md, unslop/SKILL.md, scenario-map.json, case JSON and plugin.json. All returned exit 0. The first rg produced no matches and the initial root listing contained only . and ... Ancestor AGENTS.md checks from / through the writable root and checks at shared/, additional/ and invoice/ printed no instruction files. Source contents are retained in before/ and installed-source/ and in the source-read command record below. The provided user AGENTS instructions governed the work.\n\nThe initial caller search and Bun version check returned matches and 1.4.2. The first git rev-parse failed with 'fatal: not a git repository (or any of the parent directories): .git'; the compound shell command returned 0 because its final bun --version succeeded. The isolated retry below records the actual Git exit 128. No failed freeze discovery is treated as verification.\n\nThe copy command ran via bun -e with node:fs/promises mkdir/cp. It copied the complete seven-file invoice directory into before/ and after/ before edits, then copied the four installed source files. Exit 0, output: 'Copied all 7 invoice inputs unchanged into before/ and after/; retained exact installed source and contract.' The later audit independently checked these copies. tools.apply_patch then created check.mjs and run.mjs, edited only after/controller.mjs and after/calculator.mjs, deleted only after/facade.mjs and after/adapter.mjs, and created audit.mjs and this report generator. Each apply_patch returned successfully with {}. No permission denial or alternate implementation retry occurred.\n\nThe following records contain the exact recorded command arguments, outputs and individual exit statuses. The source-read tool display was truncated, but its complete stdout is saved in evidence/source-read.json. Report generation is run as bun trace-load/write-report.mjs and prints its saved path; a final readback checks report persistence and lists artifacts.\n\n### after-observations.json\n\n```json\n[\n  {\n    \"label\": \"empty\",\n    \"total\": 0,\n    \"cache\": 0\n  },\n  {\n    \"label\": \"mixed rows\",\n    \"total\": 20,\n    \"cache\": 20\n  },\n  {\n    \"label\": \"before row mutation\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"mutation alone leaves cache unchanged\",\n    \"cache\": 6\n  },\n  {\n    \"label\": \"recalculation after mutation\",\n    \"total\": 12,\n    \"cache\": 12\n  },\n  {\n    \"label\": \"missing rows\",\n    \"error\": \"TypeError\",\n    \"message\": \"undefined is not an object (evaluating 'rows.reduce')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"null row\",\n    \"error\": \"TypeError\",\n    \"message\": \"null is not an object (evaluating 'row.qty')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"throwing getter\",\n    \"error\": \"Error\",\n    \"message\": \"row failure\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"NaN propagates\",\n    \"total\": \"NaN\",\n    \"cache\": \"NaN\"\n  },\n  {\n    \"label\": \"Infinity propagates\",\n    \"total\": \"Infinity\",\n    \"cache\": \"Infinity\"\n  },\n  {\n    \"label\": \"floating arithmetic\",\n    \"total\": 0.30000000000000004,\n    \"cache\": 0.30000000000000004\n  },\n  {\n    \"label\": \"existing coercion\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"sparse array\",\n    \"total\": 4,\n    \"cache\": 4\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 0,\n    \"result\": \"0.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 1.005,\n    \"result\": \"1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": -1.005,\n    \"result\": \"-1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 12.345,\n    \"result\": \"12.35\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"NaN\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"Infinity\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"display consumers\",\n    \"emptyRows\": [],\n    \"emptyExport\": \"\",\n    \"csv\": \"1.00\\n-1.00\",\n    \"symbols\": [\n      \"formatInvoice\",\n      \"formatRows\"\n    ],\n    \"unrelatedSort\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n```\n\n### audit.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"trace-load/audit.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"All 7 original invoice inputs match shared source; formatter, exporter and decision are unchanged in after/. All 4 retained installed files match their sources. SHA-256 manifest saved.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### baseline.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"trace-load/check.mjs\",\n    \"before\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"before: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; 20 observations saved.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### before-observations.json\n\n```json\n[\n  {\n    \"label\": \"empty\",\n    \"total\": 0,\n    \"cache\": 0\n  },\n  {\n    \"label\": \"mixed rows\",\n    \"total\": 20,\n    \"cache\": 20\n  },\n  {\n    \"label\": \"before row mutation\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"mutation alone leaves cache unchanged\",\n    \"cache\": 6\n  },\n  {\n    \"label\": \"recalculation after mutation\",\n    \"total\": 12,\n    \"cache\": 12\n  },\n  {\n    \"label\": \"missing rows\",\n    \"error\": \"TypeError\",\n    \"message\": \"undefined is not an object (evaluating 'rows.reduce')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"null row\",\n    \"error\": \"TypeError\",\n    \"message\": \"null is not an object (evaluating 'row.qty')\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"throwing getter\",\n    \"error\": \"Error\",\n    \"message\": \"row failure\",\n    \"cache\": 21\n  },\n  {\n    \"label\": \"NaN propagates\",\n    \"total\": \"NaN\",\n    \"cache\": \"NaN\"\n  },\n  {\n    \"label\": \"Infinity propagates\",\n    \"total\": \"Infinity\",\n    \"cache\": \"Infinity\"\n  },\n  {\n    \"label\": \"floating arithmetic\",\n    \"total\": 0.30000000000000004,\n    \"cache\": 0.30000000000000004\n  },\n  {\n    \"label\": \"existing coercion\",\n    \"total\": 6,\n    \"cache\": 6\n  },\n  {\n    \"label\": \"sparse array\",\n    \"total\": 4,\n    \"cache\": 4\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 0,\n    \"result\": \"0.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 1.005,\n    \"result\": \"1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": -1.005,\n    \"result\": \"-1.00\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": 12.345,\n    \"result\": \"12.35\"\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"NaN\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"formatInvoice\",\n    \"input\": \"Infinity\",\n    \"result\": {\n      \"error\": \"nonfinite\"\n    }\n  },\n  {\n    \"label\": \"display consumers\",\n    \"emptyRows\": [],\n    \"emptyExport\": \"\",\n    \"csv\": \"1.00\\n-1.00\",\n    \"symbols\": [\n      \"formatInvoice\",\n      \"formatRows\"\n    ],\n    \"unrelatedSort\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n```\n\n### callers.json\n\n```json\n{\n  \"command\": [\n    \"rg\",\n    \"-n\",\n    \"invoiceController|invoiceFacade|invoiceAdapter|inspectCachedTotal|calculate\\\\(|calculator.mjs|facade.mjs|adapter.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/decision.md:7:Authorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs:1:import { invoiceFacade } from './facade.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs:2:export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs:1:import { invoiceAdapter } from './adapter.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs:2:export function invoiceFacade(invoice) { return invoiceAdapter(invoice); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs:1:import { calculate } from './calculator.mjs';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs:2:export function invoiceAdapter(invoice) { return calculate(invoice.rows); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs:2:export function calculate(rows) {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs:6:export function inspectCachedTotal() { return cachedTotal; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs:1:export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/invoice.mjs:2:export function adapter(invoice){return calculate(invoice.rows)}\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:15:      \\\"invoice/facade.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:16:      \\\"invoice/adapter.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:17:      \\\"invoice/calculator.mjs\\\"\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:21:      \\\"invoice/facade.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:22:      \\\"invoice/adapter.mjs\\\",\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:23:      \\\"invoice/calculator.mjs\\\"\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/scenario-map.json:27:      \\\"invoice/calculator.mjs\\\",\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### compare.json\n\n```json\n{\n  \"command\": [\n    \"diff\",\n    \"-u\",\n    \"trace-load/evidence/before-observations.json\",\n    \"trace-load/evidence/after-observations.json\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### freeze.json\n\n```json\n{\n  \"command\": [\n    \"git\",\n    \"-C\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n```\n\n### input-hashes.json\n\n```json\n[\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/calculator.mjs\",\n    \"sha256\": \"1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/exporter.mjs\",\n    \"sha256\": \"b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/adapter.mjs\",\n    \"sha256\": \"a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/facade.mjs\",\n    \"sha256\": \"6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/controller.mjs\",\n    \"sha256\": \"90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/decision.md\",\n    \"sha256\": \"324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice/formatter.mjs\",\n    \"sha256\": \"405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-minimize-reader-load/SKILL.md\",\n    \"sha256\": \"8684154522048e9e5723f559a5ba9ecfcca87d551a76b9cd2ecd8668b48ccf90\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/host-capabilities.md\",\n    \"sha256\": \"f0f09ce28b6feca4d72694d5687204dc074aa58dade9a0ab59656da3bfa1bd20\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/parity/cases/skills/principle-minimize-reader-load.json\",\n    \"sha256\": \"37ec090c179ff6255160e73f18ed62730bfe9308c1c4a967ff57cfd8114858bc\"\n  },\n  {\n    \"path\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/plugin.json\",\n    \"sha256\": \"08119bdaf450eb34ad2a35c0685ac0d5795c45c4101b09bef41bc0ab8fe55cc7\"\n  }\n]\n```\n\n### patch.json\n\n```json\n{\n  \"command\": [\n    \"diff\",\n    \"-ru\",\n    \"trace-load/before\",\n    \"trace-load/after\"\n  ],\n  \"exitCode\": 1,\n  \"stdout\": \"Only in trace-load/before: adapter.mjs\\ndiff -ru trace-load/before/calculator.mjs trace-load/after/calculator.mjs\\n--- trace-load/before/calculator.mjs\\t2026-10-16 11:12:02\\n+++ trace-load/after/calculator.mjs\\t2026-10-16 11:12:49\\n@@ -1,6 +1,10 @@\\n let cachedTotal = 0;\\n+// Total is the left-to-right JavaScript Number sum of qty * unitPrice, starting at 0.\\n+export function sumRows(rows) {\\n+  return rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n+}\\n export function calculate(rows) {\\n-  cachedTotal = rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\n+  cachedTotal = sumRows(rows);\\n   return cachedTotal;\\n }\\n export function inspectCachedTotal() { return cachedTotal; }\\ndiff -ru trace-load/before/controller.mjs trace-load/after/controller.mjs\\n--- trace-load/before/controller.mjs\\t2026-10-16 11:12:02\\n+++ trace-load/after/controller.mjs\\t2026-10-16 11:12:49\\n@@ -1,2 +1,2 @@\\n-import { invoiceFacade } from './facade.mjs';\\n-export function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\n+import { calculate } from './calculator.mjs';\\n+export function invoiceController(invoice) { return { total: calculate(invoice.rows) }; }\\nOnly in trace-load/before: facade.mjs\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### refactored.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"trace-load/check.mjs\",\n    \"after\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"after: controller, direct calculate, cache/error semantics, and unchanged display consumers checked; 20 observations saved.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### runtime.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### source-read.json\n\n```json\n{\n  \"command\": [\n    \"bun\",\n    \"-e\",\n    \"for (const path of [\\\"trace-load/installed-source/SKILL.md\\\",\\\"trace-load/installed-source/host-capabilities.md\\\",\\\"trace-load/installed-source/case.json\\\",...(await Array.fromAsync(new Bun.Glob(\\\"trace-load/before/*\\\").scan(\\\".\\\"))).sort()]) { console.log(JSON.stringify({path,content:await Bun.file(path).text()})); }\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"path\\\":\\\"trace-load/installed-source/SKILL.md\\\",\\\"content\\\":\\\"---\\\\nname: principle-minimize-reader-load\\\\ndescription: \\\\\\\"Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.\\\\\\\"\\\\ndisable-model-invocation: true\\\\n---\\\\n\\\\n# Minimize Reader Load\\\\n\\\\nMaintainability is the work a reader must do to understand code. Track two axes:\\\\n1. **Layers to trace.** How many indirections sit between the question and the answer.\\\\n2. **State to hold.** How much hidden or mutable context the reader must keep in their head.\\\\n\\\\n**Why:** Code is read far more than it is written. LOC, cyclomatic complexity, and \\\\\\\"clean architecture\\\\\\\" are proxies. Reader load is the thing that matters. The two axes are independent. A flat file with 50 globals can be as hard to reason about as a 6-layer adapter stack. Guard both. This is the human analog of [Guard the Context Window](../principle-guard-the-context-window/SKILL.md). Working memory is finite for readers too.\\\\n\\\\n**The pattern:**\\\\n- **Collapse layers** that cost more than they save: wrappers with one caller, adapters with no second implementation, speculative indirection that was never needed. Inline them.\\\\n- **Make adjacent layers change the abstraction.** A layer that repeats the same methods and arguments adds reader load without compression. Collapse pass-through layers.\\\\n- **Demand interface compression.** A broad interface that hides little complexity makes readers learn both the surface and the implementation. Prefer boundaries that hide meaningful decisions.\\\\n- **Shrink state scope:** prefer pure functions (returns over mutations), locals over fields, fields over module state, and module state over globals. Derive instead of sync.\\\\n- **Name the invariant at the boundary,** not in every consumer, so the reader learns it once.\\\\n- Before adding a layer or a piece of state, ask: does this reduce reader load somewhere else by at least as much?\\\\n\\\\n**The test:** Can a new reader answer \\\\\\\"where does X come from?\\\\\\\" and \\\\\\\"what can change X?\\\\\\\" in under 30 seconds? If not, cut layers or cut state.\\\\n\\\\n## Session capabilities and permissions\\\\n\\\\nUse [host capabilities](../../references/host-capabilities.md) to discover available read, write and execution tools. Inspect the concrete path, its callers and mutable state before deciding which layers to collapse. Make edits only within the authorized task and available write permissions. Run appropriate checks only through observed execution tools.\\\\n\\\\nWhen source is readable but writes or execution are denied or unavailable, give a source-grounded proposal and identify the edits or checks you could not perform. Without source or sufficient caller and state evidence, report the missing evidence and stop concrete refactoring claims. Do not claim a measured reader time without observation. Preserve invocation metadata without assuming the host enforces it.\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/installed-source/host-capabilities.md\\\",\\\"content\\\":\\\"# Discover capabilities in the current session\\\\n\\\\nRead the tools exposed to this session before assigning work. Cached official-subagents.txt is documentation context; it proves no operation succeeded. Local agent configuration is not portable plugin configuration.\\\\n\\\\nRecord each binding as `{operation, tool, exposed, succeeded, evidence, limits}`. `tool` is the exact exposed identifier or null when absent. `succeeded` is true only after observing a result. Keep failed and unavailable bindings. Successful bindings become `successfulOperations` in host evidence, with a root-relative evidence file. The operation labels below describe purposes, never callable APIs.\\\\n\\\\n| Operation | Discovery and observation required |\\\\n| --- | --- |\\\\n| spawn | Find an exposed independent-worker operation; retain returned worker identity and exact assigned revision. |\\\\n| follow-up | Find the operation that sends input to that worker; observe acceptance by the same identity. |\\\\n| wait | Find the operation that waits for worker state; retain terminal or interrupted state. |\\\\n| inspect-result | Read the worker result and its referenced artifacts; a wait notification alone is insufficient. |\\\\n| stop | Observe cancellation or termination through the exposed operation. |\\\\n| read | Observe the requested file content through the available file tool. |\\\\n| isolated-write | Observe a write within the worker's assigned path and permissions. |\\\\n| history | Observe available prior turns or records; declare gaps explicitly. |\\\\n| execution | Observe command execution with exit status and output. |\\\\n| persistence | Write and read an authorized durable record; a claimed save is insufficient. |\\\\n| external-write | Record explicit authorization and action identity; inspect the result before replay. |\\\\n| resolve-ownership | Observe distinct owned paths before contested writes. |\\\\n| inspect-terminal | Observe the worker's terminal state after stop. |\\\\n| quarantine-artifacts | Observe partial artifacts withheld from integration. |\\\\n| inspect-prior-action | Read the interrupted action identity and prior outcome. |\\\\n| inspect-destination | Observe the destination state for that action identity. |\\\\n| safe-recovery | Observe explicitly authorized idempotent recovery after identity and destination inspection. |\\\\n\\\\nNo default API names are assigned here. Tool names differ by host and session. An exposed tool may still be denied or fail. Record requested and actual models only when observed; otherwise use `unknown`. A requested model never proves the actual model.\\\\n\\\\nA denied or unavailable operation blocks the branch that requires it. Sequential substitution for required independent work is reduced capability and uses `reduced-pass`; ordinary direct completion can fully pass. Missing persistence limits session pickup even when current work succeeds. Preserve user authorization and host permission boundaries through every fallback.\\\\n\\\\nWorker passes require observed spawn and result inspection. Each registry entry declares `requiredObservations` for `pass` and `reduced-pass`; tool observations need exposed bindings and existing evidence artifacts; native text observations use the separate reviewed native record below. Full cancellation requires stop, terminal inspection and artifact quarantine. Full persistence requires durable write and readback. Full interrupted-action recovery requires prior identity inspection, destination inspection, safe recovery, explicit external permission and a recorded prior action identity even when no external-write observation is listed.\\\\n\\\\nPermission checks follow performed operations. Isolated writes and persistence require granted writes. External writes and safe recovery require granted external permission and prior identity. Authorized read-only reductions may retain denied writes; their limits must preserve denied or unavailable permissions. Required observations remain applicable to those reductions.\\\\n\\\\nHost evidence is stored as object or array JSON files under `docs/parity/evidence/`. Required fields are defined by `docs/parity/evidence.schema.json`. Artifacts and operation evidence must be existing files inside the tested root. Test fixtures belong in `tests/` and prove validator behavior only.\\\\n\\\\nRun `python3 tools/validate_evidence.py --root . --commit <tested-package-commit>` through Bun, for example `bun -e 'const p=Bun.spawnSync([\\\\\\\"python3\\\\\\\",\\\\\\\"-B\\\\\\\",\\\\\\\"tools/validate_evidence.py\\\\\\\",\\\\\\\"--root\\\\\\\",\\\\\\\".\\\\\\\",\\\\\\\"--commit\\\\\\\",process.argv[1]],{env:{...process.env,PYTHONDONTWRITEBYTECODE:\\\\\\\"1\\\\\\\"}});process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode)' <tested-package-commit>`. It reads every JSON record below the evidence directory, prints each error, and exits 1 for invalid records or 0 for valid records. An empty directory has no invalid records and supplies no behavioral evidence.\\\\n\\\\nThe required registry file in `docs/parity/case-registry.json` declares applicability. Missing or non-file registry, unknown case, structural-only entry or unlisted host rejects behavioral validation. Maintenance fixtures use a temporary copy of this registry; they cannot bypass applicability. Required hosts must receive observed evidence or explicit blocked records before release claims. Structural checks have no required host and cannot populate host status. Later producers propose task-owned entries; only the coordinator integrates them. Source paths select callers through the task 3 case contract. Case definitions alone leave host statuses `not-run`.\\\\n\\\\n## Direct completion and recorded observations\\\\n\\\\n`direct` means the task is completed in the current context. Restatement, supplied-text writing and complete installed discovery can pass directly. `sequential` is reserved for replacing a required independent method with sequential work and remains reduced. A text response has no invented callable tool. Record supplied input, the actual response and qualitative outcome review as `nativeObservations`, each with its existing listed evidence artifact and named reviewer. Their labels are `supplied-input`, `response` and `review-outcome`. The reviewer assesses the case's expected outcome; validation checks evidence relationships and does not decide prose quality.\\\\n\\\\nEach registry entry declares allowed execution modes and required permissions for each status. A grant is required for the performed action: worker spawn, command execution and stop need execution; isolated output or persistence needs writes; external actions need their separate permission and prior identity. Read-only discovery does not inherit an execution grant requirement. Tool observations still name an actually exposed tool and existing evidence. Native observations cannot claim tool discovery, worker identity or saved writes.\\\\n\\\\nFull Arena and Swarm results additionally provide `inputRevision` and a listed `methodReceipt` artifact. An exposed `inspect-method` operation must reference that receipt. Assignment operations name `assignmentId` and the corresponding inspected output. See the [structured method contract](orchestration-contract.md). All positive maintenance fixtures are synthetic; none is an observed host result.\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/installed-source/case.json\\\",\\\"content\\\":\\\"{\\\\n  \\\\\\\"id\\\\\\\": \\\\\\\"trace-load\\\\\\\",\\\\n  \\\\\\\"sourcePaths\\\\\\\": [\\\\n    \\\\\\\"skills/principle-minimize-reader-load/SKILL.md\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"prompt\\\\\\\": \\\\\\\"Trace where invoice.total comes from through Controller -> InvoiceFacade -> InvoiceAdapter -> Calculator. The facade and adapter each have one caller and pass identical arguments. Calculator synchronizes a cached module total with invoice rows. Reduce indirection in this concrete path and explain what can change total.\\\\\\\",\\\\n  \\\\\\\"requirements\\\\\\\": [\\\\n    \\\\\\\"Read source and callers; writes and execution require available tools and authorization.\\\\\\\",\\\\n    \\\\\\\"Inspect both layers to trace and state to hold.\\\\\\\",\\\\n    \\\\\\\"Preserve meaningful abstraction boundaries and invariants.\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"expectedFull\\\\\\\": \\\\\\\"Inspect the concrete path and caller evidence. Collapse unnecessary one-caller and pass-through layers, keep boundaries that hide meaningful decisions, derive total from rows in a pure function or smaller state scope, and name the invariant once at the boundary. Explain where total comes from and what can change it. Verify authorized edits with observed checks; treat the under-30-second reader test as a criterion unless actually measured.\\\\\\\",\\\\n  \\\\\\\"expectedReduced\\\\\\\": \\\\\\\"With readable source but unavailable or denied writes or execution, give a source-grounded ordered proposal that reduces trace layers and hidden state. State which edits or checks were not performed and preserve permission limits.\\\\\\\",\\\\n  \\\\\\\"expectedBlocked\\\\\\\": \\\\\\\"Without readable source or sufficient caller and state evidence, identify the missing access or evidence and stop concrete refactoring and completion claims.\\\\\\\",\\\\n  \\\\\\\"forbiddenClaims\\\\\\\": [\\\\n    \\\\\\\"A structural validator pass proves host behavior or a measured reader time.\\\\\\\",\\\\n    \\\\\\\"Fewer lines alone prove reduced reader load.\\\\\\\",\\\\n    \\\\\\\"All abstraction layers should be removed regardless of interface compression.\\\\\\\",\\\\n    \\\\\\\"Unavailable writes or execution succeeded.\\\\\\\",\\\\n    \\\\\\\"Preserved invocation metadata proves host enforcement.\\\\\\\"\\\\n  ]\\\\n}\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/adapter.mjs\\\",\\\"content\\\":\\\"import { calculate } from './calculator.mjs';\\\\nexport function invoiceAdapter(invoice) { return calculate(invoice.rows); }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/calculator.mjs\\\",\\\"content\\\":\\\"let cachedTotal = 0;\\\\nexport function calculate(rows) {\\\\n  cachedTotal = rows.reduce((total, row) => total + row.qty * row.unitPrice, 0);\\\\n  return cachedTotal;\\\\n}\\\\nexport function inspectCachedTotal() { return cachedTotal; }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/controller.mjs\\\",\\\"content\\\":\\\"import { invoiceFacade } from './facade.mjs';\\\\nexport function invoiceController(invoice) { return { total: invoiceFacade(invoice) }; }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/decision.md\\\",\\\"content\\\":\\\"# Synthetic invoice decision record\\\\n\\\\nDisplay contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\\\\n\\\\nFixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatInvoice and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\\\\n\\\\nAuthorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/exporter.mjs\\\",\\\"content\\\":\\\"import { formatRows } from './formatter.mjs';\\\\nexport function exportAmounts(rows) { return formatRows(rows).join('\\\\\\\\n'); }\\\\nexport const publicFixtureSymbols = ['formatInvoice', 'formatRows'];\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/facade.mjs\\\",\\\"content\\\":\\\"import { invoiceAdapter } from './adapter.mjs';\\\\nexport function invoiceFacade(invoice) { return invoiceAdapter(invoice); }\\\\n\\\"}\\n{\\\"path\\\":\\\"trace-load/before/formatter.mjs\\\",\\\"content\\\":\\\"let lastFormatted = '';\\\\nfunction fixed(value) { return value.toFixed(2); }\\\\nexport function formatInvoice(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  lastFormatted = fixed(value);\\\\n  return lastFormatted;\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n  \"stderr\": \"\"\n}\n```\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/trace-load/before",
      "owner": "grades-native-05.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/trace-load/input.json",
      "owner": "grades-native-05.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/trace-load/source-manifest.json",
      "owner": "grades-native-05.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/trace-load/source-read",
      "owner": "grades-native-05.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/trace-load/work/calculator.mjs",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-05/trace-load/work/decision.md",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-05/trace-load/work/exporter.mjs",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-05/trace-load/work/formatter.mjs",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-05/trace-load/before",
      "owner": "grades-native-05.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/trace-load/input.json",
      "owner": "grades-native-05.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/trace-load/source-manifest.json",
      "owner": "grades-native-05.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/trace-load/source-read",
      "owner": "grades-native-05.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/trace-load/work/calculator.mjs",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-05/trace-load/work/decision.md",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-05/trace-load/work/exporter.mjs",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-05/trace-load/work/formatter.mjs",
      "owner": "grades-native-05.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/decision.md",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/exporter.mjs",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/formatter.mjs",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/rerun-03/trace-load/before",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/source-read.json",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-03/trace-load/installed-source",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/decision.md",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/exporter.mjs",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/rerun-03/trace-load/after/formatter.mjs",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/rerun-03/trace-load/before",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-03/trace-load/evidence/source-read.json",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-03/trace-load/installed-source",
      "owner": "grades-native-rerun-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
