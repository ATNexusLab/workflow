---
description: Check what the delivery gate does not — surfaces, docs, traceability, security debt — before the commit
argument-hint: "[optional scope note]"
---

Run the closeout for the delivery in progress, after its gates are green and it has been run and
observed, and before I hand it over for the commit. Those gates and run-to-verify belong to the
delivery itself and are not repeated here. Each item below gets a recorded decision
(`done at <path>` / `n/a` / `deferred → issue #`). **Silence on any item is a failure.**

Nothing here assumes a stack. Discover the repo's tooling, commands, and conventions from its own
config — never invent them, never assume a particular linter, runner, framework, or database.

## 0. Scope — which surfaces this diff touched

List the changed files (`git diff --name-only`, plus untracked). From them, name the surfaces in
play. **Only the surfaces you name run in §1**, so name them explicitly — an unnamed surface is a
scope decision on the record, not an omission.

## 1. Surface gates

Run only the surfaces named in §0.

### Interface — anything a person sees or operates
- Keyboard reachable, focus visible, controls labeled, contrast holds.
- Loading, empty, and error states exist — not only the happy path.
- Holds at the smallest viewport or terminal width the project supports.
- No layout shift or re-render storm on interaction.
- Nothing needlessly heavy added to what ships to the client.
- User-facing copy in the project's UI language.

### Request handling — anything answering a caller
- Input validated at the boundary; rejection is typed, never a bare string.
- Authorization checked per resource, not merely authentication.
- Errors propagate with actionable messages; nothing swallowed.
- Response shape and status match the documented contract.
- Repeated or retried calls are idempotent where they must be.

### Data & persistence
- Migration is reversible and safe against rows that already exist.
- New query paths have the constraints and indexes they need.
- No N+1, no unbounded result set.
- Nothing sensitive newly logged or stored in the clear.

### Async & background work
- Failure is visible — logged or alerted, never silent.
- Retry is bounded and idempotent.
- No unbounded queue or backlog growth.

### Configuration & secrets
- No env fallback; every variable required and validated fail-fast at boot.
- New variables documented in the committed example/template.
- No secret hardcoded, logged, or committed.

## 2. Docs upkeep (only when warranted)

Use `tightship:technical-writing` as the lens — including its first question, whether the doc should exist at all.

- Public contract changed (API/CLI/env/schema)? → update `README.md` / `docs/`.
- Cross-cutting decision made? → `/tightship:spec` an ADR in `docs/decisions/`.
- Setup/run commands changed? → update README Quick Start.
- Architecture or data changed? → `docs/architecture/`, `docs/data-model/`, and their diagrams match
  what was built (`tightship:project-docs`).

## 3. Traceability — always, never `n/a`

- The work has an issue. An epic's work sits on its branch `<type>/<epic>-<slug>`, one commit per
  sub-issue ending in `(closes #<sub-issue>)`, and its PR targets the integration branch with
  `Closes #<n>` for the epic and each sub-issue. An issue with no epic has its own branch
  `<type>/<issue>-<slug>`.
- Once the PR is merged into the integration branch, the epic and its sub-issues move to Staging
  (`gh project item-edit`). They close, and go to Done, when the release reaches `main`.
- The issue's Status in the Project matches reality, and it sits in the current `Sprint`.

## 4. Security debt

Review open `security-debt` issues touching this area (via `gh`). Anything deferred this session
must already be filed. Nothing security-related is dropped silently.

Before filing, search the backlog for the issue that already owns the item — often the next delivery,
named by its spec. Only what has no owner gets a new issue, and every issue opened is reported.

## Output

```
Closeout:
- Surfaces:      [which the diff touched]
- Surface gates: [per surface: pass / findings / n/a by scope]
- Docs:          [updated at <path> / n/a]
- Traceability:  [issue #n · branch · PR → integration branch · Status/Sprint ok]
- Security-debt: [none / issues #… / filed #…]
```
Do not hand the delivery over for the commit until this block is produced with no failing item.
