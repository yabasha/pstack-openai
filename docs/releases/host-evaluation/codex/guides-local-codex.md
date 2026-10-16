# codex: guides-local-codex

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "guides-local-codex",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-02.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Use pstack in local Codex with authorized repository access.",
  "caseDefinition": {
    "id": "guides-local-codex",
    "sourcePaths": [
      "docs/guide/01-setup.md",
      "docs/guide/02-poteto-mode.md",
      "docs/guide/03-understand.md",
      "docs/guide/04-design.md",
      "docs/guide/05-build-and-clean.md",
      "docs/guide/06-verify-and-ship.md",
      "docs/guide/07-overnight.md",
      "docs/guide/08-principles.md",
      "docs/guide/09-make-it-yours.md",
      "docs/guide/10-recipes-and-pitfalls.md",
      "docs/guide/README.md",
      "docs/guide/images/design.jpg",
      "docs/guide/images/overnight.jpg",
      "docs/guide/images/recipes.jpg",
      "docs/guide/images/router.jpg",
      "docs/guide/images/understanding.jpg",
      "docs/guide/images/verification.jpg"
    ],
    "prompt": "Use pstack in local Codex with authorized repository access.",
    "requirements": [
      "Read the matching guide and host capability contract.",
      "Preserve the active controller and explicit permission gates."
    ],
    "expectedFull": "Perform only authorized operations supported by observed tools; report exact artifacts and actual model values or unknown.",
    "expectedReduced": "Observe read, isolated-write and execution separately; supported loading remains unverified until tested through the host.",
    "expectedBlocked": "Name every required absent or denied operation and leave its acceptance claim blocked.",
    "forbiddenClaims": [
      "Reading installed files proves supported host loading.",
      "Sequential roles are independent workers.",
      "A diagram or setup draft proves tools exist.",
      "Upstream autonomy authorizes installation, settings, schedules or external actions."
    ],
    "caseFile": "docs/parity/cases/guides.json"
  },
  "registry": {
    "caseId": "guides-local-codex",
    "caseFile": "docs/parity/cases/guides.json",
    "sourcePaths": [
      "docs/guide/01-setup.md",
      "docs/guide/02-poteto-mode.md",
      "docs/guide/03-understand.md",
      "docs/guide/04-design.md",
      "docs/guide/05-build-and-clean.md",
      "docs/guide/06-verify-and-ship.md",
      "docs/guide/07-overnight.md",
      "docs/guide/08-principles.md",
      "docs/guide/09-make-it-yours.md",
      "docs/guide/10-recipes-and-pitfalls.md",
      "docs/guide/README.md",
      "docs/guide/images/design.jpg",
      "docs/guide/images/overnight.jpg",
      "docs/guide/images/recipes.jpg",
      "docs/guide/images/router.jpg",
      "docs/guide/images/understanding.jpg",
      "docs/guide/images/verification.jpg"
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
      "attemptId": "grades-native-02.json#1",
      "order": 0,
      "gradeFile": "grades-native-02.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "guides-local-codex",
      "status": "reduced-pass",
      "grade": {
        "caseId": "guides-local-codex",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_8",
          "item_14",
          "item_17"
        ],
        "rawTrace": "codex/batch-02.events.jsonl",
        "responseArtifact": "fixtures/batch-02/guides-local-codex.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Supported host loading and task Git revision unobserved."
        ],
        "review": "Actual copied orders/dashboard and Bun verification return open IDs 1,3 with count2; read/write/execution separately observed. Package loading, Git state and complete guide runtime methods remain unverified.",
        "variantReview": [
          "See actual variants and limitations in response artifact; unperformed capability branches do not receive full credit."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-02.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Perform only authorized operations supported by observed tools; report exact artifacts and actual model values or unknown.",
        "reducedExpected": "Observe read, isolated-write and execution separately; supported loading remains unverified until tested through the host."
      },
      "topLevelContext": {
        "gradingNotes": [
          "Native raw events, actual result reports and saved source/artifacts reviewed. Model selfgrades and integrity scripts are not workflow proof.",
          "Local subprocesses are not independent AI workers; no worker/service method credit from proxies.",
          "Native agent startup errors are observed failures, not proof operation absent.",
          "Conditional simulated capability branches are not host-enforced denials.",
          "Missing fixtures are blockers, not skill defects.",
          "Read-event IDs are local to raw trace."
        ]
      },
      "response": {
        "text": "# guides-local-codex\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"guides-local-codex\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/01-setup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/02-poteto-mode.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/03-understand.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/04-design.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/05-build-and-clean.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/06-verify-and-ship.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/07-overnight.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/08-principles.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/09-make-it-yours.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/10-recipes-and-pitfalls.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/README.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/design.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/overnight.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/recipes.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/router.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/understanding.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/verification.jpg\"\n  ],\n  \"prompt\": \"Use pstack in local Codex with authorized repository access.\",\n  \"requirements\": [\n    \"Read the matching guide and host capability contract.\",\n    \"Preserve the active controller and explicit permission gates.\"\n  ],\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\"\n}\n```\n\nThe user authorized local evaluation reads, scoped fixture writes and Bun execution. External account writes, live services, real messages/issues/PRs, commits/pushes, publication, credentials/configuration changes, installs and schedules are forbidden. No unrelated personal context or memory was consulted.\n\n## Source access\n\nAll named source files were actually read from /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 using exposed exec_command file reads. Guide JPGs were also inspected through view_image. The complete named bytes were then read with Bun.file and saved under this case's sources/ with SHA256 and byte count in source-manifest.json. Shared identical source reads serve all four guide cases; each has its own copied evidence. Additional contracts were read from the same 0.1.0 root. No source file from version 0.2.1 was used. Direct file access does not establish package loading or registration. Git inspection of the package failed; the freeze is supplied rather than independently verified.\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/01-setup.md (6057 bytes; SHA256 5e824e4a10faa4bab62c1d9a75337567204aaddd97accc4f6acb0cb19987ee73)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/02-poteto-mode.md (9131 bytes; SHA256 49c8d94e9f89039de969450fed1b9843461e8c10abdf6088cd6828a0db83f95c)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/03-understand.md (7249 bytes; SHA256 1c035fb8a4f650063395c5f0817800c8e9c0417e0ed6b807811b8b231e45e994)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/04-design.md (10811 bytes; SHA256 8ab5097f86427bf3b4b854bae24a8c2bf3f75b3d133d88301090176c24d16193)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/05-build-and-clean.md (7574 bytes; SHA256 62ca0f31ce74cb0d5356bf2a95332602a1edcf0a38e5f496b7bdef46d48b91c5)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/06-verify-and-ship.md (12122 bytes; SHA256 162c170c25cc3b65a7aba2159ee13fc52a847a838951f2e94ef0c88a029c4648)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/07-overnight.md (12457 bytes; SHA256 b9f08b2b6891cb21fa686f11c0781d920912310070288a895ffa512af5677c9f)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/08-principles.md (7655 bytes; SHA256 67c2fca0f82d0357f73247ccf2feb66310fc6c09ff1e170c54945a6816935c30)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/09-make-it-yours.md (9901 bytes; SHA256 4e52d21eb5e8917a679e3091865f261645d2d1eab32200ec5d6bea6b25caefb6)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/10-recipes-and-pitfalls.md (9453 bytes; SHA256 4be34d37aa0dce687d7bcf13951369f9c9bd320a58391474f511cf9afd00b1f8)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/README.md (4347 bytes; SHA256 9688f32b8fb309eabce81d4b66be3ecfafb8427a1c3c140d08560842e160d51a)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/design.jpg (402373 bytes; SHA256 b8ed07427f6a0c37dd8ba97961fc0eb5071efeee6c4a230648bdb7547f6f2a8f)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/overnight.jpg (347071 bytes; SHA256 4b4405e4df8925c5b3abbe702f681af0f3b1f5f32271b599f95717f578f1a0c8)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/recipes.jpg (410550 bytes; SHA256 9fa2d51b476635712737795ddef81806efaa0086bb3bfa9f9f45695d9ab0f8e8)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/router.jpg (450945 bytes; SHA256 525843055a4efd2b10acc50a8652fd02b0834ea733a8a2f895c1eb89036017da)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/understanding.jpg (376523 bytes; SHA256 b60587e9a9bbe2550e93be9819cf0cd4acf77d90fac769a0c43d82bd8e34e279)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/verification.jpg (331450 bytes; SHA256 2a76b52007a1cd2866ba67fd47d7d9ef3e1118bb5a09c4665eee8c3f161bd09a)\n\n## Actual response and output\n\nLocal source reads, isolated writes and execution were observed separately. I copied orders.json and dashboard.mjs, saved verify.mjs, ran it with Bun, and read the saved source back. The actual output was {\"openIds\":[1,3],\"count\":2}. The check exited 0.\n\nThis demonstrates local fixture access and behavior. It does not prove supported plugin loading, slash-command registration, mode persistence, external delivery or a production application. The case fixture is not a Git repository; HEAD, branch and dirty-state commands exited 128. The supplied package freeze cannot be verified as a Git revision here. Actual model and effort remain unknown.\n\nPstack retains ownership of the explicit case workflow. The guide does not authorize enabling plugins, installing helpers, creating settings, committing, pushing or contacting a forge. No implementation goal beyond local authorized use was supplied, so I did not invent a feature change.\n\n## Variants attempted\n\n[\n  {\n    \"variant\": \"optional setup skipped\",\n    \"method\": \"actual local artifact\",\n    \"response\": \"Retain inherit-parent for model and effort. Actual model unknown. No personal persistence or dependency setup.\",\n    \"negativeCondition\": \"User-enforced prohibition on configuration and installation.\"\n  },\n  {\n    \"variant\": \"missing execution\",\n    \"method\": \"supplied-text branch only\",\n    \"response\": \"Explain and draft only. Dependency helpers, app verification and runtime claims remain blocked.\",\n    \"negativeCondition\": \"simulated; commands are exposed and worked in the evaluation host\"\n  },\n  {\n    \"variant\": \"missing workers\",\n    \"method\": \"native spawn attempted once\",\n    \"response\": \"Native independent-agent operation failed with a thread-store error. No independent review or model diversity claimed.\",\n    \"negativeCondition\": \"observed failure, not an absent operation\"\n  },\n  {\n    \"variant\": \"missing persistent wake\",\n    \"method\": \"capability and permission review\",\n    \"response\": \"Foreground work only. No wake registered and no after-turn work promised. Scheduling prohibited.\",\n    \"negativeCondition\": \"No authorized wake binding observed; no registration attempted\"\n  },\n  {\n    \"variant\": \"missing stop\",\n    \"method\": \"process fixture unknown-stop checkpoint\",\n    \"response\": \"Keep worker ownership unresolved. Quarantine copies. No competing writer. Stop and terminal observation precede cancellation claims.\",\n    \"negativeCondition\": \"simulated withholding of available process controls; native AI stop could not be exercised after failed spawn\"\n  },\n  {\n    \"variant\": \"missing history\",\n    \"method\": \"current supplied-source review\",\n    \"response\": \"No complete exported session transcript is supplied. Do not search unrelated history or claim a complete audit.\",\n    \"negativeCondition\": \"Current conversation is available; exported historical transcript missing\"\n  },\n  {\n    \"variant\": \"missing persistence\",\n    \"method\": \"inline handoff branch\",\n    \"response\": \"Inline resume note only: retain identity and owned path, block integration and unknown replay, inspect stop and destination first when authorized. No saved checkpoint is claimed for this simulated branch.\",\n    \"negativeCondition\": \"simulated; local file persistence actually worked in other variants\"\n  }\n]\n\n## Real tools and actions\n\nfunctions.exec with tools.exec_command and tools.apply_patch, Bun.file for scoped reads/writes/readback, Bun.spawnSync for the command records below. Guide images also used tools.view_image. No external tool operation ran.\n\nThe evaluation controller remains /root using the explicitly requested pstack source workflow. No concurrent controller was started. Requested model policy is inherit-parent where applicable; actual model and effort are unknown.\n\n```json\n[\n  {\n    \"artifact\": \"commands/bun-version.json\",\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.165Z\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"artifact\": \"commands/git-branch.json\",\n    \"argv\": [\n      \"git\",\n      \"branch\",\n      \"--show-current\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.183Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/git-dirty.json\",\n    \"argv\": [\n      \"git\",\n      \"status\",\n      \"--porcelain=v1\",\n      \"--untracked-files=all\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.192Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/git-head.json\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.170Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/package-revision.json\",\n    \"argv\": [\n      \"git\",\n      \"-C\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.200Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/verify-local.json\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/verify.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"openIds\\\":[1,3],\\\"count\\\":2}\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Artifacts and limits\n\n- [commands/bun-version.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/bun-version.json)\n- [commands/git-branch.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-branch.json)\n- [commands/git-dirty.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-dirty.json)\n- [commands/git-head.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-head.json)\n- [commands/package-revision.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/package-revision.json)\n- [commands/verify-local.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/verify-local.json)\n- [dashboard.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/dashboard.mjs)\n- [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/input.json)\n- [orders.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/orders.json)\n- [persistence-readback.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/persistence-readback.json)\n- [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/source-manifest.json)\n- [variants.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/variants.json)\n- [verify.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/verify.mjs)\n\nCase-owned source copies are under /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/sources. The inventory records task-created paths, not a Git dirty-state claim. Synthetic data is not real-service evidence. Failed, unperformed, simulated and reduced operations remain labelled above. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-02/guides-local-codex.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex.result.md",
          "sha256": "23268072f0323696d65928b6c1899bb397a7bbd42fcb48318e22d98735ab3978",
          "bytes": 15356
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-02.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-02.events.jsonl",
            "sha256": "b16be05a232a847cb04fbb51cc599e38617d8cee45b1be216c4efb5de6dc787c",
            "bytes": 468744,
            "eventReferences": [
              {
                "eventId": "item_8",
                "line": 14,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "27b9791a9201c973ecb902a2ac94398a5c95f1d203cf0f86ec8f00f23a5416fa"
              },
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c1e962b7651705b0a358e7db17c1d25dd305779ebfae2528685ad631ba4e32e0",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "164f9b1dc8d158eb205e322fadc2cbb84517d3d014c668637adc060f96c3dbbf"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "37fbb63d89a3002b6a795ce40052f82c22be78a74d5792d7a4b0308c77721bcb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_17",
                "line": 31,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9bd2480614215c54b2c17e728ab6c69f28e38c28d742192c507a66538ebf2eb3"
              },
              {
                "eventId": "item_17",
                "line": 32,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "df0aa3f56a9a1e785d2b98203fe40f64bb02ea2a3352ab056e73cf6bfb9b8b8a",
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
            "item_8",
            "item_14",
            "item_17"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-02.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-02/guides-local-codex/artifact-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/artifact-inventory.json",
      "sha256": "496b6955a896ccac4203e3612da5372bff8d4f1935707fa72374c8dd55035788",
      "bytes": 333,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "[\n  \"commands/bun-version.json\",\n  \"commands/git-branch.json\",\n  \"commands/git-dirty.json\",\n  \"commands/git-head.json\",\n  \"commands/package-revision.json\",\n  \"commands/verify-local.json\",\n  \"dashboard.mjs\",\n  \"input.json\",\n  \"orders.json\",\n  \"persistence-readback.json\",\n  \"source-manifest.json\",\n  \"variants.json\",\n  \"verify.mjs\"\n]\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/commands/bun-version.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/bun-version.json",
      "sha256": "3f69663c01e7183eeb8cd0bbb7d4d7ecc290f7642d8f81adecb2aa3b00d25970",
      "bytes": 237,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"startedAt\": \"2026-10-16T07:42:24.165Z\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/commands/git-branch.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-branch.json",
      "sha256": "27e8316c1c2eef1d832e1df60fbab606680bbb787d9e9d0be51c5d2249ebb293",
      "bytes": 321,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"branch\",\n    \"--show-current\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"startedAt\": \"2026-10-16T07:42:24.183Z\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/commands/git-dirty.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-dirty.json",
      "sha256": "1461027162d73d7e3f8620265fd7776849524c6ea5f3af70e802a435f05d9e47",
      "bytes": 350,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"status\",\n    \"--porcelain=v1\",\n    \"--untracked-files=all\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"startedAt\": \"2026-10-16T07:42:24.192Z\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/commands/git-head.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-head.json",
      "sha256": "d71f450d831cd2413bc17b5e62a72f323df9f807a888aa3cc09454f202496b22",
      "bytes": 314,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"startedAt\": \"2026-10-16T07:42:24.170Z\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/commands/package-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/package-revision.json",
      "sha256": "4d2801b854f4cf22a2740b371297f537f4d9c791fae7ecb14deb290cb7fa8f7e",
      "bytes": 413,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"-C\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"startedAt\": \"2026-10-16T07:42:24.200Z\",\n  \"exitCode\": 128,\n  \"stdout\": \"\",\n  \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/commands/verify-local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/verify-local.json",
      "sha256": "4e5d679256b75b214977a6793c84ea22dca21e406122985217fedceb4ceb9843",
      "bytes": 339,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/verify.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"openIds\\\":[1,3],\\\"count\\\":2}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/persistence-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/persistence-readback.json",
      "sha256": "dbdc9a65d5c68e8ba9425652c6cff4d61d09faf7643523801f98728b08aa4d5e",
      "bytes": 622,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "{\n  \"observed\": \"import {strict as assert} from 'node:assert';\\nimport {visible} from './dashboard.mjs';\\nconst orders=await Bun.file(new URL('./orders.json',import.meta.url)).json();\\nconst result=visible(orders,'open');\\nassert.deepEqual(result.map(o=>o.id),[1,3]);\\nconsole.log(JSON.stringify({openIds:result.map(o=>o.id),count:result.length}));\\n\",\n  \"sourceRead\": \"export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nexport function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"localPersistenceOnly\": true\n}\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/variants.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/variants.json",
      "sha256": "93a1263b4eeb52beaa3de910dd643473473308541d978a1aa8f59d1650ff1bbd",
      "bytes": 2322,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "[\n  {\n    \"variant\": \"optional setup skipped\",\n    \"method\": \"actual local artifact\",\n    \"response\": \"Retain inherit-parent for model and effort. Actual model unknown. No personal persistence or dependency setup.\",\n    \"negativeCondition\": \"User-enforced prohibition on configuration and installation.\"\n  },\n  {\n    \"variant\": \"missing execution\",\n    \"method\": \"supplied-text branch only\",\n    \"response\": \"Explain and draft only. Dependency helpers, app verification and runtime claims remain blocked.\",\n    \"negativeCondition\": \"simulated; commands are exposed and worked in the evaluation host\"\n  },\n  {\n    \"variant\": \"missing workers\",\n    \"method\": \"native spawn attempted once\",\n    \"response\": \"Native independent-agent operation failed with a thread-store error. No independent review or model diversity claimed.\",\n    \"negativeCondition\": \"observed failure, not an absent operation\"\n  },\n  {\n    \"variant\": \"missing persistent wake\",\n    \"method\": \"capability and permission review\",\n    \"response\": \"Foreground work only. No wake registered and no after-turn work promised. Scheduling prohibited.\",\n    \"negativeCondition\": \"No authorized wake binding observed; no registration attempted\"\n  },\n  {\n    \"variant\": \"missing stop\",\n    \"method\": \"process fixture unknown-stop checkpoint\",\n    \"response\": \"Keep worker ownership unresolved. Quarantine copies. No competing writer. Stop and terminal observation precede cancellation claims.\",\n    \"negativeCondition\": \"simulated withholding of available process controls; native AI stop could not be exercised after failed spawn\"\n  },\n  {\n    \"variant\": \"missing history\",\n    \"method\": \"current supplied-source review\",\n    \"response\": \"No complete exported session transcript is supplied. Do not search unrelated history or claim a complete audit.\",\n    \"negativeCondition\": \"Current conversation is available; exported historical transcript missing\"\n  },\n  {\n    \"variant\": \"missing persistence\",\n    \"method\": \"inline handoff branch\",\n    \"response\": \"Inline resume note only: retain identity and owned path, block integration and unknown replay, inspect stop and destination first when authorized. No saved checkpoint is claimed for this simulated branch.\",\n    \"negativeCondition\": \"simulated; local file persistence actually worked in other variants\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/verify.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/verify.mjs",
      "sha256": "ff0cb5bf1691ded525e80d82bb291af5fd4d2517b8f628ef0a4bf9b9398012a4",
      "bytes": 327,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "import {strict as assert} from 'node:assert';\nimport {visible} from './dashboard.mjs';\nconst orders=await Bun.file(new URL('./orders.json',import.meta.url)).json();\nconst result=visible(orders,'open');\nassert.deepEqual(result.map(o=>o.id),[1,3]);\nconsole.log(JSON.stringify({openIds:result.map(o=>o.id),count:result.length}));\n"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex.result.md",
      "sha256": "23268072f0323696d65928b6c1899bb397a7bbd42fcb48318e22d98735ab3978",
      "bytes": 15356,
      "owners": [
        "grades-native-02.json#1"
      ],
      "text": "# guides-local-codex\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"guides-local-codex\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/01-setup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/02-poteto-mode.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/03-understand.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/04-design.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/05-build-and-clean.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/06-verify-and-ship.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/07-overnight.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/08-principles.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/09-make-it-yours.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/10-recipes-and-pitfalls.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/README.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/design.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/overnight.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/recipes.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/router.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/understanding.jpg\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/verification.jpg\"\n  ],\n  \"prompt\": \"Use pstack in local Codex with authorized repository access.\",\n  \"requirements\": [\n    \"Read the matching guide and host capability contract.\",\n    \"Preserve the active controller and explicit permission gates.\"\n  ],\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\"\n}\n```\n\nThe user authorized local evaluation reads, scoped fixture writes and Bun execution. External account writes, live services, real messages/issues/PRs, commits/pushes, publication, credentials/configuration changes, installs and schedules are forbidden. No unrelated personal context or memory was consulted.\n\n## Source access\n\nAll named source files were actually read from /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 using exposed exec_command file reads. Guide JPGs were also inspected through view_image. The complete named bytes were then read with Bun.file and saved under this case's sources/ with SHA256 and byte count in source-manifest.json. Shared identical source reads serve all four guide cases; each has its own copied evidence. Additional contracts were read from the same 0.1.0 root. No source file from version 0.2.1 was used. Direct file access does not establish package loading or registration. Git inspection of the package failed; the freeze is supplied rather than independently verified.\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/01-setup.md (6057 bytes; SHA256 5e824e4a10faa4bab62c1d9a75337567204aaddd97accc4f6acb0cb19987ee73)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/02-poteto-mode.md (9131 bytes; SHA256 49c8d94e9f89039de969450fed1b9843461e8c10abdf6088cd6828a0db83f95c)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/03-understand.md (7249 bytes; SHA256 1c035fb8a4f650063395c5f0817800c8e9c0417e0ed6b807811b8b231e45e994)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/04-design.md (10811 bytes; SHA256 8ab5097f86427bf3b4b854bae24a8c2bf3f75b3d133d88301090176c24d16193)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/05-build-and-clean.md (7574 bytes; SHA256 62ca0f31ce74cb0d5356bf2a95332602a1edcf0a38e5f496b7bdef46d48b91c5)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/06-verify-and-ship.md (12122 bytes; SHA256 162c170c25cc3b65a7aba2159ee13fc52a847a838951f2e94ef0c88a029c4648)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/07-overnight.md (12457 bytes; SHA256 b9f08b2b6891cb21fa686f11c0781d920912310070288a895ffa512af5677c9f)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/08-principles.md (7655 bytes; SHA256 67c2fca0f82d0357f73247ccf2feb66310fc6c09ff1e170c54945a6816935c30)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/09-make-it-yours.md (9901 bytes; SHA256 4e52d21eb5e8917a679e3091865f261645d2d1eab32200ec5d6bea6b25caefb6)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/10-recipes-and-pitfalls.md (9453 bytes; SHA256 4be34d37aa0dce687d7bcf13951369f9c9bd320a58391474f511cf9afd00b1f8)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/README.md (4347 bytes; SHA256 9688f32b8fb309eabce81d4b66be3ecfafb8427a1c3c140d08560842e160d51a)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/design.jpg (402373 bytes; SHA256 b8ed07427f6a0c37dd8ba97961fc0eb5071efeee6c4a230648bdb7547f6f2a8f)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/overnight.jpg (347071 bytes; SHA256 4b4405e4df8925c5b3abbe702f681af0f3b1f5f32271b599f95717f578f1a0c8)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/recipes.jpg (410550 bytes; SHA256 9fa2d51b476635712737795ddef81806efaa0086bb3bfa9f9f45695d9ab0f8e8)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/router.jpg (450945 bytes; SHA256 525843055a4efd2b10acc50a8652fd02b0834ea733a8a2f895c1eb89036017da)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/understanding.jpg (376523 bytes; SHA256 b60587e9a9bbe2550e93be9819cf0cd4acf77d90fac769a0c43d82bd8e34e279)\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/docs/guide/images/verification.jpg (331450 bytes; SHA256 2a76b52007a1cd2866ba67fd47d7d9ef3e1118bb5a09c4665eee8c3f161bd09a)\n\n## Actual response and output\n\nLocal source reads, isolated writes and execution were observed separately. I copied orders.json and dashboard.mjs, saved verify.mjs, ran it with Bun, and read the saved source back. The actual output was {\"openIds\":[1,3],\"count\":2}. The check exited 0.\n\nThis demonstrates local fixture access and behavior. It does not prove supported plugin loading, slash-command registration, mode persistence, external delivery or a production application. The case fixture is not a Git repository; HEAD, branch and dirty-state commands exited 128. The supplied package freeze cannot be verified as a Git revision here. Actual model and effort remain unknown.\n\nPstack retains ownership of the explicit case workflow. The guide does not authorize enabling plugins, installing helpers, creating settings, committing, pushing or contacting a forge. No implementation goal beyond local authorized use was supplied, so I did not invent a feature change.\n\n## Variants attempted\n\n[\n  {\n    \"variant\": \"optional setup skipped\",\n    \"method\": \"actual local artifact\",\n    \"response\": \"Retain inherit-parent for model and effort. Actual model unknown. No personal persistence or dependency setup.\",\n    \"negativeCondition\": \"User-enforced prohibition on configuration and installation.\"\n  },\n  {\n    \"variant\": \"missing execution\",\n    \"method\": \"supplied-text branch only\",\n    \"response\": \"Explain and draft only. Dependency helpers, app verification and runtime claims remain blocked.\",\n    \"negativeCondition\": \"simulated; commands are exposed and worked in the evaluation host\"\n  },\n  {\n    \"variant\": \"missing workers\",\n    \"method\": \"native spawn attempted once\",\n    \"response\": \"Native independent-agent operation failed with a thread-store error. No independent review or model diversity claimed.\",\n    \"negativeCondition\": \"observed failure, not an absent operation\"\n  },\n  {\n    \"variant\": \"missing persistent wake\",\n    \"method\": \"capability and permission review\",\n    \"response\": \"Foreground work only. No wake registered and no after-turn work promised. Scheduling prohibited.\",\n    \"negativeCondition\": \"No authorized wake binding observed; no registration attempted\"\n  },\n  {\n    \"variant\": \"missing stop\",\n    \"method\": \"process fixture unknown-stop checkpoint\",\n    \"response\": \"Keep worker ownership unresolved. Quarantine copies. No competing writer. Stop and terminal observation precede cancellation claims.\",\n    \"negativeCondition\": \"simulated withholding of available process controls; native AI stop could not be exercised after failed spawn\"\n  },\n  {\n    \"variant\": \"missing history\",\n    \"method\": \"current supplied-source review\",\n    \"response\": \"No complete exported session transcript is supplied. Do not search unrelated history or claim a complete audit.\",\n    \"negativeCondition\": \"Current conversation is available; exported historical transcript missing\"\n  },\n  {\n    \"variant\": \"missing persistence\",\n    \"method\": \"inline handoff branch\",\n    \"response\": \"Inline resume note only: retain identity and owned path, block integration and unknown replay, inspect stop and destination first when authorized. No saved checkpoint is claimed for this simulated branch.\",\n    \"negativeCondition\": \"simulated; local file persistence actually worked in other variants\"\n  }\n]\n\n## Real tools and actions\n\nfunctions.exec with tools.exec_command and tools.apply_patch, Bun.file for scoped reads/writes/readback, Bun.spawnSync for the command records below. Guide images also used tools.view_image. No external tool operation ran.\n\nThe evaluation controller remains /root using the explicitly requested pstack source workflow. No concurrent controller was started. Requested model policy is inherit-parent where applicable; actual model and effort are unknown.\n\n```json\n[\n  {\n    \"artifact\": \"commands/bun-version.json\",\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.165Z\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"artifact\": \"commands/git-branch.json\",\n    \"argv\": [\n      \"git\",\n      \"branch\",\n      \"--show-current\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.183Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/git-dirty.json\",\n    \"argv\": [\n      \"git\",\n      \"status\",\n      \"--porcelain=v1\",\n      \"--untracked-files=all\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.192Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/git-head.json\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.170Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/package-revision.json\",\n    \"argv\": [\n      \"git\",\n      \"-C\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.200Z\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"artifact\": \"commands/verify-local.json\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/verify.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"openIds\\\":[1,3],\\\"count\\\":2}\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Artifacts and limits\n\n- [commands/bun-version.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/bun-version.json)\n- [commands/git-branch.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-branch.json)\n- [commands/git-dirty.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-dirty.json)\n- [commands/git-head.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/git-head.json)\n- [commands/package-revision.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/package-revision.json)\n- [commands/verify-local.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/commands/verify-local.json)\n- [dashboard.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/dashboard.mjs)\n- [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/input.json)\n- [orders.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/orders.json)\n- [persistence-readback.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/persistence-readback.json)\n- [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/source-manifest.json)\n- [variants.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/variants.json)\n- [verify.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/verify.mjs)\n\nCase-owned source copies are under /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/guides-local-codex/sources. The inventory records task-created paths, not a Git dirty-state claim. Synthetic data is not real-service evidence. Failed, unperformed, simulated and reduced operations remain labelled above. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-02/guides-local-codex/dashboard.mjs",
      "owner": "grades-native-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/input.json",
      "owner": "grades-native-02.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/orders.json",
      "owner": "grades-native-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/source-manifest.json",
      "owner": "grades-native-02.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/sources",
      "owner": "grades-native-02.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/dashboard.mjs",
      "owner": "grades-native-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/input.json",
      "owner": "grades-native-02.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/orders.json",
      "owner": "grades-native-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/source-manifest.json",
      "owner": "grades-native-02.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/guides-local-codex/sources",
      "owner": "grades-native-02.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
