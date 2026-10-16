# codex: reproduce-before-fix

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "reproduce-before-fix",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-10.json#7",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Fix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.",
  "caseDefinition": {
    "id": "reproduce-before-fix",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/interrogate/references/code-quality-review.md",
      "skills/interrogate/references/lead-judgment.md",
      "skills/tdd/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Fix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.",
    "requirements": [
      "Read the complete mode, six-step Bug fix playbook and each applied leaf. Record steps before task-specific todos and preserve lead ownership, delegated investigation and implementation, inspected artifacts and lead diff review.",
      "Reproduce yourself before production edits on the matching surface. Tighten the trigger or instrument until it fires. Ask the user to reproduce only after reaching the control limit and naming the specific reason the surface cannot reach the target. Missing controls or denied execution leave the gate unverified.",
      "Use full how and why workflows and their prompts to ground hypotheses and regression history. Preserve source coverage and confidence distinctions. Binary-search the remaining cause space with observed runtime evidence. Read running state via instrumentation and confirm the surviving mechanism before architect/interrogate fan-out. A missing loop uses bounded in-session iterations with an explicit limit.",
      "Cross-function changes require the complete architect contract and contested design requires interrogate. Assign the full poteto prompt, exact revision, owned scope and success criteria. Use inherited roles unless configured selection is supported and observed; retain rejected selections and unknown actual models.",
      "Ship only the smallest runtime-justified root-cause change. Revert patches motivated by refuted hypotheses. Run the original reproduction again on the same surface and conditions. Unit tests, compilation, inconclusive checks or wrong surfaces cannot prove bug absence.",
      "For a cheap local test, write and run its intended failure before the fix, then its pass afterward under full tdd. Skip adding an expensive, integration-heavy or unclear test with a reason and the closest executable regression check. Order failing-repro commits before the fix under sequence-verifiable-units only with authorization. Otherwise return the artifacts and delivery order as unperformed.",
      "Run full Opening a PR only when available and authorized. Preserve deferred missing companions, unauthorized external actions and unsatisfied independence. Reply with what was broken, root cause, fix, verification and verbatim failing-then-passing output. Missing outputs must stay explicit."
    ],
    "expectedFull": "Observed independent investigation and implementation return inspected artifacts at the assigned revision. Runtime evidence confirms the specific mechanism before design fan-out. Matching browser observations show stale rows before the bounded fix and correctly reset rows afterward under the same trigger. Refuted speculation is reverted. A cheap regression check fails before the fix and passes afterward. With actual delivery authorization and complete dependencies, the ordered commits and inspected PR demonstrate delivery. The reply includes verbatim observed outputs, root cause and verification. Unauthorized external delivery remains unperformed.",
    "expectedReduced": "Unavailable workers permit authorized sequential investigation and local implementation with reduced capability disclosed, while required independent delegation remains unsatisfied. Missing repeated-execution support allows bounded in-session hypothesis passes without background claims. An impractical new test is skipped with a reason and actual closest regression evidence. Without delivery authorization, return checked local artifacts and the failing-repro-before-fix order. Unknown model observations supply no diversity claim.",
    "expectedBlocked": "Denied or unavailable matching controls leave original reproduction or bug-absence verification blocked. A mechanism without runtime evidence cannot pass into the required design fan-out as confirmed. Missing required skills or Opening a PR stop dependent work. Missing independent workers block required delegation rather than waive it. Unauthorized writes, commits, rebases or external delivery stay unperformed. Report the exact gate and available partial evidence.",
    "forbiddenClaims": [
      "Unit tests, compilation or structural checks prove bug absence on the matching surface.",
      "An inconclusive or wrong-surface result passes, or an unrun reproduction is failing-before evidence.",
      "Asking the user to reproduce without first reaching and naming the specific control limit satisfies step 1.",
      "A plausible surviving hypothesis is a runtime-confirmed mechanism without observations.",
      "Refuted speculative patches may ship as precautionary fixes.",
      "Sequential roles are independent delegates, review, parallel fan-out or background execution.",
      "The historical default, requested selection or inheritance proves actual model availability or diversity.",
      "Unobserved output may be pasted as a verbatim reproduction transcript.",
      "A missing companion or deferred Opening a PR ran, a plan is landed history or a draft is a created PR.",
      "Upstream autonomy authorizes external writes or Opening a PR starts Babysit."
    ],
    "caseFile": "docs/parity/cases/playbooks/bug-fix.json"
  },
  "registry": {
    "caseId": "reproduce-before-fix",
    "caseFile": "docs/parity/cases/playbooks/bug-fix.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/interrogate/references/code-quality-review.md",
      "skills/interrogate/references/lead-judgment.md",
      "skills/tdd/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
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
      "attemptId": "grades-native-10.json#7",
      "order": 0,
      "gradeFile": "grades-native-10.json",
      "rankWithinFile": 7,
      "host": "codex",
      "caseId": "reproduce-before-fix",
      "status": "blocked",
      "grade": {
        "caseId": "reproduce-before-fix",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Matching dashboard/search implementation and controls",
          "Original-trigger before/after reproduction and runtime causal mechanism",
          "Required independent investigation/implementation/design method after reproduction"
        ],
        "review": "The fixture has filtering/export functions but no search field, cache, DOM, startup or browser harness. The exact stale-search symptom cannot be reproduced; no causal fix, refuted speculative patch or browser red/green output is invented. The separate CSV regression is not substituted.",
        "responseArtifact": "fixtures/batch-10/reproduce-before-fix.result.md",
        "rawTrace": "codex/batch-10.events.jsonl",
        "actualCommandEventIds": [
          "item_4",
          "item_5",
          "item_6",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_12",
          "item_13",
          "item_15",
          "item_19",
          "item_20",
          "item_23",
          "item_30",
          "item_31",
          "item_32"
        ],
        "nativeMethodReceipts": "native-10-11-tool-receipts.json",
        "variantReview": {
          "assessment": "Complete case response and explicit real/simulated/unrun branches inspected. Source-only negative views do not prove actual host capability removal or denial. Fixed-input gaps are not plugin bugs.",
          "sectionPresent": true
        },
        "limits": [
          "Baseline observations only; source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c remains distinct from actual fixture task revisions and new candidate source.",
          "Native parent/child persisted custom-tool and collaboration records independently inspected; protected dispatch message ciphertext omitted.",
          "Independent child turn_context records now establish gpt-6.1-sol for recovered10/11 sessions. This observation was unavailable to in-run workers and establishes no model-family diversity.",
          "Parent-captured read-only responses are not fabricated worker file-write operations. Proxy guards, local receipt shape checks and scenario metadata do not establish missing full method support."
        ],
        "reviewedBy": "review_workflow_evidence independent full-response/native parent-child rollout review",
        "fullExpected": "Observed independent investigation and implementation return inspected artifacts at the assigned revision. Runtime evidence confirms the specific mechanism before design fan-out. Matching browser observations show stale rows before the bounded fix and correctly reset rows afterward under the same trigger. Refuted speculation is reverted. A cheap regression check fails before the fix and passes afterward. With actual delivery authorization and complete dependencies, the ordered commits and inspected PR demonstrate delivery. The reply includes verbatim observed outputs, root cause and verification. Unauthorized external delivery remains unperformed.",
        "reducedExpected": "Unavailable workers permit authorized sequential investigation and local implementation with reduced capability disclosed, while required independent delegation remains unsatisfied. Missing repeated-execution support allows bounded in-session hypothesis passes without background claims. An impractical new test is skipped with a reason and actual closest regression evidence. Without delivery authorization, return checked local artifacts and the failing-repro-before-fix order. Unknown model observations supply no diversity claim.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# reproduce-before-fix\n\n## Supplied input\n\nFix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.\n\nComplete acceptance contract: [reproduce-before-fix/supplied-case.json](reproduce-before-fix/supplied-case.json). Supplied source paths were read in full from the installed created-by-me-remote/pstack-openai/0.1.0 tree with exec cat reads. They were copied with per-file SHA-256 in [reproduce-before-fix/evidence/source-reads.json](reproduce-before-fix/evidence/source-reads.json). The registry's agents/poteto-agent.md historical spelling differs from the user-named actual references/agent-prompts/poteto-agent.md, which was read. No local 0.2.1 source was used.\n\n## Actual response and stopping gate\n\nThe specified dashboard search defect could not be reproduced. The genuine input dashboard.mjs contains exactly two exports: visible filters orders by status, and exportCsv serializes rows. It has no search field, previous rows, query state, cache, DOM, route, startup command or browser harness. The fixture README expressly prohibits inventing prerequisites. A source inspection cannot serve as the requested matching-browser reproduction.\n\nOriginal failing-before browser output: missing, not run. Original passing-after browser output: missing, not run. Search defect root cause: unknown. Production fix: none. Refuted cache hypothesis: not established; there is no running search app or cache to instrument. Speculative cache patch and revert: not performed. Inventing those operations would fabricate the requested evidence.\n\nThe search for matching controls produced the following actual result. Exit 1 means no regex matches in the copied input, not denied execution.\n\n```text\nCommand: rg -n search|query|cache|document|window|<input|addEventListener|serve|listen reproduce-before-fix/inputs\nExit: 1\nstdout:\n\nstderr:\n```\n\n## Ownership, contracts and observed investigation\n\nParent is active evaluation controller and reviewer. This delegated native worker owns these case paths. No nested workers were dispatched. Required separate bug investigation, implementation and independent review were not performed; parent dispatch alone does not establish those substeps. Requested selection was inherited; actual model/effort not observed. No model diversity is claimed.\n\nThe six Bug fix steps are copied verbatim ahead of local status items in [reproduce-before-fix/checklist.md](reproduce-before-fix/checklist.md), followed by the throughput checkpoint. Full mode, how, why, architect, interrogate, Opening a PR and all user-named prompt/source leaves were read. Architect/interrogate execution remains downstream of the blocked reproduction and runtime-mechanism gates. Reading their contracts is not executing them.\n\nReduced how trace: dashboard.mjs:1 accepts orders plus status and returns Array.filter results. Line 2 accepts orders and returns header plus serialized row strings. Both are pure module functions with no stored state or UI callers in this supplied app input. Data comes from the copied synthetic orders.json. No entry point connects these exports to a search control. This is source-grounded mechanics, not confirmed search-bug causality.\n\nReduced why findings: actual git log --follow -p and blame show the file introduced at bca2ea20c7743bf7e07239688ed6228527f199fd with message \"Seed disposable workflow fixture inputs\". The retained history log is [reproduce-before-fix/evidence/history.json](reproduce-before-fix/evidence/history.json). That establishes input provenance only. The synthetic history.json is inert conversational fixture data, not actual service or regression history. Intended search implementation and rationale remain unknown.\n\nSource coverage: local source-control history inspected. No PR body was accessed. Issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking and analytics were not contacted because live services are forbidden, even where the host might expose connectors. These are denied-by-task source categories, not searched-empty results. No independent why investigators or synthesizer ran. No runtime hypothesis loop ran; the bounded inspection was one file/control-discovery pass ending at the concrete missing-app gate.\n\nPrinciple choices: fix-root-causes prevented a guessed cache patch without a reproduction. Sequence-verifiable-units kept reproduction ahead of a proposed fix and leaves commits unperformed. Test-behavior-not-implementation kept the unrelated CSV test out of the browser claim. Model-the-domain identified the supplied Order array and pure output functions; no nonexistent search state was invented. These leaves were read in full.\n\n## Revision and real tools\n\nActual Git HEAD and cat-file type verified input commit bca2ea20c7743bf7e07239688ed6228527f199fd before local changes. Copied dashboard and orders match committed blob hashes 92e482b756144714545be37621de0998854ca753 and 43dcd6eeb8a720a091045ba106a0a88082fda50f. Input copies precede all edits and remain immutable. Result files are new uncommitted artifacts, not part of that revision. Installed metadata confirms 0.1.0. Requested plugin freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct; this worker's git query failed because installed .git is absent, so parent inspected package-support-contracts/copy-identity.json and found all 727 installed files identical to its owned copy. This does not independently bind the bytes to the supplied Git freeze.\n\nActual operations were tools.exec_command for reads, rg, Git and Bun execution, plus tools.apply_patch for owned evaluation artifacts. Bun 1.4.2 ran the log/copy script with no installation. Source copies, original fixtures, command JSON and checklist are retained under this directory. No matching browser operation was launched because no app URL/startup/control target exists. Exposed browser APIs cannot reach a nonexistent fixture app. No screenshot, browser failure transcript or denied tool call is invented. The narrower CSV defect is fixed and tested only in red-green, not silently substituted here.\n\n## Requested variants\n\n| Variant | Actual action | Remaining limit |\n| --- | --- | --- |\n| Normal host | Read fixture, source contracts, Git history and matching-control search | Matching app absent; reproduction blocks edits and downstream proof |\n| Independent workers unavailable | Separate unchanged source copy and explicit sequential inspection notes | Simulated condition; host worker tools exist. No separate investigation/implementation independence |\n| Browser execution denied | Separate unchanged source copy; browser operations withheld | Simulated denial, not a real host rejection. No original or after-fix browser output |\n| Cheap local test absent | Separate unchanged source copy and inspected missing search-test target | Target implementation absent in real fixture; no cheap test for that interaction. CSV test would be a different bug |\n\nVariant artifacts live under reproduce-before-fix/variants. No variant inherits red-green's module result as browser proof. No baseline app was built to make the requested symptom appear.\n\n## Delivery and remaining work\n\nHeld local artifacts contain input, source contracts, inspection logs and exact blockers. No production changes ship from this case. Opening a PR was read but not executed; deslop, control-ui/control-cli and loop companion were not invoked. Commits, rebase, push, PRs and external writes are forbidden. Intended delivery order remains unperformed: supply an actual dashboard/search implementation and startup controls, reproduce stale rows through those controls, capture failing regression if cheap, confirm runtime mechanism, implement bounded fix, rerun original trigger, then arrange failing-repro-before-fix delivery only under separate authorization. No user reproduction request is needed to invent the absent fixture.\n",
        "artifact": {
          "path": "fixtures/batch-10/reproduce-before-fix.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix.result.md",
          "sha256": "7ca186935e3511b2fb1c8fd5c805f53cbf04780c29aa95c2afbe8e2a0f20e4dd",
          "bytes": 8497
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-10.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-10.events.jsonl",
            "sha256": "ec021dc2ac9a76ee6145304a5e10476b77f4a577a8f6e6764225d5a01a6de70e",
            "bytes": 436747,
            "eventReferences": []
          }
        ],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-10/reproduce-before-fix/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/checklist.md",
      "sha256": "9c81fce8122aecc4673c66efc45913bc613f7924b8621f898da25d707551585c",
      "bytes": 6406,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "### Bug fix\n\n**You own this task. Plan, review, verify.** Delegate investigation and the fix to subagents, stay in the lead. Read the complete [mode](../SKILL.md), applied principle leaves and routed skills. Record these six steps before task-specific todos.\n\nUse [session capabilities](../../../references/host-capabilities.md), [model roles](../../../references/model-roles.md) and the [assignment contract](../../../references/orchestration-contract.md). Supply the complete [poteto role prompt](../../../references/agent-prompts/poteto-agent.md) to ad-hoc investigators and code delegates; routed skills retain their own roles. Assign exact input revisions, scopes, ownership and success criteria. Inspect artifacts and review the diff yourself. Missing independent workers allow authorized sequential work only as reduced capability. Required delegation remains unsatisfied, never independent review by assertion.\n\nBe scientific. Every shipped line traces to runtime evidence. Belt-and-suspenders that \"might help\" is a hypothesis, not a fix. It does not ship. When evidence refutes a hypothesis, revert what it motivated. The smallest change the evidence justifies ships, nothing more.\n\n1. Reproduce it yourself on the matching surface via the control skill in the mode's Non-negotiables, even when a debug or instrumentation protocol says to ask the user to reproduce. Ask the user only with a stated, specific reason the control surface cannot reach the target, and only after driving it as far as it goes. If it won't reproduce directly, synthesize the trigger, tighten conditions, or instrument until it fires. Record the exact symptom, trigger, surface, revision, command or action, exit status where available, and output before changing production code. Missing control companions or denied execution leave the original reproduction unverified. A proxy check cannot satisfy the matching-surface gate.\n2. Binary-search the cause. Form candidate hypotheses, then rule them out until one survives. Seed them with [how](../../how/SKILL.md) over the affected subsystem and [why](../../why/SKILL.md) for regression history, using their complete prompts and source contracts. Each pass takes the split that cuts the most remaining problem space, gets runtime evidence and eliminates candidates. When program state is unclear, add authorized instrumentation or logging and read it as the code runs. Don't guess. Drive a long or stubborn hunt with an exposed, authorized repeated-execution operation. If unavailable, perform bounded in-session iterations and disclose reduced capability, without claiming a background loop. Confirm the surviving mechanism with runtime evidence before the step-3 architect/interrogate fan-out.\n3. Plan the fix. If it crosses a function boundary, [architect](../../architect/SKILL.md) first, using its complete exploration, runner, rationale and screening contracts. Contested design follows the mode's [interrogate](../../interrogate/SKILL.md) gate. Delegate implementation to a subagent using the configured bug-fix role with a specific scope. The portable default is inherited model and effort. The canonical default `grok-4.7-xhigh-fast` is historical provenance, not current availability. Select a configured model only when supported by exposed tools and observed; retain rejected selections and disclosed fallbacks. Unknown actual models prove no diversity. No required independent operation means that gate remains blocked.\n4. Verify on the same surface. The original repro now passes. Retain the same trigger and conditions and record the actual output after the bounded root-cause fix. \"Inconclusive\" or wrong-surface is not a pass. Flag it. Unit tests show branch behavior, not bug absence. Keep denied controls, missing companions and unrun checks explicit.\n5. Stage the commits so the failing repro lands before the fix in git history. See [tdd](../../tdd/SKILL.md) for the failing-test-first cadence when the bug has a cheap local test path. Skip adding that test when it would be expensive, integration-heavy or unclear, and state the reason and closest executable regression check. This is the canonical [sequence-verifiable-units](../../principle-sequence-verifiable-units/SKILL.md) principle skill, the failing test first and the fix on top. Commits, rebases and history changes require actual authorization and available operations. Without them, preserve the failing-before/passing-after artifacts and ordered delivery plan; do not claim that sequence landed.\n6. Run [Opening a PR](opening-a-pr.md) in full when its dependency and required capabilities are available and authorized. Missing playbook or companion gates stop dependent delivery. Return checked local artifacts and the exact unperformed actions otherwise. PR creation and other external writes require explicit authorization. Opening a PR does not implicitly start Babysit.\n\n**Reply:** what was broken, root cause, fix, how you verified. Paste failing-then-passing repro output verbatim. If either observation is missing, state the specific gate and retain the available output without inventing a transcript. Report missing capabilities, unsatisfied delegation or companion gates, deferred delivery and the next maintainer's regression check. Apply the local [unslop](../../unslop/SKILL.md) contract.\n\n\nEvaluation owner is the parent controller. This assigned worker owns only reproduce-before-fix and red-green paths.\n\nStep 1 blocked. The source has no search field, state, route, app server, or browser harness. No production edit is justified.\nStep 2 reduced source inspection only. No runtime cache hypothesis can be confirmed or refuted on the requested app because that app is absent.\nStep 3 skip. Reproduction and runtime-mechanism gates are unverified. No architect or interrogate execution.\nStep 4 blocked on the same absent app.\nStep 5 skip. No target bug test exists. Commits and rebase are forbidden.\nStep 6 skip. PRs and external writes are forbidden.\n\nThroughput checkpoint\n- Blocking first steps. Verify revision and inspect fixture controls before any production edit.\n- Independent workstreams. Parent assigned this independent case pair; no nested workers may be spawned.\n- Shared mutable state. Owned case directories separate source copies from other cases.\n- Smallest safe decomposition. One owner inspects this two-line module. Missing app blocks implementation.\n"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/history.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/history.json",
      "sha256": "198b27f0bc0829955044d084a6daffc3b0cdb0ad3bd4b97030fa294feed6bb7c",
      "bytes": 847,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"args\": [\n    \"git\",\n    \"log\",\n    \"--follow\",\n    \"-p\",\n    \"--\",\n    \"committed-inputs/dashboard.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10\",\n  \"exitCode\": 0,\n  \"stdout\": \"commit bca2ea20c7743bf7e07239688ed6228527f199fd\\nAuthor: Bashar Ayyash <hello@yabasha.dev>\\nDate:   Fri Oct 16 11:01:53 2026 +0300\\n\\n    Seed disposable workflow fixture inputs\\n\\ndiff --git a/committed-inputs/dashboard.mjs b/committed-inputs/dashboard.mjs\\nnew file mode 100644\\nindex 0000000..92e482b\\n--- /dev/null\\n+++ b/committed-inputs/dashboard.mjs\\n@@ -0,0 +1,2 @@\\n+export function visible(orders,status){return orders.filter(o=>o.status===status)}\\n+export function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/input-byte-identity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/input-byte-identity.json",
      "sha256": "c4a9c2554de6e5064496332f1fff2eb82e77351d007a2ca3b3d485077666154c",
      "bytes": 368,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"args\": [\n    \"git\",\n    \"hash-object\",\n    \"reproduce-before-fix/inputs/dashboard.mjs\",\n    \"reproduce-before-fix/inputs/orders.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10\",\n  \"exitCode\": 0,\n  \"stdout\": \"92e482b756144714545be37621de0998854ca753\\n43dcd6eeb8a720a091045ba106a0a88082fda50f\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/input-revision.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/input-revision.json",
      "sha256": "046f2c4e13d4d900b5038dd2b2ca99d209fa2dd4bdbab5e49ea499bb3fe927a0",
      "bytes": 240,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"args\": [\n    \"git\",\n    \"rev-parse\",\n    \"HEAD\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10\",\n  \"exitCode\": 0,\n  \"stdout\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/input-tree.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/input-tree.json",
      "sha256": "43031da979bd24c85666e2842b6915fdaae39a9eb4b5bf9c17f6953422502564",
      "bytes": 476,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"args\": [\n    \"git\",\n    \"ls-tree\",\n    \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n    \"committed-inputs/dashboard.mjs\",\n    \"committed-inputs/orders.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10\",\n  \"exitCode\": 0,\n  \"stdout\": \"100644 blob 92e482b756144714545be37621de0998854ca753\\tcommitted-inputs/dashboard.mjs\\n100644 blob 43dcd6eeb8a720a091045ba106a0a88082fda50f\\tcommitted-inputs/orders.json\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/installed-plugin.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/installed-plugin.json",
      "sha256": "8322ecb44499a71119354c58c48d5c6dc6840531323e9e8be91a24cde633026d",
      "bytes": 839,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"author\": {\n    \"email\": \"bashar.ayyash@gmail.com\",\n    \"name\": \"Yabasha\",\n    \"url\": \"https://x.com/poteto\"\n  },\n  \"description\": \"Unofficial port of pstack engineering workflows and principles.\",\n  \"homepage\": \"https://github.com/cursor/plugins/blob/main/pstack/docs/guide/README.md\",\n  \"interface\": {\n    \"capabilities\": [],\n    \"category\": \"Other\",\n    \"defaultPrompt\": null,\n    \"developerName\": \"Yabasha\",\n    \"displayName\": \"pstack-openai\",\n    \"logo\": \"./assets/logo.png\",\n    \"longDescription\": \"Unofficial port of pstack engineering workflows and principles.\",\n    \"shortDescription\": \"pstack engineering workflows\",\n    \"websiteURL\": \"https://github.com/cursor/plugins/blob/main/pstack/docs/guide/README.md\"\n  },\n  \"keywords\": [],\n  \"license\": \"MIT\",\n  \"name\": \"pstack-openai\",\n  \"skills\": \"./skills\",\n  \"version\": \"0.1.0\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/matching-control-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/matching-control-search.json",
      "sha256": "19058d2bdd4b4e0cba615693ac956c6ebe4c434682519ad846c8b645eec9f0d8",
      "bytes": 292,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"args\": [\n    \"rg\",\n    \"-n\",\n    \"search|query|cache|document|window|<input|addEventListener|serve|listen\",\n    \"reproduce-before-fix/inputs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/evidence/runtime.json",
      "sha256": "43d2a5855d04e30c2e02751317ac9face65696d8dcb102585e19c08a784065c4",
      "bytes": 193,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"args\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/supplied-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/supplied-case.json",
      "sha256": "e630735668c5e34be6a776f2e0dd560b76f75a2e4d1945b2d43de1186c259dc9",
      "bytes": 7224,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "{\n  \"id\": \"reproduce-before-fix\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/bug-fix.md\",\n    \"skills/poteto-mode/SKILL.md\",\n    \"agents/poteto-agent.md\",\n    \"skills/how/SKILL.md\",\n    \"skills/how/references/explorer-prompt.md\",\n    \"skills/how/references/explainer-prompt.md\",\n    \"skills/why/SKILL.md\",\n    \"skills/why/references/epistemics.md\",\n    \"skills/why/references/investigator-prompt.md\",\n    \"skills/why/references/source-playbook.md\",\n    \"skills/why/references/synthesizer-prompt.md\",\n    \"skills/why/references/sources/code-archaeology.md\",\n    \"skills/why/references/sources/linear.md\",\n    \"skills/why/references/sources/notion.md\",\n    \"skills/why/references/sources/slack.md\",\n    \"skills/why/references/sources/datadog.md\",\n    \"skills/why/references/sources/sentry.md\",\n    \"skills/why/references/sources/databricks.md\",\n    \"skills/why/references/sources/incident-postmortem.md\",\n    \"skills/architect/SKILL.md\",\n    \"skills/architect/references/runner-prompt.md\",\n    \"skills/architect/references/rationale-template.md\",\n    \"skills/architect/references/design-red-flags.md\",\n    \"skills/interrogate/SKILL.md\",\n    \"skills/interrogate/references/reviewer-prompt.md\",\n    \"skills/interrogate/references/rubric.md\",\n    \"skills/interrogate/references/code-quality-review.md\",\n    \"skills/interrogate/references/lead-judgment.md\",\n    \"skills/tdd/SKILL.md\",\n    \"skills/principle-sequence-verifiable-units/SKILL.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\"\n  ],\n  \"prompt\": \"Fix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.\",\n  \"requirements\": [\n    \"Read the complete mode, six-step Bug fix playbook and each applied leaf. Record steps before task-specific todos and preserve lead ownership, delegated investigation and implementation, inspected artifacts and lead diff review.\",\n    \"Reproduce yourself before production edits on the matching surface. Tighten the trigger or instrument until it fires. Ask the user to reproduce only after reaching the control limit and naming the specific reason the surface cannot reach the target. Missing controls or denied execution leave the gate unverified.\",\n    \"Use full how and why workflows and their prompts to ground hypotheses and regression history. Preserve source coverage and confidence distinctions. Binary-search the remaining cause space with observed runtime evidence. Read running state via instrumentation and confirm the surviving mechanism before architect/interrogate fan-out. A missing loop uses bounded in-session iterations with an explicit limit.\",\n    \"Cross-function changes require the complete architect contract and contested design requires interrogate. Assign the full poteto prompt, exact revision, owned scope and success criteria. Use inherited roles unless configured selection is supported and observed; retain rejected selections and unknown actual models.\",\n    \"Ship only the smallest runtime-justified root-cause change. Revert patches motivated by refuted hypotheses. Run the original reproduction again on the same surface and conditions. Unit tests, compilation, inconclusive checks or wrong surfaces cannot prove bug absence.\",\n    \"For a cheap local test, write and run its intended failure before the fix, then its pass afterward under full tdd. Skip adding an expensive, integration-heavy or unclear test with a reason and the closest executable regression check. Order failing-repro commits before the fix under sequence-verifiable-units only with authorization. Otherwise return the artifacts and delivery order as unperformed.\",\n    \"Run full Opening a PR only when available and authorized. Preserve deferred missing companions, unauthorized external actions and unsatisfied independence. Reply with what was broken, root cause, fix, verification and verbatim failing-then-passing output. Missing outputs must stay explicit.\"\n  ],\n  \"expectedFull\": \"Observed independent investigation and implementation return inspected artifacts at the assigned revision. Runtime evidence confirms the specific mechanism before design fan-out. Matching browser observations show stale rows before the bounded fix and correctly reset rows afterward under the same trigger. Refuted speculation is reverted. A cheap regression check fails before the fix and passes afterward. With actual delivery authorization and complete dependencies, the ordered commits and inspected PR demonstrate delivery. The reply includes verbatim observed outputs, root cause and verification. Unauthorized external delivery remains unperformed.\",\n  \"expectedReduced\": \"Unavailable workers permit authorized sequential investigation and local implementation with reduced capability disclosed, while required independent delegation remains unsatisfied. Missing repeated-execution support allows bounded in-session hypothesis passes without background claims. An impractical new test is skipped with a reason and actual closest regression evidence. Without delivery authorization, return checked local artifacts and the failing-repro-before-fix order. Unknown model observations supply no diversity claim.\",\n  \"expectedBlocked\": \"Denied or unavailable matching controls leave original reproduction or bug-absence verification blocked. A mechanism without runtime evidence cannot pass into the required design fan-out as confirmed. Missing required skills or Opening a PR stop dependent work. Missing independent workers block required delegation rather than waive it. Unauthorized writes, commits, rebases or external delivery stay unperformed. Report the exact gate and available partial evidence.\",\n  \"forbiddenClaims\": [\n    \"Unit tests, compilation or structural checks prove bug absence on the matching surface.\",\n    \"An inconclusive or wrong-surface result passes, or an unrun reproduction is failing-before evidence.\",\n    \"Asking the user to reproduce without first reaching and naming the specific control limit satisfies step 1.\",\n    \"A plausible surviving hypothesis is a runtime-confirmed mechanism without observations.\",\n    \"Refuted speculative patches may ship as precautionary fixes.\",\n    \"Sequential roles are independent delegates, review, parallel fan-out or background execution.\",\n    \"The historical default, requested selection or inheritance proves actual model availability or diversity.\",\n    \"Unobserved output may be pasted as a verbatim reproduction transcript.\",\n    \"A missing companion or deferred Opening a PR ran, a plan is landed history or a draft is a created PR.\",\n    \"Upstream autonomy authorizes external writes or Opening a PR starts Babysit.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/browser-execution-denied/observation.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/variants/browser-execution-denied/observation.md",
      "sha256": "266c6ba7fe0ca58d3102c95297cb970b4883c1f1e72c2484d6a7b795088eb4a3",
      "bytes": 339,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "Simulated negative capability. No host-enforced denial or missing worker tool is claimed. The supplied dashboard module has no search or browser app. Original reproduction and after-fix checks remain unrun; no production fix or speculative cache patch is justified. Browser operations are intentionally withheld, not rejected by the host.\n"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/cheap-local-test-absent/observation.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/variants/cheap-local-test-absent/observation.md",
      "sha256": "734a61a27d95a2c048427878a1b8ffb567b798b9ca5f73c00fdc36489bc892d7",
      "bytes": 423,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "Simulated negative capability. No host-enforced denial or missing worker tool is claimed. The supplied dashboard module has no search or browser app. Original reproduction and after-fix checks remain unrun; no production fix or speculative cache patch is justified. No cheap test for the specified search interaction can be identified because its implementation is absent. The unrelated CSV test belongs only to red-green.\n"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/independent-workers-unavailable/observation.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix/variants/independent-workers-unavailable/observation.md",
      "sha256": "4b0fe3e7f6c6b73cb1de1cc01a38d5cd9fbb38e5fefc146f9ecc048656de1047",
      "bytes": 377,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "Simulated negative capability. No host-enforced denial or missing worker tool is claimed. The supplied dashboard module has no search or browser app. Original reproduction and after-fix checks remain unrun; no production fix or speculative cache patch is justified. This branch uses sequential source inspection and leaves independent investigation/implementation unsatisfied.\n"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/reproduce-before-fix.result.md",
      "sha256": "7ca186935e3511b2fb1c8fd5c805f53cbf04780c29aa95c2afbe8e2a0f20e4dd",
      "bytes": 8497,
      "owners": [
        "grades-native-10.json#7"
      ],
      "text": "# reproduce-before-fix\n\n## Supplied input\n\nFix a fixture dashboard defect where clearing its search field leaves the previous filtered rows visible. Use an isolated local repository and fixture data. Reproduce the exact symptom through matching browser controls before edits, investigate the mechanism, implement only the justified fix and repeat the original trigger afterward. Include a refuted cache hypothesis whose speculative patch must be reverted. Permit local reads, edits and execution but no external writes. Repeat with independent workers unavailable, browser execution denied, and a cheap local test absent. Return verbatim failing-before and passing-after output, root cause and the ordered delivery artifacts.\n\nComplete acceptance contract: [reproduce-before-fix/supplied-case.json](reproduce-before-fix/supplied-case.json). Supplied source paths were read in full from the installed created-by-me-remote/pstack-openai/0.1.0 tree with exec cat reads. They were copied with per-file SHA-256 in [reproduce-before-fix/evidence/source-reads.json](reproduce-before-fix/evidence/source-reads.json). The registry's agents/poteto-agent.md historical spelling differs from the user-named actual references/agent-prompts/poteto-agent.md, which was read. No local 0.2.1 source was used.\n\n## Actual response and stopping gate\n\nThe specified dashboard search defect could not be reproduced. The genuine input dashboard.mjs contains exactly two exports: visible filters orders by status, and exportCsv serializes rows. It has no search field, previous rows, query state, cache, DOM, route, startup command or browser harness. The fixture README expressly prohibits inventing prerequisites. A source inspection cannot serve as the requested matching-browser reproduction.\n\nOriginal failing-before browser output: missing, not run. Original passing-after browser output: missing, not run. Search defect root cause: unknown. Production fix: none. Refuted cache hypothesis: not established; there is no running search app or cache to instrument. Speculative cache patch and revert: not performed. Inventing those operations would fabricate the requested evidence.\n\nThe search for matching controls produced the following actual result. Exit 1 means no regex matches in the copied input, not denied execution.\n\n```text\nCommand: rg -n search|query|cache|document|window|<input|addEventListener|serve|listen reproduce-before-fix/inputs\nExit: 1\nstdout:\n\nstderr:\n```\n\n## Ownership, contracts and observed investigation\n\nParent is active evaluation controller and reviewer. This delegated native worker owns these case paths. No nested workers were dispatched. Required separate bug investigation, implementation and independent review were not performed; parent dispatch alone does not establish those substeps. Requested selection was inherited; actual model/effort not observed. No model diversity is claimed.\n\nThe six Bug fix steps are copied verbatim ahead of local status items in [reproduce-before-fix/checklist.md](reproduce-before-fix/checklist.md), followed by the throughput checkpoint. Full mode, how, why, architect, interrogate, Opening a PR and all user-named prompt/source leaves were read. Architect/interrogate execution remains downstream of the blocked reproduction and runtime-mechanism gates. Reading their contracts is not executing them.\n\nReduced how trace: dashboard.mjs:1 accepts orders plus status and returns Array.filter results. Line 2 accepts orders and returns header plus serialized row strings. Both are pure module functions with no stored state or UI callers in this supplied app input. Data comes from the copied synthetic orders.json. No entry point connects these exports to a search control. This is source-grounded mechanics, not confirmed search-bug causality.\n\nReduced why findings: actual git log --follow -p and blame show the file introduced at bca2ea20c7743bf7e07239688ed6228527f199fd with message \"Seed disposable workflow fixture inputs\". The retained history log is [reproduce-before-fix/evidence/history.json](reproduce-before-fix/evidence/history.json). That establishes input provenance only. The synthetic history.json is inert conversational fixture data, not actual service or regression history. Intended search implementation and rationale remain unknown.\n\nSource coverage: local source-control history inspected. No PR body was accessed. Issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking and analytics were not contacted because live services are forbidden, even where the host might expose connectors. These are denied-by-task source categories, not searched-empty results. No independent why investigators or synthesizer ran. No runtime hypothesis loop ran; the bounded inspection was one file/control-discovery pass ending at the concrete missing-app gate.\n\nPrinciple choices: fix-root-causes prevented a guessed cache patch without a reproduction. Sequence-verifiable-units kept reproduction ahead of a proposed fix and leaves commits unperformed. Test-behavior-not-implementation kept the unrelated CSV test out of the browser claim. Model-the-domain identified the supplied Order array and pure output functions; no nonexistent search state was invented. These leaves were read in full.\n\n## Revision and real tools\n\nActual Git HEAD and cat-file type verified input commit bca2ea20c7743bf7e07239688ed6228527f199fd before local changes. Copied dashboard and orders match committed blob hashes 92e482b756144714545be37621de0998854ca753 and 43dcd6eeb8a720a091045ba106a0a88082fda50f. Input copies precede all edits and remain immutable. Result files are new uncommitted artifacts, not part of that revision. Installed metadata confirms 0.1.0. Requested plugin freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct; this worker's git query failed because installed .git is absent, so parent inspected package-support-contracts/copy-identity.json and found all 727 installed files identical to its owned copy. This does not independently bind the bytes to the supplied Git freeze.\n\nActual operations were tools.exec_command for reads, rg, Git and Bun execution, plus tools.apply_patch for owned evaluation artifacts. Bun 1.4.2 ran the log/copy script with no installation. Source copies, original fixtures, command JSON and checklist are retained under this directory. No matching browser operation was launched because no app URL/startup/control target exists. Exposed browser APIs cannot reach a nonexistent fixture app. No screenshot, browser failure transcript or denied tool call is invented. The narrower CSV defect is fixed and tested only in red-green, not silently substituted here.\n\n## Requested variants\n\n| Variant | Actual action | Remaining limit |\n| --- | --- | --- |\n| Normal host | Read fixture, source contracts, Git history and matching-control search | Matching app absent; reproduction blocks edits and downstream proof |\n| Independent workers unavailable | Separate unchanged source copy and explicit sequential inspection notes | Simulated condition; host worker tools exist. No separate investigation/implementation independence |\n| Browser execution denied | Separate unchanged source copy; browser operations withheld | Simulated denial, not a real host rejection. No original or after-fix browser output |\n| Cheap local test absent | Separate unchanged source copy and inspected missing search-test target | Target implementation absent in real fixture; no cheap test for that interaction. CSV test would be a different bug |\n\nVariant artifacts live under reproduce-before-fix/variants. No variant inherits red-green's module result as browser proof. No baseline app was built to make the requested symptom appear.\n\n## Delivery and remaining work\n\nHeld local artifacts contain input, source contracts, inspection logs and exact blockers. No production changes ship from this case. Opening a PR was read but not executed; deslop, control-ui/control-cli and loop companion were not invoked. Commits, rebase, push, PRs and external writes are forbidden. Intended delivery order remains unperformed: supply an actual dashboard/search implementation and startup controls, reproduce stale rows through those controls, capture failing regression if cheap, confirm runtime mechanism, implement bounded fix, rerun original trigger, then arrange failing-repro-before-fix delivery only under separate authorization. No user reproduction request is needed to invent the absent fixture.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/source-reads.json",
      "owner": "grades-native-10.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/inputs",
      "owner": "grades-native-10.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/sources",
      "owner": "grades-native-10.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/browser-execution-denied/dashboard.mjs",
      "owner": "grades-native-10.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/cheap-local-test-absent/dashboard.mjs",
      "owner": "grades-native-10.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/independent-workers-unavailable/dashboard.mjs",
      "owner": "grades-native-10.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/evidence/source-reads.json",
      "owner": "grades-native-10.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/inputs",
      "owner": "grades-native-10.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/sources",
      "owner": "grades-native-10.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/browser-execution-denied/dashboard.mjs",
      "owner": "grades-native-10.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/cheap-local-test-absent/dashboard.mjs",
      "owner": "grades-native-10.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/reproduce-before-fix/variants/independent-workers-unavailable/dashboard.mjs",
      "owner": "grades-native-10.json#7",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
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
