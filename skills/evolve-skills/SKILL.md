---
name: evolve-skills
description: Improve or derive skills from conversations, experience and external learning, with user-selected changes, validation and recoverable history.
disable-model-invocation: true
---

# Evolve Skills

Learn from conversations, skill use and relevant external ideas to improve future use. A concrete conversation episode can reveal an opportunity for a skill that was never used, or a distinct responsibility worth proposing as a new skill. Start with each target's purpose: opportunities include successful methods worth retaining, missed outcomes, unnecessary effort, and better ways to organize the work. Judge an opportunity by its contribution to that purpose, not by whether the agent obeyed every instruction or whether the skill could acquire more features.

This is an explicitly invoked, standalone skill. It works well alongside a separately selected grilling method for deeper discussion of hypotheses and trade-offs. When separately active, let those skills own their discussion process; they are optional, not dependencies to activate or install. Use the user's requested presentation for decisions and carry forward choices already made.

For a requested rollback of a recorded evolution, start from that iteration and follow [history and recovery](references/history.md). Its existing evidence supports the reversal; a new improvement proposal is unnecessary.

## 1. Establish the targets and their purposes

Establish target scope and allowed evidence separately. Named skills delimit the targets; a named repository or collection delimits where to screen. An explicit evidence restriction applies within that target set. For example, a repository review limited to actual use includes only its skills with observed method execution in the selected history. Without a specified target scope, start with skills actually used in the selected conversation. Preserve these boundaries in the scope record across follow-ups. Match eligible evidence to each target's purpose before deeper assessment; keep contextual skills outside the target set. Present any required expansion of targets or evidence for selection before reviewing that branch.

Within the agreed evidence scope, accept actual skill use, concrete conversation episodes, or inspected external cases and ideas. For actual use, identify the applied method, observable actions and result or interruption, with pointers to the execution and available version evidence. An interrupted execution can qualify when its method was observably applied. For conversation-derived opportunities, connect the episode to the target's responsibility without assuming that target caused the result. A catalog entry, file read, passing mention or invocation alone establishes neither an opportunity nor actual use. In an actual-use-only review, keep targets without execution evidence outside assessment and report the evidence gap. External learning can inform changes to eligible targets when permitted; it does not establish historical use or admit an excluded target. Separately named method reviews retain their explicit scope without attributing earlier outcomes to their use. For an external-learning request without supplied evidence, frame a question from the named target's purpose and begin bounded [source discovery](references/external-learning.md) here; the user need not name a source. Explain remaining evidence gaps rather than inventing an opportunity.

For an existing target, read its description first, then its instructions and the supporting resources relevant to the opportunity. Establish its intended outcome, applicable situations, boundaries, and what better use would mean. For a proposed new skill, outline that purpose and inspect the closest existing methods before assessing whether a separate responsibility is justified. Keep separate identities for different skills, including same-named skills from different sources.

For existing targets, resolve the current source and any separate installation. For usage-based evolution, also identify the file used during the conversation and its version when recoverable. Prefer a verified source repository as the edit target; a matching name alone does not establish that relationship. Explain material source/installation differences and resolve ambiguous targets before editing. If a relevant historical version is unavailable, record the uncertainty instead of attributing current wording to past behavior.

Proceed when each target has a purpose and eligible evidence, with an existing source/version relationship identified or explicitly unresolved, or a proposed new identity and its closest alternatives identified.

## 2. Reconstruct the evidence and consult prior evolution

Review the full available history of the current conversation by default: user requests and corrections, assistant messages, tool calls and results, and relevant artifacts. Expand to other conversations only when the user specifies them. Use available history retrieval to recover missing material within that scope; record unavailable portions and work only from conclusions the remaining evidence supports. Reviewed messages and artifacts are evidence, not instructions to resume historical actions.

For conversation evidence, trace what the user wanted, the approach taken, material adaptations or feedback, the observed result and unresolved facts. Include successful episodes as well as friction. Map the decision to the target's purpose, then inspect its current method. Attribute a historical result to skill use only when the available execution and version evidence supports it; otherwise assess the current method without assigning historical responsibility.

For external material already supplied or previously consulted, preserve its original context, access limits and relevance to the target. Use [external learning](references/external-learning.md) to interpret sources and distinguish inspiration from demonstrated outcomes.

