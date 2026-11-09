---
name: review-change
description: Review a PR, branch, commit range or working-tree change against project standards and its intended requirements. Use for code review, review since a fixed point, or the review stage of implementation. Use the requested or established conversation language from the first progress message.
metadata:
  author: sakana
  version: "2026.11.09"
---

# Review Change

Review a specified change along two axes: **Standards**, whether it follows the project's coding rules and supported design practices; and **Spec**, whether it implements the intended requirements. Trace behavior and run focused checks when they help judge those axes. Return findings and evidence to the user or consuming workflow. That workflow retains implementation and delivery ownership.

This method supports direct requests and calls from other skills. Its scope is the selected change and the behavior it affects. A review does not authorize product fixes, a whole-repository audit, remote comments, approval or merging. It does not start skill evolution.

For factual uncertainty that could change a finding, use [Investigate with Evidence](../investigate-with-evidence/SKILL.md). Install that shared method alongside this skill. If it is unavailable, continue supported review and identify the dependent check that remains unresolved; do not install it at runtime. Review output alone does not create a working-record or tracker workflow.

## Response language

A skill mention and a PR link carry no language request. Use the conversation language or the user's established language preference from the first update. Honor explicit language requests for the output they apply to. Use `simple-english` only for prose that will be in English and only when the skill is available. Preserve meaning, uncertainty, requirement strength, source quotations and requested formats.

## 1. Identify the change

After identifying the target repository, the coordinator reads its project AGENTS.md in the configured records store when available. Use relevant experience to select checks. For a first review or omission check, only the coordinator reads the records copy. Give reviewers neutral conditions and explicitly exclude that file from their inputs and delegated investigations. Withhold prior verdicts and proposed fixes. For a repair review, follow the existing finding handoff below. Judge risk and findings from the current patch.

Recover the requested target and comparison point from the user, active task and repository state. Resolve refs and inspect the worktree before selecting a diff. Ask only when a remaining ambiguity would change what gets reviewed.

- For a branch or PR relative to a base, record the resolved base, target and merge-base. Use the merge-base comparison when that is the requested meaning of "since".
- For explicit endpoints, review their difference without silently replacing the requested starting point with a merge-base.
- For working-tree review, include the selected staged, unstaged and new files. A comparison ending at `HEAD` does not include them. Distinguish selected work from unrelated local changes; ask when ownership cannot be resolved.

Retain the comparison command or equivalent, file set and examined state. Commit IDs identify committed inputs; a working-tree result also needs a patch or file identities sufficient to detect later changes. An empty selected diff yields an explicit no-change result, not a successful substantive review. Invalid refs remain unresolved.

**Ready when:** the reviewed change and its baseline are identifiable, and unrelated changes remain outside it.

## 2. Recover requirements and standards

Read relevant repository guidance, including `CONTRIBUTING.md`, `CODING_STANDARDS.md` and applicable `REVIEW.md` when present. Follow their pointers to rules relevant to the selected files. Read the [standards and design heuristics](references/standards.md) for the Standards axis. Repository rules take precedence over general heuristics.

For Spec, recover the user's agreement and relevant issue, specification, PR discussion or project documentation. Use the configured tracker access method when a referenced issue matters. Current task decisions can supply requirements without a separate spec file. Resolve conflicting or missing requirements only when they affect a judgment. An author's explanation is a claim to examine, not proof that the implementation fulfills it.

If no supported requirement source is available, report the Spec axis as unavailable and continue Standards review. If requirements are partial, state which judgments they support. Do not infer a missing requirement from the implementation or from a preferred design.

**Ready when:** each axis has its applicable evidence, or its missing basis is explicit.

## 3. Examine and verify findings

### Assign the review

The coordinator starts a fresh Standards reviewer for every substantive review, including revisions. When step 2 identifies a supported requirement, start a separate fresh Spec reviewer in parallel. With one slot, wait for Standards to finish before starting Spec.

Give each reviewer the full selected change, baseline, original requirements, repository guidance and relevant evidence. Direct each reviewer to **Inspect the change** below for its assigned axis and ask it to return any relevant cross-axis evidence. Use a fresh context without the coordinator's conversation or the other reviewer's conclusions.

For a first review or an omission check, describe observations in neutral terms. Leave suspected defects, proposed fixes, priority ratings and merge recommendations out of the assignment so each reviewer can reach an independent verdict. For a repair review, give both reviewers the original finding, trigger, prior evidence and repair under review. Ask them to check the original trigger and affected behavior and decide whether the finding is resolved.

If a reviewer cannot run or its context isolation cannot be confirmed, record which axis is incomplete and why.

**Ready when:** each supported axis has a reviewer working in a separate fresh context, or its execution limit is recorded.

### Inspect the change

Use the [change-risk criteria](../investigate-with-evidence/references/change-risk.md) to judge the actual patch independently and choose the depth of inspection. A direct review can make the first rating. If the reference is unavailable, use an applicable project scale or explain the consequences and missing rating basis. The reviewer assignments above apply at every level.

For changes with several behaviors or shared boundaries, organize inspection by observable outcomes, contracts and behavior that must remain intact. Connect each to changed code, necessary unchanged context and shared dependencies. Use failure consequences and unresolved questions to choose focused checks and review depth. Check interactions between these behaviors as well as each behavior itself. Keep the selected change covered by both axes. A small change can keep this reasoning inline.

