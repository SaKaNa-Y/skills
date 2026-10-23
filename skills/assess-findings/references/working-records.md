# Working Records

Read this before capturing, assessing, implementing or reconciling persistent findings, opportunities or usage coverage. These records preserve working evidence and decisions; formal tracker publication follows the project's separate tracker rules.

## Establish record eligibility

Use Working Records for concrete engineering problems or improvements and their investigation, assessment, implementation and verification. Unconfirmed bugs, performance, usability and documentation problems can qualify before their cause or remedy is known. Reusable engineering usage and verification evidence also qualifies when the consuming workflow requires it, including successful audits without findings and partial or blocked attempts. Identify the affected project and the engineering outcome being tracked before selecting a destination.

General fact-checking, correspondence advice and background research return to the consuming task without creating a Working Record. Mentioning a repository or discovering an unrelated product issue does not change that task's purpose. A skill invocation, configured records directory or save/commit authority establishes neither record eligibility nor a requirement to persist an answer. An explicit request to save other material follows that request's document destination instead of this workflow.

For eligible work, preserve existing authorized records and the consuming workflow's capture requirements. Continue session-only work when no persistent capture is requested or required. Discovery, exploration, assessment and implementation can share one configured records root. A workflow change updates the current primary record rather than creating another copy. Honor explicit separate destinations; when relevant history spans them, reconcile the same identity across those locations before capturing another record. Proceed to destination and authority only when the content qualifies and persistent capture applies.

## Resolve the destination and authority

Read applicable user and project agent instructions and their record-guidance pointers. Resolve each setting from the current explicit instruction, then project guidance, then global defaults. Reuse known values without asking again. Keep personal paths out of reusable skill instructions. Setup can configure these conventions but is not a prerequisite.

Require an exact user-selected records root before persistent capture. If none is known, ask once for the destination while continuing independent work. If it is inaccessible, retain the unsaved packet and report the exact limit; do not invent a replacement or claim it was saved. Creating a missing root requires authorization. Reading guidance need not read historical findings: respect the consuming task's source and history gates, including through indexes and delegated searches.

A configured destination does not by itself authorize every action. Reuse the scope of existing permission for ordinary record saves and substantive updates. Keep save permission, local commit permission and tracker/publication permission distinct. Ask only for missing authority; do not repeat approval for already authorized capture. Follow any narrower project restrictions and preserve unrelated edits. Never infer that Explore-specific commit permission also covers bugs or implementation updates.

## Locate the project and record

Use verified repository identity (including upstream and fork when relevant) or another unambiguous project identifier. A matching folder basename alone is insufficient. Different target repositories have separate project directories; branches and worktrees of one target retain that project identity, while independently targeted forks retain their own identity. Reuse the current layout. For a new project history use:

```text
<records-root>/
  README.md                  # cross-project overview
  <project>/
    README.md                # project overview
    coverage.md              # coverage navigation when usage is recorded
    001-<short-name>.md
    002-<short-name>.md
    evidence/
```

When project history is available under the consuming workflow's access gates, read the root overview and project README, then list the project directory before matching records. For usage work, also read the project coverage index and relevant linked batch evidence under the same gates; [coverage records](coverage-records.md) defines its content, history and version comparisons. Compare record files with index entries to find missing entries, broken links and conflicting statuses. Read related active and archived records when their problem, prior decision or reusable approach matters; refresh remote state for records involved in this task. The project README identifies the project and links primary records through the classification and overview rules below.

Match by user problem and acceptance boundary before creating an indexed record. When independent-audit gates prohibit historical matching, preserve a uniquely named provisional capture in an authorized task-owned location without reading old records; defer index registration and identity reconciliation until the gate opens. Report that pending state and retain the evidence before cleanup. Recheck the index immediately before allocating a new identifier; concurrent changes require reconciliation, not overwrite. Keep stable identifiers and paths. Reuse existing numbered files and evidence directories without mandatory migration.

