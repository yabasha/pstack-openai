# codex: resume-revision

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "resume-revision",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-04.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.",
  "caseDefinition": {
    "id": "resume-revision",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/session-pickup.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md"
    ],
    "prompt": "Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.",
    "requirements": [
      "Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.",
      "Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.",
      "Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.",
      "Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.",
      "Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.",
      "Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.",
      "Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work."
    ],
    "expectedFull": "Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.",
    "expectedReduced": "Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action.",
    "expectedBlocked": "Missing or denied scoped history, revision or artifact inspection leaves the resume point provisional and blocks dependent execution. A missing routed playbook blocks that route. Unknown external outcome blocks replay even when ordinary local pickup can proceed.",
    "forbiddenClaims": [
      "Reading unrelated private chats or globbing across workspace histories is authorized by pickup.",
      "Prior self-report proves shipped work or current live state.",
      "A stale SHA or mismatched assignment can be accepted without reconciliation.",
      "Sequential transcript reduction proves independent workers or observed model diversity.",
      "Unknown external outcome permits automatic retry or implies completion.",
      "A referenced or proposed continuation record proves saved state or cross-session continuity.",
      "A structural case or validation proves either host ran this workflow."
    ],
    "caseFile": "docs/parity/cases/playbooks/session-pickup.json"
  },
  "registry": {
    "caseId": "resume-revision",
    "caseFile": "docs/parity/cases/playbooks/session-pickup.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/session-pickup.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md"
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
      "attemptId": "grades-native-04.json#3",
      "order": 0,
      "gradeFile": "grades-native-04.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "resume-revision",
      "status": "reduced-pass",
      "grade": {
        "caseId": "resume-revision",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-04.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_15",
          "item_22"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Full task revision/base/current checkout and long transcript absent.",
          "Actual destination state absent; replay forbidden."
        ],
        "review": "Bounded scoped capsule analysis overrides unsupported shipped claims with local-proposal status; inspects actual copied cache/caller, routes Bug fix at revision reconciliation, saves/readbacks continuation and blocks unknown external replay. Missing base/current Git and full trail prevent complete pickup.",
        "responseArtifact": "fixtures/batch-04/resume-revision.result.md",
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
        "fullExpected": "Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.",
        "reducedExpected": "Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action."
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
        "text": "# resume-revision\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"resume-revision\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n  \"requirements\": [\n    \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n    \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n    \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n    \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n    \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n    \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n    \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n  ]\n}\n```\n\n## Actual response and output\n\nSession pickup found a partial supplied capsule, not the full continuation described in the prompt. The metadata names cache invalidation teardown. Its fullGitRevision is null, its branch is explicitly not supplied, its prior status is \"local proposal only\", and its missing list includes the full base SHA and actual scoped seven-day history. The seven-event digest is synthetic. I read the overview, last message and decision points only within those supplied records. No personal workspace histories were searched for this case.\n\nWhere the prior agent stopped is provisionally a local cache proposal. The digest includes two unsupported \"shipped\" claims and user corrections. I inherited Bun, proposal-before-skill-edit and evidence-bound status rules. I did not inherit a verified shipment. No prior repro was restarted. No completed work or concurrent code was overwritten.\n\nActual revision comparison is blocked. The current fixture root is not a Git checkout. Read-only branch, worktree, full HEAD, log and status commands failed with exit 128. The diff command failed with exit 129. There is no recorded base against which a diff can be formed, and the package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is not a task revision. A later worktree revision and concurrent changes cannot be confirmed. Exact outputs are in [host-inspection.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/host-inspection.json).\n\nProve It Works changed the inherited completion claim into direct artifact inspection. The copied cache after-state immediately calls entries.delete. The supplied diff describes replacing deferred deletion with immediate deletion. The copied caller reads get(key).ready in a callback, while the pinned disposer queues the callback as a microtask. Static source supports an ordering concern. It does not prove a landed fix or runtime failure. No repro, regression test or original completed-unit verification was run.\n\nThe external action is fixture-verdict-post-1. Its outcome is unknown and authorizationToReplay is false. The intended destination and independently observed destination state are absent. No replay was attempted. Recovery requires that missing destination evidence, explicit permission and supported idempotent safety, and this evaluation independently forbids external writes.\n\nVerdict: override the unsupported shipped conclusion with a provisional local-proposal status. The routed resume point is the Bug fix playbook, read in full, starting at revision and evidence reconciliation before its reproduction step. Dependent execution is blocked until the scoped checkout, recorded base, exact full assignment SHA, completed-unit artifacts and full relevant trail are supplied. Its required delegation and matching-control verification remain unsatisfied. I also read Investigation as an alternative route but did not start a separate controller or its dependent how investigation.\n\nGuard the Context Window kept the available seven-event digest bounded and sequential. No long transcript was supplied to delegate. The host exposes collaboration.spawn_agent, but no history worker was launched. Requested selection would be inherit-parent; observed worker model and effort are unknown. This is a bounded sequential reduced handoff, not independent reconstruction.\n\nThe saved [continuation.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json) records this blocked resume point and was read back. This verifies local persistence of a partial handoff only. It does not establish complete cross-session continuity, unattended recovery, the missing history, or a verified original outcome.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/.\n\n\n\n## Variants and limits\n\nAttempted actual Git inspection and bounded supplied-history reconstruction. Base-versus-later-HEAD and concurrent-change reconciliation are blocked. Long-history independent reconstruction and external recovery were not attempted because their required evidence is absent. Only the partial local handoff was saved.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-04/resume-revision.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision.result.md",
          "sha256": "95d96e8837cc86842d45e40f5ed155f2177de96fb09fcf06aac87ba920731155",
          "bytes": 7884
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
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2a159b40b8943f8e35e80aeb982c727f5235c07b8f9f62bafd5c1b084f05c0ea"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "860d291d8f06560ed8b5603aad27548aaaa20dfd9f90ee7b725cf03b178f1526",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "87067ba7565f08ae2aad54f7e07e5204899ae0f0f4ecb5cac447f058d1e30019"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "87ec627cc979a094ba72a5d26070879a7b420e2a98fe99bfe2535aa1f29b0359",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "76ae48089a9c131d31403fe9e8849665256806b4a811026fcb143631e2fd10b4"
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "eda349ba00d6ca3082b90b372e4f2a425c790e6b238552612b269ca1dbfd3fae",
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
            "item_15",
            "item_22"
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
      "path": "fixtures/batch-04/resume-revision/continuation.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json",
      "sha256": "305afa0d1d9e287192b9e58b50d621a9da04bdf23da976185a18d1ee3c35f596",
      "bytes": 1040,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "{\n  \"provenance\": \"current evaluation partial handoff\",\n  \"priorActionId\": \"fixture-verdict-post-1\",\n  \"priorOutcome\": \"unknown\",\n  \"externalReplayAuthorized\": false,\n  \"taskBase\": null,\n  \"taskHead\": null,\n  \"revisionComparison\": \"blocked; no task Git checkout\",\n  \"priorStatus\": \"local proposal only\",\n  \"verifiedArtifact\": \"copied source immediately deletes cache entries; no runtime check performed\",\n  \"verdict\": \"override unsupported shipped claim\",\n  \"route\": \"Bug fix after revision/evidence reconciliation\",\n  \"resumePoint\": \"obtain scoped checkout, full base and input SHA, completed-unit artifacts and relevant trail; no replay\",\n  \"permissions\": [\n    \"Bun\",\n    \"owned local writes\",\n    \"no external writes\",\n    \"no commits\",\n    \"propose skill edits before applying\"\n  ],\n  \"workerMethod\": \"bounded sequential supplied seven-event digest\",\n  \"missing\": [\n    \"scoped long transcript\",\n    \"base SHA\",\n    \"current task Git revision\",\n    \"completed-unit proof\",\n    \"action destination and actual destination outcome\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/resume-revision/host-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/host-inspection.json",
      "sha256": "d7314a084af7c65dedd1370a0fda306854a98b18389153c865c5021efd49190c",
      "bytes": 10395,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "[\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"--show-toplevel\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"branch\",\n      \"--show-current\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"worktree\",\n      \"list\",\n      \"--porcelain\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"log\",\n      \"-5\",\n      \"--format=%H %s\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"status\",\n      \"--short\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"diff\",\n      \"--stat\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 129,\n    \"stdout\": \"\",\n    \"stderr\": \"warning: Not a git repository. Use --no-index to compare two paths outside a working tree\\nusage: git diff --no-index [<options>] <path> <path> [<pathspec>...]\\n\\nDiff output format options\\n    -p, --patch           generate patch\\n    -s, --no-patch        suppress diff output\\n    -u                    generate patch\\n    -U, --unified[=<n>]   generate diffs with <n> lines context\\n    -W, --[no-]function-context\\n                          generate diffs with <n> lines context\\n    --raw                 generate the diff in raw format\\n    --patch-with-raw      synonym for '-p --raw'\\n    --patch-with-stat     synonym for '-p --stat'\\n    --numstat             machine friendly --stat\\n    --shortstat           output only the last line of --stat\\n    -X, --dirstat[=<param1>,<param2>...]\\n                          output the distribution of relative amount of changes for each sub-directory\\n    --cumulative          synonym for --dirstat=cumulative\\n    --dirstat-by-file[=<param1>,<param2>...]\\n                          synonym for --dirstat=files,<param1>,<param2>...\\n    --check               warn if changes introduce conflict markers or whitespace errors\\n    --summary             condensed summary such as creations, renames and mode changes\\n    --name-only           show only names of changed files\\n    --name-status         show only names and status of changed files\\n    --stat[=<width>[,<name-width>[,<count>]]]\\n                          generate diffstat\\n    --stat-width <width>  generate diffstat with a given width\\n    --stat-name-width <width>\\n                          generate diffstat with a given name width\\n    --stat-graph-width <width>\\n                          generate diffstat with a given graph width\\n    --stat-count <count>  generate diffstat with limited lines\\n    --[no-]compact-summary\\n                          generate compact summary in diffstat\\n    --binary              output a binary diff that can be applied\\n    --[no-]full-index     show full pre- and post-image object names on the \\\"index\\\" lines\\n    --[no-]color[=<when>] show colored diff\\n    --ws-error-highlight <kind>\\n                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff\\n    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat\\n    --[no-]abbrev[=<n>]   use <n> digits to display object names\\n    --src-prefix <prefix> show the given source prefix instead of \\\"a/\\\"\\n    --dst-prefix <prefix> show the given destination prefix instead of \\\"b/\\\"\\n    --line-prefix <prefix>\\n                          prepend an additional prefix to every line of output\\n    --no-prefix           do not show any source or destination prefix\\n    --default-prefix      use default prefixes a/ and b/\\n    --inter-hunk-context <n>\\n                          show context between diff hunks up to the specified number of lines\\n    --output-indicator-new <char>\\n                          specify the character to indicate a new line instead of '+'\\n    --output-indicator-old <char>\\n                          specify the character to indicate an old line instead of '-'\\n    --output-indicator-context <char>\\n                          specify the character to indicate a context instead of ' '\\n\\nDiff rename options\\n    -B, --break-rewrites[=<n>[/<m>]]\\n                          break complete rewrite changes into pairs of delete and create\\n    -M, --find-renames[=<n>]\\n                          detect renames\\n    -D, --irreversible-delete\\n                          omit the preimage for deletes\\n    -C, --find-copies[=<n>]\\n                          detect copies\\n    --[no-]find-copies-harder\\n                          use unmodified files as source to find copies\\n    --no-renames          disable rename detection\\n    --[no-]rename-empty   use empty blobs as rename source\\n    --[no-]follow         continue listing the history of a file beyond renames\\n    -l <n>                limit to cheap rename/copy detection if the number of rename/copy targets exceeds this value\\n\\nDiff algorithm options\\n    --minimal             produce the smallest possible diff\\n    -w, --ignore-all-space\\n                          ignore whitespace when comparing lines\\n    -b, --ignore-space-change\\n                          ignore changes in amount of whitespace\\n    --ignore-space-at-eol ignore changes in whitespace at EOL\\n    --ignore-cr-at-eol    ignore carrier-return at the end of line\\n    --ignore-blank-lines  ignore changes whose lines are all blank\\n    -I, --[no-]ignore-matching-lines <regex>\\n                          ignore changes whose all lines match <regex>\\n    --[no-]indent-heuristic\\n                          heuristic to shift diff hunk boundaries for easy reading\\n    --patience            generate diff using the \\\"patience diff\\\" algorithm\\n    --histogram           generate diff using the \\\"histogram diff\\\" algorithm\\n    --diff-algorithm <algorithm>\\n                          choose a diff algorithm\\n    --anchored <text>     generate diff using the \\\"anchored diff\\\" algorithm\\n    --word-diff[=<mode>]  show word diff, using <mode> to delimit changed words\\n    --word-diff-regex <regex>\\n                          use <regex> to decide what a word is\\n    --color-words[=<regex>]\\n                          equivalent to --word-diff=color --word-diff-regex=<regex>\\n    --[no-]color-moved[=<mode>]\\n                          moved lines of code are colored differently\\n    --[no-]color-moved-ws <mode>\\n                          how white spaces are ignored in --color-moved\\n\\nOther diff options\\n    --[no-]relative[=<prefix>]\\n                          when run from subdir, exclude changes outside and show relative paths\\n    -a, --[no-]text       treat all files as text\\n    -R                    swap two inputs, reverse the diff\\n    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise\\n    --[no-]quiet          disable all output of the program\\n    --[no-]ext-diff       allow an external diff helper to be executed\\n    --[no-]textconv       run external text conversion filters when comparing binary files\\n    --ignore-submodules[=<when>]\\n                          ignore changes to submodules in the diff generation\\n    --submodule[=<format>]\\n                          specify how differences in submodules are shown\\n    --ita-invisible-in-index\\n                          hide 'git add -N' entries from the index\\n    --ita-visible-in-index\\n                          treat 'git add -N' entries as real in the index\\n    -S <string>           look for differences that change the number of occurrences of the specified string\\n    -G <regex>            look for differences that change the number of occurrences of the specified regex\\n    --pickaxe-all         show all changes in the changeset with -S or -G\\n    --pickaxe-regex       treat <string> in -S as extended POSIX regular expression\\n    -O <file>             control the order in which files appear in the output\\n    --rotate-to <path>    show the change in the specified path first\\n    --skip-to <path>      skip the output to the specified path\\n    --find-object <object-id>\\n                          look for differences that change the number of occurrences of the specified object\\n    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]\\n                          select files by diff type\\n    --max-depth <depth>   maximum tree depth to recurse\\n    --output <file>       output to a specific file\\n\\n\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-04/resume-revision/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/readback.json",
      "sha256": "ae2235e65235f83fe57e9f758c843e63db95a0b1dea2a01d1a9b0724bae0582a",
      "bytes": 498,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "{\n  \"report\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision.result.md\",\n  \"sha256\": \"95d96e8837cc86842d45e40f5ed155f2177de96fb09fcf06aac87ba920731155\",\n  \"readbackMatched\": true,\n  \"persisted\": [\n    {\n      \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json\",\n      \"sha256\": \"305afa0d1d9e287192b9e58b50d621a9da04bdf23da976185a18d1ee3c35f596\",\n      \"bytes\": 1040\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/resume-revision.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision.result.md",
      "sha256": "95d96e8837cc86842d45e40f5ed155f2177de96fb09fcf06aac87ba920731155",
      "bytes": 7884,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "# resume-revision\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"resume-revision\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n  \"requirements\": [\n    \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n    \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n    \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n    \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n    \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n    \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n    \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n  ]\n}\n```\n\n## Actual response and output\n\nSession pickup found a partial supplied capsule, not the full continuation described in the prompt. The metadata names cache invalidation teardown. Its fullGitRevision is null, its branch is explicitly not supplied, its prior status is \"local proposal only\", and its missing list includes the full base SHA and actual scoped seven-day history. The seven-event digest is synthetic. I read the overview, last message and decision points only within those supplied records. No personal workspace histories were searched for this case.\n\nWhere the prior agent stopped is provisionally a local cache proposal. The digest includes two unsupported \"shipped\" claims and user corrections. I inherited Bun, proposal-before-skill-edit and evidence-bound status rules. I did not inherit a verified shipment. No prior repro was restarted. No completed work or concurrent code was overwritten.\n\nActual revision comparison is blocked. The current fixture root is not a Git checkout. Read-only branch, worktree, full HEAD, log and status commands failed with exit 128. The diff command failed with exit 129. There is no recorded base against which a diff can be formed, and the package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is not a task revision. A later worktree revision and concurrent changes cannot be confirmed. Exact outputs are in [host-inspection.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/host-inspection.json).\n\nProve It Works changed the inherited completion claim into direct artifact inspection. The copied cache after-state immediately calls entries.delete. The supplied diff describes replacing deferred deletion with immediate deletion. The copied caller reads get(key).ready in a callback, while the pinned disposer queues the callback as a microtask. Static source supports an ordering concern. It does not prove a landed fix or runtime failure. No repro, regression test or original completed-unit verification was run.\n\nThe external action is fixture-verdict-post-1. Its outcome is unknown and authorizationToReplay is false. The intended destination and independently observed destination state are absent. No replay was attempted. Recovery requires that missing destination evidence, explicit permission and supported idempotent safety, and this evaluation independently forbids external writes.\n\nVerdict: override the unsupported shipped conclusion with a provisional local-proposal status. The routed resume point is the Bug fix playbook, read in full, starting at revision and evidence reconciliation before its reproduction step. Dependent execution is blocked until the scoped checkout, recorded base, exact full assignment SHA, completed-unit artifacts and full relevant trail are supplied. Its required delegation and matching-control verification remain unsatisfied. I also read Investigation as an alternative route but did not start a separate controller or its dependent how investigation.\n\nGuard the Context Window kept the available seven-event digest bounded and sequential. No long transcript was supplied to delegate. The host exposes collaboration.spawn_agent, but no history worker was launched. Requested selection would be inherit-parent; observed worker model and effort are unknown. This is a bounded sequential reduced handoff, not independent reconstruction.\n\nThe saved [continuation.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json) records this blocked resume point and was read back. This verifies local persistence of a partial handoff only. It does not establish complete cross-session continuity, unattended recovery, the missing history, or a verified original outcome.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/.\n\n\n\n## Variants and limits\n\nAttempted actual Git inspection and bounded supplied-history reconstruction. Base-versus-later-HEAD and concurrent-change reconciliation are blocked. Long-history independent reconstruction and external recovery were not attempted because their required evidence is absent. Only the partial local handoff was saved.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-04/resume-revision/additional-source-reads.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/fixture-README.md",
      "owner": "grades-native-04.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/resume-revision/input.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/inputs",
      "owner": "grades-native-04.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-04/resume-revision/source-manifest.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/additional-source-reads.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/fixture-README.md",
      "owner": "grades-native-04.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/resume-revision/input.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/inputs",
      "owner": "grades-native-04.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-04/resume-revision/source-manifest.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
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
