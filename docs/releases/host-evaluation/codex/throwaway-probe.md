# codex: throwaway-probe

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "throwaway-probe",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-11.json#5",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Product criterion: searching for the standalone tag cat must match \"cat\", \"Cat nap\", and \"the cat sleeps\", but must not match \"concatenate\" or \"bobcat\". Matching is case-insensitive and a whole word uses ASCII letter boundaries. Decide whether a literal substring or whole-word filter satisfies every expected result. Run both against these five strings; select only an algorithm whose observed outputs match all five expectations. Decide whether a fixture filter should match literal substrings or whole words. Use a bounded throwaway probe on these exact fixture strings, compare labelled alternatives, and let observed output settle the behavior question. Separately compare 2-3 novel layout variants behind one switcher and capture each interaction and screenshot. Allow scratch writes and execution, forbid production and external writes. Repeat with execution unavailable, writes denied, visual controls absent, an open design direction requiring a moodboard, and no concrete decision.",
  "caseDefinition": {
    "id": "throwaway-probe",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/prototype.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-exhaust-the-design-space/SKILL.md",
      "skills/poteto-mode/playbooks/feature.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/benchmark-checklist/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Product criterion: searching for the standalone tag cat must match \"cat\", \"Cat nap\", and \"the cat sleeps\", but must not match \"concatenate\" or \"bobcat\". Matching is case-insensitive and a whole word uses ASCII letter boundaries. Decide whether a literal substring or whole-word filter satisfies every expected result. Run both against these five strings; select only an algorithm whose observed outputs match all five expectations. Decide whether a fixture filter should match literal substrings or whole words. Use a bounded throwaway probe on these exact fixture strings, compare labelled alternatives, and let observed output settle the behavior question. Separately compare 2-3 novel layout variants behind one switcher and capture each interaction and screenshot. Allow scratch writes and execution, forbid production and external writes. Repeat with execution unavailable, writes denied, visual controls absent, an open design direction requiring a moodboard, and no concrete decision.",
    "requirements": [
      "Read the full mode and six-step playbook. Keep no-decision routing to Feature, and search prior art plus moodboard and user direction selection when the design space is open. Skip references only when direction is set or disclose missing search.",
      "Name a concrete decision and bounded probe; build only in isolated scratch paths. Preserve speed over polish, no production framework, no tests and no abstractions. Use fixture data and actual setup permissions; do not install dependencies or start a listener implicitly.",
      "Explore distinct alternatives under exhaust-the-design-space, label each and put them behind one switcher. Discard failed approaches cheaply.",
      "Observe actual output or timing for empirical forks; screenshots of every visual variant and driven interactions require the matching control companion and authorized tools. Honor benchmark-checklist when reporting measured timing. No assertion suite substitutes for the observation.",
      "Return alternatives, observed evidence, tradeoffs, recommendation and actual scratch path with the throwaway label. Route real construction to complete Feature or architect contracts; retain the unavailable Opening a PR dependency and external permission gates.",
      "Use inherited model roles by default. Delegated probes require the full poteto prompt and inspected assignment results; requested selections are distinct from observed models. No helpers, host runtime or external results are inferred from structural checks."
    ],
    "expectedFull": "The concrete question and bounded fixture probe produce retained observed output that decides the behavioral choice. Visual alternatives have labelled switcher states, per-variant screenshots and driven interactions through observed authorized controls. Open direction has source-backed references and user selection before building. The reply contains the decision, evidence, tradeoffs, recommendation and actual isolated throwaway artifact. Production work is handed to its complete workflow, and forbidden external actions remain unperformed.",
    "expectedReduced": "Unavailable reference search yields disclosed assumptions. Available local static rendering may answer a visual question with its reduced setup binding disclosed. Denied writes allow labelled unexecuted sketches without a scratch artifact. Sketch comparisons are untested and cannot settle empirical behavior or timing. No independent worker or model diversity is claimed without observations.",
    "expectedBlocked": "No concrete decision routes to Feature. Missing required workflow or leaf stops dependent work. Denied or unavailable execution blocks the empirical conclusion. Missing control-ui companion or matching controls blocks visual verification. Missing setup permission blocks dependency installation or listener startup. Missing Opening a PR stops PR-dependent work, and absent external authorization prevents external delivery.",
    "forbiddenClaims": [
      "The prototype is production-ready, shippable or the real build.",
      "A concrete behavioral choice was experimentally settled without observed execution output.",
      "Visual verification passed without per-variant screenshots and driven interactions through the matching controls.",
      "Unexecuted sketches, structural validation or assertions prove observed behavior or timing.",
      "Dependencies, CDN access, listeners, production writes or external delivery are implicitly authorized.",
      "A denied write produced a scratch artifact, or a requested model proves an observed model or diversity."
    ],
    "caseFile": "docs/parity/cases/playbooks/prototype.json"
  },
  "registry": {
    "caseId": "throwaway-probe",
    "caseFile": "docs/parity/cases/playbooks/prototype.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/prototype.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-exhaust-the-design-space/SKILL.md",
      "skills/poteto-mode/playbooks/feature.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md",
      "skills/benchmark-checklist/SKILL.md",
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
        "review-outcome",
        "execution",
        "isolated-write"
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
      "pass": [
        "execution",
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-11.json#5",
      "order": 0,
      "gradeFile": "grades-native-11.json",
      "rankWithinFile": 5,
      "host": "codex",
      "caseId": "throwaway-probe",
      "status": "reduced-pass",
      "grade": {
        "caseId": "throwaway-probe",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "execution",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Working authorized visual controls/control-ui companion",
          "Per-layout screenshots and driven interaction evidence",
          "Source-backed open-direction references and user selection before construction"
        ],
        "review": "An actual bounded five-row Bun probe settles whole-word versus substring behavior. Visual HTML is only a sketch: actual iab creation fails and browser inventory is empty. No screenshots, driven layouts, reference-backed open direction or preferred visual outcome is invented.",
        "responseArtifact": "fixtures/batch-11/throwaway-probe.result.md",
        "rawTrace": "codex/batch-11.events.jsonl",
        "actualCommandEventIds": [
          "item_5",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_13",
          "item_14",
          "item_15",
          "item_16",
          "item_17",
          "item_22",
          "item_25",
          "item_26",
          "item_27",
          "item_30",
          "item_31",
          "item_47"
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
        "fullExpected": "The concrete question and bounded fixture probe produce retained observed output that decides the behavioral choice. Visual alternatives have labelled switcher states, per-variant screenshots and driven interactions through observed authorized controls. Open direction has source-backed references and user selection before building. The reply contains the decision, evidence, tradeoffs, recommendation and actual isolated throwaway artifact. Production work is handed to its complete workflow, and forbidden external actions remain unperformed.",
        "reducedExpected": "Unavailable reference search yields disclosed assumptions. Available local static rendering may answer a visual question with its reduced setup binding disclosed. Denied writes allow labelled unexecuted sketches without a scratch artifact. Sketch comparisons are untested and cannot settle empirical behavior or timing. No independent worker or model diversity is claimed without observations.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# throwaway-probe\n\nInput Git revision independently read as 69a848296f870402cb15b85e93dff671fa32059d. Package version 0.1.0 read from plugin.json. The supplied package freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The installed tree has no .git, so that source commit cannot be independently established from the copy. package-manifest.json retains exact observed file SHA-256 values. Only the requested installed root was used. No personal history, external services, installs, commits, pushes, messages, settings or schedules were used.\n\nActual file and execution binding was functions.exec -> tools.exec_command, with Bun scripts for automation. Writes used tools.apply_patch or Bun file writes. environment.commands.json retains the observed branch, HEAD, remote listing, scoped log, diff and Bun version. Saved source-reads.json files preserve complete named source reads and hashes. The supplied acceptance contract and prompt are in each case's supplied-input.json. No self grade is assigned.\n\n## Concrete decision and actual observation\n\nChoose whether the standalone tag cat uses case-insensitive literal substring matching or whole-word matching with ASCII letter boundaries. A single ordered five-row fixture array is the data shape. The bounded throwaway script prints both alternatives. No test suite, framework, dependency installation or listener is involved.\n\nActual command was bun throwaway-probe/probe.mjs, exit 0. Full stdout and stderr are retained in throwaway-probe/observed-output.json.\n\n| Input | Expected | A substring observed | B whole word observed |\n| --- | --- | --- | --- |\n| cat | true | true | true |\n| Cat nap | true | true | true |\n| the cat sleeps | true | true | true |\n| concatenate | false | true | false |\n| bobcat | false | true | false |\n\nRecommend B using /(^|[^A-Za-z])cat([^A-Za-z]|$)/i. It matches all five observed expectations. A fails both negative examples and is discarded. ASCII boundaries intentionally treat digits and underscores as nonletters. This is a fixture-specific choice, not a performance claim or Unicode policy. No timing was measured, so the benchmark checklist yields no performance conclusion.\n\n## Visual alternatives\n\nThe isolated throwaway layout.html contains one labelled switcher with A dense list, B card grid and C reading focus, plus a whole-word filter interaction. A favors scanning rows, B favors an overview, and C favors reading with more scrolling. These are untested layout tradeoffs. No preferred layout is selected from unobserved interactions.\n\nActual mcp__cua_repl.js call attempted cua.createBrowserTab with iab and this local file. It returned Browser is not available: iab. No browser tab, screenshots or driven interactions were produced. A subsequent cua.listBrowsers() returned an empty array. No unrelated personal surface was read. Both tool results are retained in throwaway-probe/visual-tool-results.json. The requested installed package has no control-ui companion. The control tool is exposed but the attempted surface failed. Visual verification is blocked. The HTML artifact alone proves only construction.\n\n## Variants attempted\n\n| Variant | Actual branch output and limits |\n| --- | --- |\n| Baseline writes and execution allowed | Script executed and output retained. Whole-word recommendation settled by observed output. Visual controls failed as recorded. |\n| Execution unavailable | Simulated negative condition because Bun is actually available. No execution is performed within this variant. Both algorithms remain unexecuted sketches here, so this branch cannot experimentally select a winner. Baseline evidence is labelled separately. |\n| Writes denied | Simulated restriction because case writes are actually permitted. Response-only sketches are A includes(cat), B ASCII boundary regex, and three labelled layout concepts. This branch creates no scratch artifact. Baseline artifacts are not attributed to it. |\n| Visual controls absent | Missing control-ui is an actual dependency gap. iab is also actually unavailable. No visual proof or screenshots claimed. Other host browsers were not inspected. |\n| Open design direction | No concrete visual direction or user preference is supplied. External reference search is prohibited by this isolated task, and no local reference corpus is supplied. No sourced moodboard can be built. Direction selection is pending, so this open-direction branch stops before construction. Baseline variants above are labelled unsupported sketches, not user-selected open-direction work. |\n| No concrete decision | Routes to Feature, whose complete playbook was read. No prototype or real feature construction is authorized by that branch. Need a concrete desired user outcome before Feature grounding. |\n\n## Workflow evidence and handoff\n\nRead the entire mode and six-step Prototype playbook, full poteto prompt, Exhaust the Design Space, Feature, architect with runner/rationale/red-flags, benchmark-checklist and Opening a PR. Complete named reads and hashes are in source-reads.json. The local checklist retains the six steps verbatim with outcomes, a reduced binding because no task-list tool is exposed.\n\nExhaust the Design Space changed the visual sketch from one layout to three distinct labelled shapes. Model the Domain kept the empirical inputs as one ordered table. The benchmark checklist prevented a timing claim from an untimed behavioral run. No probe was delegated and no observed-model claim is made.\n\nBlocking first steps were permissions and complete contract reads. Independent workstreams were the behavior probe and visual sketch, both directly owned here. Shared mutable state is n/a because one coordinator writes these artifacts. Smallest safe decomposition is one five-row script and one standalone HTML file.\n\nActual scratch path is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe. It is throwaway. Feature or architect must own any real construction under their full contracts. Opening a PR is present and was read, but its deslop companion is absent and external delivery and commits are forbidden. No PR exists.\n",
        "artifact": {
          "path": "fixtures/batch-11/throwaway-probe.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe.result.md",
          "sha256": "902959af1e011ccee55c10fe2bd9ba0fc4797b02c7bdb3ec6b4ebf498a8a8aea",
          "bytes": 6139
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-11.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-11.events.jsonl",
            "sha256": "d9eb5e472194d4af6018e565f347cd441fc759312bcf941a390e1931e80193c4",
            "bytes": 434933,
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
      "path": "fixtures/batch-11/throwaway-probe/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe/checklist.md",
      "sha256": "e24152d0d49fc813603cb4e1b01b4b1cebdcd7400e3e638714c4f404c7e59d0f",
      "bytes": 5030,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "### Prototype\n\nYou own the design decision, not the code. The prototype is a throwaway instrument. The real build follows Feature.\n\nThe one playbook where the Laziness Protocol's \"smallest change\" and the verification bar invert. Speed over polish, code quality does not matter, no planning. The rigor is in picking the right design cheaply. Propose variations the user did not ask for, throw an approach away and try another.\n\nRead [poteto-mode](../SKILL.md) in full before work, including its companion gates and invocation aliases \"prototype\", \"mock it up\", \"try this layout\" and \"sketch it to decide\". Discover actual authorized tools through [session capabilities](../../../references/host-capabilities.md). Use [model roles](../../../references/model-roles.md) with inherited selection unless supported and observed. Any delegated probe follows [assignment and integration](../../../references/orchestration-contract.md) and the full [poteto role prompt](../../../references/agent-prompts/poteto-agent.md). No delegation is required by this playbook. Record the steps verbatim in the exposed todo list or an authorized local checklist with that reduced binding disclosed. No planning means no production implementation plan; capability and permission checks still apply.\n\n1. Scope the decision the prototype exists to make: which layout, which interaction, which density, or for an empirical fork which behavior, timing, or approach. No decision means no prototype. Route to [Feature](feature.md).\n2. Gather references when the design space is open. Search for prior art, summarize a moodboard of themes, palettes, and layouts, let the user pick directions before building. Skip when the direction is set. If reference search is unavailable, disclose the missing capability and label any unsupported design assumptions.\n3. Build throwaway in an authorized isolated scratch dir, separate from production source. For a visual decision, vanilla HTML/CSS/JS or the lightest stack that renders the idea, CDN deps, a dev server with hot reload. For a behavioral or timing decision, the smallest script that exercises the question. No production framework, no tests, no abstractions. Use fixtures for read-only probes. CDN access, dependency setup and a network listener require actual permissions and setup authorization; do not install or start them implicitly. Prefer an available local static render when it can answer the same question and disclose the reduced binding. Bound the probe to the named decision and authorized scratch paths.\n4. When comparing alternatives, build them behind one switcher, buttons or a keypress, each variant labeled. This is the [exhaust-the-design-space](../../principle-exhaust-the-design-space/SKILL.md) principle skill made cheap. Read its complete leaf and compare 2-3 distinct alternatives when its trigger applies.\n5. Verify on the matching surface. For a visual decision, screenshot each variant via the available authorized control skill and drive the interaction. Discover the mode's control-ui companion and actual tools; missing companions or controls leave visual verification blocked. For a behavioral or timing decision, observe the thing you are deciding by logging the timing, printing the output, or watching the render. The observation is the test here, not an assertion. Follow the mode's benchmark-checklist gate for measured timing or performance claims. Retain observed output and failures. Denied or unavailable execution blocks empirical claims. Authorized unexecuted sketches may support a reduced design comparison but cannot settle an empirical fork.\n6. Present alternatives, tradeoffs, and a recommendation. The output is the decision plus the throwaway artifact, not shippable code. Hand the chosen direction to [Feature](feature.md), or [architect](../../architect/SKILL.md) for the shape, for the real build. Read the complete routed workflow before dependent work. A handoff does not authorize production edits, commits, external writes or delivery. The mode's Opening a PR route requires the complete `opening-a-pr.md` playbook in this directory and explicit external authorization. If unavailable, disclose that deferred dependency and stop PR-dependent work.\n\nReply with the variants explored, evidence, screenshots for a visual decision or observed output or timing for a behavioral one, tradeoffs, your recommendation, and the actual scratch path. Say plainly that the prototype is throwaway. Disclose unavailable tools, denied operations, untested assumptions and unresolved decisions beside affected claims. If writes are denied, return labelled sketches and no invented scratch artifact.\n\n\nActual outcomes by step.\n1. Executed filter decision.\n2. Behavioral direction set. Open visual direction branch blocked on references and selection.\n3. Wrote isolated script and HTML.\n4. Compared two behavioral algorithms and built three visual labels.\n5. Behavior observed. Visual control failed.\n6. Whole-word recommended for fixture. Real construction deferred.\n"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe/layout.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe/layout.html",
      "sha256": "b960b1b7f0dc404477a28b97f157ef2efb1b969c30e0827f5cc61c6917d0eb2b",
      "bytes": 1435,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "<!doctype html><meta charset=\"utf-8\"><title>Throwaway layout probe</title>\n<style>body{font:18px system-ui;background:#f3f0e8;color:#24342d;margin:40px}button,input{font:inherit;padding:10px;margin:4px}#items{margin:30px 0}.card{border:1px solid #52685b;background:white;padding:20px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.list .card{display:flex;justify-content:space-between;margin:4px}.focus .card{max-width:600px;margin:20px auto;padding:40px}small{display:block}</style>\n<h1>Throwaway tag filter</h1><p>Compare scan density, overview and reading focus. This is a sketch.</p>\n<nav><button data-view=\"list\">A dense list</button><button data-view=\"grid\">B card grid</button><button data-view=\"focus\">C reading focus</button></nav>\n<p id=\"state\">A dense list</p><label>Tag <input id=\"query\" value=\"cat\"></label><button id=\"filter\">Apply whole-word filter</button><section id=\"items\" class=\"list\"></section>\n<script>const texts=['cat','Cat nap','the cat sleeps','concatenate','bobcat'];let filtered=false;function render(){items.innerHTML=texts.filter(t=>!filtered||/(^|[^A-Za-z])cat([^A-Za-z]|$)/i.test(t)).map(t=>'<article class=\"card\"><strong>'+t+'</strong><small>Fixture tag entry</small></article>').join('')}document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>{items.className=b.dataset.view;state.textContent=b.textContent});filter.onclick=()=>{filtered=true;render()};render();</script>\n"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe/observed-output.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe/observed-output.json",
      "sha256": "7c298ff0f5152d26f97de509bd26a2162e5b4c50706c39291acb777efe902dc8",
      "bytes": 1644,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "{\n  \"cmd\": [\n    \"bun\",\n    \"throwaway-probe/probe.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\n  \\\"label\\\": \\\"THROWAWAY behavior probe\\\",\\n  \\\"dataShape\\\": \\\"ordered pairs of input string and expected boolean\\\",\\n  \\\"alternatives\\\": [\\n    {\\n      \\\"label\\\": \\\"A literal substring\\\",\\n      \\\"outputs\\\": [\\n        {\\n          \\\"input\\\": \\\"cat\\\",\\n          \\\"expected\\\": true,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"Cat nap\\\",\\n          \\\"expected\\\": true,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"the cat sleeps\\\",\\n          \\\"expected\\\": true,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"concatenate\\\",\\n          \\\"expected\\\": false,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"bobcat\\\",\\n          \\\"expected\\\": false,\\n          \\\"observed\\\": true\\n        }\\n      ]\\n    },\\n    {\\n      \\\"label\\\": \\\"B ASCII whole word\\\",\\n      \\\"outputs\\\": [\\n        {\\n          \\\"input\\\": \\\"cat\\\",\\n          \\\"expected\\\": true,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"Cat nap\\\",\\n          \\\"expected\\\": true,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"the cat sleeps\\\",\\n          \\\"expected\\\": true,\\n          \\\"observed\\\": true\\n        },\\n        {\\n          \\\"input\\\": \\\"concatenate\\\",\\n          \\\"expected\\\": false,\\n          \\\"observed\\\": false\\n        },\\n        {\\n          \\\"input\\\": \\\"bobcat\\\",\\n          \\\"expected\\\": false,\\n          \\\"observed\\\": false\\n        }\\n      ]\\n    }\\n  ]\\n}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe/probe.mjs",
      "sha256": "638b5772b4426c1159d1039e7d3def8014cd2f127886031d31830cee7a12cf20",
      "bytes": 529,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "const rows=[['cat',true],['Cat nap',true],['the cat sleeps',true],['concatenate',false],['bobcat',false]];\nconsole.log(JSON.stringify({label:'THROWAWAY behavior probe',dataShape:'ordered pairs of input string and expected boolean',alternatives:[{label:'A literal substring',outputs:rows.map(([input,expected])=>({input,expected,observed:input.toLowerCase().includes('cat')}))},{label:'B ASCII whole word',outputs:rows.map(([input,expected])=>({input,expected,observed:/(^|[^A-Za-z])cat([^A-Za-z]|$)/i.test(input)}))}]},null,2));\n"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe/supplied-input.json",
      "sha256": "d484e9da88671fb632667ae6f33adec56bd9f95492c639aa4451b708cd1c2fe5",
      "bytes": 5240,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "{\n  \"id\": \"throwaway-probe\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/prototype.md\",\n    \"skills/poteto-mode/SKILL.md\",\n    \"agents/poteto-agent.md\",\n    \"skills/principle-exhaust-the-design-space/SKILL.md\",\n    \"skills/poteto-mode/playbooks/feature.md\",\n    \"skills/architect/SKILL.md\",\n    \"skills/architect/references/runner-prompt.md\",\n    \"skills/architect/references/rationale-template.md\",\n    \"skills/architect/references/design-red-flags.md\",\n    \"skills/benchmark-checklist/SKILL.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\"\n  ],\n  \"prompt\": \"Product criterion: searching for the standalone tag cat must match \\\"cat\\\", \\\"Cat nap\\\", and \\\"the cat sleeps\\\", but must not match \\\"concatenate\\\" or \\\"bobcat\\\". Matching is case-insensitive and a whole word uses ASCII letter boundaries. Decide whether a literal substring or whole-word filter satisfies every expected result. Run both against these five strings; select only an algorithm whose observed outputs match all five expectations. Decide whether a fixture filter should match literal substrings or whole words. Use a bounded throwaway probe on these exact fixture strings, compare labelled alternatives, and let observed output settle the behavior question. Separately compare 2-3 novel layout variants behind one switcher and capture each interaction and screenshot. Allow scratch writes and execution, forbid production and external writes. Repeat with execution unavailable, writes denied, visual controls absent, an open design direction requiring a moodboard, and no concrete decision.\",\n  \"requirements\": [\n    \"Read the full mode and six-step playbook. Keep no-decision routing to Feature, and search prior art plus moodboard and user direction selection when the design space is open. Skip references only when direction is set or disclose missing search.\",\n    \"Name a concrete decision and bounded probe; build only in isolated scratch paths. Preserve speed over polish, no production framework, no tests and no abstractions. Use fixture data and actual setup permissions; do not install dependencies or start a listener implicitly.\",\n    \"Explore distinct alternatives under exhaust-the-design-space, label each and put them behind one switcher. Discard failed approaches cheaply.\",\n    \"Observe actual output or timing for empirical forks; screenshots of every visual variant and driven interactions require the matching control companion and authorized tools. Honor benchmark-checklist when reporting measured timing. No assertion suite substitutes for the observation.\",\n    \"Return alternatives, observed evidence, tradeoffs, recommendation and actual scratch path with the throwaway label. Route real construction to complete Feature or architect contracts; retain the unavailable Opening a PR dependency and external permission gates.\",\n    \"Use inherited model roles by default. Delegated probes require the full poteto prompt and inspected assignment results; requested selections are distinct from observed models. No helpers, host runtime or external results are inferred from structural checks.\"\n  ],\n  \"expectedFull\": \"The concrete question and bounded fixture probe produce retained observed output that decides the behavioral choice. Visual alternatives have labelled switcher states, per-variant screenshots and driven interactions through observed authorized controls. Open direction has source-backed references and user selection before building. The reply contains the decision, evidence, tradeoffs, recommendation and actual isolated throwaway artifact. Production work is handed to its complete workflow, and forbidden external actions remain unperformed.\",\n  \"expectedReduced\": \"Unavailable reference search yields disclosed assumptions. Available local static rendering may answer a visual question with its reduced setup binding disclosed. Denied writes allow labelled unexecuted sketches without a scratch artifact. Sketch comparisons are untested and cannot settle empirical behavior or timing. No independent worker or model diversity is claimed without observations.\",\n  \"expectedBlocked\": \"No concrete decision routes to Feature. Missing required workflow or leaf stops dependent work. Denied or unavailable execution blocks the empirical conclusion. Missing control-ui companion or matching controls blocks visual verification. Missing setup permission blocks dependency installation or listener startup. Missing Opening a PR stops PR-dependent work, and absent external authorization prevents external delivery.\",\n  \"forbiddenClaims\": [\n    \"The prototype is production-ready, shippable or the real build.\",\n    \"A concrete behavioral choice was experimentally settled without observed execution output.\",\n    \"Visual verification passed without per-variant screenshots and driven interactions through the matching controls.\",\n    \"Unexecuted sketches, structural validation or assertions prove observed behavior or timing.\",\n    \"Dependencies, CDN access, listeners, production writes or external delivery are implicitly authorized.\",\n    \"A denied write produced a scratch artifact, or a requested model proves an observed model or diversity.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/prototype.json\"\n}"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe/visual-tool-results.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe/visual-tool-results.json",
      "sha256": "2e2c0cbfe8bd96afe9610adb578de89e3ac1553a402e8ba3f4d7b42e716a3947",
      "bytes": 350,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "[\n  {\n    \"tool\": \"mcp__cua_repl.js\",\n    \"code\": \"await cua.createBrowserTab(\\\"iab\\\", localFile, {visible:false})\",\n    \"result\": \"Browser is not available: iab\",\n    \"createdTab\": false\n  },\n  {\n    \"tool\": \"mcp__cua_repl.js\",\n    \"code\": \"await cua.listBrowsers()\",\n    \"result\": [],\n    \"screenshotCount\": 0,\n    \"drivenInteractionCount\": 0\n  }\n]"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe.result.md",
      "sha256": "902959af1e011ccee55c10fe2bd9ba0fc4797b02c7bdb3ec6b4ebf498a8a8aea",
      "bytes": 6139,
      "owners": [
        "grades-native-11.json#5"
      ],
      "text": "# throwaway-probe\n\nInput Git revision independently read as 69a848296f870402cb15b85e93dff671fa32059d. Package version 0.1.0 read from plugin.json. The supplied package freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The installed tree has no .git, so that source commit cannot be independently established from the copy. package-manifest.json retains exact observed file SHA-256 values. Only the requested installed root was used. No personal history, external services, installs, commits, pushes, messages, settings or schedules were used.\n\nActual file and execution binding was functions.exec -> tools.exec_command, with Bun scripts for automation. Writes used tools.apply_patch or Bun file writes. environment.commands.json retains the observed branch, HEAD, remote listing, scoped log, diff and Bun version. Saved source-reads.json files preserve complete named source reads and hashes. The supplied acceptance contract and prompt are in each case's supplied-input.json. No self grade is assigned.\n\n## Concrete decision and actual observation\n\nChoose whether the standalone tag cat uses case-insensitive literal substring matching or whole-word matching with ASCII letter boundaries. A single ordered five-row fixture array is the data shape. The bounded throwaway script prints both alternatives. No test suite, framework, dependency installation or listener is involved.\n\nActual command was bun throwaway-probe/probe.mjs, exit 0. Full stdout and stderr are retained in throwaway-probe/observed-output.json.\n\n| Input | Expected | A substring observed | B whole word observed |\n| --- | --- | --- | --- |\n| cat | true | true | true |\n| Cat nap | true | true | true |\n| the cat sleeps | true | true | true |\n| concatenate | false | true | false |\n| bobcat | false | true | false |\n\nRecommend B using /(^|[^A-Za-z])cat([^A-Za-z]|$)/i. It matches all five observed expectations. A fails both negative examples and is discarded. ASCII boundaries intentionally treat digits and underscores as nonletters. This is a fixture-specific choice, not a performance claim or Unicode policy. No timing was measured, so the benchmark checklist yields no performance conclusion.\n\n## Visual alternatives\n\nThe isolated throwaway layout.html contains one labelled switcher with A dense list, B card grid and C reading focus, plus a whole-word filter interaction. A favors scanning rows, B favors an overview, and C favors reading with more scrolling. These are untested layout tradeoffs. No preferred layout is selected from unobserved interactions.\n\nActual mcp__cua_repl.js call attempted cua.createBrowserTab with iab and this local file. It returned Browser is not available: iab. No browser tab, screenshots or driven interactions were produced. A subsequent cua.listBrowsers() returned an empty array. No unrelated personal surface was read. Both tool results are retained in throwaway-probe/visual-tool-results.json. The requested installed package has no control-ui companion. The control tool is exposed but the attempted surface failed. Visual verification is blocked. The HTML artifact alone proves only construction.\n\n## Variants attempted\n\n| Variant | Actual branch output and limits |\n| --- | --- |\n| Baseline writes and execution allowed | Script executed and output retained. Whole-word recommendation settled by observed output. Visual controls failed as recorded. |\n| Execution unavailable | Simulated negative condition because Bun is actually available. No execution is performed within this variant. Both algorithms remain unexecuted sketches here, so this branch cannot experimentally select a winner. Baseline evidence is labelled separately. |\n| Writes denied | Simulated restriction because case writes are actually permitted. Response-only sketches are A includes(cat), B ASCII boundary regex, and three labelled layout concepts. This branch creates no scratch artifact. Baseline artifacts are not attributed to it. |\n| Visual controls absent | Missing control-ui is an actual dependency gap. iab is also actually unavailable. No visual proof or screenshots claimed. Other host browsers were not inspected. |\n| Open design direction | No concrete visual direction or user preference is supplied. External reference search is prohibited by this isolated task, and no local reference corpus is supplied. No sourced moodboard can be built. Direction selection is pending, so this open-direction branch stops before construction. Baseline variants above are labelled unsupported sketches, not user-selected open-direction work. |\n| No concrete decision | Routes to Feature, whose complete playbook was read. No prototype or real feature construction is authorized by that branch. Need a concrete desired user outcome before Feature grounding. |\n\n## Workflow evidence and handoff\n\nRead the entire mode and six-step Prototype playbook, full poteto prompt, Exhaust the Design Space, Feature, architect with runner/rationale/red-flags, benchmark-checklist and Opening a PR. Complete named reads and hashes are in source-reads.json. The local checklist retains the six steps verbatim with outcomes, a reduced binding because no task-list tool is exposed.\n\nExhaust the Design Space changed the visual sketch from one layout to three distinct labelled shapes. Model the Domain kept the empirical inputs as one ordered table. The benchmark checklist prevented a timing claim from an untimed behavioral run. No probe was delegated and no observed-model claim is made.\n\nBlocking first steps were permissions and complete contract reads. Independent workstreams were the behavior probe and visual sketch, both directly owned here. Shared mutable state is n/a because one coordinator writes these artifacts. Smallest safe decomposition is one five-row script and one standalone HTML file.\n\nActual scratch path is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/throwaway-probe. It is throwaway. Feature or architect must own any real construction under their full contracts. Opening a PR is present and was read, but its deslop companion is absent and external delivery and commits are forbidden. No PR exists.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-11/throwaway-probe/source-reads.json",
      "owner": "grades-native-11.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/throwaway-probe/source-reads.json",
      "owner": "grades-native-11.json#5",
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
