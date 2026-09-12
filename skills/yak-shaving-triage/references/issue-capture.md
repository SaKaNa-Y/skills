# Issue Capture

Use this reference when a newly observed problem may be distinct from the User Problem, before expanding or switching work because of it.

## Qualify the Problem

Record a Discovered Problem when all of the following are true:

- an observable behavior, failure, or violated expectation confirms it;
- it has a practical impact beyond a stylistic preference;
- it can be verified independently from the User Problem; and
- it falls outside the work required to resolve the User Problem and can be deferred without blocking that resolution.

Necessary investigation or repair continues under the active task workflow rather than being deferred.

When an observational workflow such as Just Use It is active, confirming an Audit Finding belongs to that workflow while repairing the underlying problem remains deferable. Accept its completed Finding Packet as evidence; do not repeat the experience or take over diagnosis.

Qualification depends on the observed problem, not on whether the current change introduced it. Preserve confirmed pre-existing problems under the same standard.

An unsupported suspicion remains untracked. Resume the User Problem without investigating the suspicion merely to produce an issue.

## Capture Enough Evidence

Use evidence already encountered or a cheap reconfirmation such as one focused test rerun, an existing log, a reproduction step, or an exact code location. Stop when an agent without the originating conversation can understand the problem, locate or reproduce the evidence, and verify a future resolution.

A root cause, implementation plan, or chosen solution is optional. Finding those belongs to the future issue unless the current User Problem independently requires the same investigation.

## Wait for an Eligible Checkpoint

Hold qualified Issue-ready Problems until a natural Capture Checkpoint. When another active workflow has an independence gate, preserve the evidence without reading Tracker Guidance or target tracker history until that gate opens.

For Just Use It, the Audit Reconciliation Gate opens after the source-confirmed public surface is accounted for and the independently observed findings are frozen. An explicitly concluded Partial Audit also freezes its completed Finding Packets and opens the gate. Receiving a Finding Packet before the gate does not open it; opening the gate alone preserves behavioral blindness, while reading tracker history marks the remaining current audit work and any later resume tracker-informed. Keep the gate open for new packets from tracker-informed work and batch them at later Capture Checkpoints.

## Reconcile Before Proposing a Write

Reconcile every Issue-ready Problem against the canonical tracker before drafting a tracker creation or update:

1. Read project-provided Tracker Guidance to identify the canonical destination, tool, record type, template, and metadata rules. Skill activation and repository hosting do not select a tracker.
2. Confirm that the destination can be searched well enough to rule out an existing record. If guidance is missing, access is unavailable, or search is insufficient, assign `Reconciliation Blocked`, retain the Issue-ready draft, and propose no tracker mutation.
3. Search open and closed records when the tracker provides states. Use multiple evidence-shaped queries: the distinctive symptom or error text, the affected capability or component, and the user outcome or evidence location. Inspect every plausible candidate and stop when another materially different query reveals no unexamined candidate, rather than enumerating unrelated tracker history. When the tracker exposes related implementation work, such as pull requests, inspect its current status and compare its stated or evidenced coverage with the observed reproduction and acceptance boundary. Report what is covered, what remains outside the change, and what is uncertain; touching the same component alone does not establish a matching problem.

   Treat an uncovered case as evidence for reconciliation under Problem Identity; it does not by itself justify a new record or parallel repair. Repair remains governed by the current User Problem and the user's authorization.
4. Apply Problem Identity before relying on titles or suspected causes. Finding Packets represent one problem when one resolution and acceptance boundary would resolve them together; keep them distinct when one could be resolved while another remains. Group packets sharing one identity before choosing a disposition.
5. Inspect the resolution of a matching closed record. Follow its canonical duplicate when it was closed as duplicate; treat a currently reproduced fixed issue as a potential update or reactivation under Tracker Guidance; reuse a declined or won't-fix decision instead of opening a duplicate. Create a distinct identity only when the acceptance boundary differs.
6. Assign exactly one Reconciliation Disposition:
   - `Reused` when an existing record already captures the problem; return its title, identifier, and link without mutation.
   - `Proposed Update` when a matching record lacks materially useful reproduction, scope, impact, or acceptance evidence supplied by the current packet.
   - `Proposed New` only when completed search finds no matching Problem Identity.
   - `Reconciliation Blocked` when the canonical tracker cannot be identified or searched sufficiently.

**Complete when:** every qualified problem has one disposition, every Reused result identifies its canonical record, and no Proposed Update or Proposed New exists without a completed search.

## Draft Only the Necessary Mutation

For `Proposed Update`, prepare only the missing evidence and any exact status action allowed by Tracker Guidance. For `Proposed New`, adapt this template to the destination. A `Reconciliation Blocked` problem may retain the same information as an internal Issue-ready draft, but it is not a creation proposal.

```markdown
# [Outcome-oriented title]

## Observed problem

[What happened, under which conditions.]

## Impact

[Who or what is affected and why the problem matters.]

## Evidence

- [Reproduction steps, failing test, log, request/response, or exact location.]
- [Any cheaply confirmed supporting observation.]

## Expected behavior

[The behavior that should replace the observed problem.]

## Scope and known unknowns

[Known affected area and material facts not yet established.]

## Acceptance criteria

- [Observable condition proving the problem is resolved.]
- [Regression coverage or preservation condition when relevant.]

## Deferred from current work

[Why this is a distinct problem rather than the one currently being resolved.]
```

Keep the issue factual. Mark uncertainty explicitly instead of guessing a cause or solution.

## Request Approval and Write

Present the batch as `Reused`, `Proposed Update`, `Proposed New`, or `Reconciliation Blocked`. Reused results need no approval; include their title, identifier, and link. For every Proposed Update or Proposed New, show the exact destination, action, title, body or patch, and tracker metadata, then request Tracker Write Approval so the user can approve any subset. Apply labels only when Tracker Guidance defines their use.

Perform only approved mutations. Skill invocation, urgency, a writable tool, and prior approval for a different batch are not Tracker Write Approval. Read-only search and reuse need no write approval; creating an issue, adding a comment, reactivating or closing a record, editing tracker metadata or state, and changing a repository Markdown record all do.

If an approved repository-file mutation would change the checkout that an active workflow is still auditing or validating, retain the exact approved patch and apply it only after that workflow finishes its integrity check and cleanup. Request approval again if the proposed patch changes before it is applied.

When Tracker Guidance uses GitHub, execute approved writes with the project-prescribed GitHub tool; when it uses a repository record, follow the established file conventions. A user may explicitly select a repository Markdown destination, but do not invent its path or format when repository guidance is absent.

When Tracker Guidance is absent and the user has not established a destination, keep the completed template as a Reconciliation Blocked draft. Present blocked drafts together after the current work and ask one combined question about where they should be recorded. Do not invent or configure a tracker as part of Yak Shaving Triage.

## Notify and Return

For ordinary problems, report the batch's actual dispositions at the Capture Checkpoint. Use a concise result such as:

```text
Reused <title> as <link or identifier>; recorded <title> as <link or identifier>; continuing <current work>.
```

Use `Recorded` only after the mutation succeeds and `Reused` only with the canonical record's title and link or identifier. Name Reconciliation Blocked drafts and their search limitation. For an approved target-checkout patch that must wait for the active workflow, say `Approved <title>; recording is deferred until <named completion boundary>`. When the user does not approve a proposed write, say that the named draft was retained. After a deferred write succeeds, report its final destination. Continue the current work without implying publication before it happens.

For an urgent problem, lead with the credible risk, say where it was preserved, and state that its repair remains outside the current task. Then return to the User Problem unless the user changes it.
