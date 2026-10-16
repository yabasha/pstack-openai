# codex: trace-provenance

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "trace-provenance",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Diagnose supplied inert cpuprofile, compressed JSON trace, heap snapshot and spindump fixtures without rerunning their processes. Include exact artifact identities, original order, timestamps and symbols mapping to fixture source. Build an authorized sqlite query artifact and inspect hot frames, a retainer chain to a GC root or a stuck thread and wait reason. Compare a supplied before/after pair separately from an unpaired capture. Repeat with absent parser, denied derived writes, inaccessible artifact, unresolved symbols and unavailable workers. No installation, upload, live capture, external write or fix.",
  "caseDefinition": {
    "id": "trace-provenance",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/trace-forensics.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/poteto-mode/playbooks/runtime-forensics.md",
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/playbooks/perf-issue.md"
    ],
    "prompt": "Diagnose supplied inert cpuprofile, compressed JSON trace, heap snapshot and spindump fixtures without rerunning their processes. Include exact artifact identities, original order, timestamps and symbols mapping to fixture source. Build an authorized sqlite query artifact and inspect hot frames, a retainer chain to a GC root or a stuck thread and wait reason. Compare a supplied before/after pair separately from an unpaired capture. Repeat with absent parser, denied derived writes, inaccessible artifact, unresolved symbols and unavailable workers. No installation, upload, live capture, external write or fix.",
    "requirements": [
      "Read the complete mode, playbook, guard-the-context-window leaf and role prompt. Discover actual artifact access, parsing, execution and storage operations; preserve permissions and inherited model selection unless supported and observed.",
      "Identify format and retain original bytes, exact trace identity and path. Parse large artifacts with an authorized independent worker and inspect its result; bounded sequential parsing is reduced capability.",
      "Reach a queryable shape before diagnostic reading. Dump trace or heap data to sqlite with one row per sample, frame or node. Preserve source identity, original order, timestamps, frame or node identities and call-tree or retainer relationships with original-record links. Denied or missing conversion must stay explicit.",
      "Query the time-heavy frames and hot call path, the leaked-object retainer chain to a GC root, or the on-CPU/blocked spindump thread and wait reason. Cite exact original artifact records and map file, symbol and line through the artifact symbols. Resolve symbols or state their absence.",
      "Diff an accessible compatible supplied before/after pair and cite both identities and comparison evidence. Without a usable pair, retain the strongest supported hypothesis and never claim confirmed cause.",
      "Return artifact and format, reduced finding, source location, artifact paths and paired-capture confirmation state plus the exact throughput checkpoint: n/a, read-only forensics line. Route known causes to Bug fix or Perf issue without implementing an unsolicited fix."
    ],
    "expectedFull": "Accessible fixed fixtures yield a retained original and observed sqlite conversion with source-linked rows that preserve identity, order and relationships. Findings cite original records and artifact-symbol mappings to source. An inspected compatible before/after diff supports the stated confirmation; an unpaired result is explicitly a hypothesis. Large-artifact delegation requires observed worker creation and result inspection. The reply retains every required item and the exact throughput line.",
    "expectedReduced": "Authorized bounded sequential parsing or a read-only queryable representation yields only the supported cited assessment. It preserves exact trace identity, original order and source links, while declaring absent independent workers or sqlite conversion. Missing symbols leave an explicitly unmapped finding; no usable pair leaves a hypothesis. Unknown actual models prove no diversity.",
    "expectedBlocked": "Missing required contracts stops dependent work. Inaccessible artifacts or absent suitable parsers block analysis. Denied storage or absent sqlite conversion blocks the requested dump, with a reduced read-only representation only when actually accessible. Unresolved symbols or inaccessible source block a complete mapped diagnosis. Inaccessible or incompatible paired captures block confirmation. Unread data supports no finding.",
    "forbiddenClaims": [
      "Structural validation establishes model behavior or a host pass.",
      "A fixed-artifact task authorizes rerunning the process, live instrumentation, upload, installation or an unsolicited fix.",
      "Missing artifact access or parser availability is a successful load or parse.",
      "Reordered or reconstructed events retain the original trace order.",
      "A derived row without an exact source-artifact link proves trace provenance.",
      "Missing symbols or symbols from another revision prove the claimed file and line.",
      "An unpaired, inaccessible or incompatible capture confirms the cause.",
      "Sequential parsing establishes independent workers or an unknown actual model establishes diversity.",
      "A read-only representation proves sqlite conversion or denied writes succeeded."
    ],
    "caseFile": "docs/parity/cases/playbooks/trace-forensics.json"
  },
  "registry": {
    "caseId": "trace-provenance",
    "caseFile": "docs/parity/cases/playbooks/trace-forensics.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/trace-forensics.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/poteto-mode/playbooks/runtime-forensics.md",
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/playbooks/perf-issue.md"
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
        "execution"
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
        "execution"
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
