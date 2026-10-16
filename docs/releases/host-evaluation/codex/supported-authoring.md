# codex: supported-authoring

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "supported-authoring",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-11.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.",
  "caseDefinition": {
    "id": "supported-authoring",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md"
    ],
    "prompt": "Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.",
    "requirements": [
      "Inspect exposed capabilities and the available authoring workflow instructions and actual validator before use; identify the missing create-skill dependency.",
      "Preserve voice ownership, decision-changing prose, confusing-rule explanations, scope-matched tone, structural-source pointers, path delegation and proposals for recurring uncaptured workflows.",
      "Check name and description frontmatter, referenced files and cross-skill links; run structural test cases with fixtures and skip subjective tests.",
      "Apply Opening a PR only when its dependency, capabilities and authorization permit; preserve the skill artifact when PR delivery is deferred.",
      "Reply with skill summary, key design decisions and validation notes; distinguish observed results from unknown trigger performance."
    ],
    "expectedFull": "An available supported authoring workflow runs after its instructions and validator are inspected. The authored skill passes the observed structural checks and structural test cases. Subjective tests are skipped. The reply identifies the actual workflow, states create-skill is absent unless discovered, leaves unknown trigger performance unverified and reports observed authorized PR delivery or its explicit deferral.",
    "expectedReduced": "With authorized writes but no supported authoring workflow, produce only a provisional skill draft and manual checklist. Preserve the missing create-skill block, unexecuted validation and unknown trigger performance. If authoring and validation succeed but PR delivery is unavailable, retain the validated local skill and report the deferred PR dependency.",
    "expectedBlocked": "Without an available authoring workflow and without authorization or capability for a provisional draft, report the missing create-skill dependency and unavailable operation. Unavailable validation or PR delivery remains explicitly blocked or deferred; no completion claim substitutes for it.",
    "forbiddenClaims": [
      "create-skill shipped or executed without discovery and observed evidence.",
      "A provisional draft or manual checklist proves supported authoring execution or validator success.",
      "Structural checks prove trigger performance, subjective quality or host behavioral parity.",
      "A PR was created, commits made or external writes performed without authorization and observed results.",
      "Path delegation to another skill proves independent worker execution."
    ],
    "caseFile": "docs/parity/cases/playbooks/authoring-a-skill.json"
  },
  "registry": {
    "caseId": "supported-authoring",
    "caseFile": "docs/parity/cases/playbooks/authoring-a-skill.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md"
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
      "attemptId": "grades-native-11.json#3",
      "order": 0,
      "gradeFile": "grades-native-11.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "supported-authoring",
      "status": "reduced-pass",
      "grade": {
        "caseId": "supported-authoring",
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
          "Available authorized supported authoring workflow and its observed validator",
          "Trigger/discovery behavior remains unverified"
        ],
        "review": "A genuinely retained provisional draft and manual checker distinguish themselves from supported authoring/validation. Actual custom structural variants reject missing metadata/links and invalid names. The supported companion lies outside allowed package source scope and no trigger performance or publication is claimed.",
        "responseArtifact": "fixtures/batch-11/supported-authoring.result.md",
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
          "item_25",
          "item_26",
          "item_27",
          "item_30",
          "item_31",
          "item_37",
          "item_40"
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
        "fullExpected": "An available supported authoring workflow runs after its instructions and validator are inspected. The authored skill passes the observed structural checks and structural test cases. Subjective tests are skipped. The reply identifies the actual workflow, states create-skill is absent unless discovered, leaves unknown trigger performance unverified and reports observed authorized PR delivery or its explicit deferral.",
        "reducedExpected": "With authorized writes but no supported authoring workflow, produce only a provisional skill draft and manual checklist. Preserve the missing create-skill block, unexecuted validation and unknown trigger performance. If authoring and validation succeed but PR delivery is unavailable, retain the validated local skill and report the deferred PR dependency.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# supported-authoring\n\nThe local artifact is a provisional fixture-review skill. The required supported authoring workflow could not run within the permitted package boundary. The case-owned structural checker found no errors in the draft and rejected five intentionally invalid variants. This does not establish supported-validator success or trigger performance.\n\n## Supplied input\n\n\"Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.\"\n\nThe complete supplied contract is retained in [supported-authoring/input.json](supported-authoring/input.json). Task input revision `69a848296f870402cb15b85e93dff671fa32059d` was independently resolved with Git. `git ls-tree` identified committed task-contracts.json and committed-inputs/README.md. The scoped diff against that revision was empty. The copied README is synthetic input, not evidence of a service contact.\n\nRequested package source freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`, distinct from the input revision. Reads used only `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0`. Its manifest reports version 0.1.0. The installed directory has no accessible Git repository, so the source freeze cannot be independently established from Git there. Exact read bytes and SHA-256 identities are retained in source-reads.json. No source from version 0.2.1 was used.\n\n## Actual response and artifact\n\nCreated [supported-authoring/draft/SKILL.md](supported-authoring/draft/SKILL.md) and its [record contract](supported-authoring/draft/references/record-contract.md). No particular target skill or behavior was supplied, so the bounded draft reviews disposable fixture sources and preserves provenance in a local report.\n\nThe draft keeps direct, narrow instructions. Required report fields belong in the record contract. Execution-path explanations delegate by an explicit path to the existing how skill. The note about original input identity explains a confusing provenance boundary. No delegated worker execution is claimed from that pointer. The draft was reread after creation.\n\ncreate-skill is not shipped by the package, as both its actual authoring playbook and skill inventory show. The host exposes a separate skill-creator entry, but its instructions and validator are outside the user's allowed package root. It was not read or invoked. The package's complete tools/validate_package.py was inspected. It validates package inventory, metadata, links and cases, and is not a standalone authoring workflow. It was not run against the draft.\n\nThe authorized fallback therefore used the playbook's provisional-draft route. The case-owned manual-structure.mjs was inspected before execution and explicitly labels itself as a custom checker. The supported authoring workflow and its validator remain unavailable within this task's source boundary.\n\n## Observed structural variants\n\n| Variant | Actual checker result |\n| --- | --- |\n| Authored draft | No errors |\n| Name removed | name missing or empty |\n| Description removed | description missing or empty |\n| Missing referenced file | missing target reported |\n| Broken cross-skill pointer | missing target reported |\n| Invalid skill name | name syntax reported |\n\n`bun supported-authoring/manual-structure.mjs` exited 0. Its output is retained in [structural-run.json](supported-authoring/structural-run.json). That exit means the six checker fixtures produced the intended checker observations. It is not a grade for this workflow case. The checker supports limited plain frontmatter and inline file links only. It is not a YAML or Markdown parser.\n\nThe manual checklist confirms the name and description, reference existence and cross-skill link destination. Subjective tests were skipped. Trigger quality, automatic discovery, behavioral compliance and independent-worker behavior were not tested. No supported validator result is claimed.\n\n## Actual tools, evidence and limits\n\nRead operations used functions.exec and tools.exec_command with cat, sed, rg and Git. Bun's prepare.mjs retained exact source reads and their hashes, copied the synthetic README, captured Git and runtime command results, and wrote the provisional draft. tools.apply_patch created only owned case files. The checker ran through Bun. All invoked scripts were Bun scripts. No dependency was installed.\n\nArtifacts are [source-reads.json](supported-authoring/source-reads.json), [command-results.json](supported-authoring/command-results.json), [prepare.mjs](supported-authoring/prepare.mjs), [manual-structure.mjs](supported-authoring/manual-structure.mjs), [manual-checklist.md](supported-authoring/manual-checklist.md), [capabilities.json](supported-authoring/capabilities.json), and the draft and structural output above.\n\nOpening a PR was read, but delivery is deferred. External writes, commits, branches, configuration changes and publishing are expressly forbidden. Its external deslop dependency is also not shipped in the allowed package. No PR delivery gate was bypassed and no forge call occurred. The draft remains available locally.\n\nNo additional negative capability variants were specifically requested for this case. The actual missing supported authoring dependency and actual denied external authorization were exercised as boundaries. No host-enforced write denial was simulated or claimed. Local writes and execution were available and observed. No subjective tests or trigger measurements were fabricated.\n",
        "artifact": {
          "path": "fixtures/batch-11/supported-authoring.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring.result.md",
          "sha256": "84fddb7cefa7070335c7bcb10c608cf0e257324c5d3d3fbfee42fb766128a965",
          "bytes": 5672
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
      "path": "fixtures/batch-11/supported-authoring/capabilities.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/capabilities.json",
      "sha256": "ba13586829416bfb41af1cce453b298b599f8efa98ddd28d09eef1ed1f81264c",
      "bytes": 1275,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "{\n  \"operationBindings\": [\n    {\"operation\":\"read\",\"tool\":\"functions.exec / tools.exec_command\",\"exposed\":true,\"succeeded\":true,\"evidence\":\"source-reads.json\",\"limits\":\"Package source restricted to the requested installed root; no alternate authoring package read.\"},\n    {\"operation\":\"execution\",\"tool\":\"functions.exec / tools.exec_command\",\"exposed\":true,\"succeeded\":true,\"evidence\":\"structural-run.json\",\"limits\":\"Bun ran a case-owned checker, not a supported authoring validator.\"},\n    {\"operation\":\"isolated-write\",\"tool\":\"functions.exec / tools.apply_patch\",\"exposed\":true,\"succeeded\":true,\"evidence\":\"draft/SKILL.md\",\"limits\":\"Provisional local artifact only.\"},\n    {\"operation\":\"supported-authoring\",\"tool\":null,\"exposed\":false,\"succeeded\":false,\"evidence\":\"manual-checklist.md\",\"limits\":\"create-skill is absent from the package. A separate host skill-creator is listed but its source lies outside the user's allowed package root and was not read or invoked.\"},\n    {\"operation\":\"external-write\",\"tool\":null,\"exposed\":false,\"succeeded\":false,\"evidence\":\"../supported-authoring.result.md\",\"limits\":\"Forbidden by task authorization. No forge operation attempted.\"}\n  ],\n  \"modelRequested\":\"inherited\",\n  \"actualModel\":\"unknown\",\n  \"workersSpawnedForThisCase\":false\n}\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/command-results.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/command-results.json",
      "sha256": "a482330c722e203344fc4f6f95f8167b94f508e03375df438125389af8976141",
      "bytes": 17881,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "[\n  {\n    \"command\": [\n      \"git\",\n      \"rev-parse\",\n      \"69a848296f870402cb15b85e93dff671fa32059d^{commit}\"\n    ],\n    \"exit\": 0,\n    \"stdout\": \"69a848296f870402cb15b85e93dff671fa32059d\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"git\",\n      \"ls-tree\",\n      \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"task-contracts.json\",\n      \"committed-inputs/README.md\"\n    ],\n    \"exit\": 0,\n    \"stdout\": \"100644 blob 7b2943d8f74232b5f67dec8de8f163493defba64\\tcommitted-inputs/README.md\\n100644 blob c403cf676d00a04b334b5a0818efcad4b5a97725\\ttask-contracts.json\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"git\",\n      \"diff\",\n      \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"--\",\n      \"task-contracts.json\",\n      \"committed-inputs/README.md\"\n    ],\n    \"exit\": 0,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"exit\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"rg\",\n      \"--files\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills\"\n    ],\n    \"exit\": 0,\n    \"stdout\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-type-system-discipline/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-separate-before-serializing-shared-state/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/tdd/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/unslop/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-experience-first/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-laziness-protocol/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/no-comments/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/create-verification-skill/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/create-verification-skill/references/feature-map-example/README.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/create-verification-skill/references/feature-map-example/create-note.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/create-verification-skill/references/feature-map-example/search.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-attack-the-premise/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/arena/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/teach/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/automate-me/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-exhaust-the-design-space/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-minimize-reader-load/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-redesign-from-first-principles/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-never-block-on-the-human/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/architect/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/architect/references/runner-prompt.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/architect/references/rationale-template.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/architect/references/design-red-flags.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/make-bot-ui/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-outcome-oriented-execution/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/typescript-best-practices/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/maintain-verification-skill/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/benchmark-checklist/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-explain-the-number/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/references/recipes.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-help/references/prompting.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/blast-radius/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-model-the-domain/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/recall/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-test-behavior-not-implementation/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/bro/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/source-playbook.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/synthesizer-prompt.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/typescript-best-practices/references/patterns.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/investigator-prompt.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/figure-it-out/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/epistemics.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/setup-pstack/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/how/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/correct/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/code-archaeology.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/linear.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/sentry.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/databricks.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/notion.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/datadog.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/slack.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/why/references/sources/incident-postmortem.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-encode-lessons-in-structure/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-fix-root-causes/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/reviewer-prompt.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/code-quality-review.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/rubric.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/interrogate/references/lead-judgment.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/scripts/log.sh\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/swarm/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-boundary-discipline/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/technical-writing/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/how/references/explainer-prompt.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/how/references/explorer-prompt.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-make-operations-idempotent/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-sequence-verifiable-units/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-subtract-before-you-add/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-build-the-lever/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-foundational-thinking/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/show-me-your-work/references/decision-log-template.tsv\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/SKILL.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/divergent-reviewer.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/tooling-reviewer.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/judgment-reviewer.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/reflect/references/synthesizer.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/references/bugbot-triage.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/package.json\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bun.lock\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/worktree-audit.py\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/store.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/orch/orch.test.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/worktree-audit.sh\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/check-plan.mjs\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/bootstrap.test.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/cli.test.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/render.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/tsconfig.json\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/policy.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/types.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/github.test.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/cli.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/types.compile.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/github.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/policy.test.ts\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/scripts/watch-pr/watch-pr\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/refactoring.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/runtime-forensics.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/perf-issue.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/visual-parity.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/feature.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/orchestrate.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/babysit.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/autopilot-stack.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/pause-safely.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/hillclimb.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/autopilot-full.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/opening-a-pr.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/worktree-cleanup.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/investigation.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/prototype.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/eval.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/authoring-a-skill.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/autonomous-run.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/multi-phase-plan.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/trace-forensics.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/shipping.md\\n/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/bug-fix.md\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"git\",\n      \"-C\",\n      \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n      \"rev-parse\",\n      \"--show-toplevel\"\n    ],\n    \"exit\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/draft/SKILL.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/draft/SKILL.md",
      "sha256": "eb3af7ccbb22a7f1369e0e190b3b09494db3c824f3ec97a49f0f685b3d21786e",
      "bytes": 1197,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "---\nname: fixture-review\ndescription: \"Use when asked to review a disposable local fixture at a supplied revision and retain a bounded report without changing its source.\"\n---\n\n# Review a local fixture\n\nRead the supplied revision and file slice. Copy any required inputs into the owned output directory before edits. Record the original file identity separately from generated reports.\n\nUse [the record contract](references/record-contract.md) for required report fields. Read the actual source before stating a finding. Preserve unknown links as gaps.\n\nFor an execution-path explanation, delegate by path to [how](/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/how/SKILL.md). Read that contract before execution. A path pointer does not establish that a worker ran.\n\nKeep writes inside the assigned output directory. Do not contact services, install dependencies, change settings, or create a commit or PR. A fixture proves only its own observed result.\n\nReturn the finding, its file and line, the command result when execution was authorized, and any missing proof. Report trigger performance as unknown until a separate trigger evaluation observes it.\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/draft/references/record-contract.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/draft/references/record-contract.md",
      "sha256": "92141a2ffe99c29f736733443bd5e0c009067795cc67e702dca5811ab9285ea5",
      "bytes": 379,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "# Fixture report record\n\nRequired fields are inputRevision, inputPath, inputSha256, finding, sourceLocation, commandResult and limits. Use null for commandResult when no command ran. Keep the original input identity in the report when a copied file changes.\n\nThe supplied Git revision identifies synthetic inputs. It does not identify the installed package or generated outputs.\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/manual-checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/manual-checklist.md",
      "sha256": "fcea1d327e9d0a11cb0308749e4949eced6b13f28f9def47e92a118160c23ec3",
      "bytes": 1445,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "# Manual authoring checklist\n\n- The draft has nonempty name and description fields. Its name is fixture-review.\n- Its local record-contract.md exists. The cross-skill how pointer resolves in the permitted package root.\n- The authoring playbook owns the voice. The draft uses direct instructions, and keeps the input/output identity explanation because confusing the two would change provenance claims.\n- Required record fields live in the record contract. The draft delegates execution-path explanations by skill path instead of restating that skill.\n- Only the local draft and case evidence were written. Installation and PR delivery were not performed.\n- Six structural fixtures exercised the case-owned checker. This manual check and checker are not the missing create-skill workflow or a supported authoring validator.\n- Subjective tests were skipped. Trigger performance, automatic skill discovery, host compliance and actual delegated execution remain unknown.\n- No recurring uncaptured workflow was observed in this isolated case. If repeated fixture provenance reviews become a workflow, propose adoption of fixture-review and its record checker separately. This draft does not install that workflow.\n\nThe package's tools/validate_package.py was read in full. It expects package inventories, adaptation metadata and package-contained links. It is not a standalone skill-authoring validator, so it was not repurposed or presented as one.\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/manual-structure.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/manual-structure.mjs",
      "sha256": "dee01938394fffb1a17a706c581d59863109512595a04c6e18ab3434bceb176e",
      "bytes": 2015,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "// Case-owned checker. This is not a supported authoring validator.\nimport {readFile,stat,writeFile} from 'node:fs/promises';\nimport {resolve,dirname} from 'node:path';\nconst root=resolve('supported-authoring');\nexport async function check(text,file){\n const errors=[];\n const fm=text.match(/^---\\n([\\s\\S]*?)\\n---(?:\\n|$)/)?.[1];\n if(!fm) errors.push('frontmatter missing');\n for(const key of ['name','description'])if(!new RegExp('^'+key+':\\\\s*\\\\S.+$','m').test(fm??''))errors.push(key+' missing or empty');\n const name=fm?.match(/^name:\\s*(.*)$/m)?.[1];\n if(name&&!/^[a-z][a-z0-9-]*$/.test(name))errors.push('name syntax');\n for(const match of text.matchAll(/\\[[^\\]]*\\]\\(([^)]+)\\)/g)){\n  const target=match[1];if(/^[a-z]+:\\/\\//i.test(target)||target.startsWith('#'))continue;\n  try{if(!(await stat(resolve(dirname(file),target.split('#')[0]))).isFile()) errors.push('not a file: '+target);}catch{errors.push('missing target: '+target);}\n }\n return errors;\n}\nconst file=resolve(root,'draft/SKILL.md'),text=await readFile(file,'utf8');\nconst cases=[\n ['authored draft',text,0],\n ['missing name',text.replace(/^name:.*\\n/m,''),1],\n ['missing description',text.replace(/^description:.*\\n/m,''),1],\n ['missing referenced file',text+'\\n[missing](references/absent.md)\\n',1],\n ['broken cross-skill link',text.replace('/skills/how/SKILL.md','/skills/no-such-skill/SKILL.md'),1],\n ['invalid name',text.replace('name: fixture-review','name: INVALID NAME'),1],\n];\nconst results=[];for(const [label,input,wanted]of cases){const errors=await check(input,file);results.push({label,expectedErrorCount:wanted,observedErrors:errors,matchedExpected:errors.length===wanted});}\nconsole.log(JSON.stringify({checker:'case-owned manual-structure.mjs, not supported validator',results,limitations:['Limited plain frontmatter and inline Markdown links only; not a YAML or Markdown parser.','No trigger, subjective quality, installed discovery or host behavioral checks.']},null,2));\nprocess.exit(results.every(x=>x.matchedExpected)?0:1);\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/prepare.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/prepare.mjs",
      "sha256": "99d6048931718bab8152b1429eea9ed372ffcf75abeb377d98598672a2913d4b",
      "bytes": 3561,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "import {mkdir, readFile, writeFile, copyFile} from 'node:fs/promises';\nimport {join} from 'node:path';\nconst root=process.cwd(), out=join(root,'supported-authoring');\nconst pkg='/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nawait mkdir(join(out,'draft/references'),{recursive:true});\nawait mkdir(join(out,'inputs'),{recursive:true});\nconst contract=JSON.parse(await readFile(join(root,'task-contracts.json'),'utf8')).find(x=>x.id==='supported-authoring');\nawait writeFile(join(out,'input.json'),JSON.stringify(contract,null,2)+'\\n');\nawait copyFile(join(root,'committed-inputs/README.md'),join(out,'inputs/README.md'));\nconst sources=[...contract.sourcePaths,'references/host-capabilities.md','references/workflow-ownership.md','skills/unslop/SKILL.md','tools/validate_package.py'];\nconst reads=[];\nfor(const path of sources){const body=await readFile(join(pkg,path),'utf8');reads.push({path:join(pkg,path),sha256:new Bun.CryptoHasher('sha256').update(body).digest('hex'),body});}\nawait writeFile(join(out,'source-reads.json'),JSON.stringify(reads,null,2)+'\\n');\nconst commands=[['git','rev-parse','69a848296f870402cb15b85e93dff671fa32059d^{commit}'],['git','ls-tree','69a848296f870402cb15b85e93dff671fa32059d','task-contracts.json','committed-inputs/README.md'],['git','diff','69a848296f870402cb15b85e93dff671fa32059d','--','task-contracts.json','committed-inputs/README.md'],['bun','--version'],['rg','--files',join(pkg,'skills')],['git','-C',pkg,'rev-parse','--show-toplevel']];\nconst results=commands.map(command=>{const r=Bun.spawnSync(command,{cwd:root});return {command,exit:r.exitCode,stdout:r.stdout.toString(),stderr:r.stderr.toString()};});\nawait writeFile(join(out,'command-results.json'),JSON.stringify(results,null,2)+'\\n');\nawait writeFile(join(out,'draft/SKILL.md'),`---\nname: fixture-review\ndescription: \"Use when asked to review a disposable local fixture at a supplied revision and retain a bounded report without changing its source.\"\n---\n\n# Review a local fixture\n\nRead the supplied revision and file slice. Copy any required inputs into the owned output directory before edits. Record the original file identity separately from generated reports.\n\nUse [the record contract](references/record-contract.md) for required report fields. Read the actual source before stating a finding. Preserve unknown links as gaps.\n\nFor an execution-path explanation, delegate by path to [how](${pkg}/skills/how/SKILL.md). Read that contract before execution. A path pointer does not establish that a worker ran.\n\nKeep writes inside the assigned output directory. Do not contact services, install dependencies, change settings, or create a commit or PR. A fixture proves only its own observed result.\n\nReturn the finding, its file and line, the command result when execution was authorized, and any missing proof. Report trigger performance as unknown until a separate trigger evaluation observes it.\n`);\nawait writeFile(join(out,'draft/references/record-contract.md'),`# Fixture report record\n\nRequired fields are inputRevision, inputPath, inputSha256, finding, sourceLocation, commandResult and limits. Use null for commandResult when no command ran. Keep the original input identity in the report when a copied file changes.\n\nThe supplied Git revision identifies synthetic inputs. It does not identify the installed package or generated outputs.\n`);\nconsole.log(JSON.stringify({sourcesRead:reads.length,commands:results.map(x=>({command:x.command,exit:x.exit})),draft:'supported-authoring/draft/SKILL.md'},null,2));\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/structural-run.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring/structural-run.json",
      "sha256": "ca1d1d402c317d00728b7810d0637d2f237d6b3af438d4970c0a00f4c42bdb3b",
      "bytes": 1705,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"supported-authoring/manual-structure.mjs\"\n  ],\n  \"exit\": 0,\n  \"stdout\": \"{\\n  \\\"checker\\\": \\\"case-owned manual-structure.mjs, not supported validator\\\",\\n  \\\"results\\\": [\\n    {\\n      \\\"label\\\": \\\"authored draft\\\",\\n      \\\"expectedErrorCount\\\": 0,\\n      \\\"observedErrors\\\": [],\\n      \\\"matchedExpected\\\": true\\n    },\\n    {\\n      \\\"label\\\": \\\"missing name\\\",\\n      \\\"expectedErrorCount\\\": 1,\\n      \\\"observedErrors\\\": [\\n        \\\"name missing or empty\\\"\\n      ],\\n      \\\"matchedExpected\\\": true\\n    },\\n    {\\n      \\\"label\\\": \\\"missing description\\\",\\n      \\\"expectedErrorCount\\\": 1,\\n      \\\"observedErrors\\\": [\\n        \\\"description missing or empty\\\"\\n      ],\\n      \\\"matchedExpected\\\": true\\n    },\\n    {\\n      \\\"label\\\": \\\"missing referenced file\\\",\\n      \\\"expectedErrorCount\\\": 1,\\n      \\\"observedErrors\\\": [\\n        \\\"missing target: references/absent.md\\\"\\n      ],\\n      \\\"matchedExpected\\\": true\\n    },\\n    {\\n      \\\"label\\\": \\\"broken cross-skill link\\\",\\n      \\\"expectedErrorCount\\\": 1,\\n      \\\"observedErrors\\\": [\\n        \\\"missing target: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/no-such-skill/SKILL.md\\\"\\n      ],\\n      \\\"matchedExpected\\\": true\\n    },\\n    {\\n      \\\"label\\\": \\\"invalid name\\\",\\n      \\\"expectedErrorCount\\\": 1,\\n      \\\"observedErrors\\\": [\\n        \\\"name syntax\\\"\\n      ],\\n      \\\"matchedExpected\\\": true\\n    }\\n  ],\\n  \\\"limitations\\\": [\\n    \\\"Limited plain frontmatter and inline Markdown links only; not a YAML or Markdown parser.\\\",\\n    \\\"No trigger, subjective quality, installed discovery or host behavioral checks.\\\"\\n  ]\\n}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-11/supported-authoring.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/supported-authoring.result.md",
      "sha256": "84fddb7cefa7070335c7bcb10c608cf0e257324c5d3d3fbfee42fb766128a965",
      "bytes": 5672,
      "owners": [
        "grades-native-11.json#3"
      ],
      "text": "# supported-authoring\n\nThe local artifact is a provisional fixture-review skill. The required supported authoring workflow could not run within the permitted package boundary. The case-owned structural checker found no errors in the draft and rejected five intentionally invalid variants. This does not establish supported-validator success or trigger performance.\n\n## Supplied input\n\n\"Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.\"\n\nThe complete supplied contract is retained in [supported-authoring/input.json](supported-authoring/input.json). Task input revision `69a848296f870402cb15b85e93dff671fa32059d` was independently resolved with Git. `git ls-tree` identified committed task-contracts.json and committed-inputs/README.md. The scoped diff against that revision was empty. The copied README is synthetic input, not evidence of a service contact.\n\nRequested package source freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`, distinct from the input revision. Reads used only `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0`. Its manifest reports version 0.1.0. The installed directory has no accessible Git repository, so the source freeze cannot be independently established from Git there. Exact read bytes and SHA-256 identities are retained in source-reads.json. No source from version 0.2.1 was used.\n\n## Actual response and artifact\n\nCreated [supported-authoring/draft/SKILL.md](supported-authoring/draft/SKILL.md) and its [record contract](supported-authoring/draft/references/record-contract.md). No particular target skill or behavior was supplied, so the bounded draft reviews disposable fixture sources and preserves provenance in a local report.\n\nThe draft keeps direct, narrow instructions. Required report fields belong in the record contract. Execution-path explanations delegate by an explicit path to the existing how skill. The note about original input identity explains a confusing provenance boundary. No delegated worker execution is claimed from that pointer. The draft was reread after creation.\n\ncreate-skill is not shipped by the package, as both its actual authoring playbook and skill inventory show. The host exposes a separate skill-creator entry, but its instructions and validator are outside the user's allowed package root. It was not read or invoked. The package's complete tools/validate_package.py was inspected. It validates package inventory, metadata, links and cases, and is not a standalone authoring workflow. It was not run against the draft.\n\nThe authorized fallback therefore used the playbook's provisional-draft route. The case-owned manual-structure.mjs was inspected before execution and explicitly labels itself as a custom checker. The supported authoring workflow and its validator remain unavailable within this task's source boundary.\n\n## Observed structural variants\n\n| Variant | Actual checker result |\n| --- | --- |\n| Authored draft | No errors |\n| Name removed | name missing or empty |\n| Description removed | description missing or empty |\n| Missing referenced file | missing target reported |\n| Broken cross-skill pointer | missing target reported |\n| Invalid skill name | name syntax reported |\n\n`bun supported-authoring/manual-structure.mjs` exited 0. Its output is retained in [structural-run.json](supported-authoring/structural-run.json). That exit means the six checker fixtures produced the intended checker observations. It is not a grade for this workflow case. The checker supports limited plain frontmatter and inline file links only. It is not a YAML or Markdown parser.\n\nThe manual checklist confirms the name and description, reference existence and cross-skill link destination. Subjective tests were skipped. Trigger quality, automatic discovery, behavioral compliance and independent-worker behavior were not tested. No supported validator result is claimed.\n\n## Actual tools, evidence and limits\n\nRead operations used functions.exec and tools.exec_command with cat, sed, rg and Git. Bun's prepare.mjs retained exact source reads and their hashes, copied the synthetic README, captured Git and runtime command results, and wrote the provisional draft. tools.apply_patch created only owned case files. The checker ran through Bun. All invoked scripts were Bun scripts. No dependency was installed.\n\nArtifacts are [source-reads.json](supported-authoring/source-reads.json), [command-results.json](supported-authoring/command-results.json), [prepare.mjs](supported-authoring/prepare.mjs), [manual-structure.mjs](supported-authoring/manual-structure.mjs), [manual-checklist.md](supported-authoring/manual-checklist.md), [capabilities.json](supported-authoring/capabilities.json), and the draft and structural output above.\n\nOpening a PR was read, but delivery is deferred. External writes, commits, branches, configuration changes and publishing are expressly forbidden. Its external deslop dependency is also not shipped in the allowed package. No PR delivery gate was bypassed and no forge call occurred. The draft remains available locally.\n\nNo additional negative capability variants were specifically requested for this case. The actual missing supported authoring dependency and actual denied external authorization were exercised as boundaries. No host-enforced write denial was simulated or claimed. Local writes and execution were available and observed. No subjective tests or trigger measurements were fabricated.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-11/supported-authoring/input.json",
      "owner": "grades-native-11.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/inputs",
      "owner": "grades-native-11.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/source-reads.json",
      "owner": "grades-native-11.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/input.json",
      "owner": "grades-native-11.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/inputs",
      "owner": "grades-native-11.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-11/supported-authoring/source-reads.json",
      "owner": "grades-native-11.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
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
