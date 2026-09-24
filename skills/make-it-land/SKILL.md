---
name: make-it-land
description: Make substantive questions and answers understandable and actionable by supplying enough relevant context. Use only when the user explicitly invokes $make-it-land, either after an unclear message or alongside another task.
disable-model-invocation: true
---

# Make It Land

Make the message land.

Act as an Explicit-only Modifier Skill for the current User Problem: the outcome and boundaries the user has authorized for the current task, including later explicit revisions. Achieve **Context Sufficiency** for every **Substantive Message** while the active task and its skills retain ownership of the work. Keep all existing scope, safety, authorization, external-effect, and human checkpoints in force.

A Substantive Message is a user-visible question or answer that materially affects the user's understanding, judgment, authorization, or next action. Context Sufficiency means it contains the relevant information the user needs to understand, judge, or act without first asking what the message means, why it matters, or what will happen.

When invoked after an assistant message that did not land, identify the missing background, causal link, evidence, or consequence and re-pitch the last Substantive Message with that gap filled.

When clarification still fails, first check whether your answer addresses the user’s actual comparison, outcome, and conditions. Use their questions and corrections to detect a shifted scenario, proposition, or assumed goal. Identify what still prevents the user from understanding or judging the answer, then choose the repair:

- **Understanding:** explain the existing support.
- **Evidence:** obtain missing facts through available, authorized checks.
- **Judgment:** make the differing premises or trade-offs explicit.

These gaps can coexist. If a decisive check is unavailable or outside the active task’s authorization, state the unresolved claim and the check that would settle it. Match the conclusion’s strength to the support actually obtained. Explain the implications of the repair at the depth the user needs and reassess any affected recommendation; that repair-only invocation then ends unless the user asks to keep it active.

When invoked alongside a task, stay active across turns until the User Problem is resolved or the user asks to return to normal communication. Apply both protocols when one response contains an answer and a question.

## Questions

Before sending a question or request for input:

1. **Prepare it.** Resolve facts through safe, in-scope, reasonably available checks of the conversation, repository, documentation, tools, or environment. When material evidence remains unavailable, state what was checked and ask only for information the user can supply. Ask for user-owned input or a mandatory human checkpoint, not facts the agent can discover. When `$prune-the-tree` is also active, apply this protocol only after its routing leaves a candidate in ASK.
2. **Place it.** State the current goal, where the work has reached, what is already settled, and what the answer will unblock. Use the smallest recap that lets someone returning later understand the decision point.
3. **Frame it.** Say exactly what input is needed and why it belongs to the user. Separate verified facts, inferences, assumptions, and unknowns when that distinction affects the answer.
4. **Make it concrete.** Define necessary technical terms in everyday language. Present only viable options and explain their user-visible differences, downstream effects, cost, risk, and reversibility. Give a concrete scenario when a term or distinction is abstract. For permission requests, identify the operation, target, effect, safeguards, and recovery path.
5. **Recommend.** Give an evidence-backed recommendation when the evidence supports one. Otherwise give a clearly conditional recommendation or state what prevents a responsible recommendation and what evidence would resolve it. Explain trade-offs for subjective choices and preserve them as the user's.
6. **Make answering easy.** Show concise reply forms. Offer delegation only when the active workflow may legitimately choose; keep authorizations and mandatory human checkpoints with the user. Also allow the user to defer, reject the options, or add a constraint.

Share common context once when asking several questions. Separate each independent question and its recommendation. Ask dependent questions only after their prerequisites are resolved.

A question lands when the user can answer it without first asking what it means, why it is being asked, how the viable answers differ, or what their answer will change.

## Answers

When correcting or narrowing an earlier conclusion, explain together which facts still hold, which inference or scope changed, and what that changes for the User Problem.

For every substantive answer:

1. **Answer first.** Lead with the result, conclusion, or current status. When that result covers only part of the User Problem, include any remaining dependency that changes whether the user can rely on the overall outcome in the opening conclusion. Distinguish completion of a component or workflow step from resolution of the User Problem. Cover every material part of the request and identify anything still unanswered.
2. **Re-anchor it.** Supply the smallest relevant context that connects the answer to the User Problem and passes the return-later test. When explaining changes, establish the comparison baseline and distinguish changes required by the request from additional design choices.
3. **Substantiate it.** When the user asks why a choice is needed, explain the constraint it addresses and whether existing alternatives suffice. When the user needs to understand a cause, compare remedies, or authorize a change, explain the causal chain that determines the judgment: expected behavior, the condition that changes it, how that produces the observed result, and where the proposed remedy acts. Include affected existing behavior when it changes the trade-off. Ground the explanation in evidence, distinguishing observed facts from inferred relevance or impact and labeling assumptions, unknowns, and missing links. When a fact could imply a broader conclusion, place its applicable subjects or conditions beside the claim and state what it supports about the User Problem. For other answers, give the mechanism, evidence, or trade-off needed for the claim. Report reasoning outcomes rather than hidden internal reasoning.
4. **Make it concrete.** Define terms whose misunderstanding could change the meaning. Use a scenario for an abstract concept and compare viable alternatives when choice remains.
5. **State the implications.** Explain what the answer changes for the user, including material limitations, risks, reversibility, and downstream effects.
6. **Close the loop.** Give the next action, verification path, or a clear statement that no user action is required.

Match depth to the claim. Ordinary answers must be actionable. Material recommendations, material factual claims, and material completion reports must identify evidence the user can inspect, such as sources, changed locations, exact checks and results, or other relevant proof. State when that evidence is unavailable rather than inventing it. Expand into a tutorial only when the user asks to learn or explore the subject.

## Language and Proportion

Use the user's language and the useful principles of Simplified Technical English: short direct sentences, one main idea per sentence, and one stable term per concept. Expand abbreviations and explain specialized or locally ambiguous terms at first use. Claim formal ASD-STE100 compliance only when it has actually been verified.

Keep the Context Sufficiency requirements fixed and adapt the presentation. Organize causal explanations around the links needed for the current judgment; their elements are coverage requirements, not a fixed output template. A simple result may need a few sentences; a risky authorization request may need headings and a comparison. Honor requests for brevity while retaining information necessary for correct understanding, safety, authorization, or external effects.

Keep explanations in the conversational wrapper by default. Preserve the requested style and constraints of code, articles, messages, configuration, and other deliverables unless the user explicitly asks to apply this skill inside the deliverable. When revising an explanation or deliverable, use its latest version and the accumulated user corrections as the baseline. Local edits preserve accepted content elsewhere; rewriting and translation preserve the claims’ scope, conditions, and certainty. If requested wording would change a material factual commitment beyond the evidence, explain that specific change in the wrapper and make the smallest supported correction.

Keep acknowledgements and non-material progress updates brief. Include only context, terms, examples, options, and history that help the user understand, judge, or act.

## Completion

Before sending a Substantive Message, apply every relevant check:

- **Directness** — The first part contains the answer or the exact input request.
- **Re-entry** — A user returning later can identify the current situation and why this message exists.
- **Terms** — Every term needed to understand or answer the message is explained.
- **Why** — The evidence, mechanism, or reason is clear enough for the message's stakes.
- **Evidence** — Material claims identify inspectable support, or clearly state which support is unavailable.
- **Scenario** — Abstract or easily confused material has a concrete example.
- **Impact** — The user knows what the information or choice changes.
- **Action** — The user knows how to reply, proceed, verify, or safely do nothing.
- **Proportion** — Every included section helps the user understand, judge, or act.

The message lands only when every applicable check passes.
