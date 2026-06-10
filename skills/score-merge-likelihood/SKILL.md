---
name: score-merge-likelihood
description: Estimate how likely a maintainer would be to merge each candidate PR — High/Medium/Low — from repo activity, maintainer responsiveness, label signals, contribution-guide alignment, and change size, with an explicit dominant-factor rationale. Use after assessing feasibility, to prioritize which contributions are worth the effort.
---

# Score Merge Likelihood

For each candidate, estimate the probability that maintainers would **accept and merge** the resulting PR. This is a judgement call — so always state the *dominant factor* behind each score, letting the user override your reasoning. This is an estimate, not a guarantee.

This skill is **read-only**. Never modify, stage, or commit anything.

## Inputs

- Candidates with feasibility verdicts (`assess-contribution-feasibility`).
- The **Project Profile** (`read-project-conventions`).

Score `feasible` and `needs-discussion` candidates. You may skip `blocked` ones (note them as N/A).

## Signals to gather (read-only, `gh`-first / REST fallback)

1. **Repo & maintainer activity** — is the project alive and responsive?
   ```bash
   gh repo view {owner}/{repo} --json pushedAt,stargazerCount,isArchived
   gh pr list --repo {owner}/{repo} --state merged --limit 20 --json number,createdAt,mergedAt,additions
   gh issue list --repo {owner}/{repo} --state all --limit 20 --json createdAt,closedAt,comments
   ```
   Look at recent commit cadence, time-to-first-response, and PR merge throughput. Archived/stale (no commits in many months) → strong negative.
2. **Acceptance rate of similar work** — among recent merged PRs, do same-type/size PRs land? A history of merged small fixes/docs → positive for those types.
3. **Label / maintainer signals** — issue labeled `good-first-issue`, `help-wanted`, `accepted`, or a maintainer comment asking for the change → strong positive. Maintainer hesitation or "won't fix"/"by design" → negative.
4. **Contribution-guide alignment** — does the candidate match the documented process (linked issue exists, follows commit convention, isn't a disqualified type)? Misalignment → negative.
5. **Change size** — smaller, self-contained changes merge more readily than large/cross-cutting ones (reuse the feasibility S/M/L). S → positive, L → negative.

## Scoring

Weigh the signals into one of:

- **High** — maintainer-requested or labeled-accepting, active responsive repo, small and policy-aligned. Low friction to merge.
- **Medium** — sensible change, active repo, but no explicit maintainer signal, or moderate size, or needs an issue first.
- **Low** — stale/archived repo, unresponsive maintainers, large/contentious change, disqualified type, or against stated direction.

Don't average mechanically — a single dominant factor (archived repo; maintainer already asked for it) can pin the score regardless of the others. Name that factor.

## Output

Augment each candidate:

```
- id: C<n>
  merge_likelihood: <High | Medium | Low | N/A>
  dominant_factor: <the single biggest driver of this score>
  rationale: <1-2 lines citing the concrete signals you saw>
```

## Rules

- **Cite evidence**, not vibes — "maintainer responded to last 5 PRs within a day" beats "seems active".
- Be willing to score **Low** honestly; a polished report full of false High scores wastes the user's time.
- Distinguish *merge-worthiness* (this skill) from *doability* (feasibility) — a feasible PR in a dead repo is still Low.
