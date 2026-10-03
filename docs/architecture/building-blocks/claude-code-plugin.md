# Claude Code plugin

`plugins/claude-code/` — generated files. Milestone: M1.

## Job

The directory Claude Code copies into its cache when an adopter installs `tightship@atnexuslab`. What is
in it is exactly what an adopter receives.

| Path | Holds |
| --- | --- |
| `.claude-plugin/plugin.json` | The manifest, copied from the [adapter](claude-code-adapter.md) |
| `agents/adversarial-verifier.md` | The verifier, reached as `tightship:adversarial-verifier` |
| `skills/<name>/` | The skills and the commands, from [#10](https://github.com/ATNexusLab/workflow/issues/10) |

## What it never does

- It is never edited. A file written here by hand is removed by the next build, and
  `python3 build.py --check` fails on it before that.
- It ships no hook and declares no user configuration.

## To change it safely

Edit the [canonical content](canonical-content.md) or the adapter, run `python3 build.py`, and commit
both changes together. `claude plugin validate --strict plugins/claude-code` checks the result against
Claude Code's own rules.
