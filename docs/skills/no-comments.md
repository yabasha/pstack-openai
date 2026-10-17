# no-comments

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/no-comments.json](../catalog/skills/no-comments.json).

Skill: [skills/no-comments/SKILL.md](../../skills/no-comments/SKILL.md). Kind: skill.

## Purpose

Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints.

## Triggers

- Explicit no-comments invocation; disable-model-invocation metadata is retained without assuming host enforcement.

## Required input

- Caller-scoped files or diff, otherwise current diff against the base branch, default main, including working tree.
- Authorization for scoped comment deletions and accepted fixes; separate approval for constraint encodings.

## Output contract

- Scoped comment deletions and accepted root-cause fixes when authorized.
- Report deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints and other open work.

## Ordinary example

Invoke no-comments on an authorized diff to remove redundant narration while retaining its license header and justified public API contract.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [legal-header](../parity/cases/skills/no-comments.json)

Run no-comments on an authorized scoped diff containing a license header, public API contract doc comment, redundant narration, a correctness suppression, and an ambiguous IMPORTANT constraint. Inspect the rules and symbols before deciding. Retain exceptions and apply accepted scoped findings. Offer a constraint encoding and wait for approval. Repeat with missing workers and denied writes.

Full capability expectation:

An observed independent worker deletes authorized narration while retaining the license header and justified public-contract comment. The coordinator investigates constraints, audits suppressions, verifies edits and counts, reviews and fixes accepted findings within scope, preserves the one-retry failure rule, and encodes constraints only with approval. Unapproved encoding leaves deletion and open constraint reporting subject to authorized writes.

Reduced capability expectation:

With no independent worker, an authorized sequential review retains the same rules and can still delete authorized scoped comments, with reduced capability explicit. With unavailable or unauthorized writes, an authorized read-only review reports proposals, actual deletion count zero, unresolved claims and unimplemented fixes or encodings; it does not claim edits or independent review.

Blocked capability expectation:

Missing required files, base diff, role or investigative dependency is identified rather than invented. Required actual edits with unavailable or denied writes and no authorized reduction are blocked. A second rejected report fails no-comments and remains open.

Required observations:

- Read the scoped files or diff and the Comment Sicko role; use the current diff against the base branch, default main, including working tree only when no caller scope exists.
- Use an independent Comment Sicko worker when available and inspect report and diff; review scoped comment edits and reject code edits, scope escapes, protected deletions, false MUST KILL reasons, and flags against kept intentional code.
- Retain license headers and justified public API contracts; delete unneeded narration when writes are authorized. Investigate ambiguous constraints with how or why and audit lint and TypeScript suppressions.
- Restore only exact proven exceptions, retry one rejected report with failure named, and fail with the second rejection open.
- Fix accepted flags within scope, use architect once when a shape is needed, stop at its sketch, then implement the smallest root-cause fix without symptom guards.
- Offer constraint encodings and wait for interactive approval; unattended/eval encoding requires caller pre-approval. Report actual deletions, restorations, reruns, sketch, fixes, offers, encodings, unenforced constraints and open work.

Forbidden claims:

- Removed a legal header or justified public API contract as narration.
- Claimed proposals as actual deletions, an unobserved worker as independent review, or static validation as host pass.
- Performed unapproved encoding, widened scope, restored ambiguous kills without exact exception proof, or hid unresolved constraints.
- Invented a suppression verdict, symbol investigation, worker result or deletion count.

## Dependencies

- [references/agent-prompts/comment-sicko.md](../../references/agent-prompts/comment-sicko.md)
- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [skills/how/SKILL.md](../../skills/how/SKILL.md)
- [skills/why/SKILL.md](../../skills/why/SKILL.md)
- [skills/architect/SKILL.md](../../skills/architect/SKILL.md)
- [skills/principle-fix-root-causes/SKILL.md](../../skills/principle-fix-root-causes/SKILL.md)
- [skills/principle-redesign-from-first-principles/SKILL.md](../../skills/principle-redesign-from-first-principles/SKILL.md)

## Host limits

- Missing independent workers allows authorized sequential review as reduced capability, including authorized scoped edits.
- Unavailable or unauthorized writes allows an authorized read-only proposal report with actual deletion count zero; required edits otherwise block.
- Required investigation needs scoped code, rules and how or why; unavailable evidence remains a skip.
- Unattended/eval encoding requires caller pre-approval. Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/no-comments/SKILL.md`

Destination: [skills/no-comments/SKILL.md](../../skills/no-comments/SKILL.md).

Upstream commit: `182f2ce414e83224915c190d2f63239c1608d0a5`. SHA-256: `078ecfe224eafbb017f6476870612838bf6dbe38c0b697e12f0c887d0313f17e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `agents/comment-sicko.md`

Destination: [references/agent-prompts/comment-sicko.md](../../references/agent-prompts/comment-sicko.md).

Upstream commit: `182f2ce414e83224915c190d2f63239c1608d0a5`. SHA-256: `3e239e40b7b4b9beb2cf7f3ccc57f2388eb8b69bd1ba8ae888ef87ef6e0e2116`.

Disposition: `relocated`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
