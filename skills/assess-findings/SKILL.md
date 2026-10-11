---
name: assess-findings
description: Assess findings and feature opportunities, preserve related evidence and decisions, and recommend scoped next actions. Use for Just, Yak or Explore handoffs and decisions about a fix, improvement or PR.
---

# Assess Findings

Turn an observed finding into a supported judgment and a useful next-action recommendation. Assess the finding's basis separately from the value of a proposed response. A worthwhile optional improvement can justify a PR without being necessary; reproducibility alone establishes behavior, not a defect.

Use [investigate-with-evidence](../investigate-with-evidence/SKILL.md) for factual uncertainties that could change the judgment. Install both skills together. This workflow authorizes analysis and bounded investigation within the consuming task's permissions; repair and publication remain separate actions.

## 1. Establish the assessment and its owner

Keep one accountable assessment owner for a bounded set of related findings or opportunities. The coordinator may assess directly or delegate under [coordination](references/coordination.md); reuse that owner and existing judgments across Just, Yak and Explore. Investigations return through the coordinator rather than recursively creating teams. Missing investigation support leaves only the dependent judgment pending.

When capturing or resuming persistent evidence, read [working records](references/working-records.md). Reuse the original record, keep observations before final judgment, and preserve its user decisions. If no destination or save authority exists, establish it while continuing permitted analysis; retain unsaved evidence explicitly. Session-only assessment remains available when the consuming task requests it.

Identify the scenario, affected version and environment, inspectable evidence, expectation basis, demonstrated or proposed value, current response goal, material unknowns and source/history permissions. For an opportunity, a concrete desired outcome takes the place of a claimed behavioral failure.

A packet may initially lack some of these facts. Preserve the gaps instead of filling them with inferred certainty. Related observations share an assessment when the same response and acceptance boundary resolve them; independently valuable responses remain distinguishable.

Proceed when ownership, the question, existing evidence, and permitted checks are explicit.

## 2. Respect the evidence phase

Early handoff allows feedback while usage continues. Under a Just audit, assess supplied evidence first and request discriminating public-use comparisons from usage workers. Implementation source remains closed until the coordinator ends blind usage. Once source access opens, source-supported investigation may proceed while source-discovered environments and capabilities are still being exercised. Target tracker history opens only after that additional usage finishes, or the coordinator explicitly freezes a partial audit and its independent findings. Carry these permissions through every delegated task and resumed assessment.

For standalone work, establish the consuming task's access boundaries directly. Obtain missing phase permission from the coordinator rather than assuming that assignment to Assess opens source or tracker history. Mark judgments awaiting a gate as provisional, continue permitted work, and revisit them when the gate opens.

When Yak is co-active, it owns tracker reconciliation and returns relevant records, coverage, and unresolved overlap through the coordinator. Assess consumes that evidence without invoking Yak recursively. Without Yak, perform the configured read-only tracker search once permitted, checking relevant open and closed issues and PRs and what their actual changes or discussion cover. A title, status, or empty search result alone establishes neither resolution nor novelty. Missing tracker access limits a new-PR recommendation specifically; it does not invalidate independently supported behavior or classification.

Proceed with all currently permitted decisive checks; preserve deferred checks with their reopening condition.

## 3. Judge the finding's basis

Separate what happened from why it matters. Establish the expected outcome from relevant documentation, accepted requirements, consistent product behavior, or the concrete task the interface offers. An implicit contract can be supported by the workflow and a controlled comparison; a written specification is not mandatory. Explain the basis so a reviewer can distinguish it from personal preference.

Trace the affected user path far enough to establish impact. Distinguish observed obstruction or misleading output from possible consequences. A workaround may reduce severity while leaving the original path defective. An isolated component example demonstrates that environment; verify the consumer path when the classification depends on integration. Source anomalies can explain behavior but do not supply missing user impact by themselves.

Use the smallest discriminating check for each material uncertainty. Before requesting it, state which possible results would change the judgment. Investigate root cause only as far as correctness, remedy, ownership, or scope requires. Repeatedly reproducing an established fact adds no decision evidence.

Express the supported disposition in ordinary language, optionally using these labels:

- **Confirmed defect:** demonstrated behavior conflicts with a supported expected outcome under the stated conditions.
- **Improvement opportunity:** a concrete user outcome supports a valuable change without an established contract violation.
- **Unresolved observation:** a named missing fact prevents classification or impact judgment.
- **Excluded:** evidence defeats the claimed defect or opportunity within its stated scope; record the reason.

Proceed when the classification has a traceable basis or an exact unresolved dependency. Keep evidence about behavior, cause, and impact distinct.

### Evaluate an opportunity and related observations

For an idea, evaluate its concrete user situation, incremental value over the closest working alternative, plausible implementation evidence and meaningful costs. Separate observed demand from hypothesized benefit. Reuse Explore's research and prior-work results; request only decision-changing gaps. Explore owns discovery and user discussion; Assess owns the resulting judgment, not a second discovery campaign. An opportunity need not establish a defect or necessity to be worthwhile.

