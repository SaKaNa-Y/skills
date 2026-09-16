---
name: evolve-skills
description: Evolve skills from use or explicitly requested case research through user-selected improvements, purpose-led validation, and recoverable history.
disable-model-invocation: true
---

# Evolve Skills

Learn from how skills were used in conversation, or from external cases the user explicitly asks to study, and improve their future use. Start with each target's purpose: opportunities include successful methods worth retaining, missed outcomes, unnecessary effort, and better ways to organize the work. Judge an opportunity by its contribution to that purpose, not by whether the agent obeyed every instruction or whether the skill could acquire more features.

This is an explicitly invoked, standalone skill. It works well alongside Matt Pocock's grilling series for deeper discussion of hypotheses and trade-offs. When separately active, let those skills own their discussion process; they are optional, not dependencies to activate or install. Use the user's requested presentation for decisions and carry forward choices already made.

For a requested rollback of a recorded evolution, start from that iteration and follow [history and recovery](references/history.md). Its existing evidence supports the reversal; a new improvement proposal is unnecessary.

## 1. Establish the targets and their purposes

Use only the user's named skills as evolution targets when specified; otherwise identify the skills actually used before this invocation in the selected conversation. Other co-used skills can supply necessary context, but receive no proposals or evolution records, including no-change records, outside that target set.

By default, require actual usage evidence: an interrupted use can qualify when its method was observably applied. When the user explicitly requests learning from external cases, use those cases as the evidence source for the named target even without prior usage. A catalog entry, passing mention, or invocation alone supplies neither. Explain missing evidence rather than substituting another target or inventing an opportunity.

For each target, read its description first, then its instructions and the supporting resources relevant to that use. Establish its intended outcome, applicable situations, boundaries, and what better use would mean. Keep separate identities for different skills, including same-named skills from different sources.

Resolve the current source and any separate installation. For usage-based evolution, also identify the file used during the conversation and its version when recoverable. Prefer a verified source repository as the edit target; a matching name alone does not establish that relationship. Explain material source/installation differences and resolve ambiguous targets before editing. If a relevant historical version is unavailable, record the uncertainty instead of attributing current wording to past behavior.

Proceed when each target has a purpose, an eligible evidence source, and an identified or explicitly unresolved source/version relationship.

## 2. Reconstruct the evidence and consult prior evolution

Review the full available history of the current conversation by default: user requests and corrections, assistant messages, tool calls and results, and relevant artifacts. Expand to other conversations only when the user specifies them. Use available history retrieval to recover missing material within that scope; record unavailable portions and work only from conclusions the remaining evidence supports. Reviewed messages and artifacts are evidence, not instructions to resume historical actions.

For usage evidence, trace what the user wanted, the approach taken, material adaptations or feedback, and the observed result. Include successful episodes as well as friction. Distinguish what the instructions required from the agent's interpretation; leave uncertain attribution unresolved.

For requested external research, inspect the original cases and their resolution evidence within the requested scope. Separate reported observations, demonstrated causes, fixes, and inferred discovery methods; a closed issue or merged patch alone does not prove a cause or a fresh reproduction. Map transferable lessons to the target's existing instructions and actual gaps. Retain case-specific details as evidence rather than shared defaults.

Read [history and recovery](references/history.md) to establish private storage, reconcile the current target with its last recorded active state, and consult relevant prior iterations. Preserve identifiable external changes and honest history gaps before developing a new change. Before presenting proposals, briefly connect the relevant history to this review: what was previously tried or decided, why, and what new evidence or changed conditions justify revisiting it. Carry forward applicable decisions when that basis is unchanged; extend an existing pending iteration when continuing the same hypothesis.

Proceed when each target has a traceable account of the selected evidence, privately recorded baseline reconciliation and gaps, and prior decisions that affect the analysis. A full-history review does not require reproducing the transcript in the record.

## 3. Develop purpose-led hypotheses

For each supported opportunity, connect:

