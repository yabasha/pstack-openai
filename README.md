# pstack-openai

Engineering workflows for planning, implementation, review, and verification in ChatGPT and Codex.

An unofficial, skills-only port of [pstack](https://github.com/cursor/plugins/tree/df581122cde17e6e27686b5a448bde23e4ad4318/pstack), created by **Lauren Tan**. **yabasha** maintains and publishes this port. It includes 51 skills, including 24 engineering principles, and 23 task playbooks from the pinned pstack v0.15.15 baseline.

[Website and examples](https://pstack-openai.abloommink3.chatgpt.site) · [Get started](#get-started) · [Choose a skill](#choose-a-skill) · [Compatibility](#compatibility) · [Documentation](#documentation)

Free to use, with no plugin purchases. Availability is intended for all countries supported by the distribution platform. The existing upstream icon is retained.

## What it does

- Routes engineering tasks through a playbook with `poteto-mode`.
- Compares alternative implementations with `arena`, or divides independent work with `swarm` when the host supports workers.
- Explains code and design decisions with `how`, `why`, and `teach`.
- Reviews changes with `interrogate` and checks affected code with `blast-radius`.
- Adds verification workflows and removes formulaic wording with `unslop`.

The plugin provides instructions and bundled helper source. It does not provision models, register an MCP server, or enable integrations. Worker execution, model selection, history access, and persistence depend on the host and the permissions available in the current chat.

## Get started

1. Install the package through your host's supported plugin controls. Follow the [Codex setup guide](docs/setup/codex.md) or [ChatGPT setup guide](docs/setup/chatgpt.md). Directory publication is still pending; do not assume a public listing exists.
2. Start a fresh chat with the plugin enabled and confirm its skills are available.
3. Invoke a skill with a concrete goal and a check for completion. For example:

   ```text
   Use poteto-help to choose a workflow for reviewing a pull request.
   ```

   ```text
   Use poteto-mode to fix the failing checkout flow. Reproduce the bug,
   keep the change scoped, and verify the affected user journey.
   ```

   ```text
   Use how to explain the authentication flow, citing the relevant files.
   ```

Slash-command availability depends on the host. If a command is absent, ask for the skill by name. If the host has not loaded the plugin, a name alone does not make its instructions available.

Reading skills requires no helper dependency installation. Some development helpers need Bun and their pinned dependencies. See [helper setup](docs/testing/helper-setup.md) before using those helpers.

## Choose a skill

| Goal | Start with |
| --- | --- |
| Find the right workflow | [poteto-help](skills/poteto-help/SKILL.md) |
| Implement or fix something | [poteto-mode](skills/poteto-mode/SKILL.md) |
| Sketch types and module boundaries | [architect](skills/architect/SKILL.md) |
| Compare competing solutions | [arena](skills/arena/SKILL.md) |
| Divide independent work | [swarm](skills/swarm/SKILL.md) |
| Review a change and its consequences | [interrogate](skills/interrogate/SKILL.md), [blast-radius](skills/blast-radius/SKILL.md) |
| Understand code or its rationale | [how](skills/how/SKILL.md), [why](skills/why/SKILL.md), [teach](skills/teach/SKILL.md) |
| Build a project verification workflow | [create-verification-skill](skills/create-verification-skill/SKILL.md) |
| Improve prose | [unslop](skills/unslop/SKILL.md) |

Browse [all 51 skills](docs/skills/README.md), [all 24 principles](docs/principles/README.md), or the [workflow selection guide](docs/workflows/choosing-a-workflow.md).

## Compatibility

Version 0.1.3 has retained discovery and workflow evidence for both hosts at frozen revision `51f209daf83cd97d64f89881d66533bb59dc57db`. The reviewed results cover 104 workflow cases per host:

| Host | Passed | Reduced capability | Blocked |
| --- | ---: | ---: | ---: |
| Codex | 33 | 50 | 21 |
| ChatGPT | 21 | 56 | 27 |

Package discovery is recorded separately. Reduced results do not establish full behavior or independent workers. Blocked cases remain unsupported in their recorded environment. See the [reviewed results](docs/releases/remaining-controller-report.md), [Codex case index](docs/testing/codex.md), and [ChatGPT case index](docs/testing/chatgpt.md).

These results qualify the named frozen revision. The README and listing changes in this publication candidate need a new frozen revision and fresh discovery checks before release. See [compatibility details](docs/compatibility.md) and the [publication checklist](docs/publication.md).

## Documentation

| Topic | Guide |
| --- | --- |
| Installation | [Codex](docs/setup/codex.md), [ChatGPT](docs/setup/chatgpt.md) |
| Workflow walkthroughs | [Poteto mode](docs/workflows/poteto-mode.md), [Arena](docs/workflows/arena.md), [Swarm](docs/workflows/swarm.md) |
| Original guide and port notes | [Guide index](docs/guide/README.md) |
| Troubleshooting | [Troubleshooting](docs/troubleshooting.md), [host test matrix](docs/testing/host-matrix.md) |
| Optional helpers | [Dependency setup](docs/testing/helper-setup.md), [Benny readiness](docs/testing/benny-readiness.md) |
| Maintenance | [Upstream updates](docs/maintenance/upstream-updates.md), [customization boundary](docs/maintenance/customization-boundary.md), [rollback](docs/maintenance/rollback.md) |
| Publication | [Readiness checklist and packaging command](docs/publication.md), [changelog](CHANGELOG.md) |

## Permissions

Invoking a skill does not authorize installation, changes to settings, external messages, publishing, integrations, or recurring schedules. Workflows must respect the user's scope and the host's permissions. Model and worker claims require observed execution.

## Credits and license

Lauren Tan created pstack and its skills and principles. yabasha maintains this unofficial port and its host adaptations, documentation, and packaging. The original MIT copyright and permission notice remain in [LICENSE](LICENSE).

Read [NOTICE.md](NOTICE.md) for attribution and [UPSTREAM.md](UPSTREAM.md) for source pins, hashes, and adaptation provenance. This port is not affiliated with or endorsed by the upstream project or its author.
