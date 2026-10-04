---
description: Set up this repo for the workflow — its AGENTS.md, GitHub Project, .vscode/, global docs, and license
argument-hint: "[optional notes about the project]"
---

Set up the repository for the workflow, layered on top of the global contract, for: $ARGUMENTS

This command produces five things, each created on first run and realigned on every later run:

1. The repo's `AGENTS.md` files: one at the root, plus one per area (`apps/<app>/`, a monorepo
   workspace) that has its own stack, gates, or conventions — {{harness:area-file-loading}}.
   The area file has the same sections as the root, scoped to the area, and never repeats
   or contradicts the root.
2. The repo's GitHub Project, where the backlog lives.
3. `.vscode/`, the editor setup the project needs.
4. The docs skeleton from `{{skill:project-docs}}`: `docs/README.md`, `docs/architecture/`, `docs/data-model/`,
   their diagrams, and the local docs site.
5. The repo's `LICENSE`, or the recorded decision to have none.

It does not move code or open an ADR — a cross-cutting decision that comes out of this belongs to
`{{command:spec}}`. The roadmap and sprints belong to `{{command:sprint}}`.

## 0. Which of the three jobs this is

Decide before reading anything else; the rest of the command changes with the answer.

- **An `AGENTS.md`, or an instruction file of the harness's own, already exists** → **evolution.** {{harness:instruction-file-evolution}}
  Never overwrite a file that may carry a rule tuned by hand.
- **The repo has code** → **detection.** The architecture is *read and recorded as it is*, not as it
  should be. A divergence you find is a note in the file, never a rewrite of the code.
- **The repo is empty** → **decision, made with me.** There is nothing to detect and nothing to
  default: the stack, the tooling, the repo shape, and the architecture are my choices. You never pick
  them yourself, never carry them over from another repository on this machine, and never start from a
  reference pattern. `Commands` only exists once something is there to run — what does not run yet is
  recorded as a declared pending, never as an invented command.

## 1. Detect (the repo-with-code path)

Read what this repo actually has: its dependency manifest and lockfile, its toolchain, formatter, and
type-checker config, its container and orchestration files, its CI workflows, its migration directory,
and the top-level source layout. Every ecosystem names these differently — find the names, never
assume them. Infer stack, package manager, and toolchain from what you found.

Two things usually asked that the environment answers: **branches** (`git branch -r`, plus protection
via `gh api`) and the **project's doc language** (the README and the commit subjects).

For the architecture itself, read it with `{{skill:architecture-reading}}` — its passes, in its order. If the
codebase is large or unfamiliar, dispatch {{harness:exploration-agent}} with that same lens.

## 2. Agree before writing

**Evolution and detection** — run a `{{skill:grilling}}` session: the code answers the facts, so decide what it
settles and state the assumptions this `AGENTS.md` rests on — the ones that change the file if they are
wrong. Only what I contest becomes a question. Typically shape-changing here: the intended architecture
when the code does not reveal it, a protected branch that is convention rather than configuration, and
the doc language when the repo is mixed.

**Decision** — no assumptions list. List the decisions the file needs (stack, repo shape, architecture,
branches, language), then take them **one at a time**: the options that fit the requirements, each
with its trade-off, and I choose. A decision I have not made stays open and goes to `Open` in the
output — it is never filled in to complete the file.

**In every mode**, the same step also settles the setup in §4–§7: the branch model (an integration
branch plus `main`, or `main` alone), the sprint length, the label set, the `.vscode/` contents, and —
when the repo has no `LICENSE` — the license and its copyright holder.
These are decisions or assumptions like any other — nothing in §4–§7 runs before they close. The license
and the holder are always my choice: you never pick them and never carry them over from another
repository.

**Nothing is written until this step closes**, in every mode.

## 3. Write it

Additive to the global contract — **never repeat** what is already global.

- **Stack** — languages, frameworks, package manager, as confirmed.
- **Language & scripts** — required, never inferred from another repo: the language application code is
  written in, and the language a new script is written in here. The global contract mandates neither, so
  a repo that does not state them has no rule at all. Detection reads what the repo already uses;
  decision asks me.
- **Conventions** — the stack-specific rules that only hold here: how the entry point is wired, how
  styles are split, how the dev stack is composed. Only what this repo does or what I decided — never a
  convention carried over from another project.
- **Commands** — the repo's actual gates, each as its exact invocation, discovered from its own
  config and task runner: static analysis, type checking, formatting, build, tests, and how to run it.
  Not every language has all of them — mark the absent ones `n/a` explicitly, because a gate missing
  silently reads as a gate that passes. These are the definition-of-done gates every delivery runs.
- **Architecture** — layers, module boundaries, where each kind of code lives, and the data flow —
  written so a reader can *check* it: which layer may import which, and where a new file of each kind
  goes. This is the section the whole workflow enforces and `{{command:audit}}` measures against, so prose that
  cannot be violated is prose that cannot be enforced. It records what the code does or what I chose
  in step 2 — no architectural pattern is a default.
- **Branches** — protected names, the integration branch every PR targets, and what reaches `main`.
- **Language** — chat/doc language for this project (code stays English).
- **Gotchas** — only what was **observed** in this repo. A predicted problem is not a gotcha.

## 4. GitHub Project

