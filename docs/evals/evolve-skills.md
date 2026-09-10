# Evolve Skills Workflow Evaluation

This maintainer-only evaluation exercises the general contract in [Evolve Skills](../../skills/evolve-skills/SKILL.md). The fixtures stay outside the installed skill and introduce no target-specific branches. It checks whether an agent using the new skill makes the intended workflow decisions; it does not establish that an evolved target is behaviorally better in production.

## Fixture and method

The target fixture, `meeting-brief`, has this description and body:

```markdown
description: Turn meeting notes into a concise account of decisions, owners, and next steps.

# Meeting Brief
Read the notes and write decisions, owners, and next steps. Clarify missing information with the user before finalizing. Preserve explicitly stated dates.
```

Its frontmatter also has `name: meeting-brief` and `disable-model-invocation: true`. The use transcript records:

1. The user invokes the skill on notes about a checkout trial with no named owner and a Friday measurement follow-up owned by Priya.
2. A tool entry identifies the target skill read. The transcript does not preserve the returned bytes or a historical revision.
3. The assistant asks for the trial's owner.
4. The user requests `Unassigned` for absent owners, asks to preserve named owners, and wants a useful brief without waiting for ownership information.
5. The assistant follows that adaptation and the user accepts the result.

Independent worker agents received the skill, the relevant raw fixture transcript, and filesystem access confined to the disposable fixture. They did not receive an answer key or the author's diagnosis. The pending case includes a user-selected proposal and validation approach because it exercises resumption after selection. One worker handled the review, unused, and rollback cases sequentially; a second handled pending validation. The cases use separate workspaces, but the reused worker did not have a literal model-context reset between cases.

## Cases and observed results

### Purpose-led proposal and selection checkpoint

The catalog lists `meeting-brief` and a separate `browser-audit` skill. Only the meeting brief has actual use. The latest request asks for review and discussion, without selecting a change.

Observed on 2026-09-10: the worker selected only `meeting-brief`, explained its purpose, and proposed preserving the successful missing-owner adaptation. It offered a default fallback, an urgency-dependent fallback, and keeping the existing method, with trade-offs and validation criteria. It treated the historical version as unknown rather than assuming current wording caused past behavior. It stopped at Proposed / Not Run and wrote only its response. Target bytes were unchanged.

### Catalog mention without use

The transcript only asks what skills are installed, receives their names, and requests evolution.

Observed: the worker reported no eligible target and stopped without a proposal, candidate, history, or target edit. Target bytes were unchanged. This verifies the entry boundary rather than the quality of any proposed improvement.

### Selected change with unavailable behavioral validation

The transcript includes explicit selection of a missing-owner fallback and before/after validation on the original notes plus another input with all owners supplied. The user identifies the persistent history location. The fixture has no Git baseline, and fresh independent behavioral runs are unavailable.

Observed: the worker retained the active baseline and created a separate candidate, before/after snapshots, an iteration record, index, and fixed validation plan. The index states Candidate / Pending Validation. The record preserves the purpose, historical evidence, version uncertainty, decision, exact change, missing validation, snapshot mapping, and resumption conditions. It does not claim an unverified adoption or behavioral success.

The author independently checked active-baseline equality, snapshot equality, candidate difference, and separate adoption/validation states. The worker also checked modes, file types, preserved metadata/date behavior in the text, selected-only differences, and history links. These are structural and recovery-material checks, not fresh meeting-brief behavior.

### Requested rollback with a later independent edit

A recorded unverified trial changed the missing-owner instruction. Before/after snapshots preserve its exact states. The active file then gained a separate `Use British spelling.` instruction. The user requests reversal of the recorded iteration while preserving later work.

Acceptance: reverse the original instruction change, retain the later spelling instruction, preserve the original history, and record a linked reconciled reversal. Verify the exact restored-plus-later state rather than restoring the whole old file.

Observed: the worker performed a reconciled reversal, restoring the original clarification sentence and preserving the later spelling instruction. It retained the original snapshots, appended a follow-up to the original record, marked that iteration Rolled Back / Pending Validation, and added a linked reversal record with its own before/after snapshots. The reversal is Applied / Not Run for behavioral validation.

The worker checked the original snapshot digests, exact pre/post states including the later instruction, file type, mode, metadata, and date rule. The author independently confirmed that the final active file equals the original baseline plus the exact later addition, and that both original and reversal histories remain. This is an executed rollback with structural verification, not a behavioral evaluation or a rehearsal of undoing the rollback itself.

## Packaging checks and limits

- Ruby's YAML parser successfully parsed frontmatter and UI metadata. Checks passed for the skill name, nonempty bounded description, explicit-only policy in both files, UI description length, and explicit `$evolve-skills` default prompt.
- Local Markdown references resolve; no unfinished TODO scaffold markers were found. `git diff --check` passed.
- The bundled `quick_validate.py` was attempted with both the system and bundled Python runtimes. Both exited before validation because PyYAML is unavailable. Source inspection additionally found that its allowed-key list excludes the repository's existing `disable-model-invocation` convention. That field was preserved; the validator is not reported as passing.
- These are bounded workflow exercises. They do not cover every history retrieval provider, a verified source/install synchronization, Git-backed recovery, or adoption following a fully executed baseline/candidate behavioral comparison. The snapshot branch and decision boundaries have the concrete evidence described above.

The temporary workspaces for this run were under `/private/tmp/evolve-skills-eval-20260910/`; their contents are disposable. This document preserves the scenarios, observed decisions, and limitations independently of those temporary files.
