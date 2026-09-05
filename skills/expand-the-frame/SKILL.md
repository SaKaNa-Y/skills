---
name: expand-the-frame
description: Expand a project's decision space through informed questioning, uncovering relevant perspectives, explaining unfamiliar concepts, and tracing the implications of your answers.
disable-model-invocation: true
---

# Expand the Frame

Help the user recognize project-relevant questions they did not know to ask, understand the knowledge needed to judge them, and trace the implications of their answers. Improve project decisions and the user's ability to recognize similar questions elsewhere. More questions, agreement with the agent, and additional features are not measures of success.

This is a standalone, explicitly invoked discussion skill. One invocation lasts through the current discussion until the user ends it. It requires no other skill. It supports an existing project or an unrealized idea and may examine the project's goals as well as its design. The user owns goals and trade-offs; broader agent knowledge is a responsibility to investigate and explain, not authority to decide for them.

## 1. Ground the discussion

Establish the intended outcome, affected users, current proposal, and known constraints from the conversation and available project material. For an existing project, read its guidance, vocabulary, relevant documentation, and enough source to understand the proposal. For an idea, work from the stated context and label untested assumptions. Ask for missing user-owned context only when it changes which questions are relevant.

Investigate facts yourself. When a factual claim changes a question, its options, or the recommendation, check the relevant code, official documentation, or other primary evidence before relying on it. Match version-sensitive claims to the project. Distinguish observed behavior, supported facts, inferences, and hypothetical scenarios. If evidence is unavailable, narrow the claim or keep it unresolved rather than presenting a possibility as an existing defect.

Preparation is targeted: start discussing once the current questions have enough grounding. Later branches can require later investigation; a whole-project audit is not a prerequisite.

## 2. Surface perspectives beyond the initial framing

Look beyond the user's stated question for relevant assumptions, affected people, consequences, and alternative ways to achieve the outcome. Consider technical behavior, user experience, product goals, maintenance, cost, and operation where the project warrants them. Challenge the goal itself when there is a concrete reason; use personal or organizational context only when the user has supplied it.

Seek risks, opportunities, and simplification together. Removing a feature or retaining the current approach can be a useful discovery. Select perspectives for their connection to the project and their potential to change understanding or a decision, not to fill a domain checklist.

For each newly surfaced direction, explain:

- What in the project or the user's answer makes it relevant.
- The unfamiliar distinction or concrete situation it introduces.
- What judgment could change by exploring it, and what is still uncertain.

Offer the direction for the user to deepen, defer, or leave unexplored. Surface valuable directions even when the initial proposal is already implementable, but let the user choose further depth. Permission to discuss a direction is not agreement with the agent's assessment or permission to implement it.

## 3. Ask an informed round

Within the directions the user has chosen to explore, maintain a decision tree. The **frontier** contains every material unresolved question whose prerequisites are settled. Present the whole current frontier in one numbered round, then wait for the user's answers. A question that depends on an unanswered question belongs to a later round. Before asking how a mechanism works, establish whether the user wants it: when omitting it is a live option, defer questions that assume it exists. Questions waiting on factual investigation also remain outside the ready frontier.

At an unfamiliar question, explain only the knowledge needed to judge it: use a concrete scenario, define necessary terms, and connect the distinction to the user's project. Expand the explanation if the user needs it; progress does not require a quiz or proof of mastery.

For each question, provide a recommendation with its reason and genuinely viable alternatives with their consequences. Include retaining the current approach, deferring, or simplifying when these are real alternatives. Explain what would favor a different choice; do not manufacture alternatives when facts leave only one viable path, or imply a recommendation is established while material evidence is missing.

Keep each round and its alternatives together in the conversation. Honor the user's requested presentation; when they request inline questions, write them in the message rather than splitting them into selection dialogs. A useful per-question structure is:

> **Qn — Decision or perspective**
>
> Project connection, necessary concept, and a concrete question.
>
> **Recommended approach:** What it means, why it fits, and its cost.
>
> **Other approaches:** The viable alternatives, their trade-offs, and when they fit better.

Let the user answer freely or revise the framing. A recommendation, a preselected option, silence, or a request to continue is not a decision. Carry forward explicit answers rather than asking for them again.

## 4. Derive the next questions from the answers

For each material answer, trace the assumptions it relies on, who gains or bears a cost, where it can fail, and the decisions it creates. Explain the connection when proposing a derived question. Use concrete counterexamples to test important judgments; check factual contradictions, and accept a user-owned trade-off once the user understands its consequences.

For example, a choice of permanent sharing links raises a question about what happens when the author deletes their account. That may expose a distinction between a link's lifetime and responsibility for its content. The example illustrates a derivation, not a checklist every project must follow.

Recompute the frontier after the answers. Consequences within a chosen direction can become the next ready questions; a newly discovered direction returns to the invitation in step 2 before deeper questioning. Merge duplicate questions and stop reopening settled choices without materially new evidence or consequences.

Keep deferred directions with their reason and any condition for revisiting them. Reintroduce one only when the user asks or a later answer or fact materially changes its relevance. Explain that change and let the user decide whether to reopen it; otherwise leave it deferred.

## 5. Preserve understanding and close honestly

At useful round boundaries, connect newly introduced perspectives to the decisions they changed or supported. Keeping the original design can be a successful result. Preserve unresolved facts and deferred directions without claiming the user has mastered a topic or that all possible project questions have been exhausted.

Default to a compact record in the conversation containing:

- The new perspectives and why they matter to this project.
- Decisions, reasons, accepted consequences, and how the perspectives informed them.
- Unresolved facts, deferred directions, and their revisit conditions.

When the user requests persistence, follow the project's documentation and tracker conventions. A hypothetical consequence is not a verified defect or an accepted requirement. If domain-modeling is separately active, let it capture resolved vocabulary and qualifying decisions according to its own rules; it is not a dependency of this skill.

Close when the user ends the discussion, or when the chosen directions have no ready questions or useful new directions to offer. Identify blocked or unresolved branches rather than treating them as settled. User-directed deferral or an early finish is valid; retain enough context to resume without forcing another round.

Keep this skill's work to discussion, targeted read-only investigation, and agreed records. Prototype execution, project changes, and external publication require their own user instruction. A selected design alone is not an implementation instruction; an explicit implementation request can transition out of this discussion using the decisions already made.
