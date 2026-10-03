# Purpose-led Validation

Use this reference when proposing a change and evaluating its candidate. Choose evidence that can decide the intended value of each material change. Instruction quality, reusable knowledge, behavior, and efficiency require different evidence; a single metric need not represent the whole proposal.

## Define sufficient evidence before editing

Connect each change to its expected value, applicability conditions, useful behavior to preserve, and evidence sufficient for adoption. Fix the criteria before evaluation. Distinguish historical observations from fresh runs, including model, tool, input, or environment differences that limit a comparison.

For codifying a reusable method, trace it to relevant observed cases or inspected external sources, compare it with existing instructions, and identify the useful gap: a missing decision, discovery route, context pointer, or boundary. Check that the abstraction transfers beyond the source case and that its expected value justifies its instruction cost. A list of renamed techniques or added text alone is insufficient. Existing model knowledge does not by itself establish that a reusable instruction has no value; equally, codification evidence does not establish improved execution.

For claimed behavioral improvement or efficiency, run the smallest realistic exercise that can test that claim. Compare relevant baseline and candidate outcomes, reusing trustworthy historical evidence when its conditions suffice. Separate the question of improved capability from preservation of useful behavior. An existing scenario still passing supports no observed regression there, not equal effectiveness or a gain. Add transfer or inactive-boundary probes where they resolve a material applicability or regression question. Required behavioral evidence that cannot safely be obtained remains pending; a prose prediction cannot replace it.

Before running an exercise, identify the decision or state transition the candidate is meant to improve. Inspect the actor-visible request, documentation, tool behavior, artifacts, and staged information to establish what judgment remains for the agent. Identify any part the setup performs or reveals, and material differences from the target workflow. Preserve information genuinely available in that workflow; hiding useful documentation merely to make a task harder changes what is being tested. If the setup supplies the judgment under test, revise the exercise or limit the claim it can support.

To test independent diagnosis or action selection, preserve the relevant information gap without supplying the diagnosis or selecting the repair in the request. Explicit directions remain useful for instruction-following and boundary checks; report those separately. To test continuity across turns, deliver later input after the earlier response; supplying the whole exchange at once tests a static replay instead. Keep enough context to make the task solvable, and choose the smallest exercise that preserves the difficulty relevant to the selected value.

## Check the evaluator

Identify what would distinguish success from a plausible but deficient result. For material or disputed criteria, try known satisfactory and unsatisfactory examples before relying on the evaluator, including valid alternative solutions where rigid wording could reject them. Keep these calibration examples separate from the candidate's performance evidence. Check grading sensitivity separately from whether the setup leaves the intended decision to the actor. Repair insensitive criteria before spending more runs on them; material acceptance changes return to selection.

Use deterministic checks for observable properties such as file identities or actual resulting state. Use evidence-based model judgment for open reasoning, with the relevant outputs and criteria available for inspection. Resolve value disagreements through the user's stated goals or an explicit decision. Agreement among reviewers alone establishes neither correctness nor a useful distinction.

## Review the instructions before execution

For wording-only edits, check meaning and references. For behavior changes, read the whole candidate against its purpose and agreed responsibility boundaries, consulting earlier decisions. Check decision order, context-pointer triggers, duplication, conflicting rules, and branches whose cost exceeds their value. For each materially changed behavior branch, trace its trigger, responsible actor, action and observable result, and completion or pending condition. Pending work needs an owner and next action; a blocked branch needs its limitation and resumption condition. Keep each rule in its authoritative location. This review precedes expensive runs so a readily visible instruction defect can be corrected first.

Distinguish documented domain requirements from unexplained inherited defaults. Bring an unsupported default's retention or removal into the proposal when material to this change. Generality means serving the intended domain; a whole-method review neither authorizes unrelated rewrites nor requires replaying every historical test.

## Run the checks that resolve the decision

For behavioral comparisons, keep versions in separate workspaces or contexts where practical. When independent agents or a harness are available and authorized, supply the target version, realistic request, and necessary raw artifacts without the author's diagnosis or expected answer. Otherwise perform feasible checks and state their limits. The author's role-play is not a fresh behavioral run. Separate development cases used to revise the candidate from independent confirmation when exposure to those cases could explain success; keep the necessary task information available without leaking a preferred answer.

Bind each trial to the instructions actually used, inputs, relevant environment, execution identity and known model/tool settings; preserve unavailable facts as unknown. Use the host's existing authorized execution tools. A continuation that receives revised instructions tests correction in that session; a claim about a new version starting independently needs fresh execution of the affected path. Preserve earlier results rather than relabeling them as the final version.

For actual execution trials, read [evaluation records](evaluation-records.md) and use its lightweight helper when file/evidence checks are useful. It checks record consistency and captured artifacts; actual tool events and environment inspection support execution claims. A declared fresh session does not prove isolation. When assessing orchestration, scheduling or phase boundaries, inspect the relevant execution events for behavioral claims; a proposed sequence or simulation remains design evidence.

Recreate task conditions using disposable resources or permitted fixtures for side effects. Historical commands are evidence, not authority to repeat external actions. Retain the input or fixture reference, version, relevant environment, actual outputs or actions, and criterion results. Preserve distinct evidence types:

- **Historical observation:** What the available conversation or source case shows.
- **Fresh behavioral result:** What an actual baseline or candidate run produced.
- **Artifact review:** Traceable synthesis, coverage of an instruction gap, applicability, and whole-method quality.
- **Structural check:** Metadata, reachable references, and clean diffs establish packaging and consistency rather than usefulness.
- **Unresolved:** Missing prerequisites, confounded comparisons, incomplete evidence, or indistinguishable outcomes.

A tie is inconclusive for the claimed comparative gain in that exercise; it does not establish general equivalence or statistical non-inferiority. Check whether the exercise preserved the relevant difficulty and whether its criteria can detect the difference of interest. Use a discriminating case for an insensitive exercise, or repeated comparable trials when meaningful variation prevents a judgment. Stop when further runs cannot reasonably change the adoption decision, retaining the uncertainty rather than sampling until the preferred version wins. Judge other selected values using their own evidence. Before an additional run, identify the unresolved adoption question and why the next exercise can answer it. Continue when conflicting results, meaningful variance, or changed instructions warrant it. When the exercise cannot decide the intended value, explain the mismatch and revise the evaluation with the user if its acceptance basis materially changes. Preserve prior outcomes. A request to continue until improvement supplies direction, not evidence of success.

## Report the supported scope

Report codified methods, observed behavioral gains, regressions, and unresolved claims separately against the agreed criteria. A single successful example supports only its observed scope. Use this assessment in the [main workflow's adoption decision](../SKILL.md#5-prepare-validate-and-apply).