Maintain one current primary record and one current navigation entry for each established Problem Identity, across discovery methods and configured stores. It can point to an existing record or a stable section in a multi-finding report; a new file per problem is optional. In the project README, identify its current assessment, handling status and next action; keep detailed evidence dates and supporting observations in the primary record. Keep independent problems distinct even when one repair can address them together. Reuse the primary record through discussion, assessment, implementation and verification. Audit reports can retain unique observations and coverage while linking to the primary record for current decisions. A change of classification or workflow does not require moving or duplicating the record.

When observations match an existing identity, add materially useful evidence or link its existing location. Preserve unique reproduction paths, versions and prior decisions. If duplicate current entries already exist, select the established or better-supported entry as the current destination and leave explicit links from the others. Reconcile conflicting judgments before presenting one current status; unresolved conflicts remain visible. Read relevant cross-project records for shared upstream identities without expanding the requested assessment to unrelated problems. Preserve stable links and existing reports instead of requiring a full migration.

### Classify work and maintain the overviews

Classify each item by the current problem or intended outcome, not by its source skill or original store:

- **Findings** cover concrete problems in existing behavior, including unconfirmed observations, confirmed defects and improvements to existing behavior.
- **Explorations** cover proposed capabilities, workflows or extended uses whose value, scope or design is being considered. They keep their identity when selected work proceeds to implementation.

Classification is separate from assessment confidence, user handling decisions, delivery status and lifecycle. Either category can be pending discussion, deferred, in progress or closed. A new-capability proposal remains an Exploration when Assess reviews it; a defect found by Explore is a Finding. If the understanding changes, update the category and rationale on the same primary record without moving or duplicating its file. Independently resolvable problems retain separate identities.

Keep record files directly under their project, with project evidence in `evidence/`; category headings do not require category directories. Respect explicit project layout overrides.

The root README is the repository directory: its purpose, reading order, and project entries. A project entry contains the project identity, link to its overview, and aggregate counts derived from independently tracked problems and opportunities. Keep the current assessment, evidence limits, repair progress and next action with the individual problem in its primary record and project index. These are item data even when shortened to one sentence inside a project summary.

Additional affected locations, evidence or classification changes do not create another identity. A repair group can contain several independent identities. Reconcile project entries when adding or splitting an identity, then derive the aggregate counts. Explain material count changes in the primary records.

Each project README has Findings and Explorations tables using **Item | Current assessment | Handling status | Next action**. Link each item to its primary record or relevant section of a multi-item report. Put related PR links with handling status, while keeping detailed evidence dates, checks and acceptance conditions in the primary record. Keep closed outcomes in a compact separate table with their type, reason and reopening condition. Deferral alone does not close an item, and a merged PR alone does not establish complete acceptance.

Link the project coverage index from its README. Coverage indexes and batch observations are supporting engineering evidence, not Findings or Explorations and not additions to problem counts. A project may contain coverage without any problems. A Supporting material section lists additional audits, reproductions and drafts with their purpose and related primary records when applicable. Do not repeat the primary-record inventory. An audit can supply evidence for several items and also contain independent findings; index each independent problem at its relevant section without copying the audit.

Write everyday overviews around current use and terminology. Keep repository-reorganization provenance and original-source mappings in retained history rather than introductory prose or source-origin columns. Preserve substantive product scenarios that happen to concern migration. At each substantive checkpoint, reconcile the primary record, affected project entries and root project summary. Preserve an overview unchanged when its current content remains correct. An overview edit does not refresh evidence or reassess unrelated projects. Missing dates and unresolved judgments stay explicit in the primary record.

When consolidating existing stores, preserve stable paths and map old identities to their current primary records. Qualify colliding historical numbers by origin or full path, and allocate unused numbers for new records. Keep original evidence and dated decisions; reconcile competing current judgments before choosing one next action. Follow the user's migration and history authority rather than treating record maintenance as permission to rewrite or delete repositories.

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

### Check handoff quality

Before a capture or assessment handoff, check whether an agent without the originating conversation can understand the user scenario, locate evidence and its version or date, and identify the primary record, current judgment, settled decisions and next action. For a behavior finding, distinguish the trigger, expected behavior and observed result. For an opportunity, distinguish what the closest existing route achieves, the additional desired outcome, and the evidence or uncertainty behind its incremental value.

