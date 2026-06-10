---
name: assess-contribution-feasibility
description: Judge whether each candidate contribution is actually actionable right now — checking for existing PRs/assignees, scope, reproducibility, blockers, and policy alignment — and emit a feasible/needs-discussion/blocked verdict with an effort estimate and risks. Use after finding contribution candidates, when deciding which PRs are realistic to take on.
---

# Assess Contribution Feasibility

For each candidate from `find-contribution-opportunities`, decide: **could a contributor realistically open this PR today and have it be welcome?** Output a verdict, an effort estimate, and the risks. This stage filters out work that's already taken, out of scope, blocked, or against the project's rules — *before* the merge-likelihood stage spends effort scoring it.

This skill is **read-only**. Never modify, stage, or commit anything.

## Inputs

- The **candidate list** from `find-contribution-opportunities`.
- The **Project Profile** from `read-project-conventions` (for policy/legal gates).

## Checks per candidate

Run these and record what you find:

1. **Already in flight?** Re-confirm no open/linked PR and no assignee (issue timeline, `gh pr list --search`). If taken → `blocked` (reason: in progress).
2. **Scope / blast radius.** How many files/systems does a reasonable fix touch? Bigger = riskier and slower. Estimate effort **S / M / L**:
   - **S** — single file, localized, no design decisions (typo, small bug, doc fix, one test).
   - **M** — a few files, some understanding of the module needed, no public API change.
   - **L** — cross-cutting, public API/behavior change, or needs design discussion.
3. **Reproducibility (bugs).** Can the bug be reproduced from the description, or is there a clear repro? Unreproducible → `needs-discussion`.
4. **Blockers / dependencies.** Upstream dependency, a pending decision, another unmerged PR, missing access/secrets (e.g. CI failures that need maintainer infra). Hard blocker → `blocked`.
5. **Policy alignment.** Cross-check the Project Profile:
   - Feature that requires an RFC/issue-first → `needs-discussion` until that exists.
   - Candidate type listed as a **disqualifier** → `blocked` (reason: against policy).
   - Legal gate (CLA/DCO) — not a blocker, but note it as a risk the contributor must clear.

## Verdicts

- **feasible** — actionable now; a contributor could start and reasonably expect the PR to be considered.
- **needs-discussion** — worth doing but requires a maintainer signal first (RFC, repro confirmation, scope agreement).
- **blocked** — not actionable now (taken, against policy, hard dependency).

## Output

Augment each candidate with:

```
- id: C<n>
  feasibility: <feasible | needs-discussion | blocked>
  effort: <S | M | L>
  reason: <one line — why this verdict>
  risks: <CLA/DCO required, possible breaking change, flaky to verify, large surface, etc.>
```

Keep all candidates in the list (including `blocked`/`needs-discussion`) with their verdict — the report stage decides how to present them. Don't silently drop anything; if you set something aside, say why.

## Rules

- Be honest about effort — over-optimistic S/M/L estimates mislead the user.
- A `needs-discussion` verdict is not a rejection; it's a routing decision (open an issue first).
- Never start the work or modify files to "test" feasibility — reason from reading only.
