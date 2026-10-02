# An adopter installs the plugin

Milestone: M1. Not built yet; specified in [epic #1](../../specs/installable-core.md).

1. The adopter adds the catalog in Claude Code: `/plugin marketplace add ATNexusLab/workflow`.
2. Claude Code clones the repository and reads the **Catalog**.
3. The adopter installs `tightship@atnexuslab`.
4. Claude Code copies the **Claude Code plugin** directory into its plugin cache and records the install
   in its settings. Nothing else of the repository is copied, and no script of the repository runs.
5. At the next session, Claude Code loads the plugin: the name and description of each skill and of the
   verifier enter the agent's context.
6. The adopter invokes a command as `/tightship:<name>`, the agent loads a skill when a task calls for
   it, and the main agent dispatches the verifier with one claim.
