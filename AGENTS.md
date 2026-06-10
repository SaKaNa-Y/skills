# AGENTS.md

Guidance for AI coding agents (Codex, Claude, etc.) working in this repository.

## What this repo is

A personal collection of Claude Code **skills**. Each lives in its own directory under `skills/` and is installed into a user's global skills directory (`~/.claude/skills/`).

## Skill format

- One directory per skill, containing a `SKILL.md`.
- `SKILL.md` has `name` + `description` frontmatter and a lean body; push detail into a `references/` subfolder.
- `description` uses the `"<capability>. Use when <triggers>."` pattern so the skill triggers reliably.

## Skills currently here

- `read-project-conventions`
- `find-contribution-opportunities` (+ `references/`)
- `assess-contribution-feasibility`
- `score-merge-likelihood`
- `report-contribution-candidates` (+ `references/`)

These five compose into a read-only contribution-scouting workflow (conventions → discover → feasibility → merge-likelihood → report), but each can also be used on its own.

## When editing

After changing a skill, re-install it globally (see README) so the change takes effect on the next Claude Code start.
