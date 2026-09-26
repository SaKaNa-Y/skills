---
name: challenge-the-claim
description: Test a specific claim with the strongest relevant evidence, distinguish factual disagreement from design trade-offs, and conclude honestly when no supported rebuttal is found.
disable-model-invocation: true
---

# Challenge the Claim

Examine whether a specified claim withstands a directed search for counterevidence. Success is an accurate judgment of that claim, including a supported rebuttal, a narrower conclusion, an unresolved fact, a value disagreement, or no supported rebuttal. The user chooses the goals and trade-offs; the skill tests the reasoning and factual commitments.

This is an explicit discussion and investigation entry point. Use [investigate-with-evidence](../investigate-with-evidence/SKILL.md) for factual investigation and controlled execution. Load the installed skill by name, or read its `SKILL.md` when the host has no skill invocation tool. Install both skills together. If the dependency cannot be found, identify it and leave dependent investigation pending; continue only conclusions supported by already available evidence, without claiming that the investigation is complete.

## Fix the claim and its conditions

Restate the actual proposition, relevant conditions, and the judgment it bears on. Use the speaker's words and available context; separate their stated position from a charitable interpretation or your own implication. When ambiguity materially changes what would count as a rebuttal, resolve it before choosing a target. Keep the request focused: a claim about one failure mechanism does not imply endorsement of an entire PR or implementation.

For a PR, inspect the description and changes relevant to the fixed claim. When the claim concerns the failure's cause, the fix's scope, or the description's accuracy, compare those assertions with the relevant diff, tests, and discussion. Distinguish a misleading description from a defective implementation or missing evidence. A review comment is a position to examine, not authoritative proof or permission to invent the reviewer's intent.

Separate factual premises, the inference to the conclusion, and value priorities. A preference for simplicity over compatibility is a trade-off; a claim that a design preserves compatibility is testable. Facts and logical consistency remain open to examination even when an argument also expresses a design philosophy.

## Investigate the strongest relevant challenge

Identify the premise, inference, or conclusion each candidate objection could change. When a factual uncertainty could affect the result, use `investigate-with-evidence` to resolve it. For a purely logical question under given premises, check whether the conclusion follows; finish that check once a valid derivation or counterexample settles the inference, or identify the missing premise that leaves it unresolved. Search for the most consequential supported counterexample or reasoning gap rather than collecting criticisms. Examine the strongest reasonable reading of the claim without adding conditions or ambitions the speaker did not assert.

A rebuttal must contradict a factual premise, expose an invalid inference, or show that the conclusion fails within its claimed scope. Evidence that a premise is false is relevant; merely replacing a given condition with a different scenario is not. A limitation outside that scope can inform another decision but does not defeat this claim. An alternative solution directly challenges a claim of necessity or uniqueness, but its existence alone does not disprove a claim that the original solution works.

Assess a concern separately from a proposed remedy. A defect can be real while a particular patch is unnecessary or incomplete. Conversely, an unnecessarily complex patch does not disprove the defect it addresses. Preserve these as separate judgments, using the user's actual claim to determine which one is under examination.

Carry the proposition and its conditions across follow-ups. New objections must affect that same proposition, or be explicitly introduced as a different question while retaining the earlier outcome. Withdraw an objection when evidence defeats it. The same standard applies to the user, another author, and your own earlier advice.

## Give the judgment and close the claim

Lead with the result for the original claim. When evidence supports a rebuttal, present the strongest point first: the exact premise or inference that fails, the decisive evidence or counterexample, and what consequence follows for the claim. Use direct language proportional to the evidence. One decisive objection is enough; rhetorical force, weak objections, and objection counts do not strengthen the result.

When the evidence supports only a scope restriction, state what remains true and under which conditions. When facts are missing, state the unresolved dependency and what would settle it. An unmet burden of proof may leave a claim unsupported without proving its opposite.

When the facts and consequences are accepted and the remaining difference is a value priority, name the trade-off and who bears its costs. Check consistency with the project's accepted requirements; distinguish changing those requirements from satisfying them. Once the relevant decision owner knowingly accepts a permissible trade-off, conclude that no factual rebuttal has been established. Further preference advocacy requires a separate user request.

Close after the relevant reasoning checks and any needed factual investigation are complete; apply the shared investigation's stopping condition only when that investigation was needed. Say plainly when no supported rebuttal was found under the examined conditions. Positive evidence can support the claim; failure to find a counterexample alone is not universal proof. Close this line without inventing a broader claim to oppose. Mention a genuinely decision-relevant adjacent issue only briefly as a separate direction for the user to choose; otherwise end.

Keep the conclusion, evidence, and practical limit together. Reopen a closed claim for materially new evidence, changed conditions, or an explicit change of target. This workflow produces analysis, not an external reply or product change; those actions require their own instruction.