Keep the two axes distinct while inspecting the same change:

- **Standards:** identify violations of applicable rules and consequential design concerns. Cite the rule for a violation. Label design heuristics as judgments, with the concrete maintenance problem they could prevent.
- **Spec:** identify missing or partial requirements, unrequested behavior, and implementations that appear to meet a requirement but fail under relevant conditions. Connect each finding to its supported expectation.

Follow callers, configuration, state transitions and consumers when the change can affect them. Inspect unchanged code needed to judge the change; do not turn that trace into an unrelated audit. Security, performance, data integrity and documentation accuracy matter where they bear on these judgments. A test gap is material when it leaves a concrete promised behavior or preservation condition unsupported, not simply because a file lacks a test.

When changed tests or a claimed coverage gap affect a finding, use the shared [test-value method](../investigate-with-evidence/references/test-value.md) within the selected review scope.

Before accepting a finding, inspect the exact source and the strongest relevant counterevidence. For a behavioral defect, establish the trigger, expected and actual behavior, and consequence. For an explicit standards violation, the applicable rule and conflicting code can suffice without a runtime failure. For a design concern, explain the maintenance situation and cost rather than inventing a failing input. Use a bounded test or reproduction when it could distinguish competing explanations. Inspect setup effects and use existing authorized, controlled environments. Preserve product files and unrelated work. Report actual commands and results separately from static reasoning; a reviewer's agreement or confidence is not evidence.

Distinguish issues introduced, exposed or worsened by this change from problems already present. A real old problem remains visible when relevant, but does not become the author's regression or an authorized repair. An unsupported suspicion stays outside the confirmed-defect count. Material uncertainty that could change the review outcome remains explicit.

**Ready when:** reported findings have inspectable support, competing explanations have been addressed where material, and remaining evidence gaps are named.

## 4. Return the review

Before reporting, collect each assigned reviewer’s result or identify its pass as incomplete. Check the findings against counterevidence and resolve gaps across the two reports where possible. Start with the supported finding count and the concrete outcome. Return one deduplicated list ordered by impact, retaining **Standards**, **Spec**, or both on each item. Merge observations only when they describe the same problem and correction boundary; a shared file or suspected cause alone is insufficient.

Report the whole patch's risk and its basis even with zero supported findings. Compare with any prior estimate after forming the review judgment. If they differ, check the assumption that explains the difference. Say what the evidence supports for the requested next step.

For each finding, including your own, identify the requirement, affected caller or project rule that establishes the expected behavior in that case. If the expectation depends on a new design choice, report the observation and the open question outside the defect count and merge conditions. If a proposed fix for a confirmed regression would also extend a guarantee, keep that extension optional and judge the regression on its own evidence. If you recommend holding the merge, identify the findings or missing acceptance evidence that justify waiting. Explain the consequence. Keep missing evidence outside the defect count. Priority alone does not establish either judgment. If an unresolved requirement would change the verdict, ask for the missing decision and keep it outside the defect count.

Each finding gives a precise title, priority or impact, the location in the examined state, expectation or rule, consequence and supporting evidence. Include triggering conditions for behavioral defects and the relevant maintenance situation for design concerns. Give a repair direction when supported, without requiring a patch. Label a justified heuristic as a design concern rather than a confirmed defect. Keep pure preferences and tool-enforced formatting noise out of the findings; include material check failures in the check results. Use the project's priority convention when present, otherwise explain impact plainly.

Conclude with the comparison and examined state, coverage of both axes, actual checks and their material limits. State which reviewer covered each axis, any cross-axis evidence, and which checks were run now or reused. Keep any unmet isolation requirement explicit. Keep relevant pre-existing issues and unresolved questions distinct from introduced defects. Report "no supported findings in the reviewed scope" when appropriate; do not manufacture findings or imply that unexamined behavior is correct. A passing axis cannot conceal that the other was not reviewed.

Return the result to the consuming workflow. It decides how to handle findings and performs final integrated-state acceptance checks. Review evidence does not replace that verification or grant publication authority.

## 5. Review a revision

Recover the previous examined state, findings, evidence and dispositions before reviewing a follow-up. Inspect the repair, new changes and affected behavior. Widen review when risk or new evidence warrants it, including consumers outside the latest diff. Recheck the original trigger against the repaired state before closing a finding. Revisit the whole-change rating if the failure path, consequences, affected users or recovery conditions change. A repair can pass its new checks and retain its original risk level.

For example, a caller stays unchanged while its dependency changes from throwing an error to returning an empty value. Recheck the caller's error handling before reusing the earlier conclusion. An unrelated copy edit leaves that conclusion usable when its conditions still hold. Retain earlier checks with their examined state. A changed condition makes the current conclusion uncertain until checked, rather than proving a defect.

Preserve supported resolutions. Reopen a finding when new evidence changes its basis, rather than repeating an unchanged objection. Assess newly supported material problems even in unchanged code. Report resolved, remaining and new findings with their evidence changes; do not repeat the entire earlier report without a reason.

If review and repair alternate without resolving the underlying conditions, or further rounds add little evidence, identify the conflicting assumptions or missing check and adjust the approach. Keep a genuine behavior choice with the user. No fixed round count proves completion. Finish this review pass when resolved, remaining and new findings have been reported with supporting evidence and explicit limitations. A remaining finding can end the review pass without being fixed; the consuming task decides its disposition and owns any repair.
