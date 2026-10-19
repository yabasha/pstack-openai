# Set up pstack
## Session capabilities and ownership

These prompts name pstack workflows, not guaranteed host commands. Read [session capabilities](../../references/host-capabilities.md), [model roles](../../references/model-roles.md), [assignment and action contracts](../../references/orchestration-contract.md), and [workflow ownership](../../references/workflow-ownership.md) before acting. Keep the active controller. An explicit pstack invocation owns its workflow; an active Superpowers assignment remains with Superpowers. An unqualified request retains the active owner. If both are requested, resolve ownership first.

Full behavior requires observed authorized tools for every required operation. Ordinary ChatGPT with supplied source but no execution can explain and prepare drafts; runnable verification is blocked. Worker-enabled ChatGPT and local Codex must discover and observe actual tools separately. Without independent workers, sequential role work is reduced capability and cannot satisfy independent review. Unknown actual models remain unknown. Missing history, persistence, execution, app control or GitHub access blocks dependent steps. A diagram is an illustration, never evidence that a tool exists. See the [host matrix](../testing/host-matrix.md).

Reading these files directly does not prove supported plugin loading, registration, invocation or host behavior. Both hosts remain not-run. Installation, dependency setup, host enabling, personal settings, schedules, credentials, listeners, commits and external writes retain their applicable explicit permission gates. A local draft is not a PR or verified app. Read the linked adapted workflow in full before its step; a missing required companion remains a blocked gate.


Setup separates host loading, model choices and optional development dependencies. None happens merely because you read this guide.

## Load through a supported host mechanism

Follow the current host plugin documentation only after explicit installation or enabling authorization. The supplied official research was fetched on 2026-10-07. [Plugin packaging](https://developers.openai.com/codex/plugins/) and [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) describe mechanisms; they do not prove this package loads in this session. Record the exact host operation and resulting discovery or invocation. Direct reads of installed files prove only file access. Both host loading paths remain unverified.

## Pick your models

Invoke [setup-pstack](../../skills/setup-pstack/SKILL.md) through the supported invocation mechanism, or explicitly request its workflow when the host exposes no slash menu. It enumerates actual supported choices, asks for a budget and returns a reviewed role table. The labels unlimited, large, medium and small target max, xhigh, high and medium effort only when the selected operation supports them. Defaults inherit the parent. The aliases auto and inherit-parent omit explicit model selection; neither is an observed model name. Panel roles are lists, one requested worker per entry, and swarm workers sets the default worker policy. Worker count and actual models still need observation.

Preserve changed choices on re-run, disclose retired roles, and delete a role to restore its portable inherited default. Show every role, model, effort and exact destination before a persistent override. Confirm the mapping and obtain explicit authorization before writing personal configuration. If a supported persistent mechanism is absent or setup is skipped, use the table in this session as reduced capability. No portable always-applied rule or new-session behavior is promised.

## Accept the verification offer, or decline

Setup offers [create-verification-skill](../../skills/create-verification-skill/SKILL.md) once if no verify skill or existing harness exists. Invoke it only on yes. On no, continue. Discover the project-local skill destination before writing; <project-local-skills> is a discovered directory, not a literal path. Missing authoring or driving tools leave a provisional draft and verification not-run. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers its feature map and end-to-end proof.

## Optional helper dependency setup

Bootstrap never installs. The committed pins are commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. The approved isolated snapshot 37b68c8e842b275f310ead112c0ecb7fa0ade308 passed 85 orchestration tests, 316 watcher tests and strict TypeScript with zero errors. That evidence applies only to that snapshot. The operative checkout has no installed dependencies. Both host workflows remain not-run.

The [helper setup guide](../testing/helper-setup.md) still contains pre-reconciliation history and unqualified install examples. Those are stale, do not use them. A future setup requires fresh explicit authorization for an exact writable copy under Herd, exact manifest and lock scope, registry https://registry.npmjs.org, disabled lifecycle scripts with --ignore-scripts, and a task-owned --cache-dir. Frozen installation and verification belong to that approved copy. Use Bun with --no-install for ordinary helper runs. Missing dependencies stay setup-required. Development setup is separate from plugin installation or host enabling.

## Keep costs in check

Choose a smaller supported budget, inherited roles or shorter panels through the reviewed model table. Use poteto-mode for work that needs its checks. Never assume a model slug, maximum effort or cloud placement exists.

## Run your first task

```text
/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

The matched Feature playbook supplies the checklist. A skipped step stays visible with skip and a reason. Use the host's supported invocation mechanism; a persistent mode or recurring attachment must be observed and authorized. If none exists, re-invoke explicitly on later turns.

Next: [Route work through poteto-mode](./02-poteto-mode.md).

## Optional formal verification

Setup also offers once to generate a project-local property check with [/create-formal-verification-skill](../../skills/create-formal-verification-skill/SKILL.md), unless one already exists. Say yes to invoke it or decline without changing setup. It selects a costly failure that tests rarely reach, states its bounds, and proves the check can fail. Generated-input tests are a fallback, not formal proof. Missing execution leaves a draft. After covered-code changes, use [/maintain-formal-verification-skill](../../skills/maintain-formal-verification-skill/SKILL.md). Tool installation and project writes keep their separate authorization requirements.
