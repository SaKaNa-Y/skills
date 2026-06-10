# Discovery pass: Open GitHub issues

Mine the issue tracker for work the maintainers have already signalled they want. This file also defines the **`gh`-first / REST-fallback access pattern** reused by the other passes and skills.

## Access pattern: `gh` first, REST API fallback

Detect availability once, then reuse:

```bash
gh auth status   # exit 0 → gh is installed and authenticated
```

- **If `gh` is available:** use `gh issue list`, `gh search issues`, `gh pr list`, `gh api ...`.
- **If `gh` is missing or logged out:** fall back to the unauthenticated REST API via `curl` (60 req/hr/IP — enough for a scan). If a `GITHUB_TOKEN`/`GH_TOKEN` env var exists, send it as `Authorization: Bearer $TOKEN` to raise the limit.

```bash
# REST fallback example (open issues, newest first)
curl -fsSL "https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=50&sort=updated"
```

Note `/issues` returns PRs too — skip any item that has a `pull_request` field.

All calls here are **GET / read-only**. Never call mutating endpoints.

## What to look for

Prefer issues the project has flagged as wanted and tractable:

```bash
# Curated, contributor-friendly buckets
gh issue list --repo {owner}/{repo} --state open \
  --label "good first issue" --label "help wanted" --limit 50

# Confirmed bugs and accepted work
gh issue list --repo {owner}/{repo} --state open --label "bug" --limit 50
gh search issues --repo {owner}/{repo} --state open --label "accepted" 

# Unassigned, recently active issues (no one obviously on it)
gh issue list --repo {owner}/{repo} --state open --search "no:assignee sort:updated-desc" --limit 50
```

Label names vary per project — read the **label vocabulary** from the Project Profile and adapt (`good-first-issue`, `E-easy`, `status: accepting prs`, etc.).

## Filter out work already in flight

For each candidate issue, drop it if any of these hold:

- It has an **assignee** (`assignees` field non-empty).
- It has a **linked open PR**. Check the timeline / cross-references:
  ```bash
  gh issue view <n> --repo {owner}/{repo} --json title,assignees,closedByPullRequestsReferences
  # or search for PRs that mention the issue:
  gh pr list --repo {owner}/{repo} --state open --search "<n> in:body" --limit 10
  ```
- It's a **discussion/question** with no actionable change, or is blocked/waiting on maintainer decision.

## Emit candidates

For each surviving issue, produce a candidate:

- `type`: infer from the issue (bug→`fix`, feature request the project welcomes→`feat`, doc gap→`docs`, missing test→`test`).
- `location`: `#<issue-number>`.
- `evidence`: issue title + key labels + a one-line excerpt of the ask.
- `summary`: what the issue wants and the rough shape of a fix.

Respect the Project Profile's **contribution policy** — e.g. if features require an RFC first, tag feature-request issues as `feat` but note the RFC gate in the summary so the feasibility stage can weigh it.
