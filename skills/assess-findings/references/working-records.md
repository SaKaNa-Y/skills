# Working Records

Read this before capturing, assessing, implementing or reconciling persistent findings and opportunities. These records preserve working evidence and decisions; formal tracker publication follows the project's separate tracker rules.

## Establish record eligibility

Use Working Records for concrete engineering problems or improvements and their investigation, assessment, implementation and verification. Unconfirmed bugs, performance, usability and documentation problems can qualify before their cause or remedy is known. Identify the affected project and the engineering outcome being tracked before selecting a destination.

General fact-checking, correspondence advice and background research return to the consuming task without creating a Working Record. Mentioning a repository or discovering an unrelated product issue does not change that task's purpose. A skill invocation, configured records directory or save/commit authority establishes neither record eligibility nor a requirement to persist an answer. An explicit request to save other material follows that request's document destination instead of this workflow.

For eligible work, preserve existing authorized records and the consuming workflow's capture requirements. Continue session-only work when no persistent capture is requested or required. Feature exploration keeps its separately configured record destination; an assessment handoff updates that record rather than duplicating it in the engineering findings store. Proceed to destination and authority only when the content qualifies and persistent capture applies.

## Resolve the destination and authority

Read applicable user and project agent instructions and their record-guidance pointers. Resolve each setting from the current explicit instruction, then project guidance, then global defaults. Reuse known values without asking again. Keep personal paths out of reusable skill instructions. Setup can configure these conventions but is not a prerequisite.

Require an exact user-selected records root before persistent capture. If none is known, ask once for the destination while continuing independent work. If it is inaccessible, retain the unsaved packet and report the exact limit; do not invent a replacement or claim it was saved. Creating a missing root requires authorization. Reading guidance need not read historical findings: respect the consuming task's source and history gates, including through indexes and delegated searches.

A configured destination does not by itself authorize every action. Reuse the scope of existing permission for ordinary record saves and substantive updates. Keep save permission, local commit permission and tracker/publication permission distinct. Ask only for missing authority; do not repeat approval for already authorized capture. Follow any narrower project restrictions and preserve unrelated edits. Never infer that Explore-specific commit permission also covers bugs or implementation updates.

## Locate the project and record

Use verified repository identity (including upstream and fork when relevant) or another unambiguous project identifier. A matching folder basename alone is insufficient. Reuse the current layout. For a new project history use:

```text
<records-root>/<project>/
  README.md
  001-<short-name>.md
  002-<short-name>.md
  evidence/
```

When project history is available under the consuming workflow's access gates, list the current project directory and read its README before matching records. Compare record files with index entries to find missing entries, broken links and conflicting statuses. Read related active and archived records when their problem, prior decision or reusable approach matters; refresh remote state for records involved in this task. The README identifies the project and links records with short summaries, separating active entries from a compact archived index.

Match by user problem and acceptance boundary before creating an indexed record. When independent-audit gates prohibit historical matching, preserve a uniquely named provisional capture in an authorized task-owned location without reading old records; defer index registration and identity reconciliation until the gate opens. Report that pending state and retain the evidence before cleanup. Recheck the index immediately before allocating a new identifier; concurrent changes require reconciliation, not overwrite. Keep stable identifiers and paths. Reuse existing numbered files and evidence directories without mandatory migration.

One coordinator owns writes for the current task. Workers return evidence and proposed updates; the coordinator rereads current contents and integrates changes at coherent checkpoints. Detect concurrent edits before saving. A local writer or Work Claim is advisory, not cross-chat locking.

## Keep the minimum useful account

Scale the record to the work; retain these facts when applicable rather than filling unknown fields with guesses:

- Identity, project, kind (observation or opportunity), user scenario, origin and affected revision/environment.
- Original observations, expectation basis, replayable evidence and source/history exposure; separate inference and unknowns.
- Current assessment, rationale, related record IDs and the evidence or uncertainty for each relationship.
- User decisions, selected outcome, scope, preserved behavior, acceptance conditions and unresolved decisions. Link a larger existing spec instead of copying it.
- Implementation owner, execution location/branch, last completed action, active or paused state, next step and relevant resource ownership.
- Delivery links, their provenance, covered acceptance conditions, remaining work and last checked status/date.
- Lifecycle (active or archived), archive reason when relevant, and concise dated material changes.

Save concrete observations before final assessment. A provisional record is not a confirmed defect. Revising a conclusion preserves the decisive earlier evidence and why the judgment changed. Keep related-but-distinct problems separate; one record can link several PRs, and one PR can cover several records.

Preserve essential evidence before disposable cleanup. Prefer a small replayable input, command and result over full logs; retain the version and known limitations. Sanitize secrets and unrelated personal data. A temporary path about to be removed is not durable evidence. Large evidence deletion requires an applicable retention policy or explicit instruction.

## Qualify evidence on entry

At the start or resumption of related work, and before repair, compare the recorded state with the current target and original upstream. Retain the minimal relevant identities: local source commit and material uncommitted changes; actual executable or package resolution, version and necessary content hash; known build provenance; original upstream repository, ref, commit and check time. Artifact hashes identify contents, not their source commit. The same source commit does not establish the same installed artifact.

