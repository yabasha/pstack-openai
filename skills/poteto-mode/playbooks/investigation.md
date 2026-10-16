# Investigation

You own the answer. Plan, route, write.

Investigation requests are read-only. They produce a cited explanation or a recommendation, not a code change. Read the complete [poteto mode](../SKILL.md) and this playbook before applying it. Preserve its Investigation routing for how, why, are-we-sure and choice-between-alternatives questions.

Before source reads or delegation, discover [session capabilities](../../../references/host-capabilities.md) and follow [model roles](../../../references/model-roles.md) and the [assignment contract](../../../references/orchestration-contract.md). Use only exposed, authorized read operations. Inherit parent model and effort unless a supported explicit selection is observed. Requested models are not observed models. The routed skills own their prompt and source contracts; this playbook directly invokes no script helper.

1. Route through the [how skill](../../how/SKILL.md). For motivation questions, also route through the [why skill](../../why/SKILL.md). Read their complete instructions and the prompts and source playbooks required by the chosen route. Keep every investigator and explainer read-only, including connector-backed reads. Inspect delegated findings before relying on them. If independent workers are unavailable or unauthorized, disclose reduced capability and apply the same roles sequentially. Name inaccessible, denied, failed and searched-empty sources separately. Limit the answer to inspected evidence. Missing required companions or no authorized relevant source reads blocks the dependent answer.
2. Throughput checkpoint stays one line: `throughput checkpoint: n/a, read-only investigation`.
3. Produce the how-shaped output, Overview / Key Concepts / How It Works / Where Things Live / Gotchas, omitting sections only as how permits. For a decision between alternatives, produce a recommendation with a tradeoffs table. For motivation, preserve why confidence tiers, source coverage, contradictions and unknowns within the investigation output. Cite actual inspected sources. Accessible sources that support the answer are enough to deliver it without starting a product build or prototype.
4. Apply the [unslop skill](../../unslop/SKILL.md) to the reply.

No PR, no babysit, no [architect](../../architect/SKILL.md) unless the investigation precedes a code change. If it does, hand back to the user and re-route to [Bug fix](bug-fix.md) or [Feature](feature.md). That handoff does not authorize implementation, commits, PR creation or other writes. The Investigation exception takes precedence over the mode index generic Opening a PR rule. Do not install tools, change credentials or modify source state to obtain evidence.

Reply with the investigation output. For are-we-sure answers, include your real judgment with reasons. Push back if the premise is wrong under the mode Autonomy rules. Broad autonomy never overrides user authorization or host permissions. Disclose unperformed reads, uncertain conclusions and reduced roles; structural checks establish no runtime behavior or independent-worker success.
