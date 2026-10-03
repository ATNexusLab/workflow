# Security — `SEC`

Identity, secrets, network access, and where the plugin writes.

<a id="nfr-sec-01"></a>
## NFR-SEC-01 — No personal identity in shipped content

The files a harness plugin installs shall contain 0 personal names, 0 email addresses, 0 account names,
and 0 home-directory paths of any person.

| Attribute | Value |
| --- | --- |
| Rationale | An adopter of the pre-plugin workflow reported that their agent took them for the maintainer. The cause is not found yet ([OQ-02](../open-questions.md#oq-02)); this requirement closes the one path the product controls. |
| Source | Adopter report, relayed by the maintainer on 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-SEC-01.1** — Given the files a harness plugin installs, when they are scanned for personal names,
  email addresses, account names, and home-directory paths, then the scan finds 0 matches.
- **NFR-SEC-01.2** — Given an adopter other than the maintainer, with a vault of their own, when a
  session starts, then nothing the plugin places in context attributes the session to another person.

<a id="nfr-sec-02"></a>
## NFR-SEC-02 — No secret and no vault content in the repository

This repository shall contain 0 credentials, 0 environment files with real values, and 0 notes from any
person's vault, in every commit.

| Attribute | Value |
| --- | --- |
| Rationale | The repository is public, and its source is a private configuration that sits next to credentials and a private vault. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin contract, "Security" |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-SEC-02.1** — Given every commit of this repository, when it is scanned for credentials and
  environment files with real values, then the scan finds 0.
- **NFR-SEC-02.2** — Given every commit of this repository, when it is searched for vault notes, then it
  holds 0 beyond the vault template's own files.

<a id="nfr-sec-03"></a>
## NFR-SEC-03 — No network access beyond the adopter's git remotes

The plugin shall open 0 network connections other than those to the git remote of the vault and the git
remote of the project repository, made by the handoff release, the handoff fetch, and the sync on the
adopter's invocation.

| Attribute | Value |
| --- | --- |
| Rationale | A plugin's hooks run on the adopter's machine at every session and prompt, with the adopter's privileges. The pre-plugin scripts work entirely on local files, and that is what makes them safe to install from a stranger. The three functions that reach a remote run only when the adopter invokes them, and reach only repositories the adopter configured. |
| Source | Analysis 2026-10-02; pre-plugin memory and status line scripts at the baseline; change request [#12](https://github.com/ATNexusLab/workflow/issues/12) |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-SEC-03.1** — Given a session with every optional component enabled, when the plugin's scripts
  run at session start, on each prompt, and for the status line, then they open 0 network connections.
- **NFR-SEC-03.2** — Given a vault and a project repository that each have a git remote, when the adopter
  invokes the handoff release, the handoff fetch, or the sync, then 0 network connections are opened to
  any host other than those two remotes.

<a id="nfr-sec-04"></a>
## NFR-SEC-04 — Confined writes

The scripts a harness plugin runs shall write to 4 locations only: the vault, the plugin's own state
directory, after consent the harness's status line setting, and, during a sync the adopter invoked, the
git data of the project repository.

| Attribute | Value |
| --- | --- |
| Rationale | An adopter must be able to know everything a plugin can change on their machine. The pre-plugin memory script keeps its state under one harness's user directory, which a plugin does not own. |
| Source | Analysis 2026-10-02; change request [#12](https://github.com/ATNexusLab/workflow/issues/12) |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-SEC-04.1** — Given a session with every optional component enabled, when the plugin's scripts
  run on their own, then they create or change 0 files outside the vault, the plugin's own state
  directory, and the harness's status line setting.
- **NFR-SEC-04.2** — Given a project repository with commits its remote lacks, when the adopter syncs,
  then 0 files in the project's working tree are created or changed.