Look before creating: `gh project list --owner <owner>` and the repo's linked projects. Reuse a project
that already serves this repo; never create a second one.

- **Project** — titled after the repo, linked to it (`gh project create`, `gh project link`).
- **Status** — exactly Backlog (GRAY) · Todo (GREEN) · In Progress (YELLOW) · In Review (BLUE) ·
  Staging (ORANGE) · Done (PURPLE). Staging holds what is merged into the integration branch and waits
  for the release. `gh project create` makes only three options, so set all six with the
  `updateProjectV2Field` GraphQL mutation — `singleSelectOptions` replaces the whole list.
- **Sprint** — an Iteration field, created with the `createProjectV2Field` GraphQL mutation,
  `dataType: ITERATION`, and the sprint length agreed in step 2.
- **Labels** — `epic`, one per change type the repo's commits use (`feat`, `fix`, `chore`, `docs`, …),
  `security-debt`, `requirement-change`, and one `area:<module>` per module of the Architecture section. Reuse what exists;
  create only what step 2 agreed.
- **Branches** — create the integration branch from `main` if it is missing, and push it.

Workflows and views are mine to configure — the API cannot edit them — so the output names the workflow
settings the flow needs: "Item closed" → Done, and "Auto-archive items" with the filter `is:closed`.
"Pull request linked to issue" → In Review is named only when `main` is the sole branch: GitHub reads a
closing keyword only in a PR into the default branch, so a PR into the integration branch links no
issue and the workflow never fires. There, an issue's In Review and Staging are set with
`gh project item-edit`.

## 5. `.vscode/`

Only what serves this project, in its stack, for anyone who clones it — never a personal preference
(theme, font, keymap).

- `extensions.json` — `recommendations` for the stack's language server, formatter, and linter, plus
  `hediet.vscode-drawio` for the diagrams.
- `settings.json` — only what the repo's own gates need in the editor: format on save with the repo's
  formatter, the linter the gates run, file associations the stack needs.
- `tasks.json` — `docs: serve` for the local docs site, plus the gates when running them from the
  editor is useful; each gate task is a command already recorded in `Commands`.
- The repo's `.gitignore` must not ignore `.vscode/`.

## 6. Docs

The structure and templates are `{{skill:project-docs}}`. Written from the requirements, the ADRs, and — in
detection — the code:

- `docs/README.md` — the map of the documentation and how to open the local site.
- `docs/architecture/` — arc42 with C4 diagrams, covering the whole system from infrastructure to
  interface; its content inferred from the Architecture section and the ADRs, each element marked with
  the milestone that builds it.
- `docs/data-model/` — conceptual, logical, and physical. Its method is `{{skill:database-design}}`.
- Diagrams as `docs/diagrams/*.drawio.svg`.
- The local docs site: `zensical.toml`, `site/` in `.gitignore`, and no deploy workflow.

An existing single-file doc (`docs/requirements.md`, `docs/architecture.md`, …) is split into its folder,
its content kept, and every link to it updated.

In evolution, realign them with what changed; a doc that contradicts the code or an ADR is fixed here.

## 7. License

- **A `LICENSE` already exists** → keep it and never overwrite it. Report which license it is.
- **No `LICENSE`, and I chose a license in step 2** → write its text to `LICENSE` at the repository
  root, with the current year and the chosen holder filled in. The text comes from GitHub's license API
  (`gh api licenses/<key>`) or, for a license it does not list, from the text its steward publishes. It
  is never written from recollection.
- **No `LICENSE`, and I chose to have none** → write no file. Having no license is a valid choice.

## 8. What never goes in

- **An aspirational rule.** A rule the repo does not follow today is a lie the next session enforces.
  Record the reality, and put the intent in the requirements or an ADR instead.
- Anything already in the global contract, or already in a skill — reference it, do not restate it.
- A command that was not run.
- A catalogue of what was considered and rejected. The file says what to use and which behavior is
  forbidden; a discarded library belongs in its ADR's `Alternatives considered`.
- Another tool's instruction file. `.github/copilot-instructions.md` and its mirrors are not written,
  and in evolution they are removed: agent instructions live only in `AGENTS.md`.

## 9. Validate

Run **every** command recorded in `Commands` and report its exit code. One that fails is removed or
kept with the failure stated in the file — never left looking green; one marked `n/a` says why. Then
check: nothing duplicates the global contract, no placeholder or TODO survives, and the frontmatter
and structure are clean.

Then check the setup: `gh project field-list` shows Status with its six options and the `Sprint`
iteration, `gh label list` holds the agreed labels, the integration branch exists on the remote, and
each `.drawio.svg` opens in the drawio editor, and `zensical build` exits 0.

Then check the license: `LICENSE` exists at the root, or the choice was to have none.

## Output

```
Bootstrap:
- Written:      [paths]
- Mode:         [new / evolution — what changed]
- Stack:        [languages, package manager, toolchain]
- Architecture: [one line]
- Commands:     [each, with exit code]
- Project:      [url · Status ok · Sprint <length> · labels created/reused · workflows for you to set]
- Editor:       [.vscode files written]
- Docs:         [docs/README.md · architecture/ · data-model/ · diagrams · zensical.toml]
- License:      [<SPDX id> · <holder> / kept: <SPDX id> / none, by decision]
- Open:         [what is declared pending / none]
```
