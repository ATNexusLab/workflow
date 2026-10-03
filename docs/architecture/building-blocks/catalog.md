# Catalog

`.claude-plugin/marketplace.json` — JSON. Milestone: M1.

## Job

Makes this repository a catalog Claude Code can add. It names the catalog `atnexuslab` and lists one
plugin, with the path of the [Claude Code plugin](claude-code-plugin.md) in the repository.

## What it never does

It is not generated. It sits at the repository root because Claude Code reads it there, outside
`plugins/`.

## To change it safely

- The entry's `name` is the `name` of `adapters/claude-code/plugin.json`. `python3 build.py --check`
  fails when they differ.
- `claude plugin validate --strict .` checks the file against Claude Code's own rules.
- An adopter's Claude Code reads the catalog from the branch it was added from, so a change reaches
  adopters when it reaches `main`.
