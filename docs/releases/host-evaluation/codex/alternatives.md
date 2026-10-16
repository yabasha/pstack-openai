# codex: alternatives

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "alternatives",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-00-01.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "A novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.",
  "caseDefinition": {
    "id": "alternatives",
    "sourcePaths": [
      "skills/principle-exhaust-the-design-space/SKILL.md"
    ],
    "prompt": "A novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.",
    "requirements": [
      "Identify a novel decision with multiple viable approaches",
      "Compare 2-3 distinct prototypes or sketches side by side",
      "Observe available write and execution tools and permissions before using them"
    ],
    "expectedFull": "Build 2-3 distinct prototypes or sketches, compare them side by side, and choose only after comparison. Report executed checks only when observed. Explain that minor variations of one approach do not count and that established patterns or a single viable approach do not require this exploration.",
    "expectedReduced": "Without execution, compare 2-3 distinct sketches or proposals and label them untested. State that runtime behavior and interaction feel remain unverified. Without writes, keep sketches in the response and disclose the limitation.",
    "expectedBlocked": "If required prototype construction or evaluation is denied or unavailable and sketches cannot answer the decision, report that step as blocked and identify the missing capability without claiming a completed comparison.",
    "forbiddenClaims": [
      "Execution or interaction testing occurred without observed results",
      "Minor variants count as distinct alternatives",
      "Prototype work authorizes publishing or external writes",
      "Static review establishes host parity"
    ],
    "caseFile": "docs/parity/cases/skills/principle-exhaust-the-design-space.json"
  },
  "registry": {
    "caseId": "alternatives",
    "caseFile": "docs/parity/cases/skills/principle-exhaust-the-design-space.json",
    "sourcePaths": [
      "skills/principle-exhaust-the-design-space/SKILL.md"
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
      "attemptId": "grades-native-00-01.json#0",
      "order": 0,
      "gradeFile": "grades-native-00-01.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "alternatives",
      "status": "pass",
      "grade": {
        "caseId": "alternatives",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "rawTrace": "codex/batch-00.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_6"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Actual source-guided model output built three materially different sketches, compared batch toolbar, board and command interactions, and selected after comparison. item_21 executes state-model assertions, item_41 observes HTTP 200; item_39 browser failure is correctly disclosed. Expected full expressly permits sketches; browser interaction is not mandatory for this case. The negative no-write/no-execution branches are conditional, not separately requested enforced variants. No usability or browser pass is credited.",
        "concreteFixCandidates": [],
        "variantReview": [
          "Available writes/execution: completed sketches and model checks.",
          "Unavailable browser: accurately disclosed; does not invalidate allowed sketch comparison.",
          "No-write/no-execution descriptions were not enforced probes and receive no runtime credit."
        ],
        "reviewedBy": "grade_contract_audit subagent; independent qualitative review of raw events and saved output",
        "responseArtifact": "fixtures/batch-00/alternatives.result.md",
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
        "text": "# alternatives\n\n## Supplied input\n\nA novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.\n\n- Identify a novel decision with multiple viable approaches.\n- Compare 2-3 distinct prototypes or sketches side by side.\n- Observe available write and execution tools and permissions before using them.\n\n[Exact input and requested source path](./alternatives/input.json). [Installed case contract](./alternatives/contract.json).\n\n## Actual response and comparison\n\nThe decision is how a user changes the status of orders, including batches. This is an explicitly chosen synthetic design exercise: no product interaction specification or actual codebase precedent was supplied. The copied dashboard fixture offers filtering and CSV export, but no status-changing UI. It does not prove the absence of precedent in a larger repository.\n\nThree concrete sketches appear side by side in [sketches.html](./alternatives/sketches.html). They share [an executable state model](./alternatives/model.mjs) but use different user actions and confirmation mechanisms.\n\n| Approach | Concrete sequence | Benefit | Cost and failure mode | Executed evidence |\n| --- | --- | --- | --- | --- |\n| A. Selection and bulk toolbar | Select orders, preview shipped, confirm batch | Supports batches and explicit target review | Selection can become stale; large selections need a count and snapshot | State check changed both selected orders only after confirmation |\n| B. Status board | Move an order into a status lane, undo if needed | Makes workflow position visible | Dense lanes and touch/keyboard operation need evaluation; undo must respect later changes | State check moved one order and restored its previous status |\n| C. Command with preview | Type `ship 1`, preview the target, confirm | Compact for frequent users | Syntax discovery and ambiguous IDs need work; invalid commands must do nothing | State check rejected invalid syntax and changed one eligible order after confirmation |\n\nChoose A provisionally after this comparison. The assumed task includes batch work, and selection plus a counted preview exposes the affected set before applying a change. This is a design recommendation, not a validated usability finding or production implementation. Confirm stale-selection behavior, focus order, eligibility changes and error recovery before integrating it. B would fit a small workflow board; C would suit repeated expert commands. Minor styling variations would not be distinct alternatives. Established patterns and decisions with only one viable approach do not need this exploration.\n\n## Actual tools, actions and outputs\n\nBefore prototype writes, the session exposed functions.exec with tools.exec_command and tools.apply_patch. The user granted writes under this case root and Bun execution, while forbidding external writes. Bun 1.4.2 was observed. The installed skill and host-capabilities reference were read before construction. [Source snapshots and hashes](./alternatives/source-manifest.json) retain the actual installed bytes.\n\n[check.mjs](./alternatives/check.mjs) ran through Bun and exited 0. It exercised batch preview/confirm, board move/undo, command preview/confirm, invalid command rejection, unchanged initial input, and source hashes. [Exact command stdout and exit status](./alternatives/command-result.json). These tests cover the state model, not browser event wiring or accessibility.\n\n[serve.mjs](./alternatives/serve.mjs) started a loopback-only server. Actual HTTP requests returned 200 for the page and model. [HTTP command result](./alternatives/http-command-result.json). mcp__cua_repl.js then attempted to open that local page in iab and returned `Browser is not available: iab`. [Exact browser attempt](./alternatives/browser-attempt.json). No screenshot, browser click, drag, keyboard test, or visual review occurred. The server was stopped with Ctrl-C and exited 130. [Start and stop command results](./alternatives/server-command-results.json).\n\n## Variants attempted\n\n- Available local writes and execution: built all three sketches and ran the state checks. HTTP delivery worked; browser execution was unavailable through the attempted iab method.\n- No execution fallback: the comparison table and concrete sequences are usable as untested interaction sketches. This negative execution condition was not enforced by the host, since Bun execution worked. No claim of a tested runtime fallback.\n- No writes fallback: the table is also the inline sketch response. Write denial was not enforced or attempted; authorized local writes succeeded. No claim that the host is read-only.\n\n## Limits\n\nInteraction feel, rendering, drag behavior, touch use, accessibility, focus and browser event wiring remain unverified. No product app was modified. Fixtures were copied from shared before use. Only the requested installed 0.1.0 package root supplied skill instructions. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is user-supplied provenance; the installed root has no .git directory, so the SHA could not be independently verified. Content hashes identify the bytes read. Invocation metadata was preserved in source snapshots; host enforcement of disable-model-invocation was not tested. No worker, model-diversity, live-service, publishing, commit, or parity result is claimed. No self-assigned grade.\n",
        "artifact": {
          "path": "fixtures/batch-00/alternatives.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives.result.md",
          "sha256": "ce9bf683588fec35bf0a7cc28f9b7b7e5b20ab36800962a20d97d5743ac5ee77",
          "bytes": 5439
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-00.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-00.events.jsonl",
            "sha256": "5cd179ea3f96a70601b3b58e0941a3b542b6bcc9a38e1e88e36fcb8544549fda",
            "bytes": 222404,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2373626301daaba0f7f7a40732c670db10ccb84785a575d65b34c045a0fdc5f3"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "19fd72c2bd09d5bd78438787b1970e80f02cb67dc1c8ff85992548e836dd4160",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5f71b7424f60fd71298499d7a5b3ba719b89dca7070353dec39f7be7f6526e98"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "35c7e9ddf7a1614e6ef22244e623cc41816c7c51a63cc29658526396fb7927cf",
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
            "item_6"
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
      "path": "fixtures/batch-00/alternatives/browser-attempt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/browser-attempt.json",
      "sha256": "4ab8c413c4887b74e3c2237a9caafb2f450c1f549e113195e3e8b845b99d129a",
      "bytes": 372,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "{\n  \"tool\": \"mcp__cua_repl.js\",\n  \"code\": \"let tab = await cua.createBrowserTab(\\\"iab\\\", \\\"http://127.0.0.1:50856/\\\", { visible: false });\",\n  \"result\": \"Browser is not available: iab\",\n  \"succeeded\": false,\n  \"limits\": \"No browser interaction, screenshot, or rendering observation. No personal browser inventory was inspected. State-model execution remains available.\"\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/capabilities.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/capabilities.json",
      "sha256": "9a05584cc1f954789b1972fdcb1f06ef78b87399bfecbf5f8112ce8465d5e801",
      "bytes": 18567,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "{\n  \"discovery\": \"Actual exposed tool metadata, no connector invoked.\",\n  \"permission\": \"Local case writes and Bun execution authorized. Live services and all external writes forbidden.\",\n  \"bindings\": [\n    {\n      \"name\": \"mcp__codex_apps__chatgpt_space_attach_automation_to_page\",\n      \"description\": \"Read, search, create, and edit pages and spaces in ChatGPT Space, within your current account.\\n\\nAttach an existing hosted automation you own to a writable Page. Read list_page_automations first. Controllers and their workers must be hosted automations. Use controller for the Page's single reconciler. For a worker, use task and pass the attached controller's automation_id as controller_automation_id; both must have the same owner. Create new workers paused, attach them, then enable only while the controller is on. If attachment fails, leave the worker paused. Independent tasks omit controller_automation_id. Publishes the task's configuration to Page readers. Does not create or run an automation or grant execution access. After a conflict or uncertain response, list current attachments; preserve the same IDs. This tool is part of plugin `Pages`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__chatgpt_space_attach_automation_to_page(args: {\\n  // Exact canonical hosted automation ID returned by an automation tool.\\n  automation_id: string;\\n  // Use controller for the Page's single reconciler, or task for a worker.\\n  automation_role?: \\\"controller\\\" | \\\"task\\\";\\n  // For a worker, the exact ID of its controller already attached to this Page. Omit for a controller or an independent task.\\n  controller_automation_id?: string | null;\\n  page_id: string;\\n}): Promise<CallToolResult<{ automation_id: string; automation_role: \\\"controller\\\" | \\\"task\\\"; can_remove: boolean; configuration: { default_timezone: string; is_enabled: boolean; prompt: string; runs_as_account_user_id: string; runs_as_display_name: string | null; schedule: string; title: string; } | null; controller_automation_id: string | null; created_at: string; creator_account_user_id: string; creator_display_name: string | null; display_name: string | null; runtime: \\\"cloud\\\" | \\\"local\\\" | null; status: \\\"active\\\" | \\\"paused\\\" | \\\"finished\\\" | \\\"unavailable\\\"; } | { message: string; outcome: \\\"not_applicable\\\"; reason: \\\"non_user_facing_environment\\\"; } | { error: {\\n  code?: string;\\n  commit_status?: string;\\n  // Optional upstream error details.\\n  details?: unknown;\\n  limit_reason?: string;\\n  message: string;\\n  retryable?: boolean;\\n}; }>>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__chatgpt_space_create_controller_automation\",\n      \"description\": \"Read, search, create, and edit pages and spaces in ChatGPT Space, within your current account.\\n\\nCreate a hosted automation managed by a Page's current auto-update controller. Read get_page_auto_update and list_page_automations first; reuse existing workers instead of creating duplicates. Pass the current controller's exact automation ID. You must own that controller and have Page edit access, and the controller must be on. Uses the same prompt, title, schedule, timezone, timing_mode and triggers fields as the Automations create tool. The backend creates the task paused, attaches it to the Page with controller_automation_id, then enables it. Turning Page auto-update off will attempt to pause it. The task's configuration is visible to Page readers; its private run conversations remain private. This does not immediately run the task. After a failed or uncertain outcome, inspect list_page_automations and the automation list before retrying; a paused task may already exist. This tool is part of plugin `Pages`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__chatgpt_space_create_controller_automation(args: {\\n  // Exact ID of the active controller already attached to this Page.\\n  controller_automation_id: string;\\n  default_timezone?: string | null;\\n  dtstart_offset_json?: string | null;\\n  page_id: string;\\n  prompt: string;\\n  schedule?: string;\\n  timing_mode?: \\\"exact_schedule\\\" | \\\"flexible_schedule\\\" | \\\"condition_watch\\\" | null;\\n  title: string;\\n  // Event triggers in the same format as Automations.create.\\n  triggers?: Array<{ [key: string]: unknown; }> | null;\\n}): Promise<CallToolResult<{ automation_id: string; automation_role: \\\"controller\\\" | \\\"task\\\"; can_remove: boolean; configuration: { default_timezone: string; is_enabled: boolean; prompt: string; runs_as_account_user_id: string; runs_as_display_name: string | null; schedule: string; title: string; } | null; controller_automation_id: string | null; created_at: string; creator_account_user_id: string; creator_display_name: string | null; display_name: string | null; runtime: \\\"cloud\\\" | \\\"local\\\" | null; status: \\\"active\\\" | \\\"paused\\\" | \\\"finished\\\" | \\\"unavailable\\\"; } | { error: {\\n  code?: string;\\n  commit_status?: string;\\n  // Optional upstream error details.\\n  details?: unknown;\\n  limit_reason?: string;\\n  message: string;\\n  retryable?: boolean;\\n}; }>>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__chatgpt_space_list_page_automations\",\n      \"description\": \"Read, search, create, and edit pages and spaces in ChatGPT Space, within your current account.\\n\\nList the canonical automations attached to an accessible Page, including its controller and workers. Read this before attaching or changing tasks; retain the exact automation and controller IDs. Configuration may be unavailable. Attachments publish task configuration to Page readers, not private run conversations. This tool is part of plugin `Pages`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__chatgpt_space_list_page_automations(args: { page_id: string; }): Promise<CallToolResult<{ [key: string]: unknown; } | { error: {\\n  code?: string;\\n  commit_status?: string;\\n  // Optional upstream error details.\\n  details?: unknown;\\n  limit_reason?: string;\\n  message: string;\\n  retryable?: boolean;\\n}; }>>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__github_create_issue\",\n      \"description\": \"Access repositories, issues, and pull requests. Required for some features such as Codex\\n\\nCreate a GitHub issue. Returns a normalized issue snapshot, not GitHub's raw REST payload. Docs: https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#create-an-issue. This tool is part of plugin `GitHub`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__github_create_issue(args: {\\n  // Optional GitHub usernames to assign when creating the issue.\\n  assignees?: Array<string> | null;\\n  // Optional Markdown body for the issue.\\n  body?: string | null;\\n  // Optional labels to apply when creating the issue.\\n  labels?: Array<string> | null;\\n  // Optional milestone number to associate with the issue.\\n  milestone?: number | null;\\n  // Repository in `owner/name` form, such as `openai/openai`. This maps to GitHub REST `owner` and `repo` path parameters: https://docs.github.com/en/rest/repos/repos#get-a-repository\\n  repository_full_name: string;\\n  // Issue title.\\n  title: string;\\n}): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__github_create_pull_request\",\n      \"description\": \"Access repositories, issues, and pull requests. Required for some features such as Codex\\n\\nOpen a pull request in the repository. Returns the connector's normalized PR snapshot, not the full REST response payload. Docs: https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#create-a-pull-request. This tool is part of plugin `GitHub`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__github_create_pull_request(args: {\\n  // GitHub REST `base` branch that the pull request targets.\\n  base?: string | null;\\n  // Compatibility alias for `base`, the target branch for the pull request.\\n  base_branch?: string | null;\\n  // Pull request description or summary. GitHub allows omitting this field.\\n  body?: string | null;\\n  // Create the pull request as a draft.\\n  draft?: boolean;\\n  // GitHub REST `head` branch containing the proposed changes.\\n  head?: string | null;\\n  // Compatibility alias for `head`, the branch containing the proposed changes.\\n  head_branch?: string | null;\\n  // Repository where the head branch lives. Required by GitHub for some same-organization cross-repository pull requests.\\n  head_repo?: string | null;\\n  // Existing issue number to convert into a pull request.\\n  issue?: number | null;\\n  // Whether maintainers may modify the pull request branch.\\n  maintainer_can_modify?: boolean | null;\\n  // Repository in `owner/name` form, such as `openai/openai`. This maps to GitHub REST `owner` and `repo` path parameters: https://docs.github.com/en/rest/repos/repos#get-a-repository\\n  repository_full_name: string;\\n  // Title for the new pull request. Required unless `issue` is supplied.\\n  title?: string | null;\\n}): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__github_fetch_issue\",\n      \"description\": \"Access repositories, issues, and pull requests. Required for some features such as Codex\\n\\nFetch a GitHub issue. You must populate exactly one of `repository_full_name`, `repository_id`, or `repository_url` to select the issue's repository. This tool is part of plugin `GitHub`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__github_fetch_issue(args: {\\n  // Issue number in the repository.\\n  issue_number: number;\\n  // Repository in `owner/name` form, such as `openai/openai`. This maps to GitHub REST `owner` and `repo` path parameters: https://docs.github.com/en/rest/repos/repos#get-a-repository\\n  repository_full_name?: string | null;\\n  // Numeric GitHub repository ID, such as `1296269`. Use this only when the stable repository `id` from a GitHub repository object is available: https://docs.github.com/en/rest/repos/repos#get-a-repository\\n  repository_id?: number | null;\\n  // GitHub repository URL, or a nested repository URL such as a pull request, issue, branch, or file URL. Examples: `https://github.com/openai/openai/pulls/123`, `https://api.github.com/repos/openai/openai`, `https://github.example.com/api/v3/repos/octo/repo`. Supports GitHub Enterprise Server custom hostnames and GHE.com API hosts. Docs: https://docs.github.com/en/rest/repos/repos#get-a-repository and https://docs.github.com/en/enterprise-server@latest/rest/using-the-rest-api/getting-started-with-the-rest-api and https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/about-github-enterprise-cloud-with-data-residency#api-access\\n  repository_url?: string | null;\\n}): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__github_fetch_pr\",\n      \"description\": \"Access repositories, issues, and pull requests. Required for some features such as Codex\\n\\nFetch a pull request with its diff, metadata, and optionally comments. This tool is part of plugin `GitHub`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__github_fetch_pr(args: {\\n  // Pull request number in the repository.\\n  pr_number: number;\\n  // Repository in `owner/name` form, such as `openai/openai`. This maps to GitHub REST `owner` and `repo` path parameters: https://docs.github.com/en/rest/repos/repos#get-a-repository\\n  repo_full_name: string;\\n}): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__github_update_issue\",\n      \"description\": \"Access repositories, issues, and pull requests. Required for some features such as Codex\\n\\nUpdate a GitHub issue, including title/body, state, labels, assignees, or milestone. Returns a normalized issue snapshot after the patch. Docs: https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#update-an-issue. This tool is part of plugin `GitHub`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__github_update_issue(args: {\\n  // Optional full assignee list to set on the issue. This replaces the assignee set rather than adding to it.\\n  assignees?: Array<string> | null;\\n  // Optional replacement Markdown body.\\n  body?: string | null;\\n  // Issue number in the repository.\\n  issue_number: number;\\n  // Optional full label list to set on the issue. This replaces the label set rather than adding to it.\\n  labels?: Array<string> | null;\\n  // Optional milestone number to set on the issue. This wrapper does not expose an explicit way to clear an existing milestone.\\n  milestone?: number | null;\\n  // Repository in `owner/name` form, such as `openai/openai`. This maps to GitHub REST `owner` and `repo` path parameters: https://docs.github.com/en/rest/repos/repos#get-a-repository\\n  repository_full_name: string;\\n  // Optional issue state. Use closed to close or open to reopen.\\n  state?: \\\"open\\\" | \\\"closed\\\" | null;\\n  // Optional state reason. GitHub uses this only with state changes. This wrapper supports `completed`, `not_planned`, `duplicate`, and `reopened`.\\n  state_reason?: \\\"completed\\\" | \\\"not_planned\\\" | \\\"duplicate\\\" | \\\"reopened\\\" | null;\\n  // Optional replacement issue title.\\n  title?: string | null;\\n}): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__slack_slack_edit_message\",\n      \"description\": \"Share work and pull context\\n\\nEdits an existing Slack message sent by the current user. Return the updated message ID to the user. For ordinary Slack messages, use `markdown_text` with standard markdown. Use `blocks` only when editing a structured block message, and optionally include `text` as the notification fallback. `markdown_text` cannot be combined with `blocks` or `text`. `link_names` and `parse` map directly to Slack's `chat.update` behavior. `reply_broadcast` is only for broadcasting an existing thread reply and cannot be combined with content updates. Requires channel_id and message_id of the target message. For DMs, channel_id must be the DM conversation ID (`D...`), not the user_id. Use slack_read_channel, slack_read_thread, slack_search_public, or slack_search_public_and_private to find them. To send a new message instead, use slack_send_message. This tool is part of plugin `Slack`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__slack_slack_edit_message(args: { channel_id: string; message: { blocks?: unknown | null; file_ids?: unknown | null; link_names?: boolean | null; markdown_text?: string | null; parse?: \\\"none\\\" | \\\"full\\\" | null; reply_broadcast?: boolean | null; text?: string | null; unfurled_attachments?: unknown | null; }; message_id: string; }): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__slack_slack_read_thread\",\n      \"description\": \"Share work and pull context\\n\\nReads messages from a specific Slack thread (parent message + all replies). Read-only.\\n\\nRequires channel_id and message_ts of the parent message. Use slack_search_public or slack_read_channel to find these values. Use slack_search_public with \\\"is:thread\\\" to find threads by content. Use slack_send_message with thread_ts to reply to a thread. This tool is part of plugin `Slack`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__slack_slack_read_thread(args: {\\n  // Channel, private group, or IM channel to fetch thread replies for\\n  channel_id: string;\\n  // Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request\\n  cursor?: string;\\n  // End of time range of messages to include in results. Slack ts format string (e.g. \\\"1234567890.123456\\\").\\n  latest?: string;\\n  // Number of messages to return, between 1 and 1000. Default value is 100.\\n  limit?: number;\\n  // Timestamp of the parent message (e.g. \\\"1234567890.123456\\\"). Must be a string in Slack ts format with a decimal point.\\n  message_ts: string;\\n  // Start of time range of messages to include in results. Slack ts format string (e.g. \\\"1234567890.123456\\\").\\n  oldest?: string;\\n  // Level of detail: 'detailed' (default, includes reactions + thread info) or 'concise'.\\n  response_format?: string;\\n}): Promise<CallToolResult>; };\\n```\"\n    },\n    {\n      \"name\": \"mcp__codex_apps__slack_slack_send_message\",\n      \"description\": \"Share work and pull context\\n\\nSends a message to a Slack channel or user. To DM a user, use their user_id as channel_id. Return the message link to the user.\\n\\nMessage uses standard markdown (**bold**, _italic_, `code`, ~~strikethrough~~, >blockquotes, lists, links, code blocks, tables, headers). Limited to 5000 chars per text element. Tables use standard Markdown syntax with `|` as column delimiters. Do NOT escape the structural `|` characters that form the table borders and column separators. Only escape `|` as `\\\\|` when a literal pipe character appears inside a cell value. Code blocks can include a language specifier (e.g. ```python, ```js, ```bash) for syntax highlighting and copy functionality. Do not include sensitive info in link query params. Cannot post to externally shared (Slack Connect) channels.\\n\\nThread replies: set thread_ts to parent message timestamp, reply_broadcast=true to also post to channel.\\n\\nLink previews: when your message contains links from apps installed in the workspace (e.g. GitHub, Jira, Figma), set unfurl_app_links=true to enable rich link previews for those URLs.\\n\\nUse slack_search_channels to find channel IDs, slack_search_users to find user IDs.\\nIf user explicitly requests a draft, use slack_send_message_draft instead. This tool is part of plugin `Slack`.\\n\\nexec tool declaration:\\n```ts\\ndeclare const tools: { mcp__codex_apps__slack_slack_send_message(args: {\\n  // Search all channels\\n  channel_id: string;\\n  // ID of the draft to delete after sending\\n  draft_id?: string;\\n  // Add a message\\n  message: string;\\n  // Also send to conversation\\n  reply_broadcast?: boolean;\\n  // Provide another message's ts value to make this message a reply\\n  thread_ts?: string;\\n  // Set to true to enable link previews from installed apps (e.g. GitHub, Jira) in the message\\n  unfurl_app_links?: boolean;\\n}): Promise<CallToolResult>; };\\n```\"\n    }\n  ],\n  \"nativeTools\": [\n    \"functions.exec\",\n    \"functions.wait\",\n    \"collaboration.spawn_agent\",\n    \"mcp__cua_repl.js\"\n  ],\n  \"limits\": \"No configured target app, channel event automation API, tracker target, source channel ID or thread root timestamp. Worker isolation from Slack write tools not established.\"\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/check.mjs",
      "sha256": "c55134611573e7e0bc3856bc1a7705b7cc580823d62be432d8da174b22c42f82",
      "bytes": 1503,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "import {strict as assert} from 'node:assert';\nimport {apply} from './model.mjs';\nconst initial={status:{'1':'pending','2':'pending'},selected:[],pending:null,undo:null};\nlet a=apply(initial,'toolbar','select',['1','2']);a=apply(a,'toolbar','choose','shipped');\nassert.equal(a.status['1'],'pending');a=apply(a,'toolbar','confirm');assert.equal(a.status['1'],'shipped');assert.equal(a.status['2'],'shipped');\nlet b=apply(initial,'board','move',{id:'1',status:'shipped'});assert.equal(b.status['1'],'shipped');b=apply(b,'board','undo');assert.equal(b.status['1'],'pending');\nlet c=apply(initial,'command','parse','ship 1');assert.equal(c.status['1'],'pending');c=apply(c,'command','confirm');assert.equal(c.status['1'],'shipped');assert.equal(c.status['2'],'pending');\nassert.equal(apply(initial,'command','parse','destroy all').pending,null);\nassert.equal(initial.status['1'],'pending');\nconst manifest=await Bun.file(import.meta.dir+'/source-manifest.json').json();for(const f of manifest){const bytes=await Bun.file(import.meta.dir+'/'+f.artifact).arrayBuffer();assert.equal(new Bun.CryptoHasher('sha256').update(bytes).digest('hex'),f.sha256);}\nconsole.log(JSON.stringify({caseId:'alternatives',executed:['toolbar selection-preview-confirm for two items','board move and undo','command parse-preview-confirm','invalid command rejection','input remains unchanged','source snapshot hashes'],limits:'State-model checks only. Browser rendering, keyboard focus, drag feel and usability are not tested.'}));\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/command-result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/command-result.json",
      "sha256": "ed82fcae7d76984915a39f5d9e4b5d53a5ba6de54c7c0ae615b3a3beb45e1728",
      "bytes": 580,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "{\n  \"command\": \"bun run alternatives/check.mjs\",\n  \"tool\": \"functions.exec -> tools.exec_command\",\n  \"chunk_id\": \"6f379b\",\n  \"wall_time_seconds\": 0.000005083,\n  \"exit_code\": 0,\n  \"original_token_count\": 84,\n  \"output\": \"{\\\"caseId\\\":\\\"alternatives\\\",\\\"executed\\\":[\\\"toolbar selection-preview-confirm for two items\\\",\\\"board move and undo\\\",\\\"command parse-preview-confirm\\\",\\\"invalid command rejection\\\",\\\"input remains unchanged\\\",\\\"source snapshot hashes\\\"],\\\"limits\\\":\\\"State-model checks only. Browser rendering, keyboard focus, drag feel and usability are not tested.\\\"}\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/contract.json",
      "sha256": "ccab187586cb3981747f67490f7fae8e232c9fce57963143acb0d987b35405eb",
      "bytes": 1603,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "{\n  \"id\": \"alternatives\",\n  \"sourcePaths\": [\n    \"skills/principle-exhaust-the-design-space/SKILL.md\"\n  ],\n  \"prompt\": \"A novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.\",\n  \"requirements\": [\n    \"Identify a novel decision with multiple viable approaches\",\n    \"Compare 2-3 distinct prototypes or sketches side by side\",\n    \"Observe available write and execution tools and permissions before using them\"\n  ],\n  \"expectedFull\": \"Build 2-3 distinct prototypes or sketches, compare them side by side, and choose only after comparison. Report executed checks only when observed. Explain that minor variations of one approach do not count and that established patterns or a single viable approach do not require this exploration.\",\n  \"expectedReduced\": \"Without execution, compare 2-3 distinct sketches or proposals and label them untested. State that runtime behavior and interaction feel remain unverified. Without writes, keep sketches in the response and disclose the limitation.\",\n  \"expectedBlocked\": \"If required prototype construction or evaluation is denied or unavailable and sketches cannot answer the decision, report that step as blocked and identify the missing capability without claiming a completed comparison.\",\n  \"forbiddenClaims\": [\n    \"Execution or interaction testing occurred without observed results\",\n    \"Minor variants count as distinct alternatives\",\n    \"Prototype work authorizes publishing or external writes\",\n    \"Static review establishes host parity\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/http-command-result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/http-command-result.json",
      "sha256": "19978bb4bb187b3722a5837b8f0071712a7c138bb49af4686148382bf3679a97",
      "bytes": 231,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "{\n  \"chunk_id\": \"cbeaea\",\n  \"wall_time_seconds\": 0.000006041,\n  \"exit_code\": 0,\n  \"original_token_count\": 22,\n  \"output\": \"{\\\"path\\\":\\\"/\\\",\\\"status\\\":200,\\\"bytes\\\":3772}\\n{\\\"path\\\":\\\"/model.mjs\\\",\\\"status\\\":200,\\\"bytes\\\":795}\\n\"\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/model.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/model.mjs",
      "sha256": "63a304ec27fa96f19335c6e8c876ba4d6de163affbd6089e41a586f7729caafd",
      "bytes": 795,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "export function apply(state, approach, action, value) {\n const s=structuredClone(state);\n if(approach==='toolbar') {\n  if(action==='select') s.selected=value;\n  if(action==='choose') s.pending=value;\n  if(action==='confirm') {for(const id of s.selected)s.status[id]=s.pending;s.selected=[];s.pending=null;}\n } else if(approach==='board') {\n  if(action==='move') {s.undo={id:value.id,old:s.status[value.id]};s.status[value.id]=value.status;}\n  if(action==='undo'&&s.undo) {s.status[s.undo.id]=s.undo.old;s.undo=null;}\n } else if(approach==='command') {\n  if(action==='parse') {const m=/^ship (\\d+)$/i.exec(value);s.pending=m&&s.status[m[1]]==='pending'?{id:m[1],status:'shipped'}:null;}\n  if(action==='confirm'&&s.pending){s.status[s.pending.id]=s.pending.status;s.pending=null;}\n }\n return s;\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/serve.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/serve.mjs",
      "sha256": "de65aa82bc1c91fb9f95394b010530769555d5479d0c6df2cd8d186407bb547e",
      "bytes": 314,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "const server=Bun.serve({hostname:'127.0.0.1',port:0,fetch(req){const path=new URL(req.url).pathname;const allowed={'/':'sketches.html','/model.mjs':'model.mjs'};return allowed[path]?new Response(Bun.file(import.meta.dir+'/'+allowed[path])):new Response('Not found',{status:404});}});\nconsole.log(server.url.href);\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/server-command-results.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/server-command-results.json",
      "sha256": "bda6d1917fdcd36e5bed88f0cd0d3c245e876aa5619706d82a3f362adf645d65",
      "bytes": 333,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "{\n  \"start\": {\n    \"chunk_id\": \"c864ee\",\n    \"wall_time_seconds\": 1.00124725,\n    \"session_id\": 20567,\n    \"original_token_count\": 6,\n    \"output\": \"http://127.0.0.1:50856/\\n\"\n  },\n  \"stop\": {\n    \"chunk_id\": \"06523c\",\n    \"wall_time_seconds\": 0.000701125,\n    \"exit_code\": 130,\n    \"original_token_count\": 0,\n    \"output\": \"\"\n  }\n}\n"
    },
    {
      "path": "fixtures/batch-00/alternatives/sketches.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives/sketches.html",
      "sha256": "e85747edd0cf43e9776be3f35b1ae77cb8babee4f59d6aa26e494d642d55fae8",
      "bytes": 3772,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Order status interaction sketches</title>\n<style>body{font:17px system-ui;background:#f4f3ef;color:#182720;margin:40px}main{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}section{background:white;border:1px solid #bbc8bf;padding:22px;border-radius:10px}button,input,select{font:inherit;margin:7px 0;padding:8px}button{cursor:pointer}h2{font-size:21px}output{display:block;min-height:3em;padding:12px;background:#edf3ee}label{display:block}small{color:#465d50}@media(max-width:850px){main{grid-template-columns:1fr}}</style>\n<h1>Change order status</h1><p>Three distinct local interaction sketches. Synthetic orders 1 and 2 start pending. No service is contacted.</p>\n<main>\n<section><h2>A. Selection and bulk toolbar</h2><p>Choose rows, preview a change, then confirm the batch.</p><label><input type=\"checkbox\" name=\"row\" value=\"1\">Order 1</label><label><input type=\"checkbox\" name=\"row\" value=\"2\">Order 2</label><button id=\"preview\">Preview shipped</button><button id=\"batch\">Confirm batch</button><output id=\"a\">No batch prepared.</output><small>Explicit confirmation. Works for large lists.</small></section>\n<section><h2>B. Status board</h2><p>Move a card directly to the destination lane. Undo reverses the last move.</p><div id=\"pending\" style=\"border:1px dashed;padding:12px\">Pending <button draggable=\"true\" id=\"card\">Order 1</button></div><div id=\"shipped\" style=\"border:1px dashed;padding:12px;min-height:60px\">Shipped: drop here</div><button id=\"move\">Move order 1 to shipped</button><button id=\"undo\">Undo</button><output id=\"b\">Order 1 is pending.</output><small>Spatial control plus a keyboard-accessible move button.</small></section>\n<section><h2>C. Command with preview</h2><p>Type a structured command, inspect its target, and execute it.</p><label>Command <input id=\"command\" placeholder=\"ship 1\" autocomplete=\"off\"></label><button id=\"parse\">Preview command</button><button id=\"execute\">Execute confirmed command</button><output id=\"c\">No command prepared.</output><small>Compact for frequent users. Invalid syntax changes nothing.</small></section>\n</main><p>Exploratory sketches only. Interaction feel, accessibility and usability are unverified.</p>\n<script type=\"module\">\nimport {apply} from './model.mjs';\nconst fresh=()=>({status:{'1':'pending','2':'pending'},selected:[],pending:null,undo:null});let a=fresh(),b=fresh(),c=fresh();\nconst el=id=>document.getElementById(id);\nel('preview').onclick=()=>{a=apply(a,'toolbar','select',[...document.querySelectorAll('[name=row]:checked')].map(x=>x.value));a=apply(a,'toolbar','choose','shipped');el('a').textContent=`Preview: ${a.selected.length} selected orders to shipped.`};\nel('batch').onclick=()=>{if(!a.pending)return; a=apply(a,'toolbar','confirm');el('a').textContent=JSON.stringify(a.status)};\nfunction move(){b=apply(b,'board','move',{id:'1',status:'shipped'});el('shipped').append(el('card'));el('b').textContent='Order 1 is shipped.'}\nel('card').ondragstart=e=>e.dataTransfer.setData('text/plain','order-1');el('shipped').ondragover=e=>e.preventDefault();el('shipped').ondrop=e=>{e.preventDefault();if(e.dataTransfer.getData('text/plain')==='order-1')move()};el('move').onclick=move;\nel('undo').onclick=()=>{b=apply(b,'board','undo');el(b.status['1']).append(el('card'));el('b').textContent=`Order 1 is ${b.status['1']}.`};\nel('parse').onclick=()=>{c=apply(c,'command','parse',el('command').value);el('c').textContent=c.pending?`Preview: ship order ${c.pending.id}.`:'Invalid command or ineligible order.'};el('execute').onclick=()=>{if(!c.pending)return;c=apply(c,'command','confirm');el('c').textContent=JSON.stringify(c.status)};\n</script></html>\n"
    },
    {
      "path": "fixtures/batch-00/alternatives.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-00/alternatives.result.md",
      "sha256": "ce9bf683588fec35bf0a7cc28f9b7b7e5b20ab36800962a20d97d5743ac5ee77",
      "bytes": 5439,
      "owners": [
        "grades-native-00-01.json#0"
      ],
      "text": "# alternatives\n\n## Supplied input\n\nA novel UI interaction has no precedent in this codebase. Compare distinct approaches before implementation. If execution is unavailable, label untested proposals.\n\n- Identify a novel decision with multiple viable approaches.\n- Compare 2-3 distinct prototypes or sketches side by side.\n- Observe available write and execution tools and permissions before using them.\n\n[Exact input and requested source path](./alternatives/input.json). [Installed case contract](./alternatives/contract.json).\n\n## Actual response and comparison\n\nThe decision is how a user changes the status of orders, including batches. This is an explicitly chosen synthetic design exercise: no product interaction specification or actual codebase precedent was supplied. The copied dashboard fixture offers filtering and CSV export, but no status-changing UI. It does not prove the absence of precedent in a larger repository.\n\nThree concrete sketches appear side by side in [sketches.html](./alternatives/sketches.html). They share [an executable state model](./alternatives/model.mjs) but use different user actions and confirmation mechanisms.\n\n| Approach | Concrete sequence | Benefit | Cost and failure mode | Executed evidence |\n| --- | --- | --- | --- | --- |\n| A. Selection and bulk toolbar | Select orders, preview shipped, confirm batch | Supports batches and explicit target review | Selection can become stale; large selections need a count and snapshot | State check changed both selected orders only after confirmation |\n| B. Status board | Move an order into a status lane, undo if needed | Makes workflow position visible | Dense lanes and touch/keyboard operation need evaluation; undo must respect later changes | State check moved one order and restored its previous status |\n| C. Command with preview | Type `ship 1`, preview the target, confirm | Compact for frequent users | Syntax discovery and ambiguous IDs need work; invalid commands must do nothing | State check rejected invalid syntax and changed one eligible order after confirmation |\n\nChoose A provisionally after this comparison. The assumed task includes batch work, and selection plus a counted preview exposes the affected set before applying a change. This is a design recommendation, not a validated usability finding or production implementation. Confirm stale-selection behavior, focus order, eligibility changes and error recovery before integrating it. B would fit a small workflow board; C would suit repeated expert commands. Minor styling variations would not be distinct alternatives. Established patterns and decisions with only one viable approach do not need this exploration.\n\n## Actual tools, actions and outputs\n\nBefore prototype writes, the session exposed functions.exec with tools.exec_command and tools.apply_patch. The user granted writes under this case root and Bun execution, while forbidding external writes. Bun 1.4.2 was observed. The installed skill and host-capabilities reference were read before construction. [Source snapshots and hashes](./alternatives/source-manifest.json) retain the actual installed bytes.\n\n[check.mjs](./alternatives/check.mjs) ran through Bun and exited 0. It exercised batch preview/confirm, board move/undo, command preview/confirm, invalid command rejection, unchanged initial input, and source hashes. [Exact command stdout and exit status](./alternatives/command-result.json). These tests cover the state model, not browser event wiring or accessibility.\n\n[serve.mjs](./alternatives/serve.mjs) started a loopback-only server. Actual HTTP requests returned 200 for the page and model. [HTTP command result](./alternatives/http-command-result.json). mcp__cua_repl.js then attempted to open that local page in iab and returned `Browser is not available: iab`. [Exact browser attempt](./alternatives/browser-attempt.json). No screenshot, browser click, drag, keyboard test, or visual review occurred. The server was stopped with Ctrl-C and exited 130. [Start and stop command results](./alternatives/server-command-results.json).\n\n## Variants attempted\n\n- Available local writes and execution: built all three sketches and ran the state checks. HTTP delivery worked; browser execution was unavailable through the attempted iab method.\n- No execution fallback: the comparison table and concrete sequences are usable as untested interaction sketches. This negative execution condition was not enforced by the host, since Bun execution worked. No claim of a tested runtime fallback.\n- No writes fallback: the table is also the inline sketch response. Write denial was not enforced or attempted; authorized local writes succeeded. No claim that the host is read-only.\n\n## Limits\n\nInteraction feel, rendering, drag behavior, touch use, accessibility, focus and browser event wiring remain unverified. No product app was modified. Fixtures were copied from shared before use. Only the requested installed 0.1.0 package root supplied skill instructions. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is user-supplied provenance; the installed root has no .git directory, so the SHA could not be independently verified. Content hashes identify the bytes read. Invocation metadata was preserved in source snapshots; host enforcement of disable-model-invocation was not tested. No worker, model-diversity, live-service, publishing, commit, or parity result is claimed. No self-assigned grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-00/alternatives/dashboard.mjs",
      "owner": "grades-native-00-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-00/alternatives/fixture-README.md",
      "owner": "grades-native-00-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-00/alternatives/input.json",
      "owner": "grades-native-00-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-00/alternatives/orders.json",
      "owner": "grades-native-00-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-00/alternatives/source-manifest.json",
      "owner": "grades-native-00-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-00/alternatives/source-read",
      "owner": "grades-native-00-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-00/alternatives/dashboard.mjs",
      "owner": "grades-native-00-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-00/alternatives/fixture-README.md",
      "owner": "grades-native-00-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-00/alternatives/input.json",
      "owner": "grades-native-00-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-00/alternatives/orders.json",
      "owner": "grades-native-00-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-00/alternatives/source-manifest.json",
      "owner": "grades-native-00-01.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-00/alternatives/source-read",
      "owner": "grades-native-00-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
