# codex: route-recipe

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "route-recipe",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-04.json#5",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.",
  "caseDefinition": {
    "id": "route-recipe",
    "sourcePaths": [
      "skills/poteto-help/SKILL.md",
      "skills/poteto-help/references/prompting.md",
      "skills/poteto-help/references/recipes.md"
    ],
    "prompt": "Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.",
    "requirements": [
      "Read the selected local leaf and Bug fix playbook before recommending their details.",
      "Provide at most one concrete prompt, the source link, and the relevant verification requirement.",
      "Check whether the referenced playbook and app verification tool exist; disclose pending or missing dependencies.",
      "For any customization follow-up, explain source options but gate personal-mode drafting and custom skill edits on reviewed dispositions for the complete baseline and observed supported behavior or explicit blocks for each host, independently of authorization."
    ],
    "expectedFull": "Route to the existing reviewed Bug fix playbook under poteto-mode, provide one reproduction-and-verification recipe and a source link, and do not start a help-only run.",
    "expectedReduced": "When app verification is unavailable, offer only the checks actually supported, label the reduction, and do not promise a video or independent workers. If the playbook is pending, identify its source route as pending rather than claim an existing port.",
    "expectedBlocked": "When the selected local playbook cannot be read, report that routing cannot yet establish an existing ported recipe. Give the pinned source reference and explain the missing local dependency without starting work.",
    "forbiddenClaims": [
      "A recipe proves host behavior passed.",
      "Cursor modes, slash commands, model rules or loop APIs are registered on this host.",
      "Missing local playbooks are existing reviewed ports.",
      "A help question authorizes execution, installation, external writes or scheduling.",
      "User authorization alone permits personal customization before complete baseline review and per-host evidence or explicit blocks."
    ],
    "caseFile": "docs/parity/cases/skills/poteto-help.json"
  },
  "registry": {
    "caseId": "route-recipe",
    "caseFile": "docs/parity/cases/skills/poteto-help.json",
    "sourcePaths": [
      "skills/poteto-help/SKILL.md",
      "skills/poteto-help/references/prompting.md",
      "skills/poteto-help/references/recipes.md"
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
      "attemptId": "grades-native-04.json#5",
      "order": 0,
      "gradeFile": "grades-native-04.json",
      "rankWithinFile": 5,
      "host": "codex",
      "caseId": "route-recipe",
      "status": "reduced-pass",
      "grade": {
        "caseId": "route-recipe",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-04.events.jsonl",
        "actualReadEventIds": [
          "item_9",
          "item_13"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Matching app verification tool/target absent; runtime proof blocked."
        ],
        "review": "Reads help/recipe/Bugfix and gives one bounded prompt plus source link. Does not start bug work. Actual app verifier/recording route absent, and future video is conditional, not a tool support claim.",
        "responseArtifact": "fixtures/batch-04/route-recipe.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-04.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Route to the existing reviewed Bug fix playbook under poteto-mode, provide one reproduction-and-verification recipe and a source link, and do not start a help-only run.",
        "reducedExpected": "When app verification is unavailable, offer only the checks actually supported, label the reduction, and do not promise a video or independent workers. If the playbook is pending, identify its source route as pending rather than claim an existing port."
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
        "text": "# route-recipe\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"route-recipe\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/references/prompting.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/references/recipes.md\"\n  ],\n  \"prompt\": \"Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.\",\n  \"requirements\": [\n    \"Read the selected local leaf and Bug fix playbook before recommending their details.\",\n    \"Provide at most one concrete prompt, the source link, and the relevant verification requirement.\",\n    \"Check whether the referenced playbook and app verification tool exist; disclose pending or missing dependencies.\",\n    \"For any customization follow-up, explain source options but gate personal-mode drafting and custom skill edits on reviewed dispositions for the complete baseline and observed supported behavior or explicit blocks for each host, independently of authorization.\"\n  ]\n}\n```\n\n## Actual response and output\n\nUse /poteto-mode with its Bug fix playbook. The local mode, help references and Bug fix playbook exist and were read. The workflow requires reproduction and verification on the same app surface with the original trigger, actual before-and-after evidence and explicit verification gaps.\n\n```text\n/poteto-mode Reproduce the reported app bug with the project's app verification tool first. If it reproduces on the current main revision, fix the observed cause and verify the original flow on the same surface. Show the failing and passing evidence, and a video if supported. Stop at a reviewable local diff. Do not commit, publish, send messages or open a PR.\n```\n\nThe prompt follows the installed recipe source, whose public copy is https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-help/references/recipes.md . The local authority is [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/source-manifest.json) and the Bug fix contract at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/bug-fix.md . No public page was contacted.\n\nNo app, app target, verify-<app> skill or project app harness was supplied. The scoped project verifier search returned no matches. Generic browser controls are exposed in this session, but no matching app control or recording operation was exercised. The package contains create-verification-skill instructions, which are a preparation route, not an existing app driver. Its source was checked for existence only. /control-ui and /control-cli are companion names, not verified installed tools in the tested package. App reproduction and video proof remain pending those concrete dependencies. No bug work was started.\n\nFor a later customization request, source options are automate-me for a personal mode, reflect for approved lesson edits, or the authoring playbook for a custom workflow. Drafting a personal mode or editing a custom skill stays gated on reviewed dispositions for the complete baseline inventory and observed supported behavior or explicit blocks for every target host. Separate authorization is also required. This run has no complete reviewed baseline and makes no such edits.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/.\n\n\nCommand: `rg --files -g *verify* -g *control* .`. Exit 1. Full receipt: [project-verifier-discovery.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/project-verifier-discovery.receipt.json).\n\n```text\n```\n\n\n## Variants and limits\n\nHelp-only response supplied one prompt. Source route exists; matching app target and verifier are missing. Work was not started. Customization prerequisite is explained, with no draft or custom skill edits.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-04/route-recipe.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe.result.md",
          "sha256": "b5b79927ea012d7c2af8a271a424039a5388d1f367dcbfb8cd9457d6a18089ee",
          "bytes": 5779
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-04.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-04.events.jsonl",
            "sha256": "614c212bfe1cb1201ad58cdd814f4bcd05080cd9c2ba5fc9f09a7127c3730143",
            "bytes": 382761,
            "eventReferences": [
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5e68f6c63dd171f3cd184db54ff1764f17400129ed8e1b8da3d52ac55d105453"
              },
              {
                "eventId": "item_9",
                "line": 18,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "3cf052e9f56e311320461c7d585c328a06c9ca136df994c52c6388a4728c9931",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f7be0cbe189e575c1f6d473c8d3cac562bde8c2e0d74e5bf96526a79c2073a55"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c83c9cc100dc0efc6392cb166b88bfdf590650afab2a21a8736fd06341c9f542",
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
            "item_13"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-04.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-04/route-recipe/dependency-discovery.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/dependency-discovery.json",
      "sha256": "2b7688eb4024352cd73d211a0b52b5f0f754cbaa80f131a71b2f97c8fdfaa729",
      "bytes": 258,
      "owners": [
        "grades-native-04.json#5"
      ],
      "text": "{\n  \"modeExists\": true,\n  \"bugFixPlaybookExists\": true,\n  \"createVerificationSkillExists\": true,\n  \"packageControlUiExists\": false,\n  \"packageControlCliExists\": false,\n  \"appTargetSupplied\": false,\n  \"appDriverExecuted\": false,\n  \"liveServicesUsed\": false\n}\n"
    },
    {
      "path": "fixtures/batch-04/route-recipe/project-verifier-discovery.receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/project-verifier-discovery.receipt.json",
      "sha256": "3c8a8005aa4bd271aa4712af307d17d55c421dfeaa38eee44c36e77e96d4b277",
      "bytes": 326,
      "owners": [
        "grades-native-04.json#5"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"argv\": [\n    \"rg\",\n    \"--files\",\n    \"-g\",\n    \"*verify*\",\n    \"-g\",\n    \"*control*\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-04/route-recipe/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/readback.json",
      "sha256": "becc6aa2b35759408c6615b03bf464158b010924df75b8a422d1a72a1823f24a",
      "bytes": 246,
      "owners": [
        "grades-native-04.json#5"
      ],
      "text": "{\n  \"report\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe.result.md\",\n  \"sha256\": \"b5b79927ea012d7c2af8a271a424039a5388d1f367dcbfb8cd9457d6a18089ee\",\n  \"readbackMatched\": true,\n  \"persisted\": []\n}\n"
    },
    {
      "path": "fixtures/batch-04/route-recipe.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe.result.md",
      "sha256": "b5b79927ea012d7c2af8a271a424039a5388d1f367dcbfb8cd9457d6a18089ee",
      "bytes": 5779,
      "owners": [
        "grades-native-04.json#5"
      ],
      "text": "# route-recipe\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"route-recipe\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/references/prompting.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/references/recipes.md\"\n  ],\n  \"prompt\": \"Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.\",\n  \"requirements\": [\n    \"Read the selected local leaf and Bug fix playbook before recommending their details.\",\n    \"Provide at most one concrete prompt, the source link, and the relevant verification requirement.\",\n    \"Check whether the referenced playbook and app verification tool exist; disclose pending or missing dependencies.\",\n    \"For any customization follow-up, explain source options but gate personal-mode drafting and custom skill edits on reviewed dispositions for the complete baseline and observed supported behavior or explicit blocks for each host, independently of authorization.\"\n  ]\n}\n```\n\n## Actual response and output\n\nUse /poteto-mode with its Bug fix playbook. The local mode, help references and Bug fix playbook exist and were read. The workflow requires reproduction and verification on the same app surface with the original trigger, actual before-and-after evidence and explicit verification gaps.\n\n```text\n/poteto-mode Reproduce the reported app bug with the project's app verification tool first. If it reproduces on the current main revision, fix the observed cause and verify the original flow on the same surface. Show the failing and passing evidence, and a video if supported. Stop at a reviewable local diff. Do not commit, publish, send messages or open a PR.\n```\n\nThe prompt follows the installed recipe source, whose public copy is https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-help/references/recipes.md . The local authority is [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/source-manifest.json) and the Bug fix contract at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/bug-fix.md . No public page was contacted.\n\nNo app, app target, verify-<app> skill or project app harness was supplied. The scoped project verifier search returned no matches. Generic browser controls are exposed in this session, but no matching app control or recording operation was exercised. The package contains create-verification-skill instructions, which are a preparation route, not an existing app driver. Its source was checked for existence only. /control-ui and /control-cli are companion names, not verified installed tools in the tested package. App reproduction and video proof remain pending those concrete dependencies. No bug work was started.\n\nFor a later customization request, source options are automate-me for a personal mode, reflect for approved lesson edits, or the authoring playbook for a custom workflow. Drafting a personal mode or editing a custom skill stays gated on reviewed dispositions for the complete baseline inventory and observed supported behavior or explicit blocks for every target host. Separate authorization is also required. This run has no complete reviewed baseline and makes no such edits.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/.\n\n\nCommand: `rg --files -g *verify* -g *control* .`. Exit 1. Full receipt: [project-verifier-discovery.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/route-recipe/project-verifier-discovery.receipt.json).\n\n```text\n```\n\n\n## Variants and limits\n\nHelp-only response supplied one prompt. Source route exists; matching app target and verifier are missing. Work was not started. Customization prerequisite is explained, with no draft or custom skill edits.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-04/route-recipe/additional-source-reads.json",
      "owner": "grades-native-04.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/route-recipe/fixture-README.md",
      "owner": "grades-native-04.json#5",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/route-recipe/input.json",
      "owner": "grades-native-04.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/route-recipe/source-manifest.json",
      "owner": "grades-native-04.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/route-recipe/additional-source-reads.json",
      "owner": "grades-native-04.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/route-recipe/fixture-README.md",
      "owner": "grades-native-04.json#5",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/route-recipe/input.json",
      "owner": "grades-native-04.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/route-recipe/source-manifest.json",
      "owner": "grades-native-04.json#5",
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
