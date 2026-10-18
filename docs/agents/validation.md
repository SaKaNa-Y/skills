# Check repository references

Use the repository link checker after changes to public Markdown, file paths,
or headings. It checks unchanged documents too. A heading change can break a
reference in a file that has no diff. Skill evolution and direct maintenance use
the same command. Follow this procedure before reporting local work complete.

## Run the checker

Use Python 3.9 or later. Create a virtual environment outside the candidate tree
and install the pinned runtime dependencies:

```bash
python3 -m venv /tmp/skills-link-check-env
/tmp/skills-link-check-env/bin/python -m pip install -r scripts/requirements.txt
/tmp/skills-link-check-env/bin/python scripts/check_markdown_links.py --root .
```

Pass the complete candidate tree to `--root`, not a directory that contains only
changed files. The checker resolves every local destination within that tree.
It does not fall back to the current checkout. It reads files without editing
them and never fetches URLs. Run `--help` for options, source patterns, and exit
codes. Use `--json` for a structured report.

The source scope includes root Markdown, all skill Markdown, agent guidance,
ADRs, and curated evolution README, skill indexes and iteration/discussion
records. It excludes test and fixture directories, dependencies, original
evolution evidence snapshots, planning, and research records. An explicit link into an excluded
directory still has its destination checked. Exclusion controls which documents
supply links, not whether a referenced file must exist.

## Interpret the result

The report lists each issue's source, line, original link syntax, and reason.
It also reports the source patterns, file count, local link count, external links
skipped, and incomplete checks. A line identifies the link's start within its
Markdown block. For unsupported syntax, it identifies the containing block.

Exit code 0 means no broken local references were found within the supported
profile. Exit code 1 means a local file or heading is missing. Exit code 2 means
the check is incomplete, even if it also found broken links. Missing dependencies,
unreadable Markdown, and an empty source scope also leave the check incomplete.

The parser supports CommonMark links and images, reference-style links, autolinks,
tables, and strikethrough. Code blocks, inline code, comments, and YAML frontmatter
do not supply links. File and directory destinations are checked for existence.
Markdown heading fragments use GitHub-style slugs, including duplicate headings,
inline formatting, and Unicode. URL-encoded relative paths and fragments are
decoded before checking.

Raw HTML, custom HTML anchors, absolute local paths, paths outside the candidate
root, local query strings, and fragments on non-Markdown files are reported as
incomplete. Symbolic links cannot escape the root. Unresolved explicit reference
syntax is also reported as incomplete. Undefined shortcut references are plain
text under CommonMark. This tool does not promise support for every Markdown
extension or every feature of GitHub's renderer.

