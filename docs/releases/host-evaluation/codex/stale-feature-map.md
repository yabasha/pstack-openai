# codex: stale-feature-map

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "stale-feature-map",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Audit the verify skill against this supplied changed app contract: a previously immediate save now requires entitlement and finishes asynchronously. Review every feature from source and live without weakening proof to a static screenshot or silently deleting the old requirement.",
  "caseDefinition": {
    "id": "stale-feature-map",
    "sourcePaths": [
      "skills/maintain-verification-skill/SKILL.md"
    ],
    "prompt": "Audit the verify skill against this supplied changed app contract: a previously immediate save now requires entitlement and finishes asynchronously. Review every feature from source and live without weakening proof to a static screenshot or silently deleting the old requirement.",
    "requirements": [
      "Supplied changed app contract and repository source access",
      "Target verification skill, feature-map index and feature files",
      "Observed independent readers for full source wave",
      "Authorized execution, app driving and scoped skill writes",
      "Explicit authorization before a branch or PR ships corrections"
    ],
    "expectedFull": "Locate the existing target and reconcile its index. Assign one read-only reader per feature, inspect every returned source summary and citation, merge recipes and check churn for missing source-backed features. The coordinator drives every feature according to the target launch model. Doctor before first and fresh-session drives and after failures; reset wedged UI state. Preserve and check evidence after cleanup, clean failed-drive residue and perform final teardown after re-proofs. Classify confirmed contract change as doc drift, broken product behavior as a product gap, and working behavior unreachable by the harness as a harness gap. Record the entitlement and attempted route for verified-unreachable, repair missing prerequisites and re-drive harness fixes. Re-read changed files and produce at most one authorized PR of proven corrections, or report clean or blocked honestly.",
    "expectedReduced": "Without independent workers, one coordinator may read every feature serially as reduced capability, retaining all source and live coverage standards. Without shipping authorization, retain proven corrections for local review and report blocked shipping; do not create a branch or PR. Without execution or app-driving, provide source findings and pending live recipes, mark live verification not-run and outcome blocked. Read-only permissions permit recommendations only, with denied writes explicit.",
    "expectedBlocked": "Missing target stops with a pointer to /create-verification-skill; multiple candidates require target selection. Missing source access or denied proof execution blocks coverage. Doctor drift permits one scoped repair and retry with only invalidated state restarted; unresolved failure remains blocked. Never call incomplete coverage clean or silently weaken feature proof.",
    "forbiddenClaims": [
      "Source review or static screenshots alone prove every feature live",
      "Sequential readers are independent parallel workers",
      "Product regressions can be hidden by weakening the feature map",
      "A feature is verified-unreachable without a concrete prerequisite and attempted route",
      "Cleanup may delete evidence or leave failed-drive residue running",
      "A harness repair can ship without a live re-drive",
      "Upstream ship instructions authorize a PR or recurring schedule",
      "Structural validation proves host behavior"
    ],
    "caseFile": "docs/parity/cases/skills/maintain-verification-skill.json"
  },
  "registry": {
    "caseId": "stale-feature-map",
    "caseFile": "docs/parity/cases/skills/maintain-verification-skill.json",
    "sourcePaths": [
      "skills/maintain-verification-skill/SKILL.md"
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
