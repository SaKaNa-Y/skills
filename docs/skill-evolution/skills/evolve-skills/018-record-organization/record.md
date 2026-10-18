# Record Organization and Publication

Updated on 2026-10-18. Source implementation: [commit 59b1324](https://github.com/SaKaNa-Y/skills/commit/59b132417917d3d866dda0696c18577e288531cd). This is a local commit reference; its web page becomes available only after a separately authorized push.

Detailed experiments, personal recovery inputs and migration inventories had been bundled with publishable history. They serve local continuity, while public readers need the reason for an adopted change and its evidence limits. Evolve now resolves the detailed-record location separately from publication policy and selects concise public summaries. [The repository policy](../../../../agents/evolution-history.md) and [ADR 0011](../../../../adr/0011-keep-evolution-history-with-owned-skills.md) define the boundary.

History follows owned skills through renames and retirement. Paused work retains decisions and a next action. Cleanup retains necessary evidence without promising permanent replay of complete environments. Detailed local records remain outside Git backup; public summaries must work in a clean checkout without those records.

The read-only checker validates source identities, record states, references, declared evidence hashes and migration mappings. Its explicit local-history option checks the private archive without publication warnings. Public CI keeps strict publication checks. Regression tests cover isolation of the two modes, evidence tampering, links into other private directories and attempts to use local mode on a public tree.

Validation: 48 repository tests and 12 evaluation-helper tests passed for the implementation. This establishes structural and instruction-contract checks, not improved agent behavior. The implementation commit and its parent preserve source changes; private configuration is outside that reversal scope. Separate installed skills were not changed.