The pinned [markdown-it-py parser](https://github.com/executablebooks/markdown-it-py)
and `github-slugger` dependency provide parsing and heading slug generation.
The tool checks reference structure. It does not judge whether a link supplies
the right evidence or whether a skill behaves correctly. YAML metadata and skill
invocation policy remain outside this checker.

## Validate checker changes

```bash
PYTHONDONTWRITEBYTECODE=1 /tmp/skills-link-check-env/bin/python -m unittest discover -s tests -v
```

The suite includes the [historical unchanged-reference case](../../tests/fixtures.md)
and positive and negative cases for paths, anchors, syntax, scope, and exit codes.
Keep unsupported cases visible rather than reporting them as passed. Check the
public tree after changes to the checker or its documentation.

## Continuous integration

The [Repository references workflow](../../.github/workflows/references.yml) runs
on pull requests, pushes, and manual dispatch. It installs the same pinned
dependencies, runs the checker tests, and checks the complete checkout with the
same command used locally. It does not filter by changed paths. A renamed or
deleted target can affect a reference in an unchanged document.

Both broken references and incomplete checks fail the job. The workflow does
not change branch protection or make its status a required merge check.
Local checks provide feedback before a push. CI checks the version on GitHub.

## Validate evolution history

After changing public summaries, their schema or paths, run:

```bash
/tmp/skills-link-check-env/bin/python scripts/check_skill_history.py --root . --strict
```

Pass the complete candidate tree. The read-only checker checks owned identities,
declared source names, local sequence numbers, lifecycle metadata, paused next actions, curated links,
evidence hashes, migration destinations and recovery-file presence. Historical
Markdown inside evidence packages is data, not current navigation. Old embedded
verification results remain historical statements; the manifest hashes attest
the retained files, including declared sanitized derivatives.

Publication warnings identify possible private material, binary files and files
over 5 MiB without quoting their contents. Review every warning; a clean scan
does not prove that all sensitive information was removed. `--strict` fails on
these warnings as well as structural errors. The tool never deletes files,
modifies Git, fetches sources or reruns historical trials. It checks recovery
inputs, not whether a recovery procedure works.

Before completing a migration, export the full candidate Git tree, including
new long-term records, into a clean directory and run both checkers against that
directory. A copy of the working tree containing ignored files is not this
check. Report saved, committed and pushed states separately. The checks cannot
prove that an inventory omitted no original material: compare the migration
manifest with the original inventory before releasing quarantine inputs.

### Local archive checks

Detailed history is ignored and is never required by public CI. To validate the
local archive explicitly, run:

```bash
/tmp/skills-link-check-env/bin/python scripts/check_skill_history.py --root . --local-history .local/skill-evolution
```

This mode checks that archive's navigation, declared identities, metadata and
file hashes. It allows registered `retained/` and `migration/` directories and
omits publication warnings for private text and binary evidence. It still
rejects environments, symlinks, missing inputs, changed hashes and links into
other private or temporary locations. The archive must resolve below `.local/`;
this option cannot disable publication checks on the public history tree.
Historical statements remain historical; integrity checks do not replay trials.

### History manifest version 1

`docs/skill-evolution/manifest.json` registers only selected public material.
The local archive has a separate manifest with the same four arrays:

- `skills`: `name`, `status` (`active`, `retired`, `transferred`), optional
  `previous_names` and `successors`; inactive identities also need `reason`.
- `records`: history-relative `path`, `status` (`active`, `completed`, `paused`, `blocked`,
  `abandoned`, `unknown`), `adoption`, `validation`, optional `recovery` paths and
  `limitations`. Paused or blocked work needs `next_action`; unknown legacy
  lifecycle needs a limitation. Applied work needs recovery files or an explicit
  historical recovery gap. Adoption uses `applied`, `not-applied`, `proposed`,
  `candidate`, `rejected`, `no-change`, `superseded`, `rolled-back`, or `unknown`.
  Validation uses `supported`, `unsupported`, `inconclusive`, `pending`,
  `not-run`, or `unknown`; migration never upgrades these claims.
- `files`: history-relative `path`, `sha256`, and `kind` (`original`, `sanitized`,
  `curated`, `recovery`). Every evidence/recovery file needs an entry. Sanitized
  files also need a provenance/limitation `note`; `original_sha256` can preserve
  the identity of a quarantined original without publishing it.
- `migration`: original repository-relative `source`, `disposition` (`retained`,
  `sanitized`, `quarantined`, `removed`), and `reason`. Retained or sanitized
  entries need a history-relative file `destination`. Optional source hashes
  support comparison with the original inventory. When declared, source hashes
  must match retained bytes or the sanitized file entry’s `original_sha256`.
  Each original source has one disposition; duplicate sources fail. Quarantined items deliberately
  do not require ignored inputs to exist in the exported candidate tree.

The report includes counts for identities, records, integrity files, migration
entries, curated documents and checked local links. All files in the selected history root must
be curated navigation or registered integrity inputs.

Paths resolve within the selected tree; absolute paths, traversal and history
symlinks fail. A manifest is evidence of the declared inventory, not proof of
its completeness. Curated records explain limits for people; metadata supplies
the corresponding state for mechanical checks.

Active identity checks read the initial YAML header (up to 64 KiB) and accept
one top-level kebab-case `name` scalar, optionally quoted or followed by a
comment. Unsupported or duplicate name fields fail explicitly. This bounded
check detects source-name changes without claiming general YAML validation.
