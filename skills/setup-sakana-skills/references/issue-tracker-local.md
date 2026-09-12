# Local Markdown Tracker Guidance Template

Use this seed when the user chooses local Markdown and usable guidance is missing. Replace the fields with the selected directory and existing conventions. For a new tracker, propose the minimal record structure below in the draft.

```markdown
# Issue Tracker: Local Markdown

Canonical destination: <repository-relative directory>.
Visibility: <shared in Git or private under the selected ignore rule>.
Record layout: <existing convention, or one uniquely named Markdown file per independently resolvable problem>.

Search the whole configured tracker, including closed and archived records, before proposing a write. Compare evidence and acceptance boundaries, not only filenames or titles. Follow links to canonical duplicates; retain a closed record's resolution when deciding whether new evidence belongs in it.

Each new record carries a title, explicit status, observed behavior, impact, reproduction or evidence, expected behavior, known uncertainty, and acceptance criteria. A known root cause is optional. Reuse the project's status vocabulary; for a new tracker use open and closed, with the resolution recorded in the body.

Associated GitHub repository: <verified owner/repository, or none configured>.
When configured and accessible, search its related issues and PRs as supplemental evidence. Capture useful links and coverage differences in the local draft. A remote match does not replace the canonical local search or authorize a remote write. Report unavailable supplemental search without claiming that no related work exists.

Present the exact path and proposed contents before creating or updating a record when the active skill requires write approval. Tracker selection is not approval of future writes. Keep unapproved drafts in the conversation; evaluation fixtures and skill-evolution history are not issue destinations.
```

A selected private directory needs a narrow ignore rule if it is not already ignored. Check whether files are tracked: adding an ignore rule does not untrack or erase them. Include any visibility conflict in the setup discussion rather than silently changing tracked history.
