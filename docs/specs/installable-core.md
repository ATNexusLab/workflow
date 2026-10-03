# Epic 1 — Install the core: skills, commands and the verifier

> **Status:** published
> **Profile:** API
> **Module:** `canonical/`, `adapters/claude-code/`, `plugins/claude-code/`, `.claude-plugin/`, `build.py`, `builder/`, `scan.py`
> **Epic:** [#1](https://github.com/ATNexusLab/workflow/issues/1)
> **Requirements:** [FR-INS-01](../requirements/functional/install.md#fr-ins-01),
> [FR-SKL-01](../requirements/functional/skills.md#fr-skl-01),
> [FR-SKL-02](../requirements/functional/skills.md#fr-skl-02),
> [FR-SKL-03](../requirements/functional/skills.md#fr-skl-03),
> [FR-VER-01](../requirements/functional/verifier.md#fr-ver-01),
> [FR-VER-02](../requirements/functional/verifier.md#fr-ver-02),
> [NFR-MNT-01](../requirements/non-functional/maintainability.md#nfr-mnt-01),
> [NFR-FLEX-06](../requirements/non-functional/flexibility.md#nfr-flex-06),
> [NFR-SEC-01](../requirements/non-functional/security.md#nfr-sec-01),
> [NFR-SEC-02](../requirements/non-functional/security.md#nfr-sec-02),
> [BR-02](../requirements/business-rules.md#br-02),
> [BR-03](../requirements/business-rules.md#br-03)
> **Sprint:** [1](../roadmap/sprints/sprint-01.md)
> **Decision:** [ADR 0001](../decisions/0001-canonical-content-rendered-into-one-plugin-per-harness.md)

## Assumptions the spec rests on

Confirmed by the maintainer on 2026-10-02:

1. Canonical content, one adapter per harness, and a build whose output is committed
   ([ADR 0001](../decisions/0001-canonical-content-rendered-into-one-plugin-per-harness.md)).
2. A reference is a token, and a harness-native capability is a term each adapter states.
3. A command is authored as a command; the Claude Code adapter packages it as a skill.
4. The plugin is named `tightship` and the catalog `atnexuslab`. The name is written in
   `adapters/claude-code/plugin.json` and in the catalog entry; every other occurrence is rendered.
5. English content reaches further than the one command the SRS counts: `pr-review`, `spec-writing`,
   `spec`, and `epic` carry Portuguese.
6. `closeout` ships without its memory step; epic #3 restores it with the memory functions.

Decided without objection:

- The author is the organization, never a person.
- `version` is `0.1.0`. The release version policy belongs to epic #5.
- The install steps live in the root `README.md` until epic #5 writes the install guide.

## Acceptance Criteria

### Contract

There is no HTTP surface. The contract is what the adopter and the maintainer run.

| Operation | Invocation | Who | Idempotent |
| --- | --- | --- | --- |
| Add the catalog | `/plugin marketplace add ATNexusLab/workflow` | Adopter | Yes |
| Install the plugin | `/plugin install tightship@atnexuslab` | Adopter | Yes |
| Invoke a command | `/tightship:<command> <argument text>` | Adopter | Depends on the command |
| Load a skill | `tightship:<skill>` | The agent, or the adopter as `/tightship:<skill>` | Yes |
| Dispatch the verifier | subagent `tightship:adversarial-verifier` with one claim | The main agent | Yes |
| Build the plugin | `python3 build.py` | Maintainer | Yes |
| Check the build | `python3 build.py --check` | Maintainer | Yes |
| Scan the content | `python3 scan.py` | Maintainer | Yes |
| Scan for secrets | `git ls-files -z \| xargs -0 uvx --from detect-secrets==1.5.0 detect-secrets-hook` | Maintainer | Yes |

Both adopter operations have a shell form: `claude plugin marketplace add ATNexusLab/workflow` and
`claude plugin install tightship@atnexuslab`. Until the M1 release reaches `main`, the catalog is added
from a branch: `ATNexusLab/workflow#<branch>`.

### Request

**Repository layout**

```
.claude-plugin/marketplace.json
adapters/
  neutrality-terms.txt
  claude-code/
    plugin.json
    frontmatter.json
    terms/<key>.md
canonical/
  agents/adversarial-verifier.md
  commands/<name>.md
  skills/<name>/SKILL.md
  skills/spec-writing/templates.md
plugins/claude-code/
  .claude-plugin/plugin.json
  agents/adversarial-verifier.md
  skills/<name>/SKILL.md
  skills/spec-writing/templates.md
build.py
builder/
scan.py
tests/
README.md
```

**Canonical frontmatter**

| File | Field | Type | Required | Value |
| --- | --- | --- | --- | --- |
| `skills/<name>/SKILL.md` | `name` | string | Yes | The directory name |
| `skills/<name>/SKILL.md` | `description` | string | Yes | The baseline's, unchanged |
| `commands/<name>.md` | `description` | string | Yes | The baseline's, except `closeout`, `pr-review`, and `bootstrap` (rules 9, 10, and 13) |
| `commands/<name>.md` | `argument-hint` | string | Yes | The baseline's, except `pr-review` (rule 10) |
| `agents/adversarial-verifier.md` | `name` | string | Yes | `adversarial-verifier` |
| `agents/adversarial-verifier.md` | `description` | string | Yes | The baseline's, unchanged |

No other frontmatter field is canonical. A field only one harness reads comes from its adapter.

**`adapters/claude-code/plugin.json`** — copied to `plugins/claude-code/.claude-plugin/plugin.json`.

| Field | Type | Required | Value |
| --- | --- | --- | --- |
| `name` | string | Yes | `tightship` |
| `version` | string | Yes | `0.1.0` |
| `description` | string | Yes | `A development workflow for coding agents: skills, a command for each step of the development loop, and a read-only verifier.` |
| `author.name` | string | Yes | `ATNexusLab` |
| `license` | string | Yes | `MIT`, the license of the repository's `LICENSE` |
| `repository` | string | Yes | `https://github.com/ATNexusLab/workflow` |

**`.claude-plugin/marketplace.json`** — authored at the root, where Claude Code requires it.

| Field | Type | Required | Value |
| --- | --- | --- | --- |
| `name` | string | Yes | `atnexuslab` |
| `description` | string | Yes | `Plugins published by ATNexusLab.` |
| `owner.name` | string | Yes | `ATNexusLab` |
| `plugins[0].name` | string | Yes | Equal to `name` in `adapters/claude-code/plugin.json` |
| `plugins[0].source` | string | Yes | `./plugins/claude-code` |

**`adapters/claude-code/frontmatter.json`** — lines the build adds to a piece's frontmatter. The key is the
piece's path under `canonical/`, without the file name for a skill and without the extension otherwise.

```json
{
  "skills/grill-me": ["disable-model-invocation: true"],
  "agents/adversarial-verifier": ["tools: Read, Grep, Glob, Bash"]
}
```

**`adapters/claude-code/terms/`** — one file per `{{harness:<key>}}` the content uses.

| Key | Used by | Value |
| --- | --- | --- |
| `code-review` | `audit` | `` `/code-review` `` |
| `security-review` | `audit` | `` `/security-review` `` |
| `general-agent` | `audit`, `pr-review` | `` `general-purpose` `` |
| `exploration-agent` | `bootstrap` | `the **Explore** agent` |
| `area-file-loading` | `bootstrap` | `Claude Code loads an area's file when it works there` |
| `instruction-file-evolution` | `bootstrap` | The baseline passage of `bootstrap` step 0 from "Find every one" to "before touching it." |

**`adapters/neutrality-terms.txt`** — one Python regular expression per line, matched against every file
under `canonical/`. At M1 it holds the four product names and Claude Code's native names found at the
baseline; each later milestone adds its harness's native names.

```
(?i)claude
(?i)anthropic
(?i)cursor
(?i)antigravity
(?i)codex
(?i)openai
(?i)plan mode
(?i)explore\W{0,4}agent
/code-review
/security-review
`general-purpose`
`(Bash|Grep|Glob|Read|Edit|Write|WebFetch|WebSearch)`
```

### Response

| Operation | Exit | Output |
| --- | --- | --- |
| `python3 build.py` | `0` | `Built plugins/claude-code: 22 skills, 1 agent.` |
| `python3 build.py` | `1` | One line per error from the table in Errors; `plugins/claude-code/` is left as it was |
| `python3 build.py --check` | `0` | `plugins/claude-code is up to date.` |
| `python3 build.py --check` | `1` | One line per path that differs, then `Run python3 build.py and commit the result.` |
| `python3 scan.py` | `0` | `Scan passed: 0 harness terms, 0 personal identities, 0 environment files, 0 vault notes.` |
| `python3 scan.py` | `1` | One line per finding from the table in Errors |

### Roles and permissions

| Role | Permission | Note |
| --- | --- | --- |
| Adopter | None | Anyone who can reach the public repository installs |
| Maintainer | Write access to the repository | Runs the build and the scans |

---

## Business rules

### 1. Authorization

The product has no permission. Installation is open to anyone who reaches the repository, and the
harness shows its own review step before it installs. The plugin adds no check of its own.

Scenario: 1.

### 2. Installation through the harness only

- The adopter installs with two commands of Claude Code: add the catalog, install the plugin.
- No step runs a file of this repository.
- After installation, `claude plugin list` shows `tightship@atnexuslab` at version `0.1.0`, enabled.
- The plugin declares no user configuration and ships no hook, so an install from the shell and an
  interactive install produce the same result.
- A machine that still has the pre-plugin install keeps its own copies. Every component of the plugin is
  reached by its namespaced name, so both resolve. Removing the old copies is the migration of epic #5.

Scenarios: 1, 2.

### 3. Skills

- The plugin delivers the 14 skills of FR-SKL-01, each with its supporting files. At the baseline one
  skill has one: `spec-writing/templates.md`.
- `grill-me` is offered only to the adopter: it is absent from the skills the agent can load on its own.

Scenarios: 3, 4, 5.

### 4. Commands

- The plugin delivers the 8 commands of FR-SKL-02. In Claude Code each is a skill of the plugin, invoked
  as `/tightship:<name>`.
- The text the adopter types after the name reaches the command where it writes `$ARGUMENTS`.
- A command stays invocable by the agent, as at the baseline.

Scenarios: 6, 7.

### 5. References resolve

- The canonical content writes a reference as a token: `{{command:<name>}}`, `{{skill:<name>}}`, or
  `{{harness:<key>}}`.
- The build renders `{{command:<name>}}` as `/tightship:<name>`, `{{skill:<name>}}` as
  `tightship:<name>`, and `{{harness:<key>}}` as the content of `adapters/claude-code/terms/<key>.md`
  without its final line break.
- A `{{command:…}}` must name a file in `canonical/commands/`, a `{{skill:…}}` a directory in
  `canonical/skills/`, and a `{{harness:…}}` a file in the adapter's `terms/`. Any other text between
  `{{` and `}}` resolves to nothing.
- A token that resolves to nothing fails the build with:
  > "`<file>:<line>: <token> resolves to nothing`"
- A key in `frontmatter.json` that names no canonical piece fails the build with:
  > "`adapters/claude-code/frontmatter.json: "<key>" names no canonical piece`"
- A key in `frontmatter.json` whose piece opens with no frontmatter fails the build with:
  > "`adapters/claude-code/frontmatter.json: "<key>" has no frontmatter`"
- A command with the name of a skill fails the build, since Claude Code packages both as the skill of
  that name:
  > "`canonical/commands/<name>.md: a skill is already named "<name>"`"

Scenarios: 8, 9, 10.

### 6. Verifier

- The plugin delivers the verifier as the subagent `tightship:adversarial-verifier`.
- Its tools are exactly `Read`, `Grep`, `Glob`, and `Bash`. The list comes from the adapter; the
  canonical text names no tool.
- Dispatched with one claim, it returns `verdict`, `attacks_run`, `confidence`, `reason`, and, when
  refuted, `to_pass`.
- It leaves the working tree as it found it.

Scenarios: 11, 12, 13, 14.

### 7. One authored copy

- A piece is edited only under `canonical/`. `plugins/claude-code/` is generated and never edited.
- The build writes `plugins/claude-code/` whole: a file the build does not produce is removed.
- The build renders everything before it writes anything. On any error it writes nothing.
- `python3 build.py --check` compares the committed directory with a fresh build and fails on any
  difference, one line per path:
  > "`plugins/claude-code/<path>: differs from a fresh build`"
  > "`plugins/claude-code/<path>: is not produced by the build`"
  > "`plugins/claude-code/<path>: is missing`"

  followed by:
  > "`Run python3 build.py and commit the result.`"
- The same check fails when the catalog entry and the plugin manifest disagree on the name:
  > "`.claude-plugin/marketplace.json: plugin entry "<entry>" does not match "<name>" in adapters/claude-code/plugin.json`"

Scenarios: 15, 16, 17.

### 8. Harness-neutral canonical content

- No file under `canonical/` matches a line of `adapters/neutrality-terms.txt`.
- `python3 scan.py` reports each match as:
  > "`<file>:<line>: harness term "<match>" (NFR-FLEX-06)`"
- A harness-native name found after M1 is added to the list in the commit that removes it from the
  content.

Scenarios: 18, 19.

### 9. Content carried from the baseline

Each of the 23 pieces carries the text of baseline `519cc2a`, with these changes and no other:

| Piece | Change |
| --- | --- |
| Every piece | A reference to a command or a skill becomes a token |
| `grill-me` | `disable-model-invocation` moves to the adapter |
| `adversarial-verifier` | `tools` moves to the adapter; "Use `Bash` for read-only evidence" becomes "Run commands for read-only evidence" |
| `audit` | `` `general-purpose` ``, `/security-review`, and `/code-review` become terms |
| `pr-review` | `` `general-purpose` `` becomes a term |
| `bootstrap` | The sentence on area files, the step 0 passage on instruction files, and "the **Explore** agent" become terms. The step 0 heading reads "An `AGENTS.md`, or an instruction file of the harness's own, already exists". A license step is added (rule 13) |
| `spec` | The example `.claude/context/` is removed from "Where specs live" |
| `closeout` | Step 5 "Memory" and the `Memory` line of the output block are removed. The description becomes `Check what the delivery gate does not — surfaces, docs, traceability, security debt — before the commit` |
| `pr-review`, `spec-writing`, `spec`, `epic` | Translated (rule 10) |

Scenario: 20.

### 10. English content

Everything under `plugins/claude-code/` is written in English.

- `pr-review` is translated whole. Its description becomes
  `Review someone else's PR — a briefing (what for / what / how) plus explained findings, without what another PR already solved`
  and its argument hint `[PR number or URL] [--only sec|perf|arch|maint]`. Where the baseline fixes the
  output to Portuguese, the briefing and the ready-to-paste comments follow the repository's doc
  language.
- The spec templates and every place that quotes them use these names:

  | Baseline | Canonical |
  | --- | --- |
  | `Status: rascunho` · `fechada` · `publicada` | `Status: draft` · `closed` · `published` |
  | `Perfil` · `Módulo` · `Requisitos` | `Profile` · `Module` · `Requirements` |
  | `Regras de Negócio` | `Business rules` |
  | `Cenários de Aceite (Gherkin)` | `Acceptance scenarios (Gherkin)` |
  | `Erros` · `Efeitos Colaterais` | `Errors` · `Side effects` |
  | `Impacto na arquitetura` · `Impacto no modelo de dados` | `Architecture impact` · `Data model impact` |
  | `Fora de Escopo` | `Out of scope` |
  | `Quebra em Tasks` · `Depende de` | `Task breakdown` · `Depends on` |
  | `Dado` · `E` · `Quando` · `Então` | `Given` · `And` · `When` · `Then` |
  | `a definir` · `talvez` | `to be defined` · `maybe` |

- The rule that a spec follows the repository's doc language stays. In a repository whose docs are not in
  English, the names above are written in that language, and `epic` reads the status and the headings in
  that language.
- The issue bodies `epic` builds are templated in English and filled in the repository's doc language.

Scenario: 21.

### 11. No personal identity in what the plugin installs

- `python3 scan.py` searches every file under `plugins/claude-code/` for:
  - an email address;
  - a home-directory path: `/Users/<name>`, `/home/<name>`, or `<drive>:\Users\<name>`;
  - every author and committer email of this repository's history, and every word of 4 or more letters
    of every author and committer name, matched as a whole word, case-insensitive.
- Each match is reported as:
  > "`<file>:<line>: personal identity "<match>" (NFR-SEC-01)`"
- The names are read from `git log` when the scan runs. No file of the repository lists them.
- At session start the plugin places in context only the names and descriptions of its skills and of the
  verifier. They are files the scan covers, and the plugin ships no hook.

Scenarios: 22, 23.

### 12. No secret and no vault content in the repository

- The secret scan runs over every tracked file and exits `1` on a finding. Its messages are
  detect-secrets' own.
- `python3 scan.py` fails on a tracked file named `.env` or `.env.<suffix>`, other than `.env.example`
  and `.env.template`:
  > "`<file>: environment file with values is tracked (NFR-SEC-02)`"
- `python3 scan.py` fails on a tracked file named `mem-<digits>-<slug>.md`:
  > "`<file>: vault note is tracked (NFR-SEC-02)`"
- Both scans are gates of every delivery, so every commit passes them before it exists.

Scenarios: 24, 25.

### 13. `bootstrap` settles the license

The baseline's `bootstrap` never asks about a license. The carried command does:

- The command produces a fifth thing: the repo's `LICENSE`, or the recorded decision to have none. Its
  description becomes
  `Set up this repo for the workflow — its AGENTS.md, GitHub Project, .vscode/, global docs, and license`.
- The license and the copyright holder are settled in step 2, with the other setup decisions. Both are
  the choice of whoever runs the command: it never picks them and never carries them over from another
  repository.
- A `License` step is added after `Docs`, and the later steps are renumbered:
  - A `LICENSE` that already exists is kept and never overwritten. The command reports which license it
    is.
  - With no `LICENSE`, the command writes the chosen license's text at the repository root, with the
    current year and the chosen holder filled in. The text comes from GitHub's license API
    (`gh api licenses/<key>`) or, for a license it does not list, from the text its steward publishes.
    It is never written from recollection.
  - Having no license is a valid choice. No file is written.
- The `Validate` step checks that `LICENSE` exists at the root, or that the choice was to have none.
- The output block gains the line:
  > "`- License:      [<SPDX id> · <holder> / kept: <SPDX id> / none, by decision]`"

Scenarios: 26, 27, 28.

### 14. Persistence and audit

- **Files changed:** the build writes only `plugins/claude-code/`. The scans write nothing.
- **On the adopter's machine:** the plugin writes nothing. Claude Code records the install in its own
  settings and cache.
- **Audit:** N/A — no operation of the product has an actor to record beyond git's own history.
- **Events and integrations:** N/A — nothing is emitted.

Scenarios: 9, 15.

---

## Errors

| Error | Exit | When | Message |
| --- | --- | --- | --- |
| Unresolved reference | `1` | A token in `canonical/` names no command, no skill, and no term | "`<file>:<line>: <token> resolves to nothing`" |
| Unknown piece | `1` | A key of `frontmatter.json` matches no canonical piece | "`adapters/claude-code/frontmatter.json: "<key>" names no canonical piece`" |
| No frontmatter | `1` | A key of `frontmatter.json` names a piece that opens with no frontmatter | "`adapters/claude-code/frontmatter.json: "<key>" has no frontmatter`" |
| Name taken | `1` | A command has the name of a skill | "`canonical/commands/<name>.md: a skill is already named "<name>"`" |
| Out of date | `1` | `--check` finds a path that differs, is extra, or is missing | "`plugins/claude-code/<path>: differs from a fresh build`" · "`…: is not produced by the build`" · "`…: is missing`" |
| Name mismatch | `1` | `--check` finds the catalog entry and the manifest with different names | "`.claude-plugin/marketplace.json: plugin entry "<entry>" does not match "<name>" in adapters/claude-code/plugin.json`" |
| Harness term | `1` | A file under `canonical/` matches a neutrality term | "`<file>:<line>: harness term "<match>" (NFR-FLEX-06)`" |
| Personal identity | `1` | A file under `plugins/claude-code/` matches an identity pattern | "`<file>:<line>: personal identity "<match>" (NFR-SEC-01)`" |
| Environment file | `1` | A tracked file is an environment file with values | "`<file>: environment file with values is tracked (NFR-SEC-02)`" |
| Vault note | `1` | A tracked file is named as a vault note | "`<file>: vault note is tracked (NFR-SEC-02)`" |

## Side effects

- **Persistence:** `python3 build.py` replaces `plugins/claude-code/`. Nothing else is written.
- **Concurrency:** N/A — one maintainer runs the build, and git settles two edits of the same file.
- **Transaction:** the build renders every file in memory and writes only when no error was found.

---

## Acceptance scenarios (Gherkin)

Authorization denied has no scenario: rule 1 defines no permission.

### Scenario 1 — Install from the catalog (happy path)

```gherkin
Given a machine with Claude Code 2.1.287 and git
And the plugin not installed
When the adopter runs `/plugin marketplace add ATNexusLab/workflow`
And runs `/plugin install tightship@atnexuslab` and picks a scope
Then `claude plugin list` shows `tightship@atnexuslab` at version `0.1.0`, enabled
```

### Scenario 2 — No installer script

```gherkin
Given the install steps in `README.md`
When each step is read
Then every step is a command of Claude Code or of git
And no step runs a file of this repository
```

### Scenario 3 — The skills are listed

```gherkin
Given the plugin installed
When the adopter runs `claude plugin details tightship`
Then the component inventory lists each of the 14 skills of FR-SKL-01
```

### Scenario 4 — A supporting file is readable

```gherkin
Given the plugin installed
When the agent loads `tightship:spec-writing` and reads `templates.md` from the skill's directory
Then the read returns the templates
```

### Scenario 5 — `grill-me` waits for the adopter

```gherkin
Given a session in which the adopter has not typed `/tightship:grill-me`
When the skills the agent can load on its own are listed
Then `tightship:grill-me` is not among them
And when the adopter types `/tightship:grill-me`, the agent runs a `tightship:grilling` session
```

### Scenario 6 — The commands are listed

```gherkin
Given the plugin installed
When the adopter types `/tightship:` in a session
Then each of the 8 commands of FR-SKL-02 is offered
```

### Scenario 7 — A command receives its argument

```gherkin
Given the plugin installed
When the adopter runs `/tightship:sprint plan`
Then the agent follows the `plan` path of the sprint command
```

### Scenario 8 — Every reference resolves

```gherkin
Given `plugins/claude-code/` built from `canonical/`
When it is searched for `{{`
Then the search finds 0 matches
And every `/tightship:<name>` and `tightship:<name>` written in it names a directory of `plugins/claude-code/skills/`
```

### Scenario 9 — An unresolved reference stops the build

```gherkin
Given a canonical file that writes `{{command:epik}}` on line 8
When the maintainer runs `python3 build.py`
Then it exits 1 with "<file>:8: {{command:epik}} resolves to nothing"
And `plugins/claude-code/` is unchanged
```

### Scenario 10 — An unknown piece in the adapter stops the build

```gherkin
Given `frontmatter.json` with the key `agents/adversarial-verifer`
When the maintainer runs `python3 build.py`
Then it exits 1 with "adapters/claude-code/frontmatter.json: "agents/adversarial-verifer" names no canonical piece"
And `plugins/claude-code/` is unchanged
```

### Scenario 11 — The verifier is listed

```gherkin
Given the plugin installed
When the adopter runs `claude plugin details tightship`
Then the component inventory lists the agent `adversarial-verifier`
```

### Scenario 12 — The verifier returns a verdict

```gherkin
Given the plugin installed
When the main agent dispatches `tightship:adversarial-verifier` with one claim
Then it returns `verdict`, `attacks_run`, `confidence`, and `reason` for that claim
```

### Scenario 13 — The verifier has no editing tool

```gherkin
Given `plugins/claude-code/agents/adversarial-verifier.md`
When its frontmatter is read
Then `tools` is exactly `Read, Grep, Glob, Bash`
```

### Scenario 14 — The verifier leaves the tree as it was

```gherkin
Given a repository with a clean working tree
When the verifier is dispatched and returns
Then `git status --porcelain` prints nothing
```

### Scenario 15 — One edit reaches the plugin (happy path)

```gherkin
Given a change to one line of `canonical/skills/grilling/SKILL.md`
When the maintainer runs `python3 build.py`
Then it exits 0 with "Built plugins/claude-code: 22 skills, 1 agent."
And the commit holds 1 changed file under `canonical/` and the same change under `plugins/claude-code/`
And `python3 build.py --check` exits 0 with "plugins/claude-code is up to date."
```

### Scenario 16 — A stale plugin fails the check

```gherkin
Given a change under `canonical/` with `plugins/claude-code/` not rebuilt
When the maintainer runs `python3 build.py --check`
Then it exits 1 with "plugins/claude-code/<path>: differs from a fresh build"
And "Run python3 build.py and commit the result."
```

### Scenario 17 — A catalog entry with another name fails the check

```gherkin
Given `.claude-plugin/marketplace.json` whose entry is named `tight-ship`
When the maintainer runs `python3 build.py --check`
Then it exits 1 with ".claude-plugin/marketplace.json: plugin entry "tight-ship" does not match "tightship" in adapters/claude-code/plugin.json"
```

### Scenario 18 — The canonical content names no harness (happy path)

```gherkin
Given the canonical content of this epic
When the maintainer runs `python3 scan.py`
Then it exits 0 with "Scan passed: 0 harness terms, 0 personal identities, 0 environment files, 0 vault notes."
```

### Scenario 19 — A harness name fails the scan

```gherkin
Given a canonical file that writes "Claude Code" on line 11
When the maintainer runs `python3 scan.py`
Then it exits 1 with "<file>:11: harness term "Claude" (NFR-FLEX-06)"
```

### Scenario 20 — The baseline's text is carried

```gherkin
Given baseline `519cc2a` and `plugins/claude-code/` built
When each of the 23 pieces is compared with its baseline file
Then every difference is a change listed in rule 9, rule 10, or rule 13
```

### Scenario 21 — The delivered content is English

```gherkin
Given `plugins/claude-code/` built
When it is searched for each baseline name in the table of rule 10
Then the search finds 0 matches
And `skills/pr-review/SKILL.md` carries the description of rule 10
```

### Scenario 22 — The plugin carries no personal identity (happy path)

```gherkin
Given `plugins/claude-code/` built
When the maintainer runs `python3 scan.py`
Then it reports 0 personal identities
```

### Scenario 23 — A personal identity fails the scan

```gherkin
Given a canonical file that writes `/Users/someone/notes` on line 4
And `plugins/claude-code/` rebuilt from it
When the maintainer runs `python3 scan.py`
Then it exits 1 with "<file>:4: personal identity "/Users/someone" (NFR-SEC-01)"
```

### Scenario 24 — A secret or an environment file fails the gates

```gherkin
Given a tracked file that holds an AWS access key
When the secret scan runs
Then it exits 1
And given a tracked file named `.env.local`, `python3 scan.py` exits 1 with ".env.local: environment file with values is tracked (NFR-SEC-02)"
```

### Scenario 25 — A vault note fails the scan

```gherkin
Given a tracked file named `mem-0001-example.md`
When the maintainer runs `python3 scan.py`
Then it exits 1 with "mem-0001-example.md: vault note is tracked (NFR-SEC-02)"
```

### Scenario 26 — `bootstrap` asks for the license (happy path)

```gherkin
Given a repository with no `LICENSE`
When the adopter runs `/tightship:bootstrap`
Then the license and its copyright holder are among the decisions asked before anything is written
And after the adopter chooses `MIT` and a holder, `LICENSE` at the root holds the MIT text with the current year and that holder
And the output block reads "- License:      MIT · <holder>"
```

### Scenario 27 — An existing license is kept

```gherkin
Given a repository whose `LICENSE` holds the Apache-2.0 text
When the adopter runs `/tightship:bootstrap`
Then `LICENSE` is unchanged
And the output block reads "- License:      kept: Apache-2.0"
```

### Scenario 28 — No license, by decision

```gherkin
Given a repository with no `LICENSE`
When the adopter runs `/tightship:bootstrap` and chooses to have no license
Then no `LICENSE` is written
And the output block reads "- License:      none, by decision"
```

---

## Architecture impact

- **Solution strategy:** "How the canonical content becomes one plugin per harness" moves from "Not
  decided" to "Decided", with a link to ADR 0001.
- **Building blocks**, new, all M1: Canonical content (`canonical/`) · Claude Code adapter
  (`adapters/claude-code/`) · Build (`build.py`) · Content scan (`scan.py`) · Claude Code plugin
  (`plugins/claude-code/`, generated) · Catalog (`.claude-plugin/marketplace.json`).
- **Runtime:** two scenarios — the maintainer builds and commits; the adopter adds the catalog and
  installs.
- **Deployment:** the adopter's Claude Code clones this repository as a catalog and copies
  `plugins/claude-code/` into its plugin cache. Adopters install from `main`.
- **Repository contract:** the `Architecture` section of `AGENTS.md` is written from ADR 0001, and its
  `Commands` table gains the gates as each is first run: static analysis, type checking, formatting,
  build, tests, content scan, secret scan, and plugin validation.

## Data model impact

N/A — this epic stores nothing. The state of an Install's optional components arrives with epic #2.

## Out of scope

- **The contract and the mechanism that turns an optional component on or off** — epic #2.
- **`{{agent:<name>}}`** — ADR 0001 defines it, and no piece of this epic refers to the verifier. Epic #2
  builds it with the contract, which does.
- **The memory functions and the memory step of `closeout`** — epic #3.
- **The status line** — epic #4.
- **Update, uninstall, migration from the pre-plugin install, the install guide, reduced mode, the three
  operating systems, and the release version policy** — epic #5.
- **The minimum supported version of Claude Code** ([OQ-07](../requirements/open-questions.md#oq-07)) —
  this epic is verified on 2.1.287 only; the M1 release settles the minimum in epic #5.
- **Why an adopter's agent took them for the maintainer**
  ([OQ-02](../requirements/open-questions.md#oq-02)) — it needs a reproduction on the adopter's machine.
  This epic closes the path the product controls.
- **Cursor, Antigravity CLI, and Codex**, and the native names of each in the neutrality list — M2 to M4.

## Task breakdown

| # | Issue | Title | Scope | Acceptance criterion | Depends on |
| --- | --- | --- | --- | --- | --- |
| 1 | [#8](https://github.com/ATNexusLab/workflow/issues/8) | Build the plugin from canonical content and install the verifier | `build.py` with `--check` and the frontmatter additions · `adapters/claude-code/plugin.json` and `frontmatter.json` · `.claude-plugin/marketplace.json` · `canonical/agents/` · `plugins/claude-code/` · `tests/` · install steps in `README.md` · the gates in `AGENTS.md` | Scenarios 1, 2, 10, 11, 12, 13, 14, 16, 17 | — |
| 2 | [#9](https://github.com/ATNexusLab/workflow/issues/9) | Scan the content for harness terms, personal identity, and secrets | `scan.py` · `adapters/neutrality-terms.txt` · `tests/` · the two scan gates in `AGENTS.md` | Scenarios 18, 19, 22, 23, 24, 25 | 1 |
| 3 | [#10](https://github.com/ATNexusLab/workflow/issues/10) | Carry the 14 skills and the 8 commands | Token rendering in `build.py` · `adapters/claude-code/terms/` · `canonical/skills/` · `canonical/commands/` · `plugins/claude-code/skills/` · `tests/` | Scenarios 3, 4, 5, 6, 7, 8, 9, 15, 20, 26, 27, 28 | 2 |
| 4 | [#11](https://github.com/ATNexusLab/workflow/issues/11) | Translate the Portuguese content to English | `canonical/commands/pr-review.md`, `spec.md`, `epic.md` · `canonical/skills/spec-writing/` · `plugins/claude-code/skills/` | Scenario 21 | 3 |
