---
name: setup-sakana-skills
description: Configure a project's shared conventions for Sakana's skills, including its issue tracker and Claude Code or Codex instruction entrypoints.
disable-model-invocation: true
---

# Setup Sakana Skills

Prepare project conventions that installed skills can read directly. Run only when the user invokes this skill. Reuse existing choices and configure only requirements of installed skills from this collection; the initial configuration surface is issue tracking and agent-document entrypoints. Future requirements belong here when a supported skill actually needs them.

Setup owns configuration, not runtime skill selection. Each skill retains its invocation policy, task responsibility, and approval boundaries. A skill can use sufficient existing guidance without setup having run.

## 1. Inspect the Project

Read existing `AGENTS.md`, `CLAUDE.md`, their configuration pointers, and `docs/agents/` when present. Inspect repository identity and the installed skills' actual requirements. Look for established issue directories and conventions; distinguish issue records from evaluation fixtures, evolution history, and planning notes.

Treat existing issue-tracker and domain conventions as the starting point. Identify duplicate pointers, conflicting choices, and symlinked or shared entrypoint files before editing. An unavailable skill needs no speculative configuration. If an inherited pointer already provides the needed convention, reuse it instead of copying its contents into another file.

**Complete when:** the existing conventions, supported consumers, missing requirements, and conflicting settings are known from the project rather than guessed.

## 2. Resolve Missing Choices

Carry forward choices the user has already made. Ask only unresolved decisions:

- **Agent entrypoints:** Claude Code (`CLAUDE.md`), Codex (`AGENTS.md`), or both. Existing files suggest usage but do not override the user's selected clients.
- **Canonical issue tracker:** GitHub Issues or local Markdown. Recommend an established tracker first; when none exists and a GitHub repository is verified, propose GitHub. Otherwise offer local Markdown. Preserve an existing other tracker and its usable guidance; ask for its conventions only when incomplete.
- **Destination details:** confirm the exact GitHub repository or local directory, available tool, and existing record/status conventions. For a new local tracker, propose `.scratch/issues/` with one Markdown file per problem and explicit status, then let the user choose. Record any verified associated GitHub repository as a supplemental read-only issue/PR search source.

One destination is canonical. Switching it changes future guidance; migrating, copying, or deleting existing issues is separate work. For local records, distinguish whether the chosen directory is shared in Git or private, preserve existing policy, and include any needed narrow ignore rule in the reviewable draft.

**Complete when:** each required choice has an existing or user-selected value and every proposed destination is exact. Missing access can be recorded without claiming a successful connection.

## 3. Show the Configuration Draft

Read the selected [GitHub template](references/issue-tracker-github.md) or [local Markdown template](references/issue-tracker-local.md) when creating missing tracker guidance. Adapt it to the project; preserve established guidance at its existing path when it already serves the consumers.

Show the exact proposed changes to shared guidance, selected agent entrypoints, and any selected ignore rule. Usually the shared file is `docs/agents/issue-tracker.md`; each selected entrypoint contains only a summary and pointer under its existing `## Agent skills` block:

```markdown
### Issue tracker

Issues are tracked in <selected destination>. Read <guidance path> before searching or writing issue records.
```

Keep unrelated instructions and existing domain/label sections. For both clients, point both entrypoints at the same authoritative guidance. Account for symlinks so one underlying file is edited once. Add only missing sections or update their existing content in place. Do not copy skill bodies or add runtime routing rules.

**Complete when:** the user has approved the concrete configuration changes. An explicit approval already covering the same draft remains valid; unchanged configuration needs no write.

## 4. Apply and Verify

Apply the approved changes and check that pointers resolve from each selected entrypoint, the canonical destination is consistent, and existing unrelated content survives. Creating guidance does not create issue records, publish issues, or migrate a tracker. Create a destination directory only when the approved setup includes it.

Re-read the resulting files as a second setup pass: an unchanged project should require no further edits. If a later installed skill adds a real configuration requirement, a user-requested rerun can propose that addition without resetting prior choices.

**Complete when:** the approved files exist, references resolve, the second pass finds no duplicate or required rewrite, and the user receives the changed-file list, affected consumers, and any unverified access limits.
