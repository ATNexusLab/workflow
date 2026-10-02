# The maintainer changes a piece

Milestone: M1. Not built yet; specified in [epic #1](../../specs/installable-core.md).

1. The maintainer edits one file of the **Canonical content**, or one file of the **Claude Code
   adapter**.
2. The maintainer runs the **Build**. It reads the canonical content and the adapter, replaces every
   reference token with the name Claude Code uses, and renders every file in memory.
3. A token that resolves to nothing stops the build before anything is written.
4. With no error, the build replaces the **Claude Code plugin** directory.
5. The maintainer runs the gates: the build check, the **Content scan**, and the secret scan.
6. The commit holds the authored change and the generated change together.
