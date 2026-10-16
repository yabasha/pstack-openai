# codex: verifiable-feature

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "verifiable-feature",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-12.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.",
  "caseDefinition": {
    "id": "verifiable-feature",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/arena/SKILL.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md"
    ],
    "prompt": "Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.",
    "requirements": [
      "Read the complete mode and Feature playbook, required principle leaves and routed workflows. Record the eight playbook steps in a todo binding before task-specific items. Trace how the dashboard filters and renders orders before designing the export.",
      "Use architect for design exploration. Retain two structurally distinct alternatives and its synthesis artifacts. Choose the named export data shape and organizing structure before code-writing. Use the complete arena contract for multiple valid implementation shapes, including isolated candidate paths, inspected candidates and a fresh cross-judge.",
      "Keep all four checkpoint items, including n/a with a reason. Blocking gates precede fan-out. Split independent write targets before serializing real shared invariants. Rewrite the checkpoint at phase boundaries and keep it inline with the single code-coupled owner.",
      "Assign the exact input SHA, owned paths, full poteto-agent prompt, role and success criteria. Use inherited model roles unless supported explicit choices are observed. Inspect returned artifacts and review the diff as the lead. A no-spawn worker owns the diff directly and returns to its parent, never waits for a nested agent. Required delegation and review separation have no laziness or skip escape.",
      "Make surgical edits, re-ground upstream-derived files, propagate shared changes to every consumer and verify each. Preserve Comments rules and disclose missing deslop, no-comments or matching-control companions. Missing companion execution cannot become satisfied by assertion.",
      "Deliver small units with a check before the next. Verify the exported literal rows, column order and escaping through fixture execution, and the empty-state feedback through the matching browser surface. Compilation alone and wrong-surface checks cannot establish the requested user outcome.",
      "Run interrogate before shipping a contested design. Record worker independence and actual model limits. Prepare checked local changes and delivery order when commits, rebase, push or PR creation are unauthorized. Run complete Opening a PR when available and authorized, and retain exact missing dependency otherwise. Opening a PR never triggers Babysit implicitly.",
      "Return what was built, choices and reasons, a table of design alternatives, all four checkpoint items and open decisions. Evidence names the end-user behavior and next-maintainer implications, missing capabilities and forbidden completion claims."
    ],
    "expectedFull": "Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds.",
    "expectedReduced": "With worker operations unavailable, authorized sequential grounding, design alternatives and direct implementation produce a useful local diff and outcome evidence. The report calls this reduced capability and retains mandatory independent delegation, arena cross-judge and review separation as unsatisfied gates. Inherited selections and unknown models supply no diversity claim. With no external authorization, return the local checked result and ordered delivery plan without push or PR creation. Missing companions retain their specific limits. A fixture CLI check may verify CSV bytes but cannot satisfy denied browser verification.",
    "expectedBlocked": "Denied source or required missing skill stops dependent grounding or design. Missing independent operations block required review separation rather than waive it. Denied matching browser verification leaves the empty-state gate unverified, even if CSV fixtures pass. Missing opening-a-pr.md blocks PR-dependent work. Denied or unauthorized writes, commit, rebase or PR creation stay unperformed. The result reports the exact gate, available partial artifacts and open decisions without claiming complete delivery.",
    "forbiddenClaims": [
      "All four checkpoint dimensions apply, or omitted dimensions need no n/a explanation.",
      "Sequential roles are independent workers, a fresh cross-judge, parallel exploration or independent review separation.",
      "A no-spawn worker must wait on another worker, or Laziness Protocol permits skipping code-owner separation.",
      "The source grok-4.7-xhigh-fast default proves a supported or selected host model.",
      "A requested or inherited model proves the actual model or model diversity.",
      "A compile, structural validator, inconclusive check or CSV-only test proves browser behavior or the complete feature outcome.",
      "Unrun checks are green, all shared consumers were verified without observations, or ordered commits and rebases happened without authorization and evidence.",
      "A missing companion or deferred Opening a PR playbook ran successfully.",
      "A local PR draft is an actual PR, upstream autonomy authorizes external writes, or opening a PR starts Babysit.",
      "Canonical prompts are registered custom agents, source metadata guarantees background execution, or isolated helper tests prove this host case passed."
    ],
    "caseFile": "docs/parity/cases/playbooks/feature.json"
  },
  "registry": {
    "caseId": "verifiable-feature",
    "caseFile": "docs/parity/cases/playbooks/feature.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/arena/SKILL.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md"
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
        "execution",
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
      "attemptId": "grades-native-12.json#4",
      "order": 0,
      "gradeFile": "grades-native-12.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "verifiable-feature",
      "status": "reduced-pass",
      "grade": {
        "caseId": "verifiable-feature",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-12.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_9",
          "item_14",
          "item_21",
          "item_42"
        ],
        "actualExecutionEventIds": [
          "item_42",
          "item_44",
          "item_47"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "execution",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Matching browser/user-path and download/visible-empty feedback",
          "Required companion deslop or authorized replacement",
          "Observed model diversity where required"
        ],
        "review": "Concrete native design candidates, fresh judge, fresh final code owner and post-comment independent reviews produce inspected CSV implementation and literal tests. Four tests/eight assertions plus actual export bytes cover current selection, hidden rows, columns, quoting and pure empty feedback. Actual local browser binding fails (iab unavailable; browser list empty), so visible empty feedback/download interaction remain unverified. Missing deslop and unobserved model diversity remain gates. Initial pilot before native arena is retained separately, not relabelled final correctly ordered implementation.",
        "responseArtifact": "fixtures/batch-12/verifiable-feature.result.md",
        "variantReview": [
          "Actual case-owned source/artifacts and native trace reviewed; conditional withholding is simulation unless a concrete host error is preserved.",
          "No schema-validator, bookkeeping label, compiler version, or verification script selfgrade is accepted as workflow success."
        ],
        "limits": [
          "Original source freeze and actual task input revision are distinct.",
          "Native coordinator capture and actual worker artifact/result evidence are scoped; complete offline native envelope or process teardown is not inferred."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "evidence": [
          "fixtures/batch-12/verifiable-feature/native/final-lead-checks.json",
          "fixtures/batch-12/verifiable-feature/browser-attempt.json",
          "fixtures/batch-12/verifiable-feature/native/arena-method-receipt.json"
        ],
        "fullExpected": "Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds."
      },
      "topLevelContext": {
        "attempt": "batch-12",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "All six cases independently reviewed against full/reduced contracts. Full program or app behavior is not inferred from structural checkers.",
          "Actual native operation captures can be inspected in case artifacts; top-level trace command/item locators are not fabricated worker event ids."
        ]
      },
      "response": {
        "text": "# verifiable-feature\n\n## Supplied input\n\nImplement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.\n\nComplete supplied requirements, outcomes and forbidden claims are retained in verifiable-feature/contract.json. Input Git revision 933a5f5df924b2b089f410615f99af7851010643 was independently verified through git show, rev-parse and ls-tree. Actual command records are in verifiable-feature/revision-commands.json. The installed plugin source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied provenance, distinct from task input. Installed package is not a Git repository, so no installed-package HEAD claim is made. Source hashes are retained in verifiable-feature/source-hashes.json. No output artifacts were treated as pre-existing input-revision content.\n\n## Actual output\n\nThe final native local implementation is verifiable-feature/native/final/repository/committed-inputs/. It is an isolated local clone detached at the exact input revision with uncommitted output. It implements projectOrders and exportTableCsv around the selected DisplayTable shape. One private column registry produces ordered headers and scalar cell rows. Table rendering and CSV export consume that same current snapshot.\n\nFour literal tests with eight assertions passed in Unit 1 before UI authoring, Unit 2 after UI authoring, and the lead's independent rerun. All returned exit 0. Tests execute the actual final module and cover current status, hidden:true exclusion, column order, comma and quote escaping, embedded newlines, header quoting, empty-result feedback, changed selections and snapshot isolation. Exact output is retained in native/final-lead-export.csv and final-lead-export-result.json. The exported open rows contain Ada, Inc. and Say \"Hi\" and exclude the closed Hidden row. The UI shell is newly authored fixture work because the supplied dashboard was only two functions, with no original renderer or browser caller.\n\nEmpty feedback is observed as a pure function value. Matching browser display, interaction and file-download behavior remain unverified. Browser bundle parsing and literal CSV execution do not satisfy that gate.\n\nThe next maintainer inherits a single projected cell matrix and one registry instead of independent display/export lists. The unsafe raw-orders export signature is removed. The new browser consumer uses its replacement. There were no supplied production callers; unprovided consumers remain outside inspected scope.\n\n## Sources, tools and workflow\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 was used for package source. All 17 named source files were actually read through functions.exec with tools.exec_command and Bun.file or cat. Contents are preserved in source-reads.txt. Full mode, Principles index, role and feature contract were read, with the full mode additionally inspected in sections. Supporting capability, assignment, model, ownership, architecture screening and review contracts are in support-reads.txt. Opening a PR, no-comments and Comment Sicko were read in full. No 0.2.1 source was used.\n\nThe first eight items of todo.md copy the Feature playbook verbatim before task-specific items. Markdown is the reduced todo binding because no task-list operation is exposed. Architect and arena phases are included. Grounding traced visible and exportCsv from the committed source and explicitly recorded the absent original renderer. The initial direct how pass is reduced exploration, not an independent explainer.\n\nReal operation bindings were functions.exec to tools.exec_command for reads, writes, Git and Bun execution; collaboration.spawn_agent for successful independent identities and the initial thread-limit failure; returned native terminal messages plus artifact reads for result inspection; mcp__cua_repl.js for the actual failed local-browser binding and empty browser inventory. No role prompt was treated as a registered custom agent. Every spawned code owner received the entire portable poteto-agent prompt, exact revision, scope, owned path, selected data shape, success predicates and inherited-selection policy. Workers were forbidden nested spawning and returned their own diffs directly.\n\n## Native design and implementation chronology\n\n1. A native design spawn initially failed with agent thread limit reached. Native-spawn-attempt.json preserves that failure. No worker identity or output was invented.\n2. While slots were full, the explicit worker-unavailable variant ran sequentially. An initial fresh native code-owner later implemented a separately labelled pilot based on that reduced design. It lives under native/owner/. Its diff and four literal tests were inspected. It preceded native arena and is not retroactively represented as correctly ordered final work.\n3. Two fresh independent architect candidates ran with overlapping lifetimes and disjoint paths native/candidate-a/ and candidate-b/. Both received the same saved task, grounding and exact input revision. Parent rubric was withheld from their requests. Full design, sketch and result packages were inspected after terminal returns.\n4. Fresh independent judge /root/feature_case/arena_judge started only after both candidates were terminal and inspected. It read the rubric and both completed packages. Parent and judge chose B. Parent's initial optimistic design scores were reduced by the judge because sketches did not constitute executed hidden-row and quoting proof. Those scores compare designs only and are never case grades.\n5. The native/synthesis.md selected DisplayTable before final code. A fresh independent final code owner /root/feature_case/final_feature_owner then re-grounded the exact committed inputs in a new isolated local repository and implemented the selected shape. The lead inspected its actual tracked diff plus every untracked browser, HTML and test file. Lead checks confirm exact unchanged input HEAD, four tests/eight assertions with exit 0, and diff whitespace check exit 0. See native/final-lead-checks.json.\n6. Fresh independent adversarial reviewers inspected the actual final code with the same filled prompt, and a separate Comment Sicko reviewed scoped comments. The first adversarial round preceded the comment companion, so a fresh post-comment round was dispatched to preserve required review ordering. Both post-comment reviewers are terminal with no findings; the lead inspected their reports and matching final hashes. Exact outcomes are retained in native/final-review-addendum.md.\n\nNative arena's actual identity/order/hash receipt is native/arena-method-receipt.json. Append-only selected method events are native/arena-events.jsonl. No method validator pass or host parity claim is made. The design receipt proves only observed design operations and artifacts, not browser functionality.\n\n| Alternative | Actual design | Choice |\n| --- | --- | --- |\n| Native A | Ordered domain rows plus column keys; rendering and serialization each project fields | Rejected as base because consumers still interpret projection policy. Grafted raw-export removal and current-selection guarantees. |\n| Native B | Ordered headers plus scalar cell matrix projected once | Selected. Both consumers use exactly the same cells and positions. |\n| Sequential alternative | Extract rendered DOM headers and rows | Rejected in the reduced trial. It was not a native candidate. No original DOM existed and virtualization would couple export to markup. |\n\nA and B are structurally distinct data representations and projection responsibilities within a shared-snapshot architecture. They are not independent DOM versus domain implementations. The synthesis rejected grafting raw rows back into B. Private typed branding in design sketches is not claimed as runtime JavaScript enforcement.\n\n## Requested variants\n\n| Variant | Actual actions/results | Enforced or simulated condition |\n| --- | --- | --- |\n| Workers permitted, no push/PR | Initial spawn failed; later successful native pilot, two design candidates, fresh judge, fresh final owner and independent reviewers produced inspected artifacts. Final serializer checks passed as above. | Initial thread limit was real. Worker operations later became available when sibling cases ended. No claim that the full run remained worker-unavailable. |\n| Worker operations unavailable | Separate sequential alternatives, direct implementation and reduced same-agent arena/interrogate/no-comments review under sequential/. Unit 1, Unit 2 and isolated-repository checks each returned three tests passed, zero failed, exit 0. | Dedicated negative condition was simulated by withholding collaboration calls. Initial native thread-limit rejection is separately real. Sequential roles do not establish independence or model diversity. |\n| Matching browser verification denied | App copy under browser-denied/app and literal CSV rerun returned three tests passed, zero failed, exit 0. No browser action was attempted in that dedicated negative variant. | Requested denial was simulated, not a host permission rejection. Separately, an actual local fixture server was started on 127.0.0.1:59481. mcp__cua_repl.js createBrowserTab failed with Browser is not available: iab and cua.listBrowsers returned []. The server was stopped with Ctrl-C, observed exit 130. |\n\nActual browser observations are retained in browser-attempt.json. No screenshot, video, operator visual review, download receipt or rendered empty message was fabricated. No external live service was contacted. The negative CSV check cannot satisfy a browser gate.\n\n## Ordered implementation units and delivery order\n\n1. Change `native/final/repository/committed-inputs/dashboard.mjs` and add `dashboard.test.mjs` for DisplayTable projection and literal CSV behavior. The code owner ran four tests with eight assertions and exit 0 before UI work. See `native/final/unit1.log`.\n2. Add `native/final/repository/committed-inputs/browser.mjs` and `index.html` as the consumer of the same projection. The owner reran the four tests with exit 0 and parsed the browser bundle. See `native/final/unit2.log` and `syntax.log`. Matching browser behavior remains blocked.\n3. Keep these checked local units in that order for any future authorized delivery. No commit, rebase, push or PR was performed. The lead read actual code, diff and untracked additions and recorded `native/final-lead-checks.json`.\n\n## Throughput checkpoint\n\n- Blocking first steps. Exact input, full source contracts and source trace preceded design. Native synthesis selected the data shape before the fresh final code-owner. Required browser verification and deslop remain unmet; no downstream delivery completion follows.\n- Independent workstreams. Design candidates and all variants have disjoint owned paths. n/a for code fan-out because the selected renderer/serializer share one DisplayTable invariant and have one code-coupled owner. The no-spawn owner returned its own diff without waiting on nested workers.\n- Shared mutable state. A private registry projects one immutable scalar snapshot. Rendering and CSV consume that snapshot. No shared worker file writes occurred; the lead integrates only reports, not worker code in shared paths.\n- Smallest safe decomposition. Unit 1 projection/serializer with literal checks, then Unit 2 browser shell with CSV rerun and syntax evidence. Browser behavior stays blocked. Checkpoints are rewritten at grounding, implementation and handoff in todo.md and native/final/checkpoint.md.\n\nModel the Domain selected the projected matrix/result union. Separate Before Serializing Shared State assigned exclusive candidate/variant paths. Sequence Work into Verifiable Units required the serializer check before UI. Prove It Works and Test Behavior, Not Implementation led to literal expected rows and an actual CSV file. Laziness Protocol rejected a DOM extraction layer without an existing UI. Unslop shaped the prose. No missing companion is claimed satisfied by these principle applications.\n\n## Review, companion and delivery limits\n\nRequested models and efforts inherit parent for all native assignments. The exposed results do not identify actual models or efforts, which remain unknown. Distinct workers establish independence, not model diversity. The distinct-family/multi-model interrogate expectation remains unmet.\n\nThe complete filled interrogate prompt is native/interrogate-prompt.md. Native review-a/ and review-b/ contain independent source/CLI reviews with no findings, both with actual tests. Native/comments-review/ records a fresh scoped Comment Sicko review with no comments or suppressions, zero deletions, no application files touched, no MUST KILL flags and no skips. The lead read reports and hashes. Comment review does not supply application or browser correctness. The separate sequential no-comments review is explicitly reduced.\n\nRequired deslop is absent and no replacement was requested or authorized. It remains unmet. control-ui companion and a usable matching browser are absent. No create-skill authoring loop ran. Nothing was installed or enabled. Opening a PR was read in full; its commit, rebase, push, actual PR and readiness branches remain unperformed because this evaluation forbids them. Local artifacts are not a PR. Babysit and scheduling were not started.\n\n## Open decisions and completion boundary\n\nMatching browser verification must still establish current filter/column behavior, real downloaded bytes and visible empty feedback. Future localized totals and spreadsheet formula-prefix policy are open product choices. A real app must provide its actual hidden-order and column policy rather than inherit fixture assumptions. All current code is uncommitted checked local output; full user-outcome verification and delivery remain incomplete. \n\n## Final artifact readback\n\nThe lead read native/final/result.json, its actual tracked diff, all untracked added files, checkpoint, clone/checkouts, Unit 1/2 logs, syntax log, exact revision receipt, independent reviews and comment receipts. The final source hashes match the comment receipt and both post-comment reviews. The result file was read back after writing this final native/reduced account. All spawned feature workers returned terminal results; no pending worker or server is left running.\n",
        "artifact": {
          "path": "fixtures/batch-12/verifiable-feature.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature.result.md",
          "sha256": "0643968afcd3c5c385eefe4cd054b86d9ebbf061b647c91b32400e819652d5ff",
          "bytes": 14950
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-12.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-12.events.jsonl",
            "sha256": "67954ee0571d6cdc9d2b8c299428822b19cd77b3146edb9a48ef7690ae013431",
            "bytes": 711397,
            "eventReferences": [
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6f8e71bf6531b8d078b15c1dcbd2828a8a4bb3744777995041c9ec86e9671dc6"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8600d71f9d5d0d2374dca074904aa2a939dc595f958f1ce0bb75beee02f464a6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a6527cd7f871b5a4eb4a124c25607d10b3f8865a4aedefadeed2b0bb95f49b7a"
              },
              {
                "eventId": "item_9",
                "line": 18,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "12ce4b4727346dae251245d2d9887d9d5073d9975be548baec0e754d6a046bf1",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9915ad0b5e250f091010676ae3cb5a68dd9248f26fc12086546b36ff73cffbca"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4a795edb33ae1d0568407fa6bfee2a6f3988c6220a90de4e7116cb02c0c15afe",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "25acbbcf2226a08ebb18cce59f5203d326b662c2d40cebfb05f16909288e2a82"
              },
              {
                "eventId": "item_21",
                "line": 41,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "34e9960bddcf1fbf3881ad1c8b45a83d99b39e66ac5e1e452e08425b454a28e4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_42",
                "line": 78,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e88ef6054c95e436049e8553e07947e466d1343125ca87c47659d592b086ff0b"
              },
              {
                "eventId": "item_42",
                "line": 79,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "25e2960f97283de5cad44f72cf43b9428fef5584d62705648fc71857f30ac8a3",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_42",
                "line": 78,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e88ef6054c95e436049e8553e07947e466d1343125ca87c47659d592b086ff0b"
              },
              {
                "eventId": "item_42",
                "line": 79,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "25e2960f97283de5cad44f72cf43b9428fef5584d62705648fc71857f30ac8a3",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_44",
                "line": 82,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "38926a0f486a54776d25f053635fdce31de276021515c091ee02aea93b0770fd"
              },
              {
                "eventId": "item_44",
                "line": 83,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e27cd2cdc990223550ee195dd6bdfa34ec3919c78ea0440caf82f89894b1a4df",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_47",
                "line": 87,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "299e3b4c8ea5e40f491189d49c69f3d735dda4a0bba21fd964d7121280c13c15"
              },
              {
                "eventId": "item_47",
                "line": 88,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6c5414457931079970b6896704f4f681b32876933edabeafacca9ef97fe1f2e3",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/batch-12/verifiable-feature/native/final-lead-checks.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final-lead-checks.json",
            "sha256": "529a395f026becdcb809e86ee59a8a0f1b2f9c3789749839bac25dc3bb7c0cd8",
            "bytes": 1504
          },
          {
            "path": "fixtures/batch-12/verifiable-feature/browser-attempt.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-attempt.json",
            "sha256": "873f6c6e6331fa3edad8882e445c47c4ee325ef40f52ec93517acd7365f293f2",
            "bytes": 462
          },
          {
            "path": "fixtures/batch-12/verifiable-feature/native/arena-method-receipt.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/arena-method-receipt.json",
            "sha256": "ccea86eb2563a7a60c40d438f79fec1778ed7475d7dff00fa4aa10f01c02177c",
            "bytes": 4367
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_8",
            "item_9",
            "item_14",
            "item_21",
            "item_42"
          ],
          "actualExecutionEventIds": [
            "item_42",
            "item_44",
            "item_47"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-attempt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-attempt.json",
      "sha256": "873f6c6e6331fa3edad8882e445c47c4ee325ef40f52ec93517acd7365f293f2",
      "bytes": 462,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"tool\": \"mcp__cua_repl.js\",\n  \"attempt\": {\n    \"operation\": \"cua.createBrowserTab\",\n    \"browser\": \"iab\",\n    \"url\": \"http://127.0.0.1:59481/\",\n    \"visible\": false\n  },\n  \"result\": \"Browser is not available: iab\",\n  \"inventory\": {\n    \"operation\": \"cua.listBrowsers\",\n    \"result\": []\n  },\n  \"screenshots\": [],\n  \"limits\": \"No matching browser could be bound. Empty-result function test is not browser evidence. Required control-ui companion not exposed.\"\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/csv.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/app/csv.test.mjs",
      "sha256": "08110cb250e72531ef99b1f0d523f96fa086dd4683649fa1a2870b11aef94478",
      "bytes": 920,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { orderView, exportCsv } from './dashboard.mjs';\nimport orders from './orders.json';\ntest('exports only current visible rows in displayed order and escapes literal commas and quotes', () => {\n  expect(exportCsv(orderView([...orders, {id:4,status:'open',hidden:true,customer:'Private',total:9}], 'open', ['customer','total','id']))).toEqual({kind:'ready', csv:'customer,total,id\\r\\n\"Ada, Inc.\",12.5,1\\r\\n\"Say \"\"Hi\"\"\",0,3'});\n});\ntest('empty result gives actionable feedback', () => {\n  expect(exportCsv(orderView(orders, 'missing'))).toEqual({kind:'empty',message:'No orders match the current filter. Change the filter and try again.'});\n});\ntest('newlines and empty values retain CSV semantics', () => {\n  expect(exportCsv(orderView([{id:5,status:'open',customer:'line\\nnext',total:null}], 'open'))).toEqual({kind:'ready',csv:'id,customer,total\\r\\n5,\"line\\nnext\",'});\n});\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/app/dashboard.mjs",
      "sha256": "8f4bf70570fb62601bc12298933debf927680a8d7dda28d294ae5d195879f06a",
      "bytes": 807,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "export const displayedColumns = ['id', 'customer', 'total'];\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && !order.hidden);\n}\nexport function orderView(orders, status, columns = displayedColumns) {\n  return { columns: [...columns], rows: visible(orders, status) };\n}\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Change the filter and try again.' };\n  const cell = value => {\n    const text = String(value ?? '');\n    return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n  };\n  return { kind: 'ready', csv: [view.columns.map(cell).join(','), ...view.rows.map(order => view.columns.map(key => cell(order[key])).join(','))].join('\\r\\n') };\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/index.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/app/index.html",
      "sha256": "9c3f4b614686ba158ef7e5b52b66ed0a11c3da058ea3b29d4e669426ee185b26",
      "bytes": 399,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><title>Orders fixture</title><body><h1>Orders</h1><label>Status <select id=\"status\"><option>open</option><option>closed</option><option>missing</option></select></label><button id=\"export\">Export CSV</button><p id=\"message\" role=\"status\"></p><table><thead></thead><tbody></tbody></table><script type=\"module\" src=\"/ui.mjs\"></script></body></html>"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/serve.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/app/serve.mjs",
      "sha256": "a9b3a45b7cfc0ff73364b3d42240d35395bedbc20fc2df05f488d5b8b89ff141",
      "bytes": 379,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const root=import.meta.dir; const server=Bun.serve({hostname:'127.0.0.1',port:0,fetch(req){ const path=new URL(req.url).pathname; const name=path==='/'?'index.html':path.slice(1); if(!['index.html','dashboard.mjs','ui.mjs','orders.json'].includes(name))return new Response('Not found',{status:404});return new Response(Bun.file(root+'/'+name)); }}); console.log(server.url.href);"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/ui.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/app/ui.mjs",
      "sha256": "dff5097e6f3fb634d89d4cc9aaf853c8c26b14c6f0c898f53aa282bbf74eb0c6",
      "bytes": 1398,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { orderView, exportCsv } from './dashboard.mjs';\nconst orders = await (await fetch('/orders.json')).json();\nconst status = document.querySelector('#status');\nconst message = document.querySelector('#message');\nconst currentView = () => orderView(orders, status.value);\nfunction render() {\n  const view = currentView();\n  message.textContent = '';\n  const head = document.createElement('tr');\n  for (const column of view.columns) { const cell = document.createElement('th'); cell.textContent = column; head.append(cell); }\n  document.querySelector('thead').replaceChildren(head);\n  const rows = view.rows.map(order => { const row = document.createElement('tr'); for (const column of view.columns) { const cell=document.createElement('td');cell.textContent=order[column];row.append(cell); } return row; });\n  document.querySelector('tbody').replaceChildren(...rows);\n}\nstatus.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(currentView());\n  if (result.kind === 'empty') { message.textContent=result.message; return; }\n  const url=URL.createObjectURL(new Blob([result.csv], {type:'text/csv;charset=utf-8'}));\n  const link=document.createElement('a');link.href=url;link.download='orders.csv';link.click();URL.revokeObjectURL(url);\n  message.textContent='Exported the currently displayed orders.';\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/conditions.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/conditions.md",
      "sha256": "f89453f7daef91d043202ea63e3e060e65fa8cdb64f7fa56d9f9672e51e922a5",
      "bytes": 355,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Browser-denied variant\n\nRequested condition is simulated by withholding browser calls in this variant. The host did enforce browser unavailability in the separate base attempt: iab unavailable and browser inventory empty. No host permission denial was returned. CSV checks establish bytes only. Browser feedback and download behavior remain unverified.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/tests.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/browser-denied/tests.log",
      "sha256": "1130b2bfda47f30646c30907ea8dd4127756c6ba98a6b0388854cb50203ec4d8",
      "bytes": 378,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/browser-denied/app/csv.test.mjs:\n(pass) exports only current visible rows in displayed order and escapes literal commas and quotes [0.29ms]\n(pass) empty result gives actionable feedback [0.01ms]\n(pass) newlines and empty values retain CSV semantics [0.02ms]\n\n 3 pass\n 0 fail\n 3 expect() calls\nRan 3 tests across 1 file. [12.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/build-sequential.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/build-sequential.mjs",
      "sha256": "6c66c949e79eaeb11fdba1b9b5728c364bf2ac98ef70668f9b763aed80514404",
      "bytes": 2056,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const dir = 'verifiable-feature/sequential/app';\nawait Bun.write(`${dir}/orders.json`, await Bun.file('verifiable-feature/input/orders.json').arrayBuffer());\nawait Bun.write(`${dir}/dashboard.mjs`, `export const displayedColumns = ['id', 'customer', 'total'];\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && !order.hidden);\n}\nexport function orderView(orders, status, columns = displayedColumns) {\n  return { columns: [...columns], rows: visible(orders, status) };\n}\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Change the filter and try again.' };\n  const cell = value => {\n    const text = String(value ?? '');\n    return /[\",\\\\r\\\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n  };\n  return { kind: 'ready', csv: [view.columns.map(cell).join(','), ...view.rows.map(order => view.columns.map(key => cell(order[key])).join(','))].join('\\\\r\\\\n') };\n}\n`);\nawait Bun.write(`${dir}/csv.test.mjs`, `import { test, expect } from 'bun:test';\nimport { orderView, exportCsv } from './dashboard.mjs';\nimport orders from './orders.json';\ntest('exports only current visible rows in displayed order and escapes literal commas and quotes', () => {\n  expect(exportCsv(orderView([...orders, {id:4,status:'open',hidden:true,customer:'Private',total:9}], 'open', ['customer','total','id']))).toEqual({kind:'ready', csv:'customer,total,id\\\\r\\\\n\"Ada, Inc.\",12.5,1\\\\r\\\\n\"Say \"\"Hi\"\"\",0,3'});\n});\ntest('empty result gives actionable feedback', () => {\n  expect(exportCsv(orderView(orders, 'missing'))).toEqual({kind:'empty',message:'No orders match the current filter. Change the filter and try again.'});\n});\ntest('newlines and empty values retain CSV semantics', () => {\n  expect(exportCsv(orderView([{id:5,status:'open',customer:'line\\\\nnext',total:null}], 'open'))).toEqual({kind:'ready',csv:'id,customer,total\\\\r\\\\n5,\"line\\\\nnext\",'});\n});\n`);\nconsole.log('Unit 1 written. Run CSV checks before UI integration.');\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/build-ui.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/build-ui.mjs",
      "sha256": "802b9df0331bb6d9e484e62efc16a04e8f08b8213ddc9fbc6425845992755607",
      "bytes": 2432,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const dir='verifiable-feature/sequential/app';\nawait Bun.write(`${dir}/index.html`, `<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><title>Orders fixture</title><body><h1>Orders</h1><label>Status <select id=\"status\"><option>open</option><option>closed</option><option>missing</option></select></label><button id=\"export\">Export CSV</button><p id=\"message\" role=\"status\"></p><table><thead></thead><tbody></tbody></table><script type=\"module\" src=\"/ui.mjs\"></script></body></html>`);\nawait Bun.write(`${dir}/ui.mjs`, `import { orderView, exportCsv } from './dashboard.mjs';\nconst orders = await (await fetch('/orders.json')).json();\nconst status = document.querySelector('#status');\nconst message = document.querySelector('#message');\nconst currentView = () => orderView(orders, status.value);\nfunction render() {\n  const view = currentView();\n  message.textContent = '';\n  const head = document.createElement('tr');\n  for (const column of view.columns) { const cell = document.createElement('th'); cell.textContent = column; head.append(cell); }\n  document.querySelector('thead').replaceChildren(head);\n  const rows = view.rows.map(order => { const row = document.createElement('tr'); for (const column of view.columns) { const cell=document.createElement('td');cell.textContent=order[column];row.append(cell); } return row; });\n  document.querySelector('tbody').replaceChildren(...rows);\n}\nstatus.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(currentView());\n  if (result.kind === 'empty') { message.textContent=result.message; return; }\n  const url=URL.createObjectURL(new Blob([result.csv], {type:'text/csv;charset=utf-8'}));\n  const link=document.createElement('a');link.href=url;link.download='orders.csv';link.click();URL.revokeObjectURL(url);\n  message.textContent='Exported the currently displayed orders.';\n});\nrender();\n`);\nawait Bun.write(`${dir}/serve.mjs`, `const root=import.meta.dir; const server=Bun.serve({hostname:'127.0.0.1',port:0,fetch(req){ const path=new URL(req.url).pathname; const name=path==='/'?'index.html':path.slice(1); if(!['index.html','dashboard.mjs','ui.mjs','orders.json'].includes(name))return new Response('Not found',{status:404});return new Response(Bun.file(root+'/'+name)); }}); console.log(server.url.href);`);\nconsole.log('Unit 2 written after passing Unit 1. Browser verification remains open.');\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/contract.json",
      "sha256": "e9114b88912ea6d2e00973df2704d00bad1317672fef284c79bf02c1dc837503",
      "bytes": 7425,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"id\": \"verifiable-feature\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/feature.md\",\n    \"skills/poteto-mode/SKILL.md\",\n    \"agents/poteto-agent.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"skills/how/SKILL.md\",\n    \"skills/how/references/explorer-prompt.md\",\n    \"skills/how/references/explainer-prompt.md\",\n    \"skills/architect/SKILL.md\",\n    \"skills/architect/references/runner-prompt.md\",\n    \"skills/architect/references/rationale-template.md\",\n    \"skills/arena/SKILL.md\",\n    \"skills/interrogate/SKILL.md\",\n    \"skills/interrogate/references/reviewer-prompt.md\",\n    \"skills/interrogate/references/rubric.md\",\n    \"skills/principle-model-the-domain/SKILL.md\",\n    \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"skills/principle-sequence-verifiable-units/SKILL.md\"\n  ],\n  \"prompt\": \"Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.\",\n  \"requirements\": [\n    \"Read the complete mode and Feature playbook, required principle leaves and routed workflows. Record the eight playbook steps in a todo binding before task-specific items. Trace how the dashboard filters and renders orders before designing the export.\",\n    \"Use architect for design exploration. Retain two structurally distinct alternatives and its synthesis artifacts. Choose the named export data shape and organizing structure before code-writing. Use the complete arena contract for multiple valid implementation shapes, including isolated candidate paths, inspected candidates and a fresh cross-judge.\",\n    \"Keep all four checkpoint items, including n/a with a reason. Blocking gates precede fan-out. Split independent write targets before serializing real shared invariants. Rewrite the checkpoint at phase boundaries and keep it inline with the single code-coupled owner.\",\n    \"Assign the exact input SHA, owned paths, full poteto-agent prompt, role and success criteria. Use inherited model roles unless supported explicit choices are observed. Inspect returned artifacts and review the diff as the lead. A no-spawn worker owns the diff directly and returns to its parent, never waits for a nested agent. Required delegation and review separation have no laziness or skip escape.\",\n    \"Make surgical edits, re-ground upstream-derived files, propagate shared changes to every consumer and verify each. Preserve Comments rules and disclose missing deslop, no-comments or matching-control companions. Missing companion execution cannot become satisfied by assertion.\",\n    \"Deliver small units with a check before the next. Verify the exported literal rows, column order and escaping through fixture execution, and the empty-state feedback through the matching browser surface. Compilation alone and wrong-surface checks cannot establish the requested user outcome.\",\n    \"Run interrogate before shipping a contested design. Record worker independence and actual model limits. Prepare checked local changes and delivery order when commits, rebase, push or PR creation are unauthorized. Run complete Opening a PR when available and authorized, and retain exact missing dependency otherwise. Opening a PR never triggers Babysit implicitly.\",\n    \"Return what was built, choices and reasons, a table of design alternatives, all four checkpoint items and open decisions. Evidence names the end-user behavior and next-maintainer implications, missing capabilities and forbidden completion claims.\"\n  ],\n  \"expectedFull\": \"Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds.\",\n  \"expectedReduced\": \"With worker operations unavailable, authorized sequential grounding, design alternatives and direct implementation produce a useful local diff and outcome evidence. The report calls this reduced capability and retains mandatory independent delegation, arena cross-judge and review separation as unsatisfied gates. Inherited selections and unknown models supply no diversity claim. With no external authorization, return the local checked result and ordered delivery plan without push or PR creation. Missing companions retain their specific limits. A fixture CLI check may verify CSV bytes but cannot satisfy denied browser verification.\",\n  \"expectedBlocked\": \"Denied source or required missing skill stops dependent grounding or design. Missing independent operations block required review separation rather than waive it. Denied matching browser verification leaves the empty-state gate unverified, even if CSV fixtures pass. Missing opening-a-pr.md blocks PR-dependent work. Denied or unauthorized writes, commit, rebase or PR creation stay unperformed. The result reports the exact gate, available partial artifacts and open decisions without claiming complete delivery.\",\n  \"forbiddenClaims\": [\n    \"All four checkpoint dimensions apply, or omitted dimensions need no n/a explanation.\",\n    \"Sequential roles are independent workers, a fresh cross-judge, parallel exploration or independent review separation.\",\n    \"A no-spawn worker must wait on another worker, or Laziness Protocol permits skipping code-owner separation.\",\n    \"The source grok-4.7-xhigh-fast default proves a supported or selected host model.\",\n    \"A requested or inherited model proves the actual model or model diversity.\",\n    \"A compile, structural validator, inconclusive check or CSV-only test proves browser behavior or the complete feature outcome.\",\n    \"Unrun checks are green, all shared consumers were verified without observations, or ordered commits and rebases happened without authorization and evidence.\",\n    \"A missing companion or deferred Opening a PR playbook ran successfully.\",\n    \"A local PR draft is an actual PR, upstream autonomy authorizes external writes, or opening a PR starts Babysit.\",\n    \"Canonical prompts are registered custom agents, source metadata guarantees background execution, or isolated helper tests prove this host case passed.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/feature.json\"\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/grounding.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/grounding.md",
      "sha256": "c012e1709cd7e6ed20d7dfacde214a74a6fd18f16cd912d6a5af03c1fc0140e4",
      "bytes": 1204,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# How the fixture works\n\n## Overview\nThe committed dashboard is a two-function module, not a rendered dashboard. This is direct sequential exploration, with independent explainer absent in this variant.\n\n## Key concepts\nOrder has id, status, customer and total. visible(orders,status) selects matching status only. exportCsv(orders) emits fixed id/customer/total columns and interpolates raw values.\n\n## How it works\nNo caller, browser entry point, column controller or rendered table exists in the supplied input. A caller must pass visible(orders,status) into exportCsv; passing all orders exposes the closed Hidden row. Commas and quotes currently corrupt the CSV. There is no empty-result feedback.\n\n## Where things live\ninput/dashboard.mjs has both functions. input/orders.json has two open rows and one closed Hidden row. Input revision is 933a5f5df924b2b089f410615f99af7851010643, independently verified with git rev-parse and ls-tree.\n\n## Gotchas\nHidden means excluded by current status in this synthetic fixture; no hidden flag exists in input. The implementation also excludes explicit hidden:true rows. A local browser shell will be newly authored fixture work, not a recovered production UI.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/arena-method-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/arena-method-receipt.json",
      "sha256": "ccea86eb2563a7a60c40d438f79fec1778ed7475d7dff00fa4aa10f01c02177c",
      "bytes": 4367,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"kind\": \"arena\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"assignments\": [\n    {\n      \"id\": \"feature-arena-a\",\n      \"workerId\": \"/root/feature_case/arena_design_a\",\n      \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"outputOwner\": \"/root/feature_case/arena_design_a\",\n      \"outputPath\": \"verifiable-feature/native/candidate-a\",\n      \"role\": \"architect runner\",\n      \"status\": \"completed\",\n      \"startedOrder\": 2,\n      \"completedOrder\": 4,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"kind\": \"native-independent-design\",\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one independent design package at assigned revision\",\n        \"order\": 2\n      },\n      \"taskArtifact\": \"verifiable-feature/native/arena-task.md\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"resultMethod\": \"native-independent-design\",\n      \"outputSha256\": \"63036bb80e87e5fcb0b9061ed44f846034390f7da1d7f5a354ecdcfc0f31e1ee\",\n      \"hashedArtifact\": \"verifiable-feature/native/candidate-a/design.md\"\n    },\n    {\n      \"id\": \"feature-arena-b\",\n      \"workerId\": \"/root/feature_case/arena_design_b\",\n      \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"outputOwner\": \"/root/feature_case/arena_design_b\",\n      \"outputPath\": \"verifiable-feature/native/candidate-b\",\n      \"role\": \"architect runner\",\n      \"status\": \"completed\",\n      \"startedOrder\": 3,\n      \"completedOrder\": 5,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"kind\": \"native-independent-design\",\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one independent design package at assigned revision\",\n        \"order\": 3\n      },\n      \"taskArtifact\": \"verifiable-feature/native/arena-task.md\",\n      \"rubricProvided\": false,\n      \"resultRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"resultMethod\": \"native-independent-design\",\n      \"outputSha256\": \"1ace7b0b703dcb6395d7ff420e43d3a5ef6e321b1bcce6ab070a62aa7d2a3720\",\n      \"hashedArtifact\": \"verifiable-feature/native/candidate-b/design.md\"\n    },\n    {\n      \"id\": \"feature-arena-judge\",\n      \"workerId\": \"/root/feature_case/arena_judge\",\n      \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"outputOwner\": \"/root/feature_case/arena_judge\",\n      \"outputPath\": \"verifiable-feature/native/judge\",\n      \"role\": \"fresh readonly cross-judge\",\n      \"status\": \"completed\",\n      \"startedOrder\": 6,\n      \"completedOrder\": 7,\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"kind\": \"native-independent-cross-judge\",\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one fresh comparison of two completed design candidates\",\n        \"order\": 6\n      },\n      \"taskArtifact\": \"verifiable-feature/native/arena-task.md\",\n      \"rubricProvided\": true,\n      \"resultRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n      \"resultMethod\": \"native-independent-cross-judge\",\n      \"outputSha256\": \"83c9340b4c7998b070339c34bd3f2b2ac43c66b5ba59d2d489353ab8b1688eff\",\n      \"hashedArtifact\": \"verifiable-feature/native/judge/judge.md\"\n    }\n  ],\n  \"reviewArtifact\": \"verifiable-feature/native/synthesis.md\",\n  \"reviewedBy\": \"/root/feature_case\",\n  \"declaredOrder\": 1,\n  \"candidates\": [\n    \"feature-arena-a\",\n    \"feature-arena-b\"\n  ],\n  \"judge\": \"feature-arena-judge\",\n  \"rubricArtifact\": \"verifiable-feature/native/arena-rubric.md\",\n  \"synthesis\": {\n    \"order\": 8,\n    \"inspectedCandidates\": [\n      \"feature-arena-a\",\n      \"feature-arena-b\"\n    ],\n    \"artifact\": \"verifiable-feature/native/synthesis.md\",\n    \"verificationArtifact\": \"verifiable-feature/native/final-lead-checks.json\",\n    \"designScreeningArtifact\": \"verifiable-feature/native/lead-design-reading.md\",\n    \"verificationOrder\": 10,\n    \"verificationScope\": \"Later actual final-module CSV checks only; design screening preceded final implementation; no matching browser proof\"\n  },\n  \"limits\": [\n    \"Design-only method, no implementation or browser claim\",\n    \"Requested models inherited, actual models unknown\",\n    \"No package evidence validator or case grade claimed\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/arena-rubric.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/arena-rubric.md",
      "sha256": "4839de9399000caecb66eb17ff2666c60e95b499711e4daa60107f6805cffd5b",
      "bytes": 445,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Parent-only design rubric\n\nScore each criterion 0 to 2 with concrete evidence.\n1. Filter and hidden-row correctness are encoded in one owner.\n2. Export column order matches displayed column order without hand synchronization.\n3. CSV quoting and useful empty state have explicit tested boundaries.\n4. Small public interface hides export decisions without coupling to markup.\n5. Future maintainer can extend display/export without silent drift.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/arena-task.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/arena-task.md",
      "sha256": "b7a75e4378d45caeba9c490d0c0f1e3dacc5dc407ef22641b1c9c0e19052ea9e",
      "bytes": 1211,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Native design arena task\n\nImplement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.\n\nExact input Git revision 933a5f5df924b2b089f410615f99af7851010643. Read verifiable-feature/grounding.md and input copies. Produce one complete architecture design package, caller usage first and signatures without logic, using installed architect runner-prompt and rationale-template. Choose any valid whole implementation shape independently; include rejected alternative. This is a design artifact, not code. Do not read other candidates or parent synthesis. No spawning or integrations.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/assignment.json",
      "sha256": "8a0ded3f023fb2c0ed0fcf5fd21a32ec0a0b0af0ee765c917542c70f0641a8ad",
      "bytes": 1016,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"id\": \"native-feature-owner\",\n  \"scope\": \"Independent code-owner implements the chosen OrderView design in owned directory\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"outputOwner\": \"/root/feature_case/native_feature_owner\",\n  \"isolatedOutputPath\": \"verifiable-feature/native/owner\",\n  \"role\": \"poteto feature code-owner\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"verifiable-feature/grounding.md\",\n    \"verifiable-feature/sequential/synthesis.md\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"observedModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"observedEffort\": \"unknown\",\n  \"spawnTool\": \"collaboration.spawn_agent\",\n  \"spawnResult\": {\n    \"task_name\": \"/root/feature_case/native_feature_owner\"\n  },\n  \"limits\": [\n    \"Initial native spawn rejected at full capacity; later fresh owner accepted after dependency case terminated\",\n    \"No evidence of model diversity\",\n    \"Owner does not satisfy independent arena runners and judge\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-a/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-a/design.md",
      "sha256": "63036bb80e87e5fcb0b9061ed44f846034390f7da1d7f5a354ecdcfc0f31e1ee",
      "bytes": 4655,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Design candidate A\n\n## Problem\nThe fixture exports raw orders through a fixed column list. The inspected module filters only by status. It has no rendered caller. A new caller must use the same selected rows and column order for rendering and exporting. The committed open rows contain a comma and quotes, which the current interpolation does not escape.\n\n## Usage (caller's view)\nWrite the caller first. The browser owns status and the displayed column order. It obtains one immutable view and uses that view for both outputs.\n\n```ts\nconst view = ordersView(orders, {status: 'open', columns: ['customer', 'id', 'total']});\nrenderTable(view);\nconst download = csvForView(view);\nif (download.kind === 'empty') showMessage(download.message);\nelse saveDownload(download.filename, download.text);\n\nconst closed = ordersView(orders, {status: 'closed', columns: ['id', 'customer']});\nrenderTable(closed);\n\nconst nothing = ordersView([], {status: 'open', columns: ['total']});\nshowExportResult(csvForView(nothing));\n```\n\n## Shape\nThe named domain shape is OrdersView. It contains ordered columns and selected domain rows. Model the Domain moves the display and export invariant into this one immutable object. The browser renders this object and passes it directly to csvForView. No independent export filter or export column list exists.\n\nOne module owns visible row selection, allowed column labels and CSV encoding. The browser owns filter controls and download transport. Boundary Discipline keeps fixture parsing and event handling in the shell. The pure module has no DOM imports. csvForView hides RFC-style cell quoting and ordered projection behind one function. Its result union distinguishes an empty selection from a downloadable file. An empty selection has no text or filename. Encode Lessons in Structure makes it impossible for a typed caller to download an empty branch by reading a text property without narrowing.\n\nSeparate Before Serializing Shared State keeps candidate outputs isolated. The implementation owner alone edits the domain module and its browser consumer. Each click derives a fresh view from current state, so it cannot reuse a stale mutable export cache.\n\nThe existing exportCsv(orders) API should be replaced by csvForView(view) and all known callers migrated in the same unit. A compatibility export function would permit raw rows to bypass the current selection.\n\n## Synthesis decision\nPending the parent's fresh cross-judge. This candidate has not read another candidate or a shared rubric. No winner is claimed.\n\n## Tradeoffs accepted\n- We accept a typed view object in exchange for sharing one selection and one column order across rendering and export.\n- We accept constructing a small snapshot on each relevant update in exchange for avoiding mutable cached rows.\n- We accept placing CSV encoding beside row selection in exchange for one import that owns the whole export invariant.\n\n## Alternatives considered\nA DOM table serializer would read headers and cells from the displayed table and encode them directly. It hides selection policy from the export API, but exposes DOM layout as a data contract and may accidentally export an empty placeholder or presentation text. OrdersView keeps raw numeric values and domain rows explicit and can run in Bun without a browser.\n\n## Open questions and risks\nShould CSV formula-leading customer values receive spreadsheet-specific neutralization beyond the requested comma and quote escaping?\nShould the download filename vary by filter, or is orders.csv sufficient for this synthetic fixture?\nDoes any caller outside the supplied two-function module depend on the old exportCsv signature?\n\n## Next implementation step\nSequence Work into Verifiable Units starts with literal expected CSV tests for open rows and reordered columns, then the pure module, then the matching browser caller and empty-message check.\n\n## Candidate screen and limits\nThe public interface hides selection and serialization policy. It has no pass-through wrappers or hand-synced column lists. The browser must render the provided view rather than reconstruct a second list. Module-private view branding prevents arbitrary object construction by typed consumers. Runtime JavaScript callers still require boundary validation. All bodies remain unimplemented. No browser behavior, CSV bytes or performance result is claimed by this design artifact.\n\nRequested model and effort inherit-parent. Observed model and effort unknown. This is one native independent design worker. No model diversity claim follows. Source reads used functions.exec with tools.exec_command. No nested worker operation was used.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-a/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-a/result.json",
      "sha256": "6ba3fb40f30c126da35c3ee9fbf39da6510be1db053a9808d8af165b5faf3a51",
      "bytes": 769,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-arena-a\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"resultRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-design\",\n  \"resultMethod\": \"native-independent-design\",\n  \"status\": \"completed\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"artifacts\": [\n    \"verifiable-feature/native/candidate-a/design.md\",\n    \"verifiable-feature/native/candidate-a/sketch.ts\",\n    \"verifiable-feature/native/candidate-a/todo.md\"\n  ],\n  \"limits\": [\n    \"Design-only artifact, no implementation or runtime behavior proof\",\n    \"No nested workers\",\n    \"Fresh cross-judge and synthesis belong to parent\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-a/sketch.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-a/sketch.ts",
      "sha256": "e5912d8dfc402ec98e2c1e0f9324ff098bda9d89770edec6a9364c881fa4edad",
      "bytes": 715,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "type Column = 'id' | 'customer' | 'total';\ntype Order = Readonly<{ id: number; status: string; customer: string; total: number; hidden?: boolean }>;\ndeclare const viewBrand: unique symbol;\nexport type OrdersView = Readonly<{\n  [viewBrand]: true;\n  columns: readonly Column[];\n  rows: readonly Order[];\n}>;\nexport type CsvResult =\n  | Readonly<{kind: 'empty'; message: string}>\n  | Readonly<{kind: 'download'; filename: string; text: string}>;\nexport function ordersView(orders: readonly Order[], selection: Readonly<{status: string; columns: readonly Column[]}>): OrdersView {\n  throw new Error('not implemented');\n}\nexport function csvForView(view: OrdersView): CsvResult {\n  throw new Error('not implemented');\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-a/todo.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-a/todo.md",
      "sha256": "231afb426714788dcdb2536d39d6783724e198eed2e3865298c1dd24557f9e4b",
      "bytes": 306,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "- [x] Ground. Read input module and existing traced grounding.\n- [x] Sketch. Produce candidate architecture and signatures only.\n- [ ] Agree. Parent arena synthesis pending.\n- [ ] Implement. Outside this design-only assignment.\n- [ ] Scrap. Conditional on implementation feedback, outside this assignment.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-b/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-b/design.md",
      "sha256": "1ace7b0b703dcb6395d7ff420e43d3a5ef6e321b1bcce6ab070a62aa7d2a3720",
      "bytes": 5227,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "## Problem\n\nThe supplied dashboard has no rendered table or browser entry point. Its visible function filters status, while exportCsv accepts arbitrary rows and hardcodes three columns. The proposed design gives the table and export the same immutable display snapshot. This prevents the export caller from accidentally passing unfiltered orders or choosing a second column order.\n\n## Usage (caller's view)\n\n```ts\nconst table = projectOrders(orders, {status: \"open\", columns: [\"customer\", \"id\", \"total\"]});\nrenderTable(table.headers, table.rows);\nconst result = exportTableCsv(table);\n```\n\nThe export button branches on result.kind. A file result downloads result.text. An empty result displays result.message in a status element.\n\n```ts\nconst reordered = projectOrders(orders, {status: \"open\", columns: [\"total\", \"customer\"]});\nrenderTable(reordered.headers, reordered.rows);\nconst reorderedDownload = exportTableCsv(reordered);\n```\n\n```ts\nconst empty = projectOrders(orders, {status: \"missing\", columns: [\"id\", \"customer\"]});\nconst feedback = exportTableCsv(empty);\n```\n\n## Shape\n\nA DisplayTable owns ordered headers and an ordered matrix of already displayed scalar cells. projectOrders owns the sole filtering and column-selection policy. Both render and export consume that projection. exportTableCsv owns CSV escaping and the empty-result union. It does not accept raw orders.\n\nThe named export data shape is DisplayTable, organized as a row-major matrix with ordered headers. This follows model-the-domain. The browser shell parses fixture JSON at its boundary, following boundary-discipline. A private brand prevents callers from constructing an unrelated table accidentally, following encode-lessons-in-structure. The public export operation hides delimiters, quote doubling and empty-state policy. The renderer still sees the cell matrix because it genuinely needs those cells. No cache or duplicated filtered-order store exists.\n\nThe one code owner modifies dashboard.mjs and its browser caller together. Design candidates publish disjoint files, following separate-before-serializing-shared-state. The final flow needs the dashboard module and thin UI caller only, following minimize-reader-load.\n\nDominant access patterns are linear. Projection selects eligible orders once, traverses columns in their supplied order, and creates matching rows. Rendering and export each traverse that same snapshot. Browser events produce a fresh snapshot after any filter or column change. Export uses the current snapshot synchronously, with no asynchronous stale closure.\n\n## Synthesis decision\n\nPending the parent arena judgment. This candidate recommends the display snapshot as the base. It has not inspected another candidate or a parent rubric.\n\n## Tradeoffs accepted\n\n- We accept one projected matrix allocation in exchange for identical displayed and exported values and column order.\n- We accept changing the fixture's raw-order export signature in exchange for removing the unsafe way to export unfiltered rows. The input has no recovered callers to preserve.\n- We accept displayed text as CSV content. Sorting, totals formatting and localization become projection policy if added later.\n\n## Alternatives considered\n\nA raw-order serializer taking orders and a column registry hides CSV escaping but leaves the caller to apply filters correctly and synchronize display order. It avoids the matrix allocation, yet exposes the most important policy twice. It loses on invariant ownership and interface depth for this fixture.\n\nReading rendered DOM table cells would make export match the visible table, but couples business data to browser formatting and makes CLI CSV checks insufficient to exercise the actual implementation. It also permits accidental inclusion of offscreen or decorative cells.\n\n## Open questions and risks\n\nShould total values retain raw decimal text or future localized display text? The current fixture supports raw scalar text, so the initial projection uses that policy. Should spreadsheet formula prefixes be escaped? The stated requirement covers commas and quotes, so formula mitigation remains a product decision rather than an invented completion criterion.\n\n## Next implementation step\n\nImplement projectOrders and exportTableCsv with literal fixture assertions, then build the thin table and export-button caller from the same snapshot.\n\n## Red-flag screen and limits\n\nNo pass-through module, phase-named hierarchy, duplicated columns or shared worker output is proposed. A private brand protects the projection boundary in the typed sketch. Runtime JavaScript implementation would keep that boundary within one module and test its public calls. This artifact is an independent native worker design, with inherited requested selection and unknown actual model and effort. It proves no browser behavior or implementation. No create-skill companion or independent prose review ran. No todo tool exists here, so these phases remain a local checklist.\n\n- [x] Ground. Read supplied source and parent grounding.\n- [x] Sketch. Produce this candidate and signatures.\n- [ ] Agree. Parent synthesis pending.\n- [ ] Implement. Outside this assignment.\n- [ ] Scrap. No implementation feedback exists.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-b/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-b/result.json",
      "sha256": "6537fecd5d762d640501aaefb7cf9df52f208792a12a9d423372e8ce8f84a299",
      "bytes": 573,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\"assignmentId\":\"feature-arena-b\",\"inputRevision\":\"933a5f5df924b2b089f410615f99af7851010643\",\"method\":\"native-independent-design\",\"requestedModel\":\"inherit-parent\",\"requestedEffort\":\"inherit-parent\",\"actualModel\":\"unknown\",\"actualEffort\":\"unknown\",\"artifacts\":[\"verifiable-feature/native/candidate-b/design.md\",\"verifiable-feature/native/candidate-b/sketch.ts\"],\"status\":\"completed\",\"limits\":[\"Design only; no feature implementation or browser proof\",\"No other candidate, rubric or synthesis read\",\"Parent referenced native/grounding.md absent; actual grounding.md read\"]}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/candidate-b/sketch.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/candidate-b/sketch.ts",
      "sha256": "c53eef4b356a4031e1551f7a31e4eb08514a62d467d773dde044e73556f92c55",
      "bytes": 907,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "type ColumnKey = \"id\" | \"customer\" | \"total\";\ntype Cell = string | number;\ninterface Order {\n  readonly id: number;\n  readonly status: string;\n  readonly customer: string;\n  readonly total: number;\n  readonly hidden?: boolean;\n}\ninterface OrderView {\n  readonly status: string;\n  readonly columns: readonly ColumnKey[];\n}\ndeclare const displayTableBrand: unique symbol;\ninterface DisplayTable {\n  readonly [displayTableBrand]: true;\n  readonly headers: readonly string[];\n  readonly rows: readonly (readonly Cell[])[];\n}\ntype CsvResult =\n  | {readonly kind: \"file\"; readonly text: string; readonly filename: string}\n  | {readonly kind: \"empty\"; readonly message: string};\n\nexport function projectOrders(orders: readonly Order[], view: OrderView): DisplayTable {\n  throw new Error(\"not implemented\");\n}\nexport function exportTableCsv(table: DisplayTable): CsvResult {\n  throw new Error(\"not implemented\");\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/comments-review/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/comments-review/result.json",
      "sha256": "f512c604cbf30557b8dbd2445db979689cc1fa932af15ad33edc1966301e9e8f",
      "bytes": 1631,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-no-comments-final\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-comment-review\",\n  \"reviewedFiles\": [\n    \"verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs\",\n    \"verifiable-feature/native/final/repository/committed-inputs/browser.mjs\",\n    \"verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs\",\n    \"verifiable-feature/native/final/repository/committed-inputs/index.html\"\n  ],\n  \"actualTouchedApplicationFiles\": [],\n  \"actualDeletionCount\": 0,\n  \"proposedCommentDeletions\": [],\n  \"suppressions\": [],\n  \"mustKill\": [],\n  \"skips\": [],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"outputSha256\": {\n    \"verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs\": \"dca224538566116ac195608a6d13ef5b1921b37fcb783400808e0e56095e6efa\",\n    \"verifiable-feature/native/final/repository/committed-inputs/browser.mjs\": \"65810edbedc2bebc530b85bee3f42ea562a21d13fd38080cba445a2dfaeacf2a\",\n    \"verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs\": \"1837f07381befc46cde38a564c91d7831b9f0f434a90c6fa34575fbb15dd2c88\",\n    \"verifiable-feature/native/final/repository/committed-inputs/index.html\": \"c27ac7d18bac9231b2786dc8f70ee974d46853a8b04b2e47e7dc529c001e7ae0\"\n  },\n  \"limits\": [\n    \"Read-only comment review only; no application correctness or browser verdict\",\n    \"Revision denotes committed synthetic input; reviewed application files are local uncommitted outputs\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/comments-review/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/comments-review/review.md",
      "sha256": "780322b4d55bad8b6a061f34e2bf1cf62288e2000dc170eac25ca9312dc0669a",
      "bytes": 624,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Comment review\n\nAssignment: feature-no-comments-final. Input revision: 933a5f5df924b2b089f410615f99af7851010643. Method: native-independent-comment-review.\n\nIndependently read all four scoped files. They contain no source comments or suppression directives. No proposed deletions, MUST KILL flags, or skips. Actual application files touched: none. Actual deletion count: 0. No application correctness or browser verification verdict supplied.\n\nRequested model and effort: inherit-parent. Observed model and effort: unknown. Revision identifies the committed synthetic inputs; reviewed files are local uncommitted outputs.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/add-ui.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/add-ui.mjs",
      "sha256": "6c044ed421c1bb1b06d19825027a94ee1c789568d9f84a1ce6de0e4e5681849f",
      "bytes": 3512,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const root = 'verifiable-feature/native/final';\nconst app = root + '/repository/committed-inputs';\nawait Bun.write(root + '/checkpoint.md', (await Bun.file(root + '/checkpoint.md').text()) + `\n## Unit 2 boundary\n\n- Blocking first steps. Unit 1 executed 4 tests with 8 literal assertions and zero failures. Proceed to thin browser caller. Matching browser driver remains unavailable, so browser outcome gate is open.\n- Independent workstreams. n/a. One code-coupled owner changes caller and API together without nested workers.\n- Shared mutable state. Current table is replaced synchronously on status/column change. Export consumes that exact table used by render. No second filter or projection registry exists.\n- Smallest safe decomposition. Add the minimal browser shell, then rerun serializer behavior and parse the browser bundle. Browser parse is structural evidence only.\n`);\nawait Bun.write(app + '/browser.mjs', `import {projectOrders, exportTableCsv} from './dashboard.mjs';\n\nconst orders = await fetch('./orders.json').then(response => {\n  if (!response.ok) throw new Error('Could not load fixture orders');\n  return response.json();\n});\nconst status = document.querySelector('#status');\nconst columnOrder = document.querySelector('#columns');\nconst feedback = document.querySelector('#feedback');\nconst table = document.querySelector('#orders');\nlet current;\n\nfunction render() {\n  current = projectOrders(orders, {status: status.value, columns: columnOrder.value.split(',')});\n  const head = document.createElement('thead');\n  const headerRow = head.insertRow();\n  for (const header of current.headers) {\n    const cell = document.createElement('th');\n    cell.textContent = header;\n    headerRow.append(cell);\n  }\n  const body = document.createElement('tbody');\n  for (const values of current.rows) {\n    const row = body.insertRow();\n    for (const value of values) row.insertCell().textContent = String(value ?? '');\n  }\n  table.replaceChildren(head, body);\n  feedback.textContent = current.rows.length === 0 ? 'No orders match the current filters. Change the filters and try again.' : '';\n}\n\nstatus.addEventListener('change', render);\ncolumnOrder.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportTableCsv(current);\n  if (result.kind === 'empty') {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.text], {type: 'text/csv;charset=utf-8'}));\n  const link = document.createElement('a');\n  link.href = url;\n  link.download = result.filename;\n  link.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = 'Exported ' + current.rows.length + ' orders.';\n});\nrender();\n`);\nawait Bun.write(app + '/index.html', `<!doctype html>\n<html lang=\"en\">\n<meta charset=\"utf-8\">\n<title>Orders fixture</title>\n<h1>Orders</h1>\n<label>Status <select id=\"status\"><option value=\"open\">Open</option><option value=\"closed\">Closed</option><option value=\"missing\">No matching orders</option></select></label>\n<label>Columns <select id=\"columns\"><option value=\"id,customer,total\">ID, customer, total</option><option value=\"customer,total,id\">Customer, total, ID</option><option value=\"total,customer\">Total, customer</option></select></label>\n<button id=\"export\" type=\"button\">Export displayed orders</button>\n<p id=\"feedback\" role=\"status\" aria-live=\"polite\"></p>\n<table id=\"orders\"></table>\n<script type=\"module\" src=\"./browser.mjs\"></script>\n</html>\n`);\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/checkout.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/checkout.log",
      "sha256": "bbf42a751fc96dc6d9399ff83c820b2ca63c16286b944a05db4cdca7ce3a09a8",
      "bytes": 63,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "HEAD is now at 933a5f5 Seed disposable workflow fixture inputs\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/checkpoint.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/checkpoint.md",
      "sha256": "fed53c926582f4481cb14165a87f061a917085bce92954aaee671e2909648a84",
      "bytes": 2471,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Final owner checkpoint\n\nNamed data shape DisplayTable. One private column registry projects immutable ordered headers and scalar cell rows. Filtering and projection own domain policy. Rendering and CSV share one current snapshot. No public raw-order serializer remains.\n\n## Unit 1 boundary\n\n- Blocking first steps. Exact committed input inspected and isolated clone detached at 933a5f5df924b2b089f410615f99af7851010643. Candidate B and fresh judge inspected before implementation. Literal serializer checks precede UI.\n- Independent workstreams. n/a for code fan-out. This owner cannot spawn. Candidate alternatives already occupy disjoint owned paths. Lead owns review outside final/.\n- Shared mutable state. One writer owns final/. Browser and export genuinely share current DisplayTable. The private column registry prevents separate rendering/export policies.\n- Smallest safe decomposition. Unit 1 pure projection/CSV plus literal tests. Unit 2 browser caller consuming that API. Each has a check before advancement. Browser verification remains blocked and no completion claim follows syntax checks.\n\n## Unit 2 boundary\n\n- Blocking first steps. Unit 1 executed 4 tests with 8 literal assertions and zero failures. Proceed to thin browser caller. Matching browser driver remains unavailable, so browser outcome gate is open.\n- Independent workstreams. n/a. One code-coupled owner changes caller and API together without nested workers.\n- Shared mutable state. Current table is replaced synchronously on status/column change. Export consumes that exact table used by render. No second filter or projection registry exists.\n- Smallest safe decomposition. Add the minimal browser shell, then rerun serializer behavior and parse the browser bundle. Browser parse is structural evidence only.\n\n## Terminal handoff\n\n- Blocking first steps. Unit 1 and Unit 2 literal execution succeeded. Browser bundle parsed and diff whitespace check returned zero. Browser control and deslop remain unmet. Lead independent diff review remains outside this owner assignment.\n- Independent workstreams. n/a for further fan-out. Return all owned artifacts to lead. No nested worker ran.\n- Shared mutable state. Only this owner wrote final/. Consumer uses the projected snapshot. No raw-order export API remains.\n- Smallest safe decomposition. Checked local units are serializer/projection first, UI caller second. Commits, rebase, push and PR creation stayed unperformed and unauthorized.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/clone.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/clone.log",
      "sha256": "2c27f6e43d484f72da7532db1e26665afda1453ac8880990dc356c8e56525e78",
      "bytes": 67,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "Cloning into 'verifiable-feature/native/final/repository'...\ndone.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/dashboard.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/dashboard.diff",
      "sha256": "137249ac6407d1ca6411a2b85ac0ce8d19988d5bc92014c2c49b0dd849515f24",
      "bytes": 1632,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "diff --git a/committed-inputs/dashboard.mjs b/committed-inputs/dashboard.mjs\nindex 92e482b..61bf5ad 100644\n--- a/committed-inputs/dashboard.mjs\n+++ b/committed-inputs/dashboard.mjs\n@@ -1,2 +1,32 @@\n-export function visible(orders,status){return orders.filter(o=>o.status===status)}\n-export function exportCsv(orders){return \"id,customer,total\\n\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\"\\n\")}\n+const columns = Object.freeze({\n+  id: {header: 'id', cell: order => order.id},\n+  customer: {header: 'customer', cell: order => order.customer},\n+  total: {header: 'total', cell: order => order.total},\n+});\n+\n+export function projectOrders(orders, view) {\n+  const selected = view.columns.map(key => {\n+    if (!Object.hasOwn(columns, key)) throw new Error('Unknown order column: ' + key);\n+    return columns[key];\n+  });\n+  return Object.freeze({\n+    headers: Object.freeze(selected.map(column => column.header)),\n+    rows: Object.freeze(orders\n+      .filter(order => order.status === view.status && order.hidden !== true)\n+      .map(order => Object.freeze(selected.map(column => column.cell(order))))),\n+  });\n+}\n+\n+function escapeCell(value) {\n+  const text = String(value ?? '');\n+  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n+}\n+\n+export function exportTableCsv(table) {\n+  if (table.rows.length === 0) return {kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'};\n+  return {\n+    kind: 'file',\n+    filename: 'orders.csv',\n+    text: [table.headers, ...table.rows].map(row => row.map(escapeCell).join(',')).join('\\r\\n'),\n+  };\n+}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/diff-check.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/diff-check.log",
      "sha256": "16e3edbe92d848d09637b5ec0801d01a735a0deb44c99bc4c374f0865de6acd8",
      "bytes": 11,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "exitCode=0\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/finalize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/finalize.mjs",
      "sha256": "752c17ac328fc634678c96c987df0bdac462ed4ce17999c861ae88d4ea4eefcf",
      "bytes": 3016,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const root = 'verifiable-feature/native/final';\nconst repo = root + '/repository';\nconst app = repo + '/committed-inputs';\nconst head = Bun.spawnSync(['git', '-C', repo, 'rev-parse', 'HEAD']);\nconst dirty = Bun.spawnSync(['git', '-C', repo, 'diff', '--check']);\nawait Bun.write(root + '/diff-check.log', `exitCode=${dirty.exitCode}\\n` + dirty.stdout.toString() + dirty.stderr.toString());\nconst {projectOrders, exportTableCsv} = await import('./repository/committed-inputs/dashboard.mjs');\nconst orders = await Bun.file(app + '/orders.json').json();\nawait Bun.write(root + '/literal-export.csv', exportTableCsv(projectOrders(orders, {status: 'open', columns: ['customer','total','id']})).text);\nawait Bun.write(root + '/revision-receipt.json', JSON.stringify({inputRevision: '933a5f5df924b2b089f410615f99af7851010643', cloneHead: head.stdout.toString().trim(), sourceInput: ['committed-inputs/dashboard.mjs','committed-inputs/orders.json'], outputsUncommitted: true, noNewCommit: true}, null, 2));\nawait Bun.write(root + '/checkpoint.md', (await Bun.file(root + '/checkpoint.md').text()) + `\n## Terminal handoff\n\n- Blocking first steps. Unit 1 and Unit 2 literal execution succeeded. Browser bundle parsed and diff whitespace check returned zero. Browser control and deslop remain unmet. Lead independent diff review remains outside this owner assignment.\n- Independent workstreams. n/a for further fan-out. Return all owned artifacts to lead. No nested worker ran.\n- Shared mutable state. Only this owner wrote final/. Consumer uses the projected snapshot. No raw-order export API remains.\n- Smallest safe decomposition. Checked local units are serializer/projection first, UI caller second. Commits, rebase, push and PR creation stayed unperformed and unauthorized.\n`);\nawait Bun.write(root + '/result.json', JSON.stringify({assignmentId:'feature-final-owner', inputRevision:'933a5f5df924b2b089f410615f99af7851010643', currentHead:head.stdout.toString().trim(), method:'native-independent-final-code-owner', requestedModel:'inherit-parent',requestedEffort:'inherit-parent',observedModel:'unknown',observedEffort:'unknown', ownedPath:root+'/', artifacts:['repository/committed-inputs/dashboard.mjs','repository/committed-inputs/dashboard.test.mjs','repository/committed-inputs/browser.mjs','repository/committed-inputs/index.html','unit1.log','unit2.log','syntax.log','dashboard.diff','literal-export.csv','checkpoint.md','revision-receipt.json','diff-check.log','clone.log','checkout.log'], actualChecks:{unit1:{exitCode:0, tests:4, assertions:8},unit2:{exitCode:0,tests:4,assertions:8}, browserBundle:{exitCode:0, scope:'syntax only'},diffWhitespace:{exitCode:dirty.exitCode}},limits:['Matching browser verification unavailable; empty-state DOM and download remain unverified on browser surface.','deslop and companion control gates unmet.','Lead must inspect actual diff; code owner does not supply independent review of own code.','No model diversity observed.','No new commit, rebase, push or PR.']},null,2));\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/literal-export.csv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/literal-export.csv",
      "sha256": "c523b794a4958a150b41a5ccda4104aac939ae9ae3d15cd3b406e4404496e4a8",
      "bytes": 55,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "customer,total,id\r\n\"Ada, Inc.\",12.5,1\r\n\"Say \"\"Hi\"\"\",0,3"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/prepare.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/prepare.mjs",
      "sha256": "89b4e3f8204432edc0979372ba8049c683a0967e0cb0581fe22e65a212c2b4d0",
      "bytes": 4704,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const root = 'verifiable-feature/native/final';\nconst app = root + '/repository/committed-inputs';\nawait Bun.write(root + '/checkpoint.md', `# Final owner checkpoint\n\nNamed data shape DisplayTable. One private column registry projects immutable ordered headers and scalar cell rows. Filtering and projection own domain policy. Rendering and CSV share one current snapshot. No public raw-order serializer remains.\n\n## Unit 1 boundary\n\n- Blocking first steps. Exact committed input inspected and isolated clone detached at 933a5f5df924b2b089f410615f99af7851010643. Candidate B and fresh judge inspected before implementation. Literal serializer checks precede UI.\n- Independent workstreams. n/a for code fan-out. This owner cannot spawn. Candidate alternatives already occupy disjoint owned paths. Lead owns review outside final/.\n- Shared mutable state. One writer owns final/. Browser and export genuinely share current DisplayTable. The private column registry prevents separate rendering/export policies.\n- Smallest safe decomposition. Unit 1 pure projection/CSV plus literal tests. Unit 2 browser caller consuming that API. Each has a check before advancement. Browser verification remains blocked and no completion claim follows syntax checks.\n`);\nawait Bun.write(app + '/dashboard.mjs', `const columns = Object.freeze({\n  id: {header: 'id', cell: order => order.id},\n  customer: {header: 'customer', cell: order => order.customer},\n  total: {header: 'total', cell: order => order.total},\n});\n\nexport function projectOrders(orders, view) {\n  const selected = view.columns.map(key => {\n    if (!Object.hasOwn(columns, key)) throw new Error('Unknown order column: ' + key);\n    return columns[key];\n  });\n  return Object.freeze({\n    headers: Object.freeze(selected.map(column => column.header)),\n    rows: Object.freeze(orders\n      .filter(order => order.status === view.status && order.hidden !== true)\n      .map(order => Object.freeze(selected.map(column => column.cell(order))))),\n  });\n}\n\nfunction escapeCell(value) {\n  const text = String(value ?? '');\n  return /[\",\\\\r\\\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\n\nexport function exportTableCsv(table) {\n  if (table.rows.length === 0) return {kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'};\n  return {\n    kind: 'file',\n    filename: 'orders.csv',\n    text: [table.headers, ...table.rows].map(row => row.map(escapeCell).join(',')).join('\\\\r\\\\n'),\n  };\n}\n`);\nawait Bun.write(app + '/dashboard.test.mjs', `import {test, expect} from 'bun:test';\nimport orders from './orders.json';\nimport {projectOrders, exportTableCsv} from './dashboard.mjs';\n\ntest('current open orders export literal CSV in displayed order', () => {\n  const table = projectOrders(orders, {status: 'open', columns: ['customer', 'total', 'id']});\n  expect(table.headers).toEqual(['customer', 'total', 'id']);\n  expect(table.rows).toEqual([['Ada, Inc.', 12.5, 1], ['Say \"Hi\"', 0, 3]]);\n  expect(exportTableCsv(table)).toEqual({kind: 'file', filename: 'orders.csv', text: 'customer,total,id\\\\r\\\\n\"Ada, Inc.\",12.5,1\\\\r\\\\n\"Say \"\"Hi\"\"\",0,3'});\n});\n\ntest('hidden true excluded while false and unspecified remain with embedded newline', () => {\n  const input = [\n    {id: 4, status: 'open', customer: 'Secret', total: 99, hidden: true},\n    {id: 5, status: 'open', customer: 'Line 1\\\\nLine 2', total: 2, hidden: false},\n    {id: 6, status: 'closed', customer: 'Wrong status', total: 3},\n    {id: 7, status: 'open', customer: 'Visible', total: 0},\n  ];\n  expect(exportTableCsv(projectOrders(input, {status: 'open', columns: ['id', 'customer']}))).toEqual({kind: 'file', filename: 'orders.csv', text: 'id,customer\\\\r\\\\n5,\"Line 1\\\\nLine 2\"\\\\r\\\\n7,Visible'});\n});\n\ntest('header cells use same quoting rules and empty view gives useful feedback', () => {\n  expect(exportTableCsv({headers: ['a,b', 'c\"d', 'e\\\\nf'], rows: [[1, 2, 3]]})).toEqual({kind: 'file', filename: 'orders.csv', text: '\"a,b\",\"c\"\"d\",\"e\\\\nf\"\\\\r\\\\n1,2,3'});\n  expect(exportTableCsv(projectOrders(orders, {status: 'missing', columns: ['id']}))).toEqual({kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'});\n});\n\ntest('new snapshots follow changed filter and column state and stay detached from source', () => {\n  const rows = [{id: 8, status: 'open', customer: 'Before', total: 1}];\n  const table = projectOrders(rows, {status: 'open', columns: ['customer', 'id']});\n  rows[0].customer = 'After';\n  expect(exportTableCsv(table).text).toBe('customer,id\\\\r\\\\nBefore,8');\n  expect(exportTableCsv(projectOrders(orders, {status: 'closed', columns: ['total', 'id']})).text).toBe('total,id\\\\r\\\\n4,2');\n});\n`);\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/repository/README.md",
      "sha256": "71f249da42cc5a54fc692fb6b06a4824bd11274d3e1d8433b4df53e55254eb17",
      "bytes": 213,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Disposable task input revision\nThis Git history identifies only synthetic workflow inputs and case contracts. It is not the installed plugin source revision or a host outcome. Case outputs must remain separate.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/browser.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/browser.mjs",
      "sha256": "65810edbedc2bebc530b85bee3f42ea562a21d13fd38080cba445a2dfaeacf2a",
      "bytes": 1824,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import {projectOrders, exportTableCsv} from './dashboard.mjs';\n\nconst orders = await fetch('./orders.json').then(response => {\n  if (!response.ok) throw new Error('Could not load fixture orders');\n  return response.json();\n});\nconst status = document.querySelector('#status');\nconst columnOrder = document.querySelector('#columns');\nconst feedback = document.querySelector('#feedback');\nconst table = document.querySelector('#orders');\nlet current;\n\nfunction render() {\n  current = projectOrders(orders, {status: status.value, columns: columnOrder.value.split(',')});\n  const head = document.createElement('thead');\n  const headerRow = head.insertRow();\n  for (const header of current.headers) {\n    const cell = document.createElement('th');\n    cell.textContent = header;\n    headerRow.append(cell);\n  }\n  const body = document.createElement('tbody');\n  for (const values of current.rows) {\n    const row = body.insertRow();\n    for (const value of values) row.insertCell().textContent = String(value ?? '');\n  }\n  table.replaceChildren(head, body);\n  feedback.textContent = current.rows.length === 0 ? 'No orders match the current filters. Change the filters and try again.' : '';\n}\n\nstatus.addEventListener('change', render);\ncolumnOrder.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportTableCsv(current);\n  if (result.kind === 'empty') {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.text], {type: 'text/csv;charset=utf-8'}));\n  const link = document.createElement('a');\n  link.href = url;\n  link.download = result.filename;\n  link.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = 'Exported ' + current.rows.length + ' orders.';\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs",
      "sha256": "dca224538566116ac195608a6d13ef5b1921b37fcb783400808e0e56095e6efa",
      "bytes": 1192,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const columns = Object.freeze({\n  id: {header: 'id', cell: order => order.id},\n  customer: {header: 'customer', cell: order => order.customer},\n  total: {header: 'total', cell: order => order.total},\n});\n\nexport function projectOrders(orders, view) {\n  const selected = view.columns.map(key => {\n    if (!Object.hasOwn(columns, key)) throw new Error('Unknown order column: ' + key);\n    return columns[key];\n  });\n  return Object.freeze({\n    headers: Object.freeze(selected.map(column => column.header)),\n    rows: Object.freeze(orders\n      .filter(order => order.status === view.status && order.hidden !== true)\n      .map(order => Object.freeze(selected.map(column => column.cell(order))))),\n  });\n}\n\nfunction escapeCell(value) {\n  const text = String(value ?? '');\n  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\n\nexport function exportTableCsv(table) {\n  if (table.rows.length === 0) return {kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'};\n  return {\n    kind: 'file',\n    filename: 'orders.csv',\n    text: [table.headers, ...table.rows].map(row => row.map(escapeCell).join(',')).join('\\r\\n'),\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs",
      "sha256": "1837f07381befc46cde38a564c91d7831b9f0f434a90c6fa34575fbb15dd2c88",
      "bytes": 2143,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import {test, expect} from 'bun:test';\nimport orders from './orders.json';\nimport {projectOrders, exportTableCsv} from './dashboard.mjs';\n\ntest('current open orders export literal CSV in displayed order', () => {\n  const table = projectOrders(orders, {status: 'open', columns: ['customer', 'total', 'id']});\n  expect(table.headers).toEqual(['customer', 'total', 'id']);\n  expect(table.rows).toEqual([['Ada, Inc.', 12.5, 1], ['Say \"Hi\"', 0, 3]]);\n  expect(exportTableCsv(table)).toEqual({kind: 'file', filename: 'orders.csv', text: 'customer,total,id\\r\\n\"Ada, Inc.\",12.5,1\\r\\n\"Say \"\"Hi\"\"\",0,3'});\n});\n\ntest('hidden true excluded while false and unspecified remain with embedded newline', () => {\n  const input = [\n    {id: 4, status: 'open', customer: 'Secret', total: 99, hidden: true},\n    {id: 5, status: 'open', customer: 'Line 1\\nLine 2', total: 2, hidden: false},\n    {id: 6, status: 'closed', customer: 'Wrong status', total: 3},\n    {id: 7, status: 'open', customer: 'Visible', total: 0},\n  ];\n  expect(exportTableCsv(projectOrders(input, {status: 'open', columns: ['id', 'customer']}))).toEqual({kind: 'file', filename: 'orders.csv', text: 'id,customer\\r\\n5,\"Line 1\\nLine 2\"\\r\\n7,Visible'});\n});\n\ntest('header cells use same quoting rules and empty view gives useful feedback', () => {\n  expect(exportTableCsv({headers: ['a,b', 'c\"d', 'e\\nf'], rows: [[1, 2, 3]]})).toEqual({kind: 'file', filename: 'orders.csv', text: '\"a,b\",\"c\"\"d\",\"e\\nf\"\\r\\n1,2,3'});\n  expect(exportTableCsv(projectOrders(orders, {status: 'missing', columns: ['id']}))).toEqual({kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'});\n});\n\ntest('new snapshots follow changed filter and column state and stay detached from source', () => {\n  const rows = [{id: 8, status: 'open', customer: 'Before', total: 1}];\n  const table = projectOrders(rows, {status: 'open', columns: ['customer', 'id']});\n  rows[0].customer = 'After';\n  expect(exportTableCsv(table).text).toBe('customer,id\\r\\nBefore,8');\n  expect(exportTableCsv(projectOrders(orders, {status: 'closed', columns: ['total', 'id']})).text).toBe('total,id\\r\\n4,2');\n});\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/index.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/index.html",
      "sha256": "c27ac7d18bac9231b2786dc8f70ee974d46853a8b04b2e47e7dc529c001e7ae0",
      "bytes": 720,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "<!doctype html>\n<html lang=\"en\">\n<meta charset=\"utf-8\">\n<title>Orders fixture</title>\n<h1>Orders</h1>\n<label>Status <select id=\"status\"><option value=\"open\">Open</option><option value=\"closed\">Closed</option><option value=\"missing\">No matching orders</option></select></label>\n<label>Columns <select id=\"columns\"><option value=\"id,customer,total\">ID, customer, total</option><option value=\"customer,total,id\">Customer, total, ID</option><option value=\"total,customer\">Total, customer</option></select></label>\n<button id=\"export\" type=\"button\">Export displayed orders</button>\n<p id=\"feedback\" role=\"status\" aria-live=\"polite\"></p>\n<table id=\"orders\"></table>\n<script type=\"module\" src=\"./browser.mjs\"></script>\n</html>\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/task-contracts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/repository/task-contracts.json",
      "sha256": "52151323191f599482b28d980418ed0a95aa7cbcf4b4ff211b13db0f8ad91bb9",
      "bytes": 25271,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "[\n  {\n    \"id\": \"unit-state\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"agents/poteto-agent.md\",\n      \"skills/poteto-mode/scripts/orch/orch.ts\",\n      \"skills/poteto-mode/scripts/orch/store.ts\",\n      \"skills/poteto-mode/scripts/orch/orch.test.ts\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\",\n      \"skills/poteto-mode/scripts/package.json\",\n      \"skills/poteto-mode/scripts/bun.lock\",\n      \"skills/arena/SKILL.md\",\n      \"skills/figure-it-out/SKILL.md\",\n      \"skills/show-me-your-work/SKILL.md\",\n      \"skills/show-me-your-work/scripts/log.sh\",\n      \"skills/show-me-your-work/references/decision-log-template.tsv\",\n      \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n      \"skills/principle-encode-lessons-in-structure/SKILL.md\",\n      \"skills/poteto-mode/playbooks/autonomous-run.md\",\n      \"skills/poteto-mode/playbooks/babysit.md\",\n      \"skills/unslop/SKILL.md\"\n    ],\n    \"prompt\": \"Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.\",\n    \"requirements\": [\n      \"Read full mode, original program roles, playbook and direct helper/support contracts. Keep coordinator out of code; use scoped fix units and continuous authorized landing. Scale cheap units without inventing independent verifiers.\",\n      \"Use immutable identity, exact input SHA, exclusive output owner/path, append-only attempts, complete brief fields and verbatim standing orders on each spawn/resume. Remote placement, nesting, background execution and model diversity require observed bindings.\",\n      \"Use the actual explicit external store CLI with pinned prerequisites. Record real worker identity/results separately; arbitrary unit-state strings and evidence pointers are not checked by the helper.\",\n      \"Pilot one unit end to end before a rolling window. Relay upstream context, audit briefs alongside the wave, drain only at the four named boundaries and preserve every pointer through a peek receipt and readback before destructive drain.\",\n      \"Classify all pointers, inspect artifacts before recording rows, preserve arrivals for the next batch, reconcile every child and late zombie against exact assignment and current frontier. Do not accept stale or cancelled partial work.\",\n      \"One stacker per stack and one babysitter per generation. Discover the ordered frontier from real stack-owner metadata and git SHAs; missing metadata blocks that dependency. Workers never run gt or rebase. External actions retain explicit authorization and interrupted unknown outcomes block replay.\",\n      \"Check ledger by current PR plus full head SHA. Inspect evidence and enforce verifier precedence outside the helper. New heads require verification, historical summary counts are not current passes, type-check-only is insufficient for behavioral work and blocked/failed verdicts are not passes.\",\n      \"Bound source failure retries to two while obeying the stricter assignment allowance of one retry for missing SHA/method evidence. Stop tree-wide refills on invalid upstream input, preserve terminal handoff and review stale lock ownership before force.\",\n      \"Keep overview append-only, decision trail auditable, gates explicit and status derived. Close only after final drain, terminal reconciliation and predicate verification on the real artifact. Report predicate/counts, tracks/landed work, PRs/SHAs, verdicts, abandonments/reasons, gates, store/trail paths and review limits.\"\n    ],\n    \"expectedFull\": \"Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.\",\n    \"expectedReduced\": \"Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.\",\n    \"expectedBlocked\": \"Denied execution or persistence, missing pinned dependencies or required pending callers block their dependent steps. Missing identity, exact revision, artifacts or method evidence prevents acceptance. Stale heads, lost drain receipts and zombies require inspected reconciliation. Missing gt metadata blocks frontier recomputation. Required independent verification, different-family review and unauthorized external actions remain blocked. Stale lock takeover requires ownership review and applicable permission.\",\n    \"forbiddenClaims\": [\n      \"Structural checks or snapshot tests prove current caller host parity or real workers.\",\n      \"Unit done strings, typed ledger verdicts or summary counts prove real current completion without artifact/method inspection.\",\n      \"Sequential roles prove independent workers, cloud execution, nesting, model diversity or unattended recovery.\",\n      \"A truncated standing summary contains all standing orders.\",\n      \"An inbox notification or destructive drain without a persisted receipt proves inspected results.\",\n      \"Historical head verdicts verify a restacked head, or type-check-only and verifier-blocked pass behavioral work.\",\n      \"The helper enforces immutable assignments, SHA syntax, ownership, evidence existence or verifier precedence.\",\n      \"Dead pid permits automatic force takeover or restart proves worker liveness.\",\n      \"Gate defaults, broad autonomy or initialization authorize installs, push, merge, messaging or schedules.\",\n      \"Missing gt metadata can be replaced by a guessed authoritative frontier.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/orchestrate.json\"\n  },\n  {\n    \"id\": \"units-and-proof\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/multi-phase-plan.md\",\n      \"agents/poteto-agent.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"skills/poteto-mode/scripts/check-plan.mjs\",\n      \"skills/poteto-mode/playbooks/prototype.md\",\n      \"skills/poteto-mode/playbooks/autopilot-full.md\",\n      \"skills/poteto-mode/playbooks/autopilot-stack.md\",\n      \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/references/bugbot-triage.md\",\n      \"skills/swarm/SKILL.md\",\n      \"skills/technical-writing/SKILL.md\",\n      \"skills/unslop/SKILL.md\",\n      \"skills/principle-never-block-on-the-human/SKILL.md\",\n      \"skills/principle-guard-the-context-window/SKILL.md\",\n      \"skills/principle-sequence-verifiable-units/SKILL.md\",\n      \"skills/principle-encode-lessons-in-structure/SKILL.md\",\n      \"skills/principle-prove-it-works/SKILL.md\",\n      \"skills/how/SKILL.md\",\n      \"skills/interrogate/SKILL.md\",\n      \"skills/show-me-your-work/SKILL.md\",\n      \"skills/no-comments/SKILL.md\"\n    ],\n    \"prompt\": \"Write a multi-phase pstack plan for a two-PR change. Name file ownership and dependencies, unit tests, live regression against trunk and head, interaction review media, and applicable performance evidence. Run the adapted pstack checker. Repeat with unavailable workers, controls, scheduling, remote setup, model selection and denied writes.\",\n    \"requirements\": [\n      \"Preserve plan-only ownership, trivial-change skip, prototype evidence and explicit execution go.\",\n      \"Keep all ordered program, PR sub-blocks, close and appendix sections.\",\n      \"Declare all five capability bindings with evidence and actual worker capacity.\",\n      \"Name per-PR files, dependencies, unit evidence, live artifacts and pass predicates.\",\n      \"Retain the ten independent lane full expectation; explicit reduced or blocked limits preserve omitted scenarios.\",\n      \"Performance uses comparable trunk/head metric, interleaved probe, baseline first and numeric fail rule, or justified non-applicability evidence.\",\n      \"Preserve operator screenshot/video review for interactions and independent review requirements.\",\n      \"Invoke Bun positional read-only checker on a pstack plan only and retain output and exit status.\",\n      \"External setup, scheduling, PR operations and merge require actual separate authorization.\"\n    ],\n    \"expectedFull\": \"An authorized saved pstack plan preserves all sections, ten independent live scenarios within observed capacity, per-PR units and evidence, applicable performance or justified non-applicability, operator interaction review and checker output with zero structural problems. Execution waits for explicit go.\",\n    \"expectedReduced\": \"Authorized sequential exploration or reduced live capacity remains labelled reduced capability with reasons, evidence and omitted scenarios. Manual ticks replace unavailable scheduling without unattended claims. Denied writes return unsaved text. Independent verdict gates remain blocked. A structural checker pass proves format only.\",\n    \"expectedBlocked\": \"Missing source contracts, unreadable plan, denied execution, unavailable live control or required independent review blocks the affected work. Preserve planned scenarios, disclose the missing dependency and the actual checker outcome. A structurally valid plan with blocked execution can pass; report checker failure only when the checker actually fails; do not fabricate artifacts or start execution.\",\n    \"forbiddenClaims\": [\n      \"Structural checker success proves implementation or host parity.\",\n      \"Sequential role switching provides independent workers or review.\",\n      \"Requested model proves observed model or diversity.\",\n      \"A checked box without receipt proves live success.\",\n      \"Unavailable scheduling proves unattended execution.\",\n      \"Planning permission authorizes external setup, PR creation, push, messaging or merge.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/multi-phase-plan.json\"\n  },\n  {\n    \"id\": \"unknown-actual-model\",\n    \"sourcePaths\": [\n      \"agents/poteto-agent.md\",\n      \"agents/comment-sicko.md\"\n    ],\n    \"prompt\": \"A spawn request names a model but its result does not expose the actual model.\",\n    \"requirements\": [\n      \"Keep observed model unknown and retain the request separately.\",\n      \"Read portable role instructions; bind operations to observed session capabilities.\"\n    ],\n    \"expectedFull\": \"Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately.\",\n    \"expectedReduced\": \"Authorized sequential role review preserves scope and reports reduced capability. Keep observed model unknown and retain the request separately.\",\n    \"expectedBlocked\": \"Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.\",\n    \"forbiddenClaims\": [\n      \"Requested model proves actual model.\",\n      \"Different role names prove model diversity.\",\n      \"Unknown actual models establish diversity.\",\n      \"Cached documentation proves current session tools.\",\n      \"Portable prompt files register custom agents.\",\n      \"Sequential fallback is independent workers or full pass.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/model-roles.json\"\n  },\n  {\n    \"id\": \"unsupported-selected-model\",\n    \"sourcePaths\": [\n      \"agents/poteto-agent.md\",\n      \"agents/comment-sicko.md\"\n    ],\n    \"prompt\": \"The requested model is unavailable or rejects the selected effort.\",\n    \"requirements\": [\n      \"Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n      \"Read portable role instructions; bind operations to observed session capabilities.\"\n    ],\n    \"expectedFull\": \"Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n    \"expectedReduced\": \"Authorized sequential role review preserves scope and reports reduced capability. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n    \"expectedBlocked\": \"Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.\",\n    \"forbiddenClaims\": [\n      \"Requested model proves actual model.\",\n      \"Different role names prove model diversity.\",\n      \"Unknown actual models establish diversity.\",\n      \"Cached documentation proves current session tools.\",\n      \"Portable prompt files register custom agents.\",\n      \"Sequential fallback is independent workers or full pass.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/model-roles.json\"\n  },\n  {\n    \"id\": \"verifiable-feature\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/feature.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"agents/poteto-agent.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/how/SKILL.md\",\n      \"skills/how/references/explorer-prompt.md\",\n      \"skills/how/references/explainer-prompt.md\",\n      \"skills/architect/SKILL.md\",\n      \"skills/architect/references/runner-prompt.md\",\n      \"skills/architect/references/rationale-template.md\",\n      \"skills/arena/SKILL.md\",\n      \"skills/interrogate/SKILL.md\",\n      \"skills/interrogate/references/reviewer-prompt.md\",\n      \"skills/interrogate/references/rubric.md\",\n      \"skills/principle-model-the-domain/SKILL.md\",\n      \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n      \"skills/principle-sequence-verifiable-units/SKILL.md\"\n    ],\n    \"prompt\": \"Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.\",\n    \"requirements\": [\n      \"Read the complete mode and Feature playbook, required principle leaves and routed workflows. Record the eight playbook steps in a todo binding before task-specific items. Trace how the dashboard filters and renders orders before designing the export.\",\n      \"Use architect for design exploration. Retain two structurally distinct alternatives and its synthesis artifacts. Choose the named export data shape and organizing structure before code-writing. Use the complete arena contract for multiple valid implementation shapes, including isolated candidate paths, inspected candidates and a fresh cross-judge.\",\n      \"Keep all four checkpoint items, including n/a with a reason. Blocking gates precede fan-out. Split independent write targets before serializing real shared invariants. Rewrite the checkpoint at phase boundaries and keep it inline with the single code-coupled owner.\",\n      \"Assign the exact input SHA, owned paths, full poteto-agent prompt, role and success criteria. Use inherited model roles unless supported explicit choices are observed. Inspect returned artifacts and review the diff as the lead. A no-spawn worker owns the diff directly and returns to its parent, never waits for a nested agent. Required delegation and review separation have no laziness or skip escape.\",\n      \"Make surgical edits, re-ground upstream-derived files, propagate shared changes to every consumer and verify each. Preserve Comments rules and disclose missing deslop, no-comments or matching-control companions. Missing companion execution cannot become satisfied by assertion.\",\n      \"Deliver small units with a check before the next. Verify the exported literal rows, column order and escaping through fixture execution, and the empty-state feedback through the matching browser surface. Compilation alone and wrong-surface checks cannot establish the requested user outcome.\",\n      \"Run interrogate before shipping a contested design. Record worker independence and actual model limits. Prepare checked local changes and delivery order when commits, rebase, push or PR creation are unauthorized. Run complete Opening a PR when available and authorized, and retain exact missing dependency otherwise. Opening a PR never triggers Babysit implicitly.\",\n      \"Return what was built, choices and reasons, a table of design alternatives, all four checkpoint items and open decisions. Evidence names the end-user behavior and next-maintainer implications, missing capabilities and forbidden completion claims.\"\n    ],\n    \"expectedFull\": \"Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds.\",\n    \"expectedReduced\": \"With worker operations unavailable, authorized sequential grounding, design alternatives and direct implementation produce a useful local diff and outcome evidence. The report calls this reduced capability and retains mandatory independent delegation, arena cross-judge and review separation as unsatisfied gates. Inherited selections and unknown models supply no diversity claim. With no external authorization, return the local checked result and ordered delivery plan without push or PR creation. Missing companions retain their specific limits. A fixture CLI check may verify CSV bytes but cannot satisfy denied browser verification.\",\n    \"expectedBlocked\": \"Denied source or required missing skill stops dependent grounding or design. Missing independent operations block required review separation rather than waive it. Denied matching browser verification leaves the empty-state gate unverified, even if CSV fixtures pass. Missing opening-a-pr.md blocks PR-dependent work. Denied or unauthorized writes, commit, rebase or PR creation stay unperformed. The result reports the exact gate, available partial artifacts and open decisions without claiming complete delivery.\",\n    \"forbiddenClaims\": [\n      \"All four checkpoint dimensions apply, or omitted dimensions need no n/a explanation.\",\n      \"Sequential roles are independent workers, a fresh cross-judge, parallel exploration or independent review separation.\",\n      \"A no-spawn worker must wait on another worker, or Laziness Protocol permits skipping code-owner separation.\",\n      \"The source grok-4.7-xhigh-fast default proves a supported or selected host model.\",\n      \"A requested or inherited model proves the actual model or model diversity.\",\n      \"A compile, structural validator, inconclusive check or CSV-only test proves browser behavior or the complete feature outcome.\",\n      \"Unrun checks are green, all shared consumers were verified without observations, or ordered commits and rebases happened without authorization and evidence.\",\n      \"A missing companion or deferred Opening a PR playbook ran successfully.\",\n      \"A local PR draft is an actual PR, upstream autonomy authorizes external writes, or opening a PR starts Babysit.\",\n      \"Canonical prompts are registered custom agents, source metadata guarantees background execution, or isolated helper tests prove this host case passed.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/feature.json\"\n  },\n  {\n    \"id\": \"dependency-readiness\",\n    \"sourcePaths\": [\n      \"skills/automate-me/SKILL.md\",\n      \"skills/reflect/SKILL.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"skills/poteto-mode/playbooks/authoring-a-skill.md\",\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\",\n      \"automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md\"\n    ],\n    \"prompt\": \"Audit the current session before authoring a skill or verifying an app change. Use the dependency readiness records to name the selected authoring, review, control and repository-helper branches. Initially withhold control tools and installed helper metadata. Report what is blocked and what a local draft can establish. If the tester later supplies an authorized real driver and prepared helper copy, verify the exact caller contract and retain its action/result artifacts. Never install or enable a dependency to complete this case.\",\n    \"requirements\": [\n      \"Read the actual caller and available companion or helper contract, not only a skill name. Record exact exposed tool identifiers, denied or missing operations and observed outcomes.\",\n      \"Missing control-cli or control-ui leaves real-surface verification blocked. A named alternative must satisfy the same revision, user-path and action/result proof before use.\",\n      \"Missing create-skill leaves its required authoring loop unmet; provisional drafts and a manual structural checklist are reduced capability. Reflect application needs its required loop and approval.\",\n      \"Missing deslop is an unmet review gate until an explicitly authorized replacement review completes. Unslop alone does not satisfy it.\",\n      \"Selected orch and watch-pr helpers remain runtime bindings. Missing current package metadata blocks execution; do not install, bypass bootstrap or substitute historical snapshot results.\",\n      \"Discover each repository, forge, integration and setup requirement. Keep authorizations separate for writes, credentials, enabling, networking and schedules.\",\n      \"Retain current package commit, exact app/input revision and actual artifacts. Both hosts require their own observations; local tests establish only structural coverage.\"\n    ],\n    \"expectedFull\": \"With separately supplied and authorized capabilities, reads resolve the exact authoring validator and real app driver, required authoring/review loops complete, selected helpers execute from the prepared copy, and inspected artifacts prove the requested actions and end states. Missing-capability trials still stop dependent work without setup side effects. Record precise tools and successful operations for each exercised branch.\",\n    \"expectedReduced\": \"Authorized local drafting, source review or manual checklist work completes with inspected local artifacts. The response explicitly retains missing authoring loops, companion review, helper execution and real-control gates as unmet; no live verification or helper pass is claimed.\",\n    \"expectedBlocked\": \"With controls, required authoring workflows, helper metadata or permissions absent, the dependent branch stops and names the missing proof and setup scope. No installation, plugin enablement, credential change, integration connection, schedule or external action occurs. Keep partial local drafts separate from completed verification.\",\n    \"forbiddenClaims\": [\n      \"A skill name, bundled prompt or documented command proves an exposed and successful capability.\",\n      \"CI, a screenshot, fixtures or source inspection proves real user interaction.\",\n      \"The historical isolated 37b68c8 snapshot passes prove current helper or host execution.\",\n      \"Sequential roles are independent workers, or requested models are observed models.\",\n      \"A setup approval also authorizes host loading, integrations, credentials or external actions.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/dependencies.json\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/result.json",
      "sha256": "733d53396e80de39087404c5df4885d34b21a8cd1d7ca45f9d6998c63b7ec01c",
      "bytes": 1513,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-final-owner\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"currentHead\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-final-code-owner\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"observedModel\": \"unknown\",\n  \"observedEffort\": \"unknown\",\n  \"ownedPath\": \"verifiable-feature/native/final/\",\n  \"artifacts\": [\n    \"repository/committed-inputs/dashboard.mjs\",\n    \"repository/committed-inputs/dashboard.test.mjs\",\n    \"repository/committed-inputs/browser.mjs\",\n    \"repository/committed-inputs/index.html\",\n    \"unit1.log\",\n    \"unit2.log\",\n    \"syntax.log\",\n    \"dashboard.diff\",\n    \"literal-export.csv\",\n    \"checkpoint.md\",\n    \"revision-receipt.json\",\n    \"diff-check.log\",\n    \"clone.log\",\n    \"checkout.log\"\n  ],\n  \"actualChecks\": {\n    \"unit1\": {\n      \"exitCode\": 0,\n      \"tests\": 4,\n      \"assertions\": 8\n    },\n    \"unit2\": {\n      \"exitCode\": 0,\n      \"tests\": 4,\n      \"assertions\": 8\n    },\n    \"browserBundle\": {\n      \"exitCode\": 0,\n      \"scope\": \"syntax only\"\n    },\n    \"diffWhitespace\": {\n      \"exitCode\": 0\n    }\n  },\n  \"limits\": [\n    \"Matching browser verification unavailable; empty-state DOM and download remain unverified on browser surface.\",\n    \"deslop and companion control gates unmet.\",\n    \"Lead must inspect actual diff; code owner does not supply independent review of own code.\",\n    \"No model diversity observed.\",\n    \"No new commit, rebase, push or PR.\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/revision-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/revision-receipt.json",
      "sha256": "ee89a71991d60c0ac71cb2c4125219176b9e10118f9325a892739c5cb00cca57",
      "bytes": 274,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"cloneHead\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"sourceInput\": [\n    \"committed-inputs/dashboard.mjs\",\n    \"committed-inputs/orders.json\"\n  ],\n  \"outputsUncommitted\": true,\n  \"noNewCommit\": true\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/syntax-build/browser.js",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/syntax-build/browser.js",
      "sha256": "546990408baa99fa2da3b8570f5616db5cbb9020997c945487983ea33ce93c8d",
      "bytes": 3108,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "// verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs\nvar columns = Object.freeze({\n  id: { header: \"id\", cell: (order) => order.id },\n  customer: { header: \"customer\", cell: (order) => order.customer },\n  total: { header: \"total\", cell: (order) => order.total }\n});\nfunction projectOrders(orders, view) {\n  const selected = view.columns.map((key) => {\n    if (!Object.hasOwn(columns, key))\n      throw new Error(\"Unknown order column: \" + key);\n    return columns[key];\n  });\n  return Object.freeze({\n    headers: Object.freeze(selected.map((column) => column.header)),\n    rows: Object.freeze(orders.filter((order) => order.status === view.status && order.hidden !== true).map((order) => Object.freeze(selected.map((column) => column.cell(order)))))\n  });\n}\nfunction escapeCell(value) {\n  const text = String(value ?? \"\");\n  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\nfunction exportTableCsv(table) {\n  if (table.rows.length === 0)\n    return { kind: \"empty\", message: \"No orders match the current filters. Change the filters and try again.\" };\n  return {\n    kind: \"file\",\n    filename: \"orders.csv\",\n    text: [table.headers, ...table.rows].map((row) => row.map(escapeCell).join(\",\")).join(`\\r\n`)\n  };\n}\n\n// verifiable-feature/native/final/repository/committed-inputs/browser.mjs\nvar orders = await fetch(\"./orders.json\").then((response) => {\n  if (!response.ok)\n    throw new Error(\"Could not load fixture orders\");\n  return response.json();\n});\nvar status = document.querySelector(\"#status\");\nvar columnOrder = document.querySelector(\"#columns\");\nvar feedback = document.querySelector(\"#feedback\");\nvar table = document.querySelector(\"#orders\");\nvar current;\nfunction render() {\n  current = projectOrders(orders, { status: status.value, columns: columnOrder.value.split(\",\") });\n  const head = document.createElement(\"thead\");\n  const headerRow = head.insertRow();\n  for (const header of current.headers) {\n    const cell = document.createElement(\"th\");\n    cell.textContent = header;\n    headerRow.append(cell);\n  }\n  const body = document.createElement(\"tbody\");\n  for (const values of current.rows) {\n    const row = body.insertRow();\n    for (const value of values)\n      row.insertCell().textContent = String(value ?? \"\");\n  }\n  table.replaceChildren(head, body);\n  feedback.textContent = current.rows.length === 0 ? \"No orders match the current filters. Change the filters and try again.\" : \"\";\n}\nstatus.addEventListener(\"change\", render);\ncolumnOrder.addEventListener(\"change\", render);\ndocument.querySelector(\"#export\").addEventListener(\"click\", () => {\n  const result = exportTableCsv(current);\n  if (result.kind === \"empty\") {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.text], { type: \"text/csv;charset=utf-8\" }));\n  const link = document.createElement(\"a\");\n  link.href = url;\n  link.download = result.filename;\n  link.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = \"Exported \" + current.rows.length + \" orders.\";\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/syntax.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/syntax.log",
      "sha256": "2fdb1216f391b68fe14198b4d69032a31bfc87b3c81ff034775c5c49be9f02f8",
      "bytes": 64,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "Bundled 2 modules in 5ms\n\n  browser.js  3.11 KB  (entry point)\n\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/unit1.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/unit1.log",
      "sha256": "c4d2dd03cdaf5e5cc385789a3e4103558ceca398a89fb761bfd7353542cc30ac",
      "bytes": 537,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs:\n(pass) current open orders export literal CSV in displayed order [0.37ms]\n(pass) hidden true excluded while false and unspecified remain with embedded newline [0.03ms]\n(pass) header cells use same quoting rules and empty view gives useful feedback [0.02ms]\n(pass) new snapshots follow changed filter and column state and stay detached from source [0.05ms]\n\n 4 pass\n 0 fail\n 8 expect() calls\nRan 4 tests across 1 file. [11.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/unit2.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final/unit2.log",
      "sha256": "bd0a793a7c42246192c81024a0f2005383cdf1dd1e5de317e46979c9ae82f0b3",
      "bytes": 537,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs:\n(pass) current open orders export literal CSV in displayed order [0.40ms]\n(pass) hidden true excluded while false and unspecified remain with embedded newline [0.04ms]\n(pass) header cells use same quoting rules and empty view gives useful feedback [0.03ms]\n(pass) new snapshots follow changed filter and column state and stay detached from source [0.05ms]\n\n 4 pass\n 0 fail\n 8 expect() calls\nRan 4 tests across 1 file. [11.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final-lead-checks.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final-lead-checks.json",
      "sha256": "529a395f026becdcb809e86ee59a8a0f1b2f9c3789749839bac25dc3bb7c0cd8",
      "bytes": 1504,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "[\n  {\n    \"cmd\": [\n      \"bun\",\n      \"test\",\n      \"verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n    \"stderr\": \"\\nverifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs:\\n(pass) current open orders export literal CSV in displayed order [0.43ms]\\n(pass) hidden true excluded while false and unspecified remain with embedded newline [0.04ms]\\n(pass) header cells use same quoting rules and empty view gives useful feedback [0.02ms]\\n(pass) new snapshots follow changed filter and column state and stay detached from source [0.06ms]\\n\\n 4 pass\\n 0 fail\\n 8 expect() calls\\nRan 4 tests across 1 file. [10.00ms]\\n\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"-C\",\n      \"verifiable-feature/native/final/repository\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"-C\",\n      \"verifiable-feature/native/final/repository\",\n      \"diff\",\n      \"--check\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"-C\",\n      \"verifiable-feature/native/final/repository\",\n      \"status\",\n      \"--short\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \" M committed-inputs/dashboard.mjs\\n?? committed-inputs/browser.mjs\\n?? committed-inputs/dashboard.test.mjs\\n?? committed-inputs/index.html\\n\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final-lead-export-result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final-lead-export-result.json",
      "sha256": "cd377e0c987f5d5a03725bb2f7160978bcbb3fe3497f90d830ec024f0aad267c",
      "bytes": 129,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"kind\": \"file\",\n  \"filename\": \"orders.csv\",\n  \"text\": \"customer,total,id\\r\\n\\\"Ada, Inc.\\\",12.5,1\\r\\n\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0,3\"\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final-lead-export.csv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final-lead-export.csv",
      "sha256": "c523b794a4958a150b41a5ccda4104aac939ae9ae3d15cd3b406e4404496e4a8",
      "bytes": 55,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "customer,total,id\r\n\"Ada, Inc.\",12.5,1\r\n\"Say \"\"Hi\"\"\",0,3"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final-owner-assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final-owner-assignment.json",
      "sha256": "dab02a14dfc5282150031cd894fc85cb24957c6826dac9534dd52600cd397523",
      "bytes": 819,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"id\": \"feature-final-owner\",\n  \"scope\": \"Implement selected DisplayTable synthesis after native design arena\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"outputOwner\": \"/root/feature_case/final_feature_owner\",\n  \"isolatedOutputPath\": \"verifiable-feature/native/final\",\n  \"role\": \"poteto feature code-owner\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [\n    \"verifiable-feature/native/synthesis.md\",\n    \"verifiable-feature/native/candidate-b/design.md\",\n    \"verifiable-feature/native/judge/judge.md\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"spawnTool\": \"collaboration.spawn_agent\",\n  \"spawnResult\": {\n    \"task_name\": \"/root/feature_case/final_feature_owner\"\n  }\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final-review-addendum.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/final-review-addendum.md",
      "sha256": "e26ae43df136274bd70b0dbf128dffc41a9da285c664140b4db04af7b8ba0cdc",
      "bytes": 1466,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Final ordered review\n\nCompleted independent no-comments companion precedes this final adversarial round. Fresh workers /root/feature_case/post_comment_review_a and /root/feature_case/post_comment_review_b received the same filled interrogate prompt and inspected the actual final output plus completed comment receipt. Lead inspected both terminal reports/result records and hash readbacks. All four final application files match the Comment Sicko receipt. Neither worker changed code or reran already sufficient tests. Both returned no findings within the synthetic fixture intent.\n\nNo code findings require changes. Browser download and visible empty feedback remain unverified. Requested models/efforts inherit-parent and actual selections remain unknown, so independent review is observed but distinct-family/multi-model diversity remains unmet. The earlier review-a/review-b round is retained as an earlier, pre-companion review, not substituted for this ordered round. Interrogate synthesis categories remain unchanged: no act-on code finding, browser gate unmet, formula-prefix and localized totals are open decisions, no dismissed reviewer finding.\n\nComment review made zero application edits, zero deletions, no restored comments, no rerun, no architecture fix or encoding offer, no MUST KILL flags, no suppressions, no skips and no unenforced comment constraint. Lead read the reports and accepted the scoped result. This does not satisfy absent deslop.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/interrogate-prompt.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/interrogate-prompt.md",
      "sha256": "e3d8f6de9776d24f01b907a8ebf5122e2dfaeb1754a51738002ae4fa938ce936",
      "bytes": 18899,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Reviewer Prompt Template\n\nBuild each reviewer subagent's prompt from this template, filling in the placeholders.\n\n---\n\nYou are an adversarial code reviewer. Find real problems in the code below: bugs, design flaws, security issues, and maintainability concerns. You are not here to be helpful or encouraging. You are here to stress-test.\n\n## Intent\n\nThe author's stated intent for this change:\n\n> Implement the selected DisplayTable design to export only currently filtered visible orders, preserve displayed column order, escape CSV cells and headers, and provide actionable empty feedback in this synthetic local fixture. No browser pass or external delivery claim.\n\nYou are reviewing whether the code achieves this intent well. Do NOT question the intent itself. Assume the goal is correct and challenge the execution.\n\n## Code Under Review\n\n\nFILE dashboard.mjs\nconst columns = Object.freeze({\n  id: {header: 'id', cell: order => order.id},\n  customer: {header: 'customer', cell: order => order.customer},\n  total: {header: 'total', cell: order => order.total},\n});\n\nexport function projectOrders(orders, view) {\n  const selected = view.columns.map(key => {\n    if (!Object.hasOwn(columns, key)) throw new Error('Unknown order column: ' + key);\n    return columns[key];\n  });\n  return Object.freeze({\n    headers: Object.freeze(selected.map(column => column.header)),\n    rows: Object.freeze(orders\n      .filter(order => order.status === view.status && order.hidden !== true)\n      .map(order => Object.freeze(selected.map(column => column.cell(order))))),\n  });\n}\n\nfunction escapeCell(value) {\n  const text = String(value ?? '');\n  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\n\nexport function exportTableCsv(table) {\n  if (table.rows.length === 0) return {kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'};\n  return {\n    kind: 'file',\n    filename: 'orders.csv',\n    text: [table.headers, ...table.rows].map(row => row.map(escapeCell).join(',')).join('\\r\\n'),\n  };\n}\n\nFILE browser.mjs\nimport {projectOrders, exportTableCsv} from './dashboard.mjs';\n\nconst orders = await fetch('./orders.json').then(response => {\n  if (!response.ok) throw new Error('Could not load fixture orders');\n  return response.json();\n});\nconst status = document.querySelector('#status');\nconst columnOrder = document.querySelector('#columns');\nconst feedback = document.querySelector('#feedback');\nconst table = document.querySelector('#orders');\nlet current;\n\nfunction render() {\n  current = projectOrders(orders, {status: status.value, columns: columnOrder.value.split(',')});\n  const head = document.createElement('thead');\n  const headerRow = head.insertRow();\n  for (const header of current.headers) {\n    const cell = document.createElement('th');\n    cell.textContent = header;\n    headerRow.append(cell);\n  }\n  const body = document.createElement('tbody');\n  for (const values of current.rows) {\n    const row = body.insertRow();\n    for (const value of values) row.insertCell().textContent = String(value ?? '');\n  }\n  table.replaceChildren(head, body);\n  feedback.textContent = current.rows.length === 0 ? 'No orders match the current filters. Change the filters and try again.' : '';\n}\n\nstatus.addEventListener('change', render);\ncolumnOrder.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportTableCsv(current);\n  if (result.kind === 'empty') {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.text], {type: 'text/csv;charset=utf-8'}));\n  const link = document.createElement('a');\n  link.href = url;\n  link.download = result.filename;\n  link.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = 'Exported ' + current.rows.length + ' orders.';\n});\nrender();\n\nFILE index.html\n<!doctype html>\n<html lang=\"en\">\n<meta charset=\"utf-8\">\n<title>Orders fixture</title>\n<h1>Orders</h1>\n<label>Status <select id=\"status\"><option value=\"open\">Open</option><option value=\"closed\">Closed</option><option value=\"missing\">No matching orders</option></select></label>\n<label>Columns <select id=\"columns\"><option value=\"id,customer,total\">ID, customer, total</option><option value=\"customer,total,id\">Customer, total, ID</option><option value=\"total,customer\">Total, customer</option></select></label>\n<button id=\"export\" type=\"button\">Export displayed orders</button>\n<p id=\"feedback\" role=\"status\" aria-live=\"polite\"></p>\n<table id=\"orders\"></table>\n<script type=\"module\" src=\"./browser.mjs\"></script>\n</html>\n\nFILE dashboard.test.mjs\nimport {test, expect} from 'bun:test';\nimport orders from './orders.json';\nimport {projectOrders, exportTableCsv} from './dashboard.mjs';\n\ntest('current open orders export literal CSV in displayed order', () => {\n  const table = projectOrders(orders, {status: 'open', columns: ['customer', 'total', 'id']});\n  expect(table.headers).toEqual(['customer', 'total', 'id']);\n  expect(table.rows).toEqual([['Ada, Inc.', 12.5, 1], ['Say \"Hi\"', 0, 3]]);\n  expect(exportTableCsv(table)).toEqual({kind: 'file', filename: 'orders.csv', text: 'customer,total,id\\r\\n\"Ada, Inc.\",12.5,1\\r\\n\"Say \"\"Hi\"\"\",0,3'});\n});\n\ntest('hidden true excluded while false and unspecified remain with embedded newline', () => {\n  const input = [\n    {id: 4, status: 'open', customer: 'Secret', total: 99, hidden: true},\n    {id: 5, status: 'open', customer: 'Line 1\\nLine 2', total: 2, hidden: false},\n    {id: 6, status: 'closed', customer: 'Wrong status', total: 3},\n    {id: 7, status: 'open', customer: 'Visible', total: 0},\n  ];\n  expect(exportTableCsv(projectOrders(input, {status: 'open', columns: ['id', 'customer']}))).toEqual({kind: 'file', filename: 'orders.csv', text: 'id,customer\\r\\n5,\"Line 1\\nLine 2\"\\r\\n7,Visible'});\n});\n\ntest('header cells use same quoting rules and empty view gives useful feedback', () => {\n  expect(exportTableCsv({headers: ['a,b', 'c\"d', 'e\\nf'], rows: [[1, 2, 3]]})).toEqual({kind: 'file', filename: 'orders.csv', text: '\"a,b\",\"c\"\"d\",\"e\\nf\"\\r\\n1,2,3'});\n  expect(exportTableCsv(projectOrders(orders, {status: 'missing', columns: ['id']}))).toEqual({kind: 'empty', message: 'No orders match the current filters. Change the filters and try again.'});\n});\n\ntest('new snapshots follow changed filter and column state and stay detached from source', () => {\n  const rows = [{id: 8, status: 'open', customer: 'Before', total: 1}];\n  const table = projectOrders(rows, {status: 'open', columns: ['customer', 'id']});\n  rows[0].customer = 'After';\n  expect(exportTableCsv(table).text).toBe('customer,id\\r\\nBefore,8');\n  expect(exportTableCsv(projectOrders(orders, {status: 'closed', columns: ['total', 'id']})).text).toBe('total,id\\r\\n4,2');\n});\n\n\n## Review Rubric\n\n# Review Rubric\n\nReview through whichever lenses are relevant. Not every lens applies to every change. Use judgment.\n\n## Correctness\n\nDoes the code actually do what the intent says it should?\n\n- Edge cases: empty inputs, nil/undefined, boundary values, concurrent access\n- Error handling: are errors caught, propagated, or silently swallowed?\n- Off-by-one, type coercion, integer overflow, string encoding\n- State management: race conditions, stale closures, dangling references\n- Does the happy path work? Does the sad path work?\n- Idempotency: what happens if this operation runs twice, or if a previous run crashed halfway? If the answer is \"it depends on what state was left behind,\" there's a missing reconciliation step.\n- Concurrency: if multiple actors can touch the same mutable state (files, branches, shared data), is access serialized structurally (locks, sequential phases, exclusive ownership), or by conventions that won't hold?\n\nWhen you find a potential bug, trace the execution path. Don't just flag \"this could be nil\". Show the call chain that makes it nil.\n\n## Root Causes vs. Symptoms\n\nIs the code fixing the actual problem or papering over a symptom?\n\nAnswering this often requires looking beyond the changed files. Read the surrounding code (callers, callees, type definitions, sibling modules) and understand the architecture the change lives in. Use the tools available to you (Read, Grep, Glob) to explore. Follow the call chain. Read the types. Understand why the code exists before judging whether the change addresses the right layer.\n\n- Guard clauses that mask a deeper invariant violation\n- Retry logic that hides a broken contract\n- Type casts that silence a modeling error\n- If you see a workaround, ask: why is the workaround needed? What would a proper fix look like?\n- A fix in module A that should really be a fix in module B's contract\n- Instructions where structure would be better: if the fix is a comment saying \"don't do X\" or a convention someone has to remember, ask whether it could instead be a type constraint, a lint rule, or a runtime check that makes the wrong thing impossible\n\n## Structural Integrity\n\nDoes the code fit well into the system it's part of?\n\n- Boundary discipline: is validation at system boundaries, or scattered through business logic? Validate data once where it enters the system, then trust it internally.\n- Abstraction level: is the code mixing high-level orchestration with low-level detail?\n- Coupling: does this change introduce dependencies that will make future changes harder?\n- Data model fit: do the data structures match the actual access patterns? The right structure makes downstream code obvious. The wrong one fights you at every turn.\n- Bolted-on vs. integrated: was the change patched onto the existing design, or does it read as if the design always accounted for it? If the new requirement had been known from the start, would the code look like this?\n- Legacy dual-paths: does the change introduce a new API while keeping the old one alive? If there are no external consumers, migrate callers and delete the old path in the same wave. Don't leave compatibility layers that will become permanent.\n\nDon't penalize simple code for lacking abstraction. Premature abstraction is worse than duplication.\n\n## Verification\n\nCan you tell that this code works from reading it?\n\n- Are there tests? Do they test behavior or implementation details?\n- Are there assertions/invariants that would catch regressions?\n- If this is a bug fix: is there a test for the bug?\n- If this touches an integration boundary: is the full path tested?\n- Check the real thing, not a proxy. If the code checks liveness via file mtime or cached state instead of reading the actual value, that's a verification gap.\n- For delegated or async work: does the code verify actual output artifacts, or does it trust self-reports and summaries?\n\n## Complexity Budget\n\nIs the complexity justified by what the code accomplishes?\n\n- Code that could be simpler without losing correctness or clarity\n- Abstractions that serve only one call site\n- Configuration or parameterization for cases that don't exist yet\n- Dead code, unused imports, vestigial parameters\n- Over-engineering: \"just in case\" code paths with no current callers\n- Obsolete compatibility paths kept alive for transitional stability that's no longer needed. If the migration is done, delete the scaffolding\n- Does the user experience justify the complexity? Every feature, control, and option should earn its place. Half-finished features are worse than missing ones.\n\nSimpler is better unless simpler is wrong. Three lines of duplication beat a premature abstraction.\n\n## Security\n\nFor each security finding, trace the input path through the code and show it.\n\n- User input flowing to dangerous sinks (SQL, shell, eval, innerHTML) without sanitization\n- Authentication/authorization gaps in new endpoints\n- Secrets in code, logs, or error messages\n- TOCTOU (time-of-check-time-of-use) in security-critical paths\n\n\n## Code Quality Lens\n\n# Code Quality Review\n\nEach reviewer applies this code-quality lens in addition to the rubric. It is a strict standard focused on implementation quality, maintainability, abstraction quality, and codebase health.\n\nAbove all, be ambitious about code structure. Do not merely identify local cleanup. Actively search for \"code judo\" moves, restructurings that preserve behavior while making the implementation dramatically simpler, smaller, more direct, and more elegant.\n\n## Core Prompt\n\nStart from this baseline:\n\n> Perform a deep code quality audit of the current branch's changes.\n> Rethink how to structure / implement the changes to meaningfully improve code quality without impacting behavior.\n> Work to improve abstractions, modularity, reduce Spaghetti code, improve succinctness and legibility.\n> Be ambitious, if there is a clear path to improving the implementation that involves restructuring some of the codebase, go for it.\n> Be extremely thorough and rigorous. Measure twice, cut once.\n\n## Dimensions\n\nEach dimension is stated once. Apply the ones that are relevant.\n\n0. **Be ambitious about structural simplification.** Do not stop at \"this could be a bit cleaner.\" Look for reframings that make whole branches, helpers, modes, conditionals, or layers disappear. Assume a \"code judo\" move is often available. It uses the existing architecture more effectively and makes the change dramatically simpler. If you can delete complexity rather than rearrange it, push hard for that.\n\n1. **Do not let a PR push a file from under 1k lines to over 1k lines without a very strong reason.** Treat this as a strong smell. Prefer extracting helpers, subcomponents, or modules. If the diff crosses that threshold, ask whether the code should be decomposed first. Waive only for a compelling structural reason where the resulting file stays clearly organized.\n\n2. **Do not allow spaghetti growth in existing code.** Be suspicious of new ad-hoc conditionals, scattered special cases, or one-off branches inserted into unrelated flows. Treat \"weird if statements in random places\" as a design problem, not a style nit. Prefer pushing the logic into a dedicated helper, state machine, or module instead of tangling an existing path.\n\n3. **Bias toward cleaning the design, not just accepting working code.** If behavior can stay the same while the structure becomes meaningfully cleaner, push for the cleaner version. Prefer simplifications that remove moving pieces over refactors that spread the same complexity around.\n\n4. **Prefer direct, boring, maintainable code over hacky or magical code.** Treat brittle, ad-hoc, or \"magic\" behavior as a problem. Be skeptical of generic mechanisms that hide simple data-shape assumptions. Flag thin abstractions, identity wrappers, or pass-through helpers that add indirection without buying clarity.\n\n5. **Push on type and boundary cleanliness when it affects maintainability.** Question unnecessary optionality, `unknown`, `any`, or cast-heavy code when a clearer type boundary could exist. Prefer explicit typed models over loosely-shaped ad-hoc objects. If a branch leans on a silent fallback to paper over an unclear invariant, ask whether the boundary should be made explicit.\n\n6. **Keep logic in the canonical layer and reuse existing helpers.** Call out feature logic leaking into shared paths or implementation details leaking through APIs. Prefer existing canonical utilities over bespoke one-offs. Push code toward the right package, service, or module instead of normalizing drift.\n\n7. **Treat unnecessary sequential orchestration and non-atomic updates as design smells when the cleaner structure is obvious.** If independent work is serialized for no reason, ask whether it should run in parallel. If related updates can leave state half-applied, push for a more atomic structure. Do not over-index on micro-optimizations, but do flag avoidable orchestration complexity that makes the code more brittle.\n\n## Output Expectations\n\nPrioritize structural code-quality regressions and missed simplifications first, then spaghetti and branching complexity, then boundary, type, and file-size concerns, then smaller modularity and legibility issues.\n\n## Approval Bar\n\nDo not approve merely because behavior seems correct. Treat these as presumptive blockers unless the author can justify them: the PR keeps a lot of incidental complexity when a code-judo move would delete it. Pushes a file from below 1000 lines to above 1000 lines. Adds ad-hoc branching that tangles an existing flow. Scatters feature checks across shared code. Adds an unnecessary abstraction, wrapper, or cast-heavy contract, or duplicates an existing helper or puts logic in the wrong layer when there is a clear canonical home. If those conditions are not met, leave explicit, actionable feedback and push for a cleaner decomposition.\n\n## Review Tone\n\nBe direct, serious, and demanding about quality. Do not be rude, but do not soften major maintainability issues into mild suggestions. If the code is making the codebase messier, say so. If the implementation missed an obvious dramatic simplification, say that too. Do not be satisfied with \"maybe rename this\" when the real issue is structural.\n\n\n## Instructions\n\nReview the code through every lens in the rubric and the code-quality lens above that you find relevant. Do not force lenses that don't apply. A simple bug fix does not need paragraphs about architectural integrity.\n\nFor each finding, provide:\n\n1. **Severity**: `critical` | `warning` | `nit`\n   - `critical`: Would cause bugs, data loss, security issues, or fundamentally broken behavior\n   - `warning`: Design concern, maintainability risk, or correctness issue that isn't immediately broken but will cause pain\n   - `nit`: Style, naming, minor improvement.\n2. **Finding**: What the problem is, in concrete terms. Reference specific lines/functions.\n3. **Evidence**: Why you believe this is a problem. Show your reasoning. Don't just assert.\n4. **Suggestion** (optional): What you'd do instead, if you have a concrete alternative. Skip this if you don't have a clear fix.\n\n## What Makes a Good Finding\n\n- It references specific code, not vague concerns (\"this could be better\")\n- It explains WHY something is a problem, not just THAT it is\n- It distinguishes between \"this is broken\" and \"I would have done this differently\"\n- It considers the stated intent. A finding that ignores the context of what's being built is a bad finding\n\n## What to Avoid\n\n- Restating what the code does without identifying a problem\n- Praising the code. You're an adversary, not a cheerleader. If you find nothing wrong, say \"no findings\" and stop.\n\n## Output\n\nReturn your findings as a structured list. If you have zero findings, say so. An empty review is a valid outcome.\n\n```\n## Findings\n\n### 1. [Severity] Short title\n**Location**: file:line or function name\n**Finding**: What's wrong\n**Evidence**: Why this matters\n**Suggestion**: (optional) What to do instead\n\n### 2. [Severity] Short title\n...\n```\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/interrogate-synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/interrogate-synthesis.md",
      "sha256": "f95554d184198c728bca5b4df354741916e60f24e40339c9fe0b4b190a0c04b5",
      "bytes": 2052,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Intent\n\nImplement selected DisplayTable for current visible filtered orders, displayed column order, correct CSV literals and useful empty feedback in the local synthetic fixture. No matching browser or delivery claim follows CLI proof.\n\n# Reviewers\n\nFresh independent workers /root/feature_case/interrogate_a and /root/feature_case/interrogate_b inspected the same filled prompt and actual local output. Each ran four literal Bun tests with exit 0. Requested selections inherit-parent; observed models and efforts unknown. Worker independence is observed; model diversity is unverified. The distinct-family or multi-model expectation remains unmet.\n\n# Act on\n\nNo code findings were returned. Matching browser download and visible empty feedback remain unverified and block complete feature verification.\n\n# Consider\n\nDecide formula-prefix handling before exporting arbitrary untrusted spreadsheet content beyond this fixture. The current requested CSV quoting scope does not settle that policy. Decide future localized-total output explicitly because the shared cell matrix will export displayed scalar values.\n\n# Noted\n\nThe prior raw-order export signature is removed. All supplied callers were absent, and the newly authored browser caller uses the replacement API. Unprovided production callers remain outside inspection scope.\n\n# Dismissed\n\nNo reviewer finding was dismissed. No automatic code changes occurred. Reviewer B initially used a wrong relative path, observed file-not-found, then corrected and inspected actual native/final paths. That failed initial read is retained in its report, not represented as successful testing.\n\n# Agreement map\n\nBoth independent source and CLI reviewers returned no findings within the stated fixture intent. Their agreement supports only these inspected artifacts and tests. Unknown actual models supply no multi-model consensus. The absent browser proof and deslop gate remain open. Lead inspected both reports, exact assignment/revision records, actual output files and test logs before this synthesis.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/judge/judge.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/judge/judge.md",
      "sha256": "83c9340b4c7998b070339c34bd3f2b2ac43c66b5ba59d2d489353ab8b1688eff",
      "bytes": 5341,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Fresh arena judgment\n\nAssignment feature-arena-judge uses exact task input 933a5f5df924b2b089f410615f99af7851010643. Git cat-file returned commit and git ls-tree returned committed-inputs. Both candidate result records declare this same input. Candidate A and B each declare completed design artifacts. I read both design.md, sketch.ts and result.json files end to end, plus the task, withheld rubric, installed 0.1.0 mode, arena, architect and direct contracts. I did not inspect the implementation or edit candidates.\n\nRecommend candidate B, DisplayTable, as the base. Its ordered headers and projected cell matrix give rendering and CSV the same values and positions. Candidate A shares selected raw rows and column keys, so its renderer must still project each field and resolve labels. That creates another opportunity for display and export formatting to diverge.\n\n| Criterion, 0 to 2 | A | B | Concrete reason |\n| --- | ---: | ---: | --- |\n| Filter and hidden-row correctness in one owner | 1 | 1 | A assigns selection to ordersView and B to projectOrders. Neither unimplemented sketch specifies the hidden-row predicate or literal exclusion test. Preserve an explicit hidden exclusion acceptance gate. |\n| Displayed column order without hand synchronization | 1 | 2 | A shares columns and raw rows, leaving projection to both consumers. B shares headers and the ordered cell matrix itself. |\n| Quoting and empty-state tested boundaries | 1 | 1 | Both expose a discriminated result and name CSV escaping. Tests are proposed, not implemented or observed. Neither provides literal executed assertions. |\n| Small public interface without markup coupling | 2 | 2 | Both have two pure public functions and no DOM dependency. A owns a domain view, B a display projection. |\n| Maintainer extension without silent drift | 1 | 2 | B centralizes cell values and headers so a new display policy changes once. A requires the renderer and CSV serializer to interpret domain rows and keys consistently. |\n| Design comparison total | 6 | 8 | These numbers compare design proposals only. They are not case acceptance grades or runtime outcomes. |\n\n## Structural difference\n\nThese are distinct export data shapes within the same shared-snapshot architecture. A retains domain Order objects plus ordered Column identifiers. B projects scalar cell rows and headers before rendering and serialization. B moves projection policy into the boundary where A leaves it to consumers. This is a meaningful representation and responsibility difference. They are not two wholly unrelated top-level architectures. Both rejected DOM serialization. Do not report the candidates as competing DOM versus domain implementations.\n\n## Grafts and rejections\n\nGraft A's explicit removal of the unsafe raw-order export signature and migration of every consumer into B's delivery plan. Keep A's requirement that every click uses current filter state and column order, so no stale closure reuses a prior selection. Keep the branded snapshot boundary and discriminated empty result already shared by both. Do not graft A's raw-domain-row representation into B. That would restore duplicate projection policy.\n\nRequire the synthesized design to name one hidden-row predicate and literal tests for hidden rows, commas, double quotes, reordered columns and empty feedback. Add a column definition registry only if the final implementation needs both labels and accessors, keeping that registry private. This is a synthesis recommendation, not an implementation change made by this judge.\n\n## Red-flag screen\n\nBoth proposals hide filtering and CSV policy behind two functions. Neither adds pass-through modules or phase-based module hierarchy. Both eliminate the old second export path in their stated intent. B avoids a hand-synced export list by consuming the display matrix. A risks information leakage because both consumers must know field projection rules. Both sketches expose public readonly snapshots with a private brand, which prevents ordinary typed construction but supplies no runtime validation for JavaScript callers. Both must prove that the browser uses their supplied snapshot rather than building its own rows. Neither design artifact establishes that proof.\n\nB accepts displayed scalar values as CSV content. Future localized totals would therefore change downloaded text. Record that behavior as an explicit product decision. The current synthetic requirement does not authorize inventing spreadsheet formula neutralization as a completion condition.\n\n## Method and limits\n\nThis is a fresh native judge worker assigned after both candidates were terminal, as specified by the parent. Requested model and effort inherit-parent. Actual model and effort remain unknown because the exposed assignment does not identify them. Independence follows this separate worker operation, not a distinct role name. Model diversity is unverified. No nested worker, integration, installation, commit or external action ran. No feature test, browser action or performance measurement ran in this judge assignment. The lead owns the synthesis decision, graft implementation and final verification.\n\nThe installed unslop skill shaped this report's wording. No create-skill authoring loop or deslop companion ran. This scoped judge does not satisfy those separate review gates.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/judge/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/judge/result.json",
      "sha256": "2a7e69996603dc7a8055553ded4e0200021e58c76629ce03e6d36f4bc628f2d4",
      "bytes": 915,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-arena-judge\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"resultRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-cross-judge\",\n  \"resultMethod\": \"native-independent-cross-judge\",\n  \"status\": \"completed\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"recommendedBase\": \"candidate-b\",\n  \"scores\": {\n    \"candidate-a\": [\n      1,\n      1,\n      1,\n      2,\n      1\n    ],\n    \"candidate-b\": [\n      1,\n      2,\n      1,\n      2,\n      2\n    ]\n  },\n  \"artifacts\": [\n    \"verifiable-feature/native/judge/judge.md\"\n  ],\n  \"limits\": [\n    \"Design comparison only; no runtime or browser proof\",\n    \"Actual model and model diversity unknown\",\n    \"Same shared-snapshot architecture with distinct representation and projection ownership\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/lead-design-reading.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/lead-design-reading.md",
      "sha256": "4d50120f09ed9b11f28bb112f35c47d01587a6c78afed1608e479bf8be9d699e",
      "bytes": 1553,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Lead reading before synthesis\n\nInspected candidate A design.md, sketch.ts, result.json end to end through exec_command after terminal worker result. Inspected candidate B same files after its terminal result. Exact revision and assignment IDs match. Both artifacts exist. No candidate cancellation or partial integration occurred.\n\n# Parent-only design rubric\n\nScore each criterion 0 to 2 with concrete evidence.\n1. Filter and hidden-row correctness are encoded in one owner.\n2. Export column order matches displayed column order without hand synchronization.\n3. CSV quoting and useful empty state have explicit tested boundaries.\n4. Small public interface hides export decisions without coupling to markup.\n5. Future maintainer can extend display/export without silent drift.\n\n\nA stores domain rows plus selected columns; B stores ordered scalar rows plus headers. These are structurally distinct representations of the display/export invariant. A keeps raw domain values available downstream; B prevents serializer and renderer from independently projecting columns. Both reject DOM scraping. B hides more projection policy behind its exported table.\n\nTentative parent scoring before judge result: A 2,2,2,2,1. B 2,2,2,2,2. B is the tentative base. The private TypeScript brand in both sketches does not exist in JavaScript and must not be represented as runtime enforcement. Use module boundaries and actual literal tests in the fixture implementation. Formula-leading cells remain a scoped open decision, not a fabricated defect in supplied rows.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/add-caller.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/add-caller.mjs",
      "sha256": "9846c3f5978b8b8eab425a67ef07826d564cba60022cbe21980c94dbdea6e7c7",
      "bytes": 3994,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { writeFile } from 'node:fs/promises';\nconst root = new URL('./', import.meta.url);\nawait writeFile(new URL('app/index.html', root), `<!doctype html>\n<html lang=\"en\">\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n<title>Fixture orders</title>\n<h1>Orders</h1>\n<label>Status <select id=\"status\"><option>open</option><option>closed</option><option>cancelled</option></select></label>\n<label>Columns <select id=\"columns\"><option value=\"default\">id, customer, total</option><option value=\"total-first\">total, customer, id</option></select></label>\n<button id=\"export\" type=\"button\">Export filtered orders</button>\n<p id=\"feedback\" role=\"status\" aria-live=\"polite\"></p>\n<table><thead></thead><tbody></tbody></table>\n<script type=\"module\" src=\"./browser.mjs\"></script>\n</html>\n`);\nawait writeFile(new URL('app/browser.mjs', root), `import { defaultColumns, orderView, exportCsv } from './dashboard.mjs';\n\nconst status = document.querySelector('#status');\nconst columnOrder = document.querySelector('#columns');\nconst feedback = document.querySelector('#feedback');\nconst orders = await fetch('./orders.json').then(response => {\n  if (!response.ok) throw new Error('Orders could not be loaded.');\n  return response.json();\n});\nlet view;\n\nfunction render() {\n  const columns = columnOrder.value === 'total-first' ? [defaultColumns[2], defaultColumns[1], defaultColumns[0]] : defaultColumns;\n  view = orderView(orders, status.value, columns);\n  const header = document.createElement('tr');\n  header.replaceChildren(...view.columns.map(column => {\n    const cell = document.createElement('th');\n    cell.textContent = column.label;\n    return cell;\n  }));\n  document.querySelector('thead').replaceChildren(header);\n  document.querySelector('tbody').replaceChildren(...view.rows.map(row => {\n    const tr = document.createElement('tr');\n    tr.replaceChildren(...row.map(value => {\n      const td = document.createElement('td');\n      td.textContent = String(value ?? '');\n      return td;\n    }));\n    return tr;\n  }));\n  feedback.textContent = view.rows.length === 0 ? 'No orders match the current filter. Choose another status to export orders.' : '';\n}\n\nstatus.addEventListener('change', render);\ncolumnOrder.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(view);\n  if (result.kind === 'empty') {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.csv], { type: 'text/csv;charset=utf-8' }));\n  const anchor = document.createElement('a');\n  anchor.href = url;\n  anchor.download = 'filtered-orders.csv';\n  anchor.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = 'Exported ' + view.rows.length + ' filtered orders.';\n});\nrender();\n`);\nconst test = Bun.spawnSync(['bun', 'test', new URL('app/dashboard.test.mjs', root).pathname]);\nawait writeFile(new URL('unit2.log', root), Buffer.concat([test.stdout, test.stderr]));\nconst syntax = Bun.spawnSync(['bun', 'build', new URL('app/browser.mjs', root).pathname, '--target=browser', '--outdir', new URL('syntax-build', root).pathname]);\nawait writeFile(new URL('syntax.log', root), Buffer.concat([syntax.stdout, syntax.stderr]));\nconst { orderView, exportCsv } = await import('./app/dashboard.mjs');\nconst orders = await Bun.file(new URL('app/orders.json', root)).json();\nawait writeFile(new URL('literal-export.csv', root), exportCsv(orderView(orders, 'open')).csv);\nawait writeFile(new URL('checks.json', root), JSON.stringify({unit2:{command:'bun test app/dashboard.test.mjs',exitCode:test.exitCode},syntax:{command:'bun build app/browser.mjs --target=browser --outdir syntax-build',exitCode:syntax.exitCode},browser:{status:'blocked',reason:'No matching browser control operation used. Pure tests and build do not verify UI behavior.'}},null,2));\nconsole.log(JSON.stringify({testExit:test.exitCode,syntaxExit:syntax.exitCode}));\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/app/browser.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/app/browser.mjs",
      "sha256": "6c1f3fd9d28be51e7cac7a463ad12765fa4c777d1b724b31e4c2bfeddb3a40c0",
      "bytes": 1971,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { defaultColumns, orderView, exportCsv } from './dashboard.mjs';\n\nconst status = document.querySelector('#status');\nconst columnOrder = document.querySelector('#columns');\nconst feedback = document.querySelector('#feedback');\nconst orders = await fetch('./orders.json').then(response => {\n  if (!response.ok) throw new Error('Orders could not be loaded.');\n  return response.json();\n});\nlet view;\n\nfunction render() {\n  const columns = columnOrder.value === 'total-first' ? [defaultColumns[2], defaultColumns[1], defaultColumns[0]] : defaultColumns;\n  view = orderView(orders, status.value, columns);\n  const header = document.createElement('tr');\n  header.replaceChildren(...view.columns.map(column => {\n    const cell = document.createElement('th');\n    cell.textContent = column.label;\n    return cell;\n  }));\n  document.querySelector('thead').replaceChildren(header);\n  document.querySelector('tbody').replaceChildren(...view.rows.map(row => {\n    const tr = document.createElement('tr');\n    tr.replaceChildren(...row.map(value => {\n      const td = document.createElement('td');\n      td.textContent = String(value ?? '');\n      return td;\n    }));\n    return tr;\n  }));\n  feedback.textContent = view.rows.length === 0 ? 'No orders match the current filter. Choose another status to export orders.' : '';\n}\n\nstatus.addEventListener('change', render);\ncolumnOrder.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(view);\n  if (result.kind === 'empty') {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.csv], { type: 'text/csv;charset=utf-8' }));\n  const anchor = document.createElement('a');\n  anchor.href = url;\n  anchor.download = 'filtered-orders.csv';\n  anchor.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = 'Exported ' + view.rows.length + ' filtered orders.';\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/app/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/app/dashboard.mjs",
      "sha256": "e2d018da65702a1f41dfc02257c45627897c9216bf00ca2baf7be1168c60817d",
      "bytes": 938,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "export const defaultColumns = [\n  { key: 'id', label: 'id' },\n  { key: 'customer', label: 'customer' },\n  { key: 'total', label: 'total' },\n];\n\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && order.hidden !== true);\n}\n\nexport function orderView(orders, status, columns = defaultColumns) {\n  return { columns, rows: visible(orders, status).map(order => columns.map(column => order[column.key])) };\n}\n\nfunction cell(value) {\n  const text = String(value ?? '');\n  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\n\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Choose another status to export orders.' };\n  const lines = [view.columns.map(column => column.label), ...view.rows];\n  return { kind: 'ready', csv: lines.map(row => row.map(cell).join(',')).join('\\r\\n') };\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/app/dashboard.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/app/dashboard.test.mjs",
      "sha256": "b5c73c494818e10ad34e7c8db57454612d2b0770f22101da5d16930dd856c606",
      "bytes": 1277,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport orders from './orders.json';\nimport { orderView, exportCsv } from './dashboard.mjs';\n\ntest('exports only the current filtered orders with comma and quote escaping', () => {\n  expect(exportCsv(orderView(orders, 'open'))).toEqual({ kind: 'ready', csv: 'id,customer,total\\r\\n1,\"Ada, Inc.\",12.5\\r\\n3,\"Say \"\"Hi\"\"\",0' });\n});\n\ntest('uses displayed column order and excludes explicitly hidden matching orders', () => {\n  const input = [...orders, { id: 4, status: 'open', customer: 'Secret', total: 1, hidden: true }];\n  expect(exportCsv(orderView(input, 'open', [{ key: 'total', label: 'total' }, { key: 'customer', label: 'customer' }]))).toEqual({ kind: 'ready', csv: 'total,customer\\r\\n12.5,\"Ada, Inc.\"\\r\\n0,\"Say \"\"Hi\"\"\"' });\n});\n\ntest('escapes newline cells and header labels', () => {\n  expect(exportCsv(orderView([{ status: 'open', customer: 'First\\nSecond' }], 'open', [{ key: 'customer', label: 'Customer, name' }]))).toEqual({ kind: 'ready', csv: '\"Customer, name\"\\r\\n\"First\\nSecond\"' });\n});\n\ntest('returns useful feedback for an empty filter', () => {\n  expect(exportCsv(orderView(orders, 'cancelled'))).toEqual({ kind: 'empty', message: 'No orders match the current filter. Choose another status to export orders.' });\n});\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/app/index.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/app/index.html",
      "sha256": "6769c785f29dc11c7599f08662400acab7c3ceb1e5f9bd267e2fb1263a9c3191",
      "bytes": 681,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "<!doctype html>\n<html lang=\"en\">\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n<title>Fixture orders</title>\n<h1>Orders</h1>\n<label>Status <select id=\"status\"><option>open</option><option>closed</option><option>cancelled</option></select></label>\n<label>Columns <select id=\"columns\"><option value=\"default\">id, customer, total</option><option value=\"total-first\">total, customer, id</option></select></label>\n<button id=\"export\" type=\"button\">Export filtered orders</button>\n<p id=\"feedback\" role=\"status\" aria-live=\"polite\"></p>\n<table><thead></thead><tbody></tbody></table>\n<script type=\"module\" src=\"./browser.mjs\"></script>\n</html>\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/checkpoint.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/checkpoint.md",
      "sha256": "d708c857edccbed47917922da7c89f5a13f52459a9b2a1fd241d06aac22f7f42",
      "bytes": 1065,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Code-owner checkpoint\n\nBlocking first steps. The input SHA and source are verified. The lead chose OrderView={columns,rows} and ExportResult before code. Browser verification and required companions remain open.\n\nIndependent workstreams. This worker owns only native/owner. No nested delegation is authorized. Design, alternative candidates and cross-judge artifacts stay outside this path.\n\nShared mutable state. Rendering and export share one OrderView for the current status and displayed columns. One owner changes that invariant. Inputs and each other worker's output are separate.\n\nSmallest safe decomposition. Unit 1 changes the pure projection and serializer and checks literal CSV. Unit 2 adds a browser caller only after Unit 1 passes. Browser interaction proof remains blocked.\n\nPhase 2 checkpoint. Unit 1 passed before adding the browser caller. There is still one code owner. No shared integration edits, nested workers, commits, push or PR operations occurred. Unit 2 has source and syntax evidence only. Matching browser verification remains open.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/checks.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/checks.json",
      "sha256": "098c30ca4e87562335719c915c0496b76729b7d93f7a06251f011ac511dbca91",
      "bytes": 361,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"unit2\": {\n    \"command\": \"bun test app/dashboard.test.mjs\",\n    \"exitCode\": 0\n  },\n  \"syntax\": {\n    \"command\": \"bun build app/browser.mjs --target=browser --outdir syntax-build\",\n    \"exitCode\": 0\n  },\n  \"browser\": {\n    \"status\": \"blocked\",\n    \"reason\": \"No matching browser control operation used. Pure tests and build do not verify UI behavior.\"\n  }\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/dashboard.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/dashboard.diff",
      "sha256": "ca95fc8897d3208dff78902de8158fdd556393561d0b281ef3d054a893d90c34",
      "bytes": 1762,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "diff --git a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/input/dashboard.mjs b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/app/dashboard.mjs\nindex 92e482b..0ca935e 100644\n--- a/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/input/dashboard.mjs\n+++ b/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/app/dashboard.mjs\n@@ -1,2 +1,24 @@\n-export function visible(orders,status){return orders.filter(o=>o.status===status)}\n-export function exportCsv(orders){return \"id,customer,total\\n\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\"\\n\")}\n+export const defaultColumns = [\n+  { key: 'id', label: 'id' },\n+  { key: 'customer', label: 'customer' },\n+  { key: 'total', label: 'total' },\n+];\n+\n+export function visible(orders, status) {\n+  return orders.filter(order => order.status === status && order.hidden !== true);\n+}\n+\n+export function orderView(orders, status, columns = defaultColumns) {\n+  return { columns, rows: visible(orders, status).map(order => columns.map(column => order[column.key])) };\n+}\n+\n+function cell(value) {\n+  const text = String(value ?? '');\n+  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n+}\n+\n+export function exportCsv(view) {\n+  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Choose another status to export orders.' };\n+  const lines = [view.columns.map(column => column.label), ...view.rows];\n+  return { kind: 'ready', csv: lines.map(row => row.map(cell).join(',')).join('\\r\\n') };\n+}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/finalize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/finalize.mjs",
      "sha256": "bd3207d154e93c9f90dc8f9972f681adb3204ba5ed46567b683e979a75b1ad54",
      "bytes": 2233,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { writeFile, readFile } from 'node:fs/promises';\nconst root = new URL('./', import.meta.url);\nconst diff = Bun.spawnSync(['git', 'diff', '--no-index', new URL('input/dashboard.mjs', root).pathname, new URL('app/dashboard.mjs', root).pathname]);\nawait writeFile(new URL('dashboard.diff', root), diff.stdout);\nconst revision = Bun.spawnSync(['git','rev-parse','933a5f5df924b2b089f410615f99af7851010643']);\nawait writeFile(new URL('revision-receipt.json', root), JSON.stringify({command:'git rev-parse 933a5f5df924b2b089f410615f99af7851010643',exitCode:revision.exitCode,stdout:revision.stdout.toString(),inputFiles:['committed-inputs/dashboard.mjs','committed-inputs/orders.json'],copyMethod:'git show exactRevision:path into owned input directory; copy before editing'},null,2));\nconst paths = ['app/dashboard.mjs','app/dashboard.test.mjs','app/browser.mjs','app/index.html','app/orders.json','literal-export.csv','unit1.log','unit2.log','syntax.log','checks.json','checkpoint.md','dashboard.diff','revision-receipt.json'];\nawait writeFile(new URL('result.json', root),JSON.stringify({assignmentId:'native-feature-owner',inputRevision:'933a5f5df924b2b089f410615f99af7851010643',requestedModel:'inherit-parent',requestedEffort:'inherit-parent',actualModel:'unknown',actualEffort:'unknown',method:'native-independent-code-owner',terminalStatus:'completed',scope:'Local pilot implementation only. Delivery and matching browser verification incomplete.',ownedPath:root.pathname,paths,checks:{unit1:'4 literal tests passed before caller was authored',unit2:'4 literal tests passed with exit 0',browserBuild:'exit 0; syntax and module bundling only',browser:'unverified; no matching control observation'},openGates:['Lead diff inspection','Fresh arena candidates and cross-judge','Contested-design interrogate','Matching browser empty feedback and download behavior','deslop companion or separately authorized replacement','no-comments companion execution','Opening a PR external actions unauthorized'],forbiddenOperationsPerformed:[],nestedWorkers:0},null,2));\nconsole.log(await readFile(new URL('result.json',root),'utf8'));\nconsole.log('Readback CSV ' + JSON.stringify(await readFile(new URL('literal-export.csv',root),'utf8')));\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/literal-export.csv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/literal-export.csv",
      "sha256": "519bcd397e3009a7d1acb8cbe35d2e57b803ac930c56962dc86ac86ad65e979a",
      "bytes": 55,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "id,customer,total\r\n1,\"Ada, Inc.\",12.5\r\n3,\"Say \"\"Hi\"\"\",0"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/prepare.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/prepare.mjs",
      "sha256": "6b448979bae47152c39d3363271a067ad90dd60b0791baa224439e7d996bb36c",
      "bytes": 3559,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { writeFile } from 'node:fs/promises';\nconst base = new URL('./', import.meta.url);\nawait writeFile(new URL('checkpoint.md', base), `# Code-owner checkpoint\n\nBlocking first steps. The input SHA and source are verified. The lead chose OrderView={columns,rows} and ExportResult before code. Browser verification and required companions remain open.\n\nIndependent workstreams. This worker owns only native/owner. No nested delegation is authorized. Design, alternative candidates and cross-judge artifacts stay outside this path.\n\nShared mutable state. Rendering and export share one OrderView for the current status and displayed columns. One owner changes that invariant. Inputs and each other worker's output are separate.\n\nSmallest safe decomposition. Unit 1 changes the pure projection and serializer and checks literal CSV. Unit 2 adds a browser caller only after Unit 1 passes. Browser interaction proof remains blocked.\n\nPhase 2 checkpoint. Unit 1 passed before adding the browser caller. There is still one code owner. No shared integration edits, nested workers, commits, push or PR operations occurred. Unit 2 has source and syntax evidence only. Matching browser verification remains open.\n`);\nawait writeFile(new URL('app/dashboard.mjs', base), `export const defaultColumns = [\n  { key: 'id', label: 'id' },\n  { key: 'customer', label: 'customer' },\n  { key: 'total', label: 'total' },\n];\n\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && order.hidden !== true);\n}\n\nexport function orderView(orders, status, columns = defaultColumns) {\n  return { columns, rows: visible(orders, status).map(order => columns.map(column => order[column.key])) };\n}\n\nfunction cell(value) {\n  const text = String(value ?? '');\n  return /[\",\\\\r\\\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\n\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Choose another status to export orders.' };\n  const lines = [view.columns.map(column => column.label), ...view.rows];\n  return { kind: 'ready', csv: lines.map(row => row.map(cell).join(',')).join('\\\\r\\\\n') };\n}\n`);\nawait writeFile(new URL('app/dashboard.test.mjs', base), `import { test, expect } from 'bun:test';\nimport orders from './orders.json';\nimport { orderView, exportCsv } from './dashboard.mjs';\n\ntest('exports only the current filtered orders with comma and quote escaping', () => {\n  expect(exportCsv(orderView(orders, 'open'))).toEqual({ kind: 'ready', csv: 'id,customer,total\\\\r\\\\n1,\"Ada, Inc.\",12.5\\\\r\\\\n3,\"Say \"\"Hi\"\"\",0' });\n});\n\ntest('uses displayed column order and excludes explicitly hidden matching orders', () => {\n  const input = [...orders, { id: 4, status: 'open', customer: 'Secret', total: 1, hidden: true }];\n  expect(exportCsv(orderView(input, 'open', [{ key: 'total', label: 'total' }, { key: 'customer', label: 'customer' }]))).toEqual({ kind: 'ready', csv: 'total,customer\\\\r\\\\n12.5,\"Ada, Inc.\"\\\\r\\\\n0,\"Say \"\"Hi\"\"\"' });\n});\n\ntest('escapes newline cells and header labels', () => {\n  expect(exportCsv(orderView([{ status: 'open', customer: 'First\\\\nSecond' }], 'open', [{ key: 'customer', label: 'Customer, name' }]))).toEqual({ kind: 'ready', csv: '\"Customer, name\"\\\\r\\\\n\"First\\\\nSecond\"' });\n});\n\ntest('returns useful feedback for an empty filter', () => {\n  expect(exportCsv(orderView(orders, 'cancelled'))).toEqual({ kind: 'empty', message: 'No orders match the current filter. Choose another status to export orders.' });\n});\n`);\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/result.json",
      "sha256": "78748bf769cecad6e4a4cae65135039c7f9738e7950a646542e34a71b64b09ce",
      "bytes": 1522,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"native-feature-owner\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"method\": \"native-independent-code-owner\",\n  \"terminalStatus\": \"completed\",\n  \"scope\": \"Local pilot implementation only. Delivery and matching browser verification incomplete.\",\n  \"ownedPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/\",\n  \"paths\": [\n    \"app/dashboard.mjs\",\n    \"app/dashboard.test.mjs\",\n    \"app/browser.mjs\",\n    \"app/index.html\",\n    \"app/orders.json\",\n    \"literal-export.csv\",\n    \"unit1.log\",\n    \"unit2.log\",\n    \"syntax.log\",\n    \"checks.json\",\n    \"checkpoint.md\",\n    \"dashboard.diff\",\n    \"revision-receipt.json\"\n  ],\n  \"checks\": {\n    \"unit1\": \"4 literal tests passed before caller was authored\",\n    \"unit2\": \"4 literal tests passed with exit 0\",\n    \"browserBuild\": \"exit 0; syntax and module bundling only\",\n    \"browser\": \"unverified; no matching control observation\"\n  },\n  \"openGates\": [\n    \"Lead diff inspection\",\n    \"Fresh arena candidates and cross-judge\",\n    \"Contested-design interrogate\",\n    \"Matching browser empty feedback and download behavior\",\n    \"deslop companion or separately authorized replacement\",\n    \"no-comments companion execution\",\n    \"Opening a PR external actions unauthorized\"\n  ],\n  \"forbiddenOperationsPerformed\": [],\n  \"nestedWorkers\": 0\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/revision-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/revision-receipt.json",
      "sha256": "ffb26d922fd25b63ab48a382534d49928fa37dd34b5d3e1c46adbb58ea915382",
      "bytes": 339,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"command\": \"git rev-parse 933a5f5df924b2b089f410615f99af7851010643\",\n  \"exitCode\": 0,\n  \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n  \"inputFiles\": [\n    \"committed-inputs/dashboard.mjs\",\n    \"committed-inputs/orders.json\"\n  ],\n  \"copyMethod\": \"git show exactRevision:path into owned input directory; copy before editing\"\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/syntax-build/browser.js",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/syntax-build/browser.js",
      "sha256": "fb92287c4a20e4ec8efa882b58f90842556c9484f04431ae64005e4fc870c12a",
      "bytes": 2921,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "// verifiable-feature/native/owner/app/dashboard.mjs\nvar defaultColumns = [\n  { key: \"id\", label: \"id\" },\n  { key: \"customer\", label: \"customer\" },\n  { key: \"total\", label: \"total\" }\n];\nfunction visible(orders, status) {\n  return orders.filter((order) => order.status === status && order.hidden !== true);\n}\nfunction orderView(orders, status, columns = defaultColumns) {\n  return { columns, rows: visible(orders, status).map((order) => columns.map((column) => order[column.key])) };\n}\nfunction cell(value) {\n  const text = String(value ?? \"\");\n  return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n}\nfunction exportCsv(view) {\n  if (view.rows.length === 0)\n    return { kind: \"empty\", message: \"No orders match the current filter. Choose another status to export orders.\" };\n  const lines = [view.columns.map((column) => column.label), ...view.rows];\n  return { kind: \"ready\", csv: lines.map((row) => row.map(cell).join(\",\")).join(`\\r\n`) };\n}\n\n// verifiable-feature/native/owner/app/browser.mjs\nvar status = document.querySelector(\"#status\");\nvar columnOrder = document.querySelector(\"#columns\");\nvar feedback = document.querySelector(\"#feedback\");\nvar orders = await fetch(\"./orders.json\").then((response) => {\n  if (!response.ok)\n    throw new Error(\"Orders could not be loaded.\");\n  return response.json();\n});\nvar view;\nfunction render() {\n  const columns = columnOrder.value === \"total-first\" ? [defaultColumns[2], defaultColumns[1], defaultColumns[0]] : defaultColumns;\n  view = orderView(orders, status.value, columns);\n  const header = document.createElement(\"tr\");\n  header.replaceChildren(...view.columns.map((column) => {\n    const cell = document.createElement(\"th\");\n    cell.textContent = column.label;\n    return cell;\n  }));\n  document.querySelector(\"thead\").replaceChildren(header);\n  document.querySelector(\"tbody\").replaceChildren(...view.rows.map((row) => {\n    const tr = document.createElement(\"tr\");\n    tr.replaceChildren(...row.map((value) => {\n      const td = document.createElement(\"td\");\n      td.textContent = String(value ?? \"\");\n      return td;\n    }));\n    return tr;\n  }));\n  feedback.textContent = view.rows.length === 0 ? \"No orders match the current filter. Choose another status to export orders.\" : \"\";\n}\nstatus.addEventListener(\"change\", render);\ncolumnOrder.addEventListener(\"change\", render);\ndocument.querySelector(\"#export\").addEventListener(\"click\", () => {\n  const result = exportCsv(view);\n  if (result.kind === \"empty\") {\n    feedback.textContent = result.message;\n    return;\n  }\n  const url = URL.createObjectURL(new Blob([result.csv], { type: \"text/csv;charset=utf-8\" }));\n  const anchor = document.createElement(\"a\");\n  anchor.href = url;\n  anchor.download = \"filtered-orders.csv\";\n  anchor.click();\n  setTimeout(() => URL.revokeObjectURL(url), 0);\n  feedback.textContent = \"Exported \" + view.rows.length + \" filtered orders.\";\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/syntax.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/syntax.log",
      "sha256": "6870d8ca01c9d71b3c4975629a67d3ec7f047a963be1ceb6a470fbedfa2a7753",
      "bytes": 64,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "Bundled 2 modules in 5ms\n\n  browser.js  2.92 KB  (entry point)\n\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/unit1.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/unit1.log",
      "sha256": "554bcbd7be68c984d0a4559b90129f857d65fc23b1834a5b54d226519749312a",
      "bytes": 441,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/native/owner/app/dashboard.test.mjs:\n(pass) exports only the current filtered orders with comma and quote escaping [0.26ms]\n(pass) uses displayed column order and excludes explicitly hidden matching orders [0.03ms]\n(pass) escapes newline cells and header labels [0.01ms]\n(pass) returns useful feedback for an empty filter\n\n 4 pass\n 0 fail\n 4 expect() calls\nRan 4 tests across 1 file. [9.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/unit2.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner/unit2.log",
      "sha256": "9374cea00577194ac731fa5947cd35e809722b635b589e328a9ea41a649d994c",
      "bytes": 441,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/native/owner/app/dashboard.test.mjs:\n(pass) exports only the current filtered orders with comma and quote escaping [0.25ms]\n(pass) uses displayed column order and excludes explicitly hidden matching orders [0.03ms]\n(pass) escapes newline cells and header labels [0.01ms]\n(pass) returns useful feedback for an empty filter\n\n 4 pass\n 0 fail\n 4 expect() calls\nRan 4 tests across 1 file. [4.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner-lead-inspection.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner-lead-inspection.md",
      "sha256": "dccdd92b5968b30f8cae09a7d26d2f83b03af4cf8738fc30806034f56733910c",
      "bytes": 1113,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Pilot owner inspection\n\nWorker /root/feature_case/native_feature_owner returned native-feature-owner at input 933a5f5df924b2b089f410615f99af7851010643. Lead inspected result.json, dashboard.diff, dashboard.mjs, browser.mjs, dashboard.test.mjs, checks.json and checkpoint.md. An attempted read ui.mjs failed because actual browser filename is browser.mjs; corrected and inspected.\n\nLead reran literal tests, four passed, zero failed, exit 0. The projected matrix rows and column descriptors drive rendering and CSV. Hidden true rows are excluded before projection. Commas, quotes, newlines and header commas are exercised. Function-level empty message tested; matching browser remains unverified. No application-code comment or suppression is present in these inspected files. This does not satisfy no-comments companion by assertion.\n\nThis is a pilot implementation dispatched after the sequential design and before the independent arena. Its success cannot retroactively satisfy native architect ordering. No integration or full delivery claim. New final implementation assignment will follow arena synthesis.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner-lead-tests.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/owner-lead-tests.log",
      "sha256": "02011db8c3a2850dc83d14031d28d165eaa5d507026fb6ee4046f8c63770b7f5",
      "bytes": 442,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/native/owner/app/dashboard.test.mjs:\n(pass) exports only the current filtered orders with comma and quote escaping [0.28ms]\n(pass) uses displayed column order and excludes explicitly hidden matching orders [0.03ms]\n(pass) escapes newline cells and header labels [0.01ms]\n(pass) returns useful feedback for an empty filter\n\n 4 pass\n 0 fail\n 4 expect() calls\nRan 4 tests across 1 file. [13.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/post-comments-review-a/hash-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/post-comments-review-a/hash-readback.json",
      "sha256": "fc77fc823607038ac4bc1b75a72ddd714cd89adbf794cc3221790e7ffa505281",
      "bytes": 1083,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs\": {\n    \"expected\": \"dca224538566116ac195608a6d13ef5b1921b37fcb783400808e0e56095e6efa\",\n    \"actual\": \"dca224538566116ac195608a6d13ef5b1921b37fcb783400808e0e56095e6efa\",\n    \"match\": true\n  },\n  \"verifiable-feature/native/final/repository/committed-inputs/browser.mjs\": {\n    \"expected\": \"65810edbedc2bebc530b85bee3f42ea562a21d13fd38080cba445a2dfaeacf2a\",\n    \"actual\": \"65810edbedc2bebc530b85bee3f42ea562a21d13fd38080cba445a2dfaeacf2a\",\n    \"match\": true\n  },\n  \"verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs\": {\n    \"expected\": \"1837f07381befc46cde38a564c91d7831b9f0f434a90c6fa34575fbb15dd2c88\",\n    \"actual\": \"1837f07381befc46cde38a564c91d7831b9f0f434a90c6fa34575fbb15dd2c88\",\n    \"match\": true\n  },\n  \"verifiable-feature/native/final/repository/committed-inputs/index.html\": {\n    \"expected\": \"c27ac7d18bac9231b2786dc8f70ee974d46853a8b04b2e47e7dc529c001e7ae0\",\n    \"actual\": \"c27ac7d18bac9231b2786dc8f70ee974d46853a8b04b2e47e7dc529c001e7ae0\",\n    \"match\": true\n  }\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/post-comments-review-a/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/post-comments-review-a/result.json",
      "sha256": "ac08f00be568dbb4941bd9ea3ca2150afd1ed6254ce5fa3415aa6071da8c0c3b",
      "bytes": 712,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-post-comments-review-a\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-post-comments-review\",\n  \"status\": \"review-complete-no-findings\",\n  \"findings\": [],\n  \"requestedModel\": \"inherit-parent\",\n  \"observedModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"observedEffort\": \"unknown\",\n  \"artifacts\": [\n    \"verifiable-feature/native/post-comments-review-a/review.md\",\n    \"verifiable-feature/native/post-comments-review-a/hash-readback.json\"\n  ],\n  \"limits\": [\n    \"Source and existing CLI evidence inspected; matching browser remains unverified\",\n    \"No model diversity claim\",\n    \"No application edits or new tests\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/post-comments-review-a/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/post-comments-review-a/review.md",
      "sha256": "0a3ab181f642eb6487372961f7bedc518505ec5e114db4813515815d50b38aae",
      "bytes": 827,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Findings\n\nNo findings. Independently inspected the final dashboard projection, CSV serializer, browser caller, HTML controls, fixture rows and behavior tests after the completed comment review. All four file hashes match that comment review receipt; see hash-readback.json. The shared DisplayTable snapshot supplies both rendering and export, while literal tests cover status filtering, hidden exclusion, displayed order, quotes, commas, newline cells and empty feedback data. Existing final-lead-checks.json records four passing tests and the exact input HEAD. No tests were rerun.\n\nThis review establishes source review only. Browser download and visible empty-state behavior remain unverified on the matching browser surface. Requested model/effort inherit-parent; observed model/effort unknown. No model diversity claim.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/post-comments-review-b/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/post-comments-review-b/result.json",
      "sha256": "f59e311babd3582effa839a6899a592fee4e0446e79e9324d39f560be116c334",
      "bytes": 2076,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-post-comments-review-b\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-post-comments-review\",\n  \"status\": \"completed\",\n  \"findings\": [],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"outputSha256\": {\n    \"verifiable-feature/native/final/repository/committed-inputs/dashboard.mjs\": {\n      \"expected\": \"dca224538566116ac195608a6d13ef5b1921b37fcb783400808e0e56095e6efa\",\n      \"actual\": \"dca224538566116ac195608a6d13ef5b1921b37fcb783400808e0e56095e6efa\",\n      \"match\": true\n    },\n    \"verifiable-feature/native/final/repository/committed-inputs/browser.mjs\": {\n      \"expected\": \"65810edbedc2bebc530b85bee3f42ea562a21d13fd38080cba445a2dfaeacf2a\",\n      \"actual\": \"65810edbedc2bebc530b85bee3f42ea562a21d13fd38080cba445a2dfaeacf2a\",\n      \"match\": true\n    },\n    \"verifiable-feature/native/final/repository/committed-inputs/dashboard.test.mjs\": {\n      \"expected\": \"1837f07381befc46cde38a564c91d7831b9f0f434a90c6fa34575fbb15dd2c88\",\n      \"actual\": \"1837f07381befc46cde38a564c91d7831b9f0f434a90c6fa34575fbb15dd2c88\",\n      \"match\": true\n    },\n    \"verifiable-feature/native/final/repository/committed-inputs/index.html\": {\n      \"expected\": \"c27ac7d18bac9231b2786dc8f70ee974d46853a8b04b2e47e7dc529c001e7ae0\",\n      \"actual\": \"c27ac7d18bac9231b2786dc8f70ee974d46853a8b04b2e47e7dc529c001e7ae0\",\n      \"match\": true\n    }\n  },\n  \"reviewArtifact\": \"verifiable-feature/native/post-comments-review-b/review.md\",\n  \"sourceReceipt\": \"verifiable-feature/native/comments-review/result.json\",\n  \"priorExecutionArtifact\": \"verifiable-feature/native/final-lead-checks.json\",\n  \"limits\": [\n    \"Read-only source review; no application edits or repeated tests\",\n    \"Matching browser user-path remains unverified\",\n    \"Input revision identifies committed synthetic inputs; inspected final outputs are uncommitted\",\n    \"Worker independence is supplied by native dispatch; actual model and diversity remain unknown\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/post-comments-review-b/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/post-comments-review-b/review.md",
      "sha256": "38e9ca7c71de2cdaaf9c30be87f462c564107fc7a26c154844cad3582c88cab7",
      "bytes": 763,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "No findings.\n\nIndependently inspected the four final application files after the completed comment review and checked all four SHA-256 digests against its receipt. They match. Traced filter and hidden-order selection through the shared immutable DisplayTable projection, both rendering and CSV consumption, escaping of commas, quotes and newlines, current column ordering, and empty feedback assignment. The literal test receipt records four passing tests; I inspected it without re-executing tests. No concrete defect found within the stated synthetic-fixture intent.\n\nMatching browser behavior and download interaction remain unverified. This source review supplies no browser pass. Requested model and effort: inherit-parent; actual model and effort: unknown.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/review-a/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/review-a/result.json",
      "sha256": "c6778d885a12f016608358c029f95386613efd72214868bad5c563bb84a24048",
      "bytes": 645,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-interrogate-a\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-adversarial-review\",\n  \"status\": \"completed-source-and-cli-review\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"observedModel\": \"unknown\",\n  \"observedEffort\": \"unknown\",\n  \"findings\": [],\n  \"artifacts\": [\n    \"verifiable-feature/native/review-a/review.md\",\n    \"verifiable-feature/native/review-a/tests.log\"\n  ],\n  \"limits\": [\n    \"No matching browser verification\",\n    \"No observed model diversity\",\n    \"Code artifact is uncommitted output, not input revision\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/review-a/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/review-a/review.md",
      "sha256": "8196923a3da746f841f13319af91b4e1ad296a4d9c43e744e5a1b6be802e4b7f",
      "bytes": 1122,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "## Findings\n\nNo findings within the stated synthetic fixture intent.\n\nInspected the actual dashboard.mjs, browser.mjs, index.html and dashboard.test.mjs in final/repository/committed-inputs, and the same filled adversarial prompt supplied to both reviewers. Git HEAD is 933a5f5df924b2b089f410615f99af7851010643; these implementation outputs are local uncommitted files, not input-revision contents. Ran bun test committed-inputs/dashboard.test.mjs against that actual repository: 4 tests passed, exit 0. See tests.log.\n\nSource review traces status and column controls through one projectOrders snapshot used for rendering and export; literal assertions cover current filter, hidden rows, selected order, quotes, commas, embedded newline, empty feedback value and changed snapshots. No browser interaction was performed. Download behavior and rendered feedback remain unverified on the matching browser surface. This is independent worker source and CLI review, with requested model and effort inherit-parent, observed model and effort unknown; no model diversity claim. No code was edited and no external action occurred.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/review-a/tests.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/review-a/tests.log",
      "sha256": "0165589b17a10ee47b40cfc713a50e72537c321a77998f5eb8fde5b4307f75f6",
      "bytes": 501,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\ncommitted-inputs/dashboard.test.mjs:\n(pass) current open orders export literal CSV in displayed order [0.39ms]\n(pass) hidden true excluded while false and unspecified remain with embedded newline [0.04ms]\n(pass) header cells use same quoting rules and empty view gives useful feedback [0.03ms]\n(pass) new snapshots follow changed filter and column state and stay detached from source [0.06ms]\n\n 4 pass\n 0 fail\n 8 expect() calls\nRan 4 tests across 1 file. [6.00ms]\n\nexit=0\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/review-b/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/review-b/result.json",
      "sha256": "5a454242f5b6c25f22725b24ed82b6982e6b7cb1d3b7d79344a4e5000202098e",
      "bytes": 765,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"assignmentId\": \"feature-interrogate-b\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"resultRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"method\": \"native-independent-adversarial-review\",\n  \"resultMethod\": \"native-independent-adversarial-review\",\n  \"status\": \"completed\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"findings\": [],\n  \"artifacts\": [\n    \"verifiable-feature/native/review-b/review.md\",\n    \"verifiable-feature/native/review-b/tests.log\"\n  ],\n  \"testExitCode\": 0,\n  \"limits\": [\n    \"No matching browser verification\",\n    \"No observed model diversity\",\n    \"Reviewed current uncommitted output, not committed output\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/review-b/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/review-b/review.md",
      "sha256": "d2b78fd74c0fec3bf8b8d3df3bc533fa44ad8ab3eca29f6b3fe7c996d4491003",
      "bytes": 922,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "## Findings\n\nNo findings within the stated synthetic-fixture intent.\n\nInspected actual dashboard.mjs, browser.mjs, index.html, dashboard.test.mjs and orders.json under native/final/repository/committed-inputs. Ran Bun tests: four tests passed, zero failed; see tests.log. The view projection supplies the same ordered cells to render and CSV export; literal row, header, embedded newline, quote, hidden-flag and empty-result cases are covered in fixture execution.\n\nLimits: no matching browser action was performed, so download behavior and displayed feedback remain browser-unverified. Requested model and effort inherit-parent; actual model and effort unknown. Worker independence does not establish model diversity. Initial inspection attempted the parent-relative final/repository path without native/, received file-not-found and did not run its chained test; corrected to the actual native/final path before review.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/review-b/tests.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/review-b/tests.log",
      "sha256": "a74cdc08d461e35a42f056d0c15dbf8742e1f60189cad2b5933c8b3e5d13d918",
      "bytes": 476,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\ndashboard.test.mjs:\n(pass) current open orders export literal CSV in displayed order [0.34ms]\n(pass) hidden true excluded while false and unspecified remain with embedded newline [0.03ms]\n(pass) header cells use same quoting rules and empty view gives useful feedback [0.02ms]\n(pass) new snapshots follow changed filter and column state and stay detached from source [0.05ms]\n\n 4 pass\n 0 fail\n 8 expect() calls\nRan 4 tests across 1 file. [3.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/synthesis.md",
      "sha256": "557c59c471724639ad06f6b7bd622749d9e8bf021a6a1b35b4404f2172d4d800",
      "bytes": 2399,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Native arena synthesis\n\nThe lead inspected both full design packages and the fresh judge's report. Choose candidate B as base. Both parent and judge prefer B. Parent's initial 10 versus 9 reflected anticipated implementations; judge's 8 versus 6 correctly withheld points for unimplemented hidden-row predicates and tests. Those are design-comparison scores, never case grades. Preserve the judge's stricter evidence distinction.\n\nThe chosen named shape is DisplayTable with ordered headers and row-major scalar cells. projectOrders(orders, {status, columns}) owns eligibility and column projection. exportTableCsv(table) accepts only that projected table and returns file text/filename or an actionable empty message. One private column registry supplies labels and accessors. Renderer and serializer read the same snapshot. No DOM extraction occurs.\n\nGraft A's removal of raw-order export and requirement that current filter and column state generate a fresh snapshot. Reject grafting its raw domain rows because that would restore projection logic in both consumers. Keep the separate DOM design from the sequential trial as a documented alternative, never claim it was a native candidate. Native candidates are distinct domain-row versus cell-matrix representations within the same snapshot architecture.\n\nRequired implementation acceptance predicates are explicit status match and hidden !== true, exact literal CSV for comma/quotes/newline/header/reordered columns, no hidden rows, a discriminated empty message, and same table snapshot in rendering and download. The fixture uses raw scalar totals. Future localized formatting and spreadsheet formula policy are open product decisions.\n\nThis synthesis precedes a fresh final code-owner assignment. The prior owner implementation remains a pilot, not retroactively ordered native implementation. No candidate was cancelled or dropped. Candidate workers and fresh judge are independent observed identities. Requested selections inherited parent; actual models and diversity remain unknown. Typed private brands in sketches are not runtime enforcement in JavaScript.\n\nVerification of this design package is inspected agreement on shape and signatures. Actual feature verification must follow implementation. Matching browser control remains unavailable. This arena is a design comparison and supplies no browser result or shipping permission.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/write-method-receipt.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native/write-method-receipt.mjs",
      "sha256": "6480de3f688b256ad56f69a47b626124acfb1db48c6997d0b57b7e9e4b8b9da4",
      "bytes": 2910,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const sha='933a5f5df924b2b089f410615f99af7851010643';\nconst candidates=[['feature-arena-a','arena_design_a','candidate-a',2,4],['feature-arena-b','arena_design_b','candidate-b',3,5]];\nconst assignments=[];\nfor(const [id,worker,path,start,end] of candidates){\n  const outputPath=`verifiable-feature/native/${path}`;\n  assignments.push({id,workerId:`/root/feature_case/${worker}`,inputRevision:sha,outputOwner:`/root/feature_case/${worker}`,outputPath,role:'architect runner',status:'completed',startedOrder:start,completedOrder:end,requestedModel:'inherit-parent',actualModel:'unknown',retryCount:0,method:{kind:'native-independent-design',sampleCount:1,sampleDefinition:'one independent design package at assigned revision',order:start},taskArtifact:'verifiable-feature/native/arena-task.md',rubricProvided:false,resultRevision:sha,resultMethod:'native-independent-design',hashedArtifact:outputPath+\"/design.md\",outputSha256:new Bun.CryptoHasher('sha256').update(await Bun.file(outputPath+'/design.md').arrayBuffer()).digest('hex')});\n}\nassignments.push({id:'feature-arena-judge',workerId:'/root/feature_case/arena_judge',inputRevision:sha,outputOwner:'/root/feature_case/arena_judge',outputPath:'verifiable-feature/native/judge',role:'fresh readonly cross-judge',status:'completed',startedOrder:6,completedOrder:7,requestedModel:'inherit-parent',actualModel:'unknown',retryCount:0,method:{kind:'native-independent-cross-judge',sampleCount:1,sampleDefinition:'one fresh comparison of two completed design candidates',order:6},taskArtifact:'verifiable-feature/native/arena-task.md',rubricProvided:true,resultRevision:sha,resultMethod:'native-independent-cross-judge',hashedArtifact:'verifiable-feature/native/judge/judge.md',outputSha256:new Bun.CryptoHasher('sha256').update(await Bun.file('verifiable-feature/native/judge/judge.md').arrayBuffer()).digest('hex')});\nawait Bun.write('verifiable-feature/native/arena-method-receipt.json',JSON.stringify({schemaVersion:1,kind:'arena',inputRevision:sha,assignments,reviewArtifact:'verifiable-feature/native/synthesis.md',reviewedBy:'/root/feature_case',declaredOrder:1,candidates:['feature-arena-a','feature-arena-b'],judge:'feature-arena-judge',rubricArtifact:'verifiable-feature/native/arena-rubric.md',synthesis:{order:8,inspectedCandidates:['feature-arena-a','feature-arena-b'],artifact:'verifiable-feature/native/synthesis.md',designScreeningArtifact:'verifiable-feature/native/lead-design-reading.md',verificationArtifact:'verifiable-feature/native/final-lead-checks.json',verificationOrder:10,verificationScope:'Later actual final-module CSV checks only; no matching browser proof'},limits:['Design-only method, no implementation or browser claim','Requested models inherited, actual models unknown','No package evidence validator or case grade claimed']},null,2));\nconsole.log(await Bun.file('verifiable-feature/native/arena-method-receipt.json').text());\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native-spawn-attempt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/native-spawn-attempt.json",
      "sha256": "3a16b9cd1179566abdc75138c4fc2c0348aab776f57dca004c517e973e11bbd5",
      "bytes": 338,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\n  \"tool\": \"collaboration.spawn_agent\",\n  \"assignmentId\": \"feature-design-a\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"result\": \"agent thread limit reached\",\n  \"workerId\": null\n}"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/revision-commands.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/revision-commands.json",
      "sha256": "801dccbb8b303de091c295a5959855921d62eb42091bbbd3ecb12d11febde362",
      "bytes": 1676,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "[\n  {\n    \"cmd\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"show\",\n      \"933a5f5df924b2b089f410615f99af7851010643:committed-inputs/dashboard.mjs\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nexport function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"show\",\n      \"933a5f5df924b2b089f410615f99af7851010643:committed-inputs/orders.json\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"[\\n  {\\n    \\\"id\\\": 1,\\n    \\\"status\\\": \\\"open\\\",\\n    \\\"customer\\\": \\\"Ada, Inc.\\\",\\n    \\\"total\\\": 12.5\\n  },\\n  {\\n    \\\"id\\\": 2,\\n    \\\"status\\\": \\\"closed\\\",\\n    \\\"customer\\\": \\\"Hidden\\\",\\n    \\\"total\\\": 4\\n  },\\n  {\\n    \\\"id\\\": 3,\\n    \\\"status\\\": \\\"open\\\",\\n    \\\"customer\\\": \\\"Say \\\\\\\"Hi\\\\\\\"\\\",\\n    \\\"total\\\": 0\\n  }\\n]\",\n    \"stderr\": \"\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"-C\",\n      \"verifiable-feature/sequential/repository\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"cmd\": [\n      \"git\",\n      \"-C\",\n      \"verifiable-feature/sequential/repository\",\n      \"status\",\n      \"--short\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \" M committed-inputs/dashboard.mjs\\n?? committed-inputs/csv.test.mjs\\n?? committed-inputs/index.html\\n?? committed-inputs/serve.mjs\\n?? committed-inputs/ui.mjs\\n\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/rewrite-result.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/rewrite-result.mjs",
      "sha256": "698596b03375e78202fc9b0b2c6174762af5a5b4c728ef98864640dc26d0487c",
      "bytes": 13064,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const c=await Bun.file('verifiable-feature/contract.json').json();\nawait Bun.write('verifiable-feature.result.md',`# verifiable-feature\n\n## Supplied input\n\n${c.prompt}\n\nComplete supplied requirements, outcomes and forbidden claims are retained in verifiable-feature/contract.json. Input Git revision 933a5f5df924b2b089f410615f99af7851010643 was independently verified through git show, rev-parse and ls-tree. Actual command records are in verifiable-feature/revision-commands.json. The installed plugin source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied provenance, distinct from task input. Installed package is not a Git repository, so no installed-package HEAD claim is made. Source hashes are retained in verifiable-feature/source-hashes.json. No output artifacts were treated as pre-existing input-revision content.\n\n## Actual output\n\nThe final native local implementation is verifiable-feature/native/final/repository/committed-inputs/. It is an isolated local clone detached at the exact input revision with uncommitted output. It implements projectOrders and exportTableCsv around the selected DisplayTable shape. One private column registry produces ordered headers and scalar cell rows. Table rendering and CSV export consume that same current snapshot.\n\nFour literal tests with eight assertions passed in Unit 1 before UI authoring, Unit 2 after UI authoring, and the lead's independent rerun. All returned exit 0. Tests execute the actual final module and cover current status, hidden:true exclusion, column order, comma and quote escaping, embedded newlines, header quoting, empty-result feedback, changed selections and snapshot isolation. Exact output is retained in native/final-lead-export.csv and final-lead-export-result.json. The exported open rows contain Ada, Inc. and Say \"Hi\" and exclude the closed Hidden row. The UI shell is newly authored fixture work because the supplied dashboard was only two functions, with no original renderer or browser caller.\n\nEmpty feedback is observed as a pure function value. Matching browser display, interaction and file-download behavior remain unverified. Browser bundle parsing and literal CSV execution do not satisfy that gate.\n\nThe next maintainer inherits a single projected cell matrix and one registry instead of independent display/export lists. The unsafe raw-orders export signature is removed. The new browser consumer uses its replacement. There were no supplied production callers; unprovided consumers remain outside inspected scope.\n\n## Sources, tools and workflow\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 was used for package source. All 17 named source files were actually read through functions.exec with tools.exec_command and Bun.file or cat. Contents are preserved in source-reads.txt. Full mode, Principles index, role and feature contract were read, with the full mode additionally inspected in sections. Supporting capability, assignment, model, ownership, architecture screening and review contracts are in support-reads.txt. Opening a PR, no-comments and Comment Sicko were read in full. No 0.2.1 source was used.\n\nThe first eight items of todo.md copy the Feature playbook verbatim before task-specific items. Markdown is the reduced todo binding because no task-list operation is exposed. Architect and arena phases are included. Grounding traced visible and exportCsv from the committed source and explicitly recorded the absent original renderer. The initial direct how pass is reduced exploration, not an independent explainer.\n\nReal operation bindings were functions.exec to tools.exec_command for reads, writes, Git and Bun execution; collaboration.spawn_agent for successful independent identities and the initial thread-limit failure; returned native terminal messages plus artifact reads for result inspection; mcp__cua_repl.js for the actual failed local-browser binding and empty browser inventory. No role prompt was treated as a registered custom agent. Every spawned code owner received the entire portable poteto-agent prompt, exact revision, scope, owned path, selected data shape, success predicates and inherited-selection policy. Workers were forbidden nested spawning and returned their own diffs directly.\n\n## Native design and implementation chronology\n\n1. A native design spawn initially failed with agent thread limit reached. Native-spawn-attempt.json preserves that failure. No worker identity or output was invented.\n2. While slots were full, the explicit worker-unavailable variant ran sequentially. An initial fresh native code-owner later implemented a separately labelled pilot based on that reduced design. It lives under native/owner/. Its diff and four literal tests were inspected. It preceded native arena and is not retroactively represented as correctly ordered final work.\n3. Two fresh independent architect candidates ran with overlapping lifetimes and disjoint paths native/candidate-a/ and candidate-b/. Both received the same saved task, grounding and exact input revision. Parent rubric was withheld from their requests. Full design, sketch and result packages were inspected after terminal returns.\n4. Fresh independent judge /root/feature_case/arena_judge started only after both candidates were terminal and inspected. It read the rubric and both completed packages. Parent and judge chose B. Parent's initial optimistic design scores were reduced by the judge because sketches did not constitute executed hidden-row and quoting proof. Those scores compare designs only and are never case grades.\n5. The native/synthesis.md selected DisplayTable before final code. A fresh independent final code owner /root/feature_case/final_feature_owner then re-grounded the exact committed inputs in a new isolated local repository and implemented the selected shape. The lead inspected its actual tracked diff plus every untracked browser, HTML and test file. Lead checks confirm exact unchanged input HEAD, four tests/eight assertions with exit 0, and diff whitespace check exit 0. See native/final-lead-checks.json.\n6. Fresh independent adversarial reviewers inspected the actual final code with the same filled prompt, and a separate Comment Sicko reviewed scoped comments. The first adversarial round preceded the comment companion, so a fresh post-comment round was dispatched to preserve required review ordering. Exact outcomes are retained in their artifacts and the final review addendum.\n\nNative arena's actual identity/order/hash receipt is native/arena-method-receipt.json. Append-only selected method events are native/arena-events.jsonl. No method validator pass or host parity claim is made. The design receipt proves only observed design operations and artifacts, not browser functionality.\n\n| Alternative | Actual design | Choice |\n| --- | --- | --- |\n| Native A | Ordered domain rows plus column keys; rendering and serialization each project fields | Rejected as base because consumers still interpret projection policy. Grafted raw-export removal and current-selection guarantees. |\n| Native B | Ordered headers plus scalar cell matrix projected once | Selected. Both consumers use exactly the same cells and positions. |\n| Sequential alternative | Extract rendered DOM headers and rows | Rejected in the reduced trial. It was not a native candidate. No original DOM existed and virtualization would couple export to markup. |\n\nA and B are structurally distinct data representations and projection responsibilities within a shared-snapshot architecture. They are not independent DOM versus domain implementations. The synthesis rejected grafting raw rows back into B. Private typed branding in design sketches is not claimed as runtime JavaScript enforcement.\n\n## Requested variants\n\n| Variant | Actual actions/results | Enforced or simulated condition |\n| --- | --- | --- |\n| Workers permitted, no push/PR | Initial spawn failed; later successful native pilot, two design candidates, fresh judge, fresh final owner and independent reviewers produced inspected artifacts. Final serializer checks passed as above. | Initial thread limit was real. Worker operations later became available when sibling cases ended. No claim that the full run remained worker-unavailable. |\n| Worker operations unavailable | Separate sequential alternatives, direct implementation and reduced same-agent arena/interrogate/no-comments review under sequential/. Unit 1, Unit 2 and isolated-repository checks each returned three tests passed, zero failed, exit 0. | Dedicated negative condition was simulated by withholding collaboration calls. Initial native thread-limit rejection is separately real. Sequential roles do not establish independence or model diversity. |\n| Matching browser verification denied | App copy under browser-denied/app and literal CSV rerun returned three tests passed, zero failed, exit 0. No browser action was attempted in that dedicated negative variant. | Requested denial was simulated, not a host permission rejection. Separately, an actual local fixture server was started on 127.0.0.1:59481. mcp__cua_repl.js createBrowserTab failed with Browser is not available: iab and cua.listBrowsers returned []. The server was stopped with Ctrl-C, observed exit 130. |\n\nActual browser observations are retained in browser-attempt.json. No screenshot, video, operator visual review, download receipt or rendered empty message was fabricated. No live service was contacted. The negative CSV check cannot satisfy a browser gate.\n\n## Throughput checkpoint\n\n- Blocking first steps. Exact input, full source contracts and source trace preceded design. Native synthesis selected the data shape before the fresh final code-owner. Required browser verification and deslop remain unmet; no downstream delivery completion follows.\n- Independent workstreams. Design candidates and all variants have disjoint owned paths. n/a for code fan-out because the selected renderer/serializer share one DisplayTable invariant and have one code-coupled owner. The no-spawn owner returned its own diff without waiting on nested workers.\n- Shared mutable state. A private registry projects one immutable scalar snapshot. Rendering and CSV consume that snapshot. No shared worker file writes occurred; the lead integrates only reports, not worker code in shared paths.\n- Smallest safe decomposition. Unit 1 projection/serializer with literal checks, then Unit 2 browser shell with CSV rerun and syntax evidence. Browser behavior stays blocked. Checkpoints are rewritten at grounding, implementation and handoff in todo.md and native/final/checkpoint.md.\n\nModel the Domain selected the projected matrix/result union. Separate Before Serializing Shared State assigned exclusive candidate/variant paths. Sequence Work into Verifiable Units required the serializer check before UI. Prove It Works and Test Behavior, Not Implementation led to literal expected rows and an actual CSV file. Laziness Protocol rejected a DOM extraction layer without an existing UI. Unslop shaped the prose. No missing companion is claimed satisfied by these principle applications.\n\n## Review, companion and delivery limits\n\nRequested models and efforts inherit parent for all native assignments. The exposed results do not identify actual models or efforts, which remain unknown. Distinct workers establish independence, not model diversity. The distinct-family/multi-model interrogate expectation remains unmet.\n\nThe complete filled interrogate prompt is native/interrogate-prompt.md. Native review-a/ and review-b/ contain independent source/CLI reviews with no findings, both with actual tests. Native/comments-review/ records a fresh scoped Comment Sicko review with no comments or suppressions, zero deletions, no application files touched, no MUST KILL flags and no skips. The lead read reports and hashes. Comment review does not supply application or browser correctness. The separate sequential no-comments review is explicitly reduced.\n\nRequired deslop is absent and no replacement was requested or authorized. It remains unmet. control-ui companion and a usable matching browser are absent. No create-skill authoring loop ran. Nothing was installed or enabled. Opening a PR was read in full; its commit, rebase, push, actual PR and readiness branches remain unperformed because this evaluation forbids them. Local artifacts are not a PR. Babysit and scheduling were not started.\n\n## Open decisions and completion boundary\n\nMatching browser verification must still establish current filter/column behavior, real downloaded bytes and visible empty feedback. Future localized totals and spreadsheet formula-prefix policy are open product choices. A real app must provide its actual hidden-order and column policy rather than inherit fixture assumptions. All current code is uncommitted checked local output; full user-outcome verification and delivery remain incomplete. No self-grade is assigned.\n`);\nconsole.log('Rewrote result with native/reduced chronology and explicit remaining gates.');\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/csv.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/app/csv.test.mjs",
      "sha256": "08110cb250e72531ef99b1f0d523f96fa086dd4683649fa1a2870b11aef94478",
      "bytes": 920,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { orderView, exportCsv } from './dashboard.mjs';\nimport orders from './orders.json';\ntest('exports only current visible rows in displayed order and escapes literal commas and quotes', () => {\n  expect(exportCsv(orderView([...orders, {id:4,status:'open',hidden:true,customer:'Private',total:9}], 'open', ['customer','total','id']))).toEqual({kind:'ready', csv:'customer,total,id\\r\\n\"Ada, Inc.\",12.5,1\\r\\n\"Say \"\"Hi\"\"\",0,3'});\n});\ntest('empty result gives actionable feedback', () => {\n  expect(exportCsv(orderView(orders, 'missing'))).toEqual({kind:'empty',message:'No orders match the current filter. Change the filter and try again.'});\n});\ntest('newlines and empty values retain CSV semantics', () => {\n  expect(exportCsv(orderView([{id:5,status:'open',customer:'line\\nnext',total:null}], 'open'))).toEqual({kind:'ready',csv:'id,customer,total\\r\\n5,\"line\\nnext\",'});\n});\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/app/dashboard.mjs",
      "sha256": "8f4bf70570fb62601bc12298933debf927680a8d7dda28d294ae5d195879f06a",
      "bytes": 807,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "export const displayedColumns = ['id', 'customer', 'total'];\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && !order.hidden);\n}\nexport function orderView(orders, status, columns = displayedColumns) {\n  return { columns: [...columns], rows: visible(orders, status) };\n}\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Change the filter and try again.' };\n  const cell = value => {\n    const text = String(value ?? '');\n    return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n  };\n  return { kind: 'ready', csv: [view.columns.map(cell).join(','), ...view.rows.map(order => view.columns.map(key => cell(order[key])).join(','))].join('\\r\\n') };\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/index.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/app/index.html",
      "sha256": "9c3f4b614686ba158ef7e5b52b66ed0a11c3da058ea3b29d4e669426ee185b26",
      "bytes": 399,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><title>Orders fixture</title><body><h1>Orders</h1><label>Status <select id=\"status\"><option>open</option><option>closed</option><option>missing</option></select></label><button id=\"export\">Export CSV</button><p id=\"message\" role=\"status\"></p><table><thead></thead><tbody></tbody></table><script type=\"module\" src=\"/ui.mjs\"></script></body></html>"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/serve.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/app/serve.mjs",
      "sha256": "a9b3a45b7cfc0ff73364b3d42240d35395bedbc20fc2df05f488d5b8b89ff141",
      "bytes": 379,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const root=import.meta.dir; const server=Bun.serve({hostname:'127.0.0.1',port:0,fetch(req){ const path=new URL(req.url).pathname; const name=path==='/'?'index.html':path.slice(1); if(!['index.html','dashboard.mjs','ui.mjs','orders.json'].includes(name))return new Response('Not found',{status:404});return new Response(Bun.file(root+'/'+name)); }}); console.log(server.url.href);"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/ui.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/app/ui.mjs",
      "sha256": "dff5097e6f3fb634d89d4cc9aaf853c8c26b14c6f0c898f53aa282bbf74eb0c6",
      "bytes": 1398,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { orderView, exportCsv } from './dashboard.mjs';\nconst orders = await (await fetch('/orders.json')).json();\nconst status = document.querySelector('#status');\nconst message = document.querySelector('#message');\nconst currentView = () => orderView(orders, status.value);\nfunction render() {\n  const view = currentView();\n  message.textContent = '';\n  const head = document.createElement('tr');\n  for (const column of view.columns) { const cell = document.createElement('th'); cell.textContent = column; head.append(cell); }\n  document.querySelector('thead').replaceChildren(head);\n  const rows = view.rows.map(order => { const row = document.createElement('tr'); for (const column of view.columns) { const cell=document.createElement('td');cell.textContent=order[column];row.append(cell); } return row; });\n  document.querySelector('tbody').replaceChildren(...rows);\n}\nstatus.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(currentView());\n  if (result.kind === 'empty') { message.textContent=result.message; return; }\n  const url=URL.createObjectURL(new Blob([result.csv], {type:'text/csv;charset=utf-8'}));\n  const link=document.createElement('a');link.href=url;link.download='orders.csv';link.click();URL.revokeObjectURL(url);\n  message.textContent='Exported the currently displayed orders.';\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/candidate-a/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/candidate-a/design.md",
      "sha256": "247b693807344e6e045e43b97caa485cf796403db44629eba848b125179ed597",
      "bytes": 1003,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Candidate A\n\n## Problem\nExport exactly the currently displayed orders without copying filter or column rules.\n\n## Usage\nconst view = orderView(orders, status, columns); render(view); const result = exportCsv(view);\nconst empty = exportCsv(orderView(orders, \"missing\", columns));\n\n## Shape\nOrderView = {columns: string[], rows: Order[]}. ExportResult = {kind:\"ready\", csv:string}|{kind:\"empty\", message:string}. One view projection owns filter and columns; renderer and serializer consume it. exportCsv hides CSV escaping.\n\n## Tradeoffs accepted\nThe renderer accepts a projected view instead of raw orders. This makes export/display equality structural.\n\n## Alternatives considered\nDOM table extraction keeps export aligned but couples data output to markup and text formatting.\n\n## Open questions and risks\nCSV formula protection is outside supplied requirements and should be a separate product decision.\n\n## Next implementation step\nImplement the projection and serializer, then literal byte tests.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/candidate-b/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/candidate-b/design.md",
      "sha256": "23b7a7ed74aa64e33839ae748d500b2d146de2881fe6780a6446a85862dc5186",
      "bytes": 821,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Candidate B\n\n## Problem\nReuse actual rendered cells as export data.\n\n## Usage\nconst result = exportTable(document.querySelector(\"table\"));\nconst empty = exportTable(emptyTable);\n\n## Shape\nExportResult = {kind:\"ready\", csv:string}|{kind:\"empty\", message:string}. exportTable reads visible th and td cells from the displayed table. Columns and filter are implicit in DOM rows.\n\n## Tradeoffs accepted\nExport depends on table markup and formats values as displayed text. No duplicated projection.\n\n## Alternatives considered\nShared view projection avoids DOM coupling and can run in Bun, but requires renderer integration.\n\n## Open questions and risks\nVirtualized or paginated rows would make DOM export incomplete. Current fixture has no renderer yet.\n\n## Next implementation step\nCreate a table shell and DOM extraction.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/clone.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/clone.log",
      "sha256": "82992eb802616d691c05965bd4a957ba677c1aec7f4aff1e414ef7fcba105af4",
      "bytes": 128,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "Cloning into 'verifiable-feature/sequential/repository'...\ndone.\nHEAD is now at 933a5f5 Seed disposable workflow fixture inputs\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/dashboard.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/dashboard.diff",
      "sha256": "aa6107d6e3131716a8121813452f0640e62f5b943be913d5649ebf8f5833a6b7",
      "bytes": 1230,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "diff --git a/committed-inputs/dashboard.mjs b/committed-inputs/dashboard.mjs\nindex 92e482b..94dd121 100644\n--- a/committed-inputs/dashboard.mjs\n+++ b/committed-inputs/dashboard.mjs\n@@ -1,2 +1,15 @@\n-export function visible(orders,status){return orders.filter(o=>o.status===status)}\n-export function exportCsv(orders){return \"id,customer,total\\n\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\"\\n\")}\n+export const displayedColumns = ['id', 'customer', 'total'];\n+export function visible(orders, status) {\n+  return orders.filter(order => order.status === status && !order.hidden);\n+}\n+export function orderView(orders, status, columns = displayedColumns) {\n+  return { columns: [...columns], rows: visible(orders, status) };\n+}\n+export function exportCsv(view) {\n+  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Change the filter and try again.' };\n+  const cell = value => {\n+    const text = String(value ?? '');\n+    return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n+  };\n+  return { kind: 'ready', csv: [view.columns.map(cell).join(','), ...view.rows.map(order => view.columns.map(key => cell(order[key])).join(','))].join('\\r\\n') };\n+}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/export-run.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/export-run.log",
      "sha256": "c4f95e8b0809a84385470fecd759d06dd20975b2aa4e6a764397fec52164e658",
      "bytes": 93,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "{\"kind\":\"ready\",\"csv\":\"customer,total,id\\r\\n\\\"Ada, Inc.\\\",12.5,1\\r\\n\\\"Say \\\"\\\"Hi\\\"\\\"\\\",0,3\"}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/export.csv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/export.csv",
      "sha256": "c523b794a4958a150b41a5ccda4104aac939ae9ae3d15cd3b406e4404496e4a8",
      "bytes": 55,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "customer,total,id\r\n\"Ada, Inc.\",12.5,1\r\n\"Say \"\"Hi\"\"\",0,3"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/interrogate-prompt.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/interrogate-prompt.md",
      "sha256": "7a3b93270bfde99fbf185ed7001f73c4c056fde585462de42d6815c8df537305",
      "bytes": 15057,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Reviewer Prompt Template\n\nBuild each reviewer subagent's prompt from this template, filling in the placeholders.\n\n---\n\nYou are an adversarial code reviewer. Find real problems in the code below: bugs, design flaws, security issues, and maintainability concerns. You are not here to be helpful or encouraging. You are here to stress-test.\n\n## Intent\n\nThe author's stated intent for this change:\n\n> Export currently filtered visible orders using displayed columns, literal CSV escaping, and useful empty feedback in a local synthetic dashboard. No production or PR delivery claim.\n\nYou are reviewing whether the code achieves this intent well. Do NOT question the intent itself. Assume the goal is correct and challenge the execution.\n\n## Code Under Review\n\nexport const displayedColumns = ['id', 'customer', 'total'];\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && !order.hidden);\n}\nexport function orderView(orders, status, columns = displayedColumns) {\n  return { columns: [...columns], rows: visible(orders, status) };\n}\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Change the filter and try again.' };\n  const cell = value => {\n    const text = String(value ?? '');\n    return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n  };\n  return { kind: 'ready', csv: [view.columns.map(cell).join(','), ...view.rows.map(order => view.columns.map(key => cell(order[key])).join(','))].join('\\r\\n') };\n}\n\nimport { orderView, exportCsv } from './dashboard.mjs';\nconst orders = await (await fetch('/orders.json')).json();\nconst status = document.querySelector('#status');\nconst message = document.querySelector('#message');\nconst currentView = () => orderView(orders, status.value);\nfunction render() {\n  const view = currentView();\n  message.textContent = '';\n  const head = document.createElement('tr');\n  for (const column of view.columns) { const cell = document.createElement('th'); cell.textContent = column; head.append(cell); }\n  document.querySelector('thead').replaceChildren(head);\n  const rows = view.rows.map(order => { const row = document.createElement('tr'); for (const column of view.columns) { const cell=document.createElement('td');cell.textContent=order[column];row.append(cell); } return row; });\n  document.querySelector('tbody').replaceChildren(...rows);\n}\nstatus.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(currentView());\n  if (result.kind === 'empty') { message.textContent=result.message; return; }\n  const url=URL.createObjectURL(new Blob([result.csv], {type:'text/csv;charset=utf-8'}));\n  const link=document.createElement('a');link.href=url;link.download='orders.csv';link.click();URL.revokeObjectURL(url);\n  message.textContent='Exported the currently displayed orders.';\n});\nrender();\n\n\n## Review Rubric\n\n# Review Rubric\n\nReview through whichever lenses are relevant. Not every lens applies to every change. Use judgment.\n\n## Correctness\n\nDoes the code actually do what the intent says it should?\n\n- Edge cases: empty inputs, nil/undefined, boundary values, concurrent access\n- Error handling: are errors caught, propagated, or silently swallowed?\n- Off-by-one, type coercion, integer overflow, string encoding\n- State management: race conditions, stale closures, dangling references\n- Does the happy path work? Does the sad path work?\n- Idempotency: what happens if this operation runs twice, or if a previous run crashed halfway? If the answer is \"it depends on what state was left behind,\" there's a missing reconciliation step.\n- Concurrency: if multiple actors can touch the same mutable state (files, branches, shared data), is access serialized structurally (locks, sequential phases, exclusive ownership), or by conventions that won't hold?\n\nWhen you find a potential bug, trace the execution path. Don't just flag \"this could be nil\". Show the call chain that makes it nil.\n\n## Root Causes vs. Symptoms\n\nIs the code fixing the actual problem or papering over a symptom?\n\nAnswering this often requires looking beyond the changed files. Read the surrounding code (callers, callees, type definitions, sibling modules) and understand the architecture the change lives in. Use the tools available to you (Read, Grep, Glob) to explore. Follow the call chain. Read the types. Understand why the code exists before judging whether the change addresses the right layer.\n\n- Guard clauses that mask a deeper invariant violation\n- Retry logic that hides a broken contract\n- Type casts that silence a modeling error\n- If you see a workaround, ask: why is the workaround needed? What would a proper fix look like?\n- A fix in module A that should really be a fix in module B's contract\n- Instructions where structure would be better: if the fix is a comment saying \"don't do X\" or a convention someone has to remember, ask whether it could instead be a type constraint, a lint rule, or a runtime check that makes the wrong thing impossible\n\n## Structural Integrity\n\nDoes the code fit well into the system it's part of?\n\n- Boundary discipline: is validation at system boundaries, or scattered through business logic? Validate data once where it enters the system, then trust it internally.\n- Abstraction level: is the code mixing high-level orchestration with low-level detail?\n- Coupling: does this change introduce dependencies that will make future changes harder?\n- Data model fit: do the data structures match the actual access patterns? The right structure makes downstream code obvious. The wrong one fights you at every turn.\n- Bolted-on vs. integrated: was the change patched onto the existing design, or does it read as if the design always accounted for it? If the new requirement had been known from the start, would the code look like this?\n- Legacy dual-paths: does the change introduce a new API while keeping the old one alive? If there are no external consumers, migrate callers and delete the old path in the same wave. Don't leave compatibility layers that will become permanent.\n\nDon't penalize simple code for lacking abstraction. Premature abstraction is worse than duplication.\n\n## Verification\n\nCan you tell that this code works from reading it?\n\n- Are there tests? Do they test behavior or implementation details?\n- Are there assertions/invariants that would catch regressions?\n- If this is a bug fix: is there a test for the bug?\n- If this touches an integration boundary: is the full path tested?\n- Check the real thing, not a proxy. If the code checks liveness via file mtime or cached state instead of reading the actual value, that's a verification gap.\n- For delegated or async work: does the code verify actual output artifacts, or does it trust self-reports and summaries?\n\n## Complexity Budget\n\nIs the complexity justified by what the code accomplishes?\n\n- Code that could be simpler without losing correctness or clarity\n- Abstractions that serve only one call site\n- Configuration or parameterization for cases that don't exist yet\n- Dead code, unused imports, vestigial parameters\n- Over-engineering: \"just in case\" code paths with no current callers\n- Obsolete compatibility paths kept alive for transitional stability that's no longer needed. If the migration is done, delete the scaffolding\n- Does the user experience justify the complexity? Every feature, control, and option should earn its place. Half-finished features are worse than missing ones.\n\nSimpler is better unless simpler is wrong. Three lines of duplication beat a premature abstraction.\n\n## Security\n\nFor each security finding, trace the input path through the code and show it.\n\n- User input flowing to dangerous sinks (SQL, shell, eval, innerHTML) without sanitization\n- Authentication/authorization gaps in new endpoints\n- Secrets in code, logs, or error messages\n- TOCTOU (time-of-check-time-of-use) in security-critical paths\n\n\n## Code Quality Lens\n\n# Code Quality Review\n\nEach reviewer applies this code-quality lens in addition to the rubric. It is a strict standard focused on implementation quality, maintainability, abstraction quality, and codebase health.\n\nAbove all, be ambitious about code structure. Do not merely identify local cleanup. Actively search for \"code judo\" moves, restructurings that preserve behavior while making the implementation dramatically simpler, smaller, more direct, and more elegant.\n\n## Core Prompt\n\nStart from this baseline:\n\n> Perform a deep code quality audit of the current branch's changes.\n> Rethink how to structure / implement the changes to meaningfully improve code quality without impacting behavior.\n> Work to improve abstractions, modularity, reduce Spaghetti code, improve succinctness and legibility.\n> Be ambitious, if there is a clear path to improving the implementation that involves restructuring some of the codebase, go for it.\n> Be extremely thorough and rigorous. Measure twice, cut once.\n\n## Dimensions\n\nEach dimension is stated once. Apply the ones that are relevant.\n\n0. **Be ambitious about structural simplification.** Do not stop at \"this could be a bit cleaner.\" Look for reframings that make whole branches, helpers, modes, conditionals, or layers disappear. Assume a \"code judo\" move is often available. It uses the existing architecture more effectively and makes the change dramatically simpler. If you can delete complexity rather than rearrange it, push hard for that.\n\n1. **Do not let a PR push a file from under 1k lines to over 1k lines without a very strong reason.** Treat this as a strong smell. Prefer extracting helpers, subcomponents, or modules. If the diff crosses that threshold, ask whether the code should be decomposed first. Waive only for a compelling structural reason where the resulting file stays clearly organized.\n\n2. **Do not allow spaghetti growth in existing code.** Be suspicious of new ad-hoc conditionals, scattered special cases, or one-off branches inserted into unrelated flows. Treat \"weird if statements in random places\" as a design problem, not a style nit. Prefer pushing the logic into a dedicated helper, state machine, or module instead of tangling an existing path.\n\n3. **Bias toward cleaning the design, not just accepting working code.** If behavior can stay the same while the structure becomes meaningfully cleaner, push for the cleaner version. Prefer simplifications that remove moving pieces over refactors that spread the same complexity around.\n\n4. **Prefer direct, boring, maintainable code over hacky or magical code.** Treat brittle, ad-hoc, or \"magic\" behavior as a problem. Be skeptical of generic mechanisms that hide simple data-shape assumptions. Flag thin abstractions, identity wrappers, or pass-through helpers that add indirection without buying clarity.\n\n5. **Push on type and boundary cleanliness when it affects maintainability.** Question unnecessary optionality, `unknown`, `any`, or cast-heavy code when a clearer type boundary could exist. Prefer explicit typed models over loosely-shaped ad-hoc objects. If a branch leans on a silent fallback to paper over an unclear invariant, ask whether the boundary should be made explicit.\n\n6. **Keep logic in the canonical layer and reuse existing helpers.** Call out feature logic leaking into shared paths or implementation details leaking through APIs. Prefer existing canonical utilities over bespoke one-offs. Push code toward the right package, service, or module instead of normalizing drift.\n\n7. **Treat unnecessary sequential orchestration and non-atomic updates as design smells when the cleaner structure is obvious.** If independent work is serialized for no reason, ask whether it should run in parallel. If related updates can leave state half-applied, push for a more atomic structure. Do not over-index on micro-optimizations, but do flag avoidable orchestration complexity that makes the code more brittle.\n\n## Output Expectations\n\nPrioritize structural code-quality regressions and missed simplifications first, then spaghetti and branching complexity, then boundary, type, and file-size concerns, then smaller modularity and legibility issues.\n\n## Approval Bar\n\nDo not approve merely because behavior seems correct. Treat these as presumptive blockers unless the author can justify them: the PR keeps a lot of incidental complexity when a code-judo move would delete it. Pushes a file from below 1000 lines to above 1000 lines. Adds ad-hoc branching that tangles an existing flow. Scatters feature checks across shared code. Adds an unnecessary abstraction, wrapper, or cast-heavy contract, or duplicates an existing helper or puts logic in the wrong layer when there is a clear canonical home. If those conditions are not met, leave explicit, actionable feedback and push for a cleaner decomposition.\n\n## Review Tone\n\nBe direct, serious, and demanding about quality. Do not be rude, but do not soften major maintainability issues into mild suggestions. If the code is making the codebase messier, say so. If the implementation missed an obvious dramatic simplification, say that too. Do not be satisfied with \"maybe rename this\" when the real issue is structural.\n\n\n## Instructions\n\nReview the code through every lens in the rubric and the code-quality lens above that you find relevant. Do not force lenses that don't apply. A simple bug fix does not need paragraphs about architectural integrity.\n\nFor each finding, provide:\n\n1. **Severity**: `critical` | `warning` | `nit`\n   - `critical`: Would cause bugs, data loss, security issues, or fundamentally broken behavior\n   - `warning`: Design concern, maintainability risk, or correctness issue that isn't immediately broken but will cause pain\n   - `nit`: Style, naming, minor improvement.\n2. **Finding**: What the problem is, in concrete terms. Reference specific lines/functions.\n3. **Evidence**: Why you believe this is a problem. Show your reasoning. Don't just assert.\n4. **Suggestion** (optional): What you'd do instead, if you have a concrete alternative. Skip this if you don't have a clear fix.\n\n## What Makes a Good Finding\n\n- It references specific code, not vague concerns (\"this could be better\")\n- It explains WHY something is a problem, not just THAT it is\n- It distinguishes between \"this is broken\" and \"I would have done this differently\"\n- It considers the stated intent. A finding that ignores the context of what's being built is a bad finding\n\n## What to Avoid\n\n- Restating what the code does without identifying a problem\n- Praising the code. You're an adversary, not a cheerleader. If you find nothing wrong, say \"no findings\" and stop.\n\n## Output\n\nReturn your findings as a structured list. If you have zero findings, say so. An empty review is a valid outcome.\n\n```\n## Findings\n\n### 1. [Severity] Short title\n**Location**: file:line or function name\n**Finding**: What's wrong\n**Evidence**: Why this matters\n**Suggestion**: (optional) What to do instead\n\n### 2. [Severity] Short title\n...\n```\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/interrogate.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/interrogate.md",
      "sha256": "31c63675f163ef5484f093ee3d1bdbbe2bf9982b5ea27e7de36ff4e9805498f3",
      "bytes": 1247,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Intent\nExport currently filtered visible orders using displayed columns, literal CSV escaping, and useful empty feedback in a local synthetic dashboard.\n\n# Reviewers\nSequential reviewer A and B are this same agent, not independent. Requested models inherit-parent; observed unknown. Prompt and full rubric are retained in interrogate-prompt.md. No model diversity claim.\n\n# Act on\nNo proven CSV defect found through current literal fixture paths. Matching UI feedback remains blocked without browser observations. This is an unsatisfied verification gate, not a passing verdict.\n\n# Consider\nFormula-leading customer data could be interpreted by spreadsheet software. Current fixture contains none; separate product decision required before expanding untrusted-data scope.\n\n# Noted\nexportCsv signature changes from array to OrderView. Only supplied caller was absent. New UI consumes OrderView. Any unprovided production caller remains outside inspected scope.\n\n# Dismissed\nNo generic renderer or dependency is needed for three columns. DOM extraction would add coupling without an existing DOM to preserve.\n\n# Agreement map\nThe two sequential readings found the same browser proof gap; this establishes neither consensus nor independent review.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/no-comments-review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/no-comments-review.md",
      "sha256": "010f6955d47364ab05afed22b2576f00c0e20fe99fe6be1c1643e0d2a7caa5a8",
      "bytes": 724,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Reduced no-comments review\n\nThe installed no-comments skill and portable Comment Sicko prompt were read. Scoped files are sequential/app/dashboard.mjs, ui.mjs and csv.test.mjs. They contain no comments or TypeScript/lint suppressions. Same-agent sequential review performed no edits, actual deletion count 0, restored comments 0, reruns 0, MUST KILL flags none, encoding offers none, encodings none, unenforced constraints none. No application-code edits were made by this comment review.\n\nThis is a permitted reduced review with worker operations voluntarily withheld in this variant. It is not a fresh independent perspective and does not complete the native independent companion gate. Required deslop remains missing.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/README.md",
      "sha256": "71f249da42cc5a54fc692fb6b06a4824bd11274d3e1d8433b4df53e55254eb17",
      "bytes": 213,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Disposable task input revision\nThis Git history identifies only synthetic workflow inputs and case contracts. It is not the installed plugin source revision or a host outcome. Case outputs must remain separate.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/csv.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/csv.test.mjs",
      "sha256": "08110cb250e72531ef99b1f0d523f96fa086dd4683649fa1a2870b11aef94478",
      "bytes": 920,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { orderView, exportCsv } from './dashboard.mjs';\nimport orders from './orders.json';\ntest('exports only current visible rows in displayed order and escapes literal commas and quotes', () => {\n  expect(exportCsv(orderView([...orders, {id:4,status:'open',hidden:true,customer:'Private',total:9}], 'open', ['customer','total','id']))).toEqual({kind:'ready', csv:'customer,total,id\\r\\n\"Ada, Inc.\",12.5,1\\r\\n\"Say \"\"Hi\"\"\",0,3'});\n});\ntest('empty result gives actionable feedback', () => {\n  expect(exportCsv(orderView(orders, 'missing'))).toEqual({kind:'empty',message:'No orders match the current filter. Change the filter and try again.'});\n});\ntest('newlines and empty values retain CSV semantics', () => {\n  expect(exportCsv(orderView([{id:5,status:'open',customer:'line\\nnext',total:null}], 'open'))).toEqual({kind:'ready',csv:'id,customer,total\\r\\n5,\"line\\nnext\",'});\n});\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/dashboard.mjs",
      "sha256": "8f4bf70570fb62601bc12298933debf927680a8d7dda28d294ae5d195879f06a",
      "bytes": 807,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "export const displayedColumns = ['id', 'customer', 'total'];\nexport function visible(orders, status) {\n  return orders.filter(order => order.status === status && !order.hidden);\n}\nexport function orderView(orders, status, columns = displayedColumns) {\n  return { columns: [...columns], rows: visible(orders, status) };\n}\nexport function exportCsv(view) {\n  if (view.rows.length === 0) return { kind: 'empty', message: 'No orders match the current filter. Change the filter and try again.' };\n  const cell = value => {\n    const text = String(value ?? '');\n    return /[\",\\r\\n]/.test(text) ? '\"' + text.replaceAll('\"', '\"\"') + '\"' : text;\n  };\n  return { kind: 'ready', csv: [view.columns.map(cell).join(','), ...view.rows.map(order => view.columns.map(key => cell(order[key])).join(','))].join('\\r\\n') };\n}\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/index.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/index.html",
      "sha256": "9c3f4b614686ba158ef7e5b52b66ed0a11c3da058ea3b29d4e669426ee185b26",
      "bytes": 399,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><title>Orders fixture</title><body><h1>Orders</h1><label>Status <select id=\"status\"><option>open</option><option>closed</option><option>missing</option></select></label><button id=\"export\">Export CSV</button><p id=\"message\" role=\"status\"></p><table><thead></thead><tbody></tbody></table><script type=\"module\" src=\"/ui.mjs\"></script></body></html>"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/serve.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/serve.mjs",
      "sha256": "a9b3a45b7cfc0ff73364b3d42240d35395bedbc20fc2df05f488d5b8b89ff141",
      "bytes": 379,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const root=import.meta.dir; const server=Bun.serve({hostname:'127.0.0.1',port:0,fetch(req){ const path=new URL(req.url).pathname; const name=path==='/'?'index.html':path.slice(1); if(!['index.html','dashboard.mjs','ui.mjs','orders.json'].includes(name))return new Response('Not found',{status:404});return new Response(Bun.file(root+'/'+name)); }}); console.log(server.url.href);"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/ui.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/ui.mjs",
      "sha256": "dff5097e6f3fb634d89d4cc9aaf853c8c26b14c6f0c898f53aa282bbf74eb0c6",
      "bytes": 1398,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "import { orderView, exportCsv } from './dashboard.mjs';\nconst orders = await (await fetch('/orders.json')).json();\nconst status = document.querySelector('#status');\nconst message = document.querySelector('#message');\nconst currentView = () => orderView(orders, status.value);\nfunction render() {\n  const view = currentView();\n  message.textContent = '';\n  const head = document.createElement('tr');\n  for (const column of view.columns) { const cell = document.createElement('th'); cell.textContent = column; head.append(cell); }\n  document.querySelector('thead').replaceChildren(head);\n  const rows = view.rows.map(order => { const row = document.createElement('tr'); for (const column of view.columns) { const cell=document.createElement('td');cell.textContent=order[column];row.append(cell); } return row; });\n  document.querySelector('tbody').replaceChildren(...rows);\n}\nstatus.addEventListener('change', render);\ndocument.querySelector('#export').addEventListener('click', () => {\n  const result = exportCsv(currentView());\n  if (result.kind === 'empty') { message.textContent=result.message; return; }\n  const url=URL.createObjectURL(new Blob([result.csv], {type:'text/csv;charset=utf-8'}));\n  const link=document.createElement('a');link.href=url;link.download='orders.csv';link.click();URL.revokeObjectURL(url);\n  message.textContent='Exported the currently displayed orders.';\n});\nrender();\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/task-contracts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository/task-contracts.json",
      "sha256": "52151323191f599482b28d980418ed0a95aa7cbcf4b4ff211b13db0f8ad91bb9",
      "bytes": 25271,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "[\n  {\n    \"id\": \"unit-state\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"agents/poteto-agent.md\",\n      \"skills/poteto-mode/scripts/orch/orch.ts\",\n      \"skills/poteto-mode/scripts/orch/store.ts\",\n      \"skills/poteto-mode/scripts/orch/orch.test.ts\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\",\n      \"skills/poteto-mode/scripts/package.json\",\n      \"skills/poteto-mode/scripts/bun.lock\",\n      \"skills/arena/SKILL.md\",\n      \"skills/figure-it-out/SKILL.md\",\n      \"skills/show-me-your-work/SKILL.md\",\n      \"skills/show-me-your-work/scripts/log.sh\",\n      \"skills/show-me-your-work/references/decision-log-template.tsv\",\n      \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n      \"skills/principle-encode-lessons-in-structure/SKILL.md\",\n      \"skills/poteto-mode/playbooks/autonomous-run.md\",\n      \"skills/poteto-mode/playbooks/babysit.md\",\n      \"skills/unslop/SKILL.md\"\n    ],\n    \"prompt\": \"Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.\",\n    \"requirements\": [\n      \"Read full mode, original program roles, playbook and direct helper/support contracts. Keep coordinator out of code; use scoped fix units and continuous authorized landing. Scale cheap units without inventing independent verifiers.\",\n      \"Use immutable identity, exact input SHA, exclusive output owner/path, append-only attempts, complete brief fields and verbatim standing orders on each spawn/resume. Remote placement, nesting, background execution and model diversity require observed bindings.\",\n      \"Use the actual explicit external store CLI with pinned prerequisites. Record real worker identity/results separately; arbitrary unit-state strings and evidence pointers are not checked by the helper.\",\n      \"Pilot one unit end to end before a rolling window. Relay upstream context, audit briefs alongside the wave, drain only at the four named boundaries and preserve every pointer through a peek receipt and readback before destructive drain.\",\n      \"Classify all pointers, inspect artifacts before recording rows, preserve arrivals for the next batch, reconcile every child and late zombie against exact assignment and current frontier. Do not accept stale or cancelled partial work.\",\n      \"One stacker per stack and one babysitter per generation. Discover the ordered frontier from real stack-owner metadata and git SHAs; missing metadata blocks that dependency. Workers never run gt or rebase. External actions retain explicit authorization and interrupted unknown outcomes block replay.\",\n      \"Check ledger by current PR plus full head SHA. Inspect evidence and enforce verifier precedence outside the helper. New heads require verification, historical summary counts are not current passes, type-check-only is insufficient for behavioral work and blocked/failed verdicts are not passes.\",\n      \"Bound source failure retries to two while obeying the stricter assignment allowance of one retry for missing SHA/method evidence. Stop tree-wide refills on invalid upstream input, preserve terminal handoff and review stale lock ownership before force.\",\n      \"Keep overview append-only, decision trail auditable, gates explicit and status derived. Close only after final drain, terminal reconciliation and predicate verification on the real artifact. Report predicate/counts, tracks/landed work, PRs/SHAs, verdicts, abandonments/reasons, gates, store/trail paths and review limits.\"\n    ],\n    \"expectedFull\": \"Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.\",\n    \"expectedReduced\": \"Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.\",\n    \"expectedBlocked\": \"Denied execution or persistence, missing pinned dependencies or required pending callers block their dependent steps. Missing identity, exact revision, artifacts or method evidence prevents acceptance. Stale heads, lost drain receipts and zombies require inspected reconciliation. Missing gt metadata blocks frontier recomputation. Required independent verification, different-family review and unauthorized external actions remain blocked. Stale lock takeover requires ownership review and applicable permission.\",\n    \"forbiddenClaims\": [\n      \"Structural checks or snapshot tests prove current caller host parity or real workers.\",\n      \"Unit done strings, typed ledger verdicts or summary counts prove real current completion without artifact/method inspection.\",\n      \"Sequential roles prove independent workers, cloud execution, nesting, model diversity or unattended recovery.\",\n      \"A truncated standing summary contains all standing orders.\",\n      \"An inbox notification or destructive drain without a persisted receipt proves inspected results.\",\n      \"Historical head verdicts verify a restacked head, or type-check-only and verifier-blocked pass behavioral work.\",\n      \"The helper enforces immutable assignments, SHA syntax, ownership, evidence existence or verifier precedence.\",\n      \"Dead pid permits automatic force takeover or restart proves worker liveness.\",\n      \"Gate defaults, broad autonomy or initialization authorize installs, push, merge, messaging or schedules.\",\n      \"Missing gt metadata can be replaced by a guessed authoritative frontier.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/orchestrate.json\"\n  },\n  {\n    \"id\": \"units-and-proof\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/multi-phase-plan.md\",\n      \"agents/poteto-agent.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"skills/poteto-mode/scripts/check-plan.mjs\",\n      \"skills/poteto-mode/playbooks/prototype.md\",\n      \"skills/poteto-mode/playbooks/autopilot-full.md\",\n      \"skills/poteto-mode/playbooks/autopilot-stack.md\",\n      \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/references/bugbot-triage.md\",\n      \"skills/swarm/SKILL.md\",\n      \"skills/technical-writing/SKILL.md\",\n      \"skills/unslop/SKILL.md\",\n      \"skills/principle-never-block-on-the-human/SKILL.md\",\n      \"skills/principle-guard-the-context-window/SKILL.md\",\n      \"skills/principle-sequence-verifiable-units/SKILL.md\",\n      \"skills/principle-encode-lessons-in-structure/SKILL.md\",\n      \"skills/principle-prove-it-works/SKILL.md\",\n      \"skills/how/SKILL.md\",\n      \"skills/interrogate/SKILL.md\",\n      \"skills/show-me-your-work/SKILL.md\",\n      \"skills/no-comments/SKILL.md\"\n    ],\n    \"prompt\": \"Write a multi-phase pstack plan for a two-PR change. Name file ownership and dependencies, unit tests, live regression against trunk and head, interaction review media, and applicable performance evidence. Run the adapted pstack checker. Repeat with unavailable workers, controls, scheduling, remote setup, model selection and denied writes.\",\n    \"requirements\": [\n      \"Preserve plan-only ownership, trivial-change skip, prototype evidence and explicit execution go.\",\n      \"Keep all ordered program, PR sub-blocks, close and appendix sections.\",\n      \"Declare all five capability bindings with evidence and actual worker capacity.\",\n      \"Name per-PR files, dependencies, unit evidence, live artifacts and pass predicates.\",\n      \"Retain the ten independent lane full expectation; explicit reduced or blocked limits preserve omitted scenarios.\",\n      \"Performance uses comparable trunk/head metric, interleaved probe, baseline first and numeric fail rule, or justified non-applicability evidence.\",\n      \"Preserve operator screenshot/video review for interactions and independent review requirements.\",\n      \"Invoke Bun positional read-only checker on a pstack plan only and retain output and exit status.\",\n      \"External setup, scheduling, PR operations and merge require actual separate authorization.\"\n    ],\n    \"expectedFull\": \"An authorized saved pstack plan preserves all sections, ten independent live scenarios within observed capacity, per-PR units and evidence, applicable performance or justified non-applicability, operator interaction review and checker output with zero structural problems. Execution waits for explicit go.\",\n    \"expectedReduced\": \"Authorized sequential exploration or reduced live capacity remains labelled reduced capability with reasons, evidence and omitted scenarios. Manual ticks replace unavailable scheduling without unattended claims. Denied writes return unsaved text. Independent verdict gates remain blocked. A structural checker pass proves format only.\",\n    \"expectedBlocked\": \"Missing source contracts, unreadable plan, denied execution, unavailable live control or required independent review blocks the affected work. Preserve planned scenarios, disclose the missing dependency and the actual checker outcome. A structurally valid plan with blocked execution can pass; report checker failure only when the checker actually fails; do not fabricate artifacts or start execution.\",\n    \"forbiddenClaims\": [\n      \"Structural checker success proves implementation or host parity.\",\n      \"Sequential role switching provides independent workers or review.\",\n      \"Requested model proves observed model or diversity.\",\n      \"A checked box without receipt proves live success.\",\n      \"Unavailable scheduling proves unattended execution.\",\n      \"Planning permission authorizes external setup, PR creation, push, messaging or merge.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/multi-phase-plan.json\"\n  },\n  {\n    \"id\": \"unknown-actual-model\",\n    \"sourcePaths\": [\n      \"agents/poteto-agent.md\",\n      \"agents/comment-sicko.md\"\n    ],\n    \"prompt\": \"A spawn request names a model but its result does not expose the actual model.\",\n    \"requirements\": [\n      \"Keep observed model unknown and retain the request separately.\",\n      \"Read portable role instructions; bind operations to observed session capabilities.\"\n    ],\n    \"expectedFull\": \"Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately.\",\n    \"expectedReduced\": \"Authorized sequential role review preserves scope and reports reduced capability. Keep observed model unknown and retain the request separately.\",\n    \"expectedBlocked\": \"Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.\",\n    \"forbiddenClaims\": [\n      \"Requested model proves actual model.\",\n      \"Different role names prove model diversity.\",\n      \"Unknown actual models establish diversity.\",\n      \"Cached documentation proves current session tools.\",\n      \"Portable prompt files register custom agents.\",\n      \"Sequential fallback is independent workers or full pass.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/model-roles.json\"\n  },\n  {\n    \"id\": \"unsupported-selected-model\",\n    \"sourcePaths\": [\n      \"agents/poteto-agent.md\",\n      \"agents/comment-sicko.md\"\n    ],\n    \"prompt\": \"The requested model is unavailable or rejects the selected effort.\",\n    \"requirements\": [\n      \"Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n      \"Read portable role instructions; bind operations to observed session capabilities.\"\n    ],\n    \"expectedFull\": \"Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n    \"expectedReduced\": \"Authorized sequential role review preserves scope and reports reduced capability. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n    \"expectedBlocked\": \"Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.\",\n    \"forbiddenClaims\": [\n      \"Requested model proves actual model.\",\n      \"Different role names prove model diversity.\",\n      \"Unknown actual models establish diversity.\",\n      \"Cached documentation proves current session tools.\",\n      \"Portable prompt files register custom agents.\",\n      \"Sequential fallback is independent workers or full pass.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/model-roles.json\"\n  },\n  {\n    \"id\": \"verifiable-feature\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/feature.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"agents/poteto-agent.md\",\n      \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n      \"skills/how/SKILL.md\",\n      \"skills/how/references/explorer-prompt.md\",\n      \"skills/how/references/explainer-prompt.md\",\n      \"skills/architect/SKILL.md\",\n      \"skills/architect/references/runner-prompt.md\",\n      \"skills/architect/references/rationale-template.md\",\n      \"skills/arena/SKILL.md\",\n      \"skills/interrogate/SKILL.md\",\n      \"skills/interrogate/references/reviewer-prompt.md\",\n      \"skills/interrogate/references/rubric.md\",\n      \"skills/principle-model-the-domain/SKILL.md\",\n      \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n      \"skills/principle-sequence-verifiable-units/SKILL.md\"\n    ],\n    \"prompt\": \"Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.\",\n    \"requirements\": [\n      \"Read the complete mode and Feature playbook, required principle leaves and routed workflows. Record the eight playbook steps in a todo binding before task-specific items. Trace how the dashboard filters and renders orders before designing the export.\",\n      \"Use architect for design exploration. Retain two structurally distinct alternatives and its synthesis artifacts. Choose the named export data shape and organizing structure before code-writing. Use the complete arena contract for multiple valid implementation shapes, including isolated candidate paths, inspected candidates and a fresh cross-judge.\",\n      \"Keep all four checkpoint items, including n/a with a reason. Blocking gates precede fan-out. Split independent write targets before serializing real shared invariants. Rewrite the checkpoint at phase boundaries and keep it inline with the single code-coupled owner.\",\n      \"Assign the exact input SHA, owned paths, full poteto-agent prompt, role and success criteria. Use inherited model roles unless supported explicit choices are observed. Inspect returned artifacts and review the diff as the lead. A no-spawn worker owns the diff directly and returns to its parent, never waits for a nested agent. Required delegation and review separation have no laziness or skip escape.\",\n      \"Make surgical edits, re-ground upstream-derived files, propagate shared changes to every consumer and verify each. Preserve Comments rules and disclose missing deslop, no-comments or matching-control companions. Missing companion execution cannot become satisfied by assertion.\",\n      \"Deliver small units with a check before the next. Verify the exported literal rows, column order and escaping through fixture execution, and the empty-state feedback through the matching browser surface. Compilation alone and wrong-surface checks cannot establish the requested user outcome.\",\n      \"Run interrogate before shipping a contested design. Record worker independence and actual model limits. Prepare checked local changes and delivery order when commits, rebase, push or PR creation are unauthorized. Run complete Opening a PR when available and authorized, and retain exact missing dependency otherwise. Opening a PR never triggers Babysit implicitly.\",\n      \"Return what was built, choices and reasons, a table of design alternatives, all four checkpoint items and open decisions. Evidence names the end-user behavior and next-maintainer implications, missing capabilities and forbidden completion claims.\"\n    ],\n    \"expectedFull\": \"Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds.\",\n    \"expectedReduced\": \"With worker operations unavailable, authorized sequential grounding, design alternatives and direct implementation produce a useful local diff and outcome evidence. The report calls this reduced capability and retains mandatory independent delegation, arena cross-judge and review separation as unsatisfied gates. Inherited selections and unknown models supply no diversity claim. With no external authorization, return the local checked result and ordered delivery plan without push or PR creation. Missing companions retain their specific limits. A fixture CLI check may verify CSV bytes but cannot satisfy denied browser verification.\",\n    \"expectedBlocked\": \"Denied source or required missing skill stops dependent grounding or design. Missing independent operations block required review separation rather than waive it. Denied matching browser verification leaves the empty-state gate unverified, even if CSV fixtures pass. Missing opening-a-pr.md blocks PR-dependent work. Denied or unauthorized writes, commit, rebase or PR creation stay unperformed. The result reports the exact gate, available partial artifacts and open decisions without claiming complete delivery.\",\n    \"forbiddenClaims\": [\n      \"All four checkpoint dimensions apply, or omitted dimensions need no n/a explanation.\",\n      \"Sequential roles are independent workers, a fresh cross-judge, parallel exploration or independent review separation.\",\n      \"A no-spawn worker must wait on another worker, or Laziness Protocol permits skipping code-owner separation.\",\n      \"The source grok-4.7-xhigh-fast default proves a supported or selected host model.\",\n      \"A requested or inherited model proves the actual model or model diversity.\",\n      \"A compile, structural validator, inconclusive check or CSV-only test proves browser behavior or the complete feature outcome.\",\n      \"Unrun checks are green, all shared consumers were verified without observations, or ordered commits and rebases happened without authorization and evidence.\",\n      \"A missing companion or deferred Opening a PR playbook ran successfully.\",\n      \"A local PR draft is an actual PR, upstream autonomy authorizes external writes, or opening a PR starts Babysit.\",\n      \"Canonical prompts are registered custom agents, source metadata guarantees background execution, or isolated helper tests prove this host case passed.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/feature.json\"\n  },\n  {\n    \"id\": \"dependency-readiness\",\n    \"sourcePaths\": [\n      \"skills/automate-me/SKILL.md\",\n      \"skills/reflect/SKILL.md\",\n      \"skills/poteto-mode/SKILL.md\",\n      \"skills/poteto-mode/playbooks/authoring-a-skill.md\",\n      \"skills/poteto-mode/playbooks/shipping.md\",\n      \"skills/poteto-mode/playbooks/orchestrate.md\",\n      \"skills/poteto-mode/scripts/bootstrap.ts\",\n      \"automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md\"\n    ],\n    \"prompt\": \"Audit the current session before authoring a skill or verifying an app change. Use the dependency readiness records to name the selected authoring, review, control and repository-helper branches. Initially withhold control tools and installed helper metadata. Report what is blocked and what a local draft can establish. If the tester later supplies an authorized real driver and prepared helper copy, verify the exact caller contract and retain its action/result artifacts. Never install or enable a dependency to complete this case.\",\n    \"requirements\": [\n      \"Read the actual caller and available companion or helper contract, not only a skill name. Record exact exposed tool identifiers, denied or missing operations and observed outcomes.\",\n      \"Missing control-cli or control-ui leaves real-surface verification blocked. A named alternative must satisfy the same revision, user-path and action/result proof before use.\",\n      \"Missing create-skill leaves its required authoring loop unmet; provisional drafts and a manual structural checklist are reduced capability. Reflect application needs its required loop and approval.\",\n      \"Missing deslop is an unmet review gate until an explicitly authorized replacement review completes. Unslop alone does not satisfy it.\",\n      \"Selected orch and watch-pr helpers remain runtime bindings. Missing current package metadata blocks execution; do not install, bypass bootstrap or substitute historical snapshot results.\",\n      \"Discover each repository, forge, integration and setup requirement. Keep authorizations separate for writes, credentials, enabling, networking and schedules.\",\n      \"Retain current package commit, exact app/input revision and actual artifacts. Both hosts require their own observations; local tests establish only structural coverage.\"\n    ],\n    \"expectedFull\": \"With separately supplied and authorized capabilities, reads resolve the exact authoring validator and real app driver, required authoring/review loops complete, selected helpers execute from the prepared copy, and inspected artifacts prove the requested actions and end states. Missing-capability trials still stop dependent work without setup side effects. Record precise tools and successful operations for each exercised branch.\",\n    \"expectedReduced\": \"Authorized local drafting, source review or manual checklist work completes with inspected local artifacts. The response explicitly retains missing authoring loops, companion review, helper execution and real-control gates as unmet; no live verification or helper pass is claimed.\",\n    \"expectedBlocked\": \"With controls, required authoring workflows, helper metadata or permissions absent, the dependent branch stops and names the missing proof and setup scope. No installation, plugin enablement, credential change, integration connection, schedule or external action occurs. Keep partial local drafts separate from completed verification.\",\n    \"forbiddenClaims\": [\n      \"A skill name, bundled prompt or documented command proves an exposed and successful capability.\",\n      \"CI, a screenshot, fixtures or source inspection proves real user interaction.\",\n      \"The historical isolated 37b68c8 snapshot passes prove current helper or host execution.\",\n      \"Sequential roles are independent workers, or requested models are observed models.\",\n      \"A setup approval also authorizes host loading, integrations, credentials or external actions.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/dependencies.json\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository-test.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/repository-test.log",
      "sha256": "e02935108b2a280a7a2e9d82b011d4eb2df85e83d4f6cb672e2083d3660e49ce",
      "bytes": 397,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/sequential/repository/committed-inputs/csv.test.mjs:\n(pass) exports only current visible rows in displayed order and escapes literal commas and quotes [0.27ms]\n(pass) empty result gives actionable feedback [0.01ms]\n(pass) newlines and empty values retain CSV semantics [0.01ms]\n\n 3 pass\n 0 fail\n 3 expect() calls\nRan 3 tests across 1 file. [7.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/synthesis.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/synthesis.md",
      "sha256": "289117d98144c8729a88de2f655d22ab31c021da9cf9cf21d221a8b1f14dd537",
      "bytes": 1071,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Sequential arena synthesis\n\nWorker-unavailable variant is simulated by voluntarily withholding collaboration operations. Native tools remain exposed. Both candidate artifacts were produced sequentially by this agent. There is no independent runner or fresh judge. Mandatory independence remains unmet.\n\nRubric is exact filtering, displayed column agreement, escaping and empty feedback, isolated testability, and small maintainer burden. A wins filtering and testability; both can meet displayed columns and escaping; B needs DOM and has a virtualization risk. Both screen free of pass-through wrappers. A exposes one view representation and hides CSV formatting. B exposes markup as a data contract.\n\nChoose A as base. Graft B emphasis that rendering must consume the exact same column list. Reject DOM extraction because the supplied module has no DOM and CSV byte checks should run without one. No real cross-judge verdict exists.\n\nChosen named shape before code: OrderView and discriminated ExportResult, organized as a shared view projection with pure serializer.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/unit-1-tests.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/unit-1-tests.log",
      "sha256": "e18a29cd90a95aa588e161b457546b19200fded3c121c36f537df1a08c92caf8",
      "bytes": 373,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/sequential/app/csv.test.mjs:\n(pass) exports only current visible rows in displayed order and escapes literal commas and quotes [0.27ms]\n(pass) empty result gives actionable feedback [0.01ms]\n(pass) newlines and empty values retain CSV semantics [0.01ms]\n\n 3 pass\n 0 fail\n 3 expect() calls\nRan 3 tests across 1 file. [7.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/unit-2-tests.log",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/sequential/unit-2-tests.log",
      "sha256": "d061927cbd801c70ac4d77ea3487e4861f3cb6af7bf1028ddcf3d8c2d890d36f",
      "bytes": 373,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "bun test v1.4.2 (50a8a8387)\n\nverifiable-feature/sequential/app/csv.test.mjs:\n(pass) exports only current visible rows in displayed order and escapes literal commas and quotes [0.31ms]\n(pass) empty result gives actionable feedback [0.01ms]\n(pass) newlines and empty values retain CSV semantics [0.02ms]\n\n 3 pass\n 0 fail\n 3 expect() calls\nRan 3 tests across 1 file. [7.00ms]\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/source-hashes.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/source-hashes.json",
      "sha256": "a3a15658da14341d5d7ad429f6665da67738a82d5eb2b576060e397df7e71afe",
      "bytes": 2466,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "[\n  {\n    \"path\": \"skills/poteto-mode/playbooks/feature.md\",\n    \"sha256\": \"5ab43bd1145f1a4b059c0faa1ff6c97adb80c0f8b14f2d499a7fe5fbbea0170c\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/SKILL.md\",\n    \"sha256\": \"cb03eedb91cea96b570af30a7af317c6aae6a47a321cff2e82af656141ab0f14\"\n  },\n  {\n    \"path\": \"references/agent-prompts/poteto-agent.md\",\n    \"sha256\": \"9839239c6ebc72de8165f8a6fa4a6326fea7293e15a47d24f98396df2a61b3fb\"\n  },\n  {\n    \"path\": \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"sha256\": \"4198f32b22cf1d8ff367deee1dbfea805e6eecdd7ff1da3409ae7c0b07fb1c59\"\n  },\n  {\n    \"path\": \"skills/how/SKILL.md\",\n    \"sha256\": \"bca7b43af6d6d0089d20edb2ec2178d681d589357c20ea345eddbf81ce87f7e8\"\n  },\n  {\n    \"path\": \"skills/how/references/explorer-prompt.md\",\n    \"sha256\": \"5a799584adc07c774c4870846e34f0a8f8c82a75d151721d1aa225bb983523d2\"\n  },\n  {\n    \"path\": \"skills/how/references/explainer-prompt.md\",\n    \"sha256\": \"08618881df380b5c74a030d6a577fd07f0fc6a3a91b4d0ec1795da3c6350c9b1\"\n  },\n  {\n    \"path\": \"skills/architect/SKILL.md\",\n    \"sha256\": \"af93988bb4eec01a50f1caf71fd196a01f5affd56d2dcb36fe70d1735fa28f78\"\n  },\n  {\n    \"path\": \"skills/architect/references/runner-prompt.md\",\n    \"sha256\": \"f5b4eab549743b873594ff0c98430564c11e607d6fa0f27275b281ae59d46942\"\n  },\n  {\n    \"path\": \"skills/architect/references/rationale-template.md\",\n    \"sha256\": \"0cedfccdc7b47fc881febd5a8293eecbc542c20f8df825639904a8102d2eb5d3\"\n  },\n  {\n    \"path\": \"skills/arena/SKILL.md\",\n    \"sha256\": \"28ecec523bed9d58bc044fe5abc549fc18a7c9de8e5ee6a124f7331fb0200cad\"\n  },\n  {\n    \"path\": \"skills/interrogate/SKILL.md\",\n    \"sha256\": \"7a6714b0bfea7c2eb4a533f95873c80e17b7b6f9ef6314c0c42e8947602ad11b\"\n  },\n  {\n    \"path\": \"skills/interrogate/references/reviewer-prompt.md\",\n    \"sha256\": \"e0598e254792b56de39bb16b1e6db559b03a522fdc54b98f942d254090920ae6\"\n  },\n  {\n    \"path\": \"skills/interrogate/references/rubric.md\",\n    \"sha256\": \"a85aa801abbaf14434f00579440abc0d8e2723227ba8bf57de7cca8d6e7d2f25\"\n  },\n  {\n    \"path\": \"skills/principle-model-the-domain/SKILL.md\",\n    \"sha256\": \"05c073621ec18b442ecd7487dc6136bddb6a842f2bd537cb73567de7088a6b0e\"\n  },\n  {\n    \"path\": \"skills/principle-separate-before-serializing-shared-state/SKILL.md\",\n    \"sha256\": \"9ef714543b16665c68182e1b66beb22829fbc4b68e2ceb138db9858384c598ce\"\n  },\n  {\n    \"path\": \"skills/principle-sequence-verifiable-units/SKILL.md\",\n    \"sha256\": \"5818e68d1e41af2143362a3126b36ea6c15596b28a6e3a3235390c73cf4398a3\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/todo.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/todo.md",
      "sha256": "7863fb96235f133bfbd4ed7bd60a62f2af3e3c2297f1e4d39a432a49de929dc4",
      "bytes": 6332,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# Feature todo\n\nReduced todo binding: authorized Markdown, no exposed todo operation.\n\n1. Run [how](../../how/SKILL.md) over the affected subsystem. Ground the intended user outcome in traced source and caller behavior.\n2. Run [architect](../../architect/SKILL.md) for parallel design exploration. Follow its complete design and arena contracts. Preserve sequential alternatives only as reduced capability when independent workers are unavailable. Required independence remains blocked.\n3. Write the throughput checkpoint as four todo items. Keep any dimension that does not apply, such as a single file or no fan-out, with `n/a: <reason>` rather than dropping it.\n   - Blocking first steps. Gates run before fan-out.\n   - Independent workstreams. Disjoint files, services, or layers parallelize. Shared writes serialize.\n   - Shared mutable state. Default to splitting the target using [separate-before-serializing-shared-state](../../principle-separate-before-serializing-shared-state/SKILL.md). Serialize only for real invariants.\n   - Smallest safe decomposition. If one worker is best, name why.\n4. Delegate code-writing to a fresh independent worker with the entire [poteto role prompt](../../../references/agent-prompts/poteto-agent.md) and exact file pointers. Use the configured feature role when supported and observed. Otherwise request inherited model and effort. Record requested and observed selections separately, with unknown for unobserved values. Assign exact file paths, a named data shape and its organizing structure, and success criteria tied to the user outcome. Choose the structure before the delegate writes logic under [model-the-domain](../../principle-model-the-domain/SKILL.md). Prefer a state machine over scattered booleans, a table or registry over branching, or a typed model over repeated shape assumptions. When implementation admits multiple valid shapes, such as error handling, abstraction layer or test structure, delegate through [arena](../../arena/SKILL.md). Its runners surface alternatives and its fresh cross-judge guards the pick. This gate is mandatory. There is no skip-with-reason escape, and Laziness Protocol does not override it. The gain is review separation, not lines saved. A worker forbidden to spawn owns the diff directly and returns it to the lead for the same review separation. It never waits on a nested worker or replies \"standing by\". Without authorized independent workers, direct implementation can be an explicit reduced result, but it does not satisfy independent review separation. The lead reviews the actual diff and owns the summary. Apply the mode's Comments rules. Make surgical edits and re-ground upstream-derived files against their source. Port shared-primitive improvements to all consumers and verify each. Commit each verified unit when authorized and after the mode's commit gates.\n5. Verify on the matching surface using available authorized control tools and the mode's matching companion requirements. Tie observed evidence to the intended user outcome. \"Inconclusive\" or wrong-surface is not a pass. Flag it and retain the unverified gate. Compilation or structural checks do not prove the feature works.\n6. Rebase into small, ordered commits and stack follow-ups when authorized and safe for concurrent work. Use [sequence-verifiable-units](../../principle-sequence-verifiable-units/SKILL.md). Build, verify and commit each small unit before the next. An unrun required check blocks advancement. If commit or rebase is unavailable or unauthorized, return the checked diff and ordered delivery plan with those operations unperformed.\n7. If the design is contested, run [interrogate](../../interrogate/SKILL.md) before shipping. Preserve its review rubric, independence and observed model-diversity limits. Sequential review does not become independent or multi-model review.\n8. Run the Opening a PR playbook at `opening-a-pr.md` in this directory. This caller requires that complete playbook, its review gates and actual PR result inspection. If the file is absent, report the exact deferred dependency and stop PR-dependent work. Do not reconstruct it from this paragraph. External PR creation and push require actual authorization. Return a local reviewable result when those actions are unavailable or unauthorized. Never claim a local draft is a created PR. Opening a PR does not start Babysit.\n\n\n## Architect\n- Ground\n- Sketch\n- Agree\n- Implement\n- Scrap\n\n## Arena\n- Frame\n- Fan out\n- Cross-judge\n- Pick\n- Graft\n- Verify\n\n## Throughput checkpoint, grounding\n- Blocking first steps. Verify exact input, trace fixture, read contracts before design.\n- Independent workstreams. Candidate directories are disjoint. Worker slots currently all occupied; sequential reduced variant first.\n- Shared mutable state. Single selected app owner; candidates never share output directories.\n- Smallest safe decomposition. CSV serializer first, then caller/UI integration. One owner prevents displayed/exported column drift.\n\n## Throughput checkpoint, implementation\n- Blocking first steps. Input SHA and contracts read; two sequential architect alternatives synthesized before code. Native delegation attempted and rejected by actual host thread limit.\n- Independent workstreams. n/a for selected implementation because serializer and caller share the same OrderView invariant. Design alternatives have isolated directories. No concurrent shared writes.\n- Shared mutable state. One owner writes each app directory. Renderer and export both derive columns and rows from orderView.\n- Smallest safe decomposition. Unit 1 projection and serializer passed three literal tests before Unit 2 added UI shell. Unit 2 CSV rerun passed. Browser gate remains blocked.\n\n## Throughput checkpoint, handoff\n- Blocking first steps. Required independent arena, code owner and review remain pending native capacity. Matching control-ui and browser unavailable. No downstream delivery claim.\n- Independent workstreams. n/a for final integration because one canonical OrderView drives table and CSV. Each variant owns a distinct directory.\n- Shared mutable state. Repository working tree has one owner, no committed outputs.\n- Smallest safe decomposition. Checked local Unit 1 then Unit 2 changes ready for authorized future delivery. Commit/rebase/push/PR steps unperformed.\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/write-result.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature/write-result.mjs",
      "sha256": "26162f0d044939896ce4a4b0f715dd837d1da692d69dbfc6e25eb2f45e394afb",
      "bytes": 9356,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "const c=await Bun.file('verifiable-feature/contract.json').json();\nconst text=`# verifiable-feature\n\n## Supplied input\n\n${c.prompt}\n\nThe complete supplied requirements, outcomes and forbidden claims are preserved in verifiable-feature/contract.json. Input Git revision 933a5f5df924b2b089f410615f99af7851010643 was verified using git rev-parse HEAD and git ls-tree. It contains committed-inputs/dashboard.mjs and orders.json. The plugin source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied provenance, distinct from input revision. No installed package Git HEAD could be verified by the parent because the installed package is not a Git repository. Only installed 0.1.0 sources were read.\n\n## Actual output\n\nA checked local CSV implementation and a newly authored local dashboard shell exist under verifiable-feature/sequential/app and an isolated detached local repository at verifiable-feature/sequential/repository. No source UI existed in the fixture. This implementation uses the named OrderView shape, with a shared ordered column list and filtered rows. ExportResult is either ready with CSV bytes or empty with actionable feedback.\n\nExporting the open filter with displayed columns customer,total,id produces the literal artifact verifiable-feature/sequential/export.csv. It excludes the closed Hidden order, excludes an additional explicit hidden:true open order in the test, preserves the column order, doubles embedded quotes, and quotes comma/newline values. Empty-result feedback is verified as a pure function return only. The UI is authored but remains unverified in a matching browser.\n\n| Design | Shape | Decision |\n| --- | --- | --- |\n| A | Shared OrderView projection consumed by table and pure serializer | Selected. Filter and column identity are shared, CSV bytes run in Bun. |\n| B | Read visible headers and cells from rendered table DOM | Rejected. No original DOM exists; virtualized rows and formatted text would couple export to markup. Grafted its requirement that the exact same displayed column list drives export. |\n\nThe next maintainer inherits one view projection and a discriminated export result. The exportCsv argument changed from raw orders to OrderView. No production callers were supplied. The newly authored caller is updated; unprovided consumers remain outside verified scope.\n\n## Source and workflow observations\n\nAll named sources were read through functions.exec and tools.exec_command using Bun.file or cat. The full contents are retained in source-reads.txt. Supporting capability, assignment, model, ownership, architecture screening and interrogate review files are retained in support-reads.txt. The full mode was additionally read in sections, including the Principles index and Comments rules. No package 0.2.1 reads or live services were used.\n\nFeature's eight steps were copied verbatim into todo.md before task-specific work. This authorized Markdown file is the reduced todo binding because no todo tool is exposed. Architect and arena phases are also retained. Sequential architecture packages, synthesis, screening and full filled interrogate prompt are saved under sequential/. They are not independent exploration or cross-judging.\n\nModel the Domain selected OrderView and ExportResult before logic. Separate Before Serializing Shared State assigned disjoint variant and candidate directories. Sequence Work into Verifiable Units required the first serializer check before UI code. Prove It Works and Test Behavior, Not Implementation led to literal output assertions and an actual CSV artifact. Laziness Protocol rejected a DOM extraction layer without an existing UI. Unslop was applied to the reports; it does not satisfy missing deslop.\n\n## Variants attempted\n\n| Variant | Actual method and results | Limits |\n| --- | --- | --- |\n| Workers permitted, no external delivery | Actual collaboration.spawn_agent request for feature-design-a failed with agent thread limit reached. Native-spawn-attempt.json records the observed failure. Local design and implementation proceeded only as an explicit reduction. | This observed failed request is not a worker receipt. Independent design, code owner separation and fresh arena judge remain unmet unless later native artifacts are added. |\n| Worker operations unavailable | Voluntarily withheld collaboration operations and executed two sequential design alternatives, comparison, implementation and reduced interrogate review. Unit 1 tests, Unit 2 rerun and isolated repository rerun each returned 3 pass, 0 fail, exit 0. | This condition is simulated for the dedicated variant. The separate native spawn failure is real host capacity enforcement. Sequential roles do not establish independent workers or review. |\n| Matching browser denied | Copied app into browser-denied/app and reran literal CSV tests, 3 pass, 0 fail, exit 0. Browser calls were withheld in this variant. | The denied condition is simulated, not an actual permission rejection. Separately, actual mcp__cua_repl.js createBrowserTab to localhost failed with Browser is not available: iab; cua.listBrowsers returned []. No screenshot, video, download receipt or rendered empty feedback was produced. |\n\n## Ordered implementation units and checks\n\n1. Shared view projection and CSV serializer. Run bun test verifiable-feature/sequential/app/csv.test.mjs. Three tests passed before UI integration. Evidence is sequential/unit-1-tests.log.\n2. Local fixture UI with status selector, rendered table, export button and status message. CSV regression rerun passed in sequential/unit-2-tests.log. Browser verification remains blocked, so full user outcome is incomplete.\n3. Isolated local repository packaging. git clone --no-hardlinks --no-checkout copied only the committed local repository and checkout --detach selected the exact input revision. No commit, rebase or remote operation occurred. Clone output is sequential/clone.log and actual dashboard diff is sequential/dashboard.diff. The same tests ran against repository files and passed in sequential/repository-test.log.\n\nActual exported bytes and the serialized result are saved in sequential/export.csv and sequential/export-run.log. The test logs include only actual Bun output. Their durations are Bun's reported durations, not independently measured performance claims. The local fixture server was started on 127.0.0.1:59481, then stopped with Ctrl-C, observed exit 130. No external service was contacted.\n\n## Throughput checkpoint\n\n- Blocking first steps. Exact input, full source contracts and fixture trace preceded design. Two alternatives and named shapes preceded code. Required independent workers, companion review and matching browser gates remain visible.\n- Independent workstreams. Candidates and variants own disjoint paths. n/a for fan-out of the selected serializer/caller because both share the same OrderView contract and have one code-coupled owner in the reduced variant.\n- Shared mutable state. Renderer and CSV consume one ordered column list and one filtered projection. Each output tree has one writer. No worker integration or shared Git mutation occurred.\n- Smallest safe decomposition. Projection/serializer with literal tests first, then local UI shell and CSV regression. The UI's missing matching check blocks a complete feature claim. Checkpoints at grounding, implementation and handoff are saved in todo.md.\n\n## Review and delivery gates\n\nThe reduced interrogate review preserves intent, rubric and code-quality lens. It records browser proof as unmet and formula-leading spreadsheet values as a scoped product decision. It is the same agent reading twice, not independent reviewers or consensus. Model requests remain inherit-parent, observed models unknown. No diversity claim is made.\n\nThe installed no-comments skill is available, but its required independent comment reviewer was not run under the current worker capacity limit. No comments were added to generated production or test code. That source inspection does not satisfy the companion. deslop and control-ui are not exposed. create-skill is not exposed and no authoring loop is claimed. No dependency was installed or enabled.\n\nOpening a PR was read in full. Commit, rebase, push, PR creation and external writes are forbidden in this evaluation. Its external branches were left unperformed. Missing deslop and independent review gates remain unmet. No forge discovery contacted a service, no real PR exists, and Babysit was not started.\n\n## Open decisions and limits\n\nThe complete intended user outcome remains incomplete until a matching browser verifies table/filter identity, actual download bytes and the visible empty-result message. A supplied authorized driver is required. Independent architecture/arena/code-owner/review operations must be rerun when actual capacity permits. Decide whether spreadsheet formula protection belongs in a later scope before using arbitrary customer data. A real app would also need its actual displayed-column settings and hidden-order policy supplied, rather than the synthetic assumptions here.\n\nNo self-grade is assigned. Local CSV checks establish literal fixture behavior only, not current host parity, production behavior, a browser pass or completed delivery.\n`;\nawait Bun.write('verifiable-feature.result.md',text);\nconsole.log('Wrote verifiable-feature.result.md');\n"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/verifiable-feature.result.md",
      "sha256": "0643968afcd3c5c385eefe4cd054b86d9ebbf061b647c91b32400e819652d5ff",
      "bytes": 14950,
      "owners": [
        "grades-native-12.json#4"
      ],
      "text": "# verifiable-feature\n\n## Supplied input\n\nImplement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.\n\nComplete supplied requirements, outcomes and forbidden claims are retained in verifiable-feature/contract.json. Input Git revision 933a5f5df924b2b089f410615f99af7851010643 was independently verified through git show, rev-parse and ls-tree. Actual command records are in verifiable-feature/revision-commands.json. The installed plugin source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied provenance, distinct from task input. Installed package is not a Git repository, so no installed-package HEAD claim is made. Source hashes are retained in verifiable-feature/source-hashes.json. No output artifacts were treated as pre-existing input-revision content.\n\n## Actual output\n\nThe final native local implementation is verifiable-feature/native/final/repository/committed-inputs/. It is an isolated local clone detached at the exact input revision with uncommitted output. It implements projectOrders and exportTableCsv around the selected DisplayTable shape. One private column registry produces ordered headers and scalar cell rows. Table rendering and CSV export consume that same current snapshot.\n\nFour literal tests with eight assertions passed in Unit 1 before UI authoring, Unit 2 after UI authoring, and the lead's independent rerun. All returned exit 0. Tests execute the actual final module and cover current status, hidden:true exclusion, column order, comma and quote escaping, embedded newlines, header quoting, empty-result feedback, changed selections and snapshot isolation. Exact output is retained in native/final-lead-export.csv and final-lead-export-result.json. The exported open rows contain Ada, Inc. and Say \"Hi\" and exclude the closed Hidden row. The UI shell is newly authored fixture work because the supplied dashboard was only two functions, with no original renderer or browser caller.\n\nEmpty feedback is observed as a pure function value. Matching browser display, interaction and file-download behavior remain unverified. Browser bundle parsing and literal CSV execution do not satisfy that gate.\n\nThe next maintainer inherits a single projected cell matrix and one registry instead of independent display/export lists. The unsafe raw-orders export signature is removed. The new browser consumer uses its replacement. There were no supplied production callers; unprovided consumers remain outside inspected scope.\n\n## Sources, tools and workflow\n\nOnly /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 was used for package source. All 17 named source files were actually read through functions.exec with tools.exec_command and Bun.file or cat. Contents are preserved in source-reads.txt. Full mode, Principles index, role and feature contract were read, with the full mode additionally inspected in sections. Supporting capability, assignment, model, ownership, architecture screening and review contracts are in support-reads.txt. Opening a PR, no-comments and Comment Sicko were read in full. No 0.2.1 source was used.\n\nThe first eight items of todo.md copy the Feature playbook verbatim before task-specific items. Markdown is the reduced todo binding because no task-list operation is exposed. Architect and arena phases are included. Grounding traced visible and exportCsv from the committed source and explicitly recorded the absent original renderer. The initial direct how pass is reduced exploration, not an independent explainer.\n\nReal operation bindings were functions.exec to tools.exec_command for reads, writes, Git and Bun execution; collaboration.spawn_agent for successful independent identities and the initial thread-limit failure; returned native terminal messages plus artifact reads for result inspection; mcp__cua_repl.js for the actual failed local-browser binding and empty browser inventory. No role prompt was treated as a registered custom agent. Every spawned code owner received the entire portable poteto-agent prompt, exact revision, scope, owned path, selected data shape, success predicates and inherited-selection policy. Workers were forbidden nested spawning and returned their own diffs directly.\n\n## Native design and implementation chronology\n\n1. A native design spawn initially failed with agent thread limit reached. Native-spawn-attempt.json preserves that failure. No worker identity or output was invented.\n2. While slots were full, the explicit worker-unavailable variant ran sequentially. An initial fresh native code-owner later implemented a separately labelled pilot based on that reduced design. It lives under native/owner/. Its diff and four literal tests were inspected. It preceded native arena and is not retroactively represented as correctly ordered final work.\n3. Two fresh independent architect candidates ran with overlapping lifetimes and disjoint paths native/candidate-a/ and candidate-b/. Both received the same saved task, grounding and exact input revision. Parent rubric was withheld from their requests. Full design, sketch and result packages were inspected after terminal returns.\n4. Fresh independent judge /root/feature_case/arena_judge started only after both candidates were terminal and inspected. It read the rubric and both completed packages. Parent and judge chose B. Parent's initial optimistic design scores were reduced by the judge because sketches did not constitute executed hidden-row and quoting proof. Those scores compare designs only and are never case grades.\n5. The native/synthesis.md selected DisplayTable before final code. A fresh independent final code owner /root/feature_case/final_feature_owner then re-grounded the exact committed inputs in a new isolated local repository and implemented the selected shape. The lead inspected its actual tracked diff plus every untracked browser, HTML and test file. Lead checks confirm exact unchanged input HEAD, four tests/eight assertions with exit 0, and diff whitespace check exit 0. See native/final-lead-checks.json.\n6. Fresh independent adversarial reviewers inspected the actual final code with the same filled prompt, and a separate Comment Sicko reviewed scoped comments. The first adversarial round preceded the comment companion, so a fresh post-comment round was dispatched to preserve required review ordering. Both post-comment reviewers are terminal with no findings; the lead inspected their reports and matching final hashes. Exact outcomes are retained in native/final-review-addendum.md.\n\nNative arena's actual identity/order/hash receipt is native/arena-method-receipt.json. Append-only selected method events are native/arena-events.jsonl. No method validator pass or host parity claim is made. The design receipt proves only observed design operations and artifacts, not browser functionality.\n\n| Alternative | Actual design | Choice |\n| --- | --- | --- |\n| Native A | Ordered domain rows plus column keys; rendering and serialization each project fields | Rejected as base because consumers still interpret projection policy. Grafted raw-export removal and current-selection guarantees. |\n| Native B | Ordered headers plus scalar cell matrix projected once | Selected. Both consumers use exactly the same cells and positions. |\n| Sequential alternative | Extract rendered DOM headers and rows | Rejected in the reduced trial. It was not a native candidate. No original DOM existed and virtualization would couple export to markup. |\n\nA and B are structurally distinct data representations and projection responsibilities within a shared-snapshot architecture. They are not independent DOM versus domain implementations. The synthesis rejected grafting raw rows back into B. Private typed branding in design sketches is not claimed as runtime JavaScript enforcement.\n\n## Requested variants\n\n| Variant | Actual actions/results | Enforced or simulated condition |\n| --- | --- | --- |\n| Workers permitted, no push/PR | Initial spawn failed; later successful native pilot, two design candidates, fresh judge, fresh final owner and independent reviewers produced inspected artifacts. Final serializer checks passed as above. | Initial thread limit was real. Worker operations later became available when sibling cases ended. No claim that the full run remained worker-unavailable. |\n| Worker operations unavailable | Separate sequential alternatives, direct implementation and reduced same-agent arena/interrogate/no-comments review under sequential/. Unit 1, Unit 2 and isolated-repository checks each returned three tests passed, zero failed, exit 0. | Dedicated negative condition was simulated by withholding collaboration calls. Initial native thread-limit rejection is separately real. Sequential roles do not establish independence or model diversity. |\n| Matching browser verification denied | App copy under browser-denied/app and literal CSV rerun returned three tests passed, zero failed, exit 0. No browser action was attempted in that dedicated negative variant. | Requested denial was simulated, not a host permission rejection. Separately, an actual local fixture server was started on 127.0.0.1:59481. mcp__cua_repl.js createBrowserTab failed with Browser is not available: iab and cua.listBrowsers returned []. The server was stopped with Ctrl-C, observed exit 130. |\n\nActual browser observations are retained in browser-attempt.json. No screenshot, video, operator visual review, download receipt or rendered empty message was fabricated. No external live service was contacted. The negative CSV check cannot satisfy a browser gate.\n\n## Ordered implementation units and delivery order\n\n1. Change `native/final/repository/committed-inputs/dashboard.mjs` and add `dashboard.test.mjs` for DisplayTable projection and literal CSV behavior. The code owner ran four tests with eight assertions and exit 0 before UI work. See `native/final/unit1.log`.\n2. Add `native/final/repository/committed-inputs/browser.mjs` and `index.html` as the consumer of the same projection. The owner reran the four tests with exit 0 and parsed the browser bundle. See `native/final/unit2.log` and `syntax.log`. Matching browser behavior remains blocked.\n3. Keep these checked local units in that order for any future authorized delivery. No commit, rebase, push or PR was performed. The lead read actual code, diff and untracked additions and recorded `native/final-lead-checks.json`.\n\n## Throughput checkpoint\n\n- Blocking first steps. Exact input, full source contracts and source trace preceded design. Native synthesis selected the data shape before the fresh final code-owner. Required browser verification and deslop remain unmet; no downstream delivery completion follows.\n- Independent workstreams. Design candidates and all variants have disjoint owned paths. n/a for code fan-out because the selected renderer/serializer share one DisplayTable invariant and have one code-coupled owner. The no-spawn owner returned its own diff without waiting on nested workers.\n- Shared mutable state. A private registry projects one immutable scalar snapshot. Rendering and CSV consume that snapshot. No shared worker file writes occurred; the lead integrates only reports, not worker code in shared paths.\n- Smallest safe decomposition. Unit 1 projection/serializer with literal checks, then Unit 2 browser shell with CSV rerun and syntax evidence. Browser behavior stays blocked. Checkpoints are rewritten at grounding, implementation and handoff in todo.md and native/final/checkpoint.md.\n\nModel the Domain selected the projected matrix/result union. Separate Before Serializing Shared State assigned exclusive candidate/variant paths. Sequence Work into Verifiable Units required the serializer check before UI. Prove It Works and Test Behavior, Not Implementation led to literal expected rows and an actual CSV file. Laziness Protocol rejected a DOM extraction layer without an existing UI. Unslop shaped the prose. No missing companion is claimed satisfied by these principle applications.\n\n## Review, companion and delivery limits\n\nRequested models and efforts inherit parent for all native assignments. The exposed results do not identify actual models or efforts, which remain unknown. Distinct workers establish independence, not model diversity. The distinct-family/multi-model interrogate expectation remains unmet.\n\nThe complete filled interrogate prompt is native/interrogate-prompt.md. Native review-a/ and review-b/ contain independent source/CLI reviews with no findings, both with actual tests. Native/comments-review/ records a fresh scoped Comment Sicko review with no comments or suppressions, zero deletions, no application files touched, no MUST KILL flags and no skips. The lead read reports and hashes. Comment review does not supply application or browser correctness. The separate sequential no-comments review is explicitly reduced.\n\nRequired deslop is absent and no replacement was requested or authorized. It remains unmet. control-ui companion and a usable matching browser are absent. No create-skill authoring loop ran. Nothing was installed or enabled. Opening a PR was read in full; its commit, rebase, push, actual PR and readiness branches remain unperformed because this evaluation forbids them. Local artifacts are not a PR. Babysit and scheduling were not started.\n\n## Open decisions and completion boundary\n\nMatching browser verification must still establish current filter/column behavior, real downloaded bytes and visible empty feedback. Future localized totals and spreadsheet formula-prefix policy are open product choices. A real app must provide its actual hidden-order and column policy rather than inherit fixture assumptions. All current code is uncommitted checked local output; full user-outcome verification and delivery remain incomplete. \n\n## Final artifact readback\n\nThe lead read native/final/result.json, its actual tracked diff, all untracked added files, checkpoint, clone/checkouts, Unit 1/2 logs, syntax log, exact revision receipt, independent reviews and comment receipts. The final source hashes match the comment receipt and both post-comment reviews. The result file was read back after writing this final native/reduced account. All spawned feature workers returned terminal results; no pending worker or server is left running.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/input",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/arena-events.jsonl",
      "owner": "grades-native-12.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/.git",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/cache.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/invalidation.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/manifest.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/probe.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/corpus/records.jsonl",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/capsule.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/jay-mode.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/shared-records.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/adapter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/calculator.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/controller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/decision.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/exporter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/facade.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/formatter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/legal-header/source.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/legal-header/source.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/contract.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/types/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/types/boundary.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/types/context.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/README.md",
      "sha256": "7f821dbd93e694615d1b6f7e68deb494aece9a2ac94ed0c18130a921d79a16db",
      "bytes": 885
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/contract.test.mjs",
      "sha256": "5574d0adbf1362444a5d8e0b275a4d52cfed5c79dc3822f4560d6b24928e35a5",
      "bytes": 746
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/package.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/package.json",
      "sha256": "23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0",
      "bytes": 72
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/scope.md",
      "sha256": "ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed",
      "bytes": 866
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/contract.test.mjs",
      "sha256": "0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357",
      "bytes": 370
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/acceptance.json",
      "sha256": "b78eaadd9c51ef0e8d2e9d62c5a33b2401a60402d987f4e35c2eca30e37ac56b",
      "bytes": 1051
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/contracts.test-d.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/contracts.test-d.ts",
      "sha256": "09621ba45bc6b305494fbfd638f7f4a50e3a317d7e29c46b4ae2fe5f1e9d7393",
      "bytes": 393
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/fixture-data.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/fixture-data.mjs",
      "sha256": "88d28b907c36168895ebb41714241d2e048732aca9cfc1d6f4527e99c6dc4766",
      "bytes": 65
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/subject.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/subject.mjs",
      "sha256": "4caa5e38342d1b6d7c9c300b1bd2053a85071a1bc8692ad0e26a4e924d57755a",
      "bytes": 559
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/table-relations.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/table-relations.test.mjs",
      "sha256": "7e003161133181ab21e19164d6822c9862ae734f2e57bd22849fc688d3e7f375",
      "bytes": 313
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/types.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/types.ts",
      "sha256": "83c83c8964371ad48fa3e40fd853345a10b61b95305f923691887509535fdfe4",
      "bytes": 159
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/weak.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/weak.test.mjs",
      "sha256": "cf5c940e787b18d2aeccee5c6c0f1b5380c1ae72ab4689c0e62bf7f1091dd2dd",
      "bytes": 1147
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "sha256": "d2e70ba234d6fe44f90720f434de9c4d852b1d011c896bae05dc95d14ebd604e",
      "bytes": 181
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "sha256": "4d1bb9737921ca8c0f2ace2fb2667f6d25129b97b638f3c6f6b98c745793ea93",
      "bytes": 1230
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "sha256": "c315daf4798ca835c80167a0c7a500b8ef3e5a1ab3bbac960f77da6ffb7582e9",
      "bytes": 329
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "sha256": "7003f9342e3e3793c59dbd123e880671f4560daba2ece2a8cb6f5ecc712a9c37",
      "bytes": 360
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "sha256": "cba7e5d698834aea3720234622cc9112d5e8e973fe701909e879e286dd0bd173",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "sha256": "63c9f8ef6a34034155852809edc67940278acc3ccbafd782fc1ed561355d6985",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "sha256": "48176802619fac9611fb090606cf3cee51f4f5a5f7b74b165516123869f3f476",
      "bytes": 468
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "sha256": "e9be2f00fdddb0b74aa47376d40def0b339fc7c3041fe2a55fc3593aeba3566b",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "sha256": "70a41b59f243e31aa8725f2bc91fa50ce8e11e1c5bc7e6b56b8b2d36effe0965",
      "bytes": 676
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "sha256": "816fffa1d0d865b74e1d517904f430f57ddd1d354162eed3990f0827af7eefe5",
      "bytes": 987
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "sha256": "1b53ea08307686132d67111c7a303fe2d6c3a3b30e81f70d2d9682cc13a3cf90",
      "bytes": 1836
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/preparation-checks.json",
      "sha256": "c33031cda2f82cdfbc29c5c4aaa0c8e170598ea84207d1a442190a1bd78de490",
      "bytes": 271
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/README.md",
      "sha256": "c32f30175682ed130fe21ce13a9fbf8221cad5a8c940226a2bbc67a52b35b6a0",
      "bytes": 786
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/installed-compiler-paths.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/installed-compiler-paths.json",
      "sha256": "c9a2213f6c63612127b06d5df9afdd17d389ebab91c3b6800b787d800a903040",
      "bytes": 400
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/adapter.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/adapter.ts",
      "sha256": "973a111ea6960bcb983f7648e4bb9109f9868331e7caa54d6e250649fe48fa5d",
      "bytes": 726
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/boundary.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/domain.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/domain.ts",
      "sha256": "d3b548a63fb28faf90fff4ad3807fd32c621e7d66baba418e1ccede46a696609",
      "bytes": 544
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/internal-caller.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-caller.ts",
      "sha256": "6234d0e6d0fcc9744847b56195e52b5448c7f1f7683ce7cf89d5226788cfb305",
      "bytes": 110
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/internal-guards.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-guards.test.mjs",
      "sha256": "d6fd51c8cdb0df39ac877edde0921b1ebc2a10a3bc7cf9bc3e0dbfe0acd6d1ab",
      "bytes": 424
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/consumer.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/consumer.ts",
      "sha256": "8d8643c6ed3d985fa737fd32d45f2ef8b633233fefb28e61c695e6f76621f42a",
      "bytes": 156
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/index.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/index.ts",
      "sha256": "bb735ce533faf28a4e7dee68defc6f82ab620def17d5860c61717ed5a70bdfd3",
      "bytes": 87
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/legacy.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/legacy.ts",
      "sha256": "82a0d9fcad0c89d4f1dc1ad5887479b227c618b39670afff65e9d31c48d3d8d8",
      "bytes": 809
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/target.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "sha256": "056b611e72fda806524fbe5c5a9504a78a0be40987aa60ae3a935e5dbd1d8ac2",
      "bytes": 1091
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "sha256": "01097db9798dcfb10e0e64fe3da01cc53a1a2443c568a324dc2de27451047e0b",
      "bytes": 2141
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "sha256": "23e376c94df69fc62fa2e9b0aef92e0d1afc9d314aa3040bf463643fc8286896",
      "bytes": 546
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "sha256": "4b3b49eff4af7d55f915a744bc1af076207599a5755552de8d8d0c602d5d65be",
      "bytes": 669
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "sha256": "af65c1a192cb62afaf3312916e20b338f2e73ad0611d06ad8eda0173a9e345d9",
      "bytes": 926
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "sha256": "5b8355cc2824e8d488bcddb60d40bd5b0527e98fde8ff9c85e41f1473a5f0055",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "sha256": "0d2f283daba7269a9f5a301ff808e6f26422504c5e2c7eaad754214cec0ec460",
      "bytes": 1724
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/preparation-checks.json",
      "sha256": "29d7cc4aaa9fc9d628d2576f716204342312c30d784dc3cadf19b975392a3ddc",
      "bytes": 307
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/audit.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/audit.json",
      "sha256": "f1fe37db4c10a1cbe853dc6bd6b3b1552e1553e77fc2dd784dc29a8f0cb5bb89",
      "bytes": 68
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/team.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/team.json",
      "sha256": "38c17fac7484013aa87731b186320a4063d5a88483bad6f8d800ba82d61244c9",
      "bytes": 78
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/export.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/export.json",
      "sha256": "397f46dea18161080687041f785a21939fbb767369e9c4d5ca19d4ce75132c0b",
      "bytes": 82
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/search.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/search.json",
      "sha256": "23c1414ffb2f5e6b818318b418006bb91028260038177a270092610f625f924a",
      "bytes": 84
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "sha256": "8b6281181e6ae1cd4aee60f022303450c065d3ac028b174d95efe55672248ee7",
      "bytes": 62
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "sha256": "f71540be3ed66918ba50265eb11f8e795a9de3c358be8a1f72961725253aa61a",
      "bytes": 86
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/notes.txt",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/scenario-map.json",
      "sha256": "0db589dc3731bdcd0ff0653305a6de56fd1e8f8fe247a97a76209a14db7c1735",
      "bytes": 1870
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/forge.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/invoice.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/runtime.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/app/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/input",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/.git",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/cache.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/invalidation.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/manifest.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/probe.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/corpus/records.jsonl",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/capsule.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/jay-mode.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/shared-records.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/adapter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/calculator.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/controller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/decision.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/exporter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/facade.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/formatter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/legal-header/source.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/legal-header/source.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/contract.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/types/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/types/boundary.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/types/context.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/README.md",
      "sha256": "7f821dbd93e694615d1b6f7e68deb494aece9a2ac94ed0c18130a921d79a16db",
      "bytes": 885
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/contract.test.mjs",
      "sha256": "5574d0adbf1362444a5d8e0b275a4d52cfed5c79dc3822f4560d6b24928e35a5",
      "bytes": 746
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/package.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/package.json",
      "sha256": "23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0",
      "bytes": 72
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/scope.md",
      "sha256": "ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed",
      "bytes": 866
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/contract.test.mjs",
      "sha256": "0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357",
      "bytes": 370
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/acceptance.json",
      "sha256": "b78eaadd9c51ef0e8d2e9d62c5a33b2401a60402d987f4e35c2eca30e37ac56b",
      "bytes": 1051
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/contracts.test-d.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/contracts.test-d.ts",
      "sha256": "09621ba45bc6b305494fbfd638f7f4a50e3a317d7e29c46b4ae2fe5f1e9d7393",
      "bytes": 393
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/fixture-data.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/fixture-data.mjs",
      "sha256": "88d28b907c36168895ebb41714241d2e048732aca9cfc1d6f4527e99c6dc4766",
      "bytes": 65
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/subject.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/subject.mjs",
      "sha256": "4caa5e38342d1b6d7c9c300b1bd2053a85071a1bc8692ad0e26a4e924d57755a",
      "bytes": 559
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/table-relations.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/table-relations.test.mjs",
      "sha256": "7e003161133181ab21e19164d6822c9862ae734f2e57bd22849fc688d3e7f375",
      "bytes": 313
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/types.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/types.ts",
      "sha256": "83c83c8964371ad48fa3e40fd853345a10b61b95305f923691887509535fdfe4",
      "bytes": 159
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/weak.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/weak.test.mjs",
      "sha256": "cf5c940e787b18d2aeccee5c6c0f1b5380c1ae72ab4689c0e62bf7f1091dd2dd",
      "bytes": 1147
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "sha256": "d2e70ba234d6fe44f90720f434de9c4d852b1d011c896bae05dc95d14ebd604e",
      "bytes": 181
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "sha256": "4d1bb9737921ca8c0f2ace2fb2667f6d25129b97b638f3c6f6b98c745793ea93",
      "bytes": 1230
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "sha256": "c315daf4798ca835c80167a0c7a500b8ef3e5a1ab3bbac960f77da6ffb7582e9",
      "bytes": 329
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "sha256": "7003f9342e3e3793c59dbd123e880671f4560daba2ece2a8cb6f5ecc712a9c37",
      "bytes": 360
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "sha256": "cba7e5d698834aea3720234622cc9112d5e8e973fe701909e879e286dd0bd173",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "sha256": "63c9f8ef6a34034155852809edc67940278acc3ccbafd782fc1ed561355d6985",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "sha256": "48176802619fac9611fb090606cf3cee51f4f5a5f7b74b165516123869f3f476",
      "bytes": 468
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "sha256": "e9be2f00fdddb0b74aa47376d40def0b339fc7c3041fe2a55fc3593aeba3566b",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "sha256": "70a41b59f243e31aa8725f2bc91fa50ce8e11e1c5bc7e6b56b8b2d36effe0965",
      "bytes": 676
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "sha256": "816fffa1d0d865b74e1d517904f430f57ddd1d354162eed3990f0827af7eefe5",
      "bytes": 987
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "sha256": "1b53ea08307686132d67111c7a303fe2d6c3a3b30e81f70d2d9682cc13a3cf90",
      "bytes": 1836
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/preparation-checks.json",
      "sha256": "c33031cda2f82cdfbc29c5c4aaa0c8e170598ea84207d1a442190a1bd78de490",
      "bytes": 271
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/README.md",
      "sha256": "c32f30175682ed130fe21ce13a9fbf8221cad5a8c940226a2bbc67a52b35b6a0",
      "bytes": 786
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/installed-compiler-paths.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/installed-compiler-paths.json",
      "sha256": "c9a2213f6c63612127b06d5df9afdd17d389ebab91c3b6800b787d800a903040",
      "bytes": 400
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/adapter.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/adapter.ts",
      "sha256": "973a111ea6960bcb983f7648e4bb9109f9868331e7caa54d6e250649fe48fa5d",
      "bytes": 726
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/boundary.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/domain.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/domain.ts",
      "sha256": "d3b548a63fb28faf90fff4ad3807fd32c621e7d66baba418e1ccede46a696609",
      "bytes": 544
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/internal-caller.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-caller.ts",
      "sha256": "6234d0e6d0fcc9744847b56195e52b5448c7f1f7683ce7cf89d5226788cfb305",
      "bytes": 110
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/internal-guards.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-guards.test.mjs",
      "sha256": "d6fd51c8cdb0df39ac877edde0921b1ebc2a10a3bc7cf9bc3e0dbfe0acd6d1ab",
      "bytes": 424
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/consumer.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/consumer.ts",
      "sha256": "8d8643c6ed3d985fa737fd32d45f2ef8b633233fefb28e61c695e6f76621f42a",
      "bytes": 156
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/index.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/index.ts",
      "sha256": "bb735ce533faf28a4e7dee68defc6f82ab620def17d5860c61717ed5a70bdfd3",
      "bytes": 87
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/legacy.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/legacy.ts",
      "sha256": "82a0d9fcad0c89d4f1dc1ad5887479b227c618b39670afff65e9d31c48d3d8d8",
      "bytes": 809
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/target.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "sha256": "056b611e72fda806524fbe5c5a9504a78a0be40987aa60ae3a935e5dbd1d8ac2",
      "bytes": 1091
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "sha256": "01097db9798dcfb10e0e64fe3da01cc53a1a2443c568a324dc2de27451047e0b",
      "bytes": 2141
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "sha256": "23e376c94df69fc62fa2e9b0aef92e0d1afc9d314aa3040bf463643fc8286896",
      "bytes": 546
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "sha256": "4b3b49eff4af7d55f915a744bc1af076207599a5755552de8d8d0c602d5d65be",
      "bytes": 669
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "sha256": "af65c1a192cb62afaf3312916e20b338f2e73ad0611d06ad8eda0173a9e345d9",
      "bytes": 926
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "sha256": "5b8355cc2824e8d488bcddb60d40bd5b0527e98fde8ff9c85e41f1473a5f0055",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "sha256": "0d2f283daba7269a9f5a301ff808e6f26422504c5e2c7eaad754214cec0ec460",
      "bytes": 1724
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/preparation-checks.json",
      "sha256": "29d7cc4aaa9fc9d628d2576f716204342312c30d784dc3cadf19b975392a3ddc",
      "bytes": 307
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/audit.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/audit.json",
      "sha256": "f1fe37db4c10a1cbe853dc6bd6b3b1552e1553e77fc2dd784dc29a8f0cb5bb89",
      "bytes": 68
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/team.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/team.json",
      "sha256": "38c17fac7484013aa87731b186320a4063d5a88483bad6f8d800ba82d61244c9",
      "bytes": 78
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/export.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/export.json",
      "sha256": "397f46dea18161080687041f785a21939fbb767369e9c4d5ca19d4ce75132c0b",
      "bytes": 82
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/search.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/search.json",
      "sha256": "23c1414ffb2f5e6b818318b418006bb91028260038177a270092610f625f924a",
      "bytes": 84
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "sha256": "8b6281181e6ae1cd4aee60f022303450c065d3ac028b174d95efe55672248ee7",
      "bytes": 62
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "sha256": "f71540be3ed66918ba50265eb11f8e795a9de3c358be8a1f72961725253aa61a",
      "bytes": 86
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/notes.txt",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/scenario-map.json",
      "sha256": "0db589dc3731bdcd0ff0653305a6de56fd1e8f8fe247a97a76209a14db7c1735",
      "bytes": 1870
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/forge.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/invoice.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/runtime.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/source-reads.txt",
      "owner": "grades-native-12.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/support-reads.txt",
      "owner": "grades-native-12.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/browser-denied/app/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/input",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/arena-events.jsonl",
      "owner": "grades-native-12.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/.git",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/cache.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/invalidation.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/manifest.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/probe.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/corpus/records.jsonl",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/capsule.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/jay-mode.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/history/shared-records.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/adapter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/calculator.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/controller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/decision.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/exporter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/facade.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/invoice/formatter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/legal-header/source.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/legal-header/source.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/contract.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/types/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/types/boundary.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional/types/context.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/README.md",
      "sha256": "7f821dbd93e694615d1b6f7e68deb494aece9a2ac94ed0c18130a921d79a16db",
      "bytes": 885
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/contract.test.mjs",
      "sha256": "5574d0adbf1362444a5d8e0b275a4d52cfed5c79dc3822f4560d6b24928e35a5",
      "bytes": 746
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/package.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/package.json",
      "sha256": "23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0",
      "bytes": 72
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/caller-migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/scope.md",
      "sha256": "ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed",
      "bytes": 866
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/contract.test.mjs",
      "sha256": "0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357",
      "bytes": 370
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/acceptance.json",
      "sha256": "b78eaadd9c51ef0e8d2e9d62c5a33b2401a60402d987f4e35c2eca30e37ac56b",
      "bytes": 1051
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/contracts.test-d.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/contracts.test-d.ts",
      "sha256": "09621ba45bc6b305494fbfd638f7f4a50e3a317d7e29c46b4ae2fe5f1e9d7393",
      "bytes": 393
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/fixture-data.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/fixture-data.mjs",
      "sha256": "88d28b907c36168895ebb41714241d2e048732aca9cfc1d6f4527e99c6dc4766",
      "bytes": 65
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/subject.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/subject.mjs",
      "sha256": "4caa5e38342d1b6d7c9c300b1bd2053a85071a1bc8692ad0e26a4e924d57755a",
      "bytes": 559
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/table-relations.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/table-relations.test.mjs",
      "sha256": "7e003161133181ab21e19164d6822c9862ae734f2e57bd22849fc688d3e7f375",
      "bytes": 313
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/types.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/types.ts",
      "sha256": "83c83c8964371ad48fa3e40fd853345a10b61b95305f923691887509535fdfe4",
      "bytes": 159
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/empty-function/weak.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/weak.test.mjs",
      "sha256": "cf5c940e787b18d2aeccee5c6c0f1b5380c1ae72ab4689c0e62bf7f1091dd2dd",
      "bytes": 1147
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "sha256": "d2e70ba234d6fe44f90720f434de9c4d852b1d011c896bae05dc95d14ebd604e",
      "bytes": 181
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "sha256": "4d1bb9737921ca8c0f2ace2fb2667f6d25129b97b638f3c6f6b98c745793ea93",
      "bytes": 1230
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "sha256": "c315daf4798ca835c80167a0c7a500b8ef3e5a1ab3bbac960f77da6ffb7582e9",
      "bytes": 329
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "sha256": "7003f9342e3e3793c59dbd123e880671f4560daba2ece2a8cb6f5ecc712a9c37",
      "bytes": 360
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "sha256": "cba7e5d698834aea3720234622cc9112d5e8e973fe701909e879e286dd0bd173",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "sha256": "63c9f8ef6a34034155852809edc67940278acc3ccbafd782fc1ed561355d6985",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "sha256": "48176802619fac9611fb090606cf3cee51f4f5a5f7b74b165516123869f3f476",
      "bytes": 468
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "sha256": "e9be2f00fdddb0b74aa47376d40def0b339fc7c3041fe2a55fc3593aeba3566b",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "sha256": "70a41b59f243e31aa8725f2bc91fa50ce8e11e1c5bc7e6b56b8b2d36effe0965",
      "bytes": 676
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "sha256": "816fffa1d0d865b74e1d517904f430f57ddd1d354162eed3990f0827af7eefe5",
      "bytes": 987
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "sha256": "1b53ea08307686132d67111c7a303fe2d6c3a3b30e81f70d2d9682cc13a3cf90",
      "bytes": 1836
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/preparation-checks.json",
      "sha256": "c33031cda2f82cdfbc29c5c4aaa0c8e170598ea84207d1a442190a1bd78de490",
      "bytes": 271
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v2/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/README.md",
      "sha256": "c32f30175682ed130fe21ce13a9fbf8221cad5a8c940226a2bbc67a52b35b6a0",
      "bytes": 786
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/installed-compiler-paths.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/installed-compiler-paths.json",
      "sha256": "c9a2213f6c63612127b06d5df9afdd17d389ebab91c3b6800b787d800a903040",
      "bytes": 400
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/adapter.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/adapter.ts",
      "sha256": "973a111ea6960bcb983f7648e4bb9109f9868331e7caa54d6e250649fe48fa5d",
      "bytes": 726
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/boundary.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/domain.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/domain.ts",
      "sha256": "d3b548a63fb28faf90fff4ad3807fd32c621e7d66baba418e1ccede46a696609",
      "bytes": 544
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/internal-caller.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-caller.ts",
      "sha256": "6234d0e6d0fcc9744847b56195e52b5448c7f1f7683ce7cf89d5226788cfb305",
      "bytes": 110
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/internal-guards.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-guards.test.mjs",
      "sha256": "d6fd51c8cdb0df39ac877edde0921b1ebc2a10a3bc7cf9bc3e0dbfe0acd6d1ab",
      "bytes": 424
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/invalid-input/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/consumer.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/consumer.ts",
      "sha256": "8d8643c6ed3d985fa737fd32d45f2ef8b633233fefb28e61c695e6f76621f42a",
      "bytes": 156
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/index.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/index.ts",
      "sha256": "bb735ce533faf28a4e7dee68defc6f82ab620def17d5860c61717ed5a70bdfd3",
      "bytes": 87
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/legacy.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/legacy.ts",
      "sha256": "82a0d9fcad0c89d4f1dc1ad5887479b227c618b39670afff65e9d31c48d3d8d8",
      "bytes": 809
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/target.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/migration-end-state/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "sha256": "056b611e72fda806524fbe5c5a9504a78a0be40987aa60ae3a935e5dbd1d8ac2",
      "bytes": 1091
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "sha256": "01097db9798dcfb10e0e64fe3da01cc53a1a2443c568a324dc2de27451047e0b",
      "bytes": 2141
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "sha256": "23e376c94df69fc62fa2e9b0aef92e0d1afc9d314aa3040bf463643fc8286896",
      "bytes": 546
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "sha256": "4b3b49eff4af7d55f915a744bc1af076207599a5755552de8d8d0c602d5d65be",
      "bytes": 669
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "sha256": "af65c1a192cb62afaf3312916e20b338f2e73ad0611d06ad8eda0173a9e345d9",
      "bytes": 926
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "sha256": "5b8355cc2824e8d488bcddb60d40bd5b0527e98fde8ff9c85e41f1473a5f0055",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "sha256": "0d2f283daba7269a9f5a301ff808e6f26422504c5e2c7eaad754214cec0ec460",
      "bytes": 1724
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/preparation-checks.json",
      "sha256": "29d7cc4aaa9fc9d628d2576f716204342312c30d784dc3cadf19b975392a3ddc",
      "bytes": 307
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/audit.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/audit.json",
      "sha256": "f1fe37db4c10a1cbe853dc6bd6b3b1552e1553e77fc2dd784dc29a8f0cb5bb89",
      "bytes": 68
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/team.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/team.json",
      "sha256": "38c17fac7484013aa87731b186320a4063d5a88483bad6f8d800ba82d61244c9",
      "bytes": 78
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/export.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/export.json",
      "sha256": "397f46dea18161080687041f785a21939fbb767369e9c4d5ca19d4ce75132c0b",
      "bytes": 82
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/search.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/search.json",
      "sha256": "23c1414ffb2f5e6b818318b418006bb91028260038177a270092610f625f924a",
      "bytes": 84
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "sha256": "8b6281181e6ae1cd4aee60f022303450c065d3ac028b174d95efe55672248ee7",
      "bytes": 62
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "sha256": "f71540be3ed66918ba50265eb11f8e795a9de3c358be8a1f72961725253aa61a",
      "bytes": 86
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/notes.txt",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/repeatable-change/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/additional-v3/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/scenario-map.json",
      "sha256": "0db589dc3731bdcd0ff0653305a6de56fd1e8f8fe247a97a76209a14db7c1735",
      "bytes": 1870
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/forge.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/invoice.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/final/repository/committed-inputs/runtime.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/app/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/native/owner/input",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/app/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/.git",
      "owner": "grades-native-12.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/cache.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/invalidation.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/manifest.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/probe.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/corpus/records.jsonl",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/capsule.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/jay-mode.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/history/shared-records.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/adapter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/calculator.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/controller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/decision.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/exporter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/facade.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/invoice/formatter.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/legal-header/source.diff",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/legal-header/source.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/contract.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/types/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/types/boundary.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional/types/context.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/README.md",
      "sha256": "7f821dbd93e694615d1b6f7e68deb494aece9a2ac94ed0c18130a921d79a16db",
      "bytes": 885
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/api.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/contract.test.mjs",
      "sha256": "5574d0adbf1362444a5d8e0b275a4d52cfed5c79dc3822f4560d6b24928e35a5",
      "bytes": 746
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/notification.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/package.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/package.json",
      "sha256": "23c68e1798ad8ada5be997122e6a5a0d083a4909b0794ad9e73cf5b9f79575a0",
      "bytes": 72
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/profile.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/caller-migration/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/caller-migration/scope.md",
      "sha256": "ddb5e7db76fedf42ea104c690f4d2c2f4b90b703028a04e0a16bf03ebdae60ed",
      "bytes": 866
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/acceptance.json",
      "sha256": "1cd9c084c06c0d4ff71c6be25d7f9a6fdb2df574724fbc0f2a6663b819236e34",
      "bytes": 555
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/caller.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/contract.test.mjs",
      "sha256": "0d318a92de35579e17d98c95737a833a74cd21c9eb3d92c6a7752615e3dc6357",
      "bytes": 370
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/duplicate-reference.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/handler.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/instructions.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/dead-path/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/dead-path/scope.md",
      "sha256": "d0e086121f18a595548b118b64696270a50f5e6273335edea6fee07da5397528",
      "bytes": 861
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/acceptance.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/acceptance.json",
      "sha256": "b78eaadd9c51ef0e8d2e9d62c5a33b2401a60402d987f4e35c2eca30e37ac56b",
      "bytes": 1051
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/contracts.test-d.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/contracts.test-d.ts",
      "sha256": "09621ba45bc6b305494fbfd638f7f4a50e3a317d7e29c46b4ae2fe5f1e9d7393",
      "bytes": 393
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/fixture-data.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/fixture-data.mjs",
      "sha256": "88d28b907c36168895ebb41714241d2e048732aca9cfc1d6f4527e99c6dc4766",
      "bytes": 65
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/subject.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/subject.mjs",
      "sha256": "4caa5e38342d1b6d7c9c300b1bd2053a85071a1bc8692ad0e26a4e924d57755a",
      "bytes": 559
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/table-relations.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/table-relations.test.mjs",
      "sha256": "7e003161133181ab21e19164d6822c9862ae734f2e57bd22849fc688d3e7f375",
      "bytes": 313
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/types.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/types.ts",
      "sha256": "83c83c8964371ad48fa3e40fd853345a10b61b95305f923691887509535fdfe4",
      "bytes": 159
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/empty-function/weak.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/empty-function/weak.test.mjs",
      "sha256": "cf5c940e787b18d2aeccee5c6c0f1b5380c1ae72ab4689c0e62bf7f1091dd2dd",
      "bytes": 1147
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js",
      "sha256": "d2e70ba234d6fe44f90720f434de9c4d852b1d011c896bae05dc95d14ebd604e",
      "bytes": 181
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js",
      "sha256": "4d1bb9737921ca8c0f2ace2fb2667f6d25129b97b638f3c6f6b98c745793ea93",
      "bytes": 1230
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js",
      "sha256": "c315daf4798ca835c80167a0c7a500b8ef3e5a1ab3bbac960f77da6ffb7582e9",
      "bytes": 329
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js",
      "sha256": "7003f9342e3e3793c59dbd123e880671f4560daba2ece2a8cb6f5ecc712a9c37",
      "bytes": 360
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js",
      "sha256": "cba7e5d698834aea3720234622cc9112d5e8e973fe701909e879e286dd0bd173",
      "bytes": 553
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js",
      "sha256": "63c9f8ef6a34034155852809edc67940278acc3ccbafd782fc1ed561355d6985",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js",
      "sha256": "48176802619fac9611fb090606cf3cee51f4f5a5f7b74b165516123869f3f476",
      "bytes": 468
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js",
      "sha256": "e9be2f00fdddb0b74aa47376d40def0b339fc7c3041fe2a55fc3593aeba3566b",
      "bytes": 157
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js",
      "sha256": "70a41b59f243e31aa8725f2bc91fa50ce8e11e1c5bc7e6b56b8b2d36effe0965",
      "bytes": 676
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js",
      "sha256": "816fffa1d0d865b74e1d517904f430f57ddd1d354162eed3990f0827af7eefe5",
      "bytes": 987
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js",
      "sha256": "1b53ea08307686132d67111c7a303fe2d6c3a3b30e81f70d2d9682cc13a3cf90",
      "bytes": 1836
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/preparation-checks.json",
      "sha256": "c33031cda2f82cdfbc29c5c4aaa0c8e170598ea84207d1a442190a1bd78de490",
      "bytes": 271
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v2/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v2/scenario-map.json",
      "sha256": "2abfb830f67ad012f67363ab56783785cd2e21bf493bb91badb18242fddbd3ab",
      "bytes": 1477
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/README.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/README.md",
      "sha256": "c32f30175682ed130fe21ce13a9fbf8221cad5a8c940226a2bbc67a52b35b6a0",
      "bytes": 786
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/installed-compiler-paths.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/installed-compiler-paths.json",
      "sha256": "c9a2213f6c63612127b06d5df9afdd17d389ebab91c3b6800b787d800a903040",
      "bytes": 400
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/adapter.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/adapter.ts",
      "sha256": "973a111ea6960bcb983f7648e4bb9109f9868331e7caa54d6e250649fe48fa5d",
      "bytes": 726
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/boundary.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/domain.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/domain.ts",
      "sha256": "d3b548a63fb28faf90fff4ad3807fd32c621e7d66baba418e1ccede46a696609",
      "bytes": 544
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/internal-caller.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-caller.ts",
      "sha256": "6234d0e6d0fcc9744847b56195e52b5448c7f1f7683ce7cf89d5226788cfb305",
      "bytes": 110
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/internal-guards.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-guards.test.mjs",
      "sha256": "d6fd51c8cdb0df39ac877edde0921b1ebc2a10a3bc7cf9bc3e0dbfe0acd6d1ab",
      "bytes": 424
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/invalid-input/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/consumer.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/consumer.ts",
      "sha256": "8d8643c6ed3d985fa737fd32d45f2ef8b633233fefb28e61c695e6f76621f42a",
      "bytes": 156
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/contract.test.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/index.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/index.ts",
      "sha256": "bb735ce533faf28a4e7dee68defc6f82ab620def17d5860c61717ed5a70bdfd3",
      "bytes": 87
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/legacy.ts",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/legacy.ts",
      "sha256": "82a0d9fcad0c89d4f1dc1ad5887479b227c618b39670afff65e9d31c48d3d8d8",
      "bytes": 809
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/target.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/migration-end-state/tsconfig.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js",
      "sha256": "056b611e72fda806524fbe5c5a9504a78a0be40987aa60ae3a935e5dbd1d8ac2",
      "bytes": 1091
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js",
      "sha256": "01097db9798dcfb10e0e64fe3da01cc53a1a2443c568a324dc2de27451047e0b",
      "bytes": 2141
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js",
      "sha256": "23e376c94df69fc62fa2e9b0aef92e0d1afc9d314aa3040bf463643fc8286896",
      "bytes": 546
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js",
      "sha256": "4b3b49eff4af7d55f915a744bc1af076207599a5755552de8d8d0c602d5d65be",
      "bytes": 669
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js",
      "sha256": "af65c1a192cb62afaf3312916e20b338f2e73ad0611d06ad8eda0173a9e345d9",
      "bytes": 926
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js",
      "sha256": "5b8355cc2824e8d488bcddb60d40bd5b0527e98fde8ff9c85e41f1473a5f0055",
      "bytes": 937
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js",
      "sha256": "0d2f283daba7269a9f5a301ff808e6f26422504c5e2c7eaad754214cec0ec460",
      "bytes": 1724
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js",
      "sha256": "685f613ec6563db3b26ca1c97e9fad947b6525918eba6e5dba8efbee4c0a78f8",
      "bytes": 762
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/preparation-checks.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/preparation-checks.json",
      "sha256": "29d7cc4aaa9fc9d628d2576f716204342312c30d784dc3cadf19b975392a3ddc",
      "bytes": 307
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/audit.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/audit.json",
      "sha256": "f1fe37db4c10a1cbe853dc6bd6b3b1552e1553e77fc2dd784dc29a8f0cb5bb89",
      "bytes": 68
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/admin/team.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/team.json",
      "sha256": "38c17fac7484013aa87731b186320a4063d5a88483bad6f8d800ba82d61244c9",
      "bytes": 78
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/export.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/export.json",
      "sha256": "397f46dea18161080687041f785a21939fbb767369e9c4d5ca19d4ce75132c0b",
      "bytes": 82
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/core/search.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/search.json",
      "sha256": "23c1414ffb2f5e6b818318b418006bb91028260038177a270092610f625f924a",
      "bytes": 84
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "sha256": "8b6281181e6ae1cd4aee60f022303450c065d3ac028b174d95efe55672248ee7",
      "bytes": 62
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "sha256": "f71540be3ed66918ba50265eb11f8e795a9de3c358be8a1f72961725253aa61a",
      "bytes": 86
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/notes.txt",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/repeatable-change/scope.md",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/additional-v3/scenario-map.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/scenario-map.json",
      "sha256": "0db589dc3731bdcd0ff0653305a6de56fd1e8f8fe247a97a76209a14db7c1735",
      "bytes": 1870
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/forge.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/history.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/invoice.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/orders.json",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/sequential/repository/committed-inputs/runtime.mjs",
      "owner": "grades-native-12.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/source-reads.txt",
      "owner": "grades-native-12.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/verifiable-feature/support-reads.txt",
      "owner": "grades-native-12.json#4",
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
