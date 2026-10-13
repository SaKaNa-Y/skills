# Historical reference case

`test_historical_unchanged_incoming_reference` retains minimal excerpts from the
October 11, 2026 Yak revision in this repository. The reference document kept its
old link while the main document changed its heading. The old checker skipped
unchanged source documents and reported no errors.

The original heading and reference are recoverable at Git revision
`163eadb14469f9f13b5234d0b8e4d7eaaed77282` in
`skills/yak-shaving-triage/SKILL.md` and
`skills/yak-shaving-triage/references/discovery-lenses.md`. The test uses the
candidate heading `1. Establish capture and guard the next branch` and the
unchanged reference to `#1-guard-the-next-branch`.

These are reduced excerpts, not a full historical checkout or a fresh product
execution. The test constructs the old, broken, and corrected states in a
temporary directory. It does not require private evolution records.
