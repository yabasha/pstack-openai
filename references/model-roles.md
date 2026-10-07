# Model selection for portable roles

Use [session capabilities](host-capabilities.md) before assigning a role. These [poteto](agent-prompts/poteto-agent.md) and [comment reviewer](agent-prompts/comment-sicko.md) prompts are instructions supplied to an exposed worker operation. Reading them does not register a custom agent or authorize delegation.

| Role | Default requested model | Observed model | Supported effort | Fallback disclosure |
| --- | --- | --- | --- | --- |
| poteto-agent | inherit-parent | unknown until observed | inherit-parent unless a supported explicit effort is verified | Record rejected selection, replacement request, observed result and limits. |
| comment-sicko | inherit-parent | unknown until observed | inherit-parent unless a supported explicit effort is verified | Record rejected selection, replacement request, observed result and limits. |

For each assignment, record requested model and effort, observed model and effort, supported effort values and their source, worker identity, and fallback disclosure. Use `unknown` for information the operation does not expose. `inherit-parent` records a selection policy, not an observed model name. Do not silently convert a requested model into an actual model.

Select an explicit model only from current exposed tool documentation or observed enumeration results. If enumeration is missing, disclose that limit and retain `inherit-parent`. Documentation examples are not a list of available models. Use only an effort supported for the selected model by the current operation; do not carry an incompatible inherited effort into an explicit selection.

If a selected model or effort is rejected, retain the rejection. Use an authorized inherited or supported alternative only after disclosing the changed selection. If the task requires that exact selection, stop and record blocked. A fallback never proves the original selection succeeded.

Identical observed models mean no model diversity. Different roles can supply distinct instructions on the same model. Unknown observed models leave diversity unverified, even when requested model names differ. Different observed models support a model-diversity statement only for those observed assignments. Worker independence still requires successful spawn and result inspection.

When workers are unavailable, apply an authorized role sequentially and label reduced capability. Preserve scope and permission boundaries. Do not claim independent review, background execution, or full worker support from sequential role switching.

The cached documentation from https://learn.chatgpt.com/docs/agent-configuration/subagents describes inheritance and optional local agent configuration. It is context only. This package writes no local custom-agent configuration and claims no current host model or worker support from that documentation.