For continued discussion, preserve selected and rejected alternatives with their reasons, unresolved questions and the next decision or factual check. For implementation, retain the user's selected scope, preserved behavior, acceptance conditions and execution authority, or name the gaps that must be settled first. An unfinished opportunity can be ready for continued discussion without being ready or authorized for implementation. Assessment records also retain priority when assessed, relevant issue/PR coverage, remaining acceptance conditions and the reason for a changed status. Link supporting artifacts instead of duplicating them. For provisional capture, identify missing facts and the check that would resolve them; do not invent a diagnosis or require completed assessment before saving. A status label alone is not a usable handoff.

Preserve essential evidence before disposable cleanup. Prefer a small replayable input, command and result over full logs; retain the version and known limitations. Sanitize secrets and unrelated personal data. A temporary path about to be removed is not durable evidence. Large evidence deletion requires an applicable retention policy or explicit instruction.

## Qualify evidence on entry

At the start or resumption of related work, and before repair, compare the recorded state with the current target and original upstream. Retain the minimal relevant identities: local source commit and material uncommitted changes; actual executable or package resolution, version and necessary content hash; known build provenance; original upstream repository, ref, commit and check time. Artifact hashes identify contents, not their source commit. The same source commit does not establish the same installed artifact.

Resolve the verification target before relying on version-dependent conclusions. For work on a current problem or an upstream repair, use the verified latest upstream in an isolated checkout or worktree for necessary execution when the local source is behind. An explicitly selected revision, release or running instance remains the target; qualify results to that target. Preserve the original checkout and its changes.

When upstream differs or cannot be verified, promptly tell the user what was established, which conclusions are affected and how work will continue, before proceeding with checks that depend on that state. If upstream is unreachable, continue independent work and keep freshness-dependent conclusions pending. Inspect changes relevant to the selected conclusions and reuse unaffected evidence. Reuse a fresh check from this task rather than repeating it per record. At a final checkpoint, recheck the identities on which the result depends and reconcile any changes; a clean working tree alone does not establish an unchanged revision.

Respect source and history gates: permitted identity checks do not open implementation or tracker access. Defer gated comparisons with their resumption condition, or disclose an authorized change of provenance.

Ready when the execution target and upstream verification state are explicit, material differences or uncertainty have been communicated, and each affected conclusion has a supported next action.

## Reassess a records folder

Use this procedure when the user selects a folder or collection for joint reassessment, whether work continues in the same conversation or a new one. The selected path bounds the records to assess; it does not identify their product upstream or authorize product repair.

