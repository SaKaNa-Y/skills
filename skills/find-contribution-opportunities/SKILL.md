---
name: find-contribution-opportunities
description: Scan a repository for concrete open-source contribution opportunities (potential PRs) across four sources — open GitHub issues, the codebase itself, docs/tests gaps, and deps/tooling — tagging each with a Conventional-Commit type. Use when the user wants to find PRs to make, find good-first-issues, or discover ways to contribute to a project.
---

# Find Contribution Opportunities

Produce a **raw candidate list**: concrete things that could each become one pull request. Tag every candidate with a Conventional-Commit type and record where the evidence came from. Do **not** judge feasibility or merge odds here — that is the job of `assess-contribution-feasibility` and `score-merge-likelihood`. This skill only discovers and classifies.

This skill is **read-only**. Never modify, stage, or commit anything.

## Prerequisite

Expect a **Project Profile** from `read-project-conventions`. Use its *disqualifiers* to skip candidate types the project won't accept (e.g. don't surface docs-only candidates if docs PRs are discouraged). If no profile was provided, run that skill first.

## The four discovery passes

Run each pass and merge the results. Each is detailed in its own reference file — read the relevant one before running that pass:

| Pass | Reference | Typical types produced |
|---|---|---|
| Open GitHub issues | `references/github-issues.md` | fix, feat, docs, test |
| Codebase scan | `references/codebase-scan.md` | fix, refactor, chore, perf |
| Docs & tests gaps | `references/docs-and-tests.md` | docs, test |
| Deps & tooling | `references/deps-and-tooling.md` | build, ci, chore |

The `gh`-first / REST-API-fallback access pattern (used by several passes) is defined once in `references/github-issues.md`; reuse it.

## Conventional-Commit types

Tag each candidate with one of: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci`, `chore`. Pick the type a maintainer would expect on the resulting PR.

## Output: candidate list

Emit a flat list. Each candidate has exactly these fields:

```
- id: C<n>                      # stable handle for later stages
  type: <conventional-commit type>
  title: <one line, imperative — reads like a PR title>
  source: <issues | codebase | docs-tests | deps-tooling>
  location: <path:line  OR  #<issue-number>  OR  url>
  summary: <1-2 sentences: what's wrong / missing and the rough shape of a fix>
  evidence: <the raw signal — the TODO text, the issue title, the failing check name, etc.>
```

## Rules

- **One PR per candidate.** If something is really five separate fixes, emit five candidates.
- **De-duplicate across passes** — a TODO that's also tracked in an issue is one candidate; prefer the issue as `location` and note the code site in `evidence`.
- **Skip work already in flight** — if an issue is assigned or has a linked open PR, drop it (the issues pass covers how to check).
- **Respect disqualifiers** from the Project Profile.
- Stay descriptive: capture *what* could change, never *write* the change.
- Pass the full candidate list to the next stage; don't truncate silently. If you cap the list, say how many you dropped and why.
