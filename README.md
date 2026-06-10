# my-skills

A personal collection of [Claude Code](https://code.claude.com) skills.

## Skills

| Skill | What it does |
|---|---|
| [`read-project-conventions`](skills/read-project-conventions) | Reads a repo's contribution rules and conventions into a structured Project Profile. |
| [`find-contribution-opportunities`](skills/find-contribution-opportunities) | Scans a repo (issues, codebase, docs/tests, deps/tooling) for candidate contributions, each tagged with a Conventional-Commit type. |
| [`assess-contribution-feasibility`](skills/assess-contribution-feasibility) | Judges each candidate: `feasible` / `needs-discussion` / `blocked`, with effort and risks. |
| [`score-merge-likelihood`](skills/score-merge-likelihood) | Estimates `High` / `Medium` / `Low` merge odds with a rationale. |
| [`report-contribution-candidates`](skills/report-contribution-candidates) | Assembles a ranked, type-grouped report of the candidates. |

More skills will be added over time.

## Install

Symlink (or copy) a skill into your global skills directory so any project can use it:

```bash
# symlink everything (live-syncs with this repo)
for d in skills/*/; do ln -s "$PWD/$d" "$HOME/.claude/skills/$(basename "$d")"; done

# or copy a single skill
cp -r skills/read-project-conventions "$HOME/.claude/skills/"
```

New skills are picked up the next time Claude Code starts. Run `/skills` to confirm they're loaded.

## Conventions

Each skill follows the standard layout: a `SKILL.md` with `name` + `description` frontmatter and a lean body, with any extra detail in a `references/` folder.
