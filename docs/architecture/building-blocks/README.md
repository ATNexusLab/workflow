# Building blocks

![Container diagram](../../diagrams/containers.drawio.svg)

Dashed elements are not built yet; each carries the milestone that builds it.

| Block | Technology | Responsibility | Talks to | Milestone |
| --- | --- | --- | --- | --- |
| Canonical content (`canonical/`) | Markdown | The authored copy of every piece, naming no harness | — | M1 |
| Claude Code adapter (`adapters/claude-code/`) | JSON, Markdown | What Claude Code needs and the canonical content cannot say: the manifest, the frontmatter additions, the terms | — | M1 |
| Build (`build.py`) | Python | Renders the canonical content into the plugin, and checks that the committed plugin matches | Canonical content, adapter, plugin (files) | M1 |
| Content scan (`scan.py`) | Python | Finds harness names in the canonical content, personal identity in the plugin, and tracked environment files and vault notes | Canonical content, plugin (files) | M1 |
| Claude Code plugin (`plugins/claude-code/`) | Generated files | What Claude Code installs | — | M1 |
| Catalog (`.claude-plugin/marketplace.json`) | JSON | Names the plugin and where it is in the repository | Plugin (path) | M1 |
| Adapters and plugins of Cursor, Antigravity CLI, and Codex | Per harness | The same two blocks for each later harness | — | M2 to M4 |

Why the blocks are split this way is
[ADR 0001](../../decisions/0001-canonical-content-rendered-into-one-plugin-per-harness.md).

Not written yet:

- **One file per block.** The pull request of [epic #1](../../specs/installable-core.md) writes them
  from what it builds.
- **The blocks of the contract, the memory layer, and the status line.** Each is added by the spec of its
  epic.
