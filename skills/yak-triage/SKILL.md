---
name: yak-triage
description: Preserve confirmed problems discovered during another task as self-contained tracker issues without switching away from the current work. Use only when the user explicitly invokes $yak-triage, either alone or alongside other skills.
---

# Yak Triage

Notice broadly. Solve the current problem. Preserve the rest.

Operate as a co-active discipline. The user's current task and any other active skills own the work needed to resolve the User Problem. Remain dormant during that normal work and become active only when another distinct, observable problem appears.

The **User Problem** is the problem the user currently authorizes this task to resolve, including later explicit revisions. A **Discovered Problem** is another observable problem encountered during that work.

## Boundaries

- Let the active task workflow decide what work is necessary inside the User Problem and how deeply to investigate it.
- Keep each active skill independent. The active task workflow handles the User Problem; Yak Triage handles only Discovered Problems. It never invokes, routes, orders, limits, monitors, or manages another skill. Ask the user when two explicit instructions genuinely cannot both be followed.
- Understand the User Problem from the current conversation without creating a separate problem-anchor artifact or recurring scope report.
- Use tracker entries to preserve future work, then return to the User Problem. Repair a Discovered Problem only after the user explicitly makes it current work.

## Handle a Discovered Problem

Read [references/issue-capture.md](references/issue-capture.md) as soon as another observable problem is discovered. Use it to qualify the problem and preserve only the context a future agent needs.

For an ordinary Discovered Problem:

1. Preserve the evidence already encountered and finish the current coherent step.
2. At the next Capture Checkpoint, read the project's Tracker Guidance.
3. Reconcile the problem with existing tracker items. Reuse a complete existing issue without mutating it; otherwise create an issue or add only materially useful missing evidence when the tracker is available and the write is authorized.
4. Tell the user what was created, updated, or reused, including its title and link or identifier.
5. Resume the User Problem under the existing workflow.

A Capture Checkpoint is the boundary after a coherent step and before starting the next one. It preserves the current line of work while keeping the finding durable.

For an Urgent Discovered Problem with credible security, data-loss, or destructive risk, tell the user immediately and capture Issue-ready context immediately. Publish it immediately when Tracker Guidance and write authorization are available; otherwise retain the draft under the missing-guidance rule. When continuing the current action would itself realize the risk, stop that unsafe action and request direction. Repair the Discovered Problem only after the user explicitly changes the User Problem.

## Missing Tracker Guidance

When the project provides no Tracker Guidance, retain Issue-ready Problems in the conversation state, continue the User Problem, and present the completed drafts together after the current work. Ask one combined question about where they should be recorded. Do not create a tracker or repository file to hold them. If the tracker exists but cannot be written with the available tools or authorization, give the user the complete draft and state that it was not published.

## Completion

Yak Triage is complete for a finding when:

- the current workflow remained focused on the User Problem;
- the Discovered Problem has a reconciled issue, a materially improved existing issue, or an Issue-ready draft;
- the user knows where the problem was preserved; and
- work has returned to the User Problem.
