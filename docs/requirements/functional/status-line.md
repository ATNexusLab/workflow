# Status line — `STL`

The opt-in status line. Whether a harness other than Claude Code can show one is
[OQ-11](../open-questions.md#oq-11).

<a id="fr-stl-01"></a>
## FR-STL-01 — Status line on opt-in

> As an adopter, I want the workflow's status line when I ask for it, so that I see the session's state
> at a glance.

While the status line is enabled, the harness shall show the workflow's status line.

| Attribute | Value |
| --- | --- |
| Rationale | The status line is part of the workflow today, and an adopter may already have their own. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin status line scripts at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-STL-01.1** — Given the status line enabled and its settings change confirmed, when a session is
  open in a git repository, then the line shows the working directory's name, the git branch, the model,
  and the share of the context window in use.
- **FR-STL-01.2** — Given a terminal too narrow for every segment, when the line is drawn, then segments
  are left out in the order the status line's spec ranks them, and the line does not wrap.
- **FR-STL-01.3** — Given the status line disabled, when a session is open, then the harness shows
  whatever status line the adopter had.

<a id="fr-stl-02"></a>
## FR-STL-02 — Consent before changing settings

> As an adopter, I want to approve any change to my harness settings, so that a plugin never rewrites my
> configuration behind my back.

The plugin shall change the adopter's harness settings to enable the status line only after the adopter
confirms the exact change.

| Attribute | Value |
| --- | --- |
| Rationale | A Claude Code plugin cannot set the session status line ([constraints](../overview.md#constraints)), so enabling it means writing to the adopter's own settings. |
| Source | Analysis 2026-10-02; Claude Code plugin manifest reference |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-STL-02.1** — Given the adopter asked to enable the status line, when the change is proposed, then
  the adopter sees the setting and the value to be written before anything is written.
- **FR-STL-02.2** — Given the proposed change, when the adopter declines, then the settings file is
  byte-identical to before.
- **FR-STL-02.3** — Given a status line already configured, when the change is proposed, then the adopter
  sees the current value, and it is replaced only on confirmation.
- **FR-STL-02.4** — Given an install during which the harness asked the adopter nothing, when the first
  interactive session starts, then the change is proposed and nothing is written before confirmation.

<a id="fr-stl-03"></a>
## FR-STL-03 — Turning it off restores the previous setting

> As an adopter, I want my old status line back when I turn the workflow's off, so that trying it is
> reversible.

When the adopter disables the status line, the plugin shall restore the status line setting that existed
before it was enabled.

| Attribute | Value |
| --- | --- |
| Rationale | A change made outside the plugin is not undone by the harness. |
| Source | Derived from FR-STL-02 in analysis, 2026-10-02 |
| Priority | Should |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-STL-03.1** — Given a status line the adopter had before enabling the workflow's, when the adopter
  disables the workflow's, then the earlier value is back in the settings.
- **FR-STL-03.2** — Given no status line before enabling the workflow's, when the adopter disables it,
  then the settings hold no status line entry.
