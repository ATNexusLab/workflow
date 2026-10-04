---
description: Plan a sprint (building the roadmap on first run) or close the current one
argument-hint: "plan | close"
---

Run the sprint step for this repo: $ARGUMENTS

The backlog lives in the repo's GitHub Project (created by `/tightship:bootstrap`); the plan and its history live in
`docs/roadmap/`, written with the `tightship:project-docs` template. Status is never mirrored into the docs — the
Project and the GitHub Milestones own it.

Stop if `/tightship:bootstrap` has not run: no Project with the six-option Status and a `Sprint` iteration field, or
no `docs/requirements/` SRS with requirement IDs (`tightship:requirements-engineering`).

## `plan`

### 1. Roadmap — only when `docs/roadmap/` is missing, or a milestone has no epics yet

- Split the next unplanned milestone of `docs/requirements/` into epics. An epic is one capability a
  user can observe, sized to be specced as one `/tightship:spec`.
- Every approved requirement of the milestone maps to exactly one epic. One without an epic, or with
  two, is fixed before anything is written.
- Run a `tightship:grilling` session over the split: the epics, their order, and what each covers. Nothing is
  created before it closes.
- Create the milestone as a GitHub Milestone `M<N> — <name>` if it does not exist
  (`gh api repos/<owner>/<repo>/milestones -f title=... -f description=...`).
- Create each epic as an issue: label `epic` and its `area:*`, the milestone's GitHub Milestone, added to
  the Project in Backlog. Body:

  ```markdown
  <One sentence: what the user can do when this epic is done.>

  **Covers:** FR-<AREA>-NN, NFR-<CHAR>-NN
  **Spec:** pending — written when the epic enters a sprint.
  ```

- Write `docs/roadmap/README.md`: the milestone with its GitHub Milestone link, its epics with issue
  numbers, and the requirement coverage table.

### 2. Refinement

Every open `requirement-change` issue gets decided before the sprint is picked: approved ones go through
`/tightship:requirements`, rejected ones are closed with the reason. The sprint then plans against the resulting
version of `docs/requirements/` — its **baseline**.

### 3. The sprint

- Pick the sprint's goal: one sentence a user could observe when it ends. Then the items that reach it,
  in dependency order: an epic whole, or the part of one that the goal needs.
- An item whose epic has no closed spec gets one before any code — list those specs as the sprint's
  first work, each a `/tightship:spec` then an `/tightship:epic` that hangs the tasks on the existing epic issue.
- Agree the goal and the items with me. Then set each item's `Sprint` to the iteration and its Status to
  Todo, write `docs/roadmap/sprints/sprint-NN.md` with its requirements baseline, and link it from the
  roadmap's `README.md`.

Only this sprint is planned in detail. The next one is planned when this one closes.

## `close`

1. List the sprint's items from the Project: done — Staging or Done — and not done. An item in Staging
   is done for the sprint; the release closes it.
2. For each item not done: why, and whether it carries over to the next sprint or returns to Backlog —
   I decide.
3. Write the dated result into `docs/roadmap/sprints/sprint-NN.md`.
   Every issue of a milestone closed → close its GitHub Milestone.
4. A requirement or architecture change the sprint revealed → `/tightship:requirements` or an ADR, named here.
5. Then run `plan` for the next sprint.

## Output

```
Sprint <N>:
- Goal:     [one sentence]
- Baseline: [docs/requirements/ v<version> · change requests decided: #… / none]
- Items:    [#n title — Status], in dependency order
- Specs:    [needed before code / all closed]
- Roadmap:  [docs/roadmap/ updated — what changed]
- Carried:  [from the previous sprint / none]
```

Every doc change goes through the normal commit approval.
