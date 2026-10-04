# Canonical content

`canonical/` — Markdown. Milestone: M1.

## Job

Holds the one authored copy of every piece of the workflow. A piece is edited here and nowhere else.

| Path | Piece |
| --- | --- |
| `agents/<name>.md` | A subagent |
| `skills/<name>/SKILL.md` | A skill, with its supporting files beside it |
| `commands/<name>.md` | A command |

## What it never does

- It names no harness, no harness path, and no harness tool or command. Nothing in it matches a line of
  `adapters/neutrality-terms.txt`.
- It carries no frontmatter field that only one harness reads. Such a field comes from that harness's
  [adapter](claude-code-adapter.md).

## To change it safely

- Run `python3 build.py` after every edit and commit the generated change with the authored one.
- A piece's frontmatter is `name` and `description`, plus `argument-hint` for a command. The table of
  canonical frontmatter is in the [spec of epic #1](../../specs/installable-core.md).
- A new agent, skill, or command needs no change to the build: it is found by its path.
- A reference to a command or a skill is written `{{command:<name>}}` or `{{skill:<name>}}`, and text
  only one harness can say is `{{harness:<key>}}`. A `{{` that opens no such token stops the build.