Compare newly accumulated observations with relevant records before choosing repair units. Distinguish one Problem Identity, independent problems, and distinct problems with possible causal, blocking or masking relationships. Record each relationship's evidence and uncertainty. A common component or suspected cause does not merge acceptance boundaries. An individual finding with sufficient evidence need not wait for a batch.

When a relationship could change scope, ownership or remedy, request the smallest check that separates the competing explanations through Investigate. Return confirmed and rejected relationships to the coordinator, revise only affected judgments, and notify affected usage or implementation owners. If one symptom disappears while another remains, retain the latter's acceptance boundary rather than declaring the whole group resolved.

## 4. Recommend a response

Fix the response goal before evaluating a remedy. Connect a proposed change to that goal, its evidence-backed benefit, the responsible consumer or repository, and meaningful costs or existing alternatives. Separate independent goals and remedies: explaining an empty view and correcting a library calculation may each have value without either requiring the other.

A positive PR recommendation needs a concrete scenario and goal, a supported defect or reasoned practical improvement value, a plausible change that achieves that goal in the appropriate owner, relevant tracker reconciliation, and no outstanding factual uncertainty that could overturn the recommendation. State reasoned benefits as reasoning when they have not been directly observed. Necessity is a stronger claim than worthwhile improvement; assess it only when the decision requires it. When a finding summary or the requested decision calls for priority, assess it using the method below. Yak requests this assessment by default for confirmed findings; other callers retain their reporting scope.

Recommend the useful next action: a scoped independent PR, contribution to existing work, a specific further check, deferral with its reason, or no change under the assessed conditions. Distinguish recommending an approach from validating a patch: inspect an actual proposal before claiming its implementation correct. Missing evidence should narrow the recommendation to what is supported, not erase established facts or imply the opposite conclusion.

### Assess suggested priority

Priority recommends how urgently to address a finding; severity describes its impact. Use the project's applicable priority scale when available and identify it. Otherwise use this fallback, label the result **Suggested priority**, and briefly state the scale once per report:

| Priority | Meaning |
| --- | --- |
| P0 | Respond immediately: major harm is occurring or imminent and requires immediate containment or action. |
| P1 | Fix ahead of routine work: a critical user path is severely blocked with no acceptable alternative. |
| P2 | Schedule a fix: demonstrated impact is bounded or an acceptable workaround exists. |
| P3 | Defer if needed: the impact is minor and does not materially obstruct task completion. |

Judge actual impact, trigger conditions, affected scope, urgency, and available alternatives together. A workaround does not make ongoing major harm routine. Do not infer a low priority from a documentation label or missing evidence, and do not infer P0 from an unverified security suspicion. These levels imply no fixed repair deadline.

Return the level, its scale, a short evidence-based reason, and material limits with the existing assessment. If a missing fact prevents a defensible level, return **Priority undetermined**, name that fact and the next check; retain the observation's classification. When the classification itself is unresolved, a follow-up's urgency is not a confirmed bug priority. Preserve immediate warnings for credible harm while further assessment is pending.

Proceed when the recommendation follows from the assessed goal and evidence, with ownership and decision-relevant limits explicit, and any requested priority has a supported level or an explicit unresolved dependency.

## 5. Preserve the judgment across follow-ups

Preserve the assessment in the original authorized Working Record: decisive evidence, relationships, selected goal and scope, preserved behavior, acceptance conditions, unresolved user decisions and supported next action. Reuse agreed discussion or link an existing spec; 'worth doing' alone does not establish readiness to implement. The coordinator owns the save and index update under the working-record contract.

Return the finding's disposition, its decisive evidence and expectation basis, the response recommendation and rationale, any assessed priority and its basis, and any remaining dependency. Scale the report to the finding rather than requiring a fixed template. The coordinator reconciles the results into the consuming task's final report; it checks the evidence and unresolved conditions rather than treating worker agreement as proof.

On follow-up, retain the version, scenario, response goal, and previous reasons. Keep unresolved, evidence-backed reasons for questioning a judgment with that judgment. When updating it, explain which reasons the new evidence, corrected inference, or changed requirement addresses; revise only the judgments it affects. Retain limits that still apply and drop reasons that no longer apply. A renewed request for objections invites examination of the same proposition, not an automatic verdict reset. If an objection concerns a different goal, distinguish that question and preserve the earlier result. When accepted facts leave a value trade-off, explain the choice and who bears its cost.

Finish when permitted decisive checks and concrete counterevidence leads have been resolved and no specific remaining check could materially change the recommendation. For pending gates, missing access, queued work, or unresolved user-owned requirements, report what is established, the exact pending work, and the resumption condition. Continue unaffected work. Assessment completion does not authorize implementation or external publication.
