# Verifier — `VER`

The read-only verifier subagent.

<a id="fr-ver-01"></a>
## FR-VER-01 — Verifier can be dispatched

> As an adopter, I want an independent skeptic the agent can call, so that a fix or a finding is
> challenged before I trust it.

The plugin shall provide the verifier as a subagent the main agent can dispatch with one claim to
disprove.

| Attribute | Value |
| --- | --- |
| Rationale | A claim checked by the agent that made it is confirmed more often than it is tested. The verifier starts from "refuted". |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin workflow at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-VER-01.1** — Given the plugin installed, when the subagents available to the main agent are listed,
  then the verifier is listed.
- **FR-VER-01.2** — Given a claim, when the main agent dispatches the verifier with it, then the verifier
  returns a verdict on that claim with the evidence it found.

<a id="fr-ver-02"></a>
## FR-VER-02 — Verifier is read-only

> As an adopter, I want the verifier unable to change my files, so that a verification never alters what
> it verifies.

The verifier shall leave every file unchanged.

| Attribute | Value |
| --- | --- |
| Rationale | In the workflow, implementation belongs to the main session and subagents only analyse. The verifier still runs commands, because disproving a claim means executing the code. |
| Source | Pre-plugin contract, "How I work"; pre-plugin verifier definition at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-VER-02.1** — Given the verifier's definition in a harness plugin, when its tools are listed, then
  they are limited to reading files, searching, and running commands, with no file-editing tool.
- **FR-VER-02.2** — Given a repository with a clean working tree, when the verifier is dispatched and
  returns, then the working tree is identical to before the dispatch.
