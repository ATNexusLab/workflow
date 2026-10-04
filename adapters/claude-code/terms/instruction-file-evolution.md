Find
  every one (`find . -name AGENTS.md -o -name CLAUDE.md -o -name CLAUDE.local.md`, outside dependency
  folders), read each, keep every rule that still holds, and show me a diff per file. A `CLAUDE.md` or
  `CLAUDE.local.md` in a directory, or above it, stops Claude Code from reading the `AGENTS.md` there,
  so each `CLAUDE.md`'s content moves into the `AGENTS.md` of the same directory and the `CLAUDE.md` is
  removed. A `CLAUDE.local.md` is personal and uncommitted: I ask whether its rules belong in the repo
  before touching it.
