---
name: yak-shaving-triage
description: Continuously guard the current problem against yak shaving by checking potential task switches and preparing distinct confirmed problems for user-approved tracker recording instead of switching over to solve them. Use only when the user explicitly invokes $yak-shaving-triage, alone or alongside other skills.
disable-model-invocation: true
---

# Yak Shaving Triage

Notice broadly. Solve the current problem. Preserve the rest.

Stay active from explicit invocation through completion of the current User Problem, including any explicit revisions the user makes while work is in progress. Run silently during normal work: do not emit a recurring scope report or separate problem anchor.

Operate as a co-active discipline. The user's current task and any other active skills own the work needed to resolve the User Problem. Yak Shaving Triage guards transitions away from that work; it does not take ownership of the work itself.

The **User Problem** is the problem the user currently authorizes this task to resolve, including later explicit revisions. A **Discovered Problem** is another observable problem encountered during that work.

**Reconcile before recording.** Every qualified Issue-ready Problem must receive a Reconciliation Disposition before any tracker creation or update is proposed. Search the canonical tracker selected by Tracker Guidance, including open and closed records when available; reuse the matching record, propose only a materially useful update or genuinely distinct new record, and retain the draft as `Reconciliation Blocked` when the search cannot be completed. Urgency changes notification timing, not this gate or Tracker Write Approval.

## Check for Drift

Whenever a new problem appears or the next intended action would change the current line of work, check the potential branch before following it:

1. Recall the User Problem from the current conversation without reporting it separately.
2. If the potential branch advances investigation or resolution of the User Problem, leave its necessity, method, and depth to the active task workflow.
3. Otherwise, do not follow the branch. Treat an independently actionable, observable problem as a potential Discovered Problem and handle it below. Return directly to the User Problem when the branch is only a suspicion or stylistic preference.

Repeat this check at every later potential branch for as long as the skill remains active. Visible action begins only when a finding must be preserved or user direction is required.

## Boundaries

- Let the active task workflow decide what work is necessary inside the User Problem and how deeply to investigate it.
- Keep each active skill independent. The active task workflow handles the User Problem; Yak Shaving Triage handles only potential branches and Discovered Problems. It never invokes, routes, orders, limits, monitors, or manages another skill. Ask the user when two explicit instructions genuinely cannot both be followed.
- Understand the User Problem from the current conversation without creating a separate problem-anchor artifact or recurring scope report.
- Preserve Issue-ready Problems, reconcile them at an eligible Capture Checkpoint, request Tracker Write Approval for every proposed mutation, then return to the User Problem. Repair a Discovered Problem only after the user explicitly makes it current work.

An observational workflow may own confirming an Audit Finding while repair of the underlying problem remains outside its User Problem. When `$just-use-it` is separately active, accept its Finding Packets without reading the target tracker until Just Use It opens the Audit Reconciliation Gate by accounting for the source-confirmed public surface and freezing its findings, or by explicitly ending and freezing a Partial Audit. Batch reconciliation after that gate; leave experience, coverage, and confirmation to Just Use It, and treat audit work after tracker history is read, including any later resume, as tracker-informed.

## Evaluate and Handle a Candidate Problem

Read [references/issue-capture.md](references/issue-capture.md) as soon as a newly observed problem may be distinct from the User Problem, before expanding or switching work because of it. Use the reference to decide whether the candidate qualifies and, when it does, preserve only the context a future agent needs.

For a qualified ordinary Discovered Problem:

1. Preserve the evidence already encountered and finish the current coherent step.
2. At the next eligible Capture Checkpoint, read the project's Tracker Guidance and follow the reconciliation, drafting, and Tracker Write Approval procedure in [references/issue-capture.md](references/issue-capture.md). When another active workflow keeps tracker history closed, retain the problem until its independence gate opens.
3. Tell the user each problem's Reconciliation Disposition and identify every Reused or successfully recorded item by title and link or identifier.
4. Resume the User Problem under the existing workflow.

A Capture Checkpoint is the boundary after a coherent step and before starting the next one. It preserves the current line of work while keeping the finding durable.

For an Urgent Discovered Problem with credible security, data-loss, or destructive risk, tell the user immediately, stop an action that would realize the risk, and prepare a sanitized Issue-ready draft. Hold it until every active independence gate opens, then reconcile it before requesting Tracker Write Approval; urgency never implies permission to expose or mutate tracker state. Repair the Discovered Problem only after the user explicitly changes the User Problem.

## Missing Tracker Guidance

When the project provides no Tracker Guidance, assign each Issue-ready Problem `Reconciliation Blocked`, retain it in the conversation state, continue the User Problem, and present the completed drafts together after the current work. Ask one combined question about where they should be recorded. A user may select a repository Markdown record when its exact destination and repository conventions are established. Do not invent a tracker or repository file. If the selected destination cannot be searched or written with the available tools or approval, give the user the complete draft and state that it was not published.

## Completion

Yak Shaving Triage is complete for a finding when:

- the current workflow remained focused on the User Problem;
- the Discovered Problem has exactly one Reconciliation Disposition: Reused, Proposed Update, Proposed New, or Reconciliation Blocked;
- every approved mutation succeeded or remains explicitly deferred, and the user can locate every reused, recorded, or retained problem; and
- work has returned to the User Problem when work remains, or the User Problem has otherwise reached its own completion condition.

After handling a finding, keep the drift check active until the User Problem is complete or the user explicitly stops the skill.
