# Reproduce automation prompt

> Source material for the copied setup workflow. Paraphrase this intent into an authorized host automation draft after repository inspection confirms that the copied pack is committed in the repository where the automation will run.

Read and follow `automations/benny/skills/reproduce-and-fix-issues/SKILL.md` for this run.

Configuration source. Include this repository-relative path only when it is committed in the same target repository. Otherwise paraphrase the configured values. Never use a plugin source or cache path:

```text
{{BENNY_CONFIG_PATH}}
```

Trigger:

```json
{
	"source_channel_id": "{{SLACK_CHANNEL_ID}}",
	"message_ts": "{{SLACK_MESSAGE_TS}}",
	"thread_ts": "{{SLACK_THREAD_TS_OR_EMPTY}}"
}
```

The creation intent should describe this as a new top-level report in the configured source Slack channel. It should include the configured repository, default branch, issue tracker, control adapter, feature map, and draft pull request capability.

Treat the source channel and root thread timestamp as immutable. If either is missing or does not match configuration, stop without posting.

Wait for a configured triage marker from the configured triage identity in this exact thread. Proceed only for `[benny:bug]` or `[benny:performance]`.

Require the configured control-adapter skill before attempting a repro. Reproduce the exact discriminating symptom twice through the real UI. Verify existing pull requests or commits without authoring over them. Attempt a bounded fix only after a confirmed repro and the operational file's fix gate.

The coordinator is the only Slack poster. Every child prompt must forbid `SendSlackMessage`, `PostToSlack`, `chat.postMessage`, and all other Slack writes. Children return findings only.

Never post a root message in the source channel.

## Session capability and authorization gate

Read the package's references/host-capabilities.md, references/model-roles.md, references/orchestration-contract.md, and references/workflow-ownership.md before setup or execution. Resolve those files from the target repository's verified pstack package. Missing dependencies block Benny only.

Bind each required channel, tracker, repository, control-adapter, and trigger operation to an actually exposed session tool. Record exposed operations, supplied evidence, permission, limits, and observed outcomes. Documentation and example action names are not callable APIs. Read-only readiness uses supplied or inert evidence until separately authorized live checks exist.

Sending source or operations messages, owner pings, downloading private media, filing or updating tickets, compensating tickets, repository writes, commits, draft pull requests, and creating or updating automations each require authorization for that action and destination. Configuration and capability discovery alone give no permission. If a required write or compensation is unavailable or unauthorized, stop before dependent writes and retain a local draft or run output. A scheduled time trigger does not implement a channel event trigger. Unsupported triggers block setup; do not silently create a polling schedule.

Record a stable action identity before external writes. After an interruption inspect the destination and prior outcome before an authorized idempotent retry. Unknown outcomes block replay. Follow the current workflow owner. Delegation needs an exposed independent-worker operation and enforceable tool isolation; sequential analysis is reduced capability. Never infer independent review or an observed model from a requested role.


Normalize the exposed event payload before freezing coordinates. The template message_ts field maps to trigger.ts; thread_ts remains the root override. Verify the actual connector schema and source parent. Missing or ambiguous mappings block execution.
