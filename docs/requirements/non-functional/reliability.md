# Reliability — `REL`

Behavior when a prerequisite or the vault is missing.

<a id="nfr-rel-01"></a>
## NFR-REL-01 — A plugin failure never blocks the session

A failure of any script the plugin runs shall block 0 sessions and 0 prompts.

| Attribute | Value |
| --- | --- |
| Rationale | The pre-plugin setup refuses to wire hooks when a prerequisite is missing, so that nothing fails on every prompt. A plugin has no setup step that can refuse, so its hooks must fail without stopping the adopter's work. |
| Source | Pre-plugin README, "Install"; analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-REL-01.1** — Given a machine with no Python, or with Python older than the prerequisite, when a
  session starts and a prompt is submitted, then the session starts and the prompt is processed.
- **NFR-REL-01.2** — Given memory enabled and no vault at the vault's location, when a session starts and
  a prompt is submitted, then the session starts and the prompt is processed.

<a id="nfr-rel-02"></a>
## NFR-REL-02 — A failure names its cause

When a script the plugin runs cannot do its work, the adopter shall receive exactly 1 message per session
that names what is missing and how to fix it.

| Attribute | Value |
| --- | --- |
| Rationale | A hook that fails quietly looks like a workflow that works. The pre-plugin memory script prints nothing when the vault is absent. |
| Source | Analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-REL-02.1** — Given Python older than the prerequisite, when a session starts, then the adopter
  receives 1 message naming Python and the minimum version.
- **NFR-REL-02.2** — Given memory enabled and no vault at the vault's location, when a session starts,
  then the adopter receives 1 message naming the location, how to create a vault, and how to turn memory
  off.
- **NFR-REL-02.3** — Given either failure, when further prompts are submitted in the same session, then
  the message is not repeated.
