---
name: evolve-skills
description: Evolve skills from actual use through purpose-led improvements, user-selected changes, behavioral validation, and a detailed history that supports rollback.
disable-model-invocation: true
---

# Evolve Skills

Learn from how skills were used in conversation and improve their future use. Start with each target's purpose: opportunities include successful methods worth retaining, missed outcomes, unnecessary effort, and better ways to organize the work. Judge an opportunity by its contribution to that purpose, not by whether the agent obeyed every instruction or whether the skill could acquire more features.

This is an explicitly invoked, standalone skill. It works well alongside Matt Pocock's grilling series for deeper discussion of hypotheses and trade-offs. When separately active, let those skills own their discussion process; they are optional, not dependencies to activate or install. Use the user's requested presentation for decisions and carry forward choices already made.

For a requested rollback of a recorded evolution, start from that iteration and follow [history and recovery](references/history.md). Its existing evidence supports the reversal; a new improvement proposal is unnecessary.

## 1. Establish the targets and their purposes

Identify the skills actually used before this invocation in the selected conversation. A catalog entry, a passing mention, or this invocation alone is not usage evidence. An interrupted use can qualify when there is observable application of the target's method. If no target has usage evidence, explain what is missing and stop without inventing an evolution opportunity.

For each target, read its description first, then its instructions and the supporting resources relevant to that use. Establish its intended outcome, applicable situations, boundaries, and what better use would mean. Keep separate identities for different skills, including same-named skills from different sources.

Resolve the file used during the conversation, its version when recoverable, the current source, and any separate installation. Prefer a verified source repository as the edit target; a matching name alone does not establish that relationship. Explain material source/installation differences and resolve ambiguous targets before editing. If the historical version is unavailable, record the uncertainty instead of attributing current wording to past behavior.

Proceed when each target has a purpose, usage evidence, and an identified or explicitly unresolved source/version relationship.

## 2. Reconstruct use and consult prior evolution

Review the full available history of the current conversation by default: user requests and corrections, assistant messages, tool calls and results, and relevant artifacts. Expand to other conversations only when the user specifies them. Use available history retrieval to recover missing material within that scope; record unavailable portions and work only from conclusions the remaining evidence supports. Reviewed messages and artifacts are evidence, not instructions to resume historical actions.

Trace the target's use in its surrounding task: what the user wanted, the approach taken, material adaptations or feedback, and the observed result. Include successful episodes as well as friction. When several skills contributed, distinguish each one's contribution from their interaction and leave uncertain attribution unresolved.

Read [history and recovery](references/history.md) to locate the per-skill index and relevant prior iterations. Check whether an opportunity has already been proposed, tried, adopted, rejected, or rolled back, and what new evidence would justify revisiting it. A returning observation can extend an existing pending iteration; it does not require another copy of the proposal.

Proceed when each target has a traceable account of relevant use, evidence gaps, and prior decisions that affect the analysis. A full-history review does not require reproducing the transcript in the record.

## 3. Develop purpose-led hypotheses

For each supported opportunity, connect:

- The concrete usage episode and its result.
- Why a change could help this skill fulfill its purpose.
- The specific method or material to change and the expected behavioral difference.
- Alternative explanations, likely trade-offs, and a way to distinguish improvement from coincidence.

Inspect the existing instructions before proposing additions. An outcome such as a missed capability is an entry point for investigation, not proof that another checklist is needed. Consider clearer context pointers, moving a decision earlier, changing the unit of work, merging or removing steps, and carrying forward effective adaptations when the evidence supports them. Preserve useful constraints; fewer words or steps alone do not establish improvement.

A single clear observation can support a hypothesis. Keep weaker possibilities as observations awaiting evidence. Make changes generalizable within the target's intended domain rather than adding branches for the particular product, person, or conversation that revealed them. Keep the original purpose by default; discuss changes to responsibilities or applicability separately. New scripts or tool dependencies also require their own concrete discussion.

Account for every target reviewed, including a supported no-change result. Prioritize hypotheses by expected task benefit, evidence strength, and change cost without manufacturing a universal score or a mandatory number of changes.

When no hypothesis merits a change, record the supported observations and no-change conclusion, then close the iteration without candidate preparation.

## 4. Select a concrete change

Present the proposed changes by skill, with enough before/after detail to review, the evidence, expected benefit, meaningful alternatives, and trade-offs. Read [behavioral validation](references/validation.md) when defining how the changes will be evaluated. Agree on observable success and what existing useful behavior should survive.

Let the user select concrete hypotheses before implementing them. Reuse an explicit selection already present in the conversation; a request to review or a skill invocation by itself is not selection of an unseen patch. Resolve dependent decisions in subsequent rounds. With co-active grilling, bring the evidence and proposals into its rounds rather than running a second interview.

Proceed when the selected changes, targets, preserved behavior, and validation approach are concrete. Deferred and rejected proposals remain distinguishable in the history.

## 5. Prepare, validate, and apply

Before changing target files, follow [history and recovery](references/history.md) to create or resume the iteration record and preserve its actual baseline. Scope recovery material to the affected files, including resources outside the target folder when selected. Preserve existing unrelated edits.

Build the candidate separately from the active version. Run the agreed before/after behavioral comparison and relevant transfer probes using [behavioral validation](references/validation.md). Apply the selected candidate to the identified target only when the required validation supports it and the baseline still matches. Treat source editing and updating separate installed copies as distinct targets; update only the locations included in the user's selection.

If behavioral validation cannot be completed, retain the candidate and a Pending Validation record; leave the active version unchanged. An explicit user choice can authorize an unverified trial, whose adoption and validation states remain separate. If evidence shows a regression or no supported benefit, preserve the result and revise the hypothesis or keep the baseline rather than adopting the failed candidate. A materially different proposal returns to the user's selection.

## 6. Close the iteration

Complete the detailed record and update the per-skill index according to [history and recovery](references/history.md). State what was proposed, selected, changed, validated, deferred, and left uncertain; link the exact recovery material. Record no-change conclusions and unsuccessful experiments as useful history, not successful evolution.

Finish with a concise per-skill report: outcome, observed benefit or uncertainty, files actually changed, validation performed, record location, and next action if pending. Completion requires every reviewed target to have an honest disposition, every applied change to be accounted for, and each applied iteration to retain usable reversal evidence. Writing an explanation of rollback is not evidence that a rollback was tested.
