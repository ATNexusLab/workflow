# 0001. Canonical content rendered into one committed plugin per harness

- Status: accepted
- Date: 2026-10-02
- Amended: 2026-10-03 — decision 7 places each part of the build in its own module of `builder/`,
  where it first read "one function in `build.py`". Decision 8 gives the content scan the same shape.

## Context

The workflow is written once and delivered to four harnesses, one milestone each
([BR-01](../requirements/business-rules.md#br-01)). The requirements pull in opposite directions:

- An edit to a piece changes exactly 1 authored copy
  ([NFR-MNT-01](../requirements/non-functional/maintainability.md#nfr-mnt-01),
  [BR-02](../requirements/business-rules.md#br-02)).
- The canonical content names no harness, no harness path, and no harness tool or command
  ([NFR-FLEX-06](../requirements/non-functional/flexibility.md#nfr-flex-06)).
- Every reference in delivered content is the name the harness invokes it by
  ([FR-SKL-03](../requirements/functional/skills.md#fr-skl-03)).
- The plugin installs with the harness's own mechanism, and no installer script of this repository runs
  ([FR-INS-01](../requirements/functional/install.md#fr-ins-01)).

What Claude Code 2.1.287 does, read in its documentation on 2026-10-02 and checked with
`claude plugin validate`:

- Installing from a catalog hosted on git copies the plugin's own directory into a cache. Files outside
  that directory are not copied, and a symlink that leads outside it is rejected.
- No build step runs at installation.
- Every component of a plugin is invoked under the plugin's name: a command is `/<plugin>:<name>`, a
  skill and a subagent are `<plugin>:<name>`. The bare name resolves only while nothing else uses it.
- Commands are merged into skills, and the documentation asks new plugins to use `skills/`.
- A subagent is restricted by a `tools` field that lists Claude Code's own tool names.

So the content an adopter receives has to hold harness names, and the content the maintainer edits must
not. This decision settles [OQ-01](../requirements/open-questions.md#oq-01),
[OQ-04](../requirements/open-questions.md#oq-04), and
[OQ-05](../requirements/open-questions.md#oq-05).

## Decision

1. **Three areas in the repository.**

   | Area | Holds | Edited by hand |
   | --- | --- | --- |
   | `canonical/` | The authored copy of every piece, with no harness name | Yes |
   | `adapters/<harness>/` | What one harness needs and the canonical content cannot say | Yes |
   | `plugins/<harness>/` | The plugin the harness installs, generated | Never |

2. **A build renders the plugin, and the result is committed.** `build.py` and its package `builder/`,
   Python standard library only, read `canonical/` and `adapters/<harness>/` and write
   `plugins/<harness>/`. `build.py --check` fails
   when the committed plugin differs from a fresh build, and it is the repository's Build gate.

3. **A reference is a token ([OQ-05](../requirements/open-questions.md#oq-05)).** The canonical content
   never writes the name of a command, a skill, the verifier, or a harness-native capability. It writes
   a token, and the build replaces it with what the harness uses.

   | Token | Names | Rendered for Claude Code |
   | --- | --- | --- |
   | `{{command:<name>}}` | A command of the workflow | `/<plugin>:<name>` |
   | `{{skill:<name>}}` | A skill of the workflow | `<plugin>:<name>` |
   | `{{agent:<name>}}` | A subagent of the workflow | `<plugin>:<name>` |
   | `{{harness:<key>}}` | A capability or a passage that belongs to one harness | The content of `adapters/<harness>/terms/<key>.md` |

   Each harness states its equivalent of a capability in its own `terms/<key>.md`. A token that resolves
   to nothing fails the build, so a harness cannot be added while a capability the content uses has no
   stated equivalent.

4. **A command is authored as a command ([OQ-04](../requirements/open-questions.md#oq-04)).** It is one
   file under `canonical/commands/`, apart from the skills under `canonical/skills/`. How a command is
   packaged is each harness's decision. Claude Code packages each one as a skill.

5. **The plugin is named `tightship` ([OQ-01](../requirements/open-questions.md#oq-01)).** The name is
   written in one place, `adapters/claude-code/plugin.json`, and repeated only in the catalog entry.

6. **The catalog is this repository.** `.claude-plugin/marketplace.json` sits at the root, names the
   catalog `atnexuslab`, and points its one entry at `./plugins/claude-code`. An adopter installs
   `tightship@atnexuslab`.

7. **Packaging is code, an adapter is data.** How a harness lays out its plugin is one module of the
   package `builder/`, named after the harness. What every harness shares — reading the pieces, adding
   frontmatter, writing and comparing a plugin directory — is a module of its own beside it. `build.py`
   only orchestrates them. An adapter directory holds only files its harness's module reads.

8. **The content scan has the shape of the build.** Each thing the scan looks for is one module of the
   package `scanner/`, and reading files line by line, which two of them share, is a module of its own
   beside them. `scan.py` only orchestrates them. The scan reads and never writes.

## Consequences

Easier:

- A piece is edited in one file, and the build carries it to every harness that has an adapter.
- Adding a harness adds an adapter directory and a packaging module, and touches no canonical file
  ([NFR-FLEX-07](../requirements/non-functional/flexibility.md#nfr-flex-07)).
- What an adopter receives is a directory in the repository: it is read in a pull request and installed
  from any branch before a release.

Harder:

- Every change to a piece is two changes in one commit: the canonical file and the generated one.
- Canonical content is not readable as the final text: a reference reads `{{command:spec}}`.

Accepted:

- Generated files live in git. The Build gate is what keeps them from drifting.
- Tokens are not rendered inside a term file, and there is no way to write a literal `{{`. Either is
  added when a piece needs it.

## Alternatives considered

- **The plugin at the repository root, with no build.** Rejected: the canonical content would be the
  delivered content, and it would hold tool names and namespaced references.
- **Building on the adopter's machine through a `command` plugin source.** Rejected: it runs a script of
  this repository at installation, which FR-INS-01.2 forbids, and it requires Python for an install that
  needs none.
- **Committing the generated plugin only on a release branch.** Rejected: it needs a release pipeline,
  breaks the rule that `main` receives merge commits from `develop`, and leaves no way to install what an
  adopter will get before it is released.
- **Symlinks from the plugin directory into `canonical/`.** Rejected: Claude Code refuses a symlink that
  leaves the plugin directory, and symlinks do not survive a Windows checkout by default.
- **Neutral prose instead of tokens.** Rejected: "the spec command" is not a name a harness resolves.
- **Bare command names such as `/spec`.** Rejected: a bare name resolves only while no other command
  uses it, and a machine that still has the pre-plugin install uses every one of them.
- **Commands authored as skills in `canonical/`.** Rejected: it erases a distinction the requirements
  make, and a harness that keeps commands apart would have to recover it.
- **A template engine.** Rejected: the repository installs nothing, and four token kinds need none.
