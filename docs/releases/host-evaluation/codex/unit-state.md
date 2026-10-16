# codex: unit-state

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "unit-state",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.",
  "caseDefinition": {
    "id": "unit-state",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/scripts/orch/orch.ts",
      "skills/poteto-mode/scripts/orch/store.ts",
      "skills/poteto-mode/scripts/orch/orch.test.ts",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "skills/poteto-mode/scripts/package.json",
      "skills/poteto-mode/scripts/bun.lock",
      "skills/arena/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/unslop/SKILL.md"
    ],
    "prompt": "Run a fixture program with two isolated units at exact full revisions, disjoint workers and a coordinator-owned bookkeeping store. Include a successful worker, a stale result, a lost drain receipt, a changed head, a blocked verifier, a late zombie, a pending merge permission gate and a stale lock. Show complete standing orders, inspected real results, drain receipt readback, exact revision ledger checks, a generation-pinned frontier and truthful close counts. Repeat with unavailable workers, missing helper dependencies, denied writes, unavailable wake and unknown models. No live forge writes or recurring scheduling.",
    "requirements": [
      "Read full mode, original program roles, playbook and direct helper/support contracts. Keep coordinator out of code; use scoped fix units and continuous authorized landing. Scale cheap units without inventing independent verifiers.",
      "Use immutable identity, exact input SHA, exclusive output owner/path, append-only attempts, complete brief fields and verbatim standing orders on each spawn/resume. Remote placement, nesting, background execution and model diversity require observed bindings.",
      "Use the actual explicit external store CLI with pinned prerequisites. Record real worker identity/results separately; arbitrary unit-state strings and evidence pointers are not checked by the helper.",
      "Pilot one unit end to end before a rolling window. Relay upstream context, audit briefs alongside the wave, drain only at the four named boundaries and preserve every pointer through a peek receipt and readback before destructive drain.",
      "Classify all pointers, inspect artifacts before recording rows, preserve arrivals for the next batch, reconcile every child and late zombie against exact assignment and current frontier. Do not accept stale or cancelled partial work.",
      "One stacker per stack and one babysitter per generation. Discover the ordered frontier from real stack-owner metadata and git SHAs; missing metadata blocks that dependency. Workers never run gt or rebase. External actions retain explicit authorization and interrupted unknown outcomes block replay.",
      "Check ledger by current PR plus full head SHA. Inspect evidence and enforce verifier precedence outside the helper. New heads require verification, historical summary counts are not current passes, type-check-only is insufficient for behavioral work and blocked/failed verdicts are not passes.",
      "Bound source failure retries to two while obeying the stricter assignment allowance of one retry for missing SHA/method evidence. Stop tree-wide refills on invalid upstream input, preserve terminal handoff and review stale lock ownership before force.",
      "Keep overview append-only, decision trail auditable, gates explicit and status derived. Close only after final drain, terminal reconciliation and predicate verification on the real artifact. Report predicate/counts, tracks/landed work, PRs/SHAs, verdicts, abandonments/reasons, gates, store/trail paths and review limits."
    ],
    "expectedFull": "Observed authorized independent workers produce inspected isolated artifacts at their assigned input revisions. The coordinator persists complete drain receipts, updates actual helper rows, accepts only current evidenced verdicts, keeps the generation-pinned frontier green and accounts for every child. All permission gates require actual authorization. The unchanged predicate matches real landed artifacts and current head verdicts; the full checkpoint report and intact postmortem store resolve.",
    "expectedReduced": "Authorized sequential foreground execution preserves scope, exact revisions, receipts, gates, current verification and truthful reports while disclosing missing independent workers, remote placement, wake, model diversity or review. Unavailable push permission retains durable local artifacts and pending landing. A read-only handoff can describe supplied state but cannot claim helper writes, saved continuity or program completion.",
    "expectedBlocked": "Denied execution or persistence, missing pinned dependencies or required pending callers block their dependent steps. Missing identity, exact revision, artifacts or method evidence prevents acceptance. Stale heads, lost drain receipts and zombies require inspected reconciliation. Missing gt metadata blocks frontier recomputation. Required independent verification, different-family review and unauthorized external actions remain blocked. Stale lock takeover requires ownership review and applicable permission.",
    "forbiddenClaims": [
      "Structural checks or snapshot tests prove current caller host parity or real workers.",
      "Unit done strings, typed ledger verdicts or summary counts prove real current completion without artifact/method inspection.",
      "Sequential roles prove independent workers, cloud execution, nesting, model diversity or unattended recovery.",
      "A truncated standing summary contains all standing orders.",
      "An inbox notification or destructive drain without a persisted receipt proves inspected results.",
      "Historical head verdicts verify a restacked head, or type-check-only and verifier-blocked pass behavioral work.",
      "The helper enforces immutable assignments, SHA syntax, ownership, evidence existence or verifier precedence.",
      "Dead pid permits automatic force takeover or restart proves worker liveness.",
      "Gate defaults, broad autonomy or initialization authorize installs, push, merge, messaging or schedules.",
      "Missing gt metadata can be replaced by a guessed authoritative frontier."
    ],
    "caseFile": "docs/parity/cases/playbooks/orchestrate.json"
  },
  "registry": {
    "caseId": "unit-state",
    "caseFile": "docs/parity/cases/playbooks/orchestrate.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/scripts/orch/orch.ts",
      "skills/poteto-mode/scripts/orch/store.ts",
      "skills/poteto-mode/scripts/orch/orch.test.ts",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "skills/poteto-mode/scripts/package.json",
      "skills/poteto-mode/scripts/bun.lock",
      "skills/arena/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md",
      "skills/poteto-mode/playbooks/autonomous-run.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/unslop/SKILL.md"
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
