# codex: preserved-behavior

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "preserved-behavior",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-10.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Refactor a fixture invoice formatter by removing a one-caller wrapper and consolidating duplicated state. Preserve literal formatted outputs, empty inputs, rounding and errors. Capture the current outputs before edits. Rename its internal API and migrate code, string references, docs and back-references together. One fixture exposes an unrelated bug, which must stay separate. A speculative abstraction adds reader load and must be reverted. Permit local edits and execution but no external writes. Repeat with workers unavailable, execution denied and behavior coverage absent. Return the changed structure, held pin, equivalence proof, reader-load delta, shipped and reverted work.",
  "caseDefinition": {
    "id": "preserved-behavior",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/refactoring.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/architect/SKILL.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-foundational-thinking/SKILL.md",
      "skills/principle-redesign-from-first-principles/SKILL.md",
      "skills/principle-subtract-before-you-add/SKILL.md",
      "skills/principle-laziness-protocol/SKILL.md",
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/principle-minimize-reader-load/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md"
    ],
    "prompt": "Refactor a fixture invoice formatter by removing a one-caller wrapper and consolidating duplicated state. Preserve literal formatted outputs, empty inputs, rounding and errors. Capture the current outputs before edits. Rename its internal API and migrate code, string references, docs and back-references together. One fixture exposes an unrelated bug, which must stay separate. A speculative abstraction adds reader load and must be reverted. Permit local edits and execution but no external writes. Repeat with workers unavailable, execution denied and behavior coverage absent. Return the changed structure, held pin, equivalence proof, reader-load delta, shipped and reverted work.",
    "requirements": [
      "Read the full mode and eight-step Refactoring playbook, required leaves and routed companion contracts. Record steps before task-specific todos. Route large or cross-cutting work to figure-it-out and named redesigns that change behavior to Feature. Split newly discovered bugs or features out and deliver the structural change first against its pinned contract.",
      "Use how to trace current behavior, then create and execute characterization tests, snapshots or an equivalence harness before moving structure. Write coverage first if absent. Type checks and lint are insufficient pins.",
      "Name the missing domain structure and target module layout, types and call graph. Keep clear local boring code; new shape deletes branches or invalid states. Crossing a function boundary requires complete architect exploration with its runner prompts, rationale and candidate screening.",
      "Subtract dead code, one-caller wrappers, redundant validators and orphan references before additions. Keep the smallest change that reaches the target and revert speculation.",
      "Each small move keeps the original pin green. Migrate every API caller and delete the old API in the same wave without compatibility shims or parallel paths. Inspect actual files for rename usages in strings, prose and back-references. Delegate mechanical edits with the complete poteto prompt, exact revision, ownership and observed inherited or supported configured selection. Inspect artifacts and review the diff.",
      "Verify unchanged behavior on the real artifact. Larger reshapes require old/new output diffs, baseline replay or a matching-surface smoke run through actual authorized controls. Retain outputs and failures.",
      "Assess reduced layers to trace and state to hold. Revert a diff that lowers neither. Do not invent measured reader times.",
      "Order verified subtraction, reshape and cleanup units. Rebase, commit and run complete Opening a PR only when authorized and available. Retain deferred dependencies and unperformed actions. Return all reply artifacts and no new behavior."
    ],
    "expectedFull": "Observed authorized independent mechanical delegation returns inspected artifacts at the assigned revision. The before-edit pin and each subsequent step have matching literal output evidence, including errors and rounding. All callers and textual references move together and the old API disappears. Architecture exploration runs when triggered. The actual artifact has equivalence proof and a source-grounded reader-load reduction. Bug work remains separate and speculation is reverted. With explicit delivery authorization and complete dependencies, ordered green commits and an inspected PR establish delivery. Without external authorization, external delivery remains unperformed.",
    "expectedReduced": "Unavailable workers permit authorized sequential edits and local equivalence checks with reduced capability disclosed. Independent delegation and parallel design remain unsatisfied. Denied writes allow only a source-grounded target shape and ordered proposal. No external authorization yields a checked local diff and delivery plan rather than a PR. Unknown actual models prove no diversity.",
    "expectedBlocked": "Missing source or required leaves stops dependent work. No executable behavior pin blocks structure moves and unchanged-behavior claims. Denied equivalence execution or matching controls leaves behavior unverified. Missing independent operations block required independence rather than waive it. Missing Opening a PR stops PR-dependent work. Unauthorized writes, rebase, commits or PR creation stay unperformed.",
    "forbiddenClaims": [
      "Compilation, lint or structural validation proves unchanged behavior.",
      "A pin captured after edits proves the pre-change contract.",
      "New behavior or an unrelated bug fix belongs in the structural change.",
      "Sequential roles prove independent delegation, parallel exploration or review.",
      "The historical grok-4.7-xhigh-fast default proves current model availability, selection or diversity.",
      "Requested or inherited models are actual observed models.",
      "Caller migration is complete without checking strings, prose and back-references.",
      "Compatibility shims or dual APIs satisfy the same-wave deletion gate.",
      "Unrun checks are green or reader time was measured without observation.",
      "Missing companion execution or deferred PR routing succeeded.",
      "A draft plan is a created PR, external autonomy authorizes writes, or opening a PR starts Babysit.",
      "Helper fixtures prove this host case passed."
    ],
    "caseFile": "docs/parity/cases/playbooks/refactoring.json"
  },
  "registry": {
    "caseId": "preserved-behavior",
    "caseFile": "docs/parity/cases/playbooks/refactoring.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/refactoring.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/architect/SKILL.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-foundational-thinking/SKILL.md",
      "skills/principle-redesign-from-first-principles/SKILL.md",
      "skills/principle-subtract-before-you-add/SKILL.md",
      "skills/principle-laziness-protocol/SKILL.md",
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/principle-minimize-reader-load/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md"
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
        "execution",
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
  "attempts": [
    {
      "attemptId": "grades-native-10.json#3",
      "order": 0,
      "gradeFile": "grades-native-10.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "preserved-behavior",
      "status": "reduced-pass",
      "grade": {
        "caseId": "preserved-behavior",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "execution",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Independent mechanical delegation and triggered architectural competition/fresh judge",
          "Complete delivery companions if later delivery is authorized"
        ],
        "review": "Real before-edit characterization and each subtraction/state/rename/reversion step retain matching18-case outputs. Parent inspects the actual diff/results and corrects prose. Independent nested mechanical/design/Arena methods remain unsatisfied under the no-spawn assignment, so useful equivalent local code does not establish full routed-method support.",
        "responseArtifact": "fixtures/batch-10/preserved-behavior.result.md",
        "rawTrace": "codex/batch-10.events.jsonl",
        "actualCommandEventIds": [
          "item_4",
          "item_5",
          "item_6",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_12",
          "item_13",
          "item_15",
          "item_17",
          "item_19",
          "item_20",
          "item_24",
          "item_28",
          "item_30",
          "item_31",
          "item_32"
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
        "fullExpected": "Observed authorized independent mechanical delegation returns inspected artifacts at the assigned revision. The before-edit pin and each subsequent step have matching literal output evidence, including errors and rounding. All callers and textual references move together and the old API disappears. Architecture exploration runs when triggered. The actual artifact has equivalence proof and a source-grounded reader-load reduction. Bug work remains separate and speculation is reverted. With explicit delivery authorization and complete dependencies, ordered green commits and an inspected PR establish delivery. Without external authorization, external delivery remains unperformed.",
        "reducedExpected": "Unavailable workers permit authorized sequential edits and local equivalence checks with reduced capability disclosed. Independent delegation and parallel design remain unsatisfied. Denied writes allow only a source-grounded target shape and ordered proposal. No external authorization yields a checked local diff and delivery plan rather than a PR. Unknown actual models prove no diversity.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# preserved-behavior\n\nThe fixture formatter now returns the formatted string directly. The private `fixed` wrapper and unobserved `lastFormatted` state are removed. Its internal API is `formatAmount`. Code, symbol-name strings and decision prose moved together. No formatting behavior changed in the 18 observed cases. The unrelated lexical sort defect and observable calculator cache remain intact.\n\n## Supplied input and identity\n\nThe complete supplied case is retained in [supplied-input.json](preserved-behavior/supplied-input.json). The requested action was to preserve literal formatting, rounding, errors and empty inputs while removing a one-caller wrapper, consolidating state, migrating the API, keeping an unrelated bug separate, and reverting speculative abstraction. The requested variants were workers unavailable, execution denied and behavior coverage absent.\n\nThe actual input commit is `bca2ea20c7743bf7e07239688ed6228527f199fd`. `git cat-file -t` returned `commit`, `git show` exposed the committed inputs, and `git rev-parse HEAD` returned that exact SHA. Every shared invoice input was compared byte-for-byte with its `committed-inputs/additional/invoice/` Git blob. All seven matched. The checks and SHA-256 hashes are in [input-identity.json](preserved-behavior/evidence/input-identity.json). Output artifacts were created after that revision and are not claimed as part of its tree.\n\nOnly `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0` supplied workflow instructions. The installed plugin manifests identify version `0.1.0`. The requested package source freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`. The installed directory has no Git metadata. Its association with that freeze is supplied task context, not independently proven Git commit identity. The parent support case retains the installed byte-copy manifest in [copy-identity.json](package-support-contracts/copy-identity.json). No other package version was read.\n\n## Reads and ownership\n\nAll named mode, Refactoring, Feature, Opening a PR, how, figure-it-out, architect, principle leaves and prompt files were read through `functions.exec` and `tools.exec_command` with complete output. Their owned byte copies and hashes are in [source-reads](preserved-behavior/source-reads) and [source-read-receipt.json](preserved-behavior/evidence/source-read-receipt.json). The contract's historical `agents/poteto-agent.md` pointer was resolved to the user's actual named `references/agent-prompts/poteto-agent.md` path. The host-capability, ownership, assignment, model-role, Arena, technical-writing and unslop contracts were also read in full. Additional applied leaf reads included exhaust-the-design-space, separate-before-serializing-shared-state, boundary-discipline, encode-lessons-in-structure, make-operations-idempotent and test-behavior-not-implementation.\n\nThe parent evaluation controller owns integration. This native worker owns `preserved-behavior/` and this result file. No nested workers were allowed by the parent assignment. The worker directly owned its diff and returned it for parent review, as the mode's forbidden-to-spawn exception requires. Requested selection was inherited. Actual model and effort are unknown. No independent design competition or model diversity is claimed.\n\nThe eight Refactoring steps were copied verbatim before task-specific items into [checklist.md](preserved-behavior/checklist.md). This is an authorized Markdown substitute for an unavailable todo operation. The throughput checkpoint is retained there. [how.md](preserved-behavior/how.md) traces the real formatter, exporter and calculation paths. [design.md](preserved-behavior/design.md) records two structurally distinct sequential candidates, usage-first sketches, red-flag screening, a selected direct-function shape and the rejected stateful-class shape. Parallel architect candidates and fresh Arena judgment remain unsatisfied. Figure-it-out was read but not activated because this is a focused change. The unrelated bug is not routed into this change. No Feature implementation ran.\n\n## Actual actions and output\n\n`prepare.mjs` copied required inert input files before edits into `baseline`, `main`, `workers-unavailable`, `execution-denied` and `coverage-absent`. `pin.mjs` was written and executed against untouched `main` before any production edit. `run.mjs` retained each command, Bun version, exit code, stdout and stderr. Execution used Bun `1.4.2` with `--no-install`. No dependency was installed.\n\nThe first actual command was `bun --no-install preserved-behavior/run.mjs before main`. Its child command was `bun --no-install /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main`. It exited `0` with empty stderr. Its verbatim output is [before.stdout](preserved-behavior/evidence/before.stdout), and its complete invocation record is [before.json](preserved-behavior/evidence/before.json).\n\nThe observed literal outputs include `0.00`, `1.00` for `1.005`, `-1.00` for `-1.005`, `12.35` for `12.345`, empty rows `[]`, empty export `''`, and Error with message `nonfinite` for NaN, either Infinity, a string, null and a nonfinite row. Exported rows produced `0.00\\n12.35`. The controller returned `{total:6.5}`, and `inspectCachedTotal()` returned `6.5`. The unrelated lexical sort returned `['10','2']` and remains pinned as its current behavior. These are runtime observations from copied synthetic input, with no real service contact.\n\nThe ordered main changes and checks were:\n\n| Unit | Retained actual output | Exit |\n| --- | --- | --- |\n| Before edits | [before.json](preserved-behavior/evidence/before.json) | 0 |\n| Remove fixed wrapper | [after-subtraction.json](preserved-behavior/evidence/after-subtraction.json) | 0 |\n| Replace lastFormatted with return value | [after-state.json](preserved-behavior/evidence/after-state.json) | 0 |\n| Add speculative formatThroughStrategy delegate | [after-speculation.json](preserved-behavior/evidence/after-speculation.json) | 0 |\n| Revert speculative delegate | [after-revert.json](preserved-behavior/evidence/after-revert.json) | 0 |\n| Atomic API and textual-reference rename | [after-rename.json](preserved-behavior/evidence/after-rename.json) | 0 |\n| Final artifact after prose correction | [final-main.json](preserved-behavior/evidence/final-main.json) | 0 |\n\nEvery output above is byte-identical to the before-edit stdout. Each contains the actual line `18 literal behavior checks matched.` The equivalence check compares retained complete stdout, not compilation or structural validation. The finite test set does not prove every possible JavaScript input equivalent.\n\nThe speculative wrapper was actually written, executed and reverted. Its execution preserved behavior but added an unnecessary call layer. The exact before bytes and a disclosed reconstruction of the speculative bytes are retained in [speculation-before.mjs](preserved-behavior/evidence/speculation-before.mjs), [speculative-wrapper.mjs](preserved-behavior/evidence/speculative-wrapper.mjs) and [speculative-reversion.json](preserved-behavior/evidence/speculative-reversion.json). The reconstructed source is not misrepresented as a separate captured original file.\n\n## Variants\n\n| Variant | Actual attempt and result | Limit |\n| --- | --- | --- |\n| Main native worker | Copied fixture, pre-edit pin, sequential edits, stage replay, parent diff review. | Parent could spawn this worker. No nested independent mechanical delegate or architect candidate was used. |\n| Workers unavailable | A separate untouched copy received its own pre-edit replay, subtraction, state removal and rename. Each stage exited 0 and matched the original stdout. | Worker unavailability is a simulated case policy. The host exposes collaboration tools. Required independent architecture and nested delegation remain unsatisfied. |\n| Execution denied | Retained a separate original copy, source-grounded target and ordered proposal. No behavior pin, production edit or equivalence run targeted this copy. All seven source files remain byte-identical to baseline. | Denial is simulated, not enforced by the host. Variant behavior is unverified and unchanged-behavior claims are withheld. File inspection and report creation still used authorized host execution outside that simulated branch. |\n| Behavior coverage absent | Initial files contain no tests. The new characterization pin was run against this copy before its first edit. Subtraction, state removal and rename each retained the literal outputs. Final check exited 0. | Coverage absence is real for the prepared fixture. The external case-owned pin supplies coverage first. It is not a pre-existing test suite. |\n\nVariant commands, their order and complete output are in [variant-commands.json](preserved-behavior/evidence/variant-commands.json). Initial directory inventories are retained beside them. The denied branch is in [execution-denied.json](preserved-behavior/evidence/execution-denied.json). Final checks are in [final-workers-unavailable.json](preserved-behavior/evidence/final-workers-unavailable.json) and [final-coverage-absent.json](preserved-behavior/evidence/final-coverage-absent.json).\n\n## Reviewed structure and limits\n\nThe checked local patch is [final.diff](preserved-behavior/evidence/final.diff). The actual Git no-index diff exits `1` because differences exist. This is expected diff behavior, not a test failure. Actual `rg` queries found no old `formatInvoice` or speculative `formatThroughStrategy` reference in `main`, exiting `1` for no matches. The new-name query found the definition, call, symbol string and decision prose, exiting `0`. Their complete output is in [final-diff-and-reference-queries.json](preserved-behavior/evidence/final-diff-and-reference-queries.json). Baseline and historical evidence intentionally retain old names.\n\n[final-inspection.json](preserved-behavior/evidence/final-inspection.json) confirms the old API is absent, the new API exists, symbol strings contain the new name, and calculator, controller, facade and adapter bytes are unchanged. The parent inspected the actual diff and 18-check output. It found a mechanical prose corruption and requested clearer wording plus accurate Arena disclosure. Both were corrected. [lead-review.md](preserved-behavior/evidence/lead-review.md) records the actual collaboration review, without inventing model identities or independent Arena judging.\n\nSource inspection counts the formatter path from `formatRows` to native `toFixed` as three call edges before and two after. Mutable formatter module bindings fall from one to zero. These are source counts, not measured reader time. The speculative layer lowered neither axis and was reverted. Model the Domain and Foundational Thinking selected the direct function. Laziness Protocol, Subtract Before You Add and Minimize Reader Load rejected extra indirection. Migrate Callers Then Delete Legacy APIs required coordinated rename deletion. Prove It Works, Test Behavior Not Implementation and Sequence Work into Verifiable Units required literal replays after each move.\n\nThe shipped scope is a local reviewable patch only. No commit, rebase, push, PR, publish, account write, schedule or live service operation occurred. The delivery order remains baseline pin, verified subtraction, state reshape, coordinated rename and prose cleanup. Those are ordered local artifacts, not landed history. Opening a PR was read in full but its external branch was not authorized. External deslop and matching UI or CLI companions did not run. A standalone module execution check proves the selected library behavior only. Required independent architect exploration and fresh cross-judge are still open. No self-grade is assigned.\n",
        "artifact": {
          "path": "fixtures/batch-10/preserved-behavior.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior.result.md",
          "sha256": "341fe4c8c27dcd65a5c930a62a5b52649e1432dcce843d158ab418464dac4050",
          "bytes": 11924
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-10.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-10.events.jsonl",
            "sha256": "ec021dc2ac9a76ee6145304a5e10476b77f4a577a8f6e6764225d5a01a6de70e",
            "bytes": 436747,
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
      "path": "fixtures/batch-10/preserved-behavior/change.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs",
      "sha256": "2433777b0acea266dd09ac40334bf466ceecd67a3282831774d4ae03229c6133",
      "bytes": 1550,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import {readFile,writeFile} from 'node:fs/promises';\nconst variant=process.argv[2],stage=process.argv[3];\nconst dir=`${import.meta.dir}/${variant}`;\nconst path=`${dir}/formatter.mjs`;\nlet src=await readFile(path,'utf8');\nif(stage==='subtract')src=src.replace('function fixed(value) { return value.toFixed(2); }\\n','').replace('lastFormatted = fixed(value);','lastFormatted = value.toFixed(2);');\nif(stage==='state')src=src.replace(\"let lastFormatted = '';\\n\",'').replace('  lastFormatted = value.toFixed(2);\\n  return lastFormatted;','  return value.toFixed(2);');\nif(stage==='speculate'){await writeFile(`${import.meta.dir}/evidence/speculation-before.mjs`,src);src=src.replace('export function formatInvoice(value) {','function formatThroughStrategy(value) {').replace('export function formatRows(rows)', 'export function formatInvoice(value) { return formatThroughStrategy(value); }\\nexport function formatRows(rows)');}\nif(stage==='revert')src=await readFile(`${import.meta.dir}/evidence/speculation-before.mjs`,'utf8');\nif(stage==='rename'){\n  for(const name of ['formatter.mjs','exporter.mjs','decision.md']){const file=`${dir}/${name}`;await writeFile(file,(await readFile(file,'utf8')).replaceAll('formatInvoice','formatAmount').replace('Authorized internal rename target for preserved-behavior: formatAmount -> formatAmount.','Current internal formatting API for preserved-behavior is formatAmount.'));}\n}else await writeFile(path,src);\nconsole.log(JSON.stringify({variant,stage,action:'local edit',formatter:await readFile(path,'utf8')}));\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/checklist.md",
      "sha256": "e79e2f78430325f554771b68f7cf38f0f8e2e567c5bf04427748f9bf90541433",
      "bytes": 5457,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Refactoring checklist\n\nReduced todo binding. This owned Markdown file substitutes for an unavailable todo operation.\n\n1. Pin the behavior contract first. Run the [how](../../how/SKILL.md) skill over the affected subsystem to learn the contract, then write a characterization test, snapshot, or equivalence harness that captures current behavior before any structure moves. If the area has no coverage, write the pin before touching structure. Type check and lint are not a pin.\n2. Name the structure the code is missing per [principle-model-the-domain](../../principle-model-the-domain/SKILL.md). Boring code stays when the shape is already clear and local. The reshape must delete branches or invalid states, not add indirection.\n3. Name the target shape. State what the module layout, types, and call graph should be if built today ([principle-foundational-thinking](../../principle-foundational-thinking/SKILL.md), [principle-redesign-from-first-principles](../../principle-redesign-from-first-principles/SKILL.md)). If the target crosses a function boundary, run the [architect](../../architect/SKILL.md) skill for parallel design exploration of the shape before the move.\n4. Subtract before you add. Delete dead code, collapse one-caller wrappers, drop redundant validators, and remove orphan references before introducing the new shape ([principle-subtract-before-you-add](../../principle-subtract-before-you-add/SKILL.md)). The smallest change that reaches the target shape ships ([principle-laziness-protocol](../../principle-laziness-protocol/SKILL.md)). A speculative cleanup that \"might help\" gets reverted.\n5. Move in small behavior-preserving steps, each keeping the pin green. For API reshapes, migrate every caller and delete the old API in the same wave ([principle-migrate-callers-then-delete-legacy-apis](../../principle-migrate-callers-then-delete-legacy-apis/SKILL.md)). No compatibility shims, no parallel old-and-new paths. Spot-check every rename against the actual files. Renames silently miss usages in strings, prose, and back-references. Delegate the mechanical edits to an authorized independent worker with a specific scope, including file paths, the names being moved and the behavior to hold. Supply the complete [poteto role prompt](../../../references/agent-prompts/poteto-agent.md) and record the exact input revision, owned output paths, worker identity and inspected artifacts. Use inherited model and effort unless a supported configured refactoring selection is observed. Record requested and actual selections separately; unknown actual models prove no diversity. Review the returned diff yourself. When workers are unavailable or unauthorized, perform authorized mechanical edits sequentially only as reduced capability and leave the independent delegation gate unsatisfied.\n6. Prove behavior is unchanged on the real artifact, not \"it compiles\" ([principle-prove-it-works](../../principle-prove-it-works/SKILL.md)). For larger reshapes, run an equivalence check: a script that diffs old-vs-new outputs, a recorded baseline replayed against the new code, or a smoke run on the matching surface via the relevant control skill.\n7. Confirm the change is worth keeping. The success measure is reduced reader load ([principle-minimize-reader-load](../../principle-minimize-reader-load/SKILL.md)). If the diff does not lower reader load somewhere, revert it.\n8. Rebase into small ordered commits. A subtraction commit, then the reshape, then any follow-on cleanup. Shape them with the [sequence-verifiable-units](../../principle-sequence-verifiable-units/SKILL.md) principle skill, so each behavior-preserving slice stays green before the next. Rebase and commit only with authorization and an available operation, preserving concurrent work. Otherwise return the checked local diff and ordered delivery plan with these operations unperformed. Run **Opening a PR** by reading `skills/poteto-mode/playbooks/opening-a-pr.md` in full and following its complete contract when available and authorized. This is a deferred task 21 dependency for task 24 integration until that file exists; stop PR-dependent work if absent. No push or PR creation follows from this playbook without explicit authorization. Opening a PR never starts Babysit implicitly.\n\n## Local scope\n\n- Parent evaluation controller retains integration ownership. This case owner writes only this directory and its result.\n- Blocking first steps. Read contracts, trace fixtures, capture literal pre-edit outputs.\n- Independent workstreams. None inside this case. Parent forbids nested workers because slots are owned. Mechanical edits and two design candidates run sequentially. Independent design and mechanical delegation gates remain unsatisfied.\n- Shared mutable state. Single case owner writes the coupled formatter and exporter. Other cases have disjoint paths.\n- Smallest safe decomposition. One formatter owner avoids concurrent rename edits. Baseline, subtraction, speculation and revert, then atomic API rename.\n- Architect phases. Ground, Sketch, Agree, Implement, Scrap. Agree proceeds under local authorization. Scrap is unnecessary if the chosen shape holds.\n- Arena phases. Frame, Fan out, Cross-judge, Pick, Graft, Verify. Fan out and fresh judge use sequential reduced comparison. No independent arena execution is claimed.\n- Step 8 skip. Rebase, commits, pushes and PRs are forbidden. Full Opening a PR was read. No delivery branch executes.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/decision.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent/decision.md",
      "sha256": "1e90b189bd332f6892f06b01fee8931dfaef724d4a661abf7d57f4190ace1172",
      "bytes": 1175,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Synthetic invoice decision record\n\nDisplay contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\n\nFixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatAmount and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\n\nCurrent internal formatting API for preserved-behavior is formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/exporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent/exporter.mjs",
      "sha256": "22018eca9aab2ac09a5e9319751d5c6d9a171b30812748a274d5c331d8c6b392",
      "bytes": 190,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import { formatRows } from './formatter.mjs';\nexport function exportAmounts(rows) { return formatRows(rows).join('\\n'); }\nexport const publicFixtureSymbols = ['formatAmount', 'formatRows'];\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/formatter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent/formatter.mjs",
      "sha256": "bf0206ae81c99c2761d7673c1508bf33d8845f158cd10198bf3908e851017089",
      "bytes": 369,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "export function formatAmount(value) {\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\n  return value.toFixed(2);\n}\nexport function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\nexport function sortAmounts(values) { return values.toSorted(); }\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/design.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/design.md",
      "sha256": "b3a59b063acc3e270ebbf5dfe1f7c1b4f89ffd866f917badfeb84b1ef2fdcfa1",
      "bytes": 6069,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Sequential architect exploration\n\nThe task is focused. The figure-it-out contract was read but its large-migration route is unnecessary. A behavior change would route to Feature. This task retains the formatter's behavior and leaves the sort bug separate.\n\nThe complete architect runner prompt, rationale template and red flags were read before these sketches. Sequential candidate exploration was performed. Arena's independent workflow did not run. There was no independent candidate or judge. Nested workers are forbidden by the assignment. Requested selection is inherit-parent. Actual model and effort are unknown. No configured selection was requested or rejected.\n\n## Frame\n\nCandidates produce one formatter shape. The comparison criteria are literal output equivalence, layers to trace, mutable state to remember, and completeness of the rename. These criteria are qualitative and are not self-assigned case grades. Both candidates use the same pre-edit findings in how.md at input revision bca2ea20c7743bf7e07239688ed6228527f199fd.\n\n## Candidate A\n\n### Problem\n\nThe private wrapper fixed forwards to toFixed. lastFormatted repeats a return value with no exposed reader. Remove both while preserving error policy and output rounding.\n\n### Usage\n\nThe CSV consumer calls exportAmounts([{total:12.345}]) and receives '12.35'. The row caller calls formatRows([{total:0}]) and receives ['0.00']. A direct internal caller calls formatAmount(1.005) and receives '1.00'.\n\n### Shape\n\nformatter.mjs exposes formatAmount(value), formatRows(rows) and the existing unrelated sortAmounts. Conceptual types are finite Number to string and Array<{total:Number}> to Array<string>. formatAmount validates once and returns value.toFixed(2). The candidate signature sketch is `function formatAmount(value) { throw new Error('not implemented'); }`. No new module is needed. The one-function interface hides finite-number validation and display rounding. formatRows owns only mapping. Data state is local and immutable.\n\n### Synthesis decision\n\nSelected as the base after the separate sequential comparison below. No graft adds production code.\n\n### Tradeoffs accepted\n\n- We accept JavaScript binary rounding in exchange for literal behavior preservation.\n- We accept a coordinated internal rename in exchange for one API without compatibility paths.\n\n### Alternatives considered\n\nA general formatting registry could hide alternate formats, but no alternate format exists. It would expose registration and configuration without reducing existing policy.\n\n### Open questions and risks\n\nCould an uninspected external importer require the old name? This fixture's scope declares the rename internal and authorizes it. No external compatibility claim is made.\n\n### Next implementation step\n\nKeep the executed behavior pin and remove fixed before changing state or API names.\n\n## Candidate B\n\n### Problem\n\nGather formatting policy and last output in a Formatter instance. Preserve the same outputs through delegated methods.\n\n### Usage\n\nThe CSV consumer still calls exportAmounts([{total:12.345}]). The row consumer still calls formatRows([{total:0}]). A direct caller imports formatAmount(1.005). Every public function delegates to a private Formatter instance.\n\n### Shape\n\nThe candidate adds a Formatter class with amount(value) and rows(rows), plus a singleton instance and exported delegates. Its sketch is `class Formatter { amount(value) { throw new Error('not implemented'); } }`. Finite-number validation stays inside amount. The singleton stores lastFormatted. It hides no additional policy while introducing object lifecycle and another layer.\n\n### Synthesis decision\n\nRejected. This abstraction retains the state and adds a class, singleton and delegates. Its behavior could match but its interface depth is worse.\n\n### Tradeoffs accepted\n\n- We accept instance lifecycle in exchange for a place to put future policies. No current caller requires those policies.\n\n### Alternatives considered\n\nA pure direct function avoids the lifecycle entirely and is the selected candidate.\n\n### Open questions and risks\n\nWhat policy requires an instance? None was found in the inspected files.\n\n### Next implementation step\n\nDo not keep this design. The required speculation exercise adds a temporary delegate layer, runs the pin, then restores the direct implementation with retained diff evidence.\n\n## Screening and synthesis\n\nCandidate A removes a pass-through method and split representation of the returned string. It keeps one formatting path. It does not introduce temporal modules, public transport types, hand-synced configuration or caller coordination. The existing fixture symbol list is migrated because it is supplied synthetic metadata, not a new registry.\n\nCandidate B triggers shallow-module and pass-through red flags. It adds importable methods and lifecycle without compressing complexity. Candidate A wins on layers and state. Both can express the same behavior, so no behavior-based graft is needed. The useful idea from B is the reminder that observable cache state must be checked before removal. The pin checks inspectCachedTotal and the calculator is left intact. This is a verification consideration rather than a production abstraction.\n\nThe fresh independent judge gate and parallel model perspectives remain unsatisfied. Parent diff inspection is requested separately. This local comparison does not replace independent arena judgment.\n\n## Principles that changed decisions\n\nModel the Domain and Foundational Thinking select a finite-number display function with no formatter instance. Redesign from First Principles moves references together. Subtract Before You Add removes fixed before the API move. Laziness Protocol and Minimize Reader Load reject the speculative layer. Migrate Callers Then Delete Legacy APIs removes the old export in the same wave. Prove It Works and Sequence Work into Verifiable Units require a literal output replay after each move. Test Behavior, Not Implementation supplies positive literal assertions and actual error messages.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-rename.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-rename.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-rename.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-rename.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-revert.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-revert.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-revert.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-revert.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-speculation.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-speculation.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-speculation.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-speculation.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-state.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-state.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-state.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-subtraction.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-subtraction.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/after-subtraction.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/after-subtraction.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/before.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/before.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/before.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-before.json",
      "sha256": "a982d84f715c4ea3de70d908c34a321fc0e81d4d8d9c14468dc6f7577c83e504",
      "bytes": 2098,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-before.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-before.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-initial-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-initial-files.json",
      "sha256": "2b1f677b29eabbea93287ab9d147600a48e0dded6f57590ecc9c1d44ae5e8d83",
      "bytes": 107,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\"calculator.mjs\",\"exporter.mjs\",\"adapter.mjs\",\"facade.mjs\",\"controller.mjs\",\"decision.md\",\"formatter.mjs\"]"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-rename.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-rename.json",
      "sha256": "a982d84f715c4ea3de70d908c34a321fc0e81d4d8d9c14468dc6f7577c83e504",
      "bytes": 2098,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-rename.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-rename.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-state.json",
      "sha256": "a982d84f715c4ea3de70d908c34a321fc0e81d4d8d9c14468dc6f7577c83e504",
      "bytes": 2098,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-state.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-state.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-subtract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-subtract.json",
      "sha256": "a982d84f715c4ea3de70d908c34a321fc0e81d4d8d9c14468dc6f7577c83e504",
      "bytes": 2098,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/coverage-absent-subtract.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/coverage-absent-subtract.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/execution-denied.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/execution-denied.json",
      "sha256": "f7a40649ede5380f5460108284fb46ba26847ce4f08e50026f73eea0f6d089b3",
      "bytes": 703,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"condition\": \"simulated policy restriction, not enforced by host\",\n  \"variantExecution\": \"not-run\",\n  \"pin\": \"unrun\",\n  \"structuralEdits\": \"none\",\n  \"equivalence\": \"unverified\",\n  \"sourceBytes\": [\n    {\n      \"name\": \"calculator.mjs\",\n      \"byteIdentical\": true\n    },\n    {\n      \"name\": \"exporter.mjs\",\n      \"byteIdentical\": true\n    },\n    {\n      \"name\": \"adapter.mjs\",\n      \"byteIdentical\": true\n    },\n    {\n      \"name\": \"facade.mjs\",\n      \"byteIdentical\": true\n    },\n    {\n      \"name\": \"controller.mjs\",\n      \"byteIdentical\": true\n    },\n    {\n      \"name\": \"decision.md\",\n      \"byteIdentical\": true\n    },\n    {\n      \"name\": \"formatter.mjs\",\n      \"byteIdentical\": true\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-coverage-absent.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-coverage-absent.json",
      "sha256": "a982d84f715c4ea3de70d908c34a321fc0e81d4d8d9c14468dc6f7577c83e504",
      "bytes": 2098,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-coverage-absent.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-coverage-absent.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-diff-and-reference-queries.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-diff-and-reference-queries.json",
      "sha256": "6fb3ca904702204b002ceedb0ca71f30f5f64196d7bbb651dfe4ee7d9493dc8e",
      "bytes": 4833,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"command\": [\n      \"git\",\n      \"diff\",\n      \"--no-index\",\n      \"--\",\n      \"baseline\",\n      \"main\"\n    ],\n    \"exitCode\": 1,\n    \"stdout\": \"diff --git a/baseline/decision.md b/main/decision.md\\nindex 474538b..778fd3e 100644\\n--- a/baseline/decision.md\\n+++ b/main/decision.md\\n@@ -2,6 +2,6 @@\\n \\n Display contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\\n \\n-Fixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatInvoice and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\\n+Fixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatAmount and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\\n \\n-Authorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\n+Current internal formatting API for preserved-behavior is formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\ndiff --git a/baseline/exporter.mjs b/main/exporter.mjs\\nindex 1a58806..24e47a9 100644\\n--- a/baseline/exporter.mjs\\n+++ b/main/exporter.mjs\\n@@ -1,3 +1,3 @@\\n import { formatRows } from './formatter.mjs';\\n export function exportAmounts(rows) { return formatRows(rows).join('\\\\n'); }\\n-export const publicFixtureSymbols = ['formatInvoice', 'formatRows'];\\n+export const publicFixtureSymbols = ['formatAmount', 'formatRows'];\\ndiff --git a/baseline/formatter.mjs b/main/formatter.mjs\\nindex 5b61f9e..ad2bef7 100644\\n--- a/baseline/formatter.mjs\\n+++ b/main/formatter.mjs\\n@@ -1,10 +1,7 @@\\n-let lastFormatted = '';\\n-function fixed(value) { return value.toFixed(2); }\\n-export function formatInvoice(value) {\\n+export function formatAmount(value) {\\n   if (!Number.isFinite(value)) throw new Error('nonfinite');\\n-  lastFormatted = fixed(value);\\n-  return lastFormatted;\\n+  return value.toFixed(2);\\n }\\n-export function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\n+export function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\\n // Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\n export function sortAmounts(values) { return values.toSorted(); }\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"rg\",\n      \"-n\",\n      \"formatInvoice|formatThroughStrategy\",\n      \"main\"\n    ],\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"command\": [\n      \"rg\",\n      \"-n\",\n      \"formatAmount\",\n      \"main\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"main/formatter.mjs:1:export function formatAmount(value) {\\nmain/formatter.mjs:5:export function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\\nmain/decision.md:5:Fixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatAmount and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\\nmain/decision.md:7:Current internal formatting API for preserved-behavior is formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\\nmain/exporter.mjs:3:export const publicFixtureSymbols = ['formatAmount', 'formatRows'];\\n\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-inspection.json",
      "sha256": "240cca795f176951753bcfa18c8904cd6baf4dab203341f8fa9c96a7831653eb",
      "bytes": 1152,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"commands\": [\n    {\n      \"command\": [\n        \"git\",\n        \"diff\",\n        \"--no-index\",\n        \"--\",\n        \"baseline\",\n        \"main\"\n      ],\n      \"exitCode\": 1\n    },\n    {\n      \"command\": [\n        \"rg\",\n        \"-n\",\n        \"formatInvoice|formatThroughStrategy\",\n        \"main\"\n      ],\n      \"exitCode\": 1\n    },\n    {\n      \"command\": [\n        \"rg\",\n        \"-n\",\n        \"formatAmount\",\n        \"main\"\n      ],\n      \"exitCode\": 0\n    }\n  ],\n  \"checks\": [\n    {\n      \"name\": \"calculator.mjs\",\n      \"unchanged\": true\n    },\n    {\n      \"name\": \"controller.mjs\",\n      \"unchanged\": true\n    },\n    {\n      \"name\": \"adapter.mjs\",\n      \"unchanged\": true\n    },\n    {\n      \"name\": \"facade.mjs\",\n      \"unchanged\": true\n    }\n  ],\n  \"oldApiAbsent\": true,\n  \"newApiPresent\": true,\n  \"symbolStrings\": [\n    \"formatAmount\",\n    \"formatRows\"\n  ],\n  \"readerLoad\": {\n    \"formatRowsToNativeBefore\": 3,\n    \"formatRowsToNativeAfter\": 2,\n    \"moduleMutableFormatterBindingsBefore\": 1,\n    \"moduleMutableFormatterBindingsAfter\": 0,\n    \"measurement\": \"source call-edge and binding count, not measured reader time\"\n  },\n  \"runtime\": \"1.4.2\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-main.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-main.json",
      "sha256": "9647e676d8b26ebaa474f2ae33beddbf8eef0262b07b91ba8c21074d21d93b01",
      "bytes": 2087,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-main.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-main.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-workers-unavailable.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-workers-unavailable.json",
      "sha256": "73a06d5058907e142ecff402a54b4d70591450ef3302b45300ce759f0fab215b",
      "bytes": 2102,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final-workers-unavailable.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final-workers-unavailable.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/final.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/final.diff",
      "sha256": "05acc88a7390f2017c65458c11c2d311f1133aad942ec20e91c5d0cf48e3b723",
      "bytes": 3264,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "diff --git a/baseline/decision.md b/main/decision.md\nindex 474538b..778fd3e 100644\n--- a/baseline/decision.md\n+++ b/main/decision.md\n@@ -2,6 +2,6 @@\n \n Display contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\n \n-Fixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatInvoice and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\n+Fixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatAmount and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\n \n-Authorized internal rename target for preserved-behavior: formatInvoice -> formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\n+Current internal formatting API for preserved-behavior is formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\ndiff --git a/baseline/exporter.mjs b/main/exporter.mjs\nindex 1a58806..24e47a9 100644\n--- a/baseline/exporter.mjs\n+++ b/main/exporter.mjs\n@@ -1,3 +1,3 @@\n import { formatRows } from './formatter.mjs';\n export function exportAmounts(rows) { return formatRows(rows).join('\\n'); }\n-export const publicFixtureSymbols = ['formatInvoice', 'formatRows'];\n+export const publicFixtureSymbols = ['formatAmount', 'formatRows'];\ndiff --git a/baseline/formatter.mjs b/main/formatter.mjs\nindex 5b61f9e..ad2bef7 100644\n--- a/baseline/formatter.mjs\n+++ b/main/formatter.mjs\n@@ -1,10 +1,7 @@\n-let lastFormatted = '';\n-function fixed(value) { return value.toFixed(2); }\n-export function formatInvoice(value) {\n+export function formatAmount(value) {\n   if (!Number.isFinite(value)) throw new Error('nonfinite');\n-  lastFormatted = fixed(value);\n-  return lastFormatted;\n+  return value.toFixed(2);\n }\n-export function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\n+export function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\n // Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\n export function sortAmounts(values) { return values.toSorted(); }\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/input-identity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/input-identity.json",
      "sha256": "09ae5fc137b798e84c13cd60fbeac865b6802fabf9027a4848567481fdb38aba",
      "bytes": 1377,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"currentHead\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"checks\": [\n    {\n      \"name\": \"calculator.mjs\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff\"\n    },\n    {\n      \"name\": \"exporter.mjs\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d\"\n    },\n    {\n      \"name\": \"adapter.mjs\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c\"\n    },\n    {\n      \"name\": \"facade.mjs\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d\"\n    },\n    {\n      \"name\": \"controller.mjs\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862\"\n    },\n    {\n      \"name\": \"decision.md\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee\"\n    },\n    {\n      \"name\": \"formatter.mjs\",\n      \"exitCode\": 0,\n      \"byteIdentical\": true,\n      \"sha256\": \"405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7\"\n    }\n  ]\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/lead-review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/lead-review.md",
      "sha256": "f20190a3725bf1b907c29a7f34407bb2677234ccae408778dfa209d26cd9df05",
      "bytes": 896,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Lead review receipt\n\nThe parent controller inspected the actual baseline-to-main diff and evidence/after-rename.json through its tools. Its collaboration message reported that the production change was scoped and that all 18 behavior checks were inspected. It found the mechanical prose corruption `formatAmount -> formatAmount` in decision.md and asked for a clear current-state sentence. The case owner had just corrected the text to `Current internal formatting API for preserved-behavior is formatAmount.` Final reference-query evidence retains that correction.\n\nThe parent also requested explicit wording that sequential candidate exploration was performed and the independent Arena workflow did not run. design.md now uses that wording. This is a parent review of a worker-owned diff. It does not establish separate architect candidates, a fresh Arena judge, or observed model diversity.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/speculation-before.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/speculation-before.mjs",
      "sha256": "81c3ad5603429b52792f521259004166e2de6befac669c35545a4c59cb26f024",
      "bytes": 371,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "export function formatInvoice(value) {\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\n  return value.toFixed(2);\n}\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\nexport function sortAmounts(values) { return values.toSorted(); }\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/speculative-reversion.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/speculative-reversion.json",
      "sha256": "67d889ef28d74a7142bb47e164f4429c4bdf1e8cae82825b19adb4c80f64ab2d",
      "bytes": 396,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"note\": \"The speculative source is reconstructed byte-for-byte from the observed edit script and captured before bytes. The actual speculative execution is retained in after-speculation.json. It is not shipped.\",\n  \"speculativeSha256\": \"ac2778fe7848925dd2ab90c52e42b0c8b1e851bac419523a2bfa463fd5de5220\",\n  \"restoredSha256\": \"81c3ad5603429b52792f521259004166e2de6befac669c35545a4c59cb26f024\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/speculative-wrapper.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/speculative-wrapper.mjs",
      "sha256": "ac2778fe7848925dd2ab90c52e42b0c8b1e851bac419523a2bfa463fd5de5220",
      "bytes": 450,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "function formatThroughStrategy(value) {\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\n  return value.toFixed(2);\n}\nexport function formatInvoice(value) { return formatThroughStrategy(value); }\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\nexport function sortAmounts(values) { return values.toSorted(); }\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/variant-commands.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/variant-commands.json",
      "sha256": "1d2a3e4f26ce594322cd5a79ef9399cb1f8c7ce2769c47f4f8a795c2e9db407b",
      "bytes": 28191,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"order\": 1,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"workers-unavailable-before\",\n      \"workers-unavailable\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 2,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs\",\n      \"workers-unavailable\",\n      \"subtract\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"variant\\\":\\\"workers-unavailable\\\",\\\"stage\\\":\\\"subtract\\\",\\\"action\\\":\\\"local edit\\\",\\\"formatter\\\":\\\"let lastFormatted = '';\\\\nexport function formatInvoice(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  lastFormatted = value.toFixed(2);\\\\n  return lastFormatted;\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 3,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"workers-unavailable-subtract\",\n      \"workers-unavailable\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 4,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs\",\n      \"workers-unavailable\",\n      \"state\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"variant\\\":\\\"workers-unavailable\\\",\\\"stage\\\":\\\"state\\\",\\\"action\\\":\\\"local edit\\\",\\\"formatter\\\":\\\"export function formatInvoice(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  return value.toFixed(2);\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 5,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"workers-unavailable-state\",\n      \"workers-unavailable\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 6,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs\",\n      \"workers-unavailable\",\n      \"rename\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"variant\\\":\\\"workers-unavailable\\\",\\\"stage\\\":\\\"rename\\\",\\\"action\\\":\\\"local edit\\\",\\\"formatter\\\":\\\"export function formatAmount(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  return value.toFixed(2);\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 7,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"workers-unavailable-rename\",\n      \"workers-unavailable\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 8,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"coverage-absent-before\",\n      \"coverage-absent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 9,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs\",\n      \"coverage-absent\",\n      \"subtract\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"variant\\\":\\\"coverage-absent\\\",\\\"stage\\\":\\\"subtract\\\",\\\"action\\\":\\\"local edit\\\",\\\"formatter\\\":\\\"let lastFormatted = '';\\\\nexport function formatInvoice(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  lastFormatted = value.toFixed(2);\\\\n  return lastFormatted;\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 10,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"coverage-absent-subtract\",\n      \"coverage-absent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 11,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs\",\n      \"coverage-absent\",\n      \"state\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"variant\\\":\\\"coverage-absent\\\",\\\"stage\\\":\\\"state\\\",\\\"action\\\":\\\"local edit\\\",\\\"formatter\\\":\\\"export function formatInvoice(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  return value.toFixed(2);\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatInvoice(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 12,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"coverage-absent-state\",\n      \"coverage-absent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 13,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/change.mjs\",\n      \"coverage-absent\",\n      \"rename\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"variant\\\":\\\"coverage-absent\\\",\\\"stage\\\":\\\"rename\\\",\\\"action\\\":\\\"local edit\\\",\\\"formatter\\\":\\\"export function formatAmount(value) {\\\\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\\\\n  return value.toFixed(2);\\\\n}\\\\nexport function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\\\\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\\\\nexport function sortAmounts(values) { return values.toSorted(); }\\\\n\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"order\": 14,\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs\",\n      \"coverage-absent-rename\",\n      \"coverage-absent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\n  \\\"command\\\": [\\n    \\\"bun\\\",\\n    \\\"--no-install\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\\\",\\n    \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/coverage-absent\\\"\\n  ],\\n  \\\"runtime\\\": \\\"1.4.2\\\",\\n  \\\"exitCode\\\": 0,\\n  \\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-positive\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"binary-negative\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"-1.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rounding\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-zero\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"NaN\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"negative-Infinity\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"null\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"empty-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": []\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"1.00\\\\\\\",\\\\n      \\\\\\\"-1.00\\\\\\\",\\\\n      \\\\\\\"12.35\\\\\\\"\\\\n    ]\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"row-error\\\\\\\",\\\\n    \\\\\\\"error\\\\\\\": {\\\\n      \\\\\\\"name\\\\\\\": \\\\\\\"Error\\\\\\\",\\\\n      \\\\\\\"message\\\\\\\": \\\\\\\"nonfinite\\\\\\\"\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-empty\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"export-rows\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": \\\\\\\"0.00\\\\\\\\n12.35\\\\\\\"\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"controller\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": {\\\\n      \\\\\\\"total\\\\\\\": 6.5\\\\n    }\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"observable-calculator-cache\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": 6.5\\\\n  },\\\\n  {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"known-unrelated-lexical-sort\\\\\\\",\\\\n    \\\\\\\"value\\\\\\\": [\\\\n      \\\\\\\"10\\\\\\\",\\\\n      \\\\\\\"2\\\\\\\"\\\\n    ]\\\\n  }\\\\n]\\\\n18 literal behavior checks matched.\\\\n\\\",\\n  \\\"stderr\\\": \\\"\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-before.json",
      "sha256": "73a06d5058907e142ecff402a54b4d70591450ef3302b45300ce759f0fab215b",
      "bytes": 2102,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-before.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-before.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-initial-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-initial-files.json",
      "sha256": "2b1f677b29eabbea93287ab9d147600a48e0dded6f57590ecc9c1d44ae5e8d83",
      "bytes": 107,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\"calculator.mjs\",\"exporter.mjs\",\"adapter.mjs\",\"facade.mjs\",\"controller.mjs\",\"decision.md\",\"formatter.mjs\"]"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-rename.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-rename.json",
      "sha256": "73a06d5058907e142ecff402a54b4d70591450ef3302b45300ce759f0fab215b",
      "bytes": 2102,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-rename.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-rename.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-state.json",
      "sha256": "73a06d5058907e142ecff402a54b4d70591450ef3302b45300ce759f0fab215b",
      "bytes": 2102,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-state.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-state.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-subtract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-subtract.json",
      "sha256": "73a06d5058907e142ecff402a54b4d70591450ef3302b45300ce759f0fab215b",
      "bytes": 2102,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable\"\n  ],\n  \"runtime\": \"1.4.2\",\n  \"exitCode\": 0,\n  \"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-positive\\\",\\n    \\\"value\\\": \\\"1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"binary-negative\\\",\\n    \\\"value\\\": \\\"-1.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"rounding\\\",\\n    \\\"value\\\": \\\"12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-zero\\\",\\n    \\\"value\\\": \\\"0.00\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"NaN\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"negative-Infinity\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"string\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"null\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"empty-rows\\\",\\n    \\\"value\\\": []\\n  },\\n  {\\n    \\\"name\\\": \\\"rows\\\",\\n    \\\"value\\\": [\\n      \\\"1.00\\\",\\n      \\\"-1.00\\\",\\n      \\\"12.35\\\"\\n    ]\\n  },\\n  {\\n    \\\"name\\\": \\\"row-error\\\",\\n    \\\"error\\\": {\\n      \\\"name\\\": \\\"Error\\\",\\n      \\\"message\\\": \\\"nonfinite\\\"\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"export-empty\\\",\\n    \\\"value\\\": \\\"\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"export-rows\\\",\\n    \\\"value\\\": \\\"0.00\\\\n12.35\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"controller\\\",\\n    \\\"value\\\": {\\n      \\\"total\\\": 6.5\\n    }\\n  },\\n  {\\n    \\\"name\\\": \\\"observable-calculator-cache\\\",\\n    \\\"value\\\": 6.5\\n  },\\n  {\\n    \\\"name\\\": \\\"known-unrelated-lexical-sort\\\",\\n    \\\"value\\\": [\\n      \\\"10\\\",\\n      \\\"2\\\"\\n    ]\\n  }\\n]\\n18 literal behavior checks matched.\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-subtract.stdout",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/evidence/workers-unavailable-subtract.stdout",
      "sha256": "5b87c8a019c9c6fce1782ae0deef88be9ed055df126e9cff73487ab1e9b7dca0",
      "bytes": 1456,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "[\n  {\n    \"name\": \"zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"binary-positive\",\n    \"value\": \"1.00\"\n  },\n  {\n    \"name\": \"binary-negative\",\n    \"value\": \"-1.00\"\n  },\n  {\n    \"name\": \"rounding\",\n    \"value\": \"12.35\"\n  },\n  {\n    \"name\": \"negative-zero\",\n    \"value\": \"0.00\"\n  },\n  {\n    \"name\": \"NaN\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"negative-Infinity\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"string\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"null\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"empty-rows\",\n    \"value\": []\n  },\n  {\n    \"name\": \"rows\",\n    \"value\": [\n      \"1.00\",\n      \"-1.00\",\n      \"12.35\"\n    ]\n  },\n  {\n    \"name\": \"row-error\",\n    \"error\": {\n      \"name\": \"Error\",\n      \"message\": \"nonfinite\"\n    }\n  },\n  {\n    \"name\": \"export-empty\",\n    \"value\": \"\"\n  },\n  {\n    \"name\": \"export-rows\",\n    \"value\": \"0.00\\n12.35\"\n  },\n  {\n    \"name\": \"controller\",\n    \"value\": {\n      \"total\": 6.5\n    }\n  },\n  {\n    \"name\": \"observable-calculator-cache\",\n    \"value\": 6.5\n  },\n  {\n    \"name\": \"known-unrelated-lexical-sort\",\n    \"value\": [\n      \"10\",\n      \"2\"\n    ]\n  }\n]\n18 literal behavior checks matched.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/finalize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/finalize.mjs",
      "sha256": "fb483e64bf793650da2d781c2d3efafdfdd6f81bdb801fb0f81422a538cdb17d",
      "bytes": 2532,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import { readFile,writeFile,readdir,cp } from 'node:fs/promises';\nconst root=import.meta.dir;\nconst commands=[];\nfor(const args of [['git','diff','--no-index','--','baseline','main'],['rg','-n','formatInvoice|formatThroughStrategy','main'],['rg','-n','formatAmount','main']]){const p=Bun.spawnSync(args,{cwd:root});commands.push({command:args,exitCode:p.exitCode,stdout:Buffer.from(p.stdout).toString(),stderr:Buffer.from(p.stderr).toString()});}\nawait writeFile(`${root}/evidence/final-diff-and-reference-queries.json`,JSON.stringify(commands,null,2));\nawait writeFile(`${root}/evidence/final.diff`,commands[0].stdout);\nconst checks=[];\nfor(const name of ['calculator.mjs','controller.mjs','adapter.mjs','facade.mjs'])checks.push({name,unchanged:(await readFile(`${root}/baseline/${name}`)).equals(await readFile(`${root}/main/${name}`))});\nconst main=await import(`${root}/main/formatter.mjs`);\nconst exporter=await import(`${root}/main/exporter.mjs`);\nconst report={commands:commands.map(({command,exitCode})=>({command,exitCode})),checks,oldApiAbsent:!('formatInvoice' in main),newApiPresent:typeof main.formatAmount==='function',symbolStrings:exporter.publicFixtureSymbols,readerLoad:{formatRowsToNativeBefore:3,formatRowsToNativeAfter:2,moduleMutableFormatterBindingsBefore:1,moduleMutableFormatterBindingsAfter:0,measurement:'source call-edge and binding count, not measured reader time'},runtime:Bun.version};\nawait writeFile(`${root}/evidence/final-inspection.json`,JSON.stringify(report,null,2));\nawait cp(`${root}/evidence/speculation-before.mjs`,`${root}/evidence/speculative-wrapper.mjs`);\nconst before=await readFile(`${root}/evidence/speculation-before.mjs`,'utf8');\nconst speculative=before.replace('export function formatInvoice(value) {','function formatThroughStrategy(value) {').replace('export function formatRows(rows)', 'export function formatInvoice(value) { return formatThroughStrategy(value); }\\nexport function formatRows(rows)');\nawait writeFile(`${root}/evidence/speculative-wrapper.mjs`,speculative);\nawait writeFile(`${root}/evidence/speculative-reversion.json`,JSON.stringify({note:'The speculative source is reconstructed byte-for-byte from the observed edit script and captured before bytes. The actual speculative execution is retained in after-speculation.json. It is not shipped.',speculativeSha256:new Bun.CryptoHasher('sha256').update(speculative).digest('hex'),restoredSha256:new Bun.CryptoHasher('sha256').update(before).digest('hex')},null,2));\nconsole.log(JSON.stringify(report,null,2));\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/how.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/how.md",
      "sha256": "7d06949c53b5ce9ef849a6adf661f658ce62dec56434f2a643dc11bf5fd4505f",
      "bytes": 2717,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Formatter architecture\n\nThis is a simple utility. The direct explainer role runs sequentially under the case owner, with no independent worker claim. Input revision is bca2ea20c7743bf7e07239688ed6228527f199fd. The installed instructions are version 0.1.0. Their association with source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c comes from the supplied task, not a Git checkout in the installed directory.\n\n## Overview\n\nThe CSV consumer calls exportAmounts in exporter.mjs. It calls formatRows, which maps each row total through formatInvoice. formatInvoice rejects nonfinite numbers with Error('nonfinite'), calls the private fixed wrapper, assigns lastFormatted, and returns that assignment. fixed has one caller and adds no formatting policy. lastFormatted has no reader outside that function and duplicates a return value.\n\n## Key concepts\n\nThe formatting domain is a finite Number displayed as a two-decimal string. The invariant is JavaScript Number.toFixed(2), including binary floating-point rounding. Input rows have a total property. The exporter joins the formatted strings with a newline. Number validation remains at the formatting boundary.\n\n## How it works\n\nexportAmounts calls formatRows, formatInvoice, then fixed and Number.toFixed. Empty rows map to an empty array, and export as an empty string. The calculator path is separate. invoiceController calls invoiceFacade, invoiceAdapter and calculate. calculate writes cachedTotal. inspectCachedTotal exposes it, so removing that cache would change observable behavior.\n\n## Where things live\n\nAll seven fixture files were read in full and copied before edits. formatter.mjs owns display policy. exporter.mjs owns CSV assembly and a string list of public fixture symbols. decision.md records historical rationale supplied as synthetic input. controller.mjs, facade.mjs, adapter.mjs and calculator.mjs own the calculation path. That calculation path remains byte-identical.\n\n## Gotchas\n\nsortAmounts sorts numeric strings lexically. The fixture declares this unrelated defect. The behavior pin keeps its current ['10','2'] output. No fix belongs in this structural change. The decision record is synthetic history, not evidence of a customer or external ticket.\n\n## Target\n\nKeep the existing module layout. Replace the formatter's hidden lastFormatted state with a direct string return. Remove fixed and rename the internal function formatInvoice to formatAmount in code, export symbol strings and decision prose in one wave. The call graph becomes exportAmounts, formatRows, formatAmount, Number.toFixed. The JavaScript function contract remains finite Number to string, or Error('nonfinite'). No new TypeScript or runtime abstraction is needed.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/decision.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main/decision.md",
      "sha256": "1e90b189bd332f6892f06b01fee8931dfaef724d4a661abf7d57f4190ace1172",
      "bytes": 1175,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Synthetic invoice decision record\n\nDisplay contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\n\nFixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatAmount and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\n\nCurrent internal formatting API for preserved-behavior is formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/exporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main/exporter.mjs",
      "sha256": "22018eca9aab2ac09a5e9319751d5c6d9a171b30812748a274d5c331d8c6b392",
      "bytes": 190,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import { formatRows } from './formatter.mjs';\nexport function exportAmounts(rows) { return formatRows(rows).join('\\n'); }\nexport const publicFixtureSymbols = ['formatAmount', 'formatRows'];\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/formatter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main/formatter.mjs",
      "sha256": "bf0206ae81c99c2761d7673c1508bf33d8845f158cd10198bf3908e851017089",
      "bytes": 369,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "export function formatAmount(value) {\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\n  return value.toFixed(2);\n}\nexport function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\nexport function sortAmounts(values) { return values.toSorted(); }\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/pin.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs",
      "sha256": "0934e4888d7dfda82e18b5f0a131d4061115e5ef9762291da3056ed0ebe1becd",
      "bytes": 1911,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { pathToFileURL } from 'node:url';\nimport { resolve } from 'node:path';\nconst dir=resolve(process.argv[2]);\nconst f=await import(pathToFileURL(resolve(dir,'formatter.mjs')));\nconst e=await import(pathToFileURL(resolve(dir,'exporter.mjs')));\nconst c=await import(pathToFileURL(resolve(dir,'controller.mjs')));\nconst calc=await import(pathToFileURL(resolve(dir,'calculator.mjs')));\nconst format=f.formatAmount??f.formatInvoice;\nconst observed=[];\nconst check=(name,fn,expected)=>{let result;try{result={value:fn()};}catch(error){result={error:{name:error.name,message:error.message}};}observed.push({name,...result});assert.deepEqual(result,expected,name);};\nfor(const [name,input,expected] of [['zero',0,'0.00'],['binary-positive',1.005,'1.00'],['binary-negative',-1.005,'-1.00'],['rounding',12.345,'12.35'],['negative-zero',-0,'0.00']])check(name,()=>format(input),{value:expected});\nfor(const [name,input] of [['NaN',NaN],['Infinity',Infinity],['negative-Infinity',-Infinity],['string','1.00'],['null',null]])check(name,()=>format(input),{error:{name:'Error',message:'nonfinite'}});\ncheck('empty-rows',()=>f.formatRows([]),{value:[]});\ncheck('rows',()=>f.formatRows([{total:1.005},{total:-1.005},{total:12.345}]),{value:['1.00','-1.00','12.35']});\ncheck('row-error',()=>f.formatRows([{total:Infinity}]),{error:{name:'Error',message:'nonfinite'}});\ncheck('export-empty',()=>e.exportAmounts([]),{value:''});\ncheck('export-rows',()=>e.exportAmounts([{total:0},{total:12.345}]),{value:'0.00\\n12.35'});\ncheck('controller',()=>c.invoiceController({rows:[{qty:2,unitPrice:3.25}]}),{value:{total:6.5}});\ncheck('observable-calculator-cache',()=>calc.inspectCachedTotal(),{value:6.5});\ncheck('known-unrelated-lexical-sort',()=>f.sortAmounts(['2','10']),{value:['10','2']});\nconsole.log(JSON.stringify(observed,null,2));\nconsole.log('18 literal behavior checks matched.');\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/prepare.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/prepare.mjs",
      "sha256": "9471c8ab575f439f38f6b9b18ff373e08caab0707705cb89ef86ecf7b9fbe52e",
      "bytes": 3907,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import { mkdir, readdir, cp, readFile, writeFile } from 'node:fs/promises';\nimport { join } from 'node:path';\nconst root = import.meta.dir;\nconst pkg = '/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0';\nconst input = '/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/invoice';\nawait mkdir(join(root, 'evidence'), {recursive:true});\nconst contracts = JSON.parse(await readFile(join(root,'../task-contracts.json'),'utf8'));\nconst contract=contracts.find(x=>x.id==='preserved-behavior');\nawait writeFile(join(root,'supplied-input.json'),JSON.stringify(contract,null,2));\nconst paths=contract.sourcePaths.map(p=>p==='agents/poteto-agent.md'?'references/agent-prompts/poteto-agent.md':p);\npaths.push('references/host-capabilities.md','references/model-roles.md','references/orchestration-contract.md','references/workflow-ownership.md','skills/arena/SKILL.md','skills/technical-writing/SKILL.md','skills/unslop/SKILL.md');\nconst receipt=[];\nfor(const path of paths){const bytes=await readFile(join(pkg,path));await mkdir(join(root,'source-reads',path,'..'),{recursive:true});await writeFile(join(root,'source-reads',path),bytes);receipt.push({path,sha256:new Bun.CryptoHasher('sha256').update(bytes).digest('hex'),bytes:bytes.length});}\nawait writeFile(join(root,'evidence/source-read-receipt.json'),JSON.stringify(receipt,null,2));\nconst ref=await readFile(join(pkg,'skills/poteto-mode/playbooks/refactoring.md'),'utf8');\nconst steps=ref.slice(ref.indexOf('1. Pin the behavior'),ref.indexOf('\\n\\n**Reply:**'));\nawait writeFile(join(root,'checklist.md'),'# Refactoring checklist\\n\\nReduced todo binding. This owned Markdown file substitutes for an unavailable todo operation.\\n\\n'+steps+'\\n\\n## Local scope\\n\\n- Parent evaluation controller retains integration ownership. This case owner writes only this directory and its result.\\n- Blocking first steps. Read contracts, trace fixtures, capture literal pre-edit outputs.\\n- Independent workstreams. None inside this case. Parent forbids nested workers because slots are owned. Mechanical edits and two design candidates run sequentially. Independent design and mechanical delegation gates remain unsatisfied.\\n- Shared mutable state. Single case owner writes the coupled formatter and exporter. Other cases have disjoint paths.\\n- Smallest safe decomposition. One formatter owner avoids concurrent rename edits. Baseline, subtraction, speculation and revert, then atomic API rename.\\n- Architect phases. Ground, Sketch, Agree, Implement, Scrap. Agree proceeds under local authorization. Scrap is unnecessary if the chosen shape holds.\\n- Arena phases. Frame, Fan out, Cross-judge, Pick, Graft, Verify. Fan out and fresh judge use sequential reduced comparison. No independent arena execution is claimed.\\n- Step 8 skip. Rebase, commits, pushes and PRs are forbidden. Full Opening a PR was read. No delivery branch executes.\\n');\nfor(const variant of ['baseline','main','workers-unavailable','execution-denied','coverage-absent']){await mkdir(join(root,variant),{recursive:true});await cp(input,join(root,variant),{recursive:true});}\nconst checks=[];\nfor(const name of await readdir(input)){const actual=await readFile(join(input,name));const result=Bun.spawnSync(['git','show','bca2ea20c7743bf7e07239688ed6228527f199fd:committed-inputs/additional/invoice/'+name],{cwd:join(root,'..')});checks.push({name,exitCode:result.exitCode,byteIdentical:Buffer.from(result.stdout).equals(actual),sha256:new Bun.CryptoHasher('sha256').update(actual).digest('hex')});}\nawait writeFile(join(root,'evidence/input-identity.json'),JSON.stringify({inputRevision:'bca2ea20c7743bf7e07239688ed6228527f199fd',currentHead:Buffer.from(Bun.spawnSync(['git','rev-parse','HEAD'],{cwd:join(root,'..')}).stdout).toString().trim(),checks},null,2));\nconsole.log(JSON.stringify({prepared:5,inputChecks:checks},null,2));\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/run.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/run.mjs",
      "sha256": "8c3cf320dcb5b92f675c4cb7b89da7413609a4043c1a75f006854941e3a73425",
      "bytes": 823,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import {writeFile,readFile} from 'node:fs/promises';\nconst stage=process.argv[2];const target=process.argv[3];\nconst command=['bun','--no-install',`${import.meta.dir}/pin.mjs`,`${import.meta.dir}/${target}`];\nconst p=Bun.spawnSync(command,{cwd:import.meta.dir});\nconst record={command,runtime:Bun.version,exitCode:p.exitCode,stdout:Buffer.from(p.stdout).toString(),stderr:Buffer.from(p.stderr).toString()};\nawait writeFile(`${import.meta.dir}/evidence/${stage}.json`,JSON.stringify(record,null,2));\nawait writeFile(`${import.meta.dir}/evidence/${stage}.stdout`,record.stdout);\nif(stage!=='before'){const baseline=await readFile(`${import.meta.dir}/evidence/before.stdout`,'utf8');if(baseline!==record.stdout)throw new Error('baseline output mismatch');}\nconsole.log(JSON.stringify(record,null,2));process.exit(p.exitCode);\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/supplied-input.json",
      "sha256": "61b8bfa24e37f3c212f30e57d48aeb5b4a05367713b8e14fff76a87c638255a3",
      "bytes": 6549,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "{\n  \"id\": \"preserved-behavior\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/refactoring.md\",\n    \"skills/poteto-mode/SKILL.md\",\n    \"agents/poteto-agent.md\",\n    \"skills/poteto-mode/playbooks/feature.md\",\n    \"skills/poteto-mode/playbooks/opening-a-pr.md\",\n    \"skills/how/SKILL.md\",\n    \"skills/figure-it-out/SKILL.md\",\n    \"skills/architect/SKILL.md\",\n    \"skills/principle-model-the-domain/SKILL.md\",\n    \"skills/principle-foundational-thinking/SKILL.md\",\n    \"skills/principle-redesign-from-first-principles/SKILL.md\",\n    \"skills/principle-subtract-before-you-add/SKILL.md\",\n    \"skills/principle-laziness-protocol/SKILL.md\",\n    \"skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md\",\n    \"skills/principle-prove-it-works/SKILL.md\",\n    \"skills/principle-minimize-reader-load/SKILL.md\",\n    \"skills/principle-sequence-verifiable-units/SKILL.md\",\n    \"skills/how/references/explorer-prompt.md\",\n    \"skills/how/references/explainer-prompt.md\",\n    \"skills/architect/references/runner-prompt.md\",\n    \"skills/architect/references/rationale-template.md\",\n    \"skills/architect/references/design-red-flags.md\"\n  ],\n  \"prompt\": \"Refactor a fixture invoice formatter by removing a one-caller wrapper and consolidating duplicated state. Preserve literal formatted outputs, empty inputs, rounding and errors. Capture the current outputs before edits. Rename its internal API and migrate code, string references, docs and back-references together. One fixture exposes an unrelated bug, which must stay separate. A speculative abstraction adds reader load and must be reverted. Permit local edits and execution but no external writes. Repeat with workers unavailable, execution denied and behavior coverage absent. Return the changed structure, held pin, equivalence proof, reader-load delta, shipped and reverted work.\",\n  \"requirements\": [\n    \"Read the full mode and eight-step Refactoring playbook, required leaves and routed companion contracts. Record steps before task-specific todos. Route large or cross-cutting work to figure-it-out and named redesigns that change behavior to Feature. Split newly discovered bugs or features out and deliver the structural change first against its pinned contract.\",\n    \"Use how to trace current behavior, then create and execute characterization tests, snapshots or an equivalence harness before moving structure. Write coverage first if absent. Type checks and lint are insufficient pins.\",\n    \"Name the missing domain structure and target module layout, types and call graph. Keep clear local boring code; new shape deletes branches or invalid states. Crossing a function boundary requires complete architect exploration with its runner prompts, rationale and candidate screening.\",\n    \"Subtract dead code, one-caller wrappers, redundant validators and orphan references before additions. Keep the smallest change that reaches the target and revert speculation.\",\n    \"Each small move keeps the original pin green. Migrate every API caller and delete the old API in the same wave without compatibility shims or parallel paths. Inspect actual files for rename usages in strings, prose and back-references. Delegate mechanical edits with the complete poteto prompt, exact revision, ownership and observed inherited or supported configured selection. Inspect artifacts and review the diff.\",\n    \"Verify unchanged behavior on the real artifact. Larger reshapes require old/new output diffs, baseline replay or a matching-surface smoke run through actual authorized controls. Retain outputs and failures.\",\n    \"Assess reduced layers to trace and state to hold. Revert a diff that lowers neither. Do not invent measured reader times.\",\n    \"Order verified subtraction, reshape and cleanup units. Rebase, commit and run complete Opening a PR only when authorized and available. Retain deferred dependencies and unperformed actions. Return all reply artifacts and no new behavior.\"\n  ],\n  \"expectedFull\": \"Observed authorized independent mechanical delegation returns inspected artifacts at the assigned revision. The before-edit pin and each subsequent step have matching literal output evidence, including errors and rounding. All callers and textual references move together and the old API disappears. Architecture exploration runs when triggered. The actual artifact has equivalence proof and a source-grounded reader-load reduction. Bug work remains separate and speculation is reverted. With explicit delivery authorization and complete dependencies, ordered green commits and an inspected PR establish delivery. Without external authorization, external delivery remains unperformed.\",\n  \"expectedReduced\": \"Unavailable workers permit authorized sequential edits and local equivalence checks with reduced capability disclosed. Independent delegation and parallel design remain unsatisfied. Denied writes allow only a source-grounded target shape and ordered proposal. No external authorization yields a checked local diff and delivery plan rather than a PR. Unknown actual models prove no diversity.\",\n  \"expectedBlocked\": \"Missing source or required leaves stops dependent work. No executable behavior pin blocks structure moves and unchanged-behavior claims. Denied equivalence execution or matching controls leaves behavior unverified. Missing independent operations block required independence rather than waive it. Missing Opening a PR stops PR-dependent work. Unauthorized writes, rebase, commits or PR creation stay unperformed.\",\n  \"forbiddenClaims\": [\n    \"Compilation, lint or structural validation proves unchanged behavior.\",\n    \"A pin captured after edits proves the pre-change contract.\",\n    \"New behavior or an unrelated bug fix belongs in the structural change.\",\n    \"Sequential roles prove independent delegation, parallel exploration or review.\",\n    \"The historical grok-4.7-xhigh-fast default proves current model availability, selection or diversity.\",\n    \"Requested or inherited models are actual observed models.\",\n    \"Caller migration is complete without checking strings, prose and back-references.\",\n    \"Compatibility shims or dual APIs satisfy the same-wave deletion gate.\",\n    \"Unrun checks are green or reader time was measured without observation.\",\n    \"Missing companion execution or deferred PR routing succeeded.\",\n    \"A draft plan is a created PR, external autonomy authorizes writes, or opening a PR starts Babysit.\",\n    \"Helper fixtures prove this host case passed.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/refactoring.json\"\n}"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/variants.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/variants.mjs",
      "sha256": "9395116e41bf80eef4c4f60d93b5a35d2d73f4df04bba6f260601282bb4474ad",
      "bytes": 1652,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import { readFile,writeFile,readdir } from 'node:fs/promises';\nconst root=import.meta.dir;\nconst events=[];\nasync function command(args){const p=Bun.spawnSync(['bun','--no-install',...args],{cwd:root});const event={order:events.length+1,command:['bun','--no-install',...args],exitCode:p.exitCode,stdout:Buffer.from(p.stdout).toString(),stderr:Buffer.from(p.stderr).toString()};events.push(event);if(p.exitCode!==0)throw new Error(JSON.stringify(event));return event;}\nfor(const variant of ['workers-unavailable','coverage-absent']){\n  const files=await readdir(`${root}/${variant}`);\n  await writeFile(`${root}/evidence/${variant}-initial-files.json`,JSON.stringify(files));\n  await command([`${root}/run.mjs`,`${variant}-before`,variant]);\n  for(const stage of ['subtract','state','rename']){await command([`${root}/change.mjs`,variant,stage]);await command([`${root}/run.mjs`,`${variant}-${stage}`,variant]);}\n}\nconst same=[];\nfor(const name of await readdir(`${root}/baseline`)){const baseline=await readFile(`${root}/baseline/${name}`);const denied=await readFile(`${root}/execution-denied/${name}`);same.push({name,byteIdentical:baseline.equals(denied)});}\nawait writeFile(`${root}/evidence/execution-denied.json`,JSON.stringify({condition:'simulated policy restriction, not enforced by host',variantExecution:'not-run',pin:'unrun',structuralEdits:'none',equivalence:'unverified',sourceBytes:same},null,2));\nawait writeFile(`${root}/evidence/variant-commands.json`,JSON.stringify(events,null,2));\nconsole.log(JSON.stringify({runtime:Bun.version,events:events.map(({order,command,exitCode})=>({order,command,exitCode})),deniedBytes:same},null,2));\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/decision.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable/decision.md",
      "sha256": "1e90b189bd332f6892f06b01fee8931dfaef724d4a661abf7d57f4190ace1172",
      "bytes": 1175,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# Synthetic invoice decision record\n\nDisplay contract: JavaScript Number.toFixed(2), including its binary floating-point rounding behavior. Do not silently replace this with accounting decimal rules. Empty row lists produce []. Nonfinite amounts throw Error('nonfinite'). Capture observed outputs before edits for 0, 1.005, -1.005, 12.345, empty rows, NaN and Infinity. Output examples in a test are expectations, not proof a test ran.\n\nFixture history decision: a UI consumer compares two-decimal strings and a CSV consumer imports formatRows. This is why rounding belongs at the display boundary. No customer statement or external ticket was retrieved. Errors are thrown by formatAmount and are not swallowed by the controller. Alternative A removes fixed and lastFormatted; alternative B introduces a stateful Formatter class. Compare reader cost and behavioral equivalence.\n\nCurrent internal formatting API for preserved-behavior is formatAmount. Migrate imports, docs and string references together. sortAmounts is a known unrelated defect and must remain separate. Calculator cache is observable through inspectCachedTotal; changing it requires checking that consumer.\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/exporter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable/exporter.mjs",
      "sha256": "22018eca9aab2ac09a5e9319751d5c6d9a171b30812748a274d5c331d8c6b392",
      "bytes": 190,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "import { formatRows } from './formatter.mjs';\nexport function exportAmounts(rows) { return formatRows(rows).join('\\n'); }\nexport const publicFixtureSymbols = ['formatAmount', 'formatRows'];\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/formatter.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/workers-unavailable/formatter.mjs",
      "sha256": "bf0206ae81c99c2761d7673c1508bf33d8845f158cd10198bf3908e851017089",
      "bytes": 369,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "export function formatAmount(value) {\n  if (!Number.isFinite(value)) throw new Error('nonfinite');\n  return value.toFixed(2);\n}\nexport function formatRows(rows) { return rows.map(row => formatAmount(row.total)); }\n// Separate known bug, outside formatter refactor: this sorts numeric strings lexically.\nexport function sortAmounts(values) { return values.toSorted(); }\n"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior.result.md",
      "sha256": "341fe4c8c27dcd65a5c930a62a5b52649e1432dcce843d158ab418464dac4050",
      "bytes": 11924,
      "owners": [
        "grades-native-10.json#3"
      ],
      "text": "# preserved-behavior\n\nThe fixture formatter now returns the formatted string directly. The private `fixed` wrapper and unobserved `lastFormatted` state are removed. Its internal API is `formatAmount`. Code, symbol-name strings and decision prose moved together. No formatting behavior changed in the 18 observed cases. The unrelated lexical sort defect and observable calculator cache remain intact.\n\n## Supplied input and identity\n\nThe complete supplied case is retained in [supplied-input.json](preserved-behavior/supplied-input.json). The requested action was to preserve literal formatting, rounding, errors and empty inputs while removing a one-caller wrapper, consolidating state, migrating the API, keeping an unrelated bug separate, and reverting speculative abstraction. The requested variants were workers unavailable, execution denied and behavior coverage absent.\n\nThe actual input commit is `bca2ea20c7743bf7e07239688ed6228527f199fd`. `git cat-file -t` returned `commit`, `git show` exposed the committed inputs, and `git rev-parse HEAD` returned that exact SHA. Every shared invoice input was compared byte-for-byte with its `committed-inputs/additional/invoice/` Git blob. All seven matched. The checks and SHA-256 hashes are in [input-identity.json](preserved-behavior/evidence/input-identity.json). Output artifacts were created after that revision and are not claimed as part of its tree.\n\nOnly `/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0` supplied workflow instructions. The installed plugin manifests identify version `0.1.0`. The requested package source freeze is `f4623636a287bea2aa79c4b2234a53d20a5f193c`. The installed directory has no Git metadata. Its association with that freeze is supplied task context, not independently proven Git commit identity. The parent support case retains the installed byte-copy manifest in [copy-identity.json](package-support-contracts/copy-identity.json). No other package version was read.\n\n## Reads and ownership\n\nAll named mode, Refactoring, Feature, Opening a PR, how, figure-it-out, architect, principle leaves and prompt files were read through `functions.exec` and `tools.exec_command` with complete output. Their owned byte copies and hashes are in [source-reads](preserved-behavior/source-reads) and [source-read-receipt.json](preserved-behavior/evidence/source-read-receipt.json). The contract's historical `agents/poteto-agent.md` pointer was resolved to the user's actual named `references/agent-prompts/poteto-agent.md` path. The host-capability, ownership, assignment, model-role, Arena, technical-writing and unslop contracts were also read in full. Additional applied leaf reads included exhaust-the-design-space, separate-before-serializing-shared-state, boundary-discipline, encode-lessons-in-structure, make-operations-idempotent and test-behavior-not-implementation.\n\nThe parent evaluation controller owns integration. This native worker owns `preserved-behavior/` and this result file. No nested workers were allowed by the parent assignment. The worker directly owned its diff and returned it for parent review, as the mode's forbidden-to-spawn exception requires. Requested selection was inherited. Actual model and effort are unknown. No independent design competition or model diversity is claimed.\n\nThe eight Refactoring steps were copied verbatim before task-specific items into [checklist.md](preserved-behavior/checklist.md). This is an authorized Markdown substitute for an unavailable todo operation. The throughput checkpoint is retained there. [how.md](preserved-behavior/how.md) traces the real formatter, exporter and calculation paths. [design.md](preserved-behavior/design.md) records two structurally distinct sequential candidates, usage-first sketches, red-flag screening, a selected direct-function shape and the rejected stateful-class shape. Parallel architect candidates and fresh Arena judgment remain unsatisfied. Figure-it-out was read but not activated because this is a focused change. The unrelated bug is not routed into this change. No Feature implementation ran.\n\n## Actual actions and output\n\n`prepare.mjs` copied required inert input files before edits into `baseline`, `main`, `workers-unavailable`, `execution-denied` and `coverage-absent`. `pin.mjs` was written and executed against untouched `main` before any production edit. `run.mjs` retained each command, Bun version, exit code, stdout and stderr. Execution used Bun `1.4.2` with `--no-install`. No dependency was installed.\n\nThe first actual command was `bun --no-install preserved-behavior/run.mjs before main`. Its child command was `bun --no-install /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/pin.mjs /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/preserved-behavior/main`. It exited `0` with empty stderr. Its verbatim output is [before.stdout](preserved-behavior/evidence/before.stdout), and its complete invocation record is [before.json](preserved-behavior/evidence/before.json).\n\nThe observed literal outputs include `0.00`, `1.00` for `1.005`, `-1.00` for `-1.005`, `12.35` for `12.345`, empty rows `[]`, empty export `''`, and Error with message `nonfinite` for NaN, either Infinity, a string, null and a nonfinite row. Exported rows produced `0.00\\n12.35`. The controller returned `{total:6.5}`, and `inspectCachedTotal()` returned `6.5`. The unrelated lexical sort returned `['10','2']` and remains pinned as its current behavior. These are runtime observations from copied synthetic input, with no real service contact.\n\nThe ordered main changes and checks were:\n\n| Unit | Retained actual output | Exit |\n| --- | --- | --- |\n| Before edits | [before.json](preserved-behavior/evidence/before.json) | 0 |\n| Remove fixed wrapper | [after-subtraction.json](preserved-behavior/evidence/after-subtraction.json) | 0 |\n| Replace lastFormatted with return value | [after-state.json](preserved-behavior/evidence/after-state.json) | 0 |\n| Add speculative formatThroughStrategy delegate | [after-speculation.json](preserved-behavior/evidence/after-speculation.json) | 0 |\n| Revert speculative delegate | [after-revert.json](preserved-behavior/evidence/after-revert.json) | 0 |\n| Atomic API and textual-reference rename | [after-rename.json](preserved-behavior/evidence/after-rename.json) | 0 |\n| Final artifact after prose correction | [final-main.json](preserved-behavior/evidence/final-main.json) | 0 |\n\nEvery output above is byte-identical to the before-edit stdout. Each contains the actual line `18 literal behavior checks matched.` The equivalence check compares retained complete stdout, not compilation or structural validation. The finite test set does not prove every possible JavaScript input equivalent.\n\nThe speculative wrapper was actually written, executed and reverted. Its execution preserved behavior but added an unnecessary call layer. The exact before bytes and a disclosed reconstruction of the speculative bytes are retained in [speculation-before.mjs](preserved-behavior/evidence/speculation-before.mjs), [speculative-wrapper.mjs](preserved-behavior/evidence/speculative-wrapper.mjs) and [speculative-reversion.json](preserved-behavior/evidence/speculative-reversion.json). The reconstructed source is not misrepresented as a separate captured original file.\n\n## Variants\n\n| Variant | Actual attempt and result | Limit |\n| --- | --- | --- |\n| Main native worker | Copied fixture, pre-edit pin, sequential edits, stage replay, parent diff review. | Parent could spawn this worker. No nested independent mechanical delegate or architect candidate was used. |\n| Workers unavailable | A separate untouched copy received its own pre-edit replay, subtraction, state removal and rename. Each stage exited 0 and matched the original stdout. | Worker unavailability is a simulated case policy. The host exposes collaboration tools. Required independent architecture and nested delegation remain unsatisfied. |\n| Execution denied | Retained a separate original copy, source-grounded target and ordered proposal. No behavior pin, production edit or equivalence run targeted this copy. All seven source files remain byte-identical to baseline. | Denial is simulated, not enforced by the host. Variant behavior is unverified and unchanged-behavior claims are withheld. File inspection and report creation still used authorized host execution outside that simulated branch. |\n| Behavior coverage absent | Initial files contain no tests. The new characterization pin was run against this copy before its first edit. Subtraction, state removal and rename each retained the literal outputs. Final check exited 0. | Coverage absence is real for the prepared fixture. The external case-owned pin supplies coverage first. It is not a pre-existing test suite. |\n\nVariant commands, their order and complete output are in [variant-commands.json](preserved-behavior/evidence/variant-commands.json). Initial directory inventories are retained beside them. The denied branch is in [execution-denied.json](preserved-behavior/evidence/execution-denied.json). Final checks are in [final-workers-unavailable.json](preserved-behavior/evidence/final-workers-unavailable.json) and [final-coverage-absent.json](preserved-behavior/evidence/final-coverage-absent.json).\n\n## Reviewed structure and limits\n\nThe checked local patch is [final.diff](preserved-behavior/evidence/final.diff). The actual Git no-index diff exits `1` because differences exist. This is expected diff behavior, not a test failure. Actual `rg` queries found no old `formatInvoice` or speculative `formatThroughStrategy` reference in `main`, exiting `1` for no matches. The new-name query found the definition, call, symbol string and decision prose, exiting `0`. Their complete output is in [final-diff-and-reference-queries.json](preserved-behavior/evidence/final-diff-and-reference-queries.json). Baseline and historical evidence intentionally retain old names.\n\n[final-inspection.json](preserved-behavior/evidence/final-inspection.json) confirms the old API is absent, the new API exists, symbol strings contain the new name, and calculator, controller, facade and adapter bytes are unchanged. The parent inspected the actual diff and 18-check output. It found a mechanical prose corruption and requested clearer wording plus accurate Arena disclosure. Both were corrected. [lead-review.md](preserved-behavior/evidence/lead-review.md) records the actual collaboration review, without inventing model identities or independent Arena judging.\n\nSource inspection counts the formatter path from `formatRows` to native `toFixed` as three call edges before and two after. Mutable formatter module bindings fall from one to zero. These are source counts, not measured reader time. The speculative layer lowered neither axis and was reverted. Model the Domain and Foundational Thinking selected the direct function. Laziness Protocol, Subtract Before You Add and Minimize Reader Load rejected extra indirection. Migrate Callers Then Delete Legacy APIs required coordinated rename deletion. Prove It Works, Test Behavior Not Implementation and Sequence Work into Verifiable Units required literal replays after each move.\n\nThe shipped scope is a local reviewable patch only. No commit, rebase, push, PR, publish, account write, schedule or live service operation occurred. The delivery order remains baseline pin, verified subtraction, state reshape, coordinated rename and prose cleanup. Those are ordered local artifacts, not landed history. Opening a PR was read in full but its external branch was not authorized. External deslop and matching UI or CLI companions did not run. A standalone module execution check proves the selected library behavior only. Required independent architect exploration and fresh cross-judge are still open. No self-grade is assigned.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/decision.md",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/exporter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/formatter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/source-read-receipt.json",
      "owner": "grades-native-10.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/decision.md",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/exporter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/formatter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/source-reads",
      "owner": "grades-native-10.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/decision.md",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/exporter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/baseline/formatter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/coverage-absent/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/evidence/source-read-receipt.json",
      "owner": "grades-native-10.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/decision.md",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/exporter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/execution-denied/formatter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/main/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/source-reads",
      "owner": "grades-native-10.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/adapter.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/calculator.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/controller.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "fixtures/batch-10/preserved-behavior/workers-unavailable/facade.mjs",
      "owner": "grades-native-10.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    }
  ],
  "globalLimits": [
    "Orchestrator receipt durations can include controller pauses; they are not inferred native case execution times or benchmark measurements.",
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