Resolve the verification target before relying on version-dependent conclusions. For work on a current problem or an upstream repair, use the verified latest upstream in an isolated checkout or worktree for necessary execution when the local source is behind. An explicitly selected revision, release or running instance remains the target; qualify results to that target. Preserve the original checkout and its changes.

When upstream differs or cannot be verified, promptly tell the user what was established, which conclusions are affected and how work will continue, before proceeding with checks that depend on that state. If upstream is unreachable, continue independent work and keep freshness-dependent conclusions pending. Inspect changes relevant to the selected conclusions and reuse unaffected evidence. Reuse a fresh check from this task rather than repeating it per record. At a final checkpoint, recheck the identities on which the result depends and reconcile any changes; a clean working tree alone does not establish an unchanged revision.

Respect source and history gates: permitted identity checks do not open implementation or tracker access. Defer gated comparisons with their resumption condition, or disclose an authorized change of provenance.

Ready when the execution target and upstream verification state are explicit, material differences or uncertainty have been communicated, and each affected conclusion has a supported next action.

## Retain coverage and repair context

Keep a compact project coverage index linked to detailed records: each block's explored depth, version-bound conclusions, unresolved questions and next useful action. Load relevant bodies and evidence on demand. Preserve scenario and acceptance, confirmed or uncertain causal/blocking/masking relationships, rejected explanations, existing implementations and ownership, and verification limits. Similarity alone establishes neither a relationship nor a shared acceptance boundary.

Save at meaningful transitions: reusable coverage, a new observation, changed judgment or relationship, implementation progress, and pause or resource interruption. Retain partial status and recovery conditions. Update related records and the index consistently in one coherent checkpoint; polling and duplicate logs do not constitute substantive progress.

Before cleaning owned temporary files, retain replayable inputs, conditions, decisive outputs and enough material to recover irreplaceable evidence. Hashes and temporary paths cannot replace contents. Rebuildable dependencies, caches and ordinary outputs can be removed after this check. Decide storage for large irreplaceable artifacts explicitly instead of automatically committing them. Apply the existing deletion authority to retained evidence; cleanup covers only task-owned temporary resources.

## Reconcile delivery on access

When resuming a relevant record, recommending new implementation or updating delivery, check known PR links against current remote state when access is permitted. If links are missing, perform a bounded search using verified project identity, issue references, distinctive behavior and known branches/commits or configured author identity. Inspect plausible matches for actual scope. Reuse fresh evidence from the current task instead of repeating searches.

Distinguish our linked implementation from third-party prior work. Authorship alone does not establish that a PR implements this record; a related third-party fix can resolve the behavior without becoming our contribution. Store the link, provenance, draft/open/merged/closed state, check date and coverage. An issue closure, PR merge and verified user outcome are different facts. Report no match only within the checked scope; unavailable access leaves status unknown or last-known, never permanently 'not submitted'.

Completion writeback and ordinary agent-entrypoint guidance reduce missing links; neither guarantees that every unrelated chat updates them. Reconcile on next access. This contract creates no background monitor.

## Archive, reopen or delete

Keep a record active while useful work or a decision remains, including partial fixes. A merged PR supports archiving as resolved only with evidence covering the accepted outcome; existing verification may suffice when it applies to the merged change. Closed-unmerged work is not a fix. A user decision not to proceed or replacement by another record may also support archive, with that distinct reason.

Archive by updating lifecycle and the index while retaining the stable record, outcome, links and necessary evidence. State the final disposition, decision owner and reason in the record's current summary and index. Distinguish a user decision not to proceed from rejection after assessment; insufficient evidence remains pending unless a decision closes it. Mark conflicting earlier recommendations as historical so they cannot be mistaken for the current next action. Reopen when a regression, revert, new evidence or explicit user request changes the conclusion. Deletion is an explicit action under the user's instruction, not a lifecycle value to maintain or a default consequence of merge. Before an authorized deletion, check inbound references and preserve or update needed links without deleting unrelated evidence.

## Save and commit a checkpoint

Before saving, reread the affected records and index and reconcile concurrent edits. Update the current summary, accepted decisions, delivery state and next action together with the README entries. Retain superseded conclusions as dated history so readers can distinguish them from current guidance. A checkpoint is complete when these current accounts agree and affected index links resolve; preserve unrelated records and edits. On failure, retain the exact pending update and return its destination, cause and next action. A successful PR with failed writeback remains a successful PR and a pending record update; do not create another PR to retry delivery.

When applicable guidance explicitly authorizes local commits for this record kind, make one commit per new record and one per substantive update (new evidence, changed decision, scope, assessment or execution/delivery progress). Group wording-only edits into the next substantive update. For a decision or lifecycle change, name the affected record and resulting disposition in the commit subject, and explain the reason in the subject or body. Inspect the worktree and index first; stage only the record's intended changes and required evidence, using hunks for shared index files. Preserve unrelated staged changes; when they cannot be isolated safely, leave the save complete and report the commit pending. Review the staged diff and verify the resulting commit's paths. Amendments, pushes and history rewrites require separate instructions. A save is not a commit; report each actual result.
