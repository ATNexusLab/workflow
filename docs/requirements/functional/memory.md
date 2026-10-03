# Memory — `MEM`

The vault functions, the vault template, and the sync with the remotes. Every requirement here applies while memory is enabled,
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
- **FR-MEM-07.3** — Given memory disabled, when the adopter invokes the handoff release, the handoff fetch,
  or the sync, then no file in the vault is read or written, no remote is contacted, and the adopter is
  told memory is disabled.

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

<a id="fr-mem-09"></a>
## FR-MEM-09 — Release a handoff

> As an adopter stopping work on a project, I want its state released as a handoff, so that the next
> session continues from it on any of my machines.

The plugin shall let the adopter release a handoff: a handoff note of the project's state, written in the
project's scope and sent to the vault's remote.

| Attribute | Value |
| --- | --- |
| Rationale | A handoff that stays on one machine does not reach the session that continues the work on another. Before this requirement a handoff was an ordinary note write, with nothing that sent it. |
| Source | Maintainer, change request [#12](https://github.com/ATNexusLab/workflow/issues/12), 2026-10-03 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.1.0 |

**Acceptance criteria**
- **FR-MEM-09.1** — Given a vault with a remote, when the adopter releases a handoff, then a handoff note
  with the project's state exists in the project's scope and the vault's remote holds it.
- **FR-MEM-09.2** — Given a vault with no remote, or a remote that cannot be reached, when the adopter
  releases a handoff, then the note exists in the local vault and the adopter is told the remote does not
  hold it and why.

<a id="fr-mem-10"></a>
## FR-MEM-10 — Fetch a handoff

> As an adopter resuming a project, I want its latest handoff fetched, so that I continue from where the
> last session stopped, on whichever machine it ran.

The plugin shall let the adopter fetch the project's latest handoff, after bringing the vault up to date
from its remote.

| Attribute | Value |
| --- | --- |
| Rationale | The session-start context shows the latest handoff on disk ([FR-MEM-01.3](#fr-mem-01)). A handoff released on another machine is not on disk until the vault is brought up to date. |
| Source | Maintainer, change request [#12](https://github.com/ATNexusLab/workflow/issues/12), 2026-10-03 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.1.0 |

**Acceptance criteria**
- **FR-MEM-10.1** — Given a handoff note in the project's scope on the vault's remote, newer than every
  local one, when the adopter fetches the handoff, then its text is in the agent's context.
- **FR-MEM-10.2** — Given no handoff note in the project's scope, locally or on the remote, when the
  adopter fetches the handoff, then the adopter is told there is none.
- **FR-MEM-10.3** — Given a vault with no remote, or a remote that cannot be reached, when the adopter
  fetches the handoff, then the text of the latest local one is in the agent's context and the adopter is
  told the remote was not read and why.

<a id="fr-mem-11"></a>
## FR-MEM-11 — Sync the vault with its remote

> As an adopter, I want the vault synchronized with its remote by one command, so that I never open a
> session only to push it.

The plugin shall synchronize the vault with its remote on the adopter's request.

| Attribute | Value |
| --- | --- |
| Rationale | In the pre-plugin workflow the maintainer opened a session only to send the vault and the harness's user directory to their remotes. The plugin replaces the user directory; the vault still has to travel. |
| Source | Maintainer, change request [#12](https://github.com/ATNexusLab/workflow/issues/12), 2026-10-03 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.1.0 |

**Acceptance criteria**
- **FR-MEM-11.1** — Given notes that exist only in the local vault and notes that exist only on its
  remote, when the adopter syncs, then the local vault and the remote hold the same notes.
- **FR-MEM-11.2** — Given a vault with no remote, or a remote that cannot be reached, when the adopter
  syncs, then no note is changed and the adopter is told why.
- **FR-MEM-11.3** — Given a note changed both locally and on the remote, when the adopter syncs, then
  neither version is discarded and the adopter is told which notes differ. How they are reconciled is
  [OQ-13](../open-questions.md#oq-13).

<a id="fr-mem-12"></a>
## FR-MEM-12 — Sync pushes the project's branch

> As an adopter finishing work, I want the same sync to send my project's commits, so that one command
> leaves nothing only on this machine.

The plugin shall, in the same sync, send the commits of the project repository's current branch to that
repository's remote.

| Attribute | Value |
| --- | --- |
| Rationale | The ceremony the sync replaces sent more than the vault. The commits stay the adopter's decision; the sync only sends the ones that exist. |
| Source | Maintainer, change request [#12](https://github.com/ATNexusLab/workflow/issues/12), 2026-10-03 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.1.0 |

**Acceptance criteria**
- **FR-MEM-12.1** — Given commits on the project's current branch that its remote lacks, when the adopter
  syncs, then the remote branch holds them.
- **FR-MEM-12.2** — Given uncommitted changes in the project repository, when the adopter syncs, then
  none of them is committed or sent and the adopter is told which files they are.
- **FR-MEM-12.3** — Given a remote branch that holds commits the local branch lacks, when the adopter
  syncs, then no commit on the remote is overwritten, nothing of the project is sent, and the adopter is
  told why.
- **FR-MEM-12.4** — Given a session outside a git repository, or in one with no remote, when the adopter
  syncs, then the vault is synchronized and the adopter is told nothing of the project was sent.
