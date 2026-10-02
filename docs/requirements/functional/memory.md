# Memory — `MEM`

The vault functions and the vault template. Every requirement here applies while memory is enabled,
except [FR-MEM-07](#fr-mem-07).

<a id="fr-mem-01"></a>
## FR-MEM-01 — Memory context at session start

> As an adopter, I want the standing facts of my project in front of the agent when a session starts, so
> that it does not rediscover them.

The plugin shall place in the agent's context, at session start, the vault's pinned notes for the current
project's scope and for the shared scope.

| Attribute | Value |
| --- | --- |
| Rationale | A pinned note is a fact the work needs before it knows to search. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin memory script at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-01.1** — Given a vault with pinned notes in the project's scope and in the shared scope, when a
  session starts in that project, then each of those notes is listed with the one-line reason it exists,
  the project's scope first.
- **FR-MEM-01.2** — Given notes in other scopes, when a session starts, then none of them is listed and
  the number of notes in each other scope is shown.
- **FR-MEM-01.3** — Given a handoff note in the project's scope, when a session starts, then the text of
  the latest one is in the context.
- **FR-MEM-01.4** — Given more pinned notes than the memory context's size limit holds, when a session
  starts, then the number of notes left out is shown.

<a id="fr-mem-02"></a>
## FR-MEM-02 — Checkpoint reminder

> As an adopter, I want the agent reminded to record durable facts, so that what a session learned is not
> lost when it ends.

The plugin shall remind the agent, at a fixed interval of prompts during a session and after every
context compaction, to record durable facts in the vault.

| Attribute | Value |
| --- | --- |
| Rationale | A fact not written during the session is gone after it, and compaction is the moment most of it is discarded. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin memory script at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-02.1** — Given a session, when its prompt count reaches a multiple of the reminder interval,
  then the reminder, with the criteria a fact must meet to enter the vault, is in the agent's context.
- **FR-MEM-02.2** — Given a session, when its context is compacted, then the reminder is in the context
  that follows.
- **FR-MEM-02.3** — Given a session, when a prompt is submitted between two multiples of the interval,
  then no reminder is added.

<a id="fr-mem-03"></a>
## FR-MEM-03 — Search the notes

> As an adopter, I want the agent to find a note by its words, so that a recorded fact is reached when the
> work calls for it.

The plugin shall let the agent search the vault's notes by terms.

| Attribute | Value |
| --- | --- |
| Rationale | Only pinned notes are listed at session start; every other note is reached by search. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin memory script at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-03.1** — Given notes that contain the terms, when the agent searches, then it receives one line
  per matching note with the note's path and reason, notes matching more terms first and, among those,
  the project's scope before the shared scope.
- **FR-MEM-03.2** — Given no note that contains the terms, when the agent searches, then it is told so
  and how to broaden the search.
- **FR-MEM-03.3** — Given matching notes in other scopes, when the agent searches without asking for
  every scope, then those notes are not returned.

<a id="fr-mem-04"></a>
## FR-MEM-04 — Write a note in one step

> As an adopter, I want a durable fact written in a single step, so that recording it never waits for a
> later promotion.

The plugin shall let the agent create a note in the vault with one invocation.

| Attribute | Value |
| --- | --- |
| Rationale | A two-step write is the step that silently fails. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin memory script at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-04.1** — Given a title, a reason, a scope, a type, a source, and a body, when the agent writes
  a note, then a note file exists in that scope with the next free identifier, the date, and the harness
  that wrote it.
- **FR-MEM-04.2** — Given a missing or invalid field, when the agent writes a note, then no file is
  created and the error names the field.

<a id="fr-mem-05"></a>
## FR-MEM-05 — Lint the vault

> As an adopter, I want the vault checked against its own rules, so that a malformed note is found before
> it is relied on.

The plugin shall report every note that breaks the vault's rules.

| Attribute | Value |
| --- | --- |
| Rationale | A note with a missing field or a duplicate identifier is skipped or misfiled without a word. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin memory script at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-05.1** — Given notes that break a rule, when the lint runs, then it lists each such note with
  each rule it breaks and reports failure.
- **FR-MEM-05.2** — Given a vault with no broken rule, when the lint runs, then it reports the note count
  and success.

<a id="fr-mem-06"></a>
## FR-MEM-06 — Create a vault from the template

> As an adopter with no vault, I want to create one from the plugin, so that I can turn memory on with a
> vault that is mine.

The plugin shall create a new vault from its template on the adopter's request.

| Attribute | Value |
| --- | --- |
| Rationale | An adopter must never need another person's vault to use memory. |
| Source | Pre-plugin install guide, section "The memory vault"; maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-06.1** — Given no vault at the vault's location, when the adopter requests a new vault, then a
  vault exists there with the template's files and zero notes.
- **FR-MEM-06.2** — Given a vault already at the vault's location, when the adopter requests a new vault,
  then no file is changed and the adopter is told a vault exists.

<a id="fr-mem-07"></a>
## FR-MEM-07 — Memory can be turned off

> As an adopter who does not want a memory layer, I want it fully off, so that nothing reads or writes a
> vault on my machine.

While memory is disabled, the plugin shall perform no memory activity: no memory function runs on its
own, and no vault is read or written.

| Attribute | Value |
| --- | --- |
| Rationale | The pre-plugin install already offers the workflow without the memory layer. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin install guide |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-07.1** — Given memory disabled, when a session starts, prompts are submitted, and the context
  is compacted, then no memory context and no checkpoint reminder is added.
- **FR-MEM-07.2** — Given memory disabled and a vault on the machine, when a session runs, then no file
  in the vault is read or written by the plugin.

<a id="fr-mem-08"></a>
## FR-MEM-08 — Vault location is the adopter's choice

> As an adopter, I want to say where my vault lives, so that it sits where I keep my repositories.

The plugin shall use the vault at the location the adopter chose, and at `~/ai-memory` when the adopter
enabled memory without choosing one.

| Attribute | Value |
| --- | --- |
| Rationale | The pre-plugin memory script reads one fixed path, which suits one person's machines and not every adopter's. |
| Source | Maintainer, validation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-MEM-08.1** — Given a location the adopter chose, when any memory function runs, then it reads and
  writes the vault at that location.
- **FR-MEM-08.2** — Given memory enabled and no location chosen, when any memory function runs, then it
  reads and writes the vault at `~/ai-memory`.