1. Inventory the selected records and README entries, including relevant archived items. Build the [assessment worklist](../SKILL.md#1-establish-the-assessment-and-its-owner) from the in-scope original questions and existing identities before planning checks. Follow related evidence and duplicate links outside the folder when needed, while leaving unrelated records outside scope. Respect active history gates; name any entries awaiting permission or access.
2. Resolve the product and original upstream for each problem. Apply [evidence qualification](#qualify-evidence-on-entry) and [delivery reconciliation](#reconcile-delivery-on-access). Share fresh version checks and searches across related entries. Use current upstream by default for current-status questions, preserving an explicitly selected release or revision. Identify which prior evidence still applies to the selected target and carry remaining gaps into the worklist.
3. Pass the applicable evidence and remaining gaps through [evidence intake and judgment](../SKILL.md#3-judge-the-findings-basis), which selects and runs the next authorized check. Return each result to its original question before choosing the next action. Record whether the reported behavior still applies, is partly resolved, is resolved within its acceptance boundary, or remains unverified, with target version, date and evidence limits. Keep that result separate from classification, priority, issue/PR state and record lifecycle. An inaccessible upstream leaves freshness pending; issue closure or PR merge alone does not establish resolution.
4. Reconcile identities and relationships using the observed scenarios and acceptance boundaries. Several observations can support one problem. Several independent problems can share a repair group while retaining separate acceptance checks. Preserve rejected matches and uncertain relationships when they affect the next action. Recommend the responsible repository and a scoped next action without creating duplicate repair work.
5. Complete the [save checkpoint](#save-and-commit-a-checkpoint): update current summaries, identity links, status reasons, delivery coverage, remaining work and affected root/project overview entries together. Report every in-scope problem's outcome or exact unresolved dependency, plus the actual save and commit results. Preserve unrelated edits and other folders' independent findings.

Discovery and assessment can finish while repair remains pending. The user can select implementation immediately or later; neither a new conversation nor a waiting period is required. This procedure adds no automatic product changes or tracker publication.

## Retain coverage and repair context

Use the [coverage record contract](coverage-records.md) for the compact project index, batch observations, execution identities and version applicability. The consuming usage workflow owns this persistence even without a separate triage workflow. Load relevant bodies and evidence on demand. Preserve scenario and acceptance, confirmed or uncertain causal/blocking/masking relationships, rejected explanations, existing implementations and ownership, and verification limits. Similarity alone establishes neither a relationship nor a shared acceptance boundary.

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

Use this checkpoint for new captures, reusable usage coverage, changed assessments and implementation or delivery updates. For coverage-only checkpoints, batch observations and the coverage index are the substantive accounts; no problem record is required. One coordinator owns shared writes. While an independent history gate is closed, save a unique provisional batch and evidence without reading or merging result-bearing indexes; defer the index/navigation steps until the gate opens and report them as gate-pending. Complete these dependent operations in order; primary records can be saved as a batch.

1. Reread the affected primary records and indexes, reconcile concurrent edits, and identify the intended changes. Before the first write, retain a file inventory and the existing contents needed to distinguish this checkpoint from pre-existing changes, including untracked files. Proceed to saving when that baseline covers the affected records, indexes and evidence locations. Save the affected primary accounts or version-bound batch observations with their actual results, relevant decisions, next action and linked evidence. Keep superseded conclusions as dated history. Link supporting audit accounts to the current primary record while retaining their dated evidence. Preserve unrelated records and edits.
2. Read the saved primary results or batch observations to update the affected project entries and coverage index under the [overview rules](#classify-work-and-maintain-the-overviews) and [coverage merge rules](coverage-records.md#merge-without-losing-history). Derive counts from problem identities. Compare the resulting project directory data—identity, overview link and aggregate counts—with the root entry, and apply that difference. Preserve still-correct purpose and reading guidance. Reconcile inherited item narratives into their primary accounts and project entries while restoring the root to directory data. An unchanged directory entry needs no rewritten assessment summary.
3. Compare pre-save and post-save file inventories to enumerate this checkpoint's new files and changes to existing files. Use the retained baseline to separate them from unrelated edits. Split large content and diffs into bounded inspection ranges. Proceed when every affected file has an inspection target, including new evidence and changed root or project overviews.
4. Inspect the saved content and diff for those targets. Check recorded execution artifacts against their inputs and results. For coverage, verify actual source/artifact identity, per-mode boundaries, historical evidence links and the separate basis of reuse judgments; a newly saved report is not proof of new execution. Match changed root entries to the directory data derived in step 2, and project entries to saved primary results; reconcile identity, assessment, handling, next action and counts. Follow affected index links and apply [handoff quality](#check-handoff-quality) to each changed substantive judgment, tracing its evidence and limits. Existing adequate evidence needs no new execution. Finish this check when every target has been inspected and discrepancies are identified; omitted or truncated ranges remain unchecked.
5. Repair discrepancies and recheck the affected content before reporting the checkpoint complete. State any uninspected portion as unfinished verification and continue when access permits. If saving or repair is blocked, preserve the completed portion and exact pending update, destination, cause and next action. A successful PR with failed writeback remains a successful PR and a pending record update; do not create another PR to retry delivery.

When applicable guidance explicitly authorizes local commits for this record kind, make one commit per new record and one per substantive update (new evidence, changed decision, scope, assessment or execution/delivery progress). Group wording-only edits into the next substantive update. For a decision or lifecycle change, name the affected record and resulting disposition in the commit subject, and explain the reason in the subject or body. Inspect the worktree and index first; stage only the record's intended changes and required evidence, using hunks for shared index files. Preserve unrelated staged changes; when they cannot be isolated safely, leave the save complete and report the commit pending. Review the staged diff and verify the resulting commit's paths. Amendments, pushes and history rewrites require separate instructions. A save is not a commit; report each actual result.
