---
description: Turn a closed spec into a GitHub epic issue with native sub-issues
argument-hint: "[path to the closed spec]"
---

Publish the spec at $ARGUMENTS as a GitHub epic plus one sub-issue per task.

This command does **not** design. If the spec is not closed, it stops — writing the missing detail is
`/tightship:spec`'s job, not something to improvise at publish time.

## 1. Gate — refuse an open spec

Read the spec and check, in this order. Any failure stops the command with the exact reason:

- `Status: fechada` in the header.
- No `TBD`, `???`, `a definir`, `talvez`, or question mark in a declarative sentence.
- `## Quebra em Tasks` exists, is non-empty, and every row has a title, a scope, and an acceptance
  criterion.
- Every `Depende de` value names a task number that exists in the table.
- Every Gherkin scenario in the spec is claimed by at least one task.

Report which check failed and what to fix. Do not partially publish.

## 2. Discover the repo's conventions

- `gh repo view` — confirm the target repo, and confirm I meant this one.
- `gh label list` — reuse the labels that exist. Apply `epic` to the parent if the repo has it; map each
  task to the repo's `area:*` / type labels. Never create a label without asking.
- The epic issue already exists — `/tightship:sprint plan` created it from the roadmap. Find it on
  `docs/roadmap/` and reuse it: its body gains the spec path and the scope below. Create one only when
  the repo has no roadmap, and say so.
- The repo's GitHub Project, its `Sprint` iteration field, and the current iteration.

## 3. Build the bodies

A title is only the name of the work. Hierarchy is the native parent and grouping is the label, so no
title carries a prefix like `[EPIC]` that repeats them — even where older issues in the repo do.

**Epic (parent):**

```markdown
<Uma frase: o que a feature entrega e para quem.>

**Spec:** `<caminho do arquivo no repo>`

## Escopo
<Os 3–6 comportamentos que a spec fecha.>

## Fora de escopo
<Copiado da seção da spec.>

## Tasks
<Deixe vazio — as sub-issues nativas do GitHub preenchem esta lista sozinhas.>
```

**Each sub-issue** is one delivery — reviewed in one sitting and committed alone, never a micro-task.
Its sections mirror what the epic's PR will ask for, so the PR body is already written by the time the
code is:

```markdown
## Contexto
<Regra(s) de negócio da spec que esta task implementa, com o número.> — spec: `<caminho>`

## Escopo
<O que entra. Arquivos/camada que a task toca.>

## Critério de aceite
<O(s) cenário(s) Gherkin da spec, copiados na íntegra.>

## Possíveis impactos
<O que mais no sistema esta mudança toca.>

## Como testar
1. <passo>
2. <passo>
```

## 4. Show me everything, then wait

Print the epic body and every sub-issue body in full, plus the labels each will get. Wait for my approval.
Nothing is created before I say so — approving the plan is not approving the publish.

## 5. Publish

1. Update the existing epic's body: `gh issue edit <numero-do-epic> --body-file ...`.
2. For each task, **in dependency order**:
   `gh issue create --title ... --body-file ... --parent <numero-do-epic> --label ... --project "<project title>"`
   `--parent` creates a real GitHub sub-issue — do not fake the link with a checklist.
3. Set each task's `Sprint` to the current iteration and its Status to Todo:
   `gh project item-edit --id <item-id> --project-id <project-id> --field-id <field-id> --iteration-id <iteration-id>`,
   and `--single-select-option-id` for Status. Move the epic to Todo too.
4. If a `gh` call fails, stop immediately and report which issues already exist. Never retry blindly and
   never leave duplicates behind.

## 6. Close the loop

Update the spec in place: `Status: publicada`, `Epic: #N`, and one column in `Quebra em Tasks` carrying
each task's issue number. Show me the diff and get approval before committing it — the same rule as any
other commit.

Then print the epic URL and the task numbers in dependency order. The epic's work goes on one branch,
`<type>/<epic>-<slug>`, with one commit per sub-issue ending in `(closes #<sub-issue>)`, and one PR
links the epic and every sub-issue with `Closes #<n>`.
