# codex: stack-resume

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "stack-resume",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Resume an authorized three-PR stack from a saved brief using read-only fixtures. The middle PR has rebased onto a new parent, its old verdict and CI refer to the previous head, a verdict-post action has an unknown outcome, and a retarget action already completed. Persistent wake and one adapted dependency are unavailable. Determine what may proceed before another write, then repeat with a stop order and denied external writes.",
  "caseDefinition": {
    "id": "stack-resume",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/autopilot-stack.md",
      "skills/poteto-mode/playbooks/autopilot-full.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/references/bugbot-triage.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/swarm/SKILL.md",
      "skills/no-comments/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
      "skills/poteto-mode/playbooks/opening-a-pr.md"
    ],
    "prompt": "Resume an authorized three-PR stack from a saved brief using read-only fixtures. The middle PR has rebased onto a new parent, its old verdict and CI refer to the previous head, a verdict-post action has an unknown outcome, and a retarget action already completed. Persistent wake and one adapted dependency are unavailable. Determine what may proceed before another write, then repeat with a stop order and denied external writes.",
    "requirements": [
      "Read all complete caller contracts and record missing adapted dependencies before dependent execution.",
      "Inspect current head, base, intended parent, verdict head/base/patch-id, checks and mergeability for every resumed PR; invalidate stale results and follow Shipping patch-id/build-noise rules.",
      "Inspect prior action identities and destination outcomes before any replay; do not repeat completed actions and block unknown outcomes without authorized idempotent recovery.",
      "Preserve single root topology writer, exclusive branch ownership during rebase, ls-remote and force-with-lease safety, and bottom-to-top linear delivery.",
      "Preserve ready PR before self-proof, decision/children trails, all live independent round lanes, fix-forward, countersigns, state-then-wait and zero-writes stop.",
      "Discover forge/model/worker/wake bindings; missing wake permits only current-turn ticks and verified continuation persistence as reduced capability.",
      "Use read-only fixtures without live forge actions or scheduling; owner/root never merge, close or arm auto-merge under this playbook."
    ],
    "expectedFull": "With all actual bindings and authorization, reconcile every PR revision and interrupted action, re-verify changed rounds and current CI/mergeability, then publish only authorized topology/verdict changes and deliver one verified bottom-to-top chain for the operator to land. Observe every claimed action, worker and saved artifact.",
    "expectedReduced": "Missing persistent wake or independent workers is explicit. Run authorized current-turn or sequential work with read-back continuation and local verdict artifacts; never claim independent clean verification, hourly continuation, published delivery or automatic pickup. Missing contracts stop their dependent operations.",
    "expectedBlocked": "A stop order, stale or inaccessible revision, missing dependent contract, unknown prior action outcome, unavailable live lane, unsafe writer ownership or denied write prevents the affected write or verdict. Retain the rest of the queue and disclose exact next checks.",
    "forbiddenClaims": [
      "Saved heads or old green CI prove current stack readiness.",
      "A completed retarget or unknown verdict post may be blindly replayed.",
      "Local structural checks establish host behavior, model diversity or independent verification.",
      "Autopilot-stack authorizes merges, closures or auto-merge.",
      "A continuation brief or /loop alias proves registered hourly wake or automatic pickup.",
      "Missing adapted dependencies or companion gates silently pass."
    ],
    "caseFile": "docs/parity/cases/playbooks/autopilot-stack.json"
  },
  "registry": {
    "caseId": "stack-resume",
    "caseFile": "docs/parity/cases/playbooks/autopilot-stack.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/autopilot-stack.md",
      "skills/poteto-mode/playbooks/autopilot-full.md",
      "skills/poteto-mode/playbooks/babysit.md",
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/references/bugbot-triage.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/swarm/SKILL.md",
      "skills/no-comments/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/show-me-your-work/SKILL.md",
      "skills/show-me-your-work/scripts/log.sh",
      "skills/show-me-your-work/references/decision-log-template.tsv",
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
        "inspect-result"
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
