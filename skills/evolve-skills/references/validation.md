# Behavioral Validation

Use this reference when defining a hypothesis's evaluation and when evaluating its candidate. The target's purpose determines the evidence needed: a discovery skill may need observable coverage, a discussion skill may need decisions clarified, and a writing skill may need an artifact that serves its intended reader. Neither longer instructions nor a larger output proves improvement.

## Define the comparison before editing

Identify the behavior the hypothesis predicts, the original scenario that exposed the opportunity, and useful behavior that should be preserved. Fix the inputs and evaluation criteria before comparing versions. Distinguish what was observed in the historical run from a fresh baseline replay; note changes in model, tools, task data, or environment that limit the comparison.

Use the smallest real behavioral exercise that can distinguish the versions. Start with the original scenario, then choose transfer probes proportional to the change: a different input, an adjacent use case, or a boundary where the new method should stay inactive. The purpose is to challenge a scenario-specific fix, not to require an exhaustive suite. Reuse suitable prior probes and revise them when the contract changes.

Keep the baseline and candidate in separate workspaces or contexts where practical. When independent agents or a test harness are available and their use is authorized, give evaluators the target version, realistic request, and necessary raw artifacts without the proposed answer or the author's diagnosis. Otherwise perform the feasible checks and accurately state their limits. A written prediction or the author's role-play of the expected answer is not a fresh behavioral run.

Replaying a conversation means recreating its task conditions, not executing its historical commands indiscriminately. Use disposable resources or permitted fixtures for side effects; obtain any additional authority required by a real external operation. Lack of a safe behavioral environment leads to Pending Validation, not fabricated success.

## Evaluate and preserve the evidence

For each scenario, retain the input or fixture reference, target version, relevant environment, observed output or actions, and the criterion's result. Separate evidence into:

- **Historical observation:** What the available conversation or artifact actually shows.
- **Fresh behavioral result:** What an actual baseline or candidate run produced.
- **Structural check:** Valid metadata, reachable references, clean diffs, or an applicable repository check. These check packaging and consistency, not behavior.
- **Unresolved:** Missing environment, confounded comparison, incomplete evidence, or a result that does not discriminate between versions.

Choose further runs when results conflict, variability could change the decision, or new edits invalidate earlier evidence. Scale the work to the uncertainty rather than using an arbitrary repetition count. Do not claim general effectiveness from a single successful example.

Adopt a selected candidate when the required comparison supports the intended benefit and relevant preserved behavior survives the probes. Report the tested scope. If benefit is unsupported or useful behavior regresses, retain that finding and refine or reject the candidate. When required behavior cannot be evaluated, retain the candidate as Pending Validation and keep the active baseline unless the user explicitly selects an unverified trial.

Recheck the active files before adoption. If they changed since capture, reconcile the candidate with the newer state and rerun affected checks before applying it. Preserve recovery evidence for the exact baseline actually changed.
