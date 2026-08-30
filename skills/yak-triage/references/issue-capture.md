# Issue Capture

Use this reference only after another observable problem is discovered while working on the User Problem.

## Qualify the Problem

Record a Discovered Problem when all of the following are true:

- an observable behavior, failure, or violated expectation confirms it;
- it has a practical impact beyond a stylistic preference;
- it can be verified independently from the User Problem; and
- it is distinct from the problem currently being resolved.

Qualification depends on the observed problem, not on whether the current change introduced it. Preserve confirmed pre-existing problems under the same standard.

An unsupported suspicion remains untracked. Resume the User Problem without investigating the suspicion merely to produce an issue.

## Capture Enough Evidence

Use evidence already encountered or a cheap reconfirmation such as one focused test rerun, an existing log, a reproduction step, or an exact code location. Stop when an agent without the originating conversation can understand the problem, locate or reproduce the evidence, and verify a future resolution.

A root cause, implementation plan, or chosen solution is optional. Finding those belongs to the future issue unless the current User Problem independently requires the same investigation.

## Write a Self-contained Issue

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

## Reconcile With the Tracker

1. After the Discovered Problem appears, read project-provided tracker instructions before choosing a tool, destination, template, or label. Yak Triage reads no Tracker Guidance merely because the skill was activated.
2. Search existing open and closed items using the distinctive symptom, affected component, and evidence location.
3. When an issue already represents the same problem, reuse it. Add only missing evidence that materially improves a future agent's ability to understand, reproduce, or verify the problem. When nothing material is missing, link the existing issue without adding a comment.
4. Otherwise create one issue for each independently actionable problem, following the project's structure. Apply labels only when Tracker Guidance defines their use.

When Tracker Guidance is absent, keep the completed template as the draft. Do not invent a tracker or configure one as part of Yak Triage.

## Notify and Return

For an ordinary problem, report the issue at the Capture Checkpoint in one concise update:

```text
Recorded <title> as <link or identifier>; continuing <current work>.
```

For an urgent problem, lead with the credible risk, say where it was preserved, and state that its repair remains outside the current task. Then return to the User Problem unless the user changes it.
