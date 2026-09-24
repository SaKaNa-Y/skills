# Use Slice-First Traversal for Usage-First Audits

Usage-first audits complete documented journeys and free exploration within each Vertical Capability Slice, while implementation source remains closed until all required hands-on slices finish. This trades broad early visibility for honest outcome evidence, bounded discovery, and resumable Partial Audits instead of shallow entrance sweeps. A bounded Reference Audit Suite may validate the general contract through real products, but it must pass the Generalization Gate and never introduce target-specific detection, branches, or rules.

## Delegated execution amendment

Just Use It delegates actual usage slices to fresh subagents, with at most two concurrent Just workers unless the user explicitly requests more. Independent slices may run together; dependent or shared-state work remains sequential. The main agent retains the combined coverage and phase boundaries, accepts compact evidence-backed handoffs, and retires each worker before assigning another slice to a fresh agent. This replaces audit-wide serial traversal while preserving depth within every slice. The cap is a conservative scheduling default, not an empirically optimal concurrency claim, and does not cap separately active skills.

This trades coordination and isolated resources for bounded worker contexts. Existing Verification Traces and Finding Packets carry results; an external conversation-handoff skill is not a dependency. Context or speed benefits require separate behavioral evidence rather than following from delegation alone.
