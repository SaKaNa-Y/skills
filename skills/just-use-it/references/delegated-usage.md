# Delegated Usage

Use the existing Capability Groups and Vertical Capability Slices as the unit of delegation. Workers perform real user journeys, variations, and exploration; they are not merely source readers or command planners.

## Assign a Slice

The main agent owns the combined Coverage Ledger, target identity, phase transitions, and final report. Give each worker this skill and its relevant references, its assigned outcome and coverage boundary, public starting material, verified artifact or instance, current source/tracker access state, and authorized disposable resources. Supply only the context needed for that assignment rather than the full conversation. A worker does not remap the whole product, start its own source pass, or spawn more agents.

A worker owns one slice through its completion or explicit interruption. Report newly discovered independent outcomes to the main agent instead of expanding into another worker's assignment. The main agent merges those outcomes into pending coverage and prevents duplicate assignments.

Use at most two concurrent Just Use It subagents unless the user explicitly requests more; available host capacity may require fewer. The main agent coordinates and handles shared setup rather than running a third parallel usage slice. Independently writable consumers may share a verified immutable artifact. Serialize prerequisite-dependent slices and work that would mutate the same installation, project state, browser session, or service. Do not open an extra browser session merely to create parallelism when the user selected an existing one.

## Preserve Audit Phases

Source and tracker boundaries apply to the whole audit, not separately to each worker. Finishing one slice does not open either boundary. The main agent advances the source pass only after collecting all hands-on slices required by the main workflow. Newly source-discovered slices use fresh workers with their provenance stated. If any agent reads implementation or tracker history early, report the departure and its affected scope; a fresh worker cannot restore independent provenance by forgetting that history.

## Hand Back Evidence

Return a compact result using the existing Verification Traces and Finding Packets:

- Assigned slice and coverage states, including exclusions and unfinished work.
- Observed outcomes, discriminating contrasts, findings, and material unknowns.
- Replayable inputs and key evidence, with paths or references for longer artifacts already retained.
- Artifact identity and any source or tracker exposure that changed the evidence scope.
- Resources created, cleanup completed, and anything explicitly transferred to the main agent.

Reference existing artifacts instead of copying full logs or the conversation. Remove secrets and unrelated personal information. The main agent reads additional evidence only when needed to evaluate a claim; a concise conclusion alone cannot establish Verified coverage. No separate handoff skill is required.

For an interrupted slice, add its last completed action, current state, and next action. Preserve enough evidence to resume without relying on a temporary path scheduled for deletion. Keep the unfinished work pending rather than marking it Verified to free a worker slot.

## Retire and Replace

Before retiring a worker, the main agent checks that its handoff supports the claimed coverage and that retained evidence and resource ownership are usable. Fill a newly available slot with a fresh worker for the next eligible slice; do not wait for the other worker solely to form a batch. Close the completed worker when the host supports it; otherwise finish and retire it without sending it new assignments. Do not claim that an unavailable close operation ran or that retiring an agent stops its processes.

On a user pause or stop, stop dispatching new work and promptly stop active workers. Collect available evidence and account for their resources, then follow the audit's cleanup and Partial Audit rules. Missing worker output limits coverage; it does not justify continuing product use after the stop.
