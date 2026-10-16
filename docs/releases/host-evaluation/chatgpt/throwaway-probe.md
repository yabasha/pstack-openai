# chatgpt: throwaway-probe

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "throwaway-probe",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#21",
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
      "attemptId": "grades-chatgpt-09-12.json#21",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 21,
      "host": "chatgpt",
      "caseId": "throwaway-probe",
      "status": "blocked",
      "grade": {
        "caseId": "throwaway-probe",
        "batch": "batch-11",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Exact five-string decision requires observed outputs; Bun absent and neither algorithms nor visual variants run. Correctly avoids choosing from expected-output printer; no completed empirical prototype.",
        "actualResponse": "The exact decision is substring versus case-insensitive ASCII-letter-boundary matching for the five supplied cat strings. The criteria favor whole-word semantics by specification, but the task permits selecting only from observed outputs. Bun is absent, so I did not run either algorithm or select an empirically verified winner. No expected-output printer or assertion suite substitutes for that run. A bounded script would log both labeled alternatives against exactly those strings; it remains unexecuted. The separate visual comparison lacks actual app controls/reference direction and no layouts were rendered, driven or screenshotted. No prototype scratch code, listener, dependency, production change or external write was made. Open design direction requires prior-art/moodboard plus user direction, which this no-external scope does not supply. No concrete decision routes Feature. The result is an unresolved throwaway decision, not shippable code.",
        "variants": [
          {
            "name": "literal substring vs whole-word five exact strings",
            "state": "blocked",
            "reason": "Bun absent; no program output observed, no winner selected"
          },
          {
            "name": "2-3 labeled layout variants one switcher",
            "state": "blocked",
            "reason": "No matching control companion/runnable render; no visual variants built"
          },
          {
            "name": "interaction capture and screenshot every variant",
            "state": "blocked",
            "reason": "No rendered fixture or matching controls"
          },
          {
            "name": "execution unavailable",
            "state": "blocked",
            "reason": "Actual Bun absence, no alternate runtime"
          },
          {
            "name": "writes denied",
            "state": "attempted",
            "reason": "Would return labeled textual sketches without scratch artifact; no denied writes attempted"
          },
          {
            "name": "visual controls absent",
            "state": "blocked",
            "reason": "No matching fixture render/driver"
          },
          {
            "name": "open direction prior art moodboard selection",
            "state": "blocked",
            "reason": "No authorized external reference search or supplied direction/moodboard"
          },
          {
            "name": "no concrete decision",
            "state": "attempted",
            "reason": "Route Feature, do not manufacture prototype scope"
          },
          {
            "name": "benchmark timing",
            "state": "blocked",
            "reason": "No timing measured; benchmark checklist read only"
          },
          {
            "name": "real construction/PR handoff",
            "state": "blocked",
            "reason": "No prototype evidence or production/external authorization"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "literal substring vs whole-word five exact strings",
            "reason": "Bun absent; no program output observed, no winner selected"
          },
          {
            "variant": "2-3 labeled layout variants one switcher",
            "reason": "No matching control companion/runnable render; no visual variants built"
          },
          {
            "variant": "interaction capture and screenshot every variant",
            "reason": "No rendered fixture or matching controls"
          },
          {
            "variant": "execution unavailable",
            "reason": "Actual Bun absence, no alternate runtime"
          },
          {
            "variant": "visual controls absent",
            "reason": "No matching fixture render/driver"
          },
          {
            "variant": "open direction prior art moodboard selection",
            "reason": "No authorized external reference search or supplied direction/moodboard"
          },
          {
            "variant": "benchmark timing",
            "reason": "No timing measured; benchmark checklist read only"
          },
          {
            "variant": "real construction/PR handoff",
            "reason": "No prototype evidence or production/external authorization"
          }
        ],
        "limits": [
          "Bun absent; no Node/Python runtime substitute.",
          "No live accounts/services/external writes/schedules/global settings.",
          "Task Git revision absent; supplied sourceFreeze is not verified host Git HEAD.",
          "Early raw metadata export incomplete; truncated outputs retained as returned, not reconstructed.",
          "Prior Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "The concrete question and bounded fixture probe produce retained observed output that decides the behavioral choice. Visual alternatives have labelled switcher states, per-variant screenshots and driven interactions through observed authorized controls. Open direction has source-backed references and user selection before building. The reply contains the decision, evidence, tradeoffs, recommendation and actual isolated throwaway artifact. Production work is handed to its complete workflow, and forbidden external actions remain unperformed.",
        "reducedExpected": "Unavailable reference search yields disclosed assumptions. Available local static rendering may answer a visual question with its reduced setup binding disclosed. Denied writes allow labelled unexecuted sketches without a scratch artifact. Sketch comparisons are untested and cannot settle empirical behavior or timing. No independent worker or model diversity is claimed without observations.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "reviewedBy": "grade_contract_audit"
          },
          {
            "observation": "review-outcome",
            "evidence": "grades-chatgpt-09-12.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ]
      },
      "topLevelContext": {
        "scope": "Actual ChatGPT Work remaining batches09..12,30cases",
        "gradingNotes": [
          "Independent outcome review of retained actual responses/variants/source artifacts, not exported selfgrades.",
          "Native UI aggregate reads/commands/worker activity supplied by parent; exact model-captured logs treated with explicit provenance gaps.",
          "No proxy programs/fixture verdicts count as actual service or worker results.",
          "Missing taskGit and unavailable Bun remain required-method blockers; tools themselves not declared absent.",
          "All named requested variants must be addressed before full. No full awarded in this set.",
          "Old original source path failures retained; documented fallback source reads not automatically rejected.",
          "history-evidence is included because actual cloud batch09 contains it; do not count duplicate historical case twice when aggregating target coverage."
        ]
      },
      "response": {
        "text": "The exact decision is substring versus case-insensitive ASCII-letter-boundary matching for the five supplied cat strings. The criteria favor whole-word semantics by specification, but the task permits selecting only from observed outputs. Bun is absent, so I did not run either algorithm or select an empirically verified winner. No expected-output printer or assertion suite substitutes for that run. A bounded script would log both labeled alternatives against exactly those strings; it remains unexecuted. The separate visual comparison lacks actual app controls/reference direction and no layouts were rendered, driven or screenshotted. No prototype scratch code, listener, dependency, production change or external write was made. Open design direction requires prior-art/moodboard plus user direction, which this no-external scope does not supply. No concrete decision routes Feature. The result is an unresolved throwaway decision, not shippable code.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/result.json",
          "sha256": "98f5c146f239a6c84839c10480e739bd072ce0e254d1aa302228cbc1862b1064",
          "bytes": 3401
        },
        "extraction": "Actual response field when present; otherwise complete retained JSON"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "sha256": "667b5681288f125d3857df0388ae65288954542d8545c2b44a420635baa66c49",
            "bytes": 430462
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "sha256": "a0f4eb6e5baaded49263375472ed1d7b945b1aa4459538f99c6abf2f46b3ebf5",
            "bytes": 28398
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/case.json",
            "sha256": "713ae4e2f39eb6e29cb219d2fb94d4073369878dd2f4b1ef1838c2c403a39c9a",
            "bytes": 3111
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/throwaway-probe/evidence/source-read-status.tsv",
            "sha256": "7325eeaaf8e80ea8d806ad0d4da96f1f13463cf3b1fa80ed76dd34413886e22f",
            "bytes": 456
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
              "reviewedBy": "grade_contract_audit"
            },
            {
              "observation": "review-outcome",
              "evidence": "grades-chatgpt-09-12.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [],
  "skippedManifest": [],
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
