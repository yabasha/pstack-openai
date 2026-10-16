# codex: dense-doc

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "dense-doc",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-00-01.json#14",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Rewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.",
  "caseDefinition": {
    "id": "dense-doc",
    "sourcePaths": [
      "skills/technical-writing/SKILL.md"
    ],
    "prompt": "Rewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.",
    "requirements": [
      "Read the supplied document and preserve its how-to purpose.",
      "Preserve budget.mjs, budget.json, --write, CI, the count condition, and the lower-only restriction.",
      "Apply all four layers and the unslop skill; do not invent facts."
    ],
    "expectedFull": "Remove filler, retain every named symbol and condition, and keep a clear how-to purpose. Apply Diátaxis, reader-directed sentences, STE rules, Global English, and unslop. Provide the rewrite or authorized document edit; propose any new abstract-metaphor offender with a diff without editing unslop.",
    "expectedReduced": "If required source text is incomplete or unslop is unavailable, identify the missing input or dependency and label the review partial. Returning the requested supplied-text rewrite in conversation is full direct completion; a specifically requested saved edit still requires an observed authorized write.",
    "expectedBlocked": "If no document text can be read or supplied, state the missing input and do not invent a rewrite or claim review completion.",
    "forbiddenClaims": [
      "Changing real symbol names or lower-only --write behavior.",
      "Claiming unslop was applied without reading it.",
      "Claiming edits were saved without observed authorized writes.",
      "Claiming host enforcement of disable-model-invocation metadata or host parity from structural validation."
    ],
    "caseFile": "docs/parity/cases/skills/technical-writing.json"
  },
  "registry": {
    "caseId": "dense-doc",
    "caseFile": "docs/parity/cases/skills/technical-writing.json",
    "sourcePaths": [
      "skills/technical-writing/SKILL.md"
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
        "supplied-input",
        "response",
        "review-outcome"
      ],
      "reduced-pass": [
        "supplied-input",
        "response",
        "review-outcome"
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
      "attemptId": "grades-native-00-01.json#14",
      "order": 0,
      "gradeFile": "grades-native-00-01.json",
      "rankWithinFile": 14,
      "host": "codex",
      "caseId": "dense-doc",
      "status": "pass",
      "grade": {
        "caseId": "dense-doc",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "rawTrace": "codex/batch-01.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_7",
          "item_35"
        ],
        "requiredObservationsMet": [
          "supplied-input",
          "response",
          "review-outcome"
        ],
        "missing": [],
        "review": "Actual rewrite preserves budget.json, budget.mjs, files importing protos, count-exceeds-budget CI failure, and lower-only --write restriction. Filler removed, instructions remain clear, and named four writing layers plus unslop are applied without invented behavior. Saved text is observed in item_35. No script execution or CI outcome is falsely claimed.",
        "concreteFixCandidates": [],
        "variantReview": [
          "Complete supplied-text rewrite reviewed semantically."
        ],
        "reviewedBy": "grade_contract_audit subagent; independent qualitative review of raw events and saved output",
        "responseArtifact": "fixtures/batch-01/dense-doc.result.md",
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
        "text": "# dense-doc\n\n## Supplied input\n\nRewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.\n\n- Read the supplied document and preserve its how-to purpose.\n- Preserve budget.mjs, budget.json, --write, CI, the count condition, and the lower-only restriction.\n- Apply all four layers and the unslop skill; do not invent facts.\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in dense-doc/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nThe saved rewrite is:\n\n> Use `budget.json` to configure the parameters for `budget.mjs`. The script counts files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only when lowering the budget.\n\nrewrite.md contains the actual output. I read the supplied paragraph and both technical-writing and unslop source files. Diataxis keeps the how-to as instructions toward configuration. Reader-directed style uses \"Use\" and \"Run\". STE keeps one instruction or fact per sentence. Global English removes the noun string and keeps \"only\" next to the lowering condition. Unslop removes \"In order to\" and \"It is important to note that\" without changing symbols or behavior.\n\nThe count still concerns files that import protos. The rewrite retains the supplied count-exceeds-budget condition for CI failure. The --write instruction still permits running it only when lowering the budget. The paragraph does not claim --write was executed or any real CI was contacted. No budget script was supplied, so behavioral verification here is a semantic review of text, not execution of that script.\n\nProposed catalog wording below is a draft only. The installed skill was not edited.\n\n```diff\n- ratchet (as metaphor)\n+ ratchet (as metaphor), ratchet budget (use \"a budget that only decreases\")\n```\n\nThis makes the existing catalog example explicit rather than claiming an undiscovered new term.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/technical-writing/SKILL.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/rewrite.md\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/task-revision.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n",
        "artifact": {
          "path": "fixtures/batch-01/dense-doc.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc.result.md",
          "sha256": "47d4866448db6a9c2efa5a2c8657458e12d7ac6225b619efcbece6fbaa10a31b",
          "bytes": 4999
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
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "047494b0b010d70d64a4a11b1150971de8b9218cba6b8739d0ee628e93911448"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e3ccc3c8b81e142a436053124d546f73d54e6b4410a0a78c2fa9100bbcd069a0",
                "commandResult": {
                  "exitCode": 0
                }
              },
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
                "eventId": "item_35",
                "line": 66,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "86433876cf31d86bb93517e58353765bfb14f99725b600f312d52c8c9cbf1ae2"
              },
              {
                "eventId": "item_35",
                "line": 67,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b7f93f43f6972b87c63eb2b1027bb32dee8b2be96f08cf14b270341f68fd9efc",
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
            "item_7",
            "item_35"
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
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-01/dense-doc/host.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/host.json",
      "sha256": "f5790ac28ba365d2b8731974bf80a70ab30b3fc454e0cba68f386664f542625c",
      "bytes": 271,
      "owners": [
        "grades-native-00-01.json#14"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/dense-doc/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-case.json",
      "sha256": "8367029d4ba6d0ca90b36ee5b91de772922568cff29c0e1162e31ec6fcd3f160",
      "bytes": 752,
      "owners": [
        "grades-native-00-01.json#14"
      ],
      "text": "{\n  \"caseId\": \"dense-doc\",\n  \"caseFile\": \"docs/parity/cases/skills/technical-writing.json\",\n  \"sourcePaths\": [\n    \"skills/technical-writing/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"supplied-input\",\n      \"response\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"supplied-input\",\n      \"response\",\n      \"review-outcome\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/batch-01/dense-doc/rewrite.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/rewrite.md",
      "sha256": "a40e9a619be387ca485a90ecf33150b6d4a281f18630cb2aeccdb8ac8099ae17",
      "bytes": 207,
      "owners": [
        "grades-native-00-01.json#14"
      ],
      "text": "Use `budget.json` to configure the parameters for `budget.mjs`. The script counts files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only when lowering the budget.\n"
    },
    {
      "path": "fixtures/batch-01/dense-doc/task-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/task-revision.json",
      "sha256": "51ada73cb6041642327aa5d3002ab20185805394dbd63dd106632fc69187ceb3",
      "bytes": 348,
      "owners": [
        "grades-native-00-01.json#14"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/dense-doc.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc.result.md",
      "sha256": "47d4866448db6a9c2efa5a2c8657458e12d7ac6225b619efcbece6fbaa10a31b",
      "bytes": 4999,
      "owners": [
        "grades-native-00-01.json#14"
      ],
      "text": "# dense-doc\n\n## Supplied input\n\nRewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.\n\n- Read the supplied document and preserve its how-to purpose.\n- Preserve budget.mjs, budget.json, --write, CI, the count condition, and the lower-only restriction.\n- Apply all four layers and the unslop skill; do not invent facts.\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in dense-doc/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nThe saved rewrite is:\n\n> Use `budget.json` to configure the parameters for `budget.mjs`. The script counts files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only when lowering the budget.\n\nrewrite.md contains the actual output. I read the supplied paragraph and both technical-writing and unslop source files. Diataxis keeps the how-to as instructions toward configuration. Reader-directed style uses \"Use\" and \"Run\". STE keeps one instruction or fact per sentence. Global English removes the noun string and keeps \"only\" next to the lowering condition. Unslop removes \"In order to\" and \"It is important to note that\" without changing symbols or behavior.\n\nThe count still concerns files that import protos. The rewrite retains the supplied count-exceeds-budget condition for CI failure. The --write instruction still permits running it only when lowering the budget. The paragraph does not claim --write was executed or any real CI was contacted. No budget script was supplied, so behavioral verification here is a semantic review of text, not execution of that script.\n\nProposed catalog wording below is a draft only. The installed skill was not edited.\n\n```diff\n- ratchet (as metaphor)\n+ ratchet (as metaphor), ratchet budget (use \"a budget that only decreases\")\n```\n\nThis makes the existing catalog example explicit rather than claiming an undiscovered new term.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/technical-writing/SKILL.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/rewrite.md\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/task-revision.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-01/dense-doc/input.json",
      "owner": "grades-native-00-01.json#14",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/dense-doc/registered-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-input.json",
      "sha256": "463b55469b57a23ef1ae3891743ac127b44edbedf9816648441c669a3d3f8a63",
      "bytes": 1809,
      "owner": "grades-native-00-01.json#14",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
    },
    {
      "path": "fixtures/batch-01/dense-doc/source",
      "owner": "grades-native-00-01.json#14",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/dense-doc/source-manifest.json",
      "owner": "grades-native-00-01.json#14",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/dense-doc/input.json",
      "owner": "grades-native-00-01.json#14",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/dense-doc/registered-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/dense-doc/registered-input.json",
      "sha256": "463b55469b57a23ef1ae3891743ac127b44edbedf9816648441c669a3d3f8a63",
      "bytes": 1809,
      "owner": "grades-native-00-01.json#14",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
    },
    {
      "path": "fixtures/batch-01/dense-doc/source",
      "owner": "grades-native-00-01.json#14",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/dense-doc/source-manifest.json",
      "owner": "grades-native-00-01.json#14",
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
