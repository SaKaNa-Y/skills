# Background Reconciliation

Read this when dispatching an Issue-ready Problem after all active independence gates are open.

## Hand Off a Bounded Search

Give the worker the User Problem and why this finding is independent, the observed evidence and acceptance boundary, the canonical Tracker Guidance or its exact pointer, and the [issue capture procedure](issue-capture.md). Supply only the context needed to distinguish records; retain the original packet in the main conversation.

Assign read-only reconciliation: search existing records and related implementation work, compare problem identity and coverage, and return the disposition with supporting evidence. The worker may read relevant PR contents to establish coverage; diagnosis, new reproduction campaigns, repairs, tracker mutations, and further delegation are outside this assignment. It returns any proposed issue text to the main agent rather than publishing it.

Continue the User Problem after dispatch. Receiving a result does not start a new repair task or interrupt the user for ordinary publication approval. Track each packet's assigned worker or deferred state so no finding is lost or searched twice.

## Return Enough to Decide

Ask for a compact result containing:

- The problem identity and Reconciliation Disposition.
- Canonical matching records: title, identifier or link, state, and why they match.
- Related issue/PR coverage: what is addressed, what remains different, and what is uncertain.
- Queries and candidates inspected, search limitations, and any missing evidence needed for a proposed update or new record.

Follow the bounded search completion rule in issue capture. A failed or unavailable canonical search returns Reconciliation Blocked with the retained evidence. An unavailable supplemental PR search is reported as a limitation rather than proof that no implementation exists.

The main agent collects these results after the main task completes, checks that each conclusion is supported by the returned evidence, and owns the final draft and approval interaction. Recheck mutable record state before an approved write when the elapsed work or new information could have changed the disposition; a materially changed proposal needs renewed approval.
