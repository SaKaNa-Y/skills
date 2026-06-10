---
name: read-project-conventions
description: Read a repository's contribution rules and conventions (CONTRIBUTING, CLAUDE.md, AGENTS.md, README, PR templates, CoC, CLA/DCO) and emit a structured Project Profile. Use at the start of any contribution-scouting workflow, or when the user asks "how do I contribute to this project", "what are this repo's PR rules", or before opening a PR somewhere new.
---

# Read Project Conventions

Build a **Project Profile**: a compact, structured summary of how a project accepts contributions. Everything downstream (finding opportunities, judging feasibility, scoring merge likelihood) consumes this profile, so be accurate and quote the source.

This skill is **read-only**. Never modify, stage, or commit anything.

## When to use

- First step of scouting a repo for contribution opportunities.
- Any time you need to know a project's PR/commit/test rules before acting.

## Procedure

### 1. Locate the source documents

Look for these, in priority order. They may live at the repo root, under `.github/`, or under `docs/`. Read the ones that exist; don't fabricate rules for ones that don't.

| Priority | Files |
|---|---|
| Contribution rules | `CONTRIBUTING.md`, `.github/CONTRIBUTING.md`, `docs/contributing*`, `CONTRIBUTING.rst` |
| PR expectations | `.github/PULL_REQUEST_TEMPLATE.md`, `.github/PULL_REQUEST_TEMPLATE/*` |
| Issue expectations | `.github/ISSUE_TEMPLATE/*` |
| Agent guidance | `CLAUDE.md`, `AGENTS.md` (Codex), `.cursorrules`, `.github/copilot-instructions.md` |
| Project overview | `README*`, `docs/` index |
| Conduct & legal | `CODE_OF_CONDUCT.md`, `LICENSE*`, any `CLA`/`DCO` mention (often inside CONTRIBUTING) |
| Dev workflow | `package.json` scripts, `Makefile`, `justfile`, `CONTRIBUTING` "development" section, `.github/workflows/*` |

Use `Glob`/`Read` for local clones. For a remote-only repo, fetch raw files (see `find-contribution-opportunities/references/github-issues.md` for the `gh`-first / REST-fallback pattern) — e.g. `gh api repos/{owner}/{repo}/contents/CONTRIBUTING.md`.

### 2. Extract the profile

Pull out only what's actually stated. Mark anything you infer as *(inferred)* and anything absent as *not specified*.

### 3. Emit the Project Profile

Output exactly this structure:

```
## Project Profile: <owner>/<repo>

- **Stack & package manager:** <languages, framework, npm/pnpm/yarn/cargo/pip/...>
- **Build / test / lint:** <commands to build, run tests, lint, format>
- **Commit convention:** <Conventional Commits? scopes? sign-off (DCO)? squash policy?>
- **PR requirements:** <tests required? changeset? linked issue required? draft-first? PR template fields>
- **Legal gate:** <CLA / DCO / none — and how it's enforced>
- **Contribution policy:** <"open an issue/RFC before features", "no drive-by refactors", labels meaning "accepting PRs", etc.>
- **Label vocabulary:** <good-first-issue, help-wanted, accepted, needs-triage, ... if documented>
- **Maintainer norms:** <review cadence, who merges, response expectations, if stated>
- **Disqualifiers:** <PR types the project explicitly discourages — e.g. "docs-only PRs", "dependency bumps", "style-only changes">
- **Sources read:** <list each file you actually read>
```

## Rules

- **Quote, don't guess.** If CONTRIBUTING says "all PRs must reference an issue", capture that verbatim intent; don't soften or invent.
- **Surface disqualifiers loudly** — they prevent the rest of the pipeline from suggesting work the project won't accept.
- If no contribution docs exist at all, say so explicitly in the profile (this itself is a signal — often lower process, but also less predictable acceptance).
- Hand the completed profile back to the caller; do not proceed to act on it.
