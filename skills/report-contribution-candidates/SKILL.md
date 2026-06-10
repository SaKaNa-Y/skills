---
name: report-contribution-candidates
description: Assemble the final ranked, type-grouped report of contribution candidates — merging feasibility and merge-likelihood, sorting by best opportunity, and giving each a non-code suggested-approach sketch — ending with an explicit "nothing was changed, the decision is yours" note. Use as the last step of a contribution-scouting workflow to present findings to the user.
---

# Report Contribution Candidates

Turn the enriched candidate list into a clear, scannable report the user can act on. This is the final stage: it **presents**, it does not act. Never propose a diff or write code — only a conceptual sketch of what a fix would involve.

This skill is **read-only**. Never modify, stage, or commit anything.

## Inputs

Candidates carrying: `type`, `title`, `location`, `summary`, `feasibility`, `effort`, `risks`, `merge_likelihood`, `dominant_factor`, `rationale`. Plus the **Project Profile** for the header.

## Ranking

Sort so the best opportunities surface first. Rank by, in order:

1. **Feasibility** — `feasible` above `needs-discussion` above `blocked`.
2. **Merge likelihood** — High → Medium → Low.
3. **Effort** — S → M → L (prefer quick wins among equals).

Then **group by Conventional-Commit type** within the report body so the user can scan by the kind of work they feel like doing.

## Format

Follow `references/report-template.md` exactly. It has three parts:

1. **Header** — target repo, key Project Profile highlights (commit convention, PR requirements, legal gate, disqualifiers), and a count of candidates by type.
2. **Top picks table** — the highest-ranked handful across all types, for an at-a-glance answer to "what should I do first".
3. **Grouped detail** — every candidate under its type heading, each with: title, location/link, feasibility + effort, merge-likelihood + dominant factor, and a **suggested approach** (1-3 sentences, conceptual — what would change and roughly where, never code).

Use a 🟢/🟡/🔴 marker for merge-likelihood (High/Medium/Low) so the table scans fast.

## Mandatory footer

End **every** report with, verbatim in spirit:

> ⚠️ Nothing has been changed. This is a scouting report only — no code was modified, no branch created, no PR opened. Picking what (if anything) to work on is entirely your call. Tell me which candidate you'd like to pursue and I'll hand it back to you / the main session to implement.

## Rules

- **The decision is always the user's.** Never imply work was started or that a candidate "should" be done — present, don't push.
- **Suggested approach ≠ implementation.** Keep it conceptual; if the user wants to build one, that happens outside this read-only workflow.
- Include `blocked`/`needs-discussion` candidates too, clearly marked, so the user sees the full picture and the reasons.
- If a stage capped or dropped candidates, state that in the header so coverage isn't silently overstated.
- Keep it scannable: tables and short lines over long prose.