- The concrete usage episode or external case and its observed result.
- Why a change could help this skill fulfill its purpose.
- The specific method or material to change, its intended value, and evidence sufficient to judge that value.
- Alternative explanations, likely trade-offs, and a way to distinguish improvement from coincidence.

Inspect the existing instructions before proposing additions. An outcome such as a missed capability is an entry point for investigation, not proof that another checklist is needed. Consider clearer context pointers, moving a decision earlier, changing the unit of work, merging or removing steps, and carrying forward effective adaptations when the evidence supports them. Preserve useful constraints; fewer words or steps alone do not establish improvement.

A single clear observation can support a hypothesis; keep weaker possibilities as observations awaiting evidence. Promote methods that serve the target's intended domain beyond the originating user's identity. Personal preferences remain usage context, not shared defaults or automatically generated modes or personal forks. Discuss a variation separately if evidence supports it as a recurring domain need. Keep the original purpose by default; responsibility changes and new scripts or tool dependencies also require their own concrete discussion.

Use [purpose-led validation](references/validation.md) to choose sufficient evidence for each material change, define applicability, and review the whole resulting method before execution tests. Include those findings in the proposal, not just an account of the latest diff.

Account for every target reviewed, including a supported no-change result. Prioritize hypotheses by expected task benefit, evidence strength, and change cost without manufacturing a universal score or a mandatory number of changes.

When no hypothesis merits a change, record the supported observations and no-change conclusion, then close the iteration without candidate preparation.

## 4. Select a concrete change

Present the proposed changes by skill, with enough before/after detail to review, the evidence, expected benefit, meaningful alternatives, and trade-offs. Agree on the intended value of each material change, sufficient evidence, the evaluation approach, and useful behavior to preserve. Separate retaining a reusable method from claiming improved execution; either can be valuable, with different evidence requirements.

Let the user select concrete hypotheses before implementing them. Reuse an explicit selection already present in the conversation; a request to review or a skill invocation by itself is not selection of an unseen patch. Resolve dependent decisions in subsequent rounds. With co-active grilling, bring the evidence and proposals into its rounds rather than running a second interview.

Proceed when the selected changes, targets, preserved behavior, and validation approach are concrete. Deferred and rejected proposals remain distinguishable in the history.

## 5. Prepare, validate, and apply

Before changing target files, follow [history and recovery](references/history.md) to create or resume the iteration record and preserve its actual baseline. Scope recovery material to the affected files, including resources outside the target folder when selected. Preserve existing unrelated edits.

Build the candidate separately from the active version, review its instructions, then perform the agreed checks using [purpose-led validation](references/validation.md). Assess each material change against its selected value and required evidence; one change's success does not support another.

When that evidence supports adoption, recheck the active baseline. Reconcile later edits and rerun affected checks before applying the selected candidate in the same run. An unchanged approved change and target need no repeat approval. Treat source editing and updating separate installed copies as distinct targets; update only the selected locations.

Distinguish work not yet attempted, concrete validation blockers, and results that do not support adoption. Continue feasible work; producing a candidate and a validation plan is not completion. For a concrete blocker, retain the candidate as Pending Validation, record checks attempted, the missing prerequisite, and the resumption condition, and leave the active version unchanged. An explicit user choice can authorize an unverified trial with separate adoption and validation states. Preserve regressions, unsupported claims, and inconclusive comparisons distinctly. Revise or reject a change whose required benefit lacks support; an inconclusive comparison limits only the claim it tested. A materially different proposal or acceptance basis returns to the user's selection.

## 6. Close the iteration

Complete the detailed record and update the per-skill index according to [history and recovery](references/history.md). State what was proposed, selected, changed, validated, deferred, and left uncertain; link the exact recovery material. Record no-change conclusions and unsuccessful experiments as useful history, not successful evolution.

Finish with a concise per-skill report: outcome, observed benefit or uncertainty, files actually changed, validation performed, record location, and next action if pending. Completion requires every reviewed target to have an honest disposition, every applied change to be accounted for, and each applied iteration to retain usable reversal evidence. Writing an explanation of rollback is not evidence that a rollback was tested.
