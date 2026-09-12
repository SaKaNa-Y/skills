---
name: yak-shaving-triage
description: Guard engineering tasks against yak shaving. Use at the start of implementation, debugging, refactoring, or a developer-tool audit, and when newly discovered problems could divert active work. Preserve independent findings and reconcile them in the background for user-approved recording.
---

# Yak Shaving Triage

Notice broadly. Solve the current problem. Preserve the rest.

Start with the engineering task, whether selected by the model or explicitly invoked by the user. A later invocation joins the current task. Stay active until the **User Problem** is complete or the user stops this skill; explicit revisions of the task update that problem. Ordinary work needs silent checks, not recurring scope reports.

The User Problem is the outcome and boundaries the user currently authorizes. The active task workflow owns its investigation, implementation, and verification. Yak handles independently actionable problems that can be deferred without blocking that outcome.

## 1. Guard the Next Branch

When an observable problem appears or the next action would switch work, compare it with the User Problem. Necessary investigation and repair stay with the active workflow, at whatever depth it needs. For a potentially independent problem, read [issue capture](references/issue-capture.md) to qualify it and preserve evidence already encountered or cheaply reconfirmed. A suspicion or stylistic preference alone returns directly to the main task.

**Complete when:** the branch either belongs to the main task or has enough evidence to be retained as a distinct candidate without pursuing its diagnosis or repair.

## 2. Reconcile in the Background

At a boundary after a coherent step, hand an Issue-ready Problem to an available subagent using [background reconciliation](references/background-reconciliation.md). Continue the User Problem while the worker searches. Reuse a worker or batch related packets where practical; keep independently resolvable problems distinct. If workers are unsupported or no slot is available, queue the evidence for main-agent reconciliation after the main task completes.

Keep co-active skills independent: each owns its own work. A search worker performs this skill's bounded reconciliation; it does not activate or manage other skills.

When an active audit keeps tracker history closed, retain its Finding Packets and dispatch only after its independence gate opens. For Just Use It, this means accounting for the source-confirmed public surface and freezing independent findings, or explicitly freezing a Partial Audit. Once target tracker history is read, further audit work and resumes are tracker-informed. A subagent does not bypass this gate.

If Tracker Guidance is missing, keep the evidence and defer the destination question to completion. Setup is optional: use existing project guidance directly and let the user initiate configuration separately.

**Complete when:** each qualified problem is assigned once to a worker or a retained queue, and the active task continues without waiting for ordinary reconciliation.

## 3. Close the Main Task and Collect Findings

Report the main task's actual completion, then collect dispatched workers and reconcile any queued problems. Workers must return bounded results or explicit search limitations; end an unproductive search as Reconciliation Blocked rather than waiting indefinitely. If the user stops work early, preserve completed and pending findings honestly and honor the stop.

After all eligible searches settle, present the batch and follow [issue capture](references/issue-capture.md) for exact drafts and Tracker Write Approval. Reused records need only a title and link or identifier. Creating or updating an issue or local Markdown record requires the user's approval of the concrete mutation. Keep unapproved drafts in the conversation.

When guidance is absent, present the retained drafts and ask one combined question about the canonical destination, including a precise path for local Markdown. Reconcile there before proposing a write. An inaccessible canonical tracker remains Reconciliation Blocked; provide the evidence without inventing a destination or claiming publication.

**Complete when:** the main task's status is clear, every retained problem has a disposition or explicit blocker, every approved write is confirmed or explicitly deferred, and the user can locate all retained or recorded findings.

## Urgent Findings

For credible security, data-loss, or destructive risk, notify the user immediately, stop an action that would realize the risk, and preserve sanitized evidence. Reconciliation still waits for any active independence gate; publication still requires exact write approval. Repair enters the main task only when the user changes its scope.
