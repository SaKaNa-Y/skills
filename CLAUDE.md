# CLAUDE.md

Guidance for Claude Code when working in this repository. Mirrors [`AGENTS.md`](AGENTS.md).

## What this repo is

A personal collection of Claude Code **skills**, one directory per skill under `skills/`, installed into `~/.claude/skills/`.

## Skill format

- Each skill is a directory with a `SKILL.md` (`name` + `description` frontmatter, lean body).
- Detail goes in a `references/` subfolder.
- `description`: `"<capability>. Use when <triggers>."`.

## Skills currently here

`read-project-conventions`, `find-contribution-opportunities`, `assess-contribution-feasibility`, `score-merge-likelihood`, `report-contribution-candidates` — five read-only skills that compose into a contribution-scouting workflow, each also usable on its own.
