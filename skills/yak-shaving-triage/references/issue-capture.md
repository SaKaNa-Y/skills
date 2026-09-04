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

## Draft a Self-contained Record

Adapt this template to the project's Tracker Guidance:

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

## Reconcile and Request Approval

1. After the Discovered Problem appears, read project-provided tracker instructions before choosing a tool, destination, template, or label. Yak Shaving Triage reads no Tracker Guidance merely because the skill was activated.
2. Search the destination's existing records using the distinctive symptom, affected component, and evidence location. Use open and closed states when the tracker provides them; use the repository record's headings, entries, or index when it does not.
3. When a record already represents the same problem, reuse it. If materially useful evidence is missing, prepare a proposed addition; otherwise link or identify the existing record without mutating it.
4. For every proposed creation or update, prepare the exact destination, action, title, body or patch, and tracker metadata. Apply labels only when Tracker Guidance defines their use.
5. Show the proposals and request Tracker Write Approval. A single checkpoint may batch proposals, but the user must be able to approve any subset.
6. Perform only approved mutations. Skill invocation, urgency, a writable tool, and prior approval for a different batch are not Tracker Write Approval.

If an approved repository-file mutation would change the checkout that an active workflow is still auditing or validating, retain the exact approved patch and apply it only after that workflow finishes its integrity check and cleanup. Request approval again if the proposed patch changes before it is applied.

Read-only search and reuse need no write approval. Creating an issue, adding a comment, editing tracker metadata or state, and changing a repository Markdown record all do. When Tracker Guidance uses GitHub, execute approved writes with the project-prescribed GitHub tool; when it uses a repository record, follow the established file conventions. A user may explicitly select a repository Markdown destination, but do not invent its path or format when repository guidance is absent.

When Tracker Guidance is absent and the user has not established a destination, keep the completed template as the draft. Do not invent or configure a tracker as part of Yak Shaving Triage.

## Notify and Return

For an ordinary problem, report its actual state at the Capture Checkpoint in one concise update:

```text
Recorded <title> as <link or identifier>; continuing <current work>.
```

Use `Recorded` only after the mutation succeeds. Use `Reused` when no mutation was needed. For an approved target-checkout patch that must wait for the active workflow, say `Approved <title>; recording is deferred until <named completion boundary>`. When the user does not approve a proposed write, say that the named draft was retained. After a deferred write succeeds, report its final destination. Continue the current work without implying publication before it happens.

For an urgent problem, lead with the credible risk, say where it was preserved, and state that its repair remains outside the current task. Then return to the User Problem unless the user changes it.