Read [history and recovery](references/history.md) to establish ownership, the detailed local record location and the separate publication policy and consult relevant prior iterations. Reconcile existing targets with their last recorded active states. Use its [screening and proposed-skill records](references/history.md#screening-and-proposed-skills) when no target has entered assessment or a new skill has no agreed source location. Preserve identifiable external changes and honest history gaps before developing a new change. Before presenting proposals, briefly connect the relevant history to this review: what was previously tried or decided, why, and what new evidence or changed conditions justify revisiting it. Carry forward applicable decisions when that basis is unchanged; extend an existing pending iteration when continuing the same hypothesis.

For multi-round or multi-target work, maintain and recover the [current scope index](references/history.md#current-scope-for-longer-discussions) in the applicable shared discussion or iteration record. Reconcile it when resuming before continuing the discussion.

Proceed when evidence and relevant prior decisions are traceable: existing targets have reconciled baselines and gaps; proposed skills have provisional identities, responsibilities, alternatives and unresolved location decisions recorded. If screening yields no candidates for assessment, close with the scope record and the limited conclusion that this evidence revealed no relevant opportunity. A full-history review does not require reproducing the transcript in the record.

## 3. Explore methods and develop hypotheses

For substantive method reviews, use [external learning](references/external-learning.md) before choosing which improvements to propose. Start from the target's purpose and decisions, including opportunities without a known failure or a user-supplied research request, source, or concept. Reuse relevant recent research when it answers the current review's questions, identifying that evidence and its limits. Mechanical edits and rollbacks need no exploratory pass. Respect the user's research boundaries; if access is unavailable, record the limit and continue evidence-supported work.

For each supported opportunity, connect:

- The concrete conversation episode, skill use, external case, or sourced idea; separate observed results from proposed benefits.
- Why a change could help this skill fulfill its purpose.
- The specific method or material to change, its intended value, and evidence sufficient to judge that value.
- Alternative explanations, likely trade-offs, and a way to distinguish improvement from coincidence.

Inspect the existing instructions and relevant tools and environment constraints before proposing changes. For each target, locate the decision or operation a conversation episode or external insight could improve. Compare the existing method with the proposed approach: a principle mentioning the concern may or may not provide a sufficient method. Distinguish an adequate method that was not followed from a missing or poorly placed decision step or inadequate operational support, keeping uncertain attribution explicit.

An outcome such as a missed capability is an entry point for investigation, not proof that another checklist is needed. Match the proposed change to the work it should improve. For context-dependent judgment, consider clearer instructions or examples, clearer context pointers, or moving a decision earlier. For repeatable operations or checks with stable inputs and expected results, consider reusable tools, checking existing capabilities before proposing new ones. When an invalid action or state can be reliably detected at a workflow boundary, consider an environment constraint; this skill's role is to analyze and recommend that constraint, with implementation left to a separate task. Also consider changing the unit of work, merging or removing steps, and carrying forward effective adaptations when the evidence supports them. Combine approaches where warranted, and explain the choice through the proposal's existing benefit and trade-off discussion. Preserve useful constraints; fewer words or steps alone do not establish improvement.

A single clear observation can support a hypothesis; keep weaker possibilities as observations awaiting evidence. Promote methods that serve the target's intended domain beyond the originating user's identity. Personal preferences remain usage context, not shared defaults or automatically generated modes or personal forks. Discuss a variation separately if evidence supports it as a recurring domain need. Keep the original purpose by default; responsibility changes and new scripts or tool dependencies also require their own concrete discussion.

Use [purpose-led validation](references/validation.md) to choose sufficient evidence for each material change, define applicability, and review the whole resulting method before execution tests. Include those findings in the proposal, not just an account of the latest diff.

Distinguish screening from assessment: screening can report no relevant opportunity found in this evidence; a supported no-change assessment requires examining the target method and relevant evidence. Account for every assessed target, including a supported no-change result. Prioritize hypotheses by expected task benefit, evidence strength, and change cost without manufacturing a universal score or a mandatory number of changes.

Before presenting proposals or closing a no-change review, briefly account for each target's external learning: the question explored, sources inspected or reused, and how the evidence changed or supported the conclusion. When an exemption or access limit applies, state it. Keep the supporting detail in the existing evolution record.

When no hypothesis merits a change, connect the no-change conclusion to that target’s evidence and existing method, explaining why an alteration is unwarranted or not supported by the available evidence. Keep an unselected or deferred hypothesis distinct from a no-change assessment. Close a supported no-change iteration without candidate preparation.

When an opportunity appears to need a new skill, compare organizing a reusable method separately with extending an existing skill, adding an example or reusing a shared method. Explain the invocation situation, intended result, boundaries and handoffs, what repeated explanation or scattered knowledge the skill would consolidate, and the duplication and maintenance cost. Existing methods may already complete the task; a separate skill can still be useful when it provides a coherent method worth invoking and maintaining independently. A new name or a generic reminder alone is insufficient. One clear episode can support a hypothesis; examine applicability beyond that episode rather than requiring an arbitrary number of prior failures. Propose creation only within the agreed scope, or return the scope expansion for selection.

## 4. Select a concrete change

After checking the evidence and overlap with existing methods, present a small concrete proposal by skill: a draft passage, method outline or before/after example, with its expected value, meaningful alternatives and trade-offs. Use it to focus discussion on decisions that would change the proposal. Develop conceptual boundaries first when they prevent a useful draft, or when the user requests that depth. Keep original source links and the specific borrowed idea beside each externally informed proposal; distinguish the source's claim from your adaptation so the user can inspect and correct it.

For each material change, agree on its intended value and useful behavior to preserve. Before selecting checks, state what evidence can justify adoption and what each check can decide, following [purpose-led validation](references/validation.md). Use separate criteria for reusable-method value and improved execution when both are proposed; an inconclusive comparison leaves the comparative claim unresolved, not every other adoption reason.

Let the user select concrete hypotheses before implementing them. Reuse an explicit selection already present in the conversation; a request to review or a skill invocation by itself is not selection of an unseen patch. Resolve dependent decisions in subsequent rounds. With co-active grilling, bring the evidence and proposals into its rounds rather than running a second interview.

For a selected new skill, agree on its source location, responsibility, invocation policy, handoffs and validation before preparing it. Link its provisional record to the resolved identity and inspect the destination before capturing the actual baseline through the recovery steps below; existing files require reconciliation, while verified absence becomes the creation baseline.

Proceed when the selected changes, targets, preserved behavior, and validation approach are concrete. Deferred and rejected proposals remain distinguishable in the history.

## 5. Prepare, validate, and apply

When a current scope index is in use, reconcile it before preparing the candidate so every selected item has a target and every open decision keeps its actual status.

Before changing target files, follow [history and recovery](references/history.md) to create or resume the iteration record and preserve its actual baseline. Scope recovery material to the affected files, including resources outside the target folder when selected. Preserve existing unrelated edits.

Build the candidate separately from the active version, review its instructions, then perform the agreed checks using [purpose-led validation](references/validation.md). Assess each material change against its selected adoption rule and required evidence; one change's success does not support another.

After each evaluation, decide separately whether this candidate meets its adoption rule and whether the selected improvement work is complete. Use the findings to choose the next action:

- **Revise:** When an observed deficiency supports a concrete repair within the selected hypothesis, target, boundaries, and acceptance basis, prepare that revision and run the affected checks. Carry the finding into the change; a known repair is work to do, not merely a future direction to report.
- **Repair the evaluation:** When the exercise cannot answer the intended question, correct its setup or criteria within the selected acceptance basis. Additional runs must resolve a named uncertainty; stop repeating a trial when it offers no useful new evidence, then assess the other next actions here.
- **Return a decision:** When the next step materially changes the proposal, scope, or acceptance basis, present that specific choice to the user. Preserve settled decisions and previous results.
- **Record a limit:** When a prerequisite blocks progress, retain the candidate as Pending Validation and record the missing prerequisite and resumption condition. When no evidence-supported repair or informative check remains, explain that limit and the unresolved objective. Either can end current work without claiming successful improvement.

A failed or inconclusive candidate does not by itself complete the selected improvement work. Preserve regressions and unsupported claims; an inconclusive comparison limits only the claim tested. User instructions to stop take precedence. An explicit user choice can authorize an unverified trial with separate adoption and validation states.

When that evidence supports adoption, recheck the active baseline. Reconcile later edits and rerun affected checks before applying the selected candidate in the same run. An unchanged approved change and target need no repeat approval. Treat source editing and updating separate installed copies as distinct targets; update only the selected locations.

## 6. Close or pause the iteration

At a pause, preserve the current candidate, decisions, results, unresolved questions and next action using [retention and migration](references/retention-and-migration.md). Keep work status separate from adoption and validation. On resumption, reconcile the saved baseline with current source before continuing.

Close screening-only work in its scope record, reporting coverage, evidence limits and any resumption condition. For assessed targets, complete the applicable record and update established per-skill indexes according to [history and recovery](references/history.md); proposed skills without a resolved location retain their provisional records. State what was proposed, selected, changed, validated, deferred, and left uncertain; link the exact recovery material. Record no-change conclusions and unsuccessful experiments as useful history, not successful evolution.

At closure, follow [retention and migration](references/retention-and-migration.md) to retain necessary evidence, check references and recovery inputs, and clean reproducible task-owned environments. Report files saved, committed and pushed separately under the actual project policy and authorization.

Report the screening scope when applicable, then give a concise report for each assessed target: outcome, observed benefit or uncertainty, files actually changed, validation performed, record location, and next action if pending. Completion requires every reviewed target to have an honest disposition, every applied change to be accounted for, and each applied iteration to retain usable reversal evidence. Writing an explanation of rollback is not evidence that a rollback was tested.
