# Scope of PR assessments and review findings

A question about whether a patch fixes a reported problem can turn into a request for unrelated repairs. Assess now selects its checks and repair recommendations from the acceptance conditions for the question. A delivery decision can require evidence beyond the original reproduction.

In an order-export exercise, the revised instructions led to different actions for the same patch. The coverage assessment checked the missing final line. The adoption assessment also tested the audit callback because the consumer needed it to reconcile orders. The exercise covered these two requests. It did not measure general review quality.

The PR entry now uses the original finding as the assessment subject. A bare PR supplies the finding and its proposed remedy. The assessor checks its impact and coverage. Code review and a merge verdict require a separate request. This restores the earlier scope-comparison instruction and the original purpose in the skill description.

Review Change now asks the coordinator to explain why a finding needs a fix in the current change. A recommendation to hold the merge must explain the findings or missing acceptance evidence that justify waiting. An unresolved requirement that could change the verdict stays open as a question.
