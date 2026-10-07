---
name: yak-shaving-triage
description: Guard engineering tasks against yak shaving. Use at the start of implementation, debugging, refactoring, or a developer-tool audit, and when newly discovered problems could divert active work. Explore concrete clues or an explicitly requested scope; preserve independent findings and reconcile them in the background for user-approved recording.
---

# Yak Shaving Triage

Notice broadly. Solve the current problem. Preserve the rest.

Start with the engineering task, whether selected by the model or explicitly invoked by the user. A later invocation joins the current task. Stay active until the **User Problem** is complete or the user stops this skill; explicit revisions of the task update that problem. Ordinary work needs silent checks, not recurring scope reports.

The User Problem is the outcome and boundaries the user currently authorizes. The active task workflow owns its investigation, implementation, and verification. Yak supplies bounded discovery methods and handles independent findings whose repair can be deferred without blocking that outcome. Use [assess-findings](../assess-findings/SKILL.md), installed with `investigate-with-evidence`, for evidence qualification and action recommendations. Reuse an assessment already owned by the active workflow; otherwise the coordinator assigns an Assess worker for a concrete observation with a user outcome at stake. A missing dependency leaves the packet pending while the main task continues.

## 1. Guard the Next Branch

When a clue, observable problem, or contemplated task switch appears, first compare it with the User Problem and assess the evidence already available. Necessary investigation and repair stay with the active workflow, at whatever depth it needs. A potentially independent observation with concrete evidence goes to [issue capture](references/issue-capture.md) for assessment reuse or assignment and recording eligibility; reuse completed evidence without another discovery probe.

For a concrete but unresolved clue outside the necessary investigation, use [discovery lenses](references/discovery-lenses.md) to choose a bounded probe. Read the same reference when the user explicitly requests exploration within the User Problem. A suspicion or stylistic preference alone returns directly to the main task. After a probe, reassess its evidence and route the result through this same scope decision.

**Complete when:** the branch belongs to the main task, is retained with its assessment or pending state, or is excluded with the evidence supporting that judgment. Resume the main task after dismissal.

## 2. Reconcile in the Background

At a boundary after a coherent step, check [search eligibility](references/issue-capture.md#wait-for-search-eligibility) before dispatching a packet with sufficient evidence to compare problem identity to an available subagent using [background reconciliation](references/background-reconciliation.md). Retain packets whose gate or prerequisites remain closed; delegation preserves those boundaries. Continue the User Problem while the worker searches. Reuse a worker or batch related packets where practical; keep independently resolvable problems distinct. If workers are unsupported or no slot is available, retain the evidence with that reason. Recheck availability at the next Capture Checkpoint; use main-agent reconciliation after the main task only if delegation remains unavailable.

Keep task ownership explicit. The coordinator dispatches Assess and reconciliation workers as distinct assignments; neither recursively invokes the other. A search worker supplies tracker evidence, and the existing assessor updates only the judgments that evidence affects. Assess owns the action recommendation and priority assessment; Yak owns record identity, disposition, report ordering and approved publication. For confirmed findings, request suggested priority by default through Assess, reusing its existing judgment and scale when available.

If Tracker Guidance is missing, keep the evidence and defer the destination question to completion. Setup is optional: use existing project guidance directly and let the user initiate configuration separately.

Keep each packet's evidence and search state together: waiting for a gate or prerequisite, assigned to a named worker, or returned with a disposition. For waiting work, retain the reason and resumption condition. At task resumption, a gate opening, or main-task completion, revisit outstanding packets before starting duplicate searches or issuing the final findings report. When search is eligible and a worker is available, dispatch it; a pause does not silently replace delegation with main-agent searching.

**Complete when:** each qualified problem is assigned once to a worker or a retained queue with a reason and next action, and the active task continues without waiting for ordinary reconciliation.

## 3. Close the Main Task and Collect Findings

Report the main task's actual completion, then collect dispatched workers and revisit queued problems under the same eligibility and delegation rules. Workers must return bounded results or explicit search limitations; end an unproductive search as Reconciliation Blocked rather than waiting indefinitely. If the user pauses or stops this skill or the current task, stop dispatching and interrupt this skill’s active searches promptly. Stopping this skill alone leaves the main workflow under its existing authorization. Preserve returned results and unfinished packets with their resumption conditions; do not continue reconciliation merely to finish the queue. A later resume rechecks those conditions without repeating completed searches unless their evidence needs refreshing.

After eligible searches settle and their material evidence has returned to the assessor, present the batch and follow [issue capture](references/issue-capture.md) for exact drafts and Tracker Write Approval. Summarize every disposition using the [outcome reporting contract](references/issue-capture.md#report-the-outcome); Reused records need no mutation draft or approval. Creating or updating an issue or local Markdown record requires the user's approval of the concrete mutation. Keep unapproved drafts in the conversation.

When guidance is absent, present the retained drafts and ask one combined question about the canonical destination, including a precise path for local Markdown. Reconcile there before proposing a write. An inaccessible canonical tracker remains Reconciliation Blocked; provide the evidence without inventing a destination or claiming publication.

**Complete when:** the main task's status is clear, every retained observation has an assessment state and every search-eligible packet has a reconciliation disposition or explicit blocker, every approved write is confirmed or explicitly deferred, and the user can locate all retained or recorded findings.

## Urgent Findings

For credible security, data-loss, or destructive risk, notify the user immediately, stop an action that would realize the risk, and preserve sanitized evidence. Reconciliation still waits for any active independence gate; publication still requires exact write approval. Repair enters the main task only when the user changes its scope.
