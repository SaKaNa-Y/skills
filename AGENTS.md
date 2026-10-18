## Agent skills

### Repository validation

When changing public Markdown, file paths, headings, or the reference checker, follow [repository validation](docs/agents/validation.md) before reporting completion. Check the complete candidate tree, including unchanged reference sources.

### Evolution records

For skill evolution, renames, retirement, and history migration, follow the [repository history policy](docs/agents/evolution-history.md). Detailed history stays local; selected summaries are tracked after publication review. Execution environments and migration quarantine stay ignored.

### Issue tracker

Issues and specs are tracked in GitHub Issues using the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical triage labels without overrides. See `docs/agents/triage-labels.md`.

### Domain docs

This repo uses the single-context layout: root `CONTEXT.md` and `docs/adr/`. See `docs/agents/domain.md`.
