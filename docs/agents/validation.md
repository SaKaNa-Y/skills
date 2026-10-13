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
and ADRs. It excludes test and fixture directories, dependencies, and private
evolution, planning, and research records. An explicit link into an excluded
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
