# GitHub Tracker Guidance Template

Use this seed when the user chooses GitHub Issues and usable guidance is missing. Replace the fields with verified project values and include the result in the configuration draft.

```markdown
# Issue Tracker: GitHub

Canonical destination: <owner/repository> GitHub Issues.
Tool: <project-selected GitHub CLI or connector>.

Read existing open and closed issues before proposing a new or updated record. Search related pull requests and compare their current state and coverage with the observed problem; a shared title or component does not establish identity or a completed fix. Use the selected repository explicitly when multiple remotes could resolve differently.

Follow existing issue templates and documented label conventions. A skill that requires approval of exact issue mutations retains that requirement; this configuration grants no publication authority.

Related PRs are reconciliation evidence. They are not an additional issue destination or a request to review, modify, or merge those PRs.
```

Keep the project's existing PR-as-request-surface setting unchanged. Supplemental reconciliation searches do not enable PR triage. Add actual issue-template or label pointers only when they exist and affect a supported consumer; setup does not manufacture a label vocabulary.
