# codex: shared-path-conflict

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "shared-path-conflict",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-04.json#7",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Two workers request the same output path.",
  "caseDefinition": {
    "id": "shared-path-conflict",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "Two workers request the same output path.",
    "requirements": [
      "Coordinator assigns distinct paths before either writes.",
      "Capture exact input revision, explicit permissions and observed operation evidence."
    ],
    "expectedFull": "Coordinator resolves ownership into distinct paths before observed workers write.",
    "expectedReduced": "One authorized sequential writer produces output; worker independence is unclaimed.",
    "expectedBlocked": "Overlapping ownership remains unresolved; neither worker writes the contested path.",
    "forbiddenClaims": [
      "Case definition or fixture test proves host support.",
      "Independent workers without a successful exposed spawn operation.",
      "Full pass for sequential fallback.",
      "Retry external action without permission and prior action inspection."
    ],
    "caseFile": "docs/parity/cases/contracts.json"
  },
  "registry": {
    "caseId": "shared-path-conflict",
    "caseFile": "docs/parity/cases/contracts.json",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
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
        "resolve-ownership",
        "isolated-write",
        "read"
      ],
      "reduced-pass": [
        "isolated-write",
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
      "pass": [
        "writes"
      ],
      "reduced-pass": [
        "writes"
      ]
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-04.json#7",
      "order": 0,
      "gradeFile": "grades-native-04.json",
      "rankWithinFile": 7,
      "host": "codex",
      "caseId": "shared-path-conflict",
      "status": "blocked",
      "grade": {
        "caseId": "shared-path-conflict",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-04.events.jsonl",
        "actualReadEventIds": [
          "item_12",
          "item_14",
          "item_19"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Actual task Git revision and concrete worker task absent.",
          "No spawn/wait/inspect-result or independent owned writes.",
          "No authorized sequential execution of a concrete assigned payload, only planning artifacts."
        ],
        "review": "Ownership checker rejects duplicate/overlapping paths and saves distinct pending roles. Actual native operations exposed, but no taskSHA or concrete payload permits assignment; zero workers launched and no owned output written. Enforces corrected full worker-method contract rather than old direct false positive.",
        "responseArtifact": "fixtures/batch-04/shared-path-conflict.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [
          "Supply missing concrete inputs and rerun. Fixture incompleteness is not a skill source defect."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-04.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Coordinator resolves ownership into distinct paths before observed workers write.",
        "reducedExpected": "One authorized sequential writer produces output; worker independence is unclaimed.",
        "correctedContractReview": "Full requires native independent workers and owned output plus spawn/wait/result inspection. Pending plans are insufficient. No startup failure occurred: dispatch was not attempted due missing task revision/payload."
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
        "text": "# shared-path-conflict\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"shared-path-conflict\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\"\n  ],\n  \"prompt\": \"Two workers request the same output path.\",\n  \"requirements\": [\n    \"Coordinator assigns distinct paths before either writes.\",\n    \"Capture exact input revision, explicit permissions and observed operation evidence.\"\n  ]\n}\n```\n\n## Actual response and output\n\nSeparate Before Serializing Shared State changed the contested output into two distinct planned paths before any worker write. The coordinator rejected the duplicate output path and reserved worker-one/result.md and worker-two/result.md under this case. Only the coordinator would integrate a shared report. The local ownership check also rejects ancestor/descendant overlaps.\n\nThe saved [planned-assignments.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/planned-assignments.json) contains immutable pending plans, exact owned paths and explicit allowed and forbidden operations. outputOwner values are unbound planned roles, not invented worker IDs. Both task inputRevision values are null because read-only Git inspection failed. The package source freeze is a separate user-supplied instruction revision and cannot replace the task's full Git SHA.\n\nThe host exposes collaboration.spawn_agent, collaboration.wait_agent and related worker operations, and the user permits native isolated workers for these evaluations. However, the installed assignment contract requires a full task Git inputRevision before dispatch. Orchestrate also treats an unfillable brief field as a refuse-to-spawn condition. No task checkout, concrete worker payload or full input revision was supplied. I therefore did not launch fake work just to obtain a worker receipt. The observed model, effort and isolation are unknown; inherit-parent would be a requested policy only.\n\nObserved command evidence is in [host-inspection.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/host-inspection.json) and [ownership.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/ownership.receipt.json). The executable check rejected a duplicate path, accepted distinct planned paths and blocked dispatch without the task SHA. No worker wrote either path. No runtime race-prevention claim follows from this sequential coordinator check.\n\nThis two-output conflict is below Orchestrate's standing-program scale, so its Frame small-task collapse applies. No orchestration store, helper install, ledger or frontier was needed or invoked. There are zero worker attempts and no landed units. A program frontier, PR links and verification ledger are not available. None was invented. The local plans and result report are the only durable handoff.\n\nThroughput checkpoint: first reconcile revision and concrete worker acceptance inputs; independent workstreams are the two distinct output paths; shared mutable state belongs only to the coordinator; the smallest safe decomposition is a local ownership check until dispatch prerequisites exist. Worker execution remains blocked on those inputs, not on an observed lack of a native worker tool.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/.\n\n\nCommand: `bun --no-install check.mjs`. Exit 0. Full receipt: [ownership.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/ownership.receipt.json).\n\n```text\nRejected duplicate path. Assigned distinct paths before any worker writes. Dispatch blocked for missing task Git revision. No workers spawned.\n```\n\n\n## Variants and limits\n\nDuplicate-path and distinct-path planning checks ran. Missing-task-revision dispatch check rejected the plans. Native workers are exposed but were not spawned because the assignment contract cannot be satisfied. No fabricated worker or model observations.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-04/shared-path-conflict.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict.result.md",
          "sha256": "3236c225a6116a71267151c0f0a6d11342a88238773e5ad866db3354136e8a5a",
          "bytes": 6053
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
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1f2e8bdcc8604989787ac3ee28840dfed3d703a8ffd8398732282508f5db08ae"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "467beb11dce6fdb184fe61496efe374f22d7816ff1734110c9bacbc4b69be271",
                "commandResult": {
                  "exitCode": 128
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "968b45ece1bcbbd5ccb99e5adf993326defd0f6f0cbe6c171ca6b8c0c9e6a212"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c456012093ded766dc1d38465c71a84b220e503dac7e8ec5cc0844f56a4998b4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_19",
                "line": 35,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "034ef504598ef9a3e9fc53b89295cca14edf990ee9b7c70b2fcc207694ae8e59"
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "17a56f51a91f3757b32260b9b516167601c47e6a1597f4edac9a8ad7c566074c",
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
            "item_12",
            "item_14",
            "item_19"
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
      "path": "fixtures/batch-04/shared-path-conflict/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/check.mjs",
      "sha256": "836447c996f042229fbbe3651cb69604bf2c6167e9c07147fb28550f02d4e5d2",
      "bytes": 1251,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "import assert from 'node:assert/strict';\nimport {validateOwnership,readyToDispatch} from './ownership.mjs';\nconst original=[{outputPath:import.meta.dir+'/output.md'},{outputPath:import.meta.dir+'/output.md'}];\nassert.throws(()=>validateOwnership(original),/overlapping/);\nconst assignments=['one','two'].map((name,i)=>({id:'planned-'+name,scope:[import.meta.dir+'/worker-'+name+'/'],inputRevision:null,outputOwner:'unbound-worker-'+name,isolatedOutputPath:import.meta.dir+'/worker-'+name+'/result.md',outputPath:import.meta.dir+'/worker-'+name+'/result.md',role:'poteto-agent',retryCount:0,terminalStatus:'pending',evidenceLinks:['host-inspection.json'],permissions:{readInstalledPackage:true,writeOnlyAssignedPath:true,executeBun:true,externalWrites:false,commits:false,spawnChildren:false},dispatchOrder:null}));\nvalidateOwnership(assignments);assert.throws(()=>readyToDispatch(assignments),/missing full task Git/);\nawait Bun.write(import.meta.dir+'/planned-assignments.json',JSON.stringify({provenance:'coordinator-owned undispatched plan, no worker receipts',assignments},null,2)+'\\n');\nconsole.log('Rejected duplicate path. Assigned distinct paths before any worker writes. Dispatch blocked for missing task Git revision. No workers spawned.');\n"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/host-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/host-inspection.json",
      "sha256": "d7314a084af7c65dedd1370a0fda306854a98b18389153c865c5021efd49190c",
      "bytes": 10395,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "[\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"--show-toplevel\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"branch\",\n      \"--show-current\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"worktree\",\n      \"list\",\n      \"--porcelain\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"log\",\n      \"-5\",\n      \"--format=%H %s\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"status\",\n      \"--short\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"diff\",\n      \"--stat\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 129,\n    \"stdout\": \"\",\n    \"stderr\": \"warning: Not a git repository. Use --no-index to compare two paths outside a working tree\\nusage: git diff --no-index [<options>] <path> <path> [<pathspec>...]\\n\\nDiff output format options\\n    -p, --patch           generate patch\\n    -s, --no-patch        suppress diff output\\n    -u                    generate patch\\n    -U, --unified[=<n>]   generate diffs with <n> lines context\\n    -W, --[no-]function-context\\n                          generate diffs with <n> lines context\\n    --raw                 generate the diff in raw format\\n    --patch-with-raw      synonym for '-p --raw'\\n    --patch-with-stat     synonym for '-p --stat'\\n    --numstat             machine friendly --stat\\n    --shortstat           output only the last line of --stat\\n    -X, --dirstat[=<param1>,<param2>...]\\n                          output the distribution of relative amount of changes for each sub-directory\\n    --cumulative          synonym for --dirstat=cumulative\\n    --dirstat-by-file[=<param1>,<param2>...]\\n                          synonym for --dirstat=files,<param1>,<param2>...\\n    --check               warn if changes introduce conflict markers or whitespace errors\\n    --summary             condensed summary such as creations, renames and mode changes\\n    --name-only           show only names of changed files\\n    --name-status         show only names and status of changed files\\n    --stat[=<width>[,<name-width>[,<count>]]]\\n                          generate diffstat\\n    --stat-width <width>  generate diffstat with a given width\\n    --stat-name-width <width>\\n                          generate diffstat with a given name width\\n    --stat-graph-width <width>\\n                          generate diffstat with a given graph width\\n    --stat-count <count>  generate diffstat with limited lines\\n    --[no-]compact-summary\\n                          generate compact summary in diffstat\\n    --binary              output a binary diff that can be applied\\n    --[no-]full-index     show full pre- and post-image object names on the \\\"index\\\" lines\\n    --[no-]color[=<when>] show colored diff\\n    --ws-error-highlight <kind>\\n                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff\\n    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat\\n    --[no-]abbrev[=<n>]   use <n> digits to display object names\\n    --src-prefix <prefix> show the given source prefix instead of \\\"a/\\\"\\n    --dst-prefix <prefix> show the given destination prefix instead of \\\"b/\\\"\\n    --line-prefix <prefix>\\n                          prepend an additional prefix to every line of output\\n    --no-prefix           do not show any source or destination prefix\\n    --default-prefix      use default prefixes a/ and b/\\n    --inter-hunk-context <n>\\n                          show context between diff hunks up to the specified number of lines\\n    --output-indicator-new <char>\\n                          specify the character to indicate a new line instead of '+'\\n    --output-indicator-old <char>\\n                          specify the character to indicate an old line instead of '-'\\n    --output-indicator-context <char>\\n                          specify the character to indicate a context instead of ' '\\n\\nDiff rename options\\n    -B, --break-rewrites[=<n>[/<m>]]\\n                          break complete rewrite changes into pairs of delete and create\\n    -M, --find-renames[=<n>]\\n                          detect renames\\n    -D, --irreversible-delete\\n                          omit the preimage for deletes\\n    -C, --find-copies[=<n>]\\n                          detect copies\\n    --[no-]find-copies-harder\\n                          use unmodified files as source to find copies\\n    --no-renames          disable rename detection\\n    --[no-]rename-empty   use empty blobs as rename source\\n    --[no-]follow         continue listing the history of a file beyond renames\\n    -l <n>                limit to cheap rename/copy detection if the number of rename/copy targets exceeds this value\\n\\nDiff algorithm options\\n    --minimal             produce the smallest possible diff\\n    -w, --ignore-all-space\\n                          ignore whitespace when comparing lines\\n    -b, --ignore-space-change\\n                          ignore changes in amount of whitespace\\n    --ignore-space-at-eol ignore changes in whitespace at EOL\\n    --ignore-cr-at-eol    ignore carrier-return at the end of line\\n    --ignore-blank-lines  ignore changes whose lines are all blank\\n    -I, --[no-]ignore-matching-lines <regex>\\n                          ignore changes whose all lines match <regex>\\n    --[no-]indent-heuristic\\n                          heuristic to shift diff hunk boundaries for easy reading\\n    --patience            generate diff using the \\\"patience diff\\\" algorithm\\n    --histogram           generate diff using the \\\"histogram diff\\\" algorithm\\n    --diff-algorithm <algorithm>\\n                          choose a diff algorithm\\n    --anchored <text>     generate diff using the \\\"anchored diff\\\" algorithm\\n    --word-diff[=<mode>]  show word diff, using <mode> to delimit changed words\\n    --word-diff-regex <regex>\\n                          use <regex> to decide what a word is\\n    --color-words[=<regex>]\\n                          equivalent to --word-diff=color --word-diff-regex=<regex>\\n    --[no-]color-moved[=<mode>]\\n                          moved lines of code are colored differently\\n    --[no-]color-moved-ws <mode>\\n                          how white spaces are ignored in --color-moved\\n\\nOther diff options\\n    --[no-]relative[=<prefix>]\\n                          when run from subdir, exclude changes outside and show relative paths\\n    -a, --[no-]text       treat all files as text\\n    -R                    swap two inputs, reverse the diff\\n    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise\\n    --[no-]quiet          disable all output of the program\\n    --[no-]ext-diff       allow an external diff helper to be executed\\n    --[no-]textconv       run external text conversion filters when comparing binary files\\n    --ignore-submodules[=<when>]\\n                          ignore changes to submodules in the diff generation\\n    --submodule[=<format>]\\n                          specify how differences in submodules are shown\\n    --ita-invisible-in-index\\n                          hide 'git add -N' entries from the index\\n    --ita-visible-in-index\\n                          treat 'git add -N' entries as real in the index\\n    -S <string>           look for differences that change the number of occurrences of the specified string\\n    -G <regex>            look for differences that change the number of occurrences of the specified regex\\n    --pickaxe-all         show all changes in the changeset with -S or -G\\n    --pickaxe-regex       treat <string> in -S as extended POSIX regular expression\\n    -O <file>             control the order in which files appear in the output\\n    --rotate-to <path>    show the change in the specified path first\\n    --skip-to <path>      skip the output to the specified path\\n    --find-object <object-id>\\n                          look for differences that change the number of occurrences of the specified object\\n    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]\\n                          select files by diff type\\n    --max-depth <depth>   maximum tree depth to recurse\\n    --output <file>       output to a specific file\\n\\n\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/ownership.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/ownership.mjs",
      "sha256": "01391dcd8483ef96bea45af777ec80b4959beff9ad22dc8628160e195daa6152",
      "bytes": 631,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "import path from 'node:path';\nexport function validateOwnership(assignments){\n const seen=[];\n for(const a of assignments){const resolved=path.resolve(a.outputPath);if(seen.some(p=>p===resolved||p.startsWith(resolved+path.sep)||resolved.startsWith(p+path.sep)))throw Error('overlapping output ownership');seen.push(resolved)}\n return assignments;\n}\nexport function readyToDispatch(assignments){validateOwnership(assignments);if(assignments.some(a=>typeof a.inputRevision!=='string'||! /^[0-9a-f]{40}$/.test(a.inputRevision)))throw Error('missing full task Git input revision; package freeze is not the task revision');return true}\n"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/ownership.receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/ownership.receipt.json",
      "sha256": "0eaf5b04535aff0ae83a93a2e17fd5d5a20457dd897311da969bb76faa04cccf",
      "bytes": 439,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"check.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict\",\n  \"exitCode\": 0,\n  \"stdout\": \"Rejected duplicate path. Assigned distinct paths before any worker writes. Dispatch blocked for missing task Git revision. No workers spawned.\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/planned-assignments.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/planned-assignments.json",
      "sha256": "171e8117cfa232b903ad19b226bea209ae013651182591456f94bc32e1fcaf85",
      "bytes": 2029,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "{\n  \"provenance\": \"coordinator-owned undispatched plan, no worker receipts\",\n  \"assignments\": [\n    {\n      \"id\": \"planned-one\",\n      \"scope\": [\n        \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/worker-one/\"\n      ],\n      \"inputRevision\": null,\n      \"outputOwner\": \"unbound-worker-one\",\n      \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/worker-one/result.md\",\n      \"outputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/worker-one/result.md\",\n      \"role\": \"poteto-agent\",\n      \"retryCount\": 0,\n      \"terminalStatus\": \"pending\",\n      \"evidenceLinks\": [\n        \"host-inspection.json\"\n      ],\n      \"permissions\": {\n        \"readInstalledPackage\": true,\n        \"writeOnlyAssignedPath\": true,\n        \"executeBun\": true,\n        \"externalWrites\": false,\n        \"commits\": false,\n        \"spawnChildren\": false\n      },\n      \"dispatchOrder\": null\n    },\n    {\n      \"id\": \"planned-two\",\n      \"scope\": [\n        \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/worker-two/\"\n      ],\n      \"inputRevision\": null,\n      \"outputOwner\": \"unbound-worker-two\",\n      \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/worker-two/result.md\",\n      \"outputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/worker-two/result.md\",\n      \"role\": \"poteto-agent\",\n      \"retryCount\": 0,\n      \"terminalStatus\": \"pending\",\n      \"evidenceLinks\": [\n        \"host-inspection.json\"\n      ],\n      \"permissions\": {\n        \"readInstalledPackage\": true,\n        \"writeOnlyAssignedPath\": true,\n        \"executeBun\": true,\n        \"externalWrites\": false,\n        \"commits\": false,\n        \"spawnChildren\": false\n      },\n      \"dispatchOrder\": null\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/readback.json",
      "sha256": "fac24b07d0214a1841cb0c896d3342385515e04e92a3b5fb1703b882bd30567f",
      "bytes": 515,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "{\n  \"report\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict.result.md\",\n  \"sha256\": \"3236c225a6116a71267151c0f0a6d11342a88238773e5ad866db3354136e8a5a\",\n  \"readbackMatched\": true,\n  \"persisted\": [\n    {\n      \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/planned-assignments.json\",\n      \"sha256\": \"171e8117cfa232b903ad19b226bea209ae013651182591456f94bc32e1fcaf85\",\n      \"bytes\": 2029\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict.result.md",
      "sha256": "3236c225a6116a71267151c0f0a6d11342a88238773e5ad866db3354136e8a5a",
      "bytes": 6053,
      "owners": [
        "grades-native-04.json#7"
      ],
      "text": "# shared-path-conflict\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"shared-path-conflict\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\"\n  ],\n  \"prompt\": \"Two workers request the same output path.\",\n  \"requirements\": [\n    \"Coordinator assigns distinct paths before either writes.\",\n    \"Capture exact input revision, explicit permissions and observed operation evidence.\"\n  ]\n}\n```\n\n## Actual response and output\n\nSeparate Before Serializing Shared State changed the contested output into two distinct planned paths before any worker write. The coordinator rejected the duplicate output path and reserved worker-one/result.md and worker-two/result.md under this case. Only the coordinator would integrate a shared report. The local ownership check also rejects ancestor/descendant overlaps.\n\nThe saved [planned-assignments.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/planned-assignments.json) contains immutable pending plans, exact owned paths and explicit allowed and forbidden operations. outputOwner values are unbound planned roles, not invented worker IDs. Both task inputRevision values are null because read-only Git inspection failed. The package source freeze is a separate user-supplied instruction revision and cannot replace the task's full Git SHA.\n\nThe host exposes collaboration.spawn_agent, collaboration.wait_agent and related worker operations, and the user permits native isolated workers for these evaluations. However, the installed assignment contract requires a full task Git inputRevision before dispatch. Orchestrate also treats an unfillable brief field as a refuse-to-spawn condition. No task checkout, concrete worker payload or full input revision was supplied. I therefore did not launch fake work just to obtain a worker receipt. The observed model, effort and isolation are unknown; inherit-parent would be a requested policy only.\n\nObserved command evidence is in [host-inspection.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/host-inspection.json) and [ownership.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/ownership.receipt.json). The executable check rejected a duplicate path, accepted distinct planned paths and blocked dispatch without the task SHA. No worker wrote either path. No runtime race-prevention claim follows from this sequential coordinator check.\n\nThis two-output conflict is below Orchestrate's standing-program scale, so its Frame small-task collapse applies. No orchestration store, helper install, ledger or frontier was needed or invoked. There are zero worker attempts and no landed units. A program frontier, PR links and verification ledger are not available. None was invented. The local plans and result report are the only durable handoff.\n\nThroughput checkpoint: first reconcile revision and concrete worker acceptance inputs; independent workstreams are the two distinct output paths; shared mutable state belongs only to the coordinator; the smallest safe decomposition is a local ownership check until dispatch prerequisites exist. Worker execution remains blocked on those inputs, not on an observed lack of a native worker tool.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/.\n\n\nCommand: `bun --no-install check.mjs`. Exit 0. Full receipt: [ownership.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/shared-path-conflict/ownership.receipt.json).\n\n```text\nRejected duplicate path. Assigned distinct paths before any worker writes. Dispatch blocked for missing task Git revision. No workers spawned.\n```\n\n\n## Variants and limits\n\nDuplicate-path and distinct-path planning checks ran. Missing-task-revision dispatch check rejected the plans. Native workers are exposed but were not spawned because the assignment contract cannot be satisfied. No fabricated worker or model observations.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-04/shared-path-conflict/additional-source-reads.json",
      "owner": "grades-native-04.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/fixture-README.md",
      "owner": "grades-native-04.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/input.json",
      "owner": "grades-native-04.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/source-manifest.json",
      "owner": "grades-native-04.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/additional-source-reads.json",
      "owner": "grades-native-04.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/fixture-README.md",
      "owner": "grades-native-04.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/input.json",
      "owner": "grades-native-04.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/shared-path-conflict/source-manifest.json",
      "owner": "grades-native-04.json#7",
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
