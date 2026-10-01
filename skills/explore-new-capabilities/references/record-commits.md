# Record Commits

Use this reference when the user or applicable instructions authorize local commits for exploration records. Resolve the Git root from the records directory before staging; it may differ from the project being explored. If it is not a Git repository, preserve the files and report the unmet prerequisite. Repository initialization needs its own authorization.

## One opportunity per commit

Save the first presentation of each new opportunity, its index entry, and its supporting evidence in one local commit. Append another commit when that opportunity gains substantive evidence, a changed conclusion, a material scope decision, or a finalized proposal. Group ordinary wording edits into the current update. Continuing or skipping an unchanged record needs no new commit.

Before committing, inspect the worktree, index, and applicable repository instructions. Review the exact changes belonging to this opportunity, including its index update and necessary evidence. Stage only those changes, using hunks when a shared file also contains unrelated work. If existing staged changes cannot be isolated without disturbing someone else's work, keep the record saved and report why its commit remains pending. Do not include unrelated staged files or silently unstage them.

Check the staged diff for unintended content and whitespace errors, then commit with the repository's message conventions. Verify the resulting commit contains only this opportunity's intended update. Preserve prior commits; amendments, history rewrites, and pushes require separate instructions. A rejected or blocked commit remains a saved record with a pending commit, not a completed checkpoint. Report the specific failure and resolve it before presenting another idea.
