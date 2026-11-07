# Rate the risk of a change

Identify the proposed repair or examined patch. Ask who could lose what if the change is wrong, how the failure could occur, and how they could recover. Use the project's own change-risk scale when it has one and name that scale. Apply required approvals and protected-path rules separately.

Otherwise use the highest level supported by a reachable failure of the whole change. Trace relevant consumers before judging how far an error can spread.

| Level | Consequence if the change is wrong | Evidence to seek |
| --- | --- | --- |
| Low | The effect is local, visible, and easy to correct. | Inspect the intent, diff and direct use. Verify the assumed boundary and one representative result. |
| Medium | A supported workflow can break or give wrong results. Its effects are bounded and users have a practical recovery path. | Follow the normal entry point to its consumers. Check the likely failure and a neighboring behavior that must still work. |
| High | A reachable failure can cause serious data loss, expand privileges, prevent startup or recovery, or spread harm that is hard to undo. | Trace the critical failure path through the relevant permissions, state transitions or recovery steps. Challenge the safeguard with evidence that distinguishes a working protection from one that fails. |

If a material assumption is open, label a defensible rating provisional and name the check that could change it. If no level has a basis yet, say what is missing. A clean review or a passing test can strengthen the evidence at any level. A lower rating needs a change in the supported failure path, consequences, affected users or recovery conditions.

Reuse evidence when its code, configuration, environment and expectation still apply. Seek the smallest authorized check that answers the remaining question. If evidence stays unavailable, state the specific outcome still unknown, which next step the evidence supports, and which decision remains open. Continue authorized work that can resolve the gap. Report a demonstrated failure as a finding.

Give the level and its concrete reason even when review finds no defects. For a small local change, one sentence can cover both the risk and the check. For consequential changes, give the decisive evidence and any choice about scope, cost or residual risk. A risk rating describes the change. Finding priority describes when to address a problem.
