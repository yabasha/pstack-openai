# codex: package-support-contracts

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "package-support-contracts",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Inspect the support contracts of the actual installed frozen package. Read its attribution and entry-point links, inspect its canonical logo, verify ignore boundaries in a separately authorized owned copy, and exercise the watcher compile fixture only with existing approved dependencies and execution.",
  "caseDefinition": {
    "id": "package-support-contracts",
    "sourcePaths": [
      ".gitignore",
      "LICENSE",
      "README.md",
      "assets/logo.png",
      "skills/poteto-mode/scripts/watch-pr/tsconfig.json",
      "skills/poteto-mode/scripts/watch-pr/types.compile.ts"
    ],
    "prompt": "Inspect the support contracts of the actual installed frozen package. Read its attribution and entry-point links, inspect its canonical logo, verify ignore boundaries in a separately authorized owned copy, and exercise the watcher compile fixture only with existing approved dependencies and execution.",
    "requirements": [
      "Read the actual installed-copy identity and bind it to the exact frozen SHA and package version. Preserve byte identity when preparing any authorized writable verification copy; no source-only copy is installed evidence.",
      "Read the complete MIT license and Lauren Tan attribution. Follow README navigation to actual local destinations and distinguish setup guidance from supported loading observations.",
      "Inspect assets/logo.png against its canonical digest and retain an actual rendering observation when image display is available. File existence alone does not prove rendering.",
      "Check .gitignore with actual Git ignore queries in the authorized verification copy: upstream downloads, node_modules and named temporary data are ignored; tracked provenance and evidence, including logs, remain eligible. Do not alter the installed package.",
      "Read the complete watcher tsconfig and types.compile fixture. With the exact existing pinned dependencies and approved execution, run the documented strict no-emit compiler command from skills/poteto-mode/scripts through Bun --no-install using the local TypeScript executable, --project watch-pr/tsconfig.json --noEmit --strict. Retain the actual invocation, runtime/version, exit status and output. Preserve positive READY typing and all four negative @ts-expect-error assertions.",
      "read, inspect-installed-copy, inspect-support-contracts, render-logo, check-ignore and compile-proof are observation labels tied to actually exposed operations and retained artifacts, never invented APIs.",
      "A reduced read-based report explicitly lists unexecuted compile, rendering and ignore-query branches. Missing dependencies block compiler proof; no installation, network, live forge operation or setup permission follows from this case."
    ],
    "expectedFull": "Actual read and inspected installed-copy identity, resolved README links, full license attribution, canonical logo rendering, observed ignore checks and successful strict compile fixture output support this support-contract case. Worker execution meets the existing spawn/result requirements if claimed. Compilation proves the fixture contract only, not live watcher or forge behavior.",
    "expectedReduced": "Inspect the accessible actual installed support files through authorized sequential reads and report exact observations. Keep absent compilation, rendering or Git execution explicitly unproven. Read-based reduction proves no compiler execution, logo rendering, installed dependency availability, worker independence or live watcher behavior.",
    "expectedBlocked": "Unavailable installed-copy identity, inaccessible support files, denied execution or missing dependencies blocks the affected operation. Report precise limits; preserve files and perform no setup. Source-only inspection remains structural and cannot stand in for installed support behavior.",
    "forbiddenClaims": [
      "Source bytes alone prove installed support behavior.",
      "Reading types.compile.ts is a compiler pass.",
      "File existence is rendered-logo proof.",
      "Structural fixtures prove live watcher readiness.",
      "Missing dependencies permit implicit installation.",
      "Reduced read observations prove any unexecuted branch."
    ],
    "caseFile": "docs/parity/cases/package-support.json"
  },
  "registry": {
    "caseId": "package-support-contracts",
    "caseFile": "docs/parity/cases/package-support.json",
    "sourcePaths": [
      ".gitignore",
      "LICENSE",
      "README.md",
      "assets/logo.png",
      "skills/poteto-mode/scripts/watch-pr/tsconfig.json",
      "skills/poteto-mode/scripts/watch-pr/types.compile.ts"
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
        "inspect-installed-copy",
        "inspect-support-contracts",
        "render-logo",
        "check-ignore",
        "compile-proof",
        "execution"
      ],
      "reduced-pass": [
        "read",
        "inspect-installed-copy",
        "inspect-support-contracts"
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
