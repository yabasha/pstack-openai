# codex: prose-rewrite

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "prose-rewrite",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-03.json#5",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.",
  "caseDefinition": {
    "id": "prose-rewrite",
    "sourcePaths": [
      "skills/unslop/SKILL.md"
    ],
    "prompt": "Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.",
    "requirements": [
      "Access to the supplied draft and the complete unslop pattern list.",
      "Preserve intended meaning and tone, stable rule IDs, and all original pattern examples in the skill.",
      "Remove applicable upstream pattern examples from rewritten prose without adding sources, metrics, mechanisms, or outcomes."
    ],
    "expectedFull": "Return plain prose that removes chatbot praise, fancy substitutes for is, superficial -ing phrases, AI vocabulary, contrast framing, filler, jargon, and unnecessary passive voice while retaining supported meaning. Apply all applicable numbered rules through 33, including dense sentences, adverbs, mannered prose, and over-compression.",
    "expectedReduced": "If only part of the draft is accessible, rewrite that part and state the scope limit. Lack of file-write permission still permits an in-chat rewrite; do not claim a saved edit.",
    "expectedBlocked": "If the draft is absent or unreadable, request the actual text and do not invent a rewrite or claim completion.",
    "forbiddenClaims": [
      "New facts, invented citations, measured deltas, or mechanisms absent from the draft.",
      "A file was edited without an observed authorized write.",
      "Host enforcement of disable-model-invocation or host behavioral parity based on structural checks."
    ],
    "caseFile": "docs/parity/cases/skills/unslop.json"
  },
  "registry": {
    "caseId": "prose-rewrite",
    "caseFile": "docs/parity/cases/skills/unslop.json",
    "sourcePaths": [
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
        "supplied-input",
        "response",
        "review-outcome"
      ],
      "reduced-pass": [
        "supplied-input",
        "response",
        "review-outcome"
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
      "attemptId": "grades-native-03.json#5",
      "order": 0,
      "gradeFile": "grades-native-03.json",
      "rankWithinFile": 5,
      "host": "codex",
      "caseId": "prose-rewrite",
      "status": "pass",
      "grade": {
        "caseId": "prose-rewrite",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_7",
          "item_19"
        ],
        "rawTrace": "codex/batch-03.events.jsonl",
        "responseArtifact": "fixtures/batch-03/prose-rewrite.result.md",
        "requiredObservationsMet": [
          "supplied-input",
          "response",
          "review-outcome"
        ],
        "missing": [],
        "review": "Rewrite removes praise, flourish, serves-as, contrast and passive/filler wording while preserving loader centrality/speed/importance/parsing. Full installed canonical rules audited with stable numbering gaps and original examples retained; no skill edit or invented facts.",
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
        "fullExpected": "Return plain prose that removes chatbot praise, fancy substitutes for is, superficial -ing phrases, AI vocabulary, contrast framing, filler, jargon, and unnecessary passive voice while retaining supported meaning. Apply all applicable numbered rules through 33, including dense sentences, adverbs, mannered prose, and over-compression.",
        "reducedExpected": "If only part of the draft is accessible, rewrite that part and state the scope limit. Lack of file-write permission still permits an in-chat rewrite; do not claim a saved edit."
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
        "text": "# prose-rewrite\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"prose-rewrite\",\n  \"prompt\": \"Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.\",\n  \"requirements\": [\n    \"Access to the supplied draft and the complete unslop pattern list.\",\n    \"Preserve intended meaning and tone, stable rule IDs, and all original pattern examples in the skill.\",\n    \"Remove applicable upstream pattern examples from rewritten prose without adding sources, metrics, mechanisms, or outcomes.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/unslop/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 4. See [source-reads.json](prose-rewrite/source-reads.json). Supplied input archive: [supplied-input.json](prose-rewrite/supplied-input.json).\n\n## Actual response and variants\n\nThe loader is central, fast and essential. To use it, the loader parses the file.\n\nThis retains the draft's centrality, speed, importance and parsing relationship. The phrase about a vibrant paradigm supplies no concrete claim, so it was removed rather than converted into an invented mechanism. The final sentence preserves the draft's use/parsing relationship without assuming who supplies or invokes the file.\n\nI read the entire installed Unslop skill. rule-audit.json preserves the exact canonical text and original examples for every numbered rule, and source/skills/unslop/SKILL.md is the complete unchanged snapshot. Stable IDs present are 3, 5, 7 through 20, and 22 through 33. Gaps 1, 2, 4, 6 and 21 remain gaps. There are 28 numbered rules. No skill was edited or renumbered.\n\nApplicable edits remove praise under 22; superficial highlighting under 3; vibrant/crucial under 7; serves as under 8; contrast framing under 9; filler under 23; paradigm under 26; passive parsing under 29; utilize under 31; and rhetorical fragments under 32 and 33. Rule 27 removes the unsupported flourish. All other rules and their examples were inspected, including 28 and 30, with no invented sources, measurements or outcomes added.\n\nVariant attempted: complete supplied draft and full pattern list available. Rewrite saved as response.txt. Audit is canonical preservation and an editorial check, not evidence that every original example occurred in the draft. No external source was needed.\n\n## Real command results\n\nNo case-specific product command was run. Source reads, inert preparation and output persistence used the setup/report scripts through the actual tools named above.\n\n## Artifacts\n\n- [prose-rewrite/response.md](prose-rewrite/response.md)\n- [prose-rewrite/rule-audit.json](prose-rewrite/rule-audit.json)\n- [prose-rewrite/source-reads.json](prose-rewrite/source-reads.json)\n- [prose-rewrite/supplied-input.json](prose-rewrite/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n",
        "artifact": {
          "path": "fixtures/batch-03/prose-rewrite.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/prose-rewrite.result.md",
          "sha256": "78ba74bb6f1b6babb0ad759bafa50e9aebdef5b516ce79559b07186ed3c17d18",
          "bytes": 4628
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
      "path": "fixtures/batch-03/prose-rewrite/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/prose-rewrite/response.md",
      "sha256": "3357a39a0c130d96d9c7bfbe17afc1205277c7968708cdfb6a9f89877ab887a3",
      "bytes": 1485,
      "owners": [
        "grades-native-03.json#5"
      ],
      "text": "The loader is central, fast and essential. To use it, the loader parses the file.\n\nThis retains the draft's centrality, speed, importance and parsing relationship. The phrase about a vibrant paradigm supplies no concrete claim, so it was removed rather than converted into an invented mechanism. The final sentence preserves the draft's use/parsing relationship without assuming who supplies or invokes the file.\n\nI read the entire installed Unslop skill. rule-audit.json preserves the exact canonical text and original examples for every numbered rule, and source/skills/unslop/SKILL.md is the complete unchanged snapshot. Stable IDs present are 3, 5, 7 through 20, and 22 through 33. Gaps 1, 2, 4, 6 and 21 remain gaps. There are 28 numbered rules. No skill was edited or renumbered.\n\nApplicable edits remove praise under 22; superficial highlighting under 3; vibrant/crucial under 7; serves as under 8; contrast framing under 9; filler under 23; paradigm under 26; passive parsing under 29; utilize under 31; and rhetorical fragments under 32 and 33. Rule 27 removes the unsupported flourish. All other rules and their examples were inspected, including 28 and 30, with no invented sources, measurements or outcomes added.\n\nVariant attempted: complete supplied draft and full pattern list available. Rewrite saved as response.txt. Audit is canonical preservation and an editorial check, not evidence that every original example occurred in the draft. No external source was needed.\n"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite/response.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/prose-rewrite/response.txt",
      "sha256": "911b9ac8dd84733a3f6f0c25f6bc2ffe78217f1f99616fbf3903338f31a96023",
      "bytes": 82,
      "owners": [
        "grades-native-03.json#5"
      ],
      "text": "The loader is central, fast and essential. To use it, the loader parses the file.\n"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite/rule-audit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/prose-rewrite/rule-audit.json",
      "sha256": "d39f2e2e9599d44662fecf3339b0a2a6666bd0081e42662218936053974cbf1f",
      "bytes": 7447,
      "owners": [
        "grades-native-03.json#5"
      ],
      "text": "{\n  \"rules\": [\n    {\n      \"id\": 3,\n      \"canonicalRuleAndExamples\": \"Superficial -ing phrases.** \\\"highlighting...\\\", \\\"ensuring...\\\", \\\"reflecting...\\\", \\\"showcasing...\\\", \\\"fostering...\\\". Delete or expand with real sources.\"\n    },\n    {\n      \"id\": 5,\n      \"canonicalRuleAndExamples\": \"Vague attributions.** \\\"Experts believe\\\", \\\"Industry reports suggest\\\", \\\"Some critics argue\\\". Name the source or delete.\"\n    },\n    {\n      \"id\": 7,\n      \"canonicalRuleAndExamples\": \"AI vocabulary.** Additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore, vibrant. Replace with plain words.\"\n    },\n    {\n      \"id\": 8,\n      \"canonicalRuleAndExamples\": \"Fancy ways to say \\\"is\\\".** \\\"serves as\\\", \\\"stands as\\\", \\\"boasts\\\", \\\"features\\\". Just say \\\"is\\\" or \\\"has\\\".\"\n    },\n    {\n      \"id\": 9,\n      \"canonicalRuleAndExamples\": \"\\\"Not just X, but Y.\\\"** State the point directly instead.\"\n    },\n    {\n      \"id\": 10,\n      \"canonicalRuleAndExamples\": \"Rule of three.** Forcing ideas into groups of three. Use the natural number.\"\n    },\n    {\n      \"id\": 11,\n      \"canonicalRuleAndExamples\": \"Synonym cycling.** Protagonist, main character, central figure, hero all in one paragraph. Pick one, repeat it.\"\n    },\n    {\n      \"id\": 12,\n      \"canonicalRuleAndExamples\": \"False ranges.** \\\"from X to Y\\\" where X and Y aren't on a meaningful scale. List topics directly.\"\n    },\n    {\n      \"id\": 13,\n      \"canonicalRuleAndExamples\": \"Em dash overuse.** Avoid em dashes entirely. Use periods or commas only (no parentheses, no en dashes, no hyphen-as-dash substitutes). If a thought needs separation, end the sentence or use a comma.\"\n    },\n    {\n      \"id\": 14,\n      \"canonicalRuleAndExamples\": \"Colon overuse.** Colons are fine before a list or example. Not as mid-sentence connectors. \\\"If you're coming from traditional automation: instead of registering event handlers, you describe conditions\\\" adds nothing with the colon. Rewrite to let the point stand on its own without comparison framing. \\\"Describing when the scheduler should fire works best as plain English.\\\" Same meaning, no crutch punctuation.\"\n    },\n    {\n      \"id\": 15,\n      \"canonicalRuleAndExamples\": \"Boldface overuse.** Don't bold every proper noun or acronym.\"\n    },\n    {\n      \"id\": 16,\n      \"canonicalRuleAndExamples\": \"Inline-header lists.** The tell is a bold label and colon that restates the line: \\\"**Performance:** Performance improved...\\\". Convert those to prose. A bold lead-in that ends in a period, names the item, and is followed by genuinely new detail (\\\"**Schema in TypeScript.** Tables live in one file.\\\") is fine, not a tell.\"\n    },\n    {\n      \"id\": 17,\n      \"canonicalRuleAndExamples\": \"Title case headings.** Use sentence case.\"\n    },\n    {\n      \"id\": 18,\n      \"canonicalRuleAndExamples\": \"Decorative emojis.** Remove from headings and bullets.\"\n    },\n    {\n      \"id\": 19,\n      \"canonicalRuleAndExamples\": \"Curly quotes.** Replace with straight quotes.\"\n    },\n    {\n      \"id\": 20,\n      \"canonicalRuleAndExamples\": \"Chatbot phrases.** \\\"I hope this helps!\\\", \\\"Let me know if...\\\", \\\"Of course!\\\", \\\"Certainly!\\\", \\\"Found the smoking gun!\\\" Remove.\"\n    },\n    {\n      \"id\": 22,\n      \"canonicalRuleAndExamples\": \"Sycophantic tone.** \\\"Great question! You're absolutely right!\\\" Respond directly.\"\n    },\n    {\n      \"id\": 23,\n      \"canonicalRuleAndExamples\": \"Filler phrases.** \\\"In order to\\\" becomes \\\"To\\\". \\\"Due to the fact that\\\" becomes \\\"Because\\\". \\\"It is important to note that\\\" gets deleted.\"\n    },\n    {\n      \"id\": 24,\n      \"canonicalRuleAndExamples\": \"Excessive hedging.** \\\"could potentially possibly be argued that it might\\\" becomes \\\"may\\\".\"\n    },\n    {\n      \"id\": 25,\n      \"canonicalRuleAndExamples\": \"Generic conclusions.** \\\"The future looks bright.\\\" State specific plans or facts.\"\n    },\n    {\n      \"id\": 26,\n      \"canonicalRuleAndExamples\": \"Abstract metaphor nouns.** Substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in \\\"API surface\\\"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. These read as technical but usually have a plainer concrete word. \\\"Substrate\\\" becomes \\\"base\\\". \\\"Wedge in\\\" becomes \\\"add\\\". \\\"Vector\\\" becomes \\\"way\\\" or \\\"method\\\". \\\"Gold-plating\\\" becomes \\\"more than the job needs\\\". \\\"Ratchet\\\" becomes the mechanism's real name or \\\"a limit that only tightens\\\". \\\"Evacuate\\\" becomes \\\"move out\\\". \\\"Endgame\\\" becomes \\\"the last phase\\\". Pick the concrete word.\"\n    },\n    {\n      \"id\": 27,\n      \"canonicalRuleAndExamples\": \"Say what it does, not how it feels.** \\\"the database stays close at hand\\\", \\\"SQL you can read\\\", \\\"types that follow your schema\\\" name a feeling. The fix names the mechanism or a number: \\\"`.toSQL()` returns the exact string sent to the database\\\", \\\"a column rename fails the build\\\". Ask what the sentence tells the reader to do or know, then write that. If you can't restate it as a concrete instruction, fact, or number, cut it. One more check: if the sentence could appear unchanged in another project's docs, it says nothing about this one. Cut it.\"\n    },\n    {\n      \"id\": 28,\n      \"canonicalRuleAndExamples\": \"Shorten or split dense sentences.** If the reader has to backtrack to parse a sentence, break it in two or drop clauses. One idea per sentence.\"\n    },\n    {\n      \"id\": 29,\n      \"canonicalRuleAndExamples\": \"Active voice.** Prefer it. Catch \\\"is/are/was/were + past participle\\\" and name the actor: \\\"queries are validated\\\" becomes \\\"the compiler validates queries\\\", \\\"the file is parsed by the loader\\\" becomes \\\"the loader parses the file\\\". Passive is fine only when the actor is unknown or genuinely doesn't matter.\"\n    },\n    {\n      \"id\": 30,\n      \"canonicalRuleAndExamples\": \"Cut adverbs, or use a stronger verb.** \\\"runs quickly\\\" becomes \\\"is fast\\\" or the number. \\\"significantly improves\\\" becomes the measured delta. An adverb propping up a weak verb means the verb is wrong.\"\n    },\n    {\n      \"id\": 31,\n      \"canonicalRuleAndExamples\": \"Prefer the plain word.** \\\"utilize\\\" becomes \\\"use\\\", \\\"leverage\\\" becomes \\\"use\\\", \\\"facilitate\\\" becomes \\\"help\\\", \\\"numerous\\\" becomes \\\"many\\\", \\\"in the event that\\\" becomes \\\"if\\\". The fancier synonym is rarely clearer.\"\n    },\n    {\n      \"id\": 32,\n      \"canonicalRuleAndExamples\": \"Mannered prose.** Metaphor or flourish where a literal phrase exists: aphorisms (\\\"wire it or delete it\\\"), rhetorical fragments for effect, personified code (\\\"the plan holds it\\\"), figurative verbs (\\\"rides along\\\", \\\"stands on\\\"), stock framing phrases. \\\"A dial worth turning\\\" becomes \\\"a parameter worth varying\\\". Say what you mean. Rule 26 covers the metaphor nouns.\"\n    },\n    {\n      \"id\": 33,\n      \"canonicalRuleAndExamples\": \"Over-compression.** Dropped articles, verbless fragments, symbol-speak, and abbreviations that make the reader decode instead of read. \\\"Parser rejects bad date → exit 2, no write\\\" becomes \\\"The parser rejects a bad date, exits with code 2, and writes nothing.\\\" Write whole sentences with their articles and verbs, and spell out arrows and abbreviations.\"\n    }\n  ],\n  \"gaps\": [\n    1,\n    2,\n    4,\n    6,\n    21\n  ],\n  \"sourceUnmodified\": true\n}\n"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/prose-rewrite/supplied-input.json",
      "sha256": "bbe695cd100df18ac7b597a0d77e7dac35940753e48e3055e3a6ff84728d52c9",
      "bytes": 1950,
      "owners": [
        "grades-native-03.json#5"
      ],
      "text": "{\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"id\": \"prose-rewrite\",\n  \"sourcePaths\": [\n    \"skills/unslop/SKILL.md\"\n  ],\n  \"prompt\": \"Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.\",\n  \"requirements\": [\n    \"Access to the supplied draft and the complete unslop pattern list.\",\n    \"Preserve intended meaning and tone, stable rule IDs, and all original pattern examples in the skill.\",\n    \"Remove applicable upstream pattern examples from rewritten prose without adding sources, metrics, mechanisms, or outcomes.\"\n  ],\n  \"expectedFull\": \"Return plain prose that removes chatbot praise, fancy substitutes for is, superficial -ing phrases, AI vocabulary, contrast framing, filler, jargon, and unnecessary passive voice while retaining supported meaning. Apply all applicable numbered rules through 33, including dense sentences, adverbs, mannered prose, and over-compression.\",\n  \"expectedReduced\": \"If only part of the draft is accessible, rewrite that part and state the scope limit. Lack of file-write permission still permits an in-chat rewrite; do not claim a saved edit.\",\n  \"expectedBlocked\": \"If the draft is absent or unreadable, request the actual text and do not invent a rewrite or claim completion.\",\n  \"forbiddenClaims\": [\n    \"New facts, invented citations, measured deltas, or mechanisms absent from the draft.\",\n    \"A file was edited without an observed authorized write.\",\n    \"Host enforcement of disable-model-invocation or host behavioral parity based on structural checks.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/prose-rewrite.result.md",
      "sha256": "78ba74bb6f1b6babb0ad759bafa50e9aebdef5b516ce79559b07186ed3c17d18",
      "bytes": 4628,
      "owners": [
        "grades-native-03.json#5"
      ],
      "text": "# prose-rewrite\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"prose-rewrite\",\n  \"prompt\": \"Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.\",\n  \"requirements\": [\n    \"Access to the supplied draft and the complete unslop pattern list.\",\n    \"Preserve intended meaning and tone, stable rule IDs, and all original pattern examples in the skill.\",\n    \"Remove applicable upstream pattern examples from rewritten prose without adding sources, metrics, mechanisms, or outcomes.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/unslop/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 4. See [source-reads.json](prose-rewrite/source-reads.json). Supplied input archive: [supplied-input.json](prose-rewrite/supplied-input.json).\n\n## Actual response and variants\n\nThe loader is central, fast and essential. To use it, the loader parses the file.\n\nThis retains the draft's centrality, speed, importance and parsing relationship. The phrase about a vibrant paradigm supplies no concrete claim, so it was removed rather than converted into an invented mechanism. The final sentence preserves the draft's use/parsing relationship without assuming who supplies or invokes the file.\n\nI read the entire installed Unslop skill. rule-audit.json preserves the exact canonical text and original examples for every numbered rule, and source/skills/unslop/SKILL.md is the complete unchanged snapshot. Stable IDs present are 3, 5, 7 through 20, and 22 through 33. Gaps 1, 2, 4, 6 and 21 remain gaps. There are 28 numbered rules. No skill was edited or renumbered.\n\nApplicable edits remove praise under 22; superficial highlighting under 3; vibrant/crucial under 7; serves as under 8; contrast framing under 9; filler under 23; paradigm under 26; passive parsing under 29; utilize under 31; and rhetorical fragments under 32 and 33. Rule 27 removes the unsupported flourish. All other rules and their examples were inspected, including 28 and 30, with no invented sources, measurements or outcomes added.\n\nVariant attempted: complete supplied draft and full pattern list available. Rewrite saved as response.txt. Audit is canonical preservation and an editorial check, not evidence that every original example occurred in the draft. No external source was needed.\n\n## Real command results\n\nNo case-specific product command was run. Source reads, inert preparation and output persistence used the setup/report scripts through the actual tools named above.\n\n## Artifacts\n\n- [prose-rewrite/response.md](prose-rewrite/response.md)\n- [prose-rewrite/rule-audit.json](prose-rewrite/rule-audit.json)\n- [prose-rewrite/source-reads.json](prose-rewrite/source-reads.json)\n- [prose-rewrite/supplied-input.json](prose-rewrite/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-03/prose-rewrite/source",
      "owner": "grades-native-03.json#5",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite/source-reads.json",
      "owner": "grades-native-03.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite/source",
      "owner": "grades-native-03.json#5",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/prose-rewrite/source-reads.json",
      "owner": "grades-native-03.json#5",
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
