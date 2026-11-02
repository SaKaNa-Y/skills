# Skill metadata

Each skill maintained in this repository declares its author and independent date version in the YAML header of `SKILL.md`:

```yaml
metadata:
  author: sakana
  version: "2026.11.02"
```

Keep the version quoted. Use `YYYY.MM.DD` with a real calendar date.
The author identifies the skill's author, not a list of contributors. Preserve applicable source attribution and license information.

## Update rules

Update the affected skill's version to the date the change is applied when its behavior, requirements, or effective guidance changes.
This includes changes to its `SKILL.md`, references, scripts, templates, and other supporting files.
For shared guidance, update each skill whose effective guidance changes.

Keep the version for formatting-only changes, typo corrections, and repository README changes.
Multiple changes on the same date use the same version. Version each skill independently.
Use the user's current date and timezone when available.

The initial metadata baseline is `2026.11.02`. It records the introduction of this policy, not the skills' creation dates.
New skills use their actual introduction date. Do not invent versions for earlier history.

## Scope and verification

The date identifies an update. It does not promise compatibility, create a release, pin an installation, or replace a Git revision.
Use Git revisions and the existing [history policy](evolution-history.md) for exact content and recovery evidence.

When adding or changing a skill, make sure that its header has one `metadata` mapping with the expected author and date string.
Preserve its name, description, invocation policy, and any other metadata unless the task explicitly changes them.
The Markdown link checker does not validate these fields. Review them separately, then run the required [repository checks](validation.md).
