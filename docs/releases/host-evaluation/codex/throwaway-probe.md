# codex: throwaway-probe

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "throwaway-probe",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
  "attempts": [],
  "artifactProjections": [],
  "skippedManifest": [],
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
