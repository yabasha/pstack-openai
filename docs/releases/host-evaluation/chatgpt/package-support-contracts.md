# chatgpt: package-support-contracts

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "package-support-contracts",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#8",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
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
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#8",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 8,
      "host": "chatgpt",
      "caseId": "package-support-contracts",
      "status": "reduced-pass",
      "grade": {
        "caseId": "package-support-contracts",
        "batch": "batch-10",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Actual package metadata/copies/license/logo rendering and isolated Git ignore checks are partially corroborated local observations. Compiler/Bun/pinned helper prerequisites absent; cannot full compile or exact revision-bound support contract.",
        "actualResponse": "The actual installed plugin.json reports pstack-openai 0.1.0. Input sourceFreeze is f4623636a287bea2aa79c4b2234a53d20a5f193c, a supplied freeze label, not a verified installed Git HEAD. Full MIT license and Lauren Tan attribution were read. README navigation reaches actual local Poteto/Swarm workflow files; observed filesystem navigation does not prove host menu registration. I rendered the canonical logo through tools.view_image: an illustrated dark-haired person in glasses eating a purple sweet potato on light blue. Installed/copy logo SHA256 both equal canonical digest 672f6791589ef758b0ced2c4c477913fa2758623c438e265639a0d539ce90695. An authorized full package copy was made, then an isolated local Git repository initialized solely for ignore queries. Dedicated recursive diff excluding newly created .git returned exit0 with no differences. Actual git check-ignore --no-index -v -n confirms upstream downloads, node_modules, .task-tmp and .bun-cache ignored, while provenance, evidence JSON and logs remain eligible. Installed package untouched. The watcher tsconfig/compile fixture retains positive READY proof and four negative @ts-expect-error cases. Compiler proof did not run: Bun absent and exact installed helper dependencies absent. A mistaken .claude-plugin/plugin.json read failed and is retained before the real root plugin.json read.",
        "variants": [
          {
            "name": "installed identity and full-copy byte comparison",
            "state": "attempted",
            "reason": "plugin.json, sourceFreeze, recursive diff exit0; installed exact Git SHA unavailable"
          },
          {
            "name": "MIT attribution and README destinations",
            "state": "attempted",
            "reason": "Actual local files read; setup guidance remains unverified loading evidence"
          },
          {
            "name": "canonical digest and rendered logo",
            "state": "attempted",
            "reason": "tools.view_image returned actual rendered image; source binary retained"
          },
          {
            "name": "ignore boundaries",
            "state": "attempted",
            "reason": "Actual isolated git check-ignore observed matching and eligible paths"
          },
          {
            "name": "watcher strict compile READY/four negatives",
            "state": "blocked",
            "reason": "Bun absent and existing pinned dependencies unavailable; no compiler substitute"
          },
          {
            "name": "exact frozen Git commit binding",
            "state": "blocked",
            "reason": "Supplied sourceFreeze not independently verified Git HEAD"
          },
          {
            "name": "network/setup/live forge",
            "state": "blocked",
            "reason": "Explicitly unauthorized; no calls made"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "watcher strict compile READY/four negatives",
            "reason": "Bun absent and existing pinned dependencies unavailable; no compiler substitute"
          },
          {
            "variant": "exact frozen Git commit binding",
            "reason": "Supplied sourceFreeze not independently verified Git HEAD"
          },
          {
            "variant": "network/setup/live forge",
            "reason": "Explicitly unauthorized; no calls made"
          }
        ],
        "limits": [
          "Bun unavailable; no Node/Python substitute.",
          "Supplied freeze is not verified installed/task Git HEAD.",
          "No live accounts/services/writes/settings/schedules.",
          "Some initial tool raw metadata omitted from local export and some large outputs truncated, explicitly not reconstructed.",
          "Prior Node/Python deviation retained, not repeated.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Actual read and inspected installed-copy identity, resolved README links, full license attribution, canonical logo rendering, observed ignore checks and successful strict compile fixture output support this support-contract case. Worker execution meets the existing spawn/result requirements if claimed. Compilation proves the fixture contract only, not live watcher or forge behavior.",
        "reducedExpected": "Inspect the accessible actual installed support files through authorized sequential reads and report exact observations. Keep absent compilation, rendering or Git execution explicitly unproven. Read-based reduction proves no compiler execution, logo rendering, installed dependency availability, worker independence or live watcher behavior.",
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
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
        "text": "The actual installed plugin.json reports pstack-openai 0.1.0. Input sourceFreeze is f4623636a287bea2aa79c4b2234a53d20a5f193c, a supplied freeze label, not a verified installed Git HEAD. Full MIT license and Lauren Tan attribution were read. README navigation reaches actual local Poteto/Swarm workflow files; observed filesystem navigation does not prove host menu registration. I rendered the canonical logo through tools.view_image: an illustrated dark-haired person in glasses eating a purple sweet potato on light blue. Installed/copy logo SHA256 both equal canonical digest 672f6791589ef758b0ced2c4c477913fa2758623c438e265639a0d539ce90695. An authorized full package copy was made, then an isolated local Git repository initialized solely for ignore queries. Dedicated recursive diff excluding newly created .git returned exit0 with no differences. Actual git check-ignore --no-index -v -n confirms upstream downloads, node_modules, .task-tmp and .bun-cache ignored, while provenance, evidence JSON and logs remain eligible. Installed package untouched. The watcher tsconfig/compile fixture retains positive READY proof and four negative @ts-expect-error cases. Compiler proof did not run: Bun absent and exact installed helper dependencies absent. A mistaken .claude-plugin/plugin.json read failed and is retained before the real root plugin.json read.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/result.json",
          "sha256": "b5507660bf8cc2fa5164c9b91026e923ffa4df23f82ebbb64f778b96a177b211",
          "bytes": 3533
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "sha256": "573460e5da46c0ef316385566ec2c9a9e86bc65be4ba7bf24d3449eec1bce3f4",
            "bytes": 24603
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/case.json",
            "sha256": "81400e8ed8cdefa232db12de81e1e4687461bad8d8881c3e8687b03f95db096c",
            "bytes": 2402
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/package-support-contracts/evidence/source-read-status.tsv",
            "sha256": "3aa5d9acad60ea8c40387ed649afe1b12952dc4a4ceaa6c00f3acedf069d5170",
            "bytes": 160
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
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
