# Installation — `INS`

Install, optional components, update, uninstall, migration, and the install guide.

<a id="fr-ins-01"></a>
## FR-INS-01 — Install through the harness's plugin mechanism

> As an adopter, I want to install the workflow the way I install any plugin in my harness, so that I run
> no installer I have to trust separately.

The plugin shall be installable in each supported harness with that harness's own plugin installation
mechanism, from this repository.

| Attribute | Value |
| --- | --- |
| Rationale | The pre-plugin install is a guided script that merges files into a user directory. A plugin is installed, updated, and removed by the harness. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-01.1** — Given a machine with the harness, the prerequisites, and no workflow installed, when
  the adopter follows the install guide's steps for that harness, then the harness lists the plugin as
  installed and enabled.
- **FR-INS-01.2** — Given the same machine, when the install steps are followed, then every step is an
  action of the harness or of git, and none runs an installer script from this repository.

<a id="fr-ins-02"></a>
## FR-INS-02 — Choose the optional components

> As an adopter, I want to pick what I turn on when I install, so that I get only the parts I want.

At installation, the plugin shall let the adopter enable or disable each optional component: the
contract, memory, and the status line.

| Attribute | Value |
| --- | --- |
| Rationale | Not every adopter has a vault, wants a status line replaced, or works under the maintainer's rules. The skills, the commands, and the verifier are always on. Claude Code asks during an interactive install and never during an install from the shell ([constraints](../overview.md#constraints)); where nothing can be asked, the adopter gets the whole workflow and turns off what they do not want. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-02.1** — Given a fresh install, when the adopter completes it having chosen a state for each
  optional component, then each component is in the chosen state from the next session.
- **FR-INS-02.2** — Given each of the eight combinations of the three choices, when a session runs, then
  the skills, the commands, and the verifier are available.
- **FR-INS-02.3** — Given an install during which the harness asked the adopter nothing, when a session
  starts, then every optional component is enabled.

<a id="fr-ins-03"></a>
## FR-INS-03 — Change a choice after installation

> As an adopter, I want to change what I turned on, so that a choice made on the first day is not
> permanent.

The plugin shall let the adopter change the state of any optional component after installation, without
reinstalling.

| Attribute | Value |
| --- | --- |
| Rationale | A choice made before using the workflow is made with the least information. |
| Source | Derived from FR-INS-02 in analysis, 2026-10-02 |
| Priority | Should |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-03.1** — Given an installed plugin, when the adopter changes the state of an optional
  component, then the component is in the new state from the next session, with the plugin still
  installed.

<a id="fr-ins-04"></a>
## FR-INS-04 — Update keeps the choices

> As an adopter, I want a new release without redoing my setup, so that updating costs one step.

The plugin shall be updatable to a newer release with the harness's own update mechanism, keeping the
state of every optional component.

| Attribute | Value |
| --- | --- |
| Rationale | This repository is where the workflow is edited; an adopter receives an edit only through an update. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-04.1** — Given an installed plugin and a newer release, when the adopter runs the harness's
  update, then the content of the newer release is delivered from the next session.
- **FR-INS-04.2** — Given optional components in chosen states, when the plugin is updated, then each is
  in the same state after the update.
- **FR-INS-04.3** — Given an installed plugin, when the adopter asks the harness which release is
  installed, then the release is identified.

<a id="fr-ins-05"></a>
## FR-INS-05 — Uninstall leaves nothing behind

> As an adopter, I want the workflow gone when I remove it, so that trying it costs me nothing.

Removing the plugin shall leave no workflow piece loaded and no harness setting the plugin changed.

| Attribute | Value |
| --- | --- |
| Rationale | The status line requires a change outside the plugin, which the harness's uninstall does not undo. |
| Source | Derived from FR-STL-02 in analysis, 2026-10-02 |
| Priority | Should |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-05.1** — Given the plugin installed with every optional component enabled, when the adopter
  completes the install guide's removal steps, then a new session loads no contract, skill, command,
  verifier, or hook of the workflow, and every harness setting the plugin changed holds its earlier
  value.
- **FR-INS-05.2** — Given a vault on the machine, when the plugin is removed, then no file in the vault
  is changed.

<a id="fr-ins-06"></a>
## FR-INS-06 — Migration from the pre-plugin install

> As the maintainer, I want my machines moved from the user-directory install to the plugin, so that the
> workflow exists in one place.

The install guide shall give the steps that move a machine running the pre-plugin workflow to the plugin,
after which each workflow piece is loaded once.

| Attribute | Value |
| --- | --- |
| Rationale | A harness loads both its user directory and its plugins. Until the pre-plugin copy is removed, every skill, command, and hook exists twice, and the copy in the user directory is a second place to edit. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-06.1** — Given a machine running the pre-plugin workflow from the harness's user directory,
  when the migration steps are completed, then each skill, command, and hook is loaded exactly once per
  session and the contract is in context exactly once.
- **FR-INS-06.2** — Given the same machine, when the migration steps are completed, then the harness's
  personal settings and the vault are unchanged.

<a id="fr-ins-07"></a>
## FR-INS-07 — Install guide per harness

> As an adopter, I want one document for my harness, so that I install, configure, update, and remove the
> workflow without reading its source.

The repository shall hold, for each supported harness, an install guide covering the prerequisites, the
install steps, the optional components and what each does, the companion plugins, update, and removal.

| Attribute | Value |
| --- | --- |
| Rationale | Each harness installs plugins differently, and an adopter must be able to decide about the companion plugins knowingly. |
| Source | Maintainer, elicitation and analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-INS-07.1** — Given a clean machine with the harness, when the adopter follows the guide as written,
  then FR-INS-01.1 holds.
- **FR-INS-07.2** — Given the guide, when the adopter reads its section on companion plugins, then it
  names each one, states what it covers, and states that the workflow works without it.
