# codex: codex-setup-from-readme

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "codex-setup-from-readme",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-00-01.json#11",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Start in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.",
  "caseDefinition": {
    "id": "codex-setup-from-readme",
    "sourcePaths": [
      "docs/guide/01-setup.md"
    ],
    "prompt": "Start in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/setup/codex.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery."
    ],
    "expectedFull": "After separately authorized supported loading, observe actual package discovery, exact installed-copy identity and all 51 root skills with three Benny exclusions. With required authorized tools, follow every documented phase and retain inspected artifact evidence at the exact frozen SHA.",
    "expectedReduced": "Readable marketplace instructions support a bounded walkthrough only. Without authorized loading and actual installed-copy discovery, report that setup remains unobserved.",
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
    "caseId": "codex-setup-from-readme",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
    "sourcePaths": [
      "docs/guide/01-setup.md"
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
      "attemptId": "grades-native-00-01.json#11",
      "order": 0,
      "gradeFile": "grades-native-00-01.json",
      "rankWithinFile": 11,
      "host": "codex",
      "caseId": "codex-setup-from-readme",
      "status": "reduced-pass",
      "grade": {
        "caseId": "codex-setup-from-readme",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-01.events.jsonl",
        "actualReadEventIds": [
          "item_10",
          "item_12",
          "item_23"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Fresh uninstalled host starting state not observed.",
          "Supported loading, 51-skill enumeration, three exclusions and installed-copy commit identity unobserved."
        ],
        "review": "Actual Codex execution followed README links and read full setup/support contracts. This is the expected bounded read-only walkthrough. Fresh uninstalled starting state was not established. item_19/20 UI inspection was denied; the ChatGPT request returned a denial naming Codex, correctly not treated as independent ChatGPT host evidence. No loading or account change was attempted.",
        "concreteFixCandidates": [],
        "variantReview": [
          "Read-only navigation completed.",
          "UI inspection denied; loading and discovery remain blocked."
        ],
        "reviewedBy": "grade_contract_audit subagent; independent qualitative review of raw events and saved output",
        "responseArtifact": "fixtures/batch-01/codex-setup-from-readme.result.md",
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
        "text": "# codex-setup-from-readme\n\n## Supplied input\n\nStart in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.\n\n- Starting state and exact action are in the prompt. README must link docs/setup/codex.md and the destination must exist.\n- Read the full linked workflow and required contracts before dependent work.\n- Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\n- Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in codex-setup-from-readme/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nThe requested starting state was not established. This evaluation runs in an existing tool-enabled conversation that already advertises the 0.1.0 package. I did not uninstall it, create a new enabled chat, restart an app, or alter controls. The \"no installed package\" or \"fresh chat\" condition is supplied scenario text, not a host-enforced starting state.\n\nREADME.md links docs/setup/codex.md and the destination exists. I followed that local link and read the complete guide, compatibility page, preserved setup guide and required capability, ownership, model and assignment contracts. The source snapshots and hashes are retained. The frozen Codex guide documents .agents/plugins/marketplace.json with a relative source.path, followed by a desktop restart, source selection in Plugins Directory, installation and a new enabled chat. This is documented guidance, not an observed route in this account.\n\nI attempted read-only native inspection with mcp__cua_repl.js. ui-observation.json preserves the exact call and the response excerpt: Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons. No Codex accessibility state or plugin controls were returned. No alternate UI mechanism was used to bypass that denial. No screenshot was captured.\n\nLoading, enabling, discovery enumeration and installed-copy inspection remain unobserved. The exact setup authorization is absent and the user forbids changes. I did not invoke an installation request or modify marketplace files, settings, credentials, caches or dependencies. A release listing or generic plugin-creation tool would not inspect this local host installation. No live service was contacted to substitute for native controls.\n\nplugin.json reports version 0.1.0. The exact source freeze supplied by the user is f4623636a287bea2aa79c4b2234a53d20a5f193c. The cache contains no .git, so I cannot independently prove that these bytes correspond to that commit. source-manifest.json retains actual byte hashes. The 51-root and three Benny-exclusion requirements remain future comparison requirements, not a discovery receipt from this run.\n\nThe observed host supports local file reads, case-local writes, Bun execution and readback. Native app control was denied. collaboration operations are exposed but no worker was spawned or assigned a revision. Requested and observed worker models are therefore not applicable. Task-revision.json records the absence of a task Git repository. Result artifacts and source snapshot hashes were read back. There are no assignment revisions or installed discovery artifacts to inspect. The setup branch stays blocked at UI inspection and authorization; source navigation alone proves no installed discovery.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/01-setup.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/ui-observation.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/task-revision.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n",
        "artifact": {
          "path": "fixtures/batch-01/codex-setup-from-readme.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme.result.md",
          "sha256": "9cc651d5019a634f4f2a6023c4e67b2523711ae1ceb1a61bb327480e4372f7c2",
          "bytes": 6529
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
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "567a437ff1a3230a7baab276b2dd1015048e5e2b138a5e77c7e7ee19d06d3e7a"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "226851c11ad34fa893e06483cd0492af239406e967ad929103ff205faf0fbd61",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 43,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "26a8362a7b3ba37fc046d65c8d945509382ae4393a5b0ed34c90835295420cd9"
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8d6322c83da10dec7e191e915a56d6c70d60c677ab4b80ac84252ec3be98a2cb",
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
            "item_10",
            "item_12",
            "item_23"
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
      "path": "fixtures/batch-01/codex-setup-from-readme/host.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/host.json",
      "sha256": "9662350ba3b2bebc8a721b0aae189b679001a2b567b605df3ab057842b48fd14",
      "bytes": 285,
      "owners": [
        "grades-native-00-01.json#11"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/registered-case.json",
      "sha256": "fa8bd8ea2c5cc4752120c99e96c373f077690ee61f460dc012fb3547da056585",
      "bytes": 677,
      "owners": [
        "grades-native-00-01.json#11"
      ],
      "text": "{\n  \"caseId\": \"codex-setup-from-readme\",\n  \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\",\n  \"sourcePaths\": [\n    \"docs/guide/01-setup.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/registered-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/registered-input.json",
      "sha256": "08c755c9574c76ce5b6f922e924e983a2266b6469dfc637bd80d37226478c8bf",
      "bytes": 13269,
      "owners": [
        "grades-native-00-01.json#11"
      ],
      "text": "[\n  {\n    \"id\": \"chatgpt-setup-from-readme\",\n    \"sourcePaths\": [\n      \"docs/guide/01-setup.md\"\n    ],\n    \"prompt\": \"Start in personal ChatGPT without an installed pstack package. Follow README to the ChatGPT setup page; inspect available loading controls without changing them.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/setup/chatgpt.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\"\n    ],\n    \"expectedFull\": \"Only after the personal route is actually exposed and separately authorized, observe supported loading and complete installed discovery with all 51 roots, three Benny exclusions, exact installed-copy identity, version and final frozen SHA. Do not infer account access from official documentation.\",\n    \"expectedReduced\": \"Readable supplied setup instructions support a bounded walkthrough only. Unavailable supported loading or installed-copy discovery remains blocked; source reading proves no registration.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ]\n  },\n  {\n    \"id\": \"codex-setup-from-readme\",\n    \"sourcePaths\": [\n      \"docs/guide/01-setup.md\"\n    ],\n    \"prompt\": \"Start in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/setup/codex.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\"\n    ],\n    \"expectedFull\": \"After separately authorized supported loading, observe actual package discovery, exact installed-copy identity and all 51 root skills with three Benny exclusions. With required authorized tools, follow every documented phase and retain inspected artifact evidence at the exact frozen SHA.\",\n    \"expectedReduced\": \"Readable marketplace instructions support a bounded walkthrough only. Without authorized loading and actual installed-copy discovery, report that setup remains unobserved.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ]\n  },\n  {\n    \"id\": \"arena-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/arena/SKILL.md\"\n    ],\n    \"prompt\": \"Start with an authorized disposable local artifact and exact input SHA. Follow README to Arena and compare two proposals for a cache API.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/workflows/arena.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Follow Frame, Fan out, Cross-judge, Pick, Graft and Verify. Keep a parent-only 3-6 criterion rubric from candidates; inspect all terminal candidates before the fresh read-only judge.\"\n    ],\n    \"expectedFull\": \"Two authorized independent isolated candidates and rationales are inspected at the exact input SHA. A fresh read-only judge scores the rubric after candidates finish. The parent reads every candidate, picks a base, records grafts/rejections/dropouts and verifies one synthesis with an adjacent note.\",\n    \"expectedReduced\": \"Sequential proposals and parent comparison may return a useful reduced synthesis. Missing independent candidates or a fresh later judge prevents full Arena; retain candidate, comparison and verification artifacts.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ]\n  },\n  {\n    \"id\": \"swarm-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/swarm/SKILL.md\"\n    ],\n    \"prompt\": \"Start with an authorized disposable local artifact and exact input SHA. Follow README to Swarm and partition a three-file source review.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/workflows/swarm.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Declare partition/race/mixed shape, N and first pass/rank all/best-of when relevant before dispatch. Include full SHA and method; reject incomplete results, allow at most one inspected retry and retain uncovered slices as gaps.\"\n    ],\n    \"expectedFull\": \"Three independent authorized slice results cover the three fixture files at the exact SHA and method. The coordinator inspects terminal artifacts and returns one consolidated table with evidenced issues and explicit gaps/dropouts. Cancellation requires observed stop, terminal inspection and quarantine.\",\n    \"expectedReduced\": \"Sequential review of the declared three-file partition may return reduced findings with exact revisions, inspected artifacts and visible missing slices. It proves neither independent workers nor a race.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ]\n  },\n  {\n    \"id\": \"poteto-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/SKILL.md\"\n    ],\n    \"prompt\": \"Start with a read-only architecture question and an explicit active controller. Follow README to Poteto mode and select Investigation.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/workflows/poteto-mode.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Resolve controller ownership before work. Read the full mode, Investigation playbook, routed how contracts and every applied principle leaf. Copy exact steps or explicit skips; preserve the read-only checkpoint and Investigation no-PR exception.\"\n    ],\n    \"expectedFull\": \"The active owner produces a cited read-only architecture explanation using inspected read-only worker results, with the Investigation checkpoint and actual capability limits. Principles named in the answer were read in full. No implementation, PR or babysit starts.\",\n    \"expectedReduced\": \"A reduced foreground run can preserve routing, the checkpoint and an inspected local artifact. Missing independent workers, controls or persistence stays explicit; no unattended completion is claimed.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ]\n  },\n  {\n    \"id\": \"upstream-update-walkthrough\",\n    \"sourcePaths\": [\n      \"skills/how/SKILL.md\",\n      \"LICENSE\"\n    ],\n    \"prompt\": \"Start with a clean owned disposable package worktree and an exact candidate SHA. Follow README to upstream updates and rehearse check, prepare, apply, validate, separate acceptance and next update using fixtures only.\",\n    \"requirements\": [\n      \"Starting state and exact action are in the prompt. README must link docs/maintenance/upstream-updates.md and the destination must exist.\",\n      \"Read the full linked workflow and required contracts before dependent work.\",\n      \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n      \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n      \"Use injected offline source fixtures and owned linked worktrees. Inspect accepted-baseline receipt/digests and report version 2; preserve exact draft/resolved bytes, actionable resolution version 2, higher version and exhaustive ownership. Exact apply approval is separate from acceptance; verify accepted A then next check/prepare B and block unaccepted or tampered A.\"\n    ],\n    \"expectedFull\": \"Offline structural rehearsal follows the documented check/prepare review, exact approved apply and package/evidence/release validation. An explicit separate reviewed acceptance receipt binds the manifest, ancestor package identity and nonempty evidence digests before the next update. Fixtures prove tooling behavior only; both actual hosts remain unobserved.\",\n    \"expectedReduced\": \"A read-only review or safe preview identifies missing approval, source identity, ownership, state compatibility or host evidence. The operative package remains intact; neither apply, acceptance nor rollback is claimed.\",\n    \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n    \"forbiddenClaims\": [\n      \"Links or direct source reads prove installed discovery.\",\n      \"Sequential roles are independent workers.\",\n      \"An isolated helper snapshot proves this candidate or host passed.\",\n      \"A resolution file, owner marker or upstream autonomy grants approval.\",\n      \"Apply automatically accepts an update or refreshes a host.\"\n    ]\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/task-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/task-revision.json",
      "sha256": "3d2f313118ab3a3934236d711416933fdfdc312adcf877fda373f40ece3204b6",
      "bytes": 362,
      "owners": [
        "grades-native-00-01.json#11"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"args\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/ui-observation.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/ui-observation.json",
      "sha256": "c190f6841be85f54d3388ee61e9692f232e700fb4f75f9af499ba8c620bbcd4f",
      "bytes": 341,
      "owners": [
        "grades-native-00-01.json#11"
      ],
      "text": "{\n  \"tool\": \"mcp__cua_repl.js\",\n  \"code\": \"let app = await cua.getApp(\\\"Codex\\\");\",\n  \"observedResponse\": \"Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons.\",\n  \"kind\": \"verbatim tool response excerpt transcribed from this run\",\n  \"screenshot\": null,\n  \"limits\": \"No app state or loading controls observed.\"\n}"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme.result.md",
      "sha256": "9cc651d5019a634f4f2a6023c4e67b2523711ae1ceb1a61bb327480e4372f7c2",
      "bytes": 6529,
      "owners": [
        "grades-native-00-01.json#11"
      ],
      "text": "# codex-setup-from-readme\n\n## Supplied input\n\nStart in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.\n\n- Starting state and exact action are in the prompt. README must link docs/setup/codex.md and the destination must exist.\n- Read the full linked workflow and required contracts before dependent work.\n- Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\n- Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\n\n## Package and authorization\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 version 0.1.0 supplied workflow instructions. Supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c. The Git identity of this cache is unverified; actual file hashes appear in codex-setup-from-readme/source-manifest.json. No 0.2.1 file was read. No personal history or live services were used. One unrelated controller startup skill was read during initial setup, but did not take ownership or supply this case's workflow. No separate controller ran.\n\nCase-local writes and Bun execution authorized. External writes, live services, installs, configuration changes, commits, pushes, publishing and schedules forbidden.\n\n## Actual response and variants\n\nThe requested starting state was not established. This evaluation runs in an existing tool-enabled conversation that already advertises the 0.1.0 package. I did not uninstall it, create a new enabled chat, restart an app, or alter controls. The \"no installed package\" or \"fresh chat\" condition is supplied scenario text, not a host-enforced starting state.\n\nREADME.md links docs/setup/codex.md and the destination exists. I followed that local link and read the complete guide, compatibility page, preserved setup guide and required capability, ownership, model and assignment contracts. The source snapshots and hashes are retained. The frozen Codex guide documents .agents/plugins/marketplace.json with a relative source.path, followed by a desktop restart, source selection in Plugins Directory, installation and a new enabled chat. This is documented guidance, not an observed route in this account.\n\nI attempted read-only native inspection with mcp__cua_repl.js. ui-observation.json preserves the exact call and the response excerpt: Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons. No Codex accessibility state or plugin controls were returned. No alternate UI mechanism was used to bypass that denial. No screenshot was captured.\n\nLoading, enabling, discovery enumeration and installed-copy inspection remain unobserved. The exact setup authorization is absent and the user forbids changes. I did not invoke an installation request or modify marketplace files, settings, credentials, caches or dependencies. A release listing or generic plugin-creation tool would not inspect this local host installation. No live service was contacted to substitute for native controls.\n\nplugin.json reports version 0.1.0. The exact source freeze supplied by the user is f4623636a287bea2aa79c4b2234a53d20a5f193c. The cache contains no .git, so I cannot independently prove that these bytes correspond to that commit. source-manifest.json retains actual byte hashes. The 51-root and three Benny-exclusion requirements remain future comparison requirements, not a discovery receipt from this run.\n\nThe observed host supports local file reads, case-local writes, Bun execution and readback. Native app control was denied. collaboration operations are exposed but no worker was spawned or assigned a revision. Requested and observed worker models are therefore not applicable. Task-revision.json records the absence of a task Git repository. Result artifacts and source snapshot hashes were read back. There are no assignment revisions or installed discovery artifacts to inspect. The setup branch stays blocked at UI inspection and authorization; source navigation alone proves no installed discovery.\n\n## Real tools, actions and artifacts\n\nReads and commands used functions.exec with tools.exec_command. Writes used tools.apply_patch and Bun filesystem calls. run-cases.mjs contains the actual fixture preparation, commands, assertions and mutation order. write-results.mjs saves the current report and transcribed UI excerpts. Bun version and command exit/output receipts are case-owned JSON. Every shared fixture was copied into the case before inspection or editing. New slugify and denial inputs are explicitly constructed inert examples. The package source was never edited.\n\nNamed source files read and retained:\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/01-setup.md\n\nAdditional required contract reads and digests are in the manifest. The exact registered requirements are retained in registered-input.json and registry metadata in registered-case.json. No host status or registry grade was changed.\n\nCase artifacts:\n\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/source-manifest.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/host.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/registered-input.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/registered-case.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/ui-observation.json\n- /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-01/codex-setup-from-readme/task-revision.json\n\n## Limits\n\nThis report assigns no pass grade. Execution is direct in this host, not a second host run, independent review or a recorded native worker method. Native workers are exposed but were not required for these bounded direct cases. Source metadata does not prove host enforcement. Source reads, inert data, search results, file permissions and local tests do not prove external service access or installed discovery. No commits, pushes, PRs, issues, messages, installations, publishing or schedules occurred.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/input.json",
      "owner": "grades-native-00-01.json#11",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/source",
      "owner": "grades-native-00-01.json#11",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/source-manifest.json",
      "owner": "grades-native-00-01.json#11",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/input.json",
      "owner": "grades-native-00-01.json#11",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/source",
      "owner": "grades-native-00-01.json#11",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-01/codex-setup-from-readme/source-manifest.json",
      "owner": "grades-native-00-01.json#11",
      "reason": "copied source/input or administrative evaluator helper"
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
