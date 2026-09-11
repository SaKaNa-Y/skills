# Behavioral Validation

Use this reference when defining a hypothesis's evaluation and when evaluating its candidate. The target's purpose determines the evidence needed: a discovery skill may need observable coverage, a discussion skill may need decisions clarified, and a writing skill may need an artifact that serves its intended reader. Neither longer instructions nor a larger output proves improvement.

## Define the comparison before editing

Identify the behavior the hypothesis predicts, the original scenario that exposed the opportunity, and useful behavior that should be preserved. Fix the inputs and evaluation criteria before comparing versions. Distinguish what was observed in the historical run from a fresh baseline replay; note changes in model, tools, task data, or environment that limit the comparison.

State the method's domain-level benefit and applicability conditions. Abstract wording or removing a person's name does not establish generality. Use the smallest real exercise that can distinguish the versions: compare the original scenario, then probe materially different user needs within the intended domain and a boundary where the new method should stay inactive. Choose probes proportional to the change, without requiring multiple real users before a hypothesis can be tried. Reuse suitable prior probes and revise them when the contract changes.

Inspect the whole proposed method each iteration against its purpose and explicitly agreed responsibility boundaries, consulting relevant earlier decisions rather than treating every current rule as justified. For existing personal-looking defaults, distinguish a documented domain requirement from unexplained inheritance. Put an unsupported default's retention or removal into the proposal as an unresolved choice instead of automatically making it a preservation criterion. Look for accumulated narrowing, duplication, conflicts, and branches whose cost exceeds their benefit. Generality means serving the intended domain, not serving every task. Propose evidenced removals or consolidation through the normal selection checkpoint; this review neither authorizes a wholesale rewrite nor requires replaying every historical test.

Keep the baseline and candidate in separate workspaces or contexts where practical. When independent agents or a test harness are available and their use is authorized, give evaluators the target version, realistic request, and necessary raw artifacts without the proposed answer or the author's diagnosis. Otherwise perform the feasible checks and accurately state their limits. A written prediction or the author's role-play of the expected answer is not a fresh behavioral run.

Replaying a conversation means recreating its task conditions, not executing its historical commands indiscriminately. Use disposable resources or permitted fixtures for side effects; obtain any additional authority required by a real external operation. Lack of a safe behavioral environment leads to Pending Validation, not fabricated success.

## Evaluate and preserve the evidence

For each scenario, retain the input or fixture reference, target version, relevant environment, observed output or actions, and the criterion's result. Separate evidence into:

- **Historical observation:** What the available conversation or artifact actually shows.
- **Fresh behavioral result:** What an actual baseline or candidate run produced.
- **Structural check:** Valid metadata, reachable references, clean diffs, or an applicable repository check. These check packaging and consistency, not behavior.
- **Unresolved:** Missing environment, confounded comparison, incomplete evidence, or a result that does not discriminate between versions.

Choose further runs when results conflict, variability could change the decision, or new edits invalidate earlier evidence. Scale the work to the uncertainty rather than using an arbitrary repetition count. Do not claim general effectiveness from a single successful example.

Report whether the required comparison supports the intended benefit and preserved behavior within the tested scope. If benefit is unsupported or useful behavior regresses, retain that finding. If evaluation is blocked, identify the missing prerequisite, feasible checks actually attempted, and a concrete resumption condition. Tests not yet run remain work to do when the necessary tools and authority are available. Follow the main workflow's adoption or pending branch from this evidence.

Recheck the active files before adoption. If they changed since capture, reconcile the candidate with the newer state and rerun affected checks before applying it. Preserve recovery evidence for the exact baseline actually changed.
