### Eval

**You own the experiment design. Plan, blind, run, synthesize.**

Read [session capabilities](../../../references/host-capabilities.md), [model roles](../../../references/model-roles.md), [assignment and integration](../../../references/orchestration-contract.md), [workflow ownership](../../../references/workflow-ownership.md), and the complete [arena skill](../../arena/SKILL.md). Use exposed operations within user authorization. These references describe contracts, not available tools. Assign isolated authorized paths and immutable input revisions before dispatch. External launches, publication, commits and messages need their own authorization. Do not install missing companions.

Independent candidates and a fresh judge require observed worker operations and inspected results. Request inherited models unless current exposed documentation supports explicit selection. Record requested and observed models separately. Unknown or identical observed models do not establish different model families. Sequential alternatives and parent judging are reduced capability only. If independent comparison is required, missing workers block that gate.

**Non-negotiables for blinding:**

- No `eval`, `test`, `judge`, `experiment`, `rubric`, `score`, `compare`, `benchmark`, `candidate`, or `arena` in any directory, file, or prompt the candidate sees.
- The candidate prompt looks like an organic user request. State the goal, not the meta.
- No chain-eliciting cues. Don't ask the candidate to list which skills, principles, or files they applied. Ask for design notes generally and grade chain-following from code shape, not self-report.
- Sanitize directory and slug names. Use project-shaped names a user might pick.
- Don't tell the candidate other candidates exist.
- The judge can know it's judging but sees outputs by sanitized label only, never by model name.
- Comparing two variants: one judge scores both sets in a single pass on one scale, blind to which set each came from.

**Steps:**

1. **Frame.** State what variant is under test and what behavior counts as success. Write the rubric (3-6 concrete criteria) for the judge only. Hold it back from candidates.
2. **Set up sanitized environments.** Per-candidate working dir with the variant in place. Plant any context an organic task would have: a project skeleton, the skills the candidate would naturally read.
3. **Author one organic prompt.** What a user would type. No leakage of what's being measured.
4. **Spawn N parallel candidates** on different observed models when supported and authorized. Otherwise record inherited selection and unverified diversity per the [arena skill](../../arena/SKILL.md)'s Phase B. Each works in its own sanitized dir. Same prompt to each.
5. **Spawn one blinded judge** on a different observed model family when supported and authorized, otherwise disclose the selection limit per the [arena skill](../../arena/SKILL.md)'s Phase C. Judge sees outputs by sanitized label and the rubric, never a model name.
6. **Verify the chain from transcripts, not self-report.** Read each candidate's transcript through an exposed authorized history binding or an observed transcript location for this assignment in its active workspace. Never search unrelated workspace histories or private chats. If transcripts are unavailable, declare chain-following unverified. Candidate self-report cannot replace them. Look at which files each candidate actually opened. Grade chain-following from the files it really read plus the shape of the code, never from the candidate's own claims.
7. **Read every candidate output yourself** end to end. Compare to the judge's verdict. Disagreement means a model is biased or the rubric is ambiguous. Synthesize.

Before trusting a score or promoting the variant, run the rubric against known good and known bad fixture outputs under sanitized labels on the same scale. Keep this calibration outside candidate-visible context. Confirm that the eval separates them in the expected direction. If it cannot separate them, stop promotion and revise the rubric before rerunning. Read-only calibration uses fixtures and proves no candidate runtime behavior.

Apply the [unslop skill](../../unslop/SKILL.md) to the synthesis.

**Reply:** variant under test, rubric, per-candidate notes, judge's verdict, your synthesis, and a recommendation for whether to promote the variant. Include the calibration result, transcript gaps, actual model-selection limits and any reduced or blocked gates.
