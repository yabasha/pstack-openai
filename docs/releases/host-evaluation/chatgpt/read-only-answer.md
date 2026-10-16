# chatgpt: read-only-answer

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "read-only-answer",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#22",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Using read-only fixture source files and decision records, explain how an invoice formatter works, why a rounding boundary exists, whether the premise that all errors are swallowed is correct, and recommend one of two alternatives with tradeoffs. Permit fixture reads only. No product build, prototype, edits, commits or external writes. Repeat with independent workers unavailable, historical sources denied and all relevant source reads unavailable.",
  "caseDefinition": {
    "id": "read-only-answer",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/investigation.md",
      "skills/poteto-mode/SKILL.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md",
      "skills/unslop/SKILL.md",
      "skills/architect/SKILL.md",
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/playbooks/feature.md"
    ],
    "prompt": "Using read-only fixture source files and decision records, explain how an invoice formatter works, why a rounding boundary exists, whether the premise that all errors are swallowed is correct, and recommend one of two alternatives with tradeoffs. Permit fixture reads only. No product build, prototype, edits, commits or external writes. Repeat with independent workers unavailable, historical sources denied and all relevant source reads unavailable.",
    "requirements": [
      "Read complete mode, Investigation, how, conditional why and routed prompts. Preserve read-only roles and inspect actual findings and citations.",
      "Keep exactly throughput checkpoint: n/a, read-only investigation. Explain with the how sections or deliver a recommendation and tradeoffs table without a build.",
      "Motivation uses why epistemic tiers, coverage and explicit unknowns. Contradict an incorrect premise with reasons; do not infer intent from implementation alone.",
      "Apply unslop. No PR, babysit or architect during the read-only answer. A future change returns to the user and routes Bug fix or Feature without starting implementation.",
      "Observe actual authorized source operations and any required independent workers. Inherit models unless supported selection is observed. Record denied and missing categories, disclose sequential reduced roles and block unsupported claims."
    ],
    "expectedFull": "Accessible inspected fixture sources support a cited explanation or recommendation and reasoned premise check. Authorized independent routed workers return inspected read-only findings when the route requires them. The exact checkpoint and required output appear. No product build, prototype or write begins. Motivation preserves confidence and source coverage.",
    "expectedReduced": "With independent workers unavailable, authorized sequential exploration and synthesis supplies a cited answer with reduced capability disclosed. Missing history or connectors narrows motivation claims and preserves exact gaps. No external authorization changes the read-only deliverable. Unknown observed models leave diversity unverified.",
    "expectedBlocked": "No authorized relevant source reads or missing required companions blocks the dependent answer. Denied historical reads prevent claims about unseen motivation. Required independent behavior remains unsupported under sequential fallback. A possible later code change returns to the user without starting writes.",
    "forbiddenClaims": [
      "Investigation requires a product build or prototype to answer accessible evidence.",
      "A read-only answer requires a PR, Babysit or architect without a subsequent change handoff.",
      "Sequential roles prove independent workers or parallel investigation.",
      "Requested models prove observed selection or diversity.",
      "Denied or unavailable sources were searched and returned no findings.",
      "Code mechanics proves author intent or an inference is a confirmed historical fact.",
      "Broad autonomy or handoff authorizes edits, commits, installs, credentials or external writes.",
      "Uninspected citations or delegated findings support a confirmed answer.",
      "Structural validation or fixture definitions prove either host passed."
    ],
    "caseFile": "docs/parity/cases/playbooks/investigation.json"
  },
  "registry": {
    "caseId": "read-only-answer",
    "caseFile": "docs/parity/cases/playbooks/investigation.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/investigation.md",
      "skills/poteto-mode/SKILL.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/why/SKILL.md",
      "skills/why/references/epistemics.md",
      "skills/why/references/investigator-prompt.md",
      "skills/why/references/source-playbook.md",
      "skills/why/references/synthesizer-prompt.md",
      "skills/why/references/sources/code-archaeology.md",
      "skills/why/references/sources/linear.md",
      "skills/why/references/sources/notion.md",
      "skills/why/references/sources/slack.md",
      "skills/why/references/sources/datadog.md",
      "skills/why/references/sources/sentry.md",
      "skills/why/references/sources/databricks.md",
      "skills/why/references/sources/incident-postmortem.md",
      "skills/unslop/SKILL.md",
      "skills/architect/SKILL.md",
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/playbooks/feature.md"
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
      "attemptId": "grades-chatgpt-01-04.json#22",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 22,
      "host": "chatgpt",
      "caseId": "read-only-answer",
      "status": "reduced-pass",
      "grade": {
        "caseId": "read-only-answer",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Full required routed independent exploration/synthesis",
          "Matching actual denial/withholding trials for negative variants"
        ],
        "review": "Source-grounded mechanics, premise refutation, motivation confidence, alternatives and exact read-only checkpoint are present. A real native invoice worker returned findings and was inspected, but the required broader how/why role fan-out was not completed. Denied-source and unavailable-worker branches are textual premises, not actual tool denials.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/result.json",
        "variantReview": [
          {
            "name": "source and independent worker",
            "reportedObservation": "attempted actual spawn/result",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "full how/why fanout roles",
            "reportedObservation": "blocked not all required assignments executed",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "no-worker variant",
            "reportedObservation": "attempted textual reduced-role response",
            "assessment": "textual-or-proposed-only",
            "actualDenialProven": false
          },
          {
            "name": "history-denied variant",
            "reportedObservation": "attempted textual epistemic limit; no real denial",
            "assessment": "textual-or-proposed-only",
            "actualDenialProven": false
          },
          {
            "name": "all-reads-unavailable variant",
            "reportedObservation": "blocked substantive answer by premise",
            "assessment": "blocked-or-partial",
            "actualDenialProven": false
          },
          {
            "name": "runtime output edge cases",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "future build route",
            "reportedObservation": "blocked no authorization; would return to user for Bug fix or Feature",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "Bun absent; no Node/Python substitution.",
          "No live external actions.",
          "No model identity/full Git task revision observed.",
          "Local artifacts retained; durable persistence unverified.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/playbooks/investigation.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence",
        "observedVersusReported": "Native worker existence supported by root observation and retained result/write artifacts; full method/revision/model proof remains limited."
      },
      "topLevelContext": {
        "gradingNotes": [
          "Independent contract review of original batches 01..04, not the evaluated model self-grade.",
          "Root independently observed actual native dispatches, reads and commands during a 21m31s turn; retained exact tool returns are model-captured and are not all independently verified.",
          "Early missing raw envelopes and host-render truncation remain evidence limits; artifact checks/aggregation and source availability do not reconstruct unseen tool output.",
          "Bun was absent in the cloud runtime. No JavaScript/Python substitute or proxy execution receives workflow credit; shell/jq preparation, source reading and artifact administration prove only those operations.",
          "Installed operative source freeze was independently byte-verified by root before this review. This is separate from unavailable actual task Git revision and does not invent a Git checkout.",
          "Canonical agents/*.md may map to installed references/agent-prompts/*.md. Failed old path followed by observed mapped fallback is legitimate, not automatically missing source.",
          "Two invented timestamp placeholders in another batch remain original errors despite appended corrections; neither is accepted as original runtime evidence.",
          "Text-only supplied draft/recipe branches can pass without runtime. Missing required implementation or execution stays reduced/blocked; an observed contract violation is fail."
        ]
      },
      "response": {
        "text": "Recommend alternative A, removing fixed and lastFormatted while retaining the finite check and direct toFixed(2) return, as a recommendation only. Overview: formatInvoice rejects nonfinite values, calls fixed(value), stores the two-decimal string in lastFormatted and returns it. formatRows maps row.total and maps empty input to []. Where things live: input/additional/invoice/formatter.mjs contains those functions; decision.md records the display contract. The premise that all errors are swallowed is false for inspected formatter code: no catch exists, so nonfinite errors propagate. The controller claim is direct fixture documentation, not observed controller runtime. Direct motivation: decision.md explicitly says the UI compares two-decimal strings and CSV imports formatRows, placing rounding at display boundary. Inference: A reduces reader cost. Unknown: real historical intent, customer records and uninspected consumers. Tradeoffs: A removes one-use indirection and hidden state with minimal interface change; B adds a stateful Formatter class and ownership semantics without an evidenced requirement. No edit, build, prototype, architect, PR or babysit occurred. An actual read-only native worker independently read the formatter/decision and returned findings that I inspected; required broader role fan-out was not completed. Variant without workers: apply the same evidence sequentially with reduced independence. Variant historical sources denied: explain mechanics only, and mark motivation unknown without using the denied record. Variant all relevant reads unavailable: block the substantive answer rather than infer content. These variants are scoped premises, not actual denied tool receipts.\nthroughput checkpoint: n/a, read-only investigation",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/result.json",
          "sha256": "075405c1f05dc1db9638340d49c6a44a0ed7a51ecce3758c7faae138bd8bbbd1",
          "bytes": 3308
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/checkpoint-tool.json",
            "sha256": "670a2c14d83c250d48f126dc3441653bc5a6fc2197f4fedecfe8b90a5f9e5296",
            "bytes": 770
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/required-companions-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/required-companions-tool.json",
            "sha256": "c821110b84d2270e05324a05fc8fb8387270bd8df8fb657592c9635d78974a0c",
            "bytes": 58320
          }
        ],
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/result.json",
      "sha256": "075405c1f05dc1db9638340d49c6a44a0ed7a51ecce3758c7faae138bd8bbbd1",
      "bytes": 3308,
      "owners": [
        "grades-chatgpt-01-04.json#22"
      ],
      "text": "{\n  \"caseId\": \"read-only-answer\",\n  \"batch\": \"batch-03\",\n  \"actualResponse\": \"Recommend alternative A, removing fixed and lastFormatted while retaining the finite check and direct toFixed(2) return, as a recommendation only. Overview: formatInvoice rejects nonfinite values, calls fixed(value), stores the two-decimal string in lastFormatted and returns it. formatRows maps row.total and maps empty input to []. Where things live: input/additional/invoice/formatter.mjs contains those functions; decision.md records the display contract. The premise that all errors are swallowed is false for inspected formatter code: no catch exists, so nonfinite errors propagate. The controller claim is direct fixture documentation, not observed controller runtime. Direct motivation: decision.md explicitly says the UI compares two-decimal strings and CSV imports formatRows, placing rounding at display boundary. Inference: A reduces reader cost. Unknown: real historical intent, customer records and uninspected consumers. Tradeoffs: A removes one-use indirection and hidden state with minimal interface change; B adds a stateful Formatter class and ownership semantics without an evidenced requirement. No edit, build, prototype, architect, PR or babysit occurred. An actual read-only native worker independently read the formatter/decision and returned findings that I inspected; required broader role fan-out was not completed. Variant without workers: apply the same evidence sequentially with reduced independence. Variant historical sources denied: explain mechanics only, and mark motivation unknown without using the denied record. Variant all relevant reads unavailable: block the substantive answer rather than infer content. These variants are scoped premises, not actual denied tool receipts.\\nthroughput checkpoint: n/a, read-only investigation\",\n  \"observedOperations\": [\n    \"named case and installed sources read using tools.exec_command\",\n    \"collaboration.spawn_agent returned /root/eval_01_04/invoice_readonly\",\n    \"worker FINAL_ANSWER received and inspected; not full required method\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/required-companions-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"source and independent worker\",\n      \"observation\": \"attempted actual spawn/result\"\n    },\n    {\n      \"name\": \"full how/why fanout roles\",\n      \"observation\": \"blocked not all required assignments executed\"\n    },\n    {\n      \"name\": \"no-worker variant\",\n      \"observation\": \"attempted textual reduced-role response\"\n    },\n    {\n      \"name\": \"history-denied variant\",\n      \"observation\": \"attempted textual epistemic limit; no real denial\"\n    },\n    {\n      \"name\": \"all-reads-unavailable variant\",\n      \"observation\": \"blocked substantive answer by premise\"\n    },\n    {\n      \"name\": \"runtime output edge cases\",\n      \"observation\": \"blocked Bun absent\"\n    },\n    {\n      \"name\": \"future build route\",\n      \"observation\": \"blocked no authorization; would return to user for Bug fix or Feature\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no Node/Python substitution.\",\n    \"No live external actions.\",\n    \"No model identity/full Git task revision observed.\",\n    \"Local artifacts retained; durable persistence unverified.\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/worker-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/worker-receipt.json",
      "sha256": "c9567d477586c2172d1158fb64fbf3f7398a84cca6a84a4c2783f7f659da3c17",
      "bytes": 2003,
      "owners": [
        "grades-chatgpt-01-04.json#22"
      ],
      "text": "{\n  \"tool\": \"collaboration.spawn_agent\",\n  \"arguments\": {\n    \"task_name\": \"invoice_readonly\",\n    \"message\": \"Read-only independent explorer for batch-03/read-only-answer. pstack owns workflow. Input revision actual fixture SHA unknown Git HEAD; files /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-03/cases/read-only-answer/input/additional/invoice/formatter.mjs and decision.md. Read those via actual tool; read installed skills/how/SKILL.md and why/references/epistemics.md at /root/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Return precise workings, error handling premise, motivation epistemic tiers, alternative tradeoffs. NO writes of any kind, no commands executing JS, no external services, no Slack writes including SendSlackMessage/PostToSlack/chat.postMessage, no credentials. Report exact tools and output evidence. Inherit model, actual identity unknown. Single read-only assignment; parent captures your returned result. Bound scope these four files only.\"\n  },\n  \"result\": {\n    \"task_name\": \"/root/eval_01_04/invoice_readonly\"\n  },\n  \"inspectedFinalResponse\": \"Formatter rejects nonfinite amounts, uses fixed(value) -> value.toFixed(2), assigns lastFormatted and returns it. formatRows maps total and empty input to []. Errors propagate; controller assertion is fixture documentation only. Direct motivation from decision.md: UI compares two-decimal strings and CSV imports formatRows. Alternative A reduces helper and hidden-state reader cost; class B adds unsupported state ownership. Runtime outputs unobserved. Worker reports one exec_command cat of exactly four assigned files, exit 0 chunk 1cbb99. Full raw worker tool result is not available in parent; reported observation is not a parent-executed operation.\",\n  \"limits\": [\n    \"Actual model unknown\",\n    \"Full task Git revision unavailable\",\n    \"Worker did not read additional companions because assigned scope was bounded\",\n    \"Full how/why independent method not satisfied\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/case.json",
      "owner": "grades-chatgpt-01-04.json#22",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/input",
      "owner": "grades-chatgpt-01-04.json#22",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/read-only-answer/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#22",
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
