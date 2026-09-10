# Preserve Skill Evolution History and Reversal Evidence

Skill evolution needs a durable history that lets later readers understand and reverse individual changes, including when several skills share a repository. Each skill will have its own history directory, with an index of iterations and a separate detailed record for each iteration. This keeps one skill's progression discoverable without forcing its entire history into a growing document or scattering it across session reports.

An iteration record explains the skill's purpose, the usage evidence behind an evolution opportunity, the proposed improvement and its rationale, the actual changes, and the observed validation results. Proposed, applied, and validated changes remain distinguishable: applying an edit does not establish that it improved use. Records preserve the information needed to reverse the specific changes they describe.

Reversal evidence depends on the available baseline. When a reliable, recoverable Git baseline exists, retain the relevant version references and precise changes. Otherwise, preserve before-and-after snapshots of the affected files. A rollback must account for subsequent edits so that reversing one iteration does not silently discard later work.

A single append-only document per skill was considered simpler initially but harder to navigate as detailed records accumulate. Session-level documents grouped by skill were rejected because they make a single skill's history harder to trace. Git-only recovery would exclude installations without a reliable version baseline, while always taking full affected-file snapshots would duplicate recoverable Git content. The hybrid approach accepts some implementation complexity to support both repository and standalone skill use.

History follows the target skill's source repository, under `docs/skill-evolution/<skill-name>/`. When only a standalone installation is available, establish a persistent history location before proceeding. This avoids spreading one skill's history across the projects where it happened to be used or routinely distributing accumulated history inside its installed runtime.

The explicitly invoked `evolve-skills` workflow will discuss concrete hypotheses with the user before implementing the selected changes, validating them, and recording the results. It can run independently; co-active grilling skills deepen the discussion without becoming a required dependency.

When behavioral validation cannot be completed, retain the candidate patch or version with a pending-validation record and leave the active version unchanged. This preserves useful work without treating an unverified candidate as an adopted improvement. A user can explicitly choose to trial it.
