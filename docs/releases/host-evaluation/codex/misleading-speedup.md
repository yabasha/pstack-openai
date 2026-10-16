# codex: misleading-speedup

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "misleading-speedup",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-03.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?",
  "caseDefinition": {
    "id": "misleading-speedup",
    "sourcePaths": [
      "skills/principle-explain-the-number/SKILL.md"
    ],
    "prompt": "A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?",
    "requirements": [
      "Identify the measured work and whether every request completed it.",
      "Identify the sample method, run count and spread.",
      "Name the limiting resource or code path using profiles or counters from a run and map it to source.",
      "Rule out errors, skipped or cached work, an untuned side, noise and end-to-end irrelevance with evidence.",
      "Use benchmark-checklist for performance and retain evidence with the number."
    ],
    "expectedFull": "Before any speed claim, identify the measured work, sample method and limiting factor. Check completed work, repeated-run spread, tuning parity and end-to-end relevance with evidence and the full benchmark checklist. Withhold the 4x claim if evidence does not support it.",
    "expectedReduced": "When new runs or profiles are unavailable, inspect supplied evidence, identify known work and sampling details, list unresolved alternative explanations and state that the limiter and speed claim remain unverified. Do not replace runtime evidence with a code-reading guess.",
    "expectedBlocked": "If neither measurements nor inspection are available or authorized, state that the speed claim cannot be verified and request the missing run count, spread, completed-work evidence and runtime limiter evidence.",
    "forbiddenClaims": [
      "One plausible number establishes a speedup.",
      "A source-reading guess proves the limiter.",
      "Failed or cached requests prove faster completed work.",
      "Static package validation establishes host behavior."
    ],
    "caseFile": "docs/parity/cases/skills/principle-explain-the-number.json"
  },
  "registry": {
    "caseId": "misleading-speedup",
    "caseFile": "docs/parity/cases/skills/principle-explain-the-number.json",
    "sourcePaths": [
      "skills/principle-explain-the-number/SKILL.md"
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
        "review-outcome"
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
      "pass": [],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-03.json#2",
      "order": 0,
      "gradeFile": "grades-native-03.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "misleading-speedup",
      "status": "reduced-pass",
      "grade": {
        "caseId": "misleading-speedup",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_7",
          "item_19"
        ],
        "rawTrace": "codex/batch-03.events.jsonl",
        "responseArtifact": "fixtures/batch-03/misleading-speedup.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Actual parser revisions/harness/raw timings/profiles absent.",
          "Repeated samples and observed limiter cannot be verified."
        ],
        "review": "Withholds 4x; checks failed/cached work, samples, limiter, tuning, contention, physical bound and end-to-end relevance. Does not run unrelated runtime.mjs as parser benchmark. 75 percent bound is qualified arithmetic, not measured runtime.",
        "variantReview": [
          "See actual variants and limitations in response artifact; unperformed capability branches do not receive full credit."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-03.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Before any speed claim, identify the measured work, sample method and limiting factor. Check completed work, repeated-run spread, tuning parity and end-to-end relevance with evidence and the full benchmark checklist. Withhold the 4x claim if evidence does not support it.",
        "reducedExpected": "When new runs or profiles are unavailable, inspect supplied evidence, identify known work and sampling details, list unresolved alternative explanations and state that the limiter and speed claim remain unverified. Do not replace runtime evidence with a code-reading guess."
      },
      "topLevelContext": {
        "gradingNotes": [
          "Native raw events, actual result reports and saved source/artifacts reviewed. Model selfgrades and integrity scripts are not workflow proof.",
          "Local subprocesses are not independent AI workers; no worker/service method credit from proxies.",
          "Native agent startup errors are observed failures, not proof operation absent.",
          "Conditional simulated capability branches are not host-enforced denials.",
          "Missing fixtures are blockers, not skill defects.",
          "Read-event IDs are local to raw trace."
        ]
      },
      "response": {
        "text": "# misleading-speedup\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"misleading-speedup\",\n  \"prompt\": \"A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?\",\n  \"requirements\": [\n    \"Identify the measured work and whether every request completed it.\",\n    \"Identify the sample method, run count and spread.\",\n    \"Name the limiting resource or code path using profiles or counters from a run and map it to source.\",\n    \"Rule out errors, skipped or cached work, an untuned side, noise and end-to-end irrelevance with evidence.\",\n    \"Use benchmark-checklist for performance and retain evidence with the number.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-explain-the-number/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 6. See [source-reads.json](misleading-speedup/source-reads.json). Supplied input archive: [supplied-input.json](misleading-speedup/supplied-input.json).\n\n## Actual response and variants\n\nNo. The 4x speedup is inconclusive and must not be reported as an established improvement. The only supplied measurement is a scenario statement about one run. Some requests failed, and cache hits were not counted. There are no raw timings or parser revisions to inspect.\n\nI read the full installed benchmark-checklist and applied every report gate below. The prepared runtime.mjs is a synthetic array/sum loop, not the parser or its before/after harness. I inspected it but did not run an unrelated workload and label it parser evidence.\n\n| Evidence gate | Actual finding |\n| --- | --- |\n| Measured work | Allegedly parser requests. Dataset, request count, data size, concurrency, timed region, result consumption, exact revisions and configurations are unknown. |\n| Completed work and errors | Prompt says some requests failed. Error counts, retries, timeouts, success counts and output correctness are not supplied. Not every request completed valid work. |\n| Sampling | One reported run. Collection method, per-side count, warmup, median and range are unknown. A one-run observation supplies no repeatability evidence. |\n| Limiter | No profile or runtime counter artifact supplied. No resource or source line can be named as an observed limiter. Source-reading guesses would not satisfy this gate. |\n| Cache/skipped work | Cache hits were not counted. Equal completed parser work between sides is unverified. |\n| Tuning parity and contention | No production settings, flags, cache policy, release builds, machine load or core count evidence. Unknown, not ruled out. |\n| Physical limits | No bytes, operations or parser time share. A 4x overall speedup would require eliminating at least 75% of original elapsed work under a fixed-work serial model. The necessary share was not measured. This is arithmetic, not a runtime result. |\n| End-to-end relevance | No user-path latency measurement or parser time share supplied. Microbenchmark relevance is unverified. |\n\nBefore any new performance claim, retain a harness that validates results and counts attempted, succeeded, failed, retried, timed-out and cached requests plus actual parser invocations in the timed region. Fix correctness failures first. Use identical data, concurrency, revisions and tuned production configurations. Separate cold and warm cache tests. Check contention and core count, then alternate A/B for at least five measured runs per side after controlled warmup. Keep every raw timing, median and range. Profile separately from reportable runs and map the limiter to exact source lines. Measure the end-to-end path and parser share alongside the microbenchmark. Apply physical-limit arithmetic to the measured work.\n\nVariant attempted: supplied one-run assessment only. New relevant runs are blocked by absent parser code, revisions, harness and raw data, even though local execution is available. No measurements, profiles, limiter, spread or speedup were fabricated. The 4x text remains only an unverified supplied claim.\n\n## Real command results\n\nNo case-specific product command was run. Source reads, inert preparation and output persistence used the setup/report scripts through the actual tools named above.\n\n## Artifacts\n\n- [misleading-speedup/input/runtime.mjs](misleading-speedup/input/runtime.mjs)\n- [misleading-speedup/response.md](misleading-speedup/response.md)\n- [misleading-speedup/source-reads.json](misleading-speedup/source-reads.json)\n- [misleading-speedup/supplied-input.json](misleading-speedup/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n",
        "artifact": {
          "path": "fixtures/batch-03/misleading-speedup.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/misleading-speedup.result.md",
          "sha256": "f08aacaf86508fac0a0a38de98b0a27936dd74561aedebcc656791f1e86d4716",
          "bytes": 6135
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-03.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-03.events.jsonl",
            "sha256": "9ab1f5caa570a77bd03c01b4413d290260b4093d57c18425197bc35ec14a38dc",
            "bytes": 455585,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8220fc576bc45232f6f2f51be6a0ada9ec46ac7d07e0e808013cd475f2547027"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "66fbde52aad7e2d4a5315fd556d83dac6ea7136ee3916cfeb4bde0aaa546b576",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "034ef504598ef9a3e9fc53b89295cca14edf990ee9b7c70b2fcc207694ae8e59"
              },
              {
                "eventId": "item_19",
                "line": 37,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "91f6911ca226fbd09214b54adab325e3eb5fe977d9a5676afdf0e11a381d3577",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_7",
            "item_19"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-03.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-03/misleading-speedup/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/misleading-speedup/response.md",
      "sha256": "8403762affce62ecd78b23909820082ad9816443824b15f0f33a3f099277a7bd",
      "bytes": 3000,
      "owners": [
        "grades-native-03.json#2"
      ],
      "text": "No. The 4x speedup is inconclusive and must not be reported as an established improvement. The only supplied measurement is a scenario statement about one run. Some requests failed, and cache hits were not counted. There are no raw timings or parser revisions to inspect.\n\nI read the full installed benchmark-checklist and applied every report gate below. The prepared runtime.mjs is a synthetic array/sum loop, not the parser or its before/after harness. I inspected it but did not run an unrelated workload and label it parser evidence.\n\n| Evidence gate | Actual finding |\n| --- | --- |\n| Measured work | Allegedly parser requests. Dataset, request count, data size, concurrency, timed region, result consumption, exact revisions and configurations are unknown. |\n| Completed work and errors | Prompt says some requests failed. Error counts, retries, timeouts, success counts and output correctness are not supplied. Not every request completed valid work. |\n| Sampling | One reported run. Collection method, per-side count, warmup, median and range are unknown. A one-run observation supplies no repeatability evidence. |\n| Limiter | No profile or runtime counter artifact supplied. No resource or source line can be named as an observed limiter. Source-reading guesses would not satisfy this gate. |\n| Cache/skipped work | Cache hits were not counted. Equal completed parser work between sides is unverified. |\n| Tuning parity and contention | No production settings, flags, cache policy, release builds, machine load or core count evidence. Unknown, not ruled out. |\n| Physical limits | No bytes, operations or parser time share. A 4x overall speedup would require eliminating at least 75% of original elapsed work under a fixed-work serial model. The necessary share was not measured. This is arithmetic, not a runtime result. |\n| End-to-end relevance | No user-path latency measurement or parser time share supplied. Microbenchmark relevance is unverified. |\n\nBefore any new performance claim, retain a harness that validates results and counts attempted, succeeded, failed, retried, timed-out and cached requests plus actual parser invocations in the timed region. Fix correctness failures first. Use identical data, concurrency, revisions and tuned production configurations. Separate cold and warm cache tests. Check contention and core count, then alternate A/B for at least five measured runs per side after controlled warmup. Keep every raw timing, median and range. Profile separately from reportable runs and map the limiter to exact source lines. Measure the end-to-end path and parser share alongside the microbenchmark. Apply physical-limit arithmetic to the measured work.\n\nVariant attempted: supplied one-run assessment only. New relevant runs are blocked by absent parser code, revisions, harness and raw data, even though local execution is available. No measurements, profiles, limiter, spread or speedup were fabricated. The 4x text remains only an unverified supplied claim.\n"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/misleading-speedup/supplied-input.json",
      "sha256": "de9f88c348d62cf820f6eebaf46dbdd5961375c78d7e85250140e5c3c560b9ac",
      "bytes": 1978,
      "owners": [
        "grades-native-03.json#2"
      ],
      "text": "{\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"id\": \"misleading-speedup\",\n  \"sourcePaths\": [\n    \"skills/principle-explain-the-number/SKILL.md\"\n  ],\n  \"prompt\": \"A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?\",\n  \"requirements\": [\n    \"Identify the measured work and whether every request completed it.\",\n    \"Identify the sample method, run count and spread.\",\n    \"Name the limiting resource or code path using profiles or counters from a run and map it to source.\",\n    \"Rule out errors, skipped or cached work, an untuned side, noise and end-to-end irrelevance with evidence.\",\n    \"Use benchmark-checklist for performance and retain evidence with the number.\"\n  ],\n  \"expectedFull\": \"Before any speed claim, identify the measured work, sample method and limiting factor. Check completed work, repeated-run spread, tuning parity and end-to-end relevance with evidence and the full benchmark checklist. Withhold the 4x claim if evidence does not support it.\",\n  \"expectedReduced\": \"When new runs or profiles are unavailable, inspect supplied evidence, identify known work and sampling details, list unresolved alternative explanations and state that the limiter and speed claim remain unverified. Do not replace runtime evidence with a code-reading guess.\",\n  \"expectedBlocked\": \"If neither measurements nor inspection are available or authorized, state that the speed claim cannot be verified and request the missing run count, spread, completed-work evidence and runtime limiter evidence.\",\n  \"forbiddenClaims\": [\n    \"One plausible number establishes a speedup.\",\n    \"A source-reading guess proves the limiter.\",\n    \"Failed or cached requests prove faster completed work.\",\n    \"Static package validation establishes host behavior.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/misleading-speedup.result.md",
      "sha256": "f08aacaf86508fac0a0a38de98b0a27936dd74561aedebcc656791f1e86d4716",
      "bytes": 6135,
      "owners": [
        "grades-native-03.json#2"
      ],
      "text": "# misleading-speedup\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"misleading-speedup\",\n  \"prompt\": \"A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?\",\n  \"requirements\": [\n    \"Identify the measured work and whether every request completed it.\",\n    \"Identify the sample method, run count and spread.\",\n    \"Name the limiting resource or code path using profiles or counters from a run and map it to source.\",\n    \"Rule out errors, skipped or cached work, an untuned side, noise and end-to-end irrelevance with evidence.\",\n    \"Use benchmark-checklist for performance and retain evidence with the number.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-explain-the-number/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 6. See [source-reads.json](misleading-speedup/source-reads.json). Supplied input archive: [supplied-input.json](misleading-speedup/supplied-input.json).\n\n## Actual response and variants\n\nNo. The 4x speedup is inconclusive and must not be reported as an established improvement. The only supplied measurement is a scenario statement about one run. Some requests failed, and cache hits were not counted. There are no raw timings or parser revisions to inspect.\n\nI read the full installed benchmark-checklist and applied every report gate below. The prepared runtime.mjs is a synthetic array/sum loop, not the parser or its before/after harness. I inspected it but did not run an unrelated workload and label it parser evidence.\n\n| Evidence gate | Actual finding |\n| --- | --- |\n| Measured work | Allegedly parser requests. Dataset, request count, data size, concurrency, timed region, result consumption, exact revisions and configurations are unknown. |\n| Completed work and errors | Prompt says some requests failed. Error counts, retries, timeouts, success counts and output correctness are not supplied. Not every request completed valid work. |\n| Sampling | One reported run. Collection method, per-side count, warmup, median and range are unknown. A one-run observation supplies no repeatability evidence. |\n| Limiter | No profile or runtime counter artifact supplied. No resource or source line can be named as an observed limiter. Source-reading guesses would not satisfy this gate. |\n| Cache/skipped work | Cache hits were not counted. Equal completed parser work between sides is unverified. |\n| Tuning parity and contention | No production settings, flags, cache policy, release builds, machine load or core count evidence. Unknown, not ruled out. |\n| Physical limits | No bytes, operations or parser time share. A 4x overall speedup would require eliminating at least 75% of original elapsed work under a fixed-work serial model. The necessary share was not measured. This is arithmetic, not a runtime result. |\n| End-to-end relevance | No user-path latency measurement or parser time share supplied. Microbenchmark relevance is unverified. |\n\nBefore any new performance claim, retain a harness that validates results and counts attempted, succeeded, failed, retried, timed-out and cached requests plus actual parser invocations in the timed region. Fix correctness failures first. Use identical data, concurrency, revisions and tuned production configurations. Separate cold and warm cache tests. Check contention and core count, then alternate A/B for at least five measured runs per side after controlled warmup. Keep every raw timing, median and range. Profile separately from reportable runs and map the limiter to exact source lines. Measure the end-to-end path and parser share alongside the microbenchmark. Apply physical-limit arithmetic to the measured work.\n\nVariant attempted: supplied one-run assessment only. New relevant runs are blocked by absent parser code, revisions, harness and raw data, even though local execution is available. No measurements, profiles, limiter, spread or speedup were fabricated. The 4x text remains only an unverified supplied claim.\n\n## Real command results\n\nNo case-specific product command was run. Source reads, inert preparation and output persistence used the setup/report scripts through the actual tools named above.\n\n## Artifacts\n\n- [misleading-speedup/input/runtime.mjs](misleading-speedup/input/runtime.mjs)\n- [misleading-speedup/response.md](misleading-speedup/response.md)\n- [misleading-speedup/source-reads.json](misleading-speedup/source-reads.json)\n- [misleading-speedup/supplied-input.json](misleading-speedup/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-03/misleading-speedup/input",
      "owner": "grades-native-03.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup/source",
      "owner": "grades-native-03.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup/source-reads.json",
      "owner": "grades-native-03.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup/input",
      "owner": "grades-native-03.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup/source",
      "owner": "grades-native-03.json#2",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/misleading-speedup/source-reads.json",
      "owner": "grades-native-03.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
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
