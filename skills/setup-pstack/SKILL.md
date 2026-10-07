---
name: setup-pstack
description: Configure which models pstack uses per role and at what reasoning budget. Reviews a role table using verified available models or inherited choices. Persistent overrides require a supported host mechanism and explicit authorization. Use for /setup-pstack, "configure pstack models", "pstack budget", or changing pstack's model choices.
---

# Setup pstack

Configure pstack's model choices per role and reasoning budget. This portable skill produces a reviewed role table. Persistent overrides need a verified host mechanism and explicit authorization for its exact destination. Reading this skill never writes personal host configuration.

Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), and the [assignment contract](../../references/orchestration-contract.md). No portable always-applied host rule is supplied. A session-only table is reduced capability when durable overrides are unavailable.

## 1. Detect available models

Enumerate the models and supported effort values accepted by the exposed worker operation in this session. Prefer a verified entitled-model API or CLI if one is exposed and authorized. Tool documentation and observed enumeration are evidence; example slugs are not. If neither source is available, ask the user for their available choices and disclose that pasted names still need verification before use. Never write or request a real slug without confirmed availability.

The aliases `inherit-parent` and `auto` both mean the role uses the parent chat model: omit an explicit model override. Keep `inherit-parent` for every role when availability is unknown. An alias is a selection policy, not an observed model name. If the host cannot represent `auto`, normalize its policy to inheritance and disclose that change.

## 2. Load current state

Start with the inherited role table below. If the user identifies an existing supported override, read it through authorized tools and treat its budget and role values as current choices. Reading does not authorize rewriting it. Drop retired roles, such as `how critics`, from the proposal and list each dropped line for review. Preserve current choices changed by family, list, or alias on a re-run.

## 3. Budget, map, and confirm

Ask for a budget using an exposed structured question tool when available, otherwise ordinary conversation. Name the current recorded budget. The upstream default budget is `large`; the portable default model policy is inherited. Offer these source labels:

- `unlimited — max reasoning`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

These labels are targets, not a claim that the host supports those efforts. Set every verified real selection, including panel entries, to the supported target effort. Where models encode effort in their slug, the effort token is last or immediately before a trailing `fast`; its ladder is `max > xhigh > high > medium > low`. If the target slug is absent, choose the same family's verified selection with the highest supported effort at or below the target. If no such selection exists, mark the role as needing a choice. With a separate effort field, verify the combination against the exposed operation. Never synthesize availability by editing a slug. Aliases do not change with budget.

Show every role and its requested model and effort. Mark unsupported choices as needing a choice; actual values remain unknown until observed. Show retired lines removed from the proposal. Ask whether to accept the table or change specific roles, offering only verified models plus the inherited aliases.

Panel roles are lists: arena runners, architect runners, and interrogate reviewers run one worker per entry, including aliases, so list length sets fan-out. The arena cross-judge pool is a list from which Arena chooses one entry whose family differs from the parent when possible. Unknown families leave diversity unverified. Swarm workers is the default for each worker unless a race or comparison assigns a model per arm. Worker count and independence still require observed host dispatch under the assignment contract.

## 4. Validate

Every real model and effort combination must be verified against the current operation. Aliases pass as inheritance policies. Stop and ask again for any unavailable real choice. If an exact unavailable selection is required, report blocked. A rejected selection must remain visible even when an authorized inherited fallback is useful.

## 5. Prepare or write the override

The portable default table is:

```text
# pstack per-role model choices
# budget: large (xhigh target; explicit effort requires verification)
# Delete a role to fall back to the portable inherited default.
# Alias entries in panel lists count toward fan-out.
feature, refactoring: inherit-parent
bug-fix: inherit-parent
perf-issue: inherit-parent
hillclimb: inherit-parent
judgment and prose: inherit-parent
hardest tasks: inherit-parent
how explorer: inherit-parent
how explainer: inherit-parent
why investigators: inherit-parent
why synthesizer: inherit-parent
reflect tooling: inherit-parent
reflect judgment, divergent, synthesizer: inherit-parent
arena runners: inherit-parent, inherit-parent
arena cross-judge pool: inherit-parent, inherit-parent
swarm workers: inherit-parent
architect runners: inherit-parent, inherit-parent
interrogate reviewers: inherit-parent, inherit-parent
```

Show the whole proposed override and destination before any write. The user's confirmed mapping and explicit authorization for the personal host configuration are both required. If no supported persistent mechanism or authorization exists, return the table for session-only use and disclose reduced capability. Never create local custom-agent configuration or an always-applied rule incidentally, and never treat such files as portable plugin configuration.

For an authorized supported destination, serialize through the verified host format, include the chosen budget label and target effort, use the exact role labels above, and replace the whole override so re-runs are idempotent. Preserve no retired role. Read back the written result. If writes or readback are denied or unavailable, report blocked persistence and the observed outcome; do not claim that a save succeeded.

## 6. Confirm

Report whether the result is a session-only proposal or a verified saved override. State its scope and when it applies only as established by the host mechanism. Do not promise new-session behavior without evidence. Re-running this skill proposes an update and preserves the same confirmation and write gates.

## 7. Offer a verification skill

Check whether the project already has a `verify-*` skill or a harness that can drive the real app. If neither exists, offer once to generate a project-local verification skill with `/create-verification-skill`. Invoke it only on yes; on no, continue without pressing. Its [leaf](../create-verification-skill/SKILL.md) is a deferred local dependency until its assigned port lands. Missing support stays visible; do not claim app verification from the model table.
