# Build

`build.py` and `builder/` — Python, standard library only. Milestone: M1.

## Job

| Command | Does |
| --- | --- |
| `python3 build.py` | Packages the canonical content and the adapter in memory, then replaces `plugins/claude-code/` |
| `python3 build.py --check` | Packages the same way and compares the result with the committed directory and the catalog entry. It is the Build gate |

## What it never does

- It writes nothing outside `plugins/`.
- It writes nothing when packaging fails: every file is produced in memory first.

## Inner blocks

| Module | Responsibility |
| --- | --- |
| `build.py` | Orchestrates: reads the arguments, asks a harness module for the plugin's files, then has them written or compared, and reports. It holds no packaging logic |
| `builder/pieces.py` | Reads `canonical/`: every agent, skill, and command, with a skill's supporting files |
| `builder/tokens.py` | Replaces each reference token of one file with its value, and lists the tokens that resolve to nothing, each with its file and line |
| `builder/frontmatter.py` | Adds lines to the end of a piece's frontmatter |
| `builder/claude_code.py` | Returns every file of the Claude Code plugin, path and content, with each token rendered as the name Claude Code uses or as the adapter's term, and compares the catalog entry with the manifest. The one place that knows how Claude Code lays out a plugin |
| `builder/plugin_directory.py` | Replaces `plugins/<harness>/`, and lists each path that differs from a fresh build, is missing, or is not produced |
| `builder/errors.py` | `BuildError` |

How Claude Code is packaged:

| Canonical | Plugin |
| --- | --- |
| `agents/<name>.md` | `agents/<name>.md` |
| `skills/<name>/` | `skills/<name>/`, every file |
| `commands/<name>.md` | `skills/<name>/SKILL.md` |

## To change it safely

- Every failure is a `BuildError` whose message is the lines the maintainer reads. It is caught once,
  where the script is run, and exits 1.
- Files are read and written as bytes, so a line ending is never translated.
- A new harness is a new module beside `builder/claude_code.py`, never a branch inside it.
- A module of `builder/` never prints and never exits. Both belong to `build.py`.
- The tests in `tests/test_build.py` run both commands on a small repository built in a temporary
  directory.
