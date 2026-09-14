# Purpose-led Validation

Use this reference when proposing a change and evaluating its candidate. Choose evidence that can decide the intended value of each material change. Instruction quality, reusable knowledge, behavior, and efficiency require different evidence; a single metric need not represent the whole proposal.

## Define sufficient evidence before editing

Connect each change to its expected value, applicability conditions, useful behavior to preserve, and evidence sufficient for adoption. Fix the criteria before evaluation. Distinguish historical observations from fresh runs, including model, tool, input, or environment differences that limit a comparison.

For codifying a reusable method, trace the method to observed cases, compare it with existing instructions, and identify the useful gap: a missing decision, discovery route, context pointer, or boundary. Check that the abstraction transfers beyond the source case and that its expected value justifies its instruction cost. A list of renamed techniques or added text alone is insufficient. Existing model knowledge does not by itself establish that a reusable instruction has no value; equally, codification evidence does not establish improved execution.

For claimed behavioral improvement or efficiency, run the smallest realistic exercise that can test that claim. Compare relevant baseline and candidate outcomes, reusing trustworthy historical evidence when its conditions suffice. Add transfer or inactive-boundary probes where they resolve a material applicability or regression question. Required behavioral evidence that cannot safely be obtained remains pending; a prose prediction cannot replace it.

## Review the instructions before execution

Read the whole candidate against its purpose and agreed responsibility boundaries, consulting earlier decisions. Check decision order, context-pointer triggers, duplication, conflicting rules, and branches whose cost exceeds their value. Keep each rule in its authoritative location. This review precedes expensive runs so a readily visible instruction defect can be corrected first.

Distinguish documented domain requirements from unexplained inherited defaults. Bring an unsupported default's retention or removal into the proposal when material to this change. Generality means serving the intended domain; a whole-method review neither authorizes unrelated rewrites nor requires replaying every historical test.

## Run the checks that resolve the decision

For behavioral comparisons, keep versions in separate workspaces or contexts where practical. When independent agents or a harness are available and authorized, supply the target version, realistic request, and necessary raw artifacts without the author's diagnosis or expected answer. Otherwise perform feasible checks and state their limits. The author's role-play is not a fresh behavioral run.

Recreate task conditions using disposable resources or permitted fixtures for side effects. Historical commands are evidence, not authority to repeat external actions. Retain the input or fixture reference, version, relevant environment, actual outputs or actions, and criterion results. Preserve distinct evidence types:

- **Historical observation:** What the available conversation or source case shows.
- **Fresh behavioral result:** What an actual baseline or candidate run produced.
- **Artifact review:** Traceable synthesis, coverage of an instruction gap, applicability, and whole-method quality.
- **Structural check:** Metadata, reachable references, and clean diffs establish packaging and consistency rather than usefulness.
- **Unresolved:** Missing prerequisites, confounded comparisons, incomplete evidence, or indistinguishable outcomes.

A tie is inconclusive for the claimed comparative gain in that exercise. Judge other selected values using their own evidence. Before an additional run, identify the unresolved adoption question and why the next exercise can answer it. Continue when conflicting results, meaningful variance, or changed instructions warrant it. When the exercise cannot decide the intended value, explain the mismatch and revise the evaluation with the user if its acceptance basis materially changes. Preserve prior outcomes. A request to continue until improvement supplies direction, not evidence of success.

## Report the supported scope

Report codified methods, observed behavioral gains, regressions, and unresolved claims separately against the agreed criteria. A single successful example supports only its observed scope. Use this assessment in the [main workflow's adoption decision](../SKILL.md#5-prepare-validate-and-apply).
