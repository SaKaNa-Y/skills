---
name: browse-records
description: Browse working records, their recorded status, and the evidence behind each item.
disable-model-invocation: true
---

# Browse Records

Show a read-only view of the configured current Working Records when the user explicitly invokes this viewer. A general status question or another workflow finishing does not activate it. The records remain authoritative; this view helps the user locate and understand them without reassessing or maintaining them.

## English output

Before writing or revising English prose, use the installed `simple-english`
skill. Load it by name, or read its `SKILL.md` and applicable references.
Reuse instructions already loaded in this context.
After reading this contract, load the dependency before sending any English
progress update, draft or final response.

Preserve meaning, uncertainty, requirement strength, domain terms and
task-required formats when style rules conflict. Keep the requested language.
Preserve code, identifiers, commands, original quotations and historical evidence.

If required instructions are unavailable, report the gap once and continue
independent work. Keep affected English output as a draft until the dependency
is available or the user explicitly authorizes an exception. Do not install
dependencies automatically or claim that an unchecked draft meets this requirement.

## Resolve the view

Use the current explicit instruction, applicable project guidance, then global configuration to locate the records root. Reuse a known location. Follow a configured migration map to current records; retained historical stores are supporting history. Resolve the project by repository identity or another unambiguous identifier, rather than its folder name alone. If the root is unknown or inaccessible, state that limit and ask for the missing location or access; do not create a replacement store.

Default to the current or clearly identified project. When no project is identified, show the root's project directory and recorded summaries instead of expanding every project. Within a project, show active Findings and Explorations separately, with archived counts and a link to archived records. Honor explicit category, item, group and lifecycle scope; “only Findings” excludes Explorations from the view. Keep lifecycle scope separate: a category or keyword filter retains the active-only default unless the user asks to include archived items. On follow-up, retain applicable scope and replace only the dimensions the user changes; an explicit whole-group request selects its recorded members.

Read the applicable overview and compare its entries with the project record files. Follow primary-record sections for the requested items, displayed status and relevant filter fields. Inspect enough of unindexed candidate records to distinguish an omitted identity from supporting material. Evidence files and audit reports are not automatically additional items. Read lengthy evidence and history only when requested or needed to explain a material conflict.

## Preserve record meaning

A Problem Identity is the recorded problem or opportunity and its acceptance boundary. One file may contain several identities; several files, locations or PRs may concern one identity. Count distinct identities, not files, evidence artifacts or repair-group names. Use established links and recorded relationships; show ambiguous identity or a broken primary link as a limitation instead of silently merging or dropping it.

Keep these dimensions separate:

- **Category:** Findings concern existing behavior, including unconfirmed observations, defects and improvements. Explorations concern proposed capabilities or workflows. Display the recorded category; this viewer does not reclassify it.
- **Assessment:** the recorded judgment, confidence, rationale and suggested priority where present.
- **Handling and lifecycle:** decisions, selection, deferral, implementation, verification, delivery and active/archived status. An assessed item may still await selection; deferred does not mean archived, and a shared PR does not give every member the same outcome.

Display conflicting index/body values with links to both. A clearly dated superseding section can identify the recorded current account; unexplained disagreement remains visible. Report missing entries or fields as missing. Totals affected by ambiguous identities or incomplete access are qualified, not presented as reconciled counts.

State the local source being viewed and the relevant recorded dates or versions. Reading a record today does not refresh its evidence or PR state. Keep delivery status labelled as recorded, with its checked date when available. This workflow performs no remote refresh, pull, record edit, commit, push, tracker mutation or experiment. Requests for reassessment or maintenance belong to their owning workflow under the user's separate scope.

## Order and filter

Preserve project-index order within each category by default. Support requested sorting by recorded priority, dated substantive update or handling state, keeping source order for ties. Keep unknown values visibly unknown and after known values for a requested sort; file modification time is not a substantive-update date. State a chosen sort direction when the user leaves it unspecified.

Apply requested filters for project, category, recorded assessment, handling/lifecycle, recorded priority, keyword, or linked issue/PR/repair group. Combine dimensions with AND and alternatives within a dimension with OR. Inspect relevant primary-record content for these fields rather than searching only overview titles. Use only recorded group membership.

Keep “unassessed” distinct from “assessed, awaiting selection.” Interpret “unfinished” as active/not archived unless context specifies a narrower meaning, and state that interpretation. Report active filters and matched versus inspected identity counts. If unreadable records could match, show that coverage limit rather than reporting a definitive zero. Preserve all matches; for a long view, state paging coverage and how to reach the remainder instead of silently selecting a top few.

## Present and finish

Use the conversation for the default view:

1. State scope, source and freshness limits. Put material conflicts, missing entries and count limitations before totals.
2. Show qualified totals and separate category tables with **Item | Recorded assessment | Handling status | Recorded next action**. Link each item directly to its original primary file or section; keep issue/PR links with handling. Include priority when recorded. Provide the archived-record entry point for the selected scope.
3. For requested archived items, show whether the accepted problem was resolved, why it was archived and its related delivery. Expand requested details rather than inserting full evidence into every row.

A focused item detail contains its scenario and impact, assessment with basis/date/version, handling and delivery, decision-changing unknowns, next action and acceptance, plus original record/evidence links. Keep consequential contrary evidence or conflicts visible in that detail. Full logs, long reproduction procedures and history are optional on request. A group view shows shared work and each member's own assessment, handling and acceptance.

Treat tables as comparable rows, not a mandatory shape for a single short answer. Avoid a combined completion percentage across different kinds of work. Interactive artifacts are an optional presentation request, not the default; any requested artifact is a labelled source snapshot, never a second canonical record store. The conversation itself needs no saved summary file.

Before finishing, check that each displayed item and field maps to the inspected original record, counts use the same scope as filters, links resolve, and unknowns/conflicts remain visible. State any incomplete coverage. Completion means a faithful view with traceable sources, not repaired records or freshly verified product status.
