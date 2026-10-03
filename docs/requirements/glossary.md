# Glossary

| Term | Meaning |
| --- | --- |
| Adopter | A person who installs the plugin in a harness. |
| Baseline | The commit of the pre-plugin workflow that parity is measured against, recorded in the [overview](overview.md#assumptions-and-dependencies). |
| Canonical content | The authored files of the workflow's pieces in this repository, before any harness-specific packaging. |
| Checkpoint | The reminder that asks the agent whether the session produced a durable fact worth a note. |
| Command | A named set of instructions the adopter invokes: one step of the development loop, or one memory function. |
| Companion plugin | A third-party plugin the maintainer uses alongside the workflow: ponytail, i-have-adhd, humanizer. |
| Contract | The workflow's always-on rules: how the agent works, writes code, tests, commits, and handles security. |
| Handoff | A note that carries a project's state from one session to the next. |
| Harness | A coding-agent product that runs sessions and loads plugins: Claude Code, Cursor, Antigravity CLI, Codex. |
| Harness plugin | The package this repository provides for one harness, built from the canonical content. |
| Hook | A script a harness runs on its own at a session event, such as session start or prompt submission. |
| Install guide | The document in this repository that tells an adopter how to install, configure, update, and remove the plugin in one harness. |
| Maintainer | The author of the workflow and the only editor of this repository. |
| Memory | The optional component made of the vault functions: session-start context, checkpoint, search, write, lint, handoff release, handoff fetch, sync. |
| Note | One durable fact in the vault, in one file, with the reason it exists. |
| Optional component | A part of the plugin an adopter can enable or disable: the contract, memory, the status line. |
| Piece | One unit of the workflow: the contract, a skill, a command, the verifier, the memory script, the status line script, the vault template. |
| Pinned note | A note listed in the agent's context at every session start. |
| Pre-plugin workflow | The workflow as it runs before this product: files in one harness's user directory, installed by script. |
| Reduced mode | The plugin running with the contract disabled: skills, commands, and the verifier work, and the contract's rules do not apply. |
| Release | A published version of a harness plugin that an adopter can install or update to. |
| Remote | The copy of a git repository on a server, which the local copy sends commits to and receives them from. |
| Scope | The grouping of notes in the vault: one per project, plus the shared scope every project reads. |
| Skill | A method the agent loads when a task calls for it. |
| Status line | The line a harness shows under the prompt with the session's state. |
| Sync | The function that makes the vault and its remote hold the same notes and sends the project's commits to the project's remote. |
| Supported version | The oldest version of a harness the plugin is verified on. Until [OQ-07](open-questions.md#oq-07) is settled, it is the version observed in the [overview](overview.md#operating-environment). |
| Vault | The adopter's own git repository of notes, shared by every harness on their machines. |
| Vault template | The files a new, empty vault starts from. |
| Verifier | The read-only subagent that tries to disprove one claim before it is trusted. |
