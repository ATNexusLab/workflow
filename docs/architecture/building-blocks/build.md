# Build

`build.py` — Python, standard library only. Milestone: M1.

## Job

| Command | Does |
| --- | --- |
| `python3 build.py` | Packages the canonical content and the adapter in memory, then replaces `plugins/claude-code/` |
| `python3 build.py --check` | Packages the same way and compares the result with the committed directory and the catalog entry. It is the Build gate |

## What it never does

- It writes nothing outside `plugins/`.
- It writes nothing when packaging fails: every file is produced in memory first.
- It does not render tokens yet. That arrives with
  [#10](https://github.com/ATNexusLab/workflow/issues/10).

## Inner blocks

| Function | Responsibility |
| --- | --- |
| `package_claude_code` | Returns every file of the Claude Code plugin, path and content. The one place that knows how Claude Code lays out a plugin |
| `build` | Replaces the plugin directory with what the packaging function returned |
| `check` | Reports each path that differs, is missing, or is not produced, and a catalog entry whose name is not the manifest's |

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
- A new harness is a new packaging function beside `package_claude_code`, never a branch inside it.
- The tests in `tests/test_build.py` run both commands on a small repository built in a temporary
  directory.
