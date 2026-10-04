---
name: project-docs
description: Use when creating or updating a project's docs under docs/ — the folder structure, the global docs (requirements, architecture, data model, roadmap), their diagrams (.drawio.svg), and the local docs site (Zensical). Templates and what each doc owns.
---

# Project Docs

Everything under `docs/` is written for people. Big files do not get read, so every doc is a **folder of
small files**, one subject each, with a `README.md` as the folder's index. GitHub shows that `README.md`
when the folder opens, VS Code shows the tree, and the local docs site turns the same folders into a
sidebar with search. Nothing is written twice for any of the three.

## Structure

```
docs/
  README.md                    map of the documentation; how to open the local site
  requirements/                the SRS — `tightship:requirements-engineering`
  architecture/                arc42 sections, C4 diagrams — see `architecture/`
    README.md                  goals, context and scope, solution strategy, and the index
    building-blocks/           the system decomposed, one file per building block
    runtime/                   scenarios, end to end across every layer
    deployment.md              where every building block runs
    concepts/                  crosscutting concepts, one file each
    risks.md                   risks and technical debt
  data-model/
    README.md                  conceptual model and the entity index
    access-patterns.md
    <entity>.md                logical model of one entity
    storage.md                 physical: tables, indexes, migrations — or files on disk
  roadmap/
    README.md                  milestones → epics, and requirement coverage
    sprints/sprint-NN.md       one sprint: plan, baseline, result
  specs/<epic>/<feature>.md    one feature in depth
  decisions/NNNN-<slug>.md     ADRs
  diagrams/<topic>.drawio.svg
```

- **One file, one subject**, readable in one sitting. A file that grows a second subject splits.
- **Every folder has a `README.md`**: what the folder holds and a linked list or table of its files.
- **Links are relative** (`../architecture/README.md`), so they work on GitHub, in VS Code, and on the
  site.
- A level the project does not have is one line in the parent `README.md` saying why, not an empty file.

## What each doc owns — one source per fact

| Doc | Owns | Never holds |
|---|---|---|
| `requirements/` | The versioned SRS: requirement IDs, attributes, acceptance criteria | Design |
| `architecture/` | The map: what exists, how it talks, which milestone builds it | The checkable import rules — `AGENTS.md` → Architecture |
| `data-model/` | Entities, relations, invariants, storage | Feature behavior |
| `roadmap/` | Milestones → epics, requirement coverage, each sprint's plan and dated result | Item status — issues, the GitHub Project, and GitHub Milestones own it |
| `decisions/` | Why a cross-cutting choice was made | The current map |
| `specs/` | One feature in depth | Anything global |

A doc that restates another is replaced by a link. `tightship:technical-writing` still decides whether a doc should
exist at all.

## `architecture/`

**Standard:** the section structure of **arc42**, drawn with the **C4 model**. Both are independent of
any architecture style.

**The content is inferred, never prescribed.** The building blocks, scenarios, and concepts come from the
architecture decided in the repo — its `AGENTS.md` Architecture section, its ADRs, and in detection its
code — and are named with that architecture's own vocabulary. This skill names no style, no layer, and no
kind of component. **Coverage is the whole system,** from infrastructure to interface: every part the
system has is documented somewhere below, and a section it lacks is one line in `README.md` saying why.

| arc42 section | Where |
|---|---|
| 1. Introduction and goals | `README.md` — the goal in one paragraph; quality goals link to `../requirements/` NFRs |
| 2. Constraints | a link to `../requirements/overview.md` |
| 3. Context and scope | `README.md` — C4 context diagram, and every external actor and system with what flows |
| 4. Solution strategy | `README.md` — the decided style and key technology choices, each linking its ADR |
| 5. Building block view | `building-blocks/` |
| 6. Runtime view | `runtime/` |
| 7. Deployment view | `deployment.md` |
| 8. Crosscutting concepts | `concepts/` |
| 9. Architecture decisions | a link to `../decisions/` |
| 10. Quality requirements | a link to `../requirements/` NFRs |
| 11. Risks and technical debt | `risks.md` |
| 12. Glossary | a link to `../requirements/glossary.md` |

- **`building-blocks/`** — `README.md` holds the C4 container diagram and a table: block · technology ·
  responsibility · talks to (protocol) · milestone · link. One file per block: its job, what it never
  does, its inner blocks (C4 component diagram and table), and what someone needs to change it safely.
  The sections of a block's file come from what that block is.
- **`runtime/<scenario>.md`** — one scenario the architecture must get right, end to end across every
  block it crosses: numbered steps, each naming the block that acts and whom it talks to.
- **`deployment.md`** — every environment and where each block runs in it, with the C4 deployment
  diagram; for software installed on the user's machine, how it is packaged and installed. Delivery —
  CI/CD, gates, release — lives here too, since it is how blocks reach their environments.
- **`concepts/<concept>.md`** — one per concept that cuts across blocks, named by the architecture.
  Security is always one of them.
- **`risks.md`** — each known risk or piece of debt: what it is, its consequence, and the issue that
  tracks it.

Everything not built yet is still drawn, marked with its milestone and dashed, so the map shows the whole
system from day one. A section that only describes something another doc owns is a link, never a copy.

## `data-model/`

The method — access patterns first, identity, invariants — is `tightship:database-design`. This folder is its
record.

- `README.md` — the conceptual model (Chen diagram) and a table: entity · one-line meaning · milestone ·
  link.
- `access-patterns.md` — operation · reads/writes · filter and order · expected volume.
- `<entity>.md`:

  ```markdown
  # <Entity>

  <One sentence: what one instance is.> Milestone: M<N>.

  | Attribute | Type | Required | Domain · rule |
  | --- | --- | --- | --- |

  - **Identity:** <key, and why that key>
  - **Relations:** <entity> (min,max) — <what deleting the parent means>
  - **Invariants:** <what is always true>
  ```

- `storage.md` — a database: tables, keys, indexes, migration path. Files: path · format · written by ·
  lifecycle.

## `roadmap/`

Status lives on GitHub, never here: each issue's Status and `Sprint` in the Project, and each milestone
as a **GitHub Milestone** holding its epics and tasks. This folder holds the plan and its history.

`README.md`:

```markdown
# Roadmap

Live status: the GitHub Project (<url>) and the milestones (<repo url>/milestones).

## M<N> — <name>
<Goal in one sentence.> GitHub Milestone: [M<N>](<milestone url>).

| Epic | Issue | Covers |
| --- | --- | --- |
| <epic name> | #<n> | FR-<AREA>-01, NFR-<CHAR>-02 |

## Requirement coverage
Every approved requirement of a planned milestone maps to exactly one epic.

| Requirement | Epic | Milestone |
| --- | --- | --- |

## Sprints
- [Sprint <N>](sprints/sprint-NN.md) — <goal>
```

`sprints/sprint-NN.md`:

```markdown
# Sprint <N> — <start> → <end>

**Goal:** <one sentence a user could observe at the end>
**Requirements baseline:** v<version>
**Items:** #<n>, #<n>

## Result — <close date>
Done: #… · Carried over: #… → Sprint <N+1>, because <reason> · Back to backlog: #…
```

## Diagrams

- One diagram per file, `docs/diagrams/<topic>.drawio.svg`, embedded with a relative path. Names:
  `context`, `containers`, `deployment`, `components-<block>`, `runtime-<scenario>`, `data-conceptual`. It is a valid
  SVG with the diagram inside: GitHub and the site render it, and the `hediet.vscode-drawio` extension
  edits it in VS Code.
- **Producing one:** write the diagram as draw.io XML (`<mxfile>`) in the scratchpad, then export with
  draw.io desktop: `draw.io --export --embed-diagram --output docs/diagrams/<topic>.drawio.svg <file>.drawio`.
  Without `--embed-diagram` the SVG can no longer be edited. No draw.io desktop on the machine → ask to
  install it (`winget install JGraph.Draw`, `brew install --cask drawio`); never hand-write the SVG half.
- **Architecture diagrams:** boxes labeled `<name>` + `[<technology>]` + a one-line responsibility; arrows
  labeled with what flows and the protocol. Built elements solid, later milestones dashed.
- **Conceptual model in Chen notation** (the BR-Modelo look): entity = rectangle; weak entity = double
  rectangle; relationship = diamond; attribute = ellipse, key attribute underlined, multivalued = double
  ellipse; cardinality `(min,max)` on each entity–relationship edge.
- After exporting, open the file in VS Code once to confirm it is still editable.

## Local docs site

Internal docs are read locally, never deployed: whoever can clone the repo runs the site. A public
documentation site, if the project has one, is a separate config and folder and never mixes with this
one.

- **Generator: Zensical** (MIT, the successor to Material for MkDocs). It builds the sidebar from the
  folders and uses each folder's `README.md` as the section page.
- `zensical.toml` at the repo root:

  ```toml
  [project]
  site_name = "<Project> — internal docs"
  docs_dir = "docs"
  ```

- `.vscode/tasks.json` holds a `docs: serve` task running `zensical serve --open`, on
  `http://localhost:8000`.
- `docs/README.md` says how to open it: `pip install zensical`, then the task or `zensical serve --open`.
- The build output `site/` is in `.gitignore`. `zensical new` also generates `.github/workflows/docs.yml`,
  a deploy workflow: never keep it.
