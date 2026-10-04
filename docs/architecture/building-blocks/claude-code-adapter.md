# Claude Code adapter

`adapters/claude-code/` — JSON and Markdown. Milestone: M1.

## Job

States what Claude Code needs and the [canonical content](canonical-content.md) cannot say.

| File | Holds | The build |
| --- | --- | --- |
| `plugin.json` | The plugin manifest. The plugin's name is written here | Copies it to `.claude-plugin/plugin.json` of the plugin |
| `frontmatter.json` | Lines to add to a piece's frontmatter, keyed by the piece | Inserts them at the end of that piece's frontmatter |
| `terms/<key>.md` | The text of one `{{harness:<key>}}` | Writes it, without its final line break, where a piece writes the token |

A key of `frontmatter.json` is the piece's path under `canonical/`: `agents/<name>`, `skills/<name>`, or
`commands/<name>`.

## What it never does

It holds no script. How Claude Code lays out a plugin is code, in the [build](build.md).

## To change it safely

- A key that names no canonical piece stops the build, so a key is added in the commit that adds its
  piece.
- Changing `name` in `plugin.json` changes every namespaced name an adopter types. The entry in the
  [catalog](catalog.md) changes with it, and `python3 build.py --check` fails until it does.
