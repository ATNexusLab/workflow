# Business rules

Policies that hold regardless of feature.

<a id="br-01"></a>
## BR-01 — Harness order and milestones

Harness plugins are released one at a time, in this order, one milestone each:

| Milestone | Harness |
| --- | --- |
| M1 | Claude Code |
| M2 | Cursor |
| M3 | Antigravity CLI |
| M4 | Codex |

Work on a harness starts only after the previous harness's plugin is released.

| Attribute | Value |
| --- | --- |
| Rationale | Claude Code is where the workflow runs today, so it is the first to prove the canonical source. Each later harness is resolved in its own turn. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

<a id="br-02"></a>
## BR-02 — One place to edit

The workflow is edited only in this repository. A harness's user directory holds only what a plugin
cannot carry.

| Attribute | Value |
| --- | --- |
| Rationale | Two editable copies diverge, and only one of them can be installed by others. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

<a id="br-03"></a>
## BR-03 — English content

Everything a harness plugin installs and every document in this repository is written in English.

| Attribute | Value |
| --- | --- |
| Rationale | The repository is public and open to any adopter. One pre-plugin command is written in Portuguese and is translated. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

<a id="br-04"></a>
## BR-04 — The contract is on or off

The contract is the maintainer's. An adopter enables it or disables it, and the plugin offers no way to
edit it or to layer rules over it. An adopter who wants other rules disables it and uses the harness's
own instruction file.

| Attribute | Value |
| --- | --- |
| Rationale | An installed plugin's files are replaced at every update, so an edited contract would not survive, and an override layer is a second product. |
| Source | Maintainer, analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

<a id="br-05"></a>
## BR-05 — Companion plugins own their rules

The workflow states no rule and ships no function that ponytail, i-have-adhd, or humanizer already
provides, and it requires none of them.

| Attribute | Value |
| --- | --- |
| Rationale | A rule kept in two products diverges. An adopter may knowingly install none of the three. |
| Source | Maintainer, analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |
