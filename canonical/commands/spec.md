---
description: Map a feature into a closed, unambiguous spec — ready to become an epic
argument-hint: "[the feature to spec, or a path to a draft spec to continue]"
---

Produce the design document **before** any implementation, for: $ARGUMENTS

This command writes the spec. It does **not** write code and does **not** open issues — `{{command:epic}}` publishes
a closed spec. Use the `{{skill:spec-writing}}` skill for the templates and the closed-spec gate.

## 1. Locate before asking

Find the facts yourself; spend my attention only on decisions.

- The feature is an item of the current sprint, with an epic issue on `docs/roadmap/`. If it is not,
  stop: it goes through `{{command:sprint}} plan` first.
- `docs/requirements/` — name the requirement IDs this feature covers (the epic lists them), and flag any
  `Open question` there that this spec will settle. If the feature contradicts what the requirements
  say, stop and raise it: one of the two documents is wrong.
- `docs/architecture/` and `docs/data-model/` — the containers, components, and entities this
  feature touches.
- Where specs live in this repo (`docs/specs/`, …) and how existing ones are named.
- The repo's `Architecture` section, its doc language, and the module this feature lands in.
- Existing permissions, roles, error codes, message strings, and field conventions to reuse — never invent
  a new one when the codebase already has the concept.
- Any draft of this spec already on disk.

State the profile you picked (**UI** or **API**, per `templates.md`) and why, in one line.

## 2. Grill me — this is the default, not an option

Run a `{{skill:grilling}}` session over the whole feature before writing anything: state the assumptions the spec
rests on, let me correct them in one pass, and turn only what I contest into a question.

**A spec grilling ends later than a plain one.** The standalone method stops when nothing left can change
the shape of the work; a spec has to be *closed*, so it continues until every line of the chosen template
has an answer and the closed-spec gate would pass. Once the assumption list is settled, the remaining
template lines are asked one at a time. Do not stop while any of these is open:

- Who can do this, and which permission gates it.
- What each field is: type, obligatoriness, domain, ordering, limit, where its data comes from.
- Every literal message the user sees, word for word.
- What happens on the exception paths — bad input, missing permission, state changed underneath.
- What persists, what is audited, what is emitted.
- What is deliberately **out of scope**.

A fact I could not possibly know (a table name, an existing enum) is yours to look up, not to ask.

## 3. Write it

Fill the profile's template from `templates.md`, in the repo's doc language, at the repo's spec location.
Nothing invented: every value in the document traces to something I confirmed or something you found in
the code.

## 4. Break it into tasks

Propose `## Quebra em Tasks` and walk me through it before finalizing. Slicing rules are in
`templates.md` — vertical slices, ordered by dependency, every scenario owned by a task.

## 5. Close it

Run the closed-spec gate from the skill line by line and report the result. If it passes, set
`Status: fechada` and tell me the spec is ready for `{{command:epic}}`. If it does not, name exactly what is still
open — never set `fechada` on a spec that has a soft spot.

Then close the loop with the requirements: for every question in `docs/requirements/open-questions.md` this spec
answered, delete the question and put a link to this spec in its place. Show me that diff separately.

And with the global docs: what the spec's `Impacto na arquitetura` and `Impacto no modelo de dados`
sections declare is applied to `docs/architecture/`, `docs/data-model/`, and their diagrams, marked
with the feature's milestone. Show me that diff separately too. The feature's PR later makes the map
match what was built.

## Also handles

- **ADR** (a cross-cutting decision) → `docs/decisions/NNNN-<slug>.md`, template in the skill. Must conform
  to — or explicitly amend — the repo's `Architecture` section.
- **Implementation plan** (how to build something already specced) → ordered by dependency, acceptance
  criteria per step. A working doc, not a repo doc unless I ask to persist it.
