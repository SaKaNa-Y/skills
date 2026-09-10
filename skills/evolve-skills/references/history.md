# History and Recovery

Use this reference when consulting earlier evolution, preparing a candidate, recording an outcome, or carrying out a requested rollback. Records explain what changed and support reversing the specific iteration; they are not a transcript archive.

## Find the history

Prefer `docs/skill-evolution/<skill-name>/` in the verified source repository of the target skill. For a standalone installation without a source repository, establish a persistent history location with the user before candidate preparation. Use an existing agreed location on subsequent runs.

Keep an identity in the index: declared name, source repository and relative skill path, and known separate installation paths. Disambiguate same-named skills from different origins with a stable source-qualified directory name. A rename retains or explicitly links its previous history. If the record directory is shared, identities still distinguish the targets.

Read the index first, then iterations relevant to the current opportunity, changed method, or pending validation. Extend an existing pending iteration when continuing its same hypothesis; create a new linked iteration when a changed hypothesis, later adoption, or new evidence represents a distinct evolution. Preserve old outcomes when appending follow-up evidence or marking an iteration superseded or rolled back.

Use one index and one directory per iteration so its record and recovery material travel together:

```text
docs/skill-evolution/<skill-name>/
  index.md
  <unique-date-and-slug>/
    record.md
    changes.patch                 # when a patch is suitable
    before/                       # snapshot fallback, affected files only
    after/                        # snapshot fallback or retained candidate
```

Create only the material needed for the chosen recovery method. Preserve relative file paths in snapshots. Record additions, deletions, file types, permissions, and any symlink targets relevant to restoring the change. History files themselves stay outside the target's recovery payload. Files outside the skill directory need an explicit path mapping rather than ambiguous flattened filenames.

## Index template

```markdown
# <Skill name> Evolution

Source: <repository and relative skill path, or standalone origin>
Installations: <known separate copies, or none identified>

| Iteration | Date | Purpose of change | Adoption | Validation | Record |
| --- | --- | --- | --- | --- | --- |
| <id> | <date> | <short outcome> | <state> | <state> | [Details](<id>/record.md) |
```

Track adoption and validation separately. Useful adoption states are Proposed, Candidate, Applied, Rejected, No Change, Superseded, and Rolled Back. Validation can be Not Run, Pending Validation, Supported, Unsupported, or Inconclusive. Record the scope and basis of a Supported result; it is not a claim that all future uses improve. An explicitly selected unverified trial is Applied / Pending Validation.

## Iteration record template

Use the following as a substantive record, replacing placeholders with observed facts and omitting inapplicable subfields. Detail should let a maintainer without the conversation understand the change, assess its evidence, and recover the earlier state.

```markdown
# <Iteration id>: <Change intent>

## Identity and state
Date; skill identity; actual edit target; source and installation relationship.
Adoption and validation states; related prior or subsequent iterations.
Historical skill version if known; actual pre-change baseline and candidate identity.

## Purpose and usage evidence
The target's intended outcome and relevant boundaries.
Conversation scope and retrieval limits; references to relevant turns, tools, or artifacts.
The user's task, meaningful actions or adaptations, feedback, and observed result.
Minimal excerpts or reproducing details needed to understand the opportunity.
Separate facts, inference, and unknowns; identify contributions from co-used skills.

## Hypothesis and decision
The opportunity, proposed change, and why it may improve the target's purpose.
Expected behavior, preserved behavior, alternatives, and trade-offs.
The user's selection and scope; deferred or rejected alternatives and reasons.
Links to earlier attempts and the new evidence supporting any revisit.

## Exact changes
Affected paths and before/after behavior; relevant instruction or resource differences.
Links to the exact patch, version references, or snapshots, including added/deleted files.
Actual target files changed; separate candidate-only work and installed-copy updates.

## Validation
Criteria and scenarios; baseline and candidate versions; actual runs and outputs.
Original-scenario comparison and relevant transfer probes.
Structural checks separately; regressions, limitations, and checks not run.
Supported benefit or uncertainty within the tested scope.

## Recovery
Recovery method; baseline identifier; payload locations; path and file-state mapping.
Post-change identity needed to detect later edits.
Specific procedure to reverse only this iteration and verify the restored state.
Whether recovery was exercised, what was checked, and any remaining limitation.

## Follow-up
Pending evidence, conditions for revisiting, and next action.
Append later results and link superseding or rollback iterations without erasing the original.
```

Sanitize excerpts and payloads so records do not copy credentials or unrelated personal material. Keep evidence pointers with enough context to understand their meaning if the original conversation is inaccessible. Sensitive recovery material needs an appropriate private location; its absence must not be described as complete recovery support.

## Preserve the actual baseline before changing it

Git is sufficient only when a recoverable revision contains the exact pre-change states of the affected files. Confirm that relationship for those paths; the presence of `.git` or a clean-looking final diff is insufficient. Record the repository and full revision, precise candidate patch, relevant paths, and post-change identity. Verify that the referenced objects and patch are available. A version label alone is not a recovery payload, and an uncommitted baseline is not represented by `HEAD`.

When the exact baseline is uncommitted, untracked, unavailable in Git, or otherwise not reliably recoverable, preserve before/after snapshots of the affected files, including explicit absence for newly created or deleted files. An exact file digest can identify a state but cannot replace its contents. Record the path mapping and verify the snapshots match the intended states before relying on them.

This workflow does not require a commit. Use Git references already available or the snapshot fallback; commit, push, and installation operations follow the user's actual authorization. Keep unrelated pre-existing edits out of this iteration's delta.

Before adoption, check that the recovery material is present and usable: for a patch, check its applicability against the captured baseline in a disposable copy and compare the result with the candidate; for snapshots, check contents and the creation/deletion mapping. Report these mechanical checks separately from any end-to-end rollback rehearsal.

## Reverse an iteration when requested

Resolve the requested iteration and target from the index, read its exact recovery record, and compare current files with its recorded post-change state. If they match, reverse that iteration's delta or restore its affected-file snapshots. Restore recorded absence only for files created by that iteration. Verify the resulting state against the baseline and run relevant structural checks.

If later edits exist, preserve them and reconcile the inverse change against the current files. Inspect dependencies on later iterations; when intent conflicts or reversal would remove later work, present the specific conflict for a user decision rather than resetting a directory or repository. Whole-file restoration is appropriate only when it preserves the required current work.

Record the actual rollback as a linked follow-up, update the index, and retain the original iteration and payloads. Distinguish an exact restoration from a reconciled reversal that intentionally retains later changes.
