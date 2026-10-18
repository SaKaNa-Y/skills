# Repository Evolution History

Use this policy for skill evolution, renames, retirement, history migration and publication. Keep detailed history in `.local/skill-evolution/`, ignored by Git. Publish selected summaries under `docs/skill-evolution/` after reviewing their value and contents. Both locations belong to this checkout; local records are not backed up by ordinary pushes. [ADR 0011](../adr/0011-keep-evolution-history-with-owned-skills.md) explains the decision.

## Record and publish

Save decisions, experiments, pauses, failures, No Change outcomes and exact private recovery inputs in the local archive. Keep per-skill `index.md` and numbered `record.md` entries under `skills/<current-or-last-name>/`; shared discussions belong in `discussions/`. The local root also holds selected `retained/` evidence and `migration/` ledgers. Continue paused work in its existing record, retaining the next action and actual validation limits.

Publish a concise summary when an adopted behavior change, rename, split, merge, retirement or durable maintenance decision helps users or maintainers. Explain the original problem, resulting behavior, important tradeoffs, actual verification and limitations. Use recoverable source commits for adopted code changes. A failed experiment or rejected option merits a public excerpt only when it explains the current design. Screening and every discussion round do not each need a public entry.

Reuse the local record's sequence and topic for its public summary; gaps are expected. Keep raw conversations, host logs, candidate variants, evaluation details, personal configuration, recovery snapshots and full migration inventories local by default. Include a small self-contained fixture publicly only when the conclusion needs it. Sanitization alone does not establish publication value.

Public files must be understandable and checkable in a clean Git checkout, without links or dependencies on ignored material. Local records may refer to public summaries. Public manifest identities and file hashes cover only published material; local inventories account for full retained history. Changing publication scope requires reviewing the actual Git history, not merely adding ignore rules.

## Ownership and lifecycle

Independent histories belong only to skills maintained or formerly maintained here. External skills may appear as context. Rename directories, indexes, current source links and identity metadata together in both applicable locations; preserve historical names inside original evidence. Retired identities keep their last names and successor links. Splits and merges link earlier owners rather than copying their histories. Record shared decisions once.

## Cleanup and validation

Execution environments belong in `.scratch/skill-evolution/`. Migration items awaiting a specific decision belong in `.local/skill-evolution-quarantine/`; completed retention moves to the local archive. Verify minimal evidence and recovery inputs before authorized deletion. File age does not authorize cleanup. Report missing historical evidence without upgrading old claims.

Follow [repository validation](validation.md) for public changes and clean-tree export checks. Use its explicit local-history check for the private archive. Publication scans assist review; they cannot certify privacy or decide deletion. Report local saves, commits and pushes separately. Private records and backup refs must not be included in a push.
