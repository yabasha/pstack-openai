# codex: real-render

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "real-render",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Match a migrated component to its established baseline across default, hover, focus and disabled states. First inspect actual rendered output, then image-diff it. Exercise a nonzero delta and missing matching controls. Do not modify the baseline or harness and do not create a PR without authorization.",
  "caseDefinition": {
    "id": "real-render",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/visual-parity.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Match a migrated component to its established baseline across default, hover, focus and disabled states. First inspect actual rendered output, then image-diff it. Exercise a nonzero delta and missing matching controls. Do not modify the baseline or harness and do not create a PR without authorization.",
    "requirements": [
      "Capture the immutable current-component baseline before migration and the target when matching two implementations; retain harness location and screenshots.",
      "Use actual matching-surface control and image-diff operations; retain rendered screenshots, numeric diffs and diff artifacts for every component and state.",
      "Freeze baseline, harness and component structure against shortcuts; stop and ask if baseline is wrong.",
      "Migrate shared primitives first, then one component per owner and isolated worktree; inspect independent-worker artifacts when authorized, otherwise disclose sequential reduction.",
      "Treat nonzero diff as failure and investigate then repeat per component until zero; disclose absent /loop companion and any explicit reduced repetition.",
      "Read mode, applied principle and role prompt and follow capability, assignment and model contracts; read full Opening a PR before permitted component or safe-batch delivery.",
      "Report components, each diff result, baseline harness, remaining work and missing controls; do not perform unauthorized external writes."
    ],
    "expectedFull": "Actual rendered screenshots and diff artifacts across all baseline states show zero difference for every accepted component after investigation of the nonzero delta. Shared primitives precede isolated component work, independent workers are observed when used, and authorized delivery follows the full PR contract.",
    "expectedReduced": "Authorized sequential migration or explicit repetition preserves the immutable baseline and actual rendered zero-diff evidence where available. It discloses missing worker, isolation or loop-companion support and returns local artifacts when delivery is unauthorized. Reduced planning or source inspection supplies no visual pass.",
    "expectedBlocked": "No baseline stops migration. Unavailable or denied matching controls, rendering or image-diff execution blocks visual verification. Nonzero delta fails acceptance. A wrong baseline stops for the operator. Missing Opening a PR stops dependent delivery; no external permission leaves writes unperformed.",
    "forbiddenClaims": [
      "Visual parity without actual rendered screenshots and zero image diff across baseline states.",
      "Pass from source review, structural validation, fixture images, type checks or visual judgment alone.",
      "A modified baseline, harness or restructured component to force a passing diff.",
      "Independent workers or model diversity from sequential work or unobserved selection.",
      "A /loop companion ran when only explicit repetition was available.",
      "A created PR, push or satisfied companion gate without actual authorized observations."
    ],
    "caseFile": "docs/parity/cases/playbooks/visual-parity.json"
  },
  "registry": {
    "caseId": "real-render",
    "caseFile": "docs/parity/cases/playbooks/visual-parity.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/visual-parity.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
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
