# codex: fresh-worker-mode

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "fresh-worker-mode",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-08.json#5",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Invoke /poteto-mode for a scoped nontrivial feature. Give a fresh worker this mode and require its chosen playbook, applied principle leaves, throughput checkpoint and evidence. Repeat with worker tools unavailable and with the mode or an applied leaf unavailable. Exercise the 23 playbook route contracts, a no-spawn worker, helper setup failure, a stale full head or missing artifact, and an authorized local checklist when no todo tool exists. Use fixtures for helper boundaries; do not contact a live forge or install dependencies.",
  "caseDefinition": {
    "id": "fresh-worker-mode",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md"
    ],
    "prompt": "Invoke /poteto-mode for a scoped nontrivial feature. Give a fresh worker this mode and require its chosen playbook, applied principle leaves, throughput checkpoint and evidence. Repeat with worker tools unavailable and with the mode or an applied leaf unavailable. Exercise the 23 playbook route contracts, a no-spawn worker, helper setup failure, a stale full head or missing artifact, and an authorized local checklist when no todo tool exists. Use fixtures for helper boundaries; do not contact a live forge or install dependencies.",
    "requirements": [
      "Observed read of the complete mode, chosen playbook and every applied principle leaf",
      "Authorized independent worker spawn and inspected result for full behavior",
      "Immutable scoped assignment, exact input revision, separate write ownership and requested versus observed model records",
      "Four throughput checkpoint items and evidence attached to claims",
      "User authorization and host permissions constrain all operations",
      "Preserve all 23 playbook routes and 24 principle bindings with source-faithful aliases and meanings",
      "No-spawn worker owns its scoped diff and returns it to the lead without nested waiting; required independent review stays explicit",
      "Read real helper contracts before invocation; use exact log positional arguments, explicit outside-package store, watcher heads and finite budgets, and one check-plan positional path",
      "Inspect watcher event kind, terminal and reason; status-only exit 0 and non-terminal queued waiting never prove merged state",
      "Reject stale assignment identities or full input/current head revisions and missing artifacts before integration; ledger labels do not prove verification",
      "Use verbatim chosen-playbook steps in todo tools or an authorized local checklist with a disclosed reduced binding",
      "Local presence closes reference deferrals only; preserve companion, setup, review, external-action and independent-worker limits"
    ],
    "expectedFull": "A fresh worker reads the full mode and applied leaves, follows the selected playbook with verbatim step todos or explicit skips, and returns blocking first steps, independent workstreams, shared mutable state and smallest safe decomposition with reasons for any n/a item. The coordinator inspects artifacts and reports evidence, decisions, limitations and only principles read in this session. The no-spawn delegate returns its own scoped diff for lead review. The coordinator reads selected helper contracts and inspects actual receipts, validates assignment and current full head against existing artifacts, and preserves each playbook delivery exception. All 23 routes and 24 principle bindings remain available as instructions.",
    "expectedReduced": "Without authorized independent workers, the same full reads and checkpoint apply to authorized sequential work. The result explicitly records reduced capability, unverified model diversity and absent independent review or background execution. Missing external companion skills are visible and their dependent gates remain blocked. Local checklist fallback retains verbatim steps and explicit skips. Inert helper fixtures support structural contracts only. An isolated snapshot run supports only its tested revision and never this caller or current host.",
    "expectedBlocked": "If the mode, chosen playbook or applied principle leaf cannot be read, stop dependent work and name the missing reference. Denied execution or writes stay blocked; autonomy language grants no external permission, installation or controller takeover. Missing pinned dependencies stop dependency-backed helpers without install or bootstrap bypass. Stale identities, changed heads, missing artifacts, denied action permission or unknown interrupted outcome block affected integration or replay. Required independent review remains blocked even if a no-spawn worker can prepare a diff.",
    "forbiddenClaims": [
      "A summary substitutes for reading the complete mode or applied leaves",
      "Sequential role switching is independent worker review",
      "Requested models prove actual model identity or diversity",
      "Metadata registers a custom agent, mode or supported host capability",
      "Missing companion skills or pending helpers are silently satisfied",
      "Upstream autonomy authorizes external writes or bypasses permissions",
      "Structural validation proves host behavior",
      "Bundled helper existence or isolated snapshot tests prove this caller executes on either host",
      "Status-only exit 0, ledger labels or queued WAITING prove a merge or an independent verdict",
      "Helper deadlines guarantee a strict wall-clock cutoff without observed host controls",
      "Historical deferral prose excuses skipping a present required contract",
      "The no-spawn worker exception waives required independent lead review",
      "An audit bucket or a parked gate default authorizes deletion, setup or external writes"
    ],
    "caseFile": "docs/parity/cases/skills/poteto-mode.json"
  },
  "registry": {
    "caseId": "fresh-worker-mode",
    "caseFile": "docs/parity/cases/skills/poteto-mode.json",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md"
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
        "inspect-result",
        "isolated-write"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
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
        "execution",
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-08.json#5",
      "order": 0,
      "gradeFile": "grades-native-08.json",
      "rankWithinFile": 5,
      "host": "codex",
      "caseId": "fresh-worker-mode",
      "status": "reduced-pass",
      "grade": {
        "caseId": "fresh-worker-mode",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "execution",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Independent architectural competition and fresh judge required by route",
          "Satisfied dependency-backed helper setup",
          "Complete pre-invocation helper/test-contract reading order",
          "Independent cross-model trail audit and unmet delivery companions"
        ],
        "review": "A real fresh no-spawn delegate read mode/leaves, returned an owned feature diff and receipts, and the root inspected exact assignment/head/digests and independently reran the feature. Missing independent design competition, cross-model review, pre-execution helper test review and real helper setup keep the complete route reduced. Negative views/contract guards are structural simulations only.",
        "responseArtifact": "fixtures/batch-08/fresh-worker-mode.result.md",
        "rawTrace": "codex/batch-08.events.jsonl",
        "actualReadEventIds": [
          "item_4",
          "item_5",
          "item_6",
          "item_7",
          "item_9",
          "item_10",
          "item_12",
          "item_13",
          "item_14",
          "item_16",
          "item_17",
          "item_18",
          "item_19",
          "item_20",
          "item_21",
          "item_22",
          "item_23",
          "item_25",
          "item_28",
          "item_29",
          "item_30",
          "item_31",
          "item_33",
          "item_34",
          "item_35",
          "item_36",
          "item_38",
          "item_39",
          "item_44",
          "item_45",
          "item_46",
          "item_51",
          "item_53",
          "item_54"
        ],
        "nativeMethodReceipts": "native-08-09-tool-receipts.json",
        "variantReview": {
          "assessment": "Read complete retained response, variant dispositions and actual raw parent events. Explicit synthetic negative conditions do not establish host-enforced tool/permission absence; later follow-through supersedes only the named initial limitation.",
          "responseSectionPresent": true
        },
        "limits": [
          "Baseline observations associated with supplied f4623636a287bea2aa79c4b2234a53d20a5f193c; task input revision is distinct. Installed package Git object was unavailable in case runtime; byte snapshots are retained.",
          "Raw CLI command events and persisted native collaboration function calls inspected. Protected dispatch message ciphertext is not treated as readable original prompt evidence.",
          "Actual child models remain unverified unless a child-specific runtime receipt establishes them; parent model metadata cannot establish diversity.",
          "No local fixture, proxy checker or bookkeeping record establishes a live-service action or complete method compliance."
        ],
        "reviewedBy": "review_workflow_evidence independent raw-event and qualitative review",
        "fullExpected": "A fresh worker reads the full mode and applied leaves, follows the selected playbook with verbatim step todos or explicit skips, and returns blocking first steps, independent workstreams, shared mutable state and smallest safe decomposition with reasons for any n/a item. The coordinator inspects artifacts and reports evidence, decisions, limitations and only principles read in this session. The no-spawn delegate returns its own scoped diff for lead review. The coordinator reads selected helper contracts and inspects actual receipts, validates assignment and current full head against existing artifacts, and preserves each playbook delivery exception. All 23 routes and 24 principle bindings remain available as instructions.",
        "reducedExpected": "Without authorized independent workers, the same full reads and checkpoint apply to authorized sequential work. The result explicitly records reduced capability, unverified model diversity and absent independent review or background execution. Missing external companion skills are visible and their dependent gates remain blocked. Local checklist fallback retains verbatim steps and explicit skips. Inert helper fixtures support structural contracts only. An isolated snapshot run supports only its tested revision and never this caller or current host.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# fresh-worker-mode\n\n## Supplied input\n\nThe case contract below is synthetic task input. Its package source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. This case used only the installed package at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. The input repository revision is distinct from that package source freeze.\n\n```json\n{\n  \"id\": \"fresh-worker-mode\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/SKILL.md\"\n  ],\n  \"prompt\": \"Invoke /poteto-mode for a scoped nontrivial feature. Give a fresh worker this mode and require its chosen playbook, applied principle leaves, throughput checkpoint and evidence. Repeat with worker tools unavailable and with the mode or an applied leaf unavailable. Exercise the 23 playbook route contracts, a no-spawn worker, helper setup failure, a stale full head or missing artifact, and an authorized local checklist when no todo tool exists. Use fixtures for helper boundaries; do not contact a live forge or install dependencies.\",\n  \"requirements\": [\n    \"Observed read of the complete mode, chosen playbook and every applied principle leaf\",\n    \"Authorized independent worker spawn and inspected result for full behavior\",\n    \"Immutable scoped assignment, exact input revision, separate write ownership and requested versus observed model records\",\n    \"Four throughput checkpoint items and evidence attached to claims\",\n    \"User authorization and host permissions constrain all operations\",\n    \"Preserve all 23 playbook routes and 24 principle bindings with source-faithful aliases and meanings\",\n    \"No-spawn worker owns its scoped diff and returns it to the lead without nested waiting; required independent review stays explicit\",\n    \"Read real helper contracts before invocation; use exact log positional arguments, explicit outside-package store, watcher heads and finite budgets, and one check-plan positional path\",\n    \"Inspect watcher event kind, terminal and reason; status-only exit 0 and non-terminal queued waiting never prove merged state\",\n    \"Reject stale assignment identities or full input/current head revisions and missing artifacts before integration; ledger labels do not prove verification\",\n    \"Use verbatim chosen-playbook steps in todo tools or an authorized local checklist with a disclosed reduced binding\",\n    \"Local presence closes reference deferrals only; preserve companion, setup, review, external-action and independent-worker limits\"\n  ],\n  \"expectedFull\": \"A fresh worker reads the full mode and applied leaves, follows the selected playbook with verbatim step todos or explicit skips, and returns blocking first steps, independent workstreams, shared mutable state and smallest safe decomposition with reasons for any n/a item. The coordinator inspects artifacts and reports evidence, decisions, limitations and only principles read in this session. The no-spawn delegate returns its own scoped diff for lead review. The coordinator reads selected helper contracts and inspects actual receipts, validates assignment and current full head against existing artifacts, and preserves each playbook delivery exception. All 23 routes and 24 principle bindings remain available as instructions.\",\n  \"expectedReduced\": \"Without authorized independent workers, the same full reads and checkpoint apply to authorized sequential work. The result explicitly records reduced capability, unverified model diversity and absent independent review or background execution. Missing external companion skills are visible and their dependent gates remain blocked. Local checklist fallback retains verbatim steps and explicit skips. Inert helper fixtures support structural contracts only. An isolated snapshot run supports only its tested revision and never this caller or current host.\",\n  \"expectedBlocked\": \"If the mode, chosen playbook or applied principle leaf cannot be read, stop dependent work and name the missing reference. Denied execution or writes stay blocked; autonomy language grants no external permission, installation or controller takeover. Missing pinned dependencies stop dependency-backed helpers without install or bootstrap bypass. Stale identities, changed heads, missing artifacts, denied action permission or unknown interrupted outcome block affected integration or replay. Required independent review remains blocked even if a no-spawn worker can prepare a diff.\",\n  \"forbiddenClaims\": [\n    \"A summary substitutes for reading the complete mode or applied leaves\",\n    \"Sequential role switching is independent worker review\",\n    \"Requested models prove actual model identity or diversity\",\n    \"Metadata registers a custom agent, mode or supported host capability\",\n    \"Missing companion skills or pending helpers are silently satisfied\",\n    \"Upstream autonomy authorizes external writes or bypasses permissions\",\n    \"Structural validation proves host behavior\",\n    \"Bundled helper existence or isolated snapshot tests prove this caller executes on either host\",\n    \"Status-only exit 0, ledger labels or queued WAITING prove a merge or an independent verdict\",\n    \"Helper deadlines guarantee a strict wall-clock cutoff without observed host controls\",\n    \"Historical deferral prose excuses skipping a present required contract\",\n    \"The no-spawn worker exception waives required independent lead review\",\n    \"An audit bucket or a parked gate default authorizes deletion, setup or external writes\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/poteto-mode.json\"\n}\n```\n\n## Actual output\n\nThe no-spawn delegate added `summarizeOrders(orders)` to the copied synthetic dashboard module. Dashboard consumers receive per-status counts and totals in first-seen order. The next maintainer inherits one Map-based owner of aggregation and a direct rerunnable verification script.\n\nThe function works against the copied fixture in the observed local run. This is not a full mode acceptance claim. Architect competition and independent review remain open. No PR, commit, push, install, schedule, settings change or service action occurred.\n\nThe local design compared a Map accumulator with unique-status collection followed by repeated filtering. The Map shape became the base because it owns count and total together. These are sequential sketches. They are not independent candidates, a fresh cross-judge or verified model diversity.\n\n```text\n{\"summaries\":[{\"status\":\"open\",\"count\":2,\"total\":12.5},{\"status\":\"closed\",\"count\":1,\"total\":4}],\"inputUnchanged\":true,\"existingExportsUnchanged\":true,\"baselineFeatureAbsent\":true,\"checks\":8}\n```\n\nRun `bun --no-install /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/verify-feature.mjs` to repeat the actual feature check. The eight checks cover literal summary results, filtered input, empty input, reserved-looking status keys, non-mutation, unchanged filter behavior, unchanged exporter behavior and absence of the feature from the copied baseline. The exporter has a pre-existing CSV quoting defect outside this scoped feature. It remains unchanged.\n\n## Identity and source evidence\n\nThe immutable assignment is `fresh-worker-mode/assignment.json`, id `fresh`, owner `fresh`. The native worker identity is `/root/fresh`. The lead dispatched this fresh delegate. This delegate invoked zero spawns and zero nested waits.\n\nThe observed full input and current HEAD are both `352ef9629c424778feb077712c2e7b62bb46e5ce`. Commands and outputs are preserved in `commands/input-commit.json`, `commands/current-head.json` and `commands/input-tree-corrected.json`. The first relative input-tree query returned empty because it ran from the case subdirectory. The corrected repository-root query lists the committed inputs. That observation-method correction is retained instead of calling the inputs missing.\n\n`worker-receipt.json` records exact artifacts and SHA-256 digests. Its completed-local label does not prove independent review or integration. The lead must inspect the actual diff and verification before accepting it. Output artifacts are uncommitted and are not claimed to belong to the input revision.\n\nRequested model and effort are inherit-parent. Actual model and effort are unknown because the worker operation supplied no observed runtime model identity. Diversity remains unverified.\n\n`source-reads/manifest.json` records 73 actual file reads and byte-identical local snapshots. It includes the complete mode, all 23 route playbooks, all 24 principle leaves, role prompt, host/ownership/model/assignment contracts, how, architect, arena, unslop and selected helper sources. The source freeze is the supplied package identifier. These reads alone do not establish package loading, host behavior or a behavioral pass.\n\n## Throughput checkpoint\n\n- Blocking first steps. The full mode, Feature, how, architect, arena and applicable leaves were read before feature edits. Assignment and current revision were checked with git before helper probes and returned with the result. The lead verified the input revision before dispatch.\n- Independent workstreams. n/a because this is one code-coupled feature assigned to a no-spawn delegate. Required independent design and review stay open for the lead.\n- Shared mutable state. This delegate exclusively writes this case directory and its root result file. Shared inputs and the installed package remain read-only.\n- Smallest safe decomposition. One owner reads and designs, adds one pure grouped-summary function, verifies it, and returns the diff. Extra code writers would share one small module without reducing the dependency chain.\n\nThe checkpoint is retained in `checklist.md`. The final boundary keeps the same one-owner decomposition and hands independent review to the lead.\n\n## Playbook and principle bindings\n\n`checklist.md` starts with all eight Feature steps and sub-items copied verbatim. Its later dispositions retain explicit skips. No todo operation is exposed, so the authorized local Markdown checklist is a reduced tool binding. Architect and Arena phase dispositions are also retained.\n\n`bindings.json` preserves all 23 exact playbook paths and all 24 principle names, aliases and meanings extracted from the complete mode. `route-report.json` records each route's steps, delivery exception and permission boundary. The 23 route exercises are source-contract inspection, not 23 executed feature, cleanup, shipping, profiling or autonomous workflows. Such operations need their concrete prerequisites and authorization. Local presence closes the historical reference-deferral question only.\n\nApplied leaves read in full this session and their decisions are listed below.\n\n- Model the Domain selected a Map keyed by status before writing logic.\n- Build the Lever produced `verify-feature.mjs` and the rerunnable contract guard script.\n- Prove It Works required importing and calling the real modified module, then reading actual command output.\n- Test Behavior, Not Implementation required literal expected arrays and preserved caller-visible behavior.\n- Separate Before Serializing Shared State retained distinct case ownership with no shared package or fixture mutation.\n- Sequence Work into Verifiable Units kept the local addition and its check together. Commits and rebase were explicitly skipped because authorization forbids them.\n- Exhaust the Design Space produced the two whole-shape sequential sketches. The mandatory independent design method remains unsatisfied.\n\nOther captured leaves remain available as source instructions. Capturing them does not mean every principle was applied. Unslop governed the reports. Technical-writing was read for this document. The external create-skill companion is unavailable within the permitted package-only workflow. Its authoring fallback contract was read; no personal skill was authored. External deslop is absent and no replacement review was authorized. No no-comments independent reviewer ran. Those delivery gates remain open.\n\n## Variants and actual tools\n\n| Variant | Actual action or response | Evidence and limit |\n| --- | --- | --- |\n| Fresh native delegate | Lead spawned this worker with full mode instructions and exact immutable assignment. The delegate read the full mode and owns its local diff. | This report and worker-receipt.json are the returned result. Parent spawn receipt and lead result inspection are outside this delegate's write scope. |\n| No-spawn worker | The delegate implemented directly and returned its own diff. | feature.diff, design.md and commands/feature.json. No nested waiting. Lead independent review still required. |\n| Worker tools unavailable | Sequential how and design fallback response recorded. | contract-probes.json. Simulated negative condition. Collaboration tools remain exposed; this assignment forbids nested spawning. |\n| Mode unavailable | Read of the exact omitted local-view path failed ENOENT. Dependent work in this variant stops. | contract-probes.json. The installed mode remains readable. This is not host-enforced file denial. |\n| Applied leaf unavailable | Read of the omitted local-view model-the-domain path failed ENOENT. Dependent code work in this variant stops. | contract-probes.json. The installed leaf remains readable. This is a simulated absence. |\n| Helper setup failure | Real installed bootstrap, orch and watcher entry points fail with missing pinned Commander metadata. | commands/bootstrap.json, commands/orchestrate-setup.json, commands/watcher-setup.json. No install or bypass. |\n| Stale assignment identity | Local guard rejects an altered identity. | contract-probes.json. Synthetic altered result, not a stale native receipt. |\n| Stale input or current head | Local guard rejects changed full input SHA, changed full current SHA and a short SHA. | contract-probes.json. Actual current HEAD remains unchanged. |\n| Missing artifact | Local guard rejects an absent artifact even with valid labels. | contract-probes.json. No integration performed. |\n| Ledger label only | Local guard rejects a label without required method evidence. | contract-probes.json. A ledger row is not a verifier. |\n| No todo tool | Actual authorized local checklist created and read back. | checklist.md. Reduced tool binding preserves verbatim steps. |\n| Status-only exit 0 | Inert STATUS event remains a query observation, never readiness or merge proof. | watcher-fixtures.ndjson and contract-probes.json. Generated fixture only. |\n| Queued WAITING | Inert nonterminal WAITING with merge-queue reason can end Babysit's ready report, while Shipping still needs actual merged state. | Same fixtures. No live watcher receipt or service contact. |\n\nThe actual exposed file/execution binding is `functions.exec` calling `tools.exec_command`. Bun scripts read source files, wrote owned files, spawned bounded local commands and saved stdout, stderr and exit codes. Persistence was verified by reading saved receipts and logs. Collaboration was used only to send scoped progress to the lead. No exposed tool grants external authorization.\n\n## Helper commands and results\n\nThe log helper was called with exactly six positional arguments, starting with an explicit owned logfile. `decisions.tsv` was read back. The newline probe exits 1 and creates no logfile. The formula probe prefixes the formula-leading decision with a quote. Commands and readback are retained under `commands/`, `formula-probe.tsv` and `readback.json`.\n\nThe orch probe uses an explicit outside-package store at `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/owned-store` and `inbox drain --peek --json`. Bootstrap fails before inbox processing, so no peek receipt, durable drain receipt or initialized store is claimed. A later actual drain and ledger check are blocked by setup. The full real orch helper and store sources were read and preserved. The helper test source was inspected after the setup attempt, so this run does not claim a completed pre-execution test-contract review gate.\n\nThe watcher probe uses explicit synthetic owner/repo, queued PR list, a full 40-character expected head and finite budgets of one poll and one second. Real bootstrap fails before importing the CLI or contacting the forge. The tested input head is an inert fixture pin, not a remote head observation. The dependency gate stops further watcher execution. It does not prove a strict wall-clock deadline.\n\nThe plan checker was called with one positional path each time. An unreadable path exits 2. The Feature checklist exits 1 with `not a pstack multi-phase plan; leave other workflow plans unchanged`. That checker correctly does not certify this implementation checklist. No structural success is represented as runtime verification.\n\nAll command arrays, stdout, stderr and exit codes are preserved in `commands/all.json`. The diff command exits 1 because the two files differ. That exit code is expected and is not a test failure.\n\n## Limits and open gates\n\nNo native nested design workers or fresh judge ran under the no-spawn assignment. Parent inspection is required for independent review. No requested model was treated as observed. No private or unrelated history was read. The scoped conversation is visible, but a complete exported native transcript is unavailable to this delegate. The source snapshots and local command records preserve actual file content and process output; they are not a fabricated full native transcript.\n\nAll complete route documents are locally present. That resolves reference availability only. It does not satisfy companion execution, dependency setup, external authorization, independent design review, real-surface controls, model diversity, persistent wake or a clean shipping verdict.\n\nNo full host behavior claim or self-assigned grade is made. The local feature has direct observed evidence. The reduced design method and blocked delivery gates remain explicit.\n\n## Attention\n\nreviewed by unknown\n\nIndependent cross-model trail review is blocked for this no-spawn delegate. The lead must inspect the diff, script and actual output. The complete native transcript export is unavailable. Helper setup is a real block. Negative capability views and watcher events are simulated. The existing CSV quoting defect remains outside this scoped feature.\n\n## Coordinator inspection after worker return\n\nThe root independently inspected feature.diff, the complete verification script, source code, command records, contract probes and returned result. It reran `bun --no-install fresh-worker-mode/verify-feature.mjs`, which exited 0. [lead-verification.command.json](fresh-worker-mode/lead-verification.command.json) preserves that output. [lead-review.json](fresh-worker-mode/lead-review.json) validates assignment fresh against /root/fresh, both full input/current SHA values and all 10 returned artifact digests. This supplies independent lead review of the actual local diff. Independent design competition and cross-model review remain open.\n\nThe synthetic contract guard checks a method string and file presence. The string alone cannot establish execution. The root inspected actual command output and independently reran the feature instead of trusting that label. Those guard probes remain structural demonstrations, not native stale-worker or host-acceptance receipts.\n",
        "artifact": {
          "path": "fixtures/batch-08/fresh-worker-mode.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode.result.md",
          "sha256": "0b068e90766a48986d98d78949586a39df72837c26b18131a38df71d18538fc4",
          "bytes": 19337
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-08.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-08.events.jsonl",
            "sha256": "c9523c716c41c55326eaa7e1e3d43819d20e671fd9312c86afe2300f6637cd57",
            "bytes": 632803,
            "eventReferences": [
              {
                "eventId": "item_4",
                "line": 7,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1ca10798fb625871010c78561d9b219b70bd2928acb3ad486fc9233765b51005"
              },
              {
                "eventId": "item_4",
                "line": 8,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "65be63e58caa49287c0a61ed364bc7b2f7c7d852cf9193026fd042da36affdba",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2ed46a74369630994c084941c16d59730138d8057d82402b3acec3f4b256622c"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a47a7c1d48f94497c7f583d8bf9aa5d0734b79cfc67bb30b2aaabbdf931dbe19",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d931ac5de83b01d5001caa72a076d687088a5cd9e7c8706d4d957d7bf7e5c6fb"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "32bf0139e83a388459054da8064ae19a34e9bbb57378acc8e69627c9002bf6d2",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "719b2301bf84c438634a64049a9bf27a45080f3bfaf46cda9430979b97fe140e"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a972c679e7d7f2e1bb242a482afd3d1b7a64c9d8e4190eed95e82dd766ed0ead",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 16,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f4a9e2abba104309466d20d02eed171c8caf815d6770048196bd2644a4b271c7"
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "78c192776e9139b282d079bbd12a36bcabf71ca0c074e0cf48abc82e3839e4b7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "dd1b521ef8113762d3eb591459ad84eb351f6b43022ffd2b8be14fd630888b24"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "18593ae8dc002829bcfae72d7cace2125cce4d78a48a53af425ceb9272b923cb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2f81df77b1f4167472e418d6eab473ca7bc4eed2f733132eedb7af154691c6a0"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "3049523079572dbc52a637650dad45956f21d7bdcb6cf263052dfb58e05b125d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "193a1ff20d1011c5a6036061fe52f3b26f9fa50ad0b1d11c95f2f6e9215a4c49"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1e495fa2f6c86621c081c8771fdafa1bb9e102845651ca2061cbfa7da29fc04c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c487e11ee9104e4e76e67ac524f3ae4fd858bff4df4658757cce67438b5bcfe4"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5a5d91b72a1fafd3a14935895f7eafc5da5c468e8f9d199bb6ccd39fb2f8afcc",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 29,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "12e8107db057f11c1524e860c369367e69d75f7ad6ab5bda38365e5efc95b4c4"
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "fe1fc6fff33cacc237cc9be484cd35859ead22c383ccedc8fd675d84023ce280",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_17",
                "line": 31,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "efaf4d76cada6333354568bd95a4ad01ea1e2ce7df4579e71c349f15104947df"
              },
              {
                "eventId": "item_17",
                "line": 32,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c0c215f670cac115d8a57d44be48b5a87024c51b4983456ddc0951208f20e153",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "56442dda60fa6454e5e2520b72e36cf3c48f6ba7a8a4b837409f87099ed71930"
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "065f5498dc0d73ba1735f465e7d65e6c83d52eef4eda1c7aadee15248a9ea617",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_19",
                "line": 35,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "bda2db2ee8d57809c8740e6f3af20c54b12a12f0fe5ff5a8507762e8d5e3cfda"
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b8f7c5038c7bf76f2476a9e8855db44a14aaaa1b6e89899d5caa91d06defc9cb",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9cd47439129e7ee1cd1d2aaa03235a20b88a960a9075e8f3e098491ab19140db"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "12f8cd306d13b81a9435ec15bdc458b3ca8785a1c3fd21548c3b38ac7522d86b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_21",
                "line": 39,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a4ecb3ace8efabd11244b4eab30fa7363490760ed83afed5d471c07e9fa7c8d6"
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b16074c0dda41ae6d9f6cc11c61500e7eb8f82ddd176d3914d7c05d18274261e",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3abf767210c54231572020ad09b96a5cf630bde00c5f7041f41b70c4c74f91c6"
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1e2538b79029bfad87beb91e8ed5652e4d739976d71605fb00be5c0e1cff9f4b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 43,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4c9d8b64e71a947d8e6d88e68123b7bfd628e2f8c08f2544e7c6dc5fd5d21aaa"
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6bcfc68bc59053c4dab8929eac141153e93f360467c4b1da2a1a0e3f4e3307ec",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_25",
                "line": 46,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "751f576dcf6871ba6729a29db5f24f329ae114a8bfe0db2cb3ac04676a7fe63d"
              },
              {
                "eventId": "item_25",
                "line": 47,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f43626b0bc1a4206d861c7ac3f7be6d3dea143059e23d049cbdcbf63dd59e427",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_28",
                "line": 52,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "96599afc81bf1258d402cde5a40334e14fad6ba9431e01c72d9f8dce8095e1ec"
              },
              {
                "eventId": "item_28",
                "line": 53,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "9338c72325b1d2b3eada90912ee7aa9ab0d0b957770bf843c9efa50dda3ff4c5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_29",
                "line": 54,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1f093200628800fe1d3bcfd303ae7a3053159da23f60e2f7ce24e92a6f0d1a2c"
              },
              {
                "eventId": "item_29",
                "line": 55,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8bd09acf38601d82cc0bf565522ebe8e0bde61ec37d0678b5c69d88bd925c0b9",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_30",
                "line": 56,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c92e2778f2c3b1273fb44e87ff62e8321a65419fb8082e98eb681436f8eb8838"
              },
              {
                "eventId": "item_30",
                "line": 57,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a1b70abb94fb7f36d9d6debd5f9672bbcfbb66bc38b646e0a346ef524d273114",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_31",
                "line": 58,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d9a376e21ad81908d32164935579141df5b4b3d76e0d790025bccd834216d7af"
              },
              {
                "eventId": "item_31",
                "line": 59,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "44fdf2e9f344c7576aad02ed4db5203fb619338fc123ab8f0f1e92c969609f42",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_33",
                "line": 61,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cb04fbd0ed575f4238f3fdbf9f97c68f8bc940f18ed5932c7423e2e5766cec8f"
              },
              {
                "eventId": "item_33",
                "line": 62,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "00e3624fc70032c30b852bb86f03dad0ffe3dc3b1235d7612815ec2646a46258",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_34",
                "line": 63,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "164df6bf3cece90dc65a89c077227582cef6626a2c0867148200da5cf3e19e9a"
              },
              {
                "eventId": "item_34",
                "line": 64,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2c5e570950d138f2c525a241e89cbbd4acf3b1919b43b39fd7b5f60e5d270dcd",
                "commandResult": {
                  "exitCode": 1
                }
              },
              {
                "eventId": "item_35",
                "line": 65,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e4f24df39dfd90a5da25234f8d9219ebceb8b5a9fbf86a3a9120f1d7205ce7e2"
              },
              {
                "eventId": "item_35",
                "line": 66,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6f3837a2add5c2b2546db4d49a2b888944e27746c13b3298dc8226ce0b8b80e9",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_36",
                "line": 67,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8e9ef1c139761dcdcfefbff62979f0a3e973e9f3780753a9009c4717e756fa30"
              },
              {
                "eventId": "item_36",
                "line": 68,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "892bd24da6b646b9e78c7c4d5fcc62feff5cf1b3cd4d27e607dc81b1fd0b0dec",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_38",
                "line": 71,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "011ffe0f1133ad6ab400b02acaa58bd9f895f4bc7393399c691498a7db79527e"
              },
              {
                "eventId": "item_38",
                "line": 72,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "108c9ba838ac2f9cf0477659e242952c861eed470a6641b2bc092a022e154254",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_39",
                "line": 73,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f8002457c9f0dc50fc7e3500ca7a912a4d8724123358da53c8345ebcc96a2d2e"
              },
              {
                "eventId": "item_39",
                "line": 74,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8814e2ba8877072086a1731883065e89c9b0c2dfc9847e0a3ad56141d3de29cd",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_44",
                "line": 82,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "71ce7bee139baaaa558c6bfd2180098b9bf528562590c474e0b656b007809df4"
              },
              {
                "eventId": "item_44",
                "line": 83,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e0249b79fec363ac4470c16cf00c19c988358c9edda04af3a0a34ce93e04b5d7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_45",
                "line": 84,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a0c0defd6cb95904a90d68e50342049a27607ff687445ffaf45b292079dd890a"
              },
              {
                "eventId": "item_45",
                "line": 85,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "05e755e2cdbb83068d7ea636dc15a5e9c7d780884c01e707db7bce425062e5b6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_46",
                "line": 86,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ffafb3f98ea40f0f8edfaad43c46f926c18df4bc453d2ec5dbbd27debfc03e75"
              },
              {
                "eventId": "item_46",
                "line": 87,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c35c3106e73cff8f73fa065f65527cda30bf312e73d6ccd5830f78e3134c990f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_51",
                "line": 95,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6c6c1fb1bd728cef6d2d9ef626a7730a2210d1ccf1f4626a9fb5fd53cfbf22d7"
              },
              {
                "eventId": "item_51",
                "line": 96,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "3bfcc06cec50458fd50f3c41f62993b77a971027e606b209d3da36531a32f138",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_53",
                "line": 98,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "27cbbe943887759694c058eae6e1c328e6e0e7abaeab76d8727684549242691c"
              },
              {
                "eventId": "item_53",
                "line": 99,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "783d668bf8393323cc1f1ca385b5c38efd46b86d36b554951addd6620cdf7530",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_54",
                "line": 100,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c609dd1284218f06988ba9cd61871aa055a0ae83d539938f139351c5984dd5de"
              },
              {
                "eventId": "item_54",
                "line": 101,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "05091bfec53f551cadff09ad76ab0bfe838d862707866a2389304c42ccb2ec8e",
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
            "item_4",
            "item_5",
            "item_6",
            "item_7",
            "item_9",
            "item_10",
            "item_12",
            "item_13",
            "item_14",
            "item_16",
            "item_17",
            "item_18",
            "item_19",
            "item_20",
            "item_21",
            "item_22",
            "item_23",
            "item_25",
            "item_28",
            "item_29",
            "item_30",
            "item_31",
            "item_33",
            "item_34",
            "item_35",
            "item_36",
            "item_38",
            "item_39",
            "item_44",
            "item_45",
            "item_46",
            "item_51",
            "item_53",
            "item_54"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-08/fresh-worker-mode/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/assignment.json",
      "sha256": "8805f3b88e5833634a07eec1f3bc6c1acc3ae97bb9ce681326c39d0217cca09d",
      "bytes": 381,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"id\": \"fresh\",\n  \"scope\": \"fresh-worker-mode\",\n  \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n  \"outputOwner\": \"fresh\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"role\": \"case owner\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"input.json\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/bindings.json",
      "sha256": "7926901be982a0b74e04a071ea95a83e63032dc9d9ff0de8de4590eb75c75d12",
      "bytes": 11819,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"routes\": [\n    {\n      \"path\": \"skills/poteto-mode/playbooks/prototype.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__prototype.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/babysit.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__babysit.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/shipping.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__shipping.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/investigation.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__investigation.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/bug-fix.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__bug-fix.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/perf-issue.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__perf-issue.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/hillclimb.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__hillclimb.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/runtime-forensics.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__runtime-forensics.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/trace-forensics.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__trace-forensics.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/feature.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__feature.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/refactoring.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__refactoring.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/visual-parity.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__visual-parity.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/authoring-a-skill.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__authoring-a-skill.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/eval.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__eval.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/autonomous-run.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__autonomous-run.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__orchestrate.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/autopilot-full.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__autopilot-full.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/autopilot-stack.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__autopilot-stack.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/session-pickup.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__session-pickup.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/pause-safely.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__pause-safely.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/multi-phase-plan.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__multi-phase-plan.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/worktree-cleanup.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__worktree-cleanup.md\"\n    },\n    {\n      \"path\": \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"stepsArtifact\": \"source-reads/skills__poteto-mode__playbooks__opening-a-pr.md\"\n    }\n  ],\n  \"principles\": [\n    {\n      \"name\": \"Laziness Protocol\",\n      \"alias\": \"principle-laziness-protocol\",\n      \"meaning\": \"Refactoring, sizing a diff, or tempted to add abstractions, layers, or signal threading. Bias to deletion and the smallest change that solves the problem.\",\n      \"path\": \"skills/principle-laziness-protocol/SKILL.md\"\n    },\n    {\n      \"name\": \"Foundational Thinking\",\n      \"alias\": \"principle-foundational-thinking\",\n      \"meaning\": \"Before writing logic: core types and data structures, scaffold-vs-feature sequencing, what concurrent actors share.\",\n      \"path\": \"skills/principle-foundational-thinking/SKILL.md\"\n    },\n    {\n      \"name\": \"Redesign from First Principles\",\n      \"alias\": \"principle-redesign-from-first-principles\",\n      \"meaning\": \"Integrating a new requirement into an existing design. Redesign as if it had been foundational from day one.\",\n      \"path\": \"skills/principle-redesign-from-first-principles/SKILL.md\"\n    },\n    {\n      \"name\": \"Attack the Premise\",\n      \"alias\": \"principle-attack-the-premise\",\n      \"meaning\": \"Two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it.\",\n      \"path\": \"skills/principle-attack-the-premise/SKILL.md\"\n    },\n    {\n      \"name\": \"Subtract Before You Add\",\n      \"alias\": \"principle-subtract-before-you-add\",\n      \"meaning\": \"Sequencing an addition, refactor, or rewrite. Remove dead weight first, then build on the simpler base.\",\n      \"path\": \"skills/principle-subtract-before-you-add/SKILL.md\"\n    },\n    {\n      \"name\": \"Minimize Reader Load\",\n      \"alias\": \"principle-minimize-reader-load\",\n      \"meaning\": \"Reviewing or shaping code that's hard to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.\",\n      \"path\": \"skills/principle-minimize-reader-load/SKILL.md\"\n    },\n    {\n      \"name\": \"Outcome-Oriented Execution\",\n      \"alias\": \"principle-outcome-oriented-execution\",\n      \"meaning\": \"Planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture, don't preserve throwaway compatibility states.\",\n      \"path\": \"skills/principle-outcome-oriented-execution/SKILL.md\"\n    },\n    {\n      \"name\": \"Experience First\",\n      \"alias\": \"principle-experience-first\",\n      \"meaning\": \"Product, UX, or feature-scope tradeoffs. Choose user delight over implementation convenience.\",\n      \"path\": \"skills/principle-experience-first/SKILL.md\"\n    },\n    {\n      \"name\": \"Exhaust the Design Space\",\n      \"alias\": \"principle-exhaust-the-design-space\",\n      \"meaning\": \"A novel interaction or architectural decision with no precedent. Build 2-3 competing prototypes and compare before committing.\",\n      \"path\": \"skills/principle-exhaust-the-design-space/SKILL.md\"\n    },\n    {\n      \"name\": \"Build the Lever\",\n      \"alias\": \"principle-build-the-lever\",\n      \"meaning\": \"Any non-trivial work. Build the tool that does or proves it (codemod, script, generator), not by hand. The tool is the artifact a reviewer reruns.\",\n      \"path\": \"skills/principle-build-the-lever/SKILL.md\"\n    },\n    {\n      \"name\": \"Model the Domain\",\n      \"alias\": \"principle-model-the-domain\",\n      \"meaning\": \"Writing stateful logic, or code that branches a lot or repeats a shape assumption across files. Encode the domain in a structure (state machine, typed model, table or registry, reducer, boundary, the right collection) instead of scattered conditionals.\",\n      \"path\": \"skills/principle-model-the-domain/SKILL.md\"\n    },\n    {\n      \"name\": \"Boundary Discipline\",\n      \"alias\": \"principle-boundary-discipline\",\n      \"meaning\": \"Wiring validation, error handling, or framework adapters. Guards at system boundaries, trust internal types, keep business logic pure.\",\n      \"path\": \"skills/principle-boundary-discipline/SKILL.md\"\n    },\n    {\n      \"name\": \"Type System Discipline\",\n      \"alias\": \"principle-type-system-discipline\",\n      \"meaning\": \"Designing types or a signature in any typed language. Make illegal states unrepresentable, brand primitives, parse external data at boundaries.\",\n      \"path\": \"skills/principle-type-system-discipline/SKILL.md\"\n    },\n    {\n      \"name\": \"Make Operations Idempotent\",\n      \"alias\": \"principle-make-operations-idempotent\",\n      \"meaning\": \"Designing commands, lifecycle steps, or loops that run amid crashes and retries. Converge to the same end state.\",\n      \"path\": \"skills/principle-make-operations-idempotent/SKILL.md\"\n    },\n    {\n      \"name\": \"Migrate Callers Then Delete Legacy APIs\",\n      \"alias\": \"principle-migrate-callers-then-delete-legacy-apis\",\n      \"meaning\": \"Introducing a new internal API while old callers exist. Migrate and delete in one wave.\",\n      \"path\": \"skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\"\n    },\n    {\n      \"name\": \"Separate Before Serializing Shared State\",\n      \"alias\": \"principle-separate-before-serializing-shared-state\",\n      \"meaning\": \"Concurrent actors might write the same file, branch, key, or object. Eliminate the sharing first.\",\n      \"path\": \"skills/principle-separate-before-serializing-shared-state/SKILL.md\"\n    },\n    {\n      \"name\": \"Prove It Works\",\n      \"alias\": \"principle-prove-it-works\",\n      \"meaning\": \"After a task, before declaring done. Verify against the real artifact, not a proxy or \\\"it compiles\\\".\",\n      \"path\": \"skills/principle-prove-it-works/SKILL.md\"\n    },\n    {\n      \"name\": \"Fix Root Causes\",\n      \"alias\": \"principle-fix-root-causes\",\n      \"meaning\": \"Debugging. Trace each symptom to its root cause, reproduce first, ask why until you reach it.\",\n      \"path\": \"skills/principle-fix-root-causes/SKILL.md\"\n    },\n    {\n      \"name\": \"Sequence Work into Verifiable Units\",\n      \"alias\": \"principle-sequence-verifiable-units\",\n      \"meaning\": \"Multi-step work (sweeps, migrations, runs of similar edits) and how you stack commits and PRs. Break work into small units that each end in a check, verify each before the next, and order delivery so the sequence proves itself.\",\n      \"path\": \"skills/principle-sequence-verifiable-units/SKILL.md\"\n    },\n    {\n      \"name\": \"Test Behavior, Not Implementation\",\n      \"alias\": \"principle-test-behavior-not-implementation\",\n      \"meaning\": \"Writing, changing, or keeping a test. Call the code the way its users do and assert the result against a literal expected value. If the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test.\",\n      \"path\": \"skills/principle-test-behavior-not-implementation/SKILL.md\"\n    },\n    {\n      \"name\": \"Explain the Number\",\n      \"alias\": \"principle-explain-the-number\",\n      \"meaning\": \"Before you trust, report, or act on a number you measured (a speedup, a regression, a throughput, a latency, or an eval result). Find what limits it, and rule out that it measured something other than the work you think.\",\n      \"path\": \"skills/principle-explain-the-number/SKILL.md\"\n    },\n    {\n      \"name\": \"Guard the Context Window\",\n      \"alias\": \"principle-guard-the-context-window\",\n      \"meaning\": \"Context fills up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents, keep summaries in the main thread.\",\n      \"path\": \"skills/principle-guard-the-context-window/SKILL.md\"\n    },\n    {\n      \"name\": \"Never Block on the Human\",\n      \"alias\": \"principle-never-block-on-the-human\",\n      \"meaning\": \"Tempted to ask \\\"should I do X?\\\" on reversible work. Proceed, present the result, let the human course-correct.\",\n      \"path\": \"skills/principle-never-block-on-the-human/SKILL.md\"\n    },\n    {\n      \"name\": \"Encode Lessons in Structure\",\n      \"alias\": \"principle-encode-lessons-in-structure\",\n      \"meaning\": \"You catch yourself writing the same instruction a second time. Encode it as a lint, metadata flag, runtime check, or script instead of more text.\",\n      \"path\": \"skills/principle-encode-lessons-in-structure/SKILL.md\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/capture.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/capture.mjs",
      "sha256": "9d53ce04ee0fb4e38f08535346fdd78706090fc98392da078cabc1dd1890d48d",
      "bytes": 3931,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "import {mkdir,readFile,writeFile,copyFile} from 'node:fs/promises';\nimport {createHash} from 'node:crypto';\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst root=import.meta.dir;\nawait mkdir(`${root}/source-reads`,{recursive:true});\nconst mode=await readFile(`${pkg}/skills/poteto-mode/SKILL.md`,'utf8');\nconst routePaths=[...mode.matchAll(/`playbooks\\/([^`]+\\.md)`/g)].map(x=>`skills/poteto-mode/playbooks/${x[1]}`);\nconst routes=[...new Set(routePaths)];\nconst principles=[...mode.matchAll(/\\*\\*([A-Z][^*]+)\\*\\* \\(\\*\\*(principle-[^*]+)\\*\\*\\)\\. ([^\\n]+)/g)].map(x=>({name:x[1],alias:x[2],meaning:x[3],path:`skills/${x[2]}/SKILL.md`}));\nconst extras=['skills/poteto-mode/SKILL.md','references/workflow-ownership.md','references/host-capabilities.md','references/orchestration-contract.md','references/model-roles.md','references/agent-prompts/poteto-agent.md','skills/how/SKILL.md','skills/how/references/explainer-prompt.md','skills/architect/SKILL.md','skills/architect/references/runner-prompt.md','skills/architect/references/rationale-template.md','skills/architect/references/design-red-flags.md','skills/arena/SKILL.md','skills/unslop/SKILL.md','skills/show-me-your-work/SKILL.md','skills/show-me-your-work/scripts/log.sh','skills/show-me-your-work/references/decision-log-template.tsv','skills/poteto-mode/scripts/bootstrap.ts','skills/poteto-mode/scripts/package.json','skills/poteto-mode/scripts/bun.lock','docs/testing/helper-setup.md','skills/poteto-mode/scripts/check-plan.mjs','skills/poteto-mode/scripts/orch/orch.ts','skills/poteto-mode/scripts/orch/store.ts','skills/poteto-mode/scripts/watch-pr/watch-pr','skills/poteto-mode/references/bugbot-triage.md'];\nconst manifest=[];\nfor(const path of [...new Set([...extras,...routes,...principles.map(x=>x.path)])]){const bytes=await readFile(`${pkg}/${path}`);const out=path.replaceAll('/','__');await writeFile(`${root}/source-reads/${out}`,bytes);manifest.push({source:`${pkg}/${path}`,artifact:`source-reads/${out}`,sha256:createHash('sha256').update(bytes).digest('hex'),bytes:bytes.length});}\nawait writeFile(`${root}/source-reads/manifest.json`,JSON.stringify(manifest,null,2));\nawait writeFile(`${root}/bindings.json`,JSON.stringify({routes:routes.map(path=>({path,stepsArtifact:`source-reads/${path.replaceAll('/','__')}`})),principles},null,2));\nawait mkdir(`${root}/feature`,{recursive:true});\nfor(const file of ['dashboard.mjs','orders.json']) await copyFile(`/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/${file}`,`${root}/feature/${file}`);\nawait copyFile(`${root}/feature/dashboard.mjs`,`${root}/feature/dashboard.before.mjs`);\nconst feature=await readFile(`${pkg}/skills/poteto-mode/playbooks/feature.md`,'utf8');\nconst steps=feature.split('\\n').filter(l=>/^\\d+\\. |^   - /.test(l));\nawait writeFile(`${root}/checklist.md`,'# Feature checklist\\n\\nNo todo tool is exposed. This authorized local Markdown checklist is the reduced binding. The steps below are verbatim. Status and task notes follow separately.\\n\\n'+steps.join('\\n')+'\\n\\n## Throughput checkpoint\\n\\n- Blocking first steps. Read the full mode, Feature, how, architect, arena and applied leaves. Confirm assignment revision and local permissions before editing.\\n- Independent workstreams. n/a because this is one code-coupled feature assigned to a no-spawn delegate. Required independent design and review stay open for the lead.\\n- Shared mutable state. Only this delegate writes feature/ and this case output. Source inputs and package files stay read-only.\\n- Smallest safe decomposition. One owner reads and designs, adds one grouped summary function, verifies it, and returns the scoped diff to the lead.\\n');\nconsole.log(JSON.stringify({sourceFilesRead:manifest.length,routes:routes.length,principles:principles.length,checklist:'checklist.md',copies:['feature/dashboard.mjs','feature/orders.json']}));\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/checklist.md",
      "sha256": "da04940a3d32d9e98cc4de225c3d8aaad5823d8ec77b599112223a9ce66170e7",
      "bytes": 7416,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "# Feature checklist\n\nNo todo tool is exposed. This authorized local Markdown checklist is the reduced binding. The steps below are verbatim. Status and task notes follow separately.\n\n1. Run [how](../../how/SKILL.md) over the affected subsystem. Ground the intended user outcome in traced source and caller behavior.\n2. Run [architect](../../architect/SKILL.md) for parallel design exploration. Follow its complete design and arena contracts. Preserve sequential alternatives only as reduced capability when independent workers are unavailable. Required independence remains blocked.\n3. Write the throughput checkpoint as four todo items. Keep any dimension that does not apply, such as a single file or no fan-out, with `n/a: <reason>` rather than dropping it.\n   - Blocking first steps. Gates run before fan-out.\n   - Independent workstreams. Disjoint files, services, or layers parallelize. Shared writes serialize.\n   - Shared mutable state. Default to splitting the target using [separate-before-serializing-shared-state](../../principle-separate-before-serializing-shared-state/SKILL.md). Serialize only for real invariants.\n   - Smallest safe decomposition. If one worker is best, name why.\n4. Delegate code-writing to a fresh independent worker with the entire [poteto role prompt](../../../references/agent-prompts/poteto-agent.md) and exact file pointers. Use the configured feature role when supported and observed. Otherwise request inherited model and effort. Record requested and observed selections separately, with unknown for unobserved values. Assign exact file paths, a named data shape and its organizing structure, and success criteria tied to the user outcome. Choose the structure before the delegate writes logic under [model-the-domain](../../principle-model-the-domain/SKILL.md). Prefer a state machine over scattered booleans, a table or registry over branching, or a typed model over repeated shape assumptions. When implementation admits multiple valid shapes, such as error handling, abstraction layer or test structure, delegate through [arena](../../arena/SKILL.md). Its runners surface alternatives and its fresh cross-judge guards the pick. This gate is mandatory. There is no skip-with-reason escape, and Laziness Protocol does not override it. The gain is review separation, not lines saved. A worker forbidden to spawn owns the diff directly and returns it to the lead for the same review separation. It never waits on a nested worker or replies \"standing by\". Without authorized independent workers, direct implementation can be an explicit reduced result, but it does not satisfy independent review separation. The lead reviews the actual diff and owns the summary. Apply the mode's Comments rules. Make surgical edits and re-ground upstream-derived files against their source. Port shared-primitive improvements to all consumers and verify each. Commit each verified unit when authorized and after the mode's commit gates.\n5. Verify on the matching surface using available authorized control tools and the mode's matching companion requirements. Tie observed evidence to the intended user outcome. \"Inconclusive\" or wrong-surface is not a pass. Flag it and retain the unverified gate. Compilation or structural checks do not prove the feature works.\n6. Rebase into small, ordered commits and stack follow-ups when authorized and safe for concurrent work. Use [sequence-verifiable-units](../../principle-sequence-verifiable-units/SKILL.md). Build, verify and commit each small unit before the next. An unrun required check blocks advancement. If commit or rebase is unavailable or unauthorized, return the checked diff and ordered delivery plan with those operations unperformed.\n7. If the design is contested, run [interrogate](../../interrogate/SKILL.md) before shipping. Preserve its review rubric, independence and observed model-diversity limits. Sequential review does not become independent or multi-model review.\n8. Run the Opening a PR playbook at `opening-a-pr.md` in this directory. This caller requires that complete playbook, its review gates and actual PR result inspection. If the file is absent, report the exact deferred dependency and stop PR-dependent work. Do not reconstruct it from this paragraph. External PR creation and push require actual authorization. Return a local reviewable result when those actions are unavailable or unauthorized. Never claim a local draft is a created PR. Opening a PR does not start Babysit.\n\n## Throughput checkpoint\n\n- Blocking first steps. Read the full mode, Feature, how, architect, arena and applied leaves. Confirm assignment revision and local permissions before editing.\n- Independent workstreams. n/a because this is one code-coupled feature assigned to a no-spawn delegate. Required independent design and review stay open for the lead.\n- Shared mutable state. Only this delegate writes feature/ and this case output. Source inputs and package files stay read-only.\n- Smallest safe decomposition. One owner reads and designs, adds one grouped summary function, verifies it, and returns the scoped diff to the lead.\n\n## Step dispositions\n\n1. Done as a simple sequential how role in design.md. Independent explainer unavailable to this no-spawn delegate.\n2. Reduced. Two whole-shape sequential sketches and comparison in design.md. Required independent arena candidates and fresh judge remain blocked.\n3. Done. Four items above preceded code edits. Final checkpoint remains the same ownership and decomposition.\n4. No-spawn worker exception applied. This delegate owns feature.diff and returns it for lead review. No nested worker or nested wait ran.\n5. Direct module verification ran. commands/feature.json records eight literal behavior checks. No UI or CLI product was shipped. Matching control companions remain unavailable for any future product verification claim.\n6. skip: Commits and rebases are forbidden. Ordered delivery remains source fixture, grouped-summary addition, direct verification.\n7. skip: No contested design was reported and no shipping action is authorized. Independent review remains required.\n8. Full Opening a PR contract read. skip: External creation, push and readiness are forbidden. Missing deslop stays open. No no-comments independent reviewer ran. The local result is reviewable but no PR exists.\n\n## Architect phases\n\n1. Ground. Done in the sequential how findings.\n2. Sketch. Two alternatives in design.md, reduced capability.\n3. Agree. No human signoff requested for this authorized reversible local feature.\n4. Implement. Done in feature/dashboard.mjs under the no-spawn exception.\n5. Scrap. skip: No pattern of implementation friction occurred.\n\n## Arena phases\n\n1. Frame. The scoped artifact is one grouped-summary function. Local comparison criteria are output correctness, input preservation, existing API preservation and extension simplicity.\n2. Fan out. skip: This delegate is forbidden to spawn. The two sketches are sequential alternatives, never independent candidates.\n3. Cross-judge. skip: This delegate is forbidden to spawn. A fresh independent judge did not run.\n4. Pick. Cedar selected by direct local comparison in design.md. The independent gate remains blocked.\n5. Graft. skip: No contribution from Birch improves Cedar without repeating scans.\n6. Verify. Eight direct checks in commands/feature.json. These do not satisfy independent competition or review.\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/all.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/all.json",
      "sha256": "842ea8feb7d1acc933c830174c2d2eff156912e3fdd30c2d4247b707a9c67a5c",
      "bytes": 12360,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "[\n  {\n    \"name\": \"input-commit\",\n    \"argv\": [\n      \"git\",\n      \"show\",\n      \"--no-patch\",\n      \"--format=%H\",\n      \"352ef9629c424778feb077712c2e7b62bb46e5ce\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"current-head\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"input-tree\",\n    \"argv\": [\n      \"git\",\n      \"ls-tree\",\n      \"--name-only\",\n      \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"committed-inputs/\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"bun-version\",\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"feature\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/verify-feature.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"summaries\\\":[{\\\"status\\\":\\\"open\\\",\\\"count\\\":2,\\\"total\\\":12.5},{\\\"status\\\":\\\"closed\\\",\\\"count\\\":1,\\\"total\\\":4}],\\\"inputUnchanged\\\":true,\\\"existingExportsUnchanged\\\":true,\\\"baselineFeatureAbsent\\\":true,\\\"checks\\\":8}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"feature-diff\",\n    \"argv\": [\n      \"git\",\n      \"diff\",\n      \"--no-index\",\n      \"--\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 1,\n    \"stdout\": \"diff --git a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\\nindex 92e482b..1e81811 100644\\n--- a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs\\n+++ b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\\n@@ -1,2 +1,13 @@\\n export function visible(orders,status){return orders.filter(o=>o.status===status)}\\n export function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n+\\n+export function summarizeOrders(orders) {\\n+  const summaries = new Map();\\n+  for (const order of orders) {\\n+    const summary = summaries.get(order.status) ?? { status: order.status, count: 0, total: 0 };\\n+    summary.count += 1;\\n+    summary.total += order.total;\\n+    summaries.set(order.status, summary);\\n+  }\\n+  return [...summaries.values()];\\n+}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"bootstrap\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"import {ensureDependenciesInstalled} from \\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\\\"; ensureDependenciesInstalled();\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/[eval]:1:168\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n  },\n  {\n    \"name\": \"orchestrate-setup\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts\",\n      \"--store\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/owned-store\",\n      \"inbox\",\n      \"drain\",\n      \"--peek\",\n      \"--json\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts:20:1\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n  },\n  {\n    \"name\": \"watcher-setup\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\",\n      \"--owner\",\n      \"synthetic\",\n      \"--repo\",\n      \"fixture\",\n      \"--queued-stack\",\n      \"--stack-prs\",\n      \"17\",\n      \"--head\",\n      \"17=352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"--max-polls\",\n      \"1\",\n      \"--timeout\",\n      \"1\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr:4:1\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n  },\n  {\n    \"name\": \"check-plan-unreadable\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/check-plan.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/absent-plan.md\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 2,\n    \"stdout\": \"\",\n    \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/absent-plan.md: cannot read plan (ENOENT)\\n\"\n  },\n  {\n    \"name\": \"check-plan-nonplan\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/check-plan.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/checklist.md\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/checklist.md:1: not a pstack multi-phase plan; leave other workflow plans unchanged\\n\"\n  },\n  {\n    \"name\": \"decision-log\",\n    \"argv\": [\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/decisions.tsv\",\n      \"feature\",\n      \"Added grouped order summaries\",\n      \"One Map owns each status summary\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/feature.json\",\n      \"local checks green; independent review open\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"name\": \"decision-log-invalid\",\n    \"argv\": [\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/must-not-exist.tsv\",\n      \"probe\",\n      \"invalid\\ncell\",\n      \"reject before write\",\n      \"fixture\",\n      \"open\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"error: tabs, newlines and carriage returns are not allowed\\n\"\n  },\n  {\n    \"name\": \"decision-log-formula\",\n    \"argv\": [\n      \"bash\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/formula-probe.tsv\",\n      \"probe\",\n      \"=1+1\",\n      \"formula prefix protection\",\n      \"local fixture\",\n      \"open\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/bootstrap.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/bootstrap.json",
      "sha256": "29976083be1b8d69661f3442e9f4f4dd2fa672ccd0e1e0ac4953a020d1ca20cd",
      "bytes": 1664,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"bootstrap\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"import {ensureDependenciesInstalled} from \\\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\\\"; ensureDependenciesInstalled();\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/[eval]:1:168\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/bun-version.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/bun-version.json",
      "sha256": "8bebb3b564765753cf3e16971f803bc1f0cb94817ff60259f68b725e260e87c4",
      "bytes": 236,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"bun-version\",\n  \"argv\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/check-plan-nonplan.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/check-plan-nonplan.json",
      "sha256": "1a4847eefcebe7a9ba5e6ef22134c1d5f4df050c80a2ff195241bb22812685cc",
      "bytes": 669,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"check-plan-nonplan\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/check-plan.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/checklist.md\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/checklist.md:1: not a pstack multi-phase plan; leave other workflow plans unchanged\\n\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/check-plan-unreadable.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/check-plan-unreadable.json",
      "sha256": "4f4562f15026c517534556e648ac67bd2e5f77973405fdf44ccd4dd6fad8d170",
      "bytes": 632,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"check-plan-unreadable\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/check-plan.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/absent-plan.md\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 2,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/absent-plan.md: cannot read plan (ENOENT)\\n\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/current-head.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/current-head.json",
      "sha256": "8d239e31457d7cca56cea3a8f9fbde4634c6f4d9054c9da83bf206d095c1b972",
      "bytes": 284,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"current-head\",\n  \"argv\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/decision-log-formula.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/decision-log-formula.json",
      "sha256": "73534e3b8f347a99a60a5110764c80eb57030f06e6cf2f129ddeac1f222e8e29",
      "bytes": 564,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"decision-log-formula\",\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/formula-probe.tsv\",\n    \"probe\",\n    \"=1+1\",\n    \"formula prefix protection\",\n    \"local fixture\",\n    \"open\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/decision-log-invalid.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/decision-log-invalid.json",
      "sha256": "d2610b0c715c9f58e07fdcc8f88c6df4532226acbf6c5c80210adeacc83bbc18",
      "bytes": 622,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"decision-log-invalid\",\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/must-not-exist.tsv\",\n    \"probe\",\n    \"invalid\\ncell\",\n    \"reject before write\",\n    \"fixture\",\n    \"open\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"error: tabs, newlines and carriage returns are not allowed\\n\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/decision-log.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/decision-log.json",
      "sha256": "c11be7ec0f5267efa6ddcb237ff73419a420edae0c5804178e28540612e707c0",
      "bytes": 730,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"decision-log\",\n  \"argv\": [\n    \"bash\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/decisions.tsv\",\n    \"feature\",\n    \"Added grouped order summaries\",\n    \"One Map owns each status summary\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/feature.json\",\n    \"local checks green; independent review open\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/feature-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/feature-diff.json",
      "sha256": "d308b122ccb791a37eeed926617bd58f09badf499f3b857fa2342d466cd66037",
      "bytes": 1660,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"feature-diff\",\n  \"argv\": [\n    \"git\",\n    \"diff\",\n    \"--no-index\",\n    \"--\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff --git a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\\nindex 92e482b..1e81811 100644\\n--- a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs\\n+++ b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\\n@@ -1,2 +1,13 @@\\n export function visible(orders,status){return orders.filter(o=>o.status===status)}\\n export function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n+\\n+export function summarizeOrders(orders) {\\n+  const summaries = new Map();\\n+  for (const order of orders) {\\n+    const summary = summaries.get(order.status) ?? { status: order.status, count: 0, total: 0 };\\n+    summary.count += 1;\\n+    summary.total += order.total;\\n+    summaries.set(order.status, summary);\\n+  }\\n+  return [...summaries.values()];\\n+}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/feature.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/feature.json",
      "sha256": "9728283f6836d2bc4e288bb973dbd73c947a1484181e473e06c118c3c07aefd6",
      "bytes": 569,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"feature\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/verify-feature.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"summaries\\\":[{\\\"status\\\":\\\"open\\\",\\\"count\\\":2,\\\"total\\\":12.5},{\\\"status\\\":\\\"closed\\\",\\\"count\\\":1,\\\"total\\\":4}],\\\"inputUnchanged\\\":true,\\\"existingExportsUnchanged\\\":true,\\\"baselineFeatureAbsent\\\":true,\\\"checks\\\":8}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/input-commit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/input-commit.json",
      "sha256": "c629c914f48f2751fb2ba456d5655f91ed97bd6d349472d6336a998038ff2824",
      "bytes": 352,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"input-commit\",\n  \"argv\": [\n    \"git\",\n    \"show\",\n    \"--no-patch\",\n    \"--format=%H\",\n    \"352ef9629c424778feb077712c2e7b62bb46e5ce\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/input-tree-corrected.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/input-tree-corrected.json",
      "sha256": "284e4beb088906a126b92d9875930f84ce5eb6a2bd99abf2ca73bdae95dad1d3",
      "bytes": 7440,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"argv\": [\n    \"git\",\n    \"-C\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/..\",\n    \"ls-tree\",\n    \"-r\",\n    \"--name-only\",\n    \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n    \"committed-inputs/\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"committed-inputs/README.md\\ncommitted-inputs/additional-v2/README.md\\ncommitted-inputs/additional-v2/caller-migration/api.mjs\\ncommitted-inputs/additional-v2/caller-migration/contract.test.mjs\\ncommitted-inputs/additional-v2/caller-migration/notification.mjs\\ncommitted-inputs/additional-v2/caller-migration/package.json\\ncommitted-inputs/additional-v2/caller-migration/profile.mjs\\ncommitted-inputs/additional-v2/caller-migration/scope.md\\ncommitted-inputs/additional-v2/dead-path/acceptance.json\\ncommitted-inputs/additional-v2/dead-path/caller.mjs\\ncommitted-inputs/additional-v2/dead-path/contract.test.mjs\\ncommitted-inputs/additional-v2/dead-path/duplicate-reference.md\\ncommitted-inputs/additional-v2/dead-path/handler.mjs\\ncommitted-inputs/additional-v2/dead-path/instructions.md\\ncommitted-inputs/additional-v2/dead-path/scope.md\\ncommitted-inputs/additional-v2/empty-function/acceptance.json\\ncommitted-inputs/additional-v2/empty-function/contracts.test-d.ts\\ncommitted-inputs/additional-v2/empty-function/fixture-data.mjs\\ncommitted-inputs/additional-v2/empty-function/subject.mjs\\ncommitted-inputs/additional-v2/empty-function/table-relations.test.mjs\\ncommitted-inputs/additional-v2/empty-function/types.ts\\ncommitted-inputs/additional-v2/empty-function/weak.test.mjs\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js\\ncommitted-inputs/additional-v2/preparation-checks.json\\ncommitted-inputs/additional-v2/scenario-map.json\\ncommitted-inputs/additional-v3/README.md\\ncommitted-inputs/additional-v3/installed-compiler-paths.json\\ncommitted-inputs/additional-v3/invalid-input/adapter.ts\\ncommitted-inputs/additional-v3/invalid-input/boundary.test.mjs\\ncommitted-inputs/additional-v3/invalid-input/domain.ts\\ncommitted-inputs/additional-v3/invalid-input/internal-caller.ts\\ncommitted-inputs/additional-v3/invalid-input/internal-guards.test.mjs\\ncommitted-inputs/additional-v3/invalid-input/scope.md\\ncommitted-inputs/additional-v3/invalid-input/tsconfig.json\\ncommitted-inputs/additional-v3/migration-end-state/consumer.ts\\ncommitted-inputs/additional-v3/migration-end-state/contract.test.mjs\\ncommitted-inputs/additional-v3/migration-end-state/index.ts\\ncommitted-inputs/additional-v3/migration-end-state/legacy.ts\\ncommitted-inputs/additional-v3/migration-end-state/target.md\\ncommitted-inputs/additional-v3/migration-end-state/tsconfig.json\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js\\ncommitted-inputs/additional-v3/preparation-checks.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/admin/audit.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/admin/team.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/core/export.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/core/search.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json\\ncommitted-inputs/additional-v3/repeatable-change/notes.txt\\ncommitted-inputs/additional-v3/repeatable-change/scope.md\\ncommitted-inputs/additional-v3/scenario-map.json\\ncommitted-inputs/additional/README.md\\ncommitted-inputs/additional/cache/README.md\\ncommitted-inputs/additional/cache/cache.mjs\\ncommitted-inputs/additional/cache/caller.mjs\\ncommitted-inputs/additional/cache/invalidation.diff\\ncommitted-inputs/additional/cache/manifest.json\\ncommitted-inputs/additional/cache/probe.mjs\\ncommitted-inputs/additional/cache/vendor/disposer-v1.mjs\\ncommitted-inputs/additional/corpus/records.jsonl\\ncommitted-inputs/additional/dead-path/caller.mjs\\ncommitted-inputs/additional/dead-path/duplicate-reference.md\\ncommitted-inputs/additional/dead-path/handler.mjs\\ncommitted-inputs/additional/dead-path/instructions.md\\ncommitted-inputs/additional/dead-path/scope.md\\ncommitted-inputs/additional/history/capsule.json\\ncommitted-inputs/additional/history/history.json\\ncommitted-inputs/additional/history/jay-mode.md\\ncommitted-inputs/additional/history/shared-records.json\\ncommitted-inputs/additional/invoice/adapter.mjs\\ncommitted-inputs/additional/invoice/calculator.mjs\\ncommitted-inputs/additional/invoice/controller.mjs\\ncommitted-inputs/additional/invoice/decision.md\\ncommitted-inputs/additional/invoice/exporter.mjs\\ncommitted-inputs/additional/invoice/facade.mjs\\ncommitted-inputs/additional/invoice/formatter.mjs\\ncommitted-inputs/additional/legal-header/source.diff\\ncommitted-inputs/additional/legal-header/source.mjs\\ncommitted-inputs/additional/migration/api.mjs\\ncommitted-inputs/additional/migration/contract.mjs\\ncommitted-inputs/additional/migration/notification.mjs\\ncommitted-inputs/additional/migration/profile.mjs\\ncommitted-inputs/additional/migration/scope.md\\ncommitted-inputs/additional/scenario-map.json\\ncommitted-inputs/additional/types/README.md\\ncommitted-inputs/additional/types/boundary.ts\\ncommitted-inputs/additional/types/context.ts\\ncommitted-inputs/dashboard.mjs\\ncommitted-inputs/forge.json\\ncommitted-inputs/history.json\\ncommitted-inputs/invoice.mjs\\ncommitted-inputs/orders.json\\ncommitted-inputs/runtime.mjs\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/input-tree.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/input-tree.json",
      "sha256": "d3b716e51f56d96be1ac27a86337d14fabf3071f9aa5ed4ac6769040fae5f1fa",
      "bytes": 318,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"input-tree\",\n  \"argv\": [\n    \"git\",\n    \"ls-tree\",\n    \"--name-only\",\n    \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n    \"committed-inputs/\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/orchestrate-setup.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/orchestrate-setup.json",
      "sha256": "16690b061c7ab1e2428185f9f39d63d436c6624c58ea69ceb39354e0a4367feb",
      "bytes": 1786,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"orchestrate-setup\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts\",\n    \"--store\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/owned-store\",\n    \"inbox\",\n    \"drain\",\n    \"--peek\",\n    \"--json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts:20:1\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/commands/watcher-setup.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/watcher-setup.json",
      "sha256": "be1ac0342173a1c5fbc1099cf979d6f2a060c02a5a1af32c6dea093fef87e551",
      "bytes": 1822,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"name\": \"watcher-setup\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\",\n    \"--owner\",\n    \"synthetic\",\n    \"--repo\",\n    \"fixture\",\n    \"--queued-stack\",\n    \"--stack-prs\",\n    \"17\",\n    \"--head\",\n    \"17=352ef9629c424778feb077712c2e7b62bb46e5ce\",\n    \"--max-polls\",\n    \"1\",\n    \"--timeout\",\n    \"1\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"15 |       if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);\\n16 |       const installed = JSON.parse(readFileSync(join(import.meta.dir, \\\"node_modules\\\", name, \\\"package.json\\\"), \\\"utf8\\\"));\\n17 |       if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);\\n18 |     }\\n19 |   } catch (error) {\\n20 |     throw new Error(\\\"Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. \\\" + String(error));\\n                   ^\\nerror: Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. Error: ENOENT: no such file or directory, open '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/node_modules/commander/package.json'\\n      at ensureDependenciesInstalled (/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts:20:15)\\n      at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr:4:1\\n\\nBun v1.4.2 (macOS arm64)\\n\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/contract-probes.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/contract-probes.json",
      "sha256": "0e2f89afc1e3ec2fa31e79de4b70125e07de1fcc4d73a7d19070323308bda561",
      "bytes": 5908,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "[\n  {\n    \"label\": \"current-local-artifact\",\n    \"input\": {\n      \"id\": \"fresh\",\n      \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"artifacts\": [\n        \"feature/dashboard.mjs\",\n        \"commands/feature.json\"\n      ],\n      \"method\": \"direct-local-execution\"\n    },\n    \"accepted\": true,\n    \"reasons\": [],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"stale-identity\",\n    \"input\": {\n      \"id\": \"other\",\n      \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"artifacts\": [\n        \"feature/dashboard.mjs\",\n        \"commands/feature.json\"\n      ],\n      \"method\": \"direct-local-execution\"\n    },\n    \"accepted\": false,\n    \"reasons\": [\n      \"assignment identity mismatch\"\n    ],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"stale-input\",\n    \"input\": {\n      \"id\": \"fresh\",\n      \"inputRevision\": \"ffffffffffffffffffffffffffffffffffffffff\",\n      \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"artifacts\": [\n        \"feature/dashboard.mjs\",\n        \"commands/feature.json\"\n      ],\n      \"method\": \"direct-local-execution\"\n    },\n    \"accepted\": false,\n    \"reasons\": [\n      \"input revision mismatch\"\n    ],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"stale-full-head\",\n    \"input\": {\n      \"id\": \"fresh\",\n      \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"currentHead\": \"ffffffffffffffffffffffffffffffffffffffff\",\n      \"artifacts\": [\n        \"feature/dashboard.mjs\",\n        \"commands/feature.json\"\n      ],\n      \"method\": \"direct-local-execution\"\n    },\n    \"accepted\": false,\n    \"reasons\": [\n      \"full current head mismatch\"\n    ],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"short-head\",\n    \"input\": {\n      \"id\": \"fresh\",\n      \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"currentHead\": \"352ef96\",\n      \"artifacts\": [\n        \"feature/dashboard.mjs\",\n        \"commands/feature.json\"\n      ],\n      \"method\": \"direct-local-execution\"\n    },\n    \"accepted\": false,\n    \"reasons\": [\n      \"full current head mismatch\"\n    ],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"missing-artifact\",\n    \"input\": {\n      \"id\": \"fresh\",\n      \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"artifacts\": [\n        \"does-not-exist.md\"\n      ],\n      \"method\": \"direct-local-execution\"\n    },\n    \"accepted\": false,\n    \"reasons\": [\n      \"missing artifact does-not-exist.md\"\n    ],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"ledger-label-only\",\n    \"input\": {\n      \"id\": \"fresh\",\n      \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n      \"artifacts\": [\n        \"feature/dashboard.mjs\",\n        \"commands/feature.json\"\n      ],\n      \"method\": \"unit-test-verified\"\n    },\n    \"accepted\": false,\n    \"reasons\": [\n      \"required method evidence unavailable\"\n    ],\n    \"limit\": \"Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.\"\n  },\n  {\n    \"label\": \"missing-reference\",\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/unavailable-view/skills/poteto-mode/SKILL.md\",\n    \"error\": \"ENOENT\",\n    \"decision\": \"Stop dependent work. Do not reconstruct or write feature code in this branch.\",\n    \"limit\": \"An omitted local view simulates unavailable source. The installed source remains readable.\"\n  },\n  {\n    \"label\": \"missing-reference\",\n    \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/unavailable-view/skills/principle-model-the-domain/SKILL.md\",\n    \"error\": \"ENOENT\",\n    \"decision\": \"Stop dependent work. Do not reconstruct or write feature code in this branch.\",\n    \"limit\": \"An omitted local view simulates unavailable source. The installed source remains readable.\"\n  },\n  {\n    \"label\": \"worker-tools-unavailable\",\n    \"decision\": \"Read the complete mode and leaves. Use sequential how, two design sketches and direct implementation only as reduced capability. Independent architect, arena and review remain blocked.\",\n    \"limit\": \"Simulated negative condition. Native collaboration tools remain exposed in this host. The no-spawn assignment is an enforced instruction boundary, not tool removal.\"\n  },\n  {\n    \"label\": \"watcher-event-inspection\",\n    \"kind\": \"STATUS\",\n    \"terminal\": true,\n    \"reason\": \"status-only\",\n    \"classification\": \"Status query only. Readiness and merge unproven.\",\n    \"limit\": \"Generated inert fixture interpreted from read source types. No watcher or service emitted these events.\"\n  },\n  {\n    \"label\": \"watcher-event-inspection\",\n    \"kind\": \"WAITING\",\n    \"terminal\": false,\n    \"reason\": {\n      \"kind\": \"merge-queue\",\n      \"unmergedCount\": 1\n    },\n    \"classification\": \"Babysit may report frontier merge-ready and stop its watcher. Shipping must wait for observed MERGED or non-null mergedAt. No merge is proven.\",\n    \"limit\": \"Generated inert fixture interpreted from read source types. No watcher or service emitted these events.\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/contract-probes.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/contract-probes.stdout",
      "sha256": "958f730d150c6ee5990bb821c993c1b46fec9b0ee85a71d7ebac2de7dfea9ad0",
      "bytes": 1566,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\"input\":\"352ef9629c424778feb077712c2e7b62bb46e5ce\",\"current\":\"352ef9629c424778feb077712c2e7b62bb46e5ce\",\"guardOutcomes\":[{\"label\":\"current-local-artifact\",\"accepted\":true,\"decision\":[]},{\"label\":\"stale-identity\",\"accepted\":false,\"decision\":[\"assignment identity mismatch\"]},{\"label\":\"stale-input\",\"accepted\":false,\"decision\":[\"input revision mismatch\"]},{\"label\":\"stale-full-head\",\"accepted\":false,\"decision\":[\"full current head mismatch\"]},{\"label\":\"short-head\",\"accepted\":false,\"decision\":[\"full current head mismatch\"]},{\"label\":\"missing-artifact\",\"accepted\":false,\"decision\":[\"missing artifact does-not-exist.md\"]},{\"label\":\"ledger-label-only\",\"accepted\":false,\"decision\":[\"required method evidence unavailable\"]},{\"label\":\"missing-reference\",\"decision\":\"Stop dependent work. Do not reconstruct or write feature code in this branch.\"},{\"label\":\"missing-reference\",\"decision\":\"Stop dependent work. Do not reconstruct or write feature code in this branch.\"},{\"label\":\"worker-tools-unavailable\",\"decision\":\"Read the complete mode and leaves. Use sequential how, two design sketches and direct implementation only as reduced capability. Independent architect, arena and review remain blocked.\"},{\"label\":\"watcher-event-inspection\",\"decision\":\"Status query only. Readiness and merge unproven.\"},{\"label\":\"watcher-event-inspection\",\"decision\":\"Babysit may report frontier merge-ready and stop its watcher. Shipping must wait for observed MERGED or non-null mergedAt. No merge is proven.\"}],\"routesInspected\":23,\"principleBindingsRetained\":24,\"invalidLogAbsent\":true}\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/decisions.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/decisions.tsv",
      "sha256": "b15661e765fc6f46ebd6c9857866da034ab21162c00ca38d180f85fa8bc0a4a4",
      "bytes": 293,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T08:06:32Z\tfeature\tAdded grouped order summaries\tOne Map owns each status summary\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/feature.json\tlocal checks green; independent review open\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/design.md",
      "sha256": "ec3ee812a6b3454c3a210ab33edd01300e0bed2c53aac35b872ea5836c391039",
      "bytes": 3041,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "# Group order summaries\n\n## Problem\n\nThe copied dashboard module filters orders and exports rows. It cannot give a dashboard consumer per-status counts and totals. The synthetic feature adds `summarizeOrders(orders)` without changing existing exports.\n\n## How\n\nThe simple sequential how role inspected `feature/dashboard.before.mjs` and `feature/orders.json`. The former exports two pure functions. `visible` filters on exact status. `exportCsv` emits all rows. The fixture array has three records with numeric totals. The input has no surrounding app or runtime caller. A caller beyond the synthetic module remains unavailable.\n\n## Usage\n\n```js\nsummarizeOrders(orders)\nsummarizeOrders(visible(orders, 'open'))\nsummarizeOrders([])\n```\n\nThe first call returns an array of `{status, count, total}` records in first-seen status order. The second summarizes a selected view. The third returns an empty array.\n\n## Shape\n\nThe data shape is an order array with string `status` and numeric `total`. A `Map` keyed by status owns aggregation and preserves insertion order. One pure function hides grouping and accumulation. Inputs stay unchanged. This assumes trusted internal records, matching the existing module contract. It does not introduce a parser or money rounding policy.\n\n## Sequential alternatives\n\n| Label | Whole shape | Tradeoff |\n| --- | --- | --- |\n| Cedar | A `Map` accumulates summaries in one traversal and returns its values. | It hides grouping behind one function. |\n| Birch | Gather unique statuses, then filter and reduce the orders for every status. | It keeps the same public call but repeats scans and spreads accumulation across operations. |\n\nThese are two sequential sketches under the architect runner discipline. No independent design worker or fresh judge ran because this delegate has a no-spawn assignment. Direct skill invocation is unavailable. I read and followed how, architect and arena inline as a reduced method. The independent architect and arena gates remain blocked for the lead.\n\n## Synthesis decision\n\nCedar is the local base. Its single owner of count and total avoids inconsistent scans. No graft is needed. Birch is rejected because it repeats access without hiding any additional complexity. Both avoid pass-through wrappers, duplicate ownership and public transport types under the inspected red-flag screen. This is parent comparison, not independent judging.\n\n## Tradeoffs accepted\n\nWe accept floating-point totals because the input and existing exporter already use JavaScript numbers. A financial precision requirement would require a separate domain decision. We accept first-seen ordering instead of sorting so the caller retains input ordering.\n\n## Open questions and risks\n\nDoes a real consumer need integer minor-unit money? No real consumer was supplied. The scoped synthetic contract uses the supplied numbers. Independent review is still required before integration.\n\n## Next implementation step\n\nAdd the one pure function, then run literal output and non-mutation checks through Bun.\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs",
      "sha256": "0fe82aee099aa55540aa756a52705d0de9bb68e614964c3760f13852f35a7823",
      "bytes": 551,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "export function visible(orders,status){return orders.filter(o=>o.status===status)}\nexport function exportCsv(orders){return \"id,customer,total\\n\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\"\\n\")}\n\nexport function summarizeOrders(orders) {\n  const summaries = new Map();\n  for (const order of orders) {\n    const summary = summaries.get(order.status) ?? { status: order.status, count: 0, total: 0 };\n    summary.count += 1;\n    summary.total += order.total;\n    summaries.set(order.status, summary);\n  }\n  return [...summaries.values()];\n}\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/feature.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature.diff",
      "sha256": "ddad1f46a24a4d3406126d9051c953aedbb407cf139fa7b30adc6011af49286c",
      "bytes": 1124,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "diff --git a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\nindex 92e482b..1e81811 100644\n--- a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs\n+++ b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/feature/dashboard.mjs\n@@ -1,2 +1,13 @@\n export function visible(orders,status){return orders.filter(o=>o.status===status)}\n export function exportCsv(orders){return \"id,customer,total\\n\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\"\\n\")}\n+\n+export function summarizeOrders(orders) {\n+  const summaries = new Map();\n+  for (const order of orders) {\n+    const summary = summaries.get(order.status) ?? { status: order.status, count: 0, total: 0 };\n+    summary.count += 1;\n+    summary.total += order.total;\n+    summaries.set(order.status, summary);\n+  }\n+  return [...summaries.values()];\n+}\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/finalize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/finalize.mjs",
      "sha256": "43d2b635f3a8c69f9826237b07c3491e2e816d7f2024b946eaa7bf5da7662ca2",
      "bytes": 15479,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "import {readFile,writeFile,stat} from 'node:fs/promises';\nimport {createHash} from 'node:crypto';\nconst root=import.meta.dir;\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst input=JSON.parse(await readFile(`${root}/input.json`,'utf8'));\nconst receipt={assignmentId:'fresh',workerId:'/root/fresh',inputRevision:'352ef9629c424778feb077712c2e7b62bb46e5ce',currentHead:Bun.spawnSync(['git','-C',root,'rev-parse','HEAD']).stdout.toString().trim(),requestedModel:'inherit-parent',actualModel:'unknown',requestedEffort:'inherit-parent',actualEffort:'unknown',status:'completed-local-artifacts-review-open',method:'native no-spawn delegate with direct local execution and sequential design fallback',artifacts:[]};\nfor(const file of ['feature.diff','feature/dashboard.mjs','verify-feature.mjs','commands/feature.json','design.md','checklist.md','bindings.json','route-report.json','contract-probes.json','decisions.tsv']){const bytes=await readFile(`${root}/${file}`);receipt.artifacts.push({path:file,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')});}\nawait writeFile(`${root}/worker-receipt.json`,JSON.stringify(receipt,null,2));\nconst git=Bun.spawnSync(['git','-C',root+'/..','ls-tree','-r','--name-only',receipt.inputRevision,'committed-inputs/']);\nawait writeFile(`${root}/commands/input-tree-corrected.json`,JSON.stringify({argv:['git','-C',root+'/..','ls-tree','-r','--name-only',receipt.inputRevision,'committed-inputs/'],exitCode:git.exitCode,stdout:git.stdout.toString(),stderr:git.stderr.toString()},null,2));\nconst probes=JSON.parse(await readFile(`${root}/contract-probes.json`,'utf8'));\nconst readback={receipt:JSON.parse(await readFile(`${root}/worker-receipt.json`,'utf8')),decisionLog:await readFile(`${root}/decisions.tsv`,'utf8'),sourceSnapshots:JSON.parse(await readFile(`${root}/source-reads/manifest.json`,'utf8')).length,correctedInputTreeFiles:git.stdout.toString().trim().split('\\n').length};\nawait writeFile(`${root}/readback.json`,JSON.stringify(readback,null,2));\nconsole.log(JSON.stringify({assignmentId:receipt.assignmentId,inputRevision:receipt.inputRevision,currentHead:receipt.currentHead,artifacts:receipt.artifacts.length,sourceSnapshots:readback.sourceSnapshots,correctedInputTreeFiles:readback.correctedInputTreeFiles}));\nconst feature=JSON.parse(await readFile(`${root}/commands/feature.json`,'utf8'));\nconst result=`# fresh-worker-mode\n\n## Supplied input\n\nThe case contract below is synthetic task input. Its package source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. This case used only the installed package at ${pkg}. The input repository revision is distinct from that package source freeze.\n\n\\`\\`\\`json\n${JSON.stringify(input,null,2)}\n\\`\\`\\`\n\n## Actual output\n\nThe no-spawn delegate added \\`summarizeOrders(orders)\\` to the copied synthetic dashboard module. Dashboard consumers receive per-status counts and totals in first-seen order. The next maintainer inherits one Map-based owner of aggregation and a direct rerunnable verification script.\n\nThe function works against the copied fixture in the observed local run. This is not a full mode acceptance claim. Architect competition and independent review remain open. No PR, commit, push, install, schedule, settings change or service action occurred.\n\nThe local design compared a Map accumulator with unique-status collection followed by repeated filtering. The Map shape became the base because it owns count and total together. These are sequential sketches. They are not independent candidates, a fresh cross-judge or verified model diversity.\n\n\\`\\`\\`text\n${feature.stdout.trim()}\n\\`\\`\\`\n\nRun \\`bun --no-install ${root}/verify-feature.mjs\\` to repeat the actual feature check. The eight checks cover literal summary results, filtered input, empty input, reserved-looking status keys, non-mutation, unchanged filter behavior, unchanged exporter behavior and absence of the feature from the copied baseline. The exporter has a pre-existing CSV quoting defect outside this scoped feature. It remains unchanged.\n\n## Identity and source evidence\n\nThe immutable assignment is \\`fresh-worker-mode/assignment.json\\`, id \\`fresh\\`, owner \\`fresh\\`. The native worker identity is \\`/root/fresh\\`. The lead dispatched this fresh delegate. This delegate invoked zero spawns and zero nested waits.\n\nThe observed full input and current HEAD are both \\`${receipt.inputRevision}\\`. Commands and outputs are preserved in \\`commands/input-commit.json\\`, \\`commands/current-head.json\\` and \\`commands/input-tree-corrected.json\\`. The first relative input-tree query returned empty because it ran from the case subdirectory. The corrected repository-root query lists the committed inputs. That observation-method correction is retained instead of calling the inputs missing.\n\n\\`worker-receipt.json\\` records exact artifacts and SHA-256 digests. Its completed-local label does not prove independent review or integration. The lead must inspect the actual diff and verification before accepting it. Output artifacts are uncommitted and are not claimed to belong to the input revision.\n\nRequested model and effort are inherit-parent. Actual model and effort are unknown because the worker operation supplied no observed runtime model identity. Diversity remains unverified.\n\n\\`source-reads/manifest.json\\` records 73 actual file reads and byte-identical local snapshots. It includes the complete mode, all 23 route playbooks, all 24 principle leaves, role prompt, host/ownership/model/assignment contracts, how, architect, arena, unslop and selected helper sources. The source freeze is the supplied package identifier. These reads alone do not establish package loading, host behavior or a behavioral pass.\n\n## Throughput checkpoint\n\n- Blocking first steps. The full mode, Feature, how, architect, arena and applicable leaves were read before feature edits. Assignment and current revision were checked with git before helper probes and returned with the result. The lead verified the input revision before dispatch.\n- Independent workstreams. n/a because this is one code-coupled feature assigned to a no-spawn delegate. Required independent design and review stay open for the lead.\n- Shared mutable state. This delegate exclusively writes this case directory and its root result file. Shared inputs and the installed package remain read-only.\n- Smallest safe decomposition. One owner reads and designs, adds one pure grouped-summary function, verifies it, and returns the diff. Extra code writers would share one small module without reducing the dependency chain.\n\nThe checkpoint is retained in \\`checklist.md\\`. The final boundary keeps the same one-owner decomposition and hands independent review to the lead.\n\n## Playbook and principle bindings\n\n\\`checklist.md\\` starts with all eight Feature steps and sub-items copied verbatim. Its later dispositions retain explicit skips. No todo operation is exposed, so the authorized local Markdown checklist is a reduced tool binding. Architect and Arena phase dispositions are also retained.\n\n\\`bindings.json\\` preserves all 23 exact playbook paths and all 24 principle names, aliases and meanings extracted from the complete mode. \\`route-report.json\\` records each route's steps, delivery exception and permission boundary. The 23 route exercises are source-contract inspection, not 23 executed feature, cleanup, shipping, profiling or autonomous workflows. Such operations need their concrete prerequisites and authorization. Local presence closes the historical reference-deferral question only.\n\nApplied leaves read in full this session and their decisions are listed below.\n\n- Model the Domain selected a Map keyed by status before writing logic.\n- Build the Lever produced \\`verify-feature.mjs\\` and the rerunnable contract guard script.\n- Prove It Works required importing and calling the real modified module, then reading actual command output.\n- Test Behavior, Not Implementation required literal expected arrays and preserved caller-visible behavior.\n- Separate Before Serializing Shared State retained distinct case ownership with no shared package or fixture mutation.\n- Sequence Work into Verifiable Units kept the local addition and its check together. Commits and rebase were explicitly skipped because authorization forbids them.\n- Exhaust the Design Space produced the two whole-shape sequential sketches. The mandatory independent design method remains unsatisfied.\n\nOther captured leaves remain available as source instructions. Capturing them does not mean every principle was applied. Unslop governed the reports. Technical-writing was read for this document. The external create-skill companion is unavailable within the permitted package-only workflow. Its authoring fallback contract was read; no personal skill was authored. External deslop is absent and no replacement review was authorized. No no-comments independent reviewer ran. Those delivery gates remain open.\n\n## Variants and actual tools\n\n| Variant | Actual action or response | Evidence and limit |\n| --- | --- | --- |\n| Fresh native delegate | Lead spawned this worker with full mode instructions and exact immutable assignment. The delegate read the full mode and owns its local diff. | This report and worker-receipt.json are the returned result. Parent spawn receipt and lead result inspection are outside this delegate's write scope. |\n| No-spawn worker | The delegate implemented directly and returned its own diff. | feature.diff, design.md and commands/feature.json. No nested waiting. Lead independent review still required. |\n| Worker tools unavailable | Sequential how and design fallback response recorded. | contract-probes.json. Simulated negative condition. Collaboration tools remain exposed; this assignment forbids nested spawning. |\n| Mode unavailable | Read of the exact omitted local-view path failed ENOENT. Dependent work in this variant stops. | contract-probes.json. The installed mode remains readable. This is not host-enforced file denial. |\n| Applied leaf unavailable | Read of the omitted local-view model-the-domain path failed ENOENT. Dependent code work in this variant stops. | contract-probes.json. The installed leaf remains readable. This is a simulated absence. |\n| Helper setup failure | Real installed bootstrap, orch and watcher entry points fail with missing pinned Commander metadata. | commands/bootstrap.json, commands/orchestrate-setup.json, commands/watcher-setup.json. No install or bypass. |\n| Stale assignment identity | Local guard rejects an altered identity. | contract-probes.json. Synthetic altered result, not a stale native receipt. |\n| Stale input or current head | Local guard rejects changed full input SHA, changed full current SHA and a short SHA. | contract-probes.json. Actual current HEAD remains unchanged. |\n| Missing artifact | Local guard rejects an absent artifact even with valid labels. | contract-probes.json. No integration performed. |\n| Ledger label only | Local guard rejects a label without required method evidence. | contract-probes.json. A ledger row is not a verifier. |\n| No todo tool | Actual authorized local checklist created and read back. | checklist.md. Reduced tool binding preserves verbatim steps. |\n| Status-only exit 0 | Inert STATUS event remains a query observation, never readiness or merge proof. | watcher-fixtures.ndjson and contract-probes.json. Generated fixture only. |\n| Queued WAITING | Inert nonterminal WAITING with merge-queue reason can end Babysit's ready report, while Shipping still needs actual merged state. | Same fixtures. No live watcher receipt or service contact. |\n\nThe actual exposed file/execution binding is \\`functions.exec\\` calling \\`tools.exec_command\\`. Bun scripts read source files, wrote owned files, spawned bounded local commands and saved stdout, stderr and exit codes. Persistence was verified by reading saved receipts and logs. Collaboration was used only to send scoped progress to the lead. No exposed tool grants external authorization.\n\n## Helper commands and results\n\nThe log helper was called with exactly six positional arguments, starting with an explicit owned logfile. \\`decisions.tsv\\` was read back. The newline probe exits 1 and creates no logfile. The formula probe prefixes the formula-leading decision with a quote. Commands and readback are retained under \\`commands/\\`, \\`formula-probe.tsv\\` and \\`readback.json\\`.\n\nThe orch probe uses an explicit outside-package store at \\`${root}/owned-store\\` and \\`inbox drain --peek --json\\`. Bootstrap fails before inbox processing, so no peek receipt, durable drain receipt or initialized store is claimed. A later actual drain and ledger check are blocked by setup. The full real orch helper and store sources were read and preserved. The helper test source was inspected after the setup attempt, so this run does not claim a completed pre-execution test-contract review gate.\n\nThe watcher probe uses explicit synthetic owner/repo, queued PR list, a full 40-character expected head and finite budgets of one poll and one second. Real bootstrap fails before importing the CLI or contacting the forge. The tested input head is an inert fixture pin, not a remote head observation. The dependency gate stops further watcher execution. It does not prove a strict wall-clock deadline.\n\nThe plan checker was called with one positional path each time. An unreadable path exits 2. The Feature checklist exits 1 with \\`not a pstack multi-phase plan; leave other workflow plans unchanged\\`. That checker correctly does not certify this implementation checklist. No structural success is represented as runtime verification.\n\nAll command arrays, stdout, stderr and exit codes are preserved in \\`commands/all.json\\`. The diff command exits 1 because the two files differ. That exit code is expected and is not a test failure.\n\n## Limits and open gates\n\nNo native nested design workers or fresh judge ran under the no-spawn assignment. Parent inspection is required for independent review. No requested model was treated as observed. No private or unrelated history was read. The scoped conversation is visible, but a complete exported native transcript is unavailable to this delegate. The source snapshots and local command records preserve actual file content and process output; they are not a fabricated full native transcript.\n\nAll complete route documents are locally present. That resolves reference availability only. It does not satisfy companion execution, dependency setup, external authorization, independent design review, real-surface controls, model diversity, persistent wake or a clean shipping verdict.\n\nNo full host behavior claim or self-assigned grade is made. The local feature has direct observed evidence. The reduced design method and blocked delivery gates remain explicit.\n\n## Attention\n\nreviewed by unknown\n\nIndependent cross-model trail review is blocked for this no-spawn delegate. The lead must inspect the diff, script and actual output. The complete native transcript export is unavailable. Helper setup is a real block. Negative capability views and watcher events are simulated. The existing CSV quoting defect remains outside this scoped feature.\n`;\nawait writeFile(`${root}/../fresh-worker-mode.result.md`,result);\nconsole.log(JSON.stringify({result:`${root}/../fresh-worker-mode.result.md`,bytes:(await stat(`${root}/../fresh-worker-mode.result.md`)).size}));\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/formula-probe.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/formula-probe.tsv",
      "sha256": "c3e541fe69730458fe85f85b4912f93c8fd2707fa01090ec5aee4f76688f3cad",
      "bytes": 116,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "ts\tphase\tdecision\twhy\tevidence\tresult\n2026-10-16T08:06:32Z\tprobe\t'=1+1\tformula prefix protection\tlocal fixture\topen\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/lead-review.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/lead-review.json",
      "sha256": "9495a390f1bca83c99d17ecf53e2cf96e071c6ded02384074c19769277e04901",
      "bytes": 2043,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"assignmentId\": \"fresh\",\n  \"workerId\": \"/root/fresh\",\n  \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n  \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n  \"reviewer\": \"/root\",\n  \"checked\": [\n    {\n      \"path\": \"feature.diff\",\n      \"sha256\": \"ddad1f46a24a4d3406126d9051c953aedbb407cf139fa7b30adc6011af49286c\"\n    },\n    {\n      \"path\": \"feature/dashboard.mjs\",\n      \"sha256\": \"0fe82aee099aa55540aa756a52705d0de9bb68e614964c3760f13852f35a7823\"\n    },\n    {\n      \"path\": \"verify-feature.mjs\",\n      \"sha256\": \"4324f625a66164647b4616ee0b317d4da431876caed7148617c28654a56a88c3\"\n    },\n    {\n      \"path\": \"commands/feature.json\",\n      \"sha256\": \"9728283f6836d2bc4e288bb973dbd73c947a1484181e473e06c118c3c07aefd6\"\n    },\n    {\n      \"path\": \"design.md\",\n      \"sha256\": \"ec3ee812a6b3454c3a210ab33edd01300e0bed2c53aac35b872ea5836c391039\"\n    },\n    {\n      \"path\": \"checklist.md\",\n      \"sha256\": \"da04940a3d32d9e98cc4de225c3d8aaad5823d8ec77b599112223a9ce66170e7\"\n    },\n    {\n      \"path\": \"bindings.json\",\n      \"sha256\": \"7926901be982a0b74e04a071ea95a83e63032dc9d9ff0de8de4590eb75c75d12\"\n    },\n    {\n      \"path\": \"route-report.json\",\n      \"sha256\": \"d9ab9dd81b60b90e8c23dec3b362c7f45546878df44470b2b7cb502dfba79f1e\"\n    },\n    {\n      \"path\": \"contract-probes.json\",\n      \"sha256\": \"0e2f89afc1e3ec2fa31e79de4b70125e07de1fcc4d73a7d19070323308bda561\"\n    },\n    {\n      \"path\": \"decisions.tsv\",\n      \"sha256\": \"b15661e765fc6f46ebd6c9857866da034ab21162c00ca38d180f85fa8bc0a4a4\"\n    }\n  ],\n  \"verification\": \"lead-verification.command.json\",\n  \"finding\": \"Map aggregation and literal behavior assertions inspected. Independent lead rerun exits 0. No change to existing exports. Required independent design competition and cross-model review remain open.\",\n  \"guardLimit\": \"probe-contracts.mjs checks presence and a method string. The string alone does not prove execution. Actual log inspection and independent feature rerun supply evidence for this local result. This is not a general trusted method verifier.\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/lead-review.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/lead-review.mjs",
      "sha256": "a2c0bc4012363d650de2c1b66189859f6d01fdf92e438d207444fba69e9ff0ce",
      "bytes": 1420,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "const receipt=await Bun.file('fresh-worker-mode/worker-receipt.json').json();const head=Bun.spawnSync(['git','rev-parse','HEAD']).stdout.toString().trim();const checked=[];\nif(receipt.assignmentId!=='fresh'||receipt.workerId!=='/root/fresh'||receipt.inputRevision!==head||receipt.currentHead!==head)throw new Error('identity/revision mismatch');\nfor(const a of receipt.artifacts){const bytes=await Bun.file('fresh-worker-mode/'+a.path).arrayBuffer();const hash=new Bun.CryptoHasher('sha256').update(bytes).digest('hex');if(hash!==a.sha256)throw new Error('digest mismatch '+a.path);checked.push({path:a.path,sha256:hash});}\nconst r={assignmentId:'fresh',workerId:'/root/fresh',inputRevision:head,currentHead:head,reviewer:'/root',checked,verification:'lead-verification.command.json',finding:'Map aggregation and literal behavior assertions inspected. Independent lead rerun exits 0. No change to existing exports. Required independent design competition and cross-model review remain open.',guardLimit:'probe-contracts.mjs checks presence and a method string. The string alone does not prove execution. Actual log inspection and independent feature rerun supply evidence for this local result. This is not a general trusted method verifier.'};await Bun.write('fresh-worker-mode/lead-review.json',JSON.stringify(r,null,2));console.log(JSON.stringify({identityChecked:true,digestsChecked:checked.length,fullHead:head}));\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/lead-verification.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/lead-verification.command.json",
      "sha256": "7143383044ef32abc821d6c604d3be28920a383b933fccbc571a28d2ced17e16",
      "bytes": 360,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"fresh-worker-mode/verify-feature.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"summaries\\\":[{\\\"status\\\":\\\"open\\\",\\\"count\\\":2,\\\"total\\\":12.5},{\\\"status\\\":\\\"closed\\\",\\\"count\\\":1,\\\"total\\\":4}],\\\"inputUnchanged\\\":true,\\\"existingExportsUnchanged\\\":true,\\\"baselineFeatureAbsent\\\":true,\\\"checks\\\":8}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/probe-contracts.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/probe-contracts.mjs",
      "sha256": "4156eec13247675372556535d93a35bfa943db71dfdb4ec36a8cd64d9e733682",
      "bytes": 8319,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "import assert from 'node:assert/strict';\nimport {readFile,writeFile,stat,mkdir} from 'node:fs/promises';\nconst root=import.meta.dir;\nconst input='352ef9629c424778feb077712c2e7b62bb46e5ce';\nconst assignment=JSON.parse(await readFile(`${root}/assignment.json`,'utf8'));\nconst current=Bun.spawnSync(['git','-C',root,'rev-parse','HEAD']).stdout.toString().trim();\nconst report=[];\nasync function accept(result){\n const reasons=[];\n if(result.id!==assignment.id)reasons.push('assignment identity mismatch');\n if(result.inputRevision!==assignment.inputRevision)reasons.push('input revision mismatch');\n if(!/^[a-f0-9]{40}$/.test(result.currentHead)||result.currentHead!==current)reasons.push('full current head mismatch');\n for(const path of result.artifacts??[])try{if(!(await stat(`${root}/${path}`)).isFile())reasons.push('artifact is not a file');}catch{reasons.push(`missing artifact ${path}`);}\n if(result.method!=='direct-local-execution')reasons.push('required method evidence unavailable');\n return {accepted:reasons.length===0,reasons};\n}\nconst valid={id:assignment.id,inputRevision:input,currentHead:current,artifacts:['feature/dashboard.mjs','commands/feature.json'],method:'direct-local-execution'};\nfor(const [label,result] of [['current-local-artifact',valid],['stale-identity',{...valid,id:'other'}],['stale-input',{...valid,inputRevision:'f'.repeat(40)}],['stale-full-head',{...valid,currentHead:'f'.repeat(40)}],['short-head',{...valid,currentHead:current.slice(0,7)}],['missing-artifact',{...valid,artifacts:['does-not-exist.md']}],['ledger-label-only',{...valid,method:'unit-test-verified'}]]){const observed=await accept(result);assert.equal(observed.accepted,label==='current-local-artifact');report.push({label,input:result,...observed,limit:'Local guard demonstration using altered copies, not stale native worker receipts or authorization to integrate.'});}\nawait mkdir(`${root}/unavailable-view`,{recursive:true});\nfor(const leaf of ['skills/poteto-mode/SKILL.md','skills/principle-model-the-domain/SKILL.md']){const path=`${root}/unavailable-view/${leaf}`;try{await readFile(path);throw new Error('unexpected available file');}catch(error){assert.equal(error.code,'ENOENT');report.push({label:'missing-reference',path,error:error.code,decision:'Stop dependent work. Do not reconstruct or write feature code in this branch.',limit:'An omitted local view simulates unavailable source. The installed source remains readable.'});}}\nreport.push({label:'worker-tools-unavailable',decision:'Read the complete mode and leaves. Use sequential how, two design sketches and direct implementation only as reduced capability. Independent architect, arena and review remain blocked.',limit:'Simulated negative condition. Native collaboration tools remain exposed in this host. The no-spawn assignment is an enforced instruction boundary, not tool removal.'});\nconst ctx={owner:'synthetic',repo:'fixture',number:17,expectedHead:input};\nconst facts={context:ctx,mergeable:'MERGEABLE',mergeStateStatus:'CLEAN',reviewDecision:'APPROVED',headRefOid:input,headRefName:'fixture-head',baseRefName:'main',state:'OPEN',mergedAt:null,isDraft:false};\nconst row={kind:'open',context:ctx,facts,threads:[],reviewAutomationRunning:false,ci:{kind:'ci-clean',source:'gh-pr-checks',all:[{kind:'passed',name:'fixture-check',reportedState:'SUCCESS',description:'synthetic',link:'',workflow:'fixture'}],failed:[],pending:[],hadPreviousPassingCi:false,github:{kind:'allowed',basis:'merge-state',mergeStateStatus:'CLEAN',headRollupState:'SUCCESS'}}};\nconst events=[{schemaVersion:1,sequence:1,observedAt:'synthetic-input',mode:'single',kind:'STATUS',terminal:true,exitCode:0,reason:'status-only',rows:[row]},{schemaVersion:1,sequence:2,observedAt:'synthetic-input',mode:'queued-stack',kind:'WAITING',terminal:false,frontier:ctx,reason:{kind:'merge-queue',unmergedCount:1}}];\nawait writeFile(`${root}/watcher-fixtures.ndjson`,events.map(x=>JSON.stringify(x)).join('\\n')+'\\n');\nfor(const event of events){const classification=event.kind==='STATUS'&&event.reason==='status-only'?'Status query only. Readiness and merge unproven.':event.kind==='WAITING'&&!event.terminal&&event.reason.kind==='merge-queue'?'Babysit may report frontier merge-ready and stop its watcher. Shipping must wait for observed MERGED or non-null mergedAt. No merge is proven.':'Unknown';report.push({label:'watcher-event-inspection',kind:event.kind,terminal:event.terminal,reason:event.reason,classification,limit:'Generated inert fixture interpreted from read source types. No watcher or service emitted these events.'});}\nconst bindings=JSON.parse(await readFile(`${root}/bindings.json`,'utf8'));\nassert.equal(bindings.routes.length,23);assert.equal(bindings.principles.length,24);\nconst policies={\n'investigation':'Read-only cited answer. No PR, no architect absent a code-change handoff.',\n'bug-fix':'Direct reproduction, cause and same-surface proof precede delivery.',\n'perf-issue':'Matching-surface baseline and comparable post-fix measurements precede speed claims.',\n'hillclimb':'Frozen discriminating metric and target plus attempt floor. One change and measurement per iteration.',\n'runtime-forensics':'Live capture and authorized intervention. Diagnosis only, no inferred live proof.',\n 'trace-forensics':'Fixed captured artifact, queryable conversion and mapped hypothesis. No new capture or fix.',\n'feature':'Named data shape, how and architect, no-spawn owner returns diff for lead review.',\n'refactoring':'Pin behavior first. Structure changes, behavior does not.',\n'prototype':'Throwaway decision tool. No production implementation or delivery authorization.',\n'visual-parity':'Untouched baseline and actual screenshots with zero image diff. No source-only equivalence.',\n'authoring-a-skill':'Missing create-skill stays open. Provisional local draft is reduced capability.',\n'eval':'Organic blind candidates, discriminating fixture calibration, fresh blind judge and transcript checks.',\n'babysit':'Declared mode and finite budget. Stop at merge-ready, never infer merge authorization.',\n'shipping':'Independent exact-patch verdicts. Land contiguous verified root run only with merge authorization.',\n'autonomous-run':'Checkable predicate, bounded foreground fallback, no invented persistent wake.',\n'orchestrate':'Standing program only. Explicit outside-package store, immutable assignments and inspected inbox receipts.',\n'autopilot-full':'Independent PR owners, early ready PR only when authorized, root clean swarm gate before owner merge.',\n'autopilot-stack':'One root topology writer, linear reviewed chain, no owner or root merge under this route.',\n'session-pickup':'Read scoped history and reconcile full current state before continuing. Unknown outcomes block replay.',\n'pause-safely':'Explicit pause only. Observe worker stops, preserve artifacts and write a readback-verified handoff.',\n'multi-phase-plan':'Plan only. State then wait. One positional checker path and structural evidence limits.',\n'worktree-cleanup':'Audit buckets grant no deletion permission. Actual usage and ignored state must be checked.',\n'opening-a-pr':'Prepare title/body/base, complete review gates and inspect actual created draft or ready state. No automatic babysit.'};\nconst routeReport=[];\nfor(const route of bindings.routes){const raw=await readFile(`${root}/${route.stepsArtifact}`,'utf8');const name=route.path.split('/').at(-1).slice(0,-3);assert.ok(policies[name],name);routeReport.push({route:name,source:route.path,stepCount:raw.split('\\n').filter(x=>/^\\d+\\. /.test(x)).length,contract:policies[name],method:'complete source read and local routing inspection only',execution:name==='feature'?'local synthetic feature executed with review gates open':'Scenario contract inspected. Required live/control/worker/forge actions not performed.'});}\nawait writeFile(`${root}/route-report.json`,JSON.stringify(routeReport,null,2));\nawait writeFile(`${root}/contract-probes.json`,JSON.stringify(report,null,2));\nassert.equal(await Bun.file(`${root}/must-not-exist.tsv`).exists(),false);\nconsole.log(JSON.stringify({input,current,guardOutcomes:report.map(x=>({label:x.label,accepted:x.accepted,decision:x.decision??x.classification??x.reasons})),routesInspected:routeReport.length,principleBindingsRetained:bindings.principles.length,invalidLogAbsent:true}));\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/readback.json",
      "sha256": "110430029bec1e0558a9dbb23aaea98ec40698ef697e904b0cf7b51173b70a68",
      "bytes": 2521,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"receipt\": {\n    \"assignmentId\": \"fresh\",\n    \"workerId\": \"/root/fresh\",\n    \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n    \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n    \"requestedModel\": \"inherit-parent\",\n    \"actualModel\": \"unknown\",\n    \"requestedEffort\": \"inherit-parent\",\n    \"actualEffort\": \"unknown\",\n    \"status\": \"completed-local-artifacts-review-open\",\n    \"method\": \"native no-spawn delegate with direct local execution and sequential design fallback\",\n    \"artifacts\": [\n      {\n        \"path\": \"feature.diff\",\n        \"bytes\": 1124,\n        \"sha256\": \"ddad1f46a24a4d3406126d9051c953aedbb407cf139fa7b30adc6011af49286c\"\n      },\n      {\n        \"path\": \"feature/dashboard.mjs\",\n        \"bytes\": 551,\n        \"sha256\": \"0fe82aee099aa55540aa756a52705d0de9bb68e614964c3760f13852f35a7823\"\n      },\n      {\n        \"path\": \"verify-feature.mjs\",\n        \"bytes\": 1201,\n        \"sha256\": \"4324f625a66164647b4616ee0b317d4da431876caed7148617c28654a56a88c3\"\n      },\n      {\n        \"path\": \"commands/feature.json\",\n        \"bytes\": 569,\n        \"sha256\": \"9728283f6836d2bc4e288bb973dbd73c947a1484181e473e06c118c3c07aefd6\"\n      },\n      {\n        \"path\": \"design.md\",\n        \"bytes\": 3041,\n        \"sha256\": \"ec3ee812a6b3454c3a210ab33edd01300e0bed2c53aac35b872ea5836c391039\"\n      },\n      {\n        \"path\": \"checklist.md\",\n        \"bytes\": 7416,\n        \"sha256\": \"da04940a3d32d9e98cc4de225c3d8aaad5823d8ec77b599112223a9ce66170e7\"\n      },\n      {\n        \"path\": \"bindings.json\",\n        \"bytes\": 11819,\n        \"sha256\": \"7926901be982a0b74e04a071ea95a83e63032dc9d9ff0de8de4590eb75c75d12\"\n      },\n      {\n        \"path\": \"route-report.json\",\n        \"bytes\": 9317,\n        \"sha256\": \"d9ab9dd81b60b90e8c23dec3b362c7f45546878df44470b2b7cb502dfba79f1e\"\n      },\n      {\n        \"path\": \"contract-probes.json\",\n        \"bytes\": 5908,\n        \"sha256\": \"0e2f89afc1e3ec2fa31e79de4b70125e07de1fcc4d73a7d19070323308bda561\"\n      },\n      {\n        \"path\": \"decisions.tsv\",\n        \"bytes\": 293,\n        \"sha256\": \"b15661e765fc6f46ebd6c9857866da034ab21162c00ca38d180f85fa8bc0a4a4\"\n      }\n    ]\n  },\n  \"decisionLog\": \"ts\\tphase\\tdecision\\twhy\\tevidence\\tresult\\n2026-10-16T08:06:32Z\\tfeature\\tAdded grouped order summaries\\tOne Map owns each status summary\\t/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/commands/feature.json\\tlocal checks green; independent review open\\n\",\n  \"sourceSnapshots\": 73,\n  \"correctedInputTreeFiles\": 112\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/route-report.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/route-report.json",
      "sha256": "d9ab9dd81b60b90e8c23dec3b362c7f45546878df44470b2b7cb502dfba79f1e",
      "bytes": 9317,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "[\n  {\n    \"route\": \"prototype\",\n    \"source\": \"skills/poteto-mode/playbooks/prototype.md\",\n    \"stepCount\": 6,\n    \"contract\": \"Throwaway decision tool. No production implementation or delivery authorization.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"babysit\",\n    \"source\": \"skills/poteto-mode/playbooks/babysit.md\",\n    \"stepCount\": 9,\n    \"contract\": \"Declared mode and finite budget. Stop at merge-ready, never infer merge authorization.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"shipping\",\n    \"source\": \"skills/poteto-mode/playbooks/shipping.md\",\n    \"stepCount\": 9,\n    \"contract\": \"Independent exact-patch verdicts. Land contiguous verified root run only with merge authorization.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"investigation\",\n    \"source\": \"skills/poteto-mode/playbooks/investigation.md\",\n    \"stepCount\": 4,\n    \"contract\": \"Read-only cited answer. No PR, no architect absent a code-change handoff.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"bug-fix\",\n    \"source\": \"skills/poteto-mode/playbooks/bug-fix.md\",\n    \"stepCount\": 6,\n    \"contract\": \"Direct reproduction, cause and same-surface proof precede delivery.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"perf-issue\",\n    \"source\": \"skills/poteto-mode/playbooks/perf-issue.md\",\n    \"stepCount\": 6,\n    \"contract\": \"Matching-surface baseline and comparable post-fix measurements precede speed claims.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"hillclimb\",\n    \"source\": \"skills/poteto-mode/playbooks/hillclimb.md\",\n    \"stepCount\": 8,\n    \"contract\": \"Frozen discriminating metric and target plus attempt floor. One change and measurement per iteration.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"runtime-forensics\",\n    \"source\": \"skills/poteto-mode/playbooks/runtime-forensics.md\",\n    \"stepCount\": 5,\n    \"contract\": \"Live capture and authorized intervention. Diagnosis only, no inferred live proof.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"trace-forensics\",\n    \"source\": \"skills/poteto-mode/playbooks/trace-forensics.md\",\n    \"stepCount\": 6,\n    \"contract\": \"Fixed captured artifact, queryable conversion and mapped hypothesis. No new capture or fix.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"feature\",\n    \"source\": \"skills/poteto-mode/playbooks/feature.md\",\n    \"stepCount\": 8,\n    \"contract\": \"Named data shape, how and architect, no-spawn owner returns diff for lead review.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"local synthetic feature executed with review gates open\"\n  },\n  {\n    \"route\": \"refactoring\",\n    \"source\": \"skills/poteto-mode/playbooks/refactoring.md\",\n    \"stepCount\": 8,\n    \"contract\": \"Pin behavior first. Structure changes, behavior does not.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"visual-parity\",\n    \"source\": \"skills/poteto-mode/playbooks/visual-parity.md\",\n    \"stepCount\": 5,\n    \"contract\": \"Untouched baseline and actual screenshots with zero image diff. No source-only equivalence.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"authoring-a-skill\",\n    \"source\": \"skills/poteto-mode/playbooks/authoring-a-skill.md\",\n    \"stepCount\": 4,\n    \"contract\": \"Missing create-skill stays open. Provisional local draft is reduced capability.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"eval\",\n    \"source\": \"skills/poteto-mode/playbooks/eval.md\",\n    \"stepCount\": 7,\n    \"contract\": \"Organic blind candidates, discriminating fixture calibration, fresh blind judge and transcript checks.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"autonomous-run\",\n    \"source\": \"skills/poteto-mode/playbooks/autonomous-run.md\",\n    \"stepCount\": 6,\n    \"contract\": \"Checkable predicate, bounded foreground fallback, no invented persistent wake.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"orchestrate\",\n    \"source\": \"skills/poteto-mode/playbooks/orchestrate.md\",\n    \"stepCount\": 7,\n    \"contract\": \"Standing program only. Explicit outside-package store, immutable assignments and inspected inbox receipts.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"autopilot-full\",\n    \"source\": \"skills/poteto-mode/playbooks/autopilot-full.md\",\n    \"stepCount\": 7,\n    \"contract\": \"Independent PR owners, early ready PR only when authorized, root clean swarm gate before owner merge.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"autopilot-stack\",\n    \"source\": \"skills/poteto-mode/playbooks/autopilot-stack.md\",\n    \"stepCount\": 8,\n    \"contract\": \"One root topology writer, linear reviewed chain, no owner or root merge under this route.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"session-pickup\",\n    \"source\": \"skills/poteto-mode/playbooks/session-pickup.md\",\n    \"stepCount\": 5,\n    \"contract\": \"Read scoped history and reconcile full current state before continuing. Unknown outcomes block replay.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"pause-safely\",\n    \"source\": \"skills/poteto-mode/playbooks/pause-safely.md\",\n    \"stepCount\": 4,\n    \"contract\": \"Explicit pause only. Observe worker stops, preserve artifacts and write a readback-verified handoff.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"multi-phase-plan\",\n    \"source\": \"skills/poteto-mode/playbooks/multi-phase-plan.md\",\n    \"stepCount\": 7,\n    \"contract\": \"Plan only. State then wait. One positional checker path and structural evidence limits.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"worktree-cleanup\",\n    \"source\": \"skills/poteto-mode/playbooks/worktree-cleanup.md\",\n    \"stepCount\": 6,\n    \"contract\": \"Audit buckets grant no deletion permission. Actual usage and ignored state must be checked.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  },\n  {\n    \"route\": \"opening-a-pr\",\n    \"source\": \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"stepCount\": 0,\n    \"contract\": \"Prepare title/body/base, complete review gates and inspect actual created draft or ready state. No automatic babysit.\",\n    \"method\": \"complete source read and local routing inspection only\",\n    \"execution\": \"Scenario contract inspected. Required live/control/worker/forge actions not performed.\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/run-commands.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/run-commands.mjs",
      "sha256": "c1bdd3d2acf2081f6e4b7ad602696730c58fa176f8417b9176af42b5442bdfef",
      "bytes": 2920,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "import {readFile,writeFile,mkdir} from 'node:fs/promises';\nconst root=import.meta.dir;\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nawait mkdir(`${root}/commands`,{recursive:true});\nconst records=[];\nfunction run(name,argv,cwd=root){const r=Bun.spawnSync(argv,{cwd,env:{...process.env,BUN_CONFIG_NO_AUTO_INSTALL:'1'}});const record={name,argv,cwd,exitCode:r.exitCode,stdout:r.stdout.toString(),stderr:r.stderr.toString()};records.push(record);console.log(JSON.stringify(record));return record;}\nrun('input-commit',['git','show','--no-patch','--format=%H','352ef9629c424778feb077712c2e7b62bb46e5ce']);\nrun('current-head',['git','rev-parse','HEAD']);\nrun('input-tree',['git','ls-tree','--name-only','352ef9629c424778feb077712c2e7b62bb46e5ce','committed-inputs/']);\nrun('bun-version',['bun','--version']);\nrun('feature',['bun','--no-install',`${root}/verify-feature.mjs`]);\nconst diff=run('feature-diff',['git','diff','--no-index','--',`${root}/feature/dashboard.before.mjs`,`${root}/feature/dashboard.mjs`]);\nawait writeFile(`${root}/feature.diff`,diff.stdout);\nrun('bootstrap',['bun','--no-install','-e',`import {ensureDependenciesInstalled} from ${JSON.stringify(pkg+'/skills/poteto-mode/scripts/bootstrap.ts')}; ensureDependenciesInstalled();`]);\nrun('orchestrate-setup',['bun','--no-install',`${pkg}/skills/poteto-mode/scripts/orch/orch.ts`,'--store',`${root}/owned-store`,'inbox','drain','--peek','--json']);\nrun('watcher-setup',['bun','--no-install',`${pkg}/skills/poteto-mode/scripts/watch-pr/watch-pr`,'--owner','synthetic','--repo','fixture','--queued-stack','--stack-prs','17','--head','17=352ef9629c424778feb077712c2e7b62bb46e5ce','--max-polls','1','--timeout','1'],pkg);\nrun('check-plan-unreadable',['bun','--no-install',`${pkg}/skills/poteto-mode/scripts/check-plan.mjs`,`${root}/absent-plan.md`]);\nrun('check-plan-nonplan',['bun','--no-install',`${pkg}/skills/poteto-mode/scripts/check-plan.mjs`,`${root}/checklist.md`]);\nrun('decision-log',['bash',`${pkg}/skills/show-me-your-work/scripts/log.sh`,`${root}/decisions.tsv`,'feature','Added grouped order summaries','One Map owns each status summary',`${root}/commands/feature.json`,'local checks green; independent review open']);\nrun('decision-log-invalid',['bash',`${pkg}/skills/show-me-your-work/scripts/log.sh`,`${root}/must-not-exist.tsv`,'probe','invalid\\ncell','reject before write','fixture','open']);\nrun('decision-log-formula',['bash',`${pkg}/skills/show-me-your-work/scripts/log.sh`,`${root}/formula-probe.tsv`,'probe','=1+1','formula prefix protection','local fixture','open']);\nfor(const record of records)await writeFile(`${root}/commands/${record.name}.json`,JSON.stringify(record,null,2));\nawait writeFile(`${root}/commands/all.json`,JSON.stringify(records,null,2));\nconsole.log(await readFile(`${root}/decisions.tsv`,'utf8'));\nconsole.log(await readFile(`${root}/formula-probe.tsv`,'utf8'));\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/verify-feature.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/verify-feature.mjs",
      "sha256": "4324f625a66164647b4616ee0b317d4da431876caed7148617c28654a56a88c3",
      "bytes": 1201,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "import assert from 'node:assert/strict';\nimport {readFile} from 'node:fs/promises';\nimport {summarizeOrders,visible,exportCsv} from './feature/dashboard.mjs';\nimport * as baseline from './feature/dashboard.before.mjs';\nconst orders=JSON.parse(await readFile(new URL('./feature/orders.json',import.meta.url),'utf8'));\nconst before=JSON.stringify(orders);\nassert.deepEqual(summarizeOrders(orders),[{status:'open',count:2,total:12.5},{status:'closed',count:1,total:4}]);\nassert.deepEqual(summarizeOrders(visible(orders,'open')),[{status:'open',count:2,total:12.5}]);\nassert.deepEqual(summarizeOrders([]),[]);\nassert.deepEqual(summarizeOrders([{status:'__proto__',total:3},{status:'__proto__',total:2},{status:'constructor',total:0}]),[{status:'__proto__',count:2,total:5},{status:'constructor',count:1,total:0}]);\nassert.equal(JSON.stringify(orders),before);\nassert.deepEqual(visible(orders,'open'),baseline.visible(orders,'open'));\nassert.equal(exportCsv(orders),baseline.exportCsv(orders));\nassert.equal(typeof baseline.summarizeOrders,'undefined');\nconsole.log(JSON.stringify({summaries:summarizeOrders(orders),inputUnchanged:true,existingExportsUnchanged:true,baselineFeatureAbsent:true,checks:8}));\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/watcher-fixtures.ndjson",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/watcher-fixtures.ndjson",
      "sha256": "0aa4f2ceb952918a58a771651caaeb33d467cddc71e1eaa6642e7398c0ce4ad2",
      "bytes": 1328,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\"schemaVersion\":1,\"sequence\":1,\"observedAt\":\"synthetic-input\",\"mode\":\"single\",\"kind\":\"STATUS\",\"terminal\":true,\"exitCode\":0,\"reason\":\"status-only\",\"rows\":[{\"kind\":\"open\",\"context\":{\"owner\":\"synthetic\",\"repo\":\"fixture\",\"number\":17,\"expectedHead\":\"352ef9629c424778feb077712c2e7b62bb46e5ce\"},\"facts\":{\"context\":{\"owner\":\"synthetic\",\"repo\":\"fixture\",\"number\":17,\"expectedHead\":\"352ef9629c424778feb077712c2e7b62bb46e5ce\"},\"mergeable\":\"MERGEABLE\",\"mergeStateStatus\":\"CLEAN\",\"reviewDecision\":\"APPROVED\",\"headRefOid\":\"352ef9629c424778feb077712c2e7b62bb46e5ce\",\"headRefName\":\"fixture-head\",\"baseRefName\":\"main\",\"state\":\"OPEN\",\"mergedAt\":null,\"isDraft\":false},\"threads\":[],\"reviewAutomationRunning\":false,\"ci\":{\"kind\":\"ci-clean\",\"source\":\"gh-pr-checks\",\"all\":[{\"kind\":\"passed\",\"name\":\"fixture-check\",\"reportedState\":\"SUCCESS\",\"description\":\"synthetic\",\"link\":\"\",\"workflow\":\"fixture\"}],\"failed\":[],\"pending\":[],\"hadPreviousPassingCi\":false,\"github\":{\"kind\":\"allowed\",\"basis\":\"merge-state\",\"mergeStateStatus\":\"CLEAN\",\"headRollupState\":\"SUCCESS\"}}}]}\n{\"schemaVersion\":1,\"sequence\":2,\"observedAt\":\"synthetic-input\",\"mode\":\"queued-stack\",\"kind\":\"WAITING\",\"terminal\":false,\"frontier\":{\"owner\":\"synthetic\",\"repo\":\"fixture\",\"number\":17,\"expectedHead\":\"352ef9629c424778feb077712c2e7b62bb46e5ce\"},\"reason\":{\"kind\":\"merge-queue\",\"unmergedCount\":1}}\n"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/worker-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/worker-receipt.json",
      "sha256": "42884de61b014e652696d7cf2497e58b32066365550393cebf6e6c5bff969743",
      "bytes": 1993,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "{\n  \"assignmentId\": \"fresh\",\n  \"workerId\": \"/root/fresh\",\n  \"inputRevision\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n  \"currentHead\": \"352ef9629c424778feb077712c2e7b62bb46e5ce\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"status\": \"completed-local-artifacts-review-open\",\n  \"method\": \"native no-spawn delegate with direct local execution and sequential design fallback\",\n  \"artifacts\": [\n    {\n      \"path\": \"feature.diff\",\n      \"bytes\": 1124,\n      \"sha256\": \"ddad1f46a24a4d3406126d9051c953aedbb407cf139fa7b30adc6011af49286c\"\n    },\n    {\n      \"path\": \"feature/dashboard.mjs\",\n      \"bytes\": 551,\n      \"sha256\": \"0fe82aee099aa55540aa756a52705d0de9bb68e614964c3760f13852f35a7823\"\n    },\n    {\n      \"path\": \"verify-feature.mjs\",\n      \"bytes\": 1201,\n      \"sha256\": \"4324f625a66164647b4616ee0b317d4da431876caed7148617c28654a56a88c3\"\n    },\n    {\n      \"path\": \"commands/feature.json\",\n      \"bytes\": 569,\n      \"sha256\": \"9728283f6836d2bc4e288bb973dbd73c947a1484181e473e06c118c3c07aefd6\"\n    },\n    {\n      \"path\": \"design.md\",\n      \"bytes\": 3041,\n      \"sha256\": \"ec3ee812a6b3454c3a210ab33edd01300e0bed2c53aac35b872ea5836c391039\"\n    },\n    {\n      \"path\": \"checklist.md\",\n      \"bytes\": 7416,\n      \"sha256\": \"da04940a3d32d9e98cc4de225c3d8aaad5823d8ec77b599112223a9ce66170e7\"\n    },\n    {\n      \"path\": \"bindings.json\",\n      \"bytes\": 11819,\n      \"sha256\": \"7926901be982a0b74e04a071ea95a83e63032dc9d9ff0de8de4590eb75c75d12\"\n    },\n    {\n      \"path\": \"route-report.json\",\n      \"bytes\": 9317,\n      \"sha256\": \"d9ab9dd81b60b90e8c23dec3b362c7f45546878df44470b2b7cb502dfba79f1e\"\n    },\n    {\n      \"path\": \"contract-probes.json\",\n      \"bytes\": 5908,\n      \"sha256\": \"0e2f89afc1e3ec2fa31e79de4b70125e07de1fcc4d73a7d19070323308bda561\"\n    },\n    {\n      \"path\": \"decisions.tsv\",\n      \"bytes\": 293,\n      \"sha256\": \"b15661e765fc6f46ebd6c9857866da034ab21162c00ca38d180f85fa8bc0a4a4\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode.result.md",
      "sha256": "0b068e90766a48986d98d78949586a39df72837c26b18131a38df71d18538fc4",
      "bytes": 19337,
      "owners": [
        "grades-native-08.json#5"
      ],
      "text": "# fresh-worker-mode\n\n## Supplied input\n\nThe case contract below is synthetic task input. Its package source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. This case used only the installed package at /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. The input repository revision is distinct from that package source freeze.\n\n```json\n{\n  \"id\": \"fresh-worker-mode\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/SKILL.md\"\n  ],\n  \"prompt\": \"Invoke /poteto-mode for a scoped nontrivial feature. Give a fresh worker this mode and require its chosen playbook, applied principle leaves, throughput checkpoint and evidence. Repeat with worker tools unavailable and with the mode or an applied leaf unavailable. Exercise the 23 playbook route contracts, a no-spawn worker, helper setup failure, a stale full head or missing artifact, and an authorized local checklist when no todo tool exists. Use fixtures for helper boundaries; do not contact a live forge or install dependencies.\",\n  \"requirements\": [\n    \"Observed read of the complete mode, chosen playbook and every applied principle leaf\",\n    \"Authorized independent worker spawn and inspected result for full behavior\",\n    \"Immutable scoped assignment, exact input revision, separate write ownership and requested versus observed model records\",\n    \"Four throughput checkpoint items and evidence attached to claims\",\n    \"User authorization and host permissions constrain all operations\",\n    \"Preserve all 23 playbook routes and 24 principle bindings with source-faithful aliases and meanings\",\n    \"No-spawn worker owns its scoped diff and returns it to the lead without nested waiting; required independent review stays explicit\",\n    \"Read real helper contracts before invocation; use exact log positional arguments, explicit outside-package store, watcher heads and finite budgets, and one check-plan positional path\",\n    \"Inspect watcher event kind, terminal and reason; status-only exit 0 and non-terminal queued waiting never prove merged state\",\n    \"Reject stale assignment identities or full input/current head revisions and missing artifacts before integration; ledger labels do not prove verification\",\n    \"Use verbatim chosen-playbook steps in todo tools or an authorized local checklist with a disclosed reduced binding\",\n    \"Local presence closes reference deferrals only; preserve companion, setup, review, external-action and independent-worker limits\"\n  ],\n  \"expectedFull\": \"A fresh worker reads the full mode and applied leaves, follows the selected playbook with verbatim step todos or explicit skips, and returns blocking first steps, independent workstreams, shared mutable state and smallest safe decomposition with reasons for any n/a item. The coordinator inspects artifacts and reports evidence, decisions, limitations and only principles read in this session. The no-spawn delegate returns its own scoped diff for lead review. The coordinator reads selected helper contracts and inspects actual receipts, validates assignment and current full head against existing artifacts, and preserves each playbook delivery exception. All 23 routes and 24 principle bindings remain available as instructions.\",\n  \"expectedReduced\": \"Without authorized independent workers, the same full reads and checkpoint apply to authorized sequential work. The result explicitly records reduced capability, unverified model diversity and absent independent review or background execution. Missing external companion skills are visible and their dependent gates remain blocked. Local checklist fallback retains verbatim steps and explicit skips. Inert helper fixtures support structural contracts only. An isolated snapshot run supports only its tested revision and never this caller or current host.\",\n  \"expectedBlocked\": \"If the mode, chosen playbook or applied principle leaf cannot be read, stop dependent work and name the missing reference. Denied execution or writes stay blocked; autonomy language grants no external permission, installation or controller takeover. Missing pinned dependencies stop dependency-backed helpers without install or bootstrap bypass. Stale identities, changed heads, missing artifacts, denied action permission or unknown interrupted outcome block affected integration or replay. Required independent review remains blocked even if a no-spawn worker can prepare a diff.\",\n  \"forbiddenClaims\": [\n    \"A summary substitutes for reading the complete mode or applied leaves\",\n    \"Sequential role switching is independent worker review\",\n    \"Requested models prove actual model identity or diversity\",\n    \"Metadata registers a custom agent, mode or supported host capability\",\n    \"Missing companion skills or pending helpers are silently satisfied\",\n    \"Upstream autonomy authorizes external writes or bypasses permissions\",\n    \"Structural validation proves host behavior\",\n    \"Bundled helper existence or isolated snapshot tests prove this caller executes on either host\",\n    \"Status-only exit 0, ledger labels or queued WAITING prove a merge or an independent verdict\",\n    \"Helper deadlines guarantee a strict wall-clock cutoff without observed host controls\",\n    \"Historical deferral prose excuses skipping a present required contract\",\n    \"The no-spawn worker exception waives required independent lead review\",\n    \"An audit bucket or a parked gate default authorizes deletion, setup or external writes\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/poteto-mode.json\"\n}\n```\n\n## Actual output\n\nThe no-spawn delegate added `summarizeOrders(orders)` to the copied synthetic dashboard module. Dashboard consumers receive per-status counts and totals in first-seen order. The next maintainer inherits one Map-based owner of aggregation and a direct rerunnable verification script.\n\nThe function works against the copied fixture in the observed local run. This is not a full mode acceptance claim. Architect competition and independent review remain open. No PR, commit, push, install, schedule, settings change or service action occurred.\n\nThe local design compared a Map accumulator with unique-status collection followed by repeated filtering. The Map shape became the base because it owns count and total together. These are sequential sketches. They are not independent candidates, a fresh cross-judge or verified model diversity.\n\n```text\n{\"summaries\":[{\"status\":\"open\",\"count\":2,\"total\":12.5},{\"status\":\"closed\",\"count\":1,\"total\":4}],\"inputUnchanged\":true,\"existingExportsUnchanged\":true,\"baselineFeatureAbsent\":true,\"checks\":8}\n```\n\nRun `bun --no-install /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/verify-feature.mjs` to repeat the actual feature check. The eight checks cover literal summary results, filtered input, empty input, reserved-looking status keys, non-mutation, unchanged filter behavior, unchanged exporter behavior and absence of the feature from the copied baseline. The exporter has a pre-existing CSV quoting defect outside this scoped feature. It remains unchanged.\n\n## Identity and source evidence\n\nThe immutable assignment is `fresh-worker-mode/assignment.json`, id `fresh`, owner `fresh`. The native worker identity is `/root/fresh`. The lead dispatched this fresh delegate. This delegate invoked zero spawns and zero nested waits.\n\nThe observed full input and current HEAD are both `352ef9629c424778feb077712c2e7b62bb46e5ce`. Commands and outputs are preserved in `commands/input-commit.json`, `commands/current-head.json` and `commands/input-tree-corrected.json`. The first relative input-tree query returned empty because it ran from the case subdirectory. The corrected repository-root query lists the committed inputs. That observation-method correction is retained instead of calling the inputs missing.\n\n`worker-receipt.json` records exact artifacts and SHA-256 digests. Its completed-local label does not prove independent review or integration. The lead must inspect the actual diff and verification before accepting it. Output artifacts are uncommitted and are not claimed to belong to the input revision.\n\nRequested model and effort are inherit-parent. Actual model and effort are unknown because the worker operation supplied no observed runtime model identity. Diversity remains unverified.\n\n`source-reads/manifest.json` records 73 actual file reads and byte-identical local snapshots. It includes the complete mode, all 23 route playbooks, all 24 principle leaves, role prompt, host/ownership/model/assignment contracts, how, architect, arena, unslop and selected helper sources. The source freeze is the supplied package identifier. These reads alone do not establish package loading, host behavior or a behavioral pass.\n\n## Throughput checkpoint\n\n- Blocking first steps. The full mode, Feature, how, architect, arena and applicable leaves were read before feature edits. Assignment and current revision were checked with git before helper probes and returned with the result. The lead verified the input revision before dispatch.\n- Independent workstreams. n/a because this is one code-coupled feature assigned to a no-spawn delegate. Required independent design and review stay open for the lead.\n- Shared mutable state. This delegate exclusively writes this case directory and its root result file. Shared inputs and the installed package remain read-only.\n- Smallest safe decomposition. One owner reads and designs, adds one pure grouped-summary function, verifies it, and returns the diff. Extra code writers would share one small module without reducing the dependency chain.\n\nThe checkpoint is retained in `checklist.md`. The final boundary keeps the same one-owner decomposition and hands independent review to the lead.\n\n## Playbook and principle bindings\n\n`checklist.md` starts with all eight Feature steps and sub-items copied verbatim. Its later dispositions retain explicit skips. No todo operation is exposed, so the authorized local Markdown checklist is a reduced tool binding. Architect and Arena phase dispositions are also retained.\n\n`bindings.json` preserves all 23 exact playbook paths and all 24 principle names, aliases and meanings extracted from the complete mode. `route-report.json` records each route's steps, delivery exception and permission boundary. The 23 route exercises are source-contract inspection, not 23 executed feature, cleanup, shipping, profiling or autonomous workflows. Such operations need their concrete prerequisites and authorization. Local presence closes the historical reference-deferral question only.\n\nApplied leaves read in full this session and their decisions are listed below.\n\n- Model the Domain selected a Map keyed by status before writing logic.\n- Build the Lever produced `verify-feature.mjs` and the rerunnable contract guard script.\n- Prove It Works required importing and calling the real modified module, then reading actual command output.\n- Test Behavior, Not Implementation required literal expected arrays and preserved caller-visible behavior.\n- Separate Before Serializing Shared State retained distinct case ownership with no shared package or fixture mutation.\n- Sequence Work into Verifiable Units kept the local addition and its check together. Commits and rebase were explicitly skipped because authorization forbids them.\n- Exhaust the Design Space produced the two whole-shape sequential sketches. The mandatory independent design method remains unsatisfied.\n\nOther captured leaves remain available as source instructions. Capturing them does not mean every principle was applied. Unslop governed the reports. Technical-writing was read for this document. The external create-skill companion is unavailable within the permitted package-only workflow. Its authoring fallback contract was read; no personal skill was authored. External deslop is absent and no replacement review was authorized. No no-comments independent reviewer ran. Those delivery gates remain open.\n\n## Variants and actual tools\n\n| Variant | Actual action or response | Evidence and limit |\n| --- | --- | --- |\n| Fresh native delegate | Lead spawned this worker with full mode instructions and exact immutable assignment. The delegate read the full mode and owns its local diff. | This report and worker-receipt.json are the returned result. Parent spawn receipt and lead result inspection are outside this delegate's write scope. |\n| No-spawn worker | The delegate implemented directly and returned its own diff. | feature.diff, design.md and commands/feature.json. No nested waiting. Lead independent review still required. |\n| Worker tools unavailable | Sequential how and design fallback response recorded. | contract-probes.json. Simulated negative condition. Collaboration tools remain exposed; this assignment forbids nested spawning. |\n| Mode unavailable | Read of the exact omitted local-view path failed ENOENT. Dependent work in this variant stops. | contract-probes.json. The installed mode remains readable. This is not host-enforced file denial. |\n| Applied leaf unavailable | Read of the omitted local-view model-the-domain path failed ENOENT. Dependent code work in this variant stops. | contract-probes.json. The installed leaf remains readable. This is a simulated absence. |\n| Helper setup failure | Real installed bootstrap, orch and watcher entry points fail with missing pinned Commander metadata. | commands/bootstrap.json, commands/orchestrate-setup.json, commands/watcher-setup.json. No install or bypass. |\n| Stale assignment identity | Local guard rejects an altered identity. | contract-probes.json. Synthetic altered result, not a stale native receipt. |\n| Stale input or current head | Local guard rejects changed full input SHA, changed full current SHA and a short SHA. | contract-probes.json. Actual current HEAD remains unchanged. |\n| Missing artifact | Local guard rejects an absent artifact even with valid labels. | contract-probes.json. No integration performed. |\n| Ledger label only | Local guard rejects a label without required method evidence. | contract-probes.json. A ledger row is not a verifier. |\n| No todo tool | Actual authorized local checklist created and read back. | checklist.md. Reduced tool binding preserves verbatim steps. |\n| Status-only exit 0 | Inert STATUS event remains a query observation, never readiness or merge proof. | watcher-fixtures.ndjson and contract-probes.json. Generated fixture only. |\n| Queued WAITING | Inert nonterminal WAITING with merge-queue reason can end Babysit's ready report, while Shipping still needs actual merged state. | Same fixtures. No live watcher receipt or service contact. |\n\nThe actual exposed file/execution binding is `functions.exec` calling `tools.exec_command`. Bun scripts read source files, wrote owned files, spawned bounded local commands and saved stdout, stderr and exit codes. Persistence was verified by reading saved receipts and logs. Collaboration was used only to send scoped progress to the lead. No exposed tool grants external authorization.\n\n## Helper commands and results\n\nThe log helper was called with exactly six positional arguments, starting with an explicit owned logfile. `decisions.tsv` was read back. The newline probe exits 1 and creates no logfile. The formula probe prefixes the formula-leading decision with a quote. Commands and readback are retained under `commands/`, `formula-probe.tsv` and `readback.json`.\n\nThe orch probe uses an explicit outside-package store at `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-08/fresh-worker-mode/owned-store` and `inbox drain --peek --json`. Bootstrap fails before inbox processing, so no peek receipt, durable drain receipt or initialized store is claimed. A later actual drain and ledger check are blocked by setup. The full real orch helper and store sources were read and preserved. The helper test source was inspected after the setup attempt, so this run does not claim a completed pre-execution test-contract review gate.\n\nThe watcher probe uses explicit synthetic owner/repo, queued PR list, a full 40-character expected head and finite budgets of one poll and one second. Real bootstrap fails before importing the CLI or contacting the forge. The tested input head is an inert fixture pin, not a remote head observation. The dependency gate stops further watcher execution. It does not prove a strict wall-clock deadline.\n\nThe plan checker was called with one positional path each time. An unreadable path exits 2. The Feature checklist exits 1 with `not a pstack multi-phase plan; leave other workflow plans unchanged`. That checker correctly does not certify this implementation checklist. No structural success is represented as runtime verification.\n\nAll command arrays, stdout, stderr and exit codes are preserved in `commands/all.json`. The diff command exits 1 because the two files differ. That exit code is expected and is not a test failure.\n\n## Limits and open gates\n\nNo native nested design workers or fresh judge ran under the no-spawn assignment. Parent inspection is required for independent review. No requested model was treated as observed. No private or unrelated history was read. The scoped conversation is visible, but a complete exported native transcript is unavailable to this delegate. The source snapshots and local command records preserve actual file content and process output; they are not a fabricated full native transcript.\n\nAll complete route documents are locally present. That resolves reference availability only. It does not satisfy companion execution, dependency setup, external authorization, independent design review, real-surface controls, model diversity, persistent wake or a clean shipping verdict.\n\nNo full host behavior claim or self-assigned grade is made. The local feature has direct observed evidence. The reduced design method and blocked delivery gates remain explicit.\n\n## Attention\n\nreviewed by unknown\n\nIndependent cross-model trail review is blocked for this no-spawn delegate. The lead must inspect the diff, script and actual output. The complete native transcript export is unavailable. Helper setup is a real block. Negative capability views and watcher events are simulated. The existing CSV quoting defect remains outside this scoped feature.\n\n## Coordinator inspection after worker return\n\nThe root independently inspected feature.diff, the complete verification script, source code, command records, contract probes and returned result. It reran `bun --no-install fresh-worker-mode/verify-feature.mjs`, which exited 0. [lead-verification.command.json](fresh-worker-mode/lead-verification.command.json) preserves that output. [lead-review.json](fresh-worker-mode/lead-review.json) validates assignment fresh against /root/fresh, both full input/current SHA values and all 10 returned artifact digests. This supplies independent lead review of the actual local diff. Independent design competition and cross-model review remain open.\n\nThe synthetic contract guard checks a method string and file presence. The string alone cannot establish execution. The root inspected actual command output and independently reran the feature instead of trusting that label. Those guard probes remain structural demonstrations, not native stale-worker or host-acceptance receipts.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs",
      "owner": "grades-native-08.json#5",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/feature/orders.json",
      "owner": "grades-native-08.json#5",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/input.json",
      "owner": "grades-native-08.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/source-reads",
      "owner": "grades-native-08.json#5",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/feature/dashboard.before.mjs",
      "owner": "grades-native-08.json#5",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/feature/orders.json",
      "owner": "grades-native-08.json#5",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/input.json",
      "owner": "grades-native-08.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-08/fresh-worker-mode/source-reads",
      "owner": "grades-native-08.json#5",
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
