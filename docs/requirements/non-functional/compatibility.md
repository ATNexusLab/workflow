# Compatibility — `COMP`

Companion plugins, one vault across harnesses, and no double loading.

<a id="nfr-comp-01"></a>
## NFR-COMP-01 — Works with or without the companion plugins

The plugin shall meet 100% of its acceptance criteria both with the 3 companion plugins installed and
with 0 of them installed.

| Attribute | Value |
| --- | --- |
| Rationale | An adopter may knowingly install none of them ([BR-05](../business-rules.md#br-05)). The pre-plugin contract hands simplicity to one of them by name. |
| Source | Maintainer, analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-COMP-01.1** — Given a harness with ponytail, i-have-adhd, and humanizer installed, when the
  plugin's acceptance criteria are run, then 100% pass.
- **NFR-COMP-01.2** — Given a harness with none of the three installed, when the plugin's acceptance
  criteria are run, then 100% pass.

<a id="nfr-comp-02"></a>
## NFR-COMP-02 — One vault across harnesses

100% of the notes written through one harness's plugin shall be found by the search and the session-start
context of every other harness's plugin on the same machine.

| Attribute | Value |
| --- | --- |
| Rationale | The vault is one curated memory shared by every harness; a fact learned in one must not be relearned in another. |
| Source | Pre-plugin vault template, operating rules |
| Priority | Must |
| Status | approved |
| Milestone | M2 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-COMP-02.1** — Given the plugin installed in two harnesses on one machine, with memory enabled and
  the same vault location in both, when a pinned note is written from one, then the next session of the
  other lists it, and its search finds it.

<a id="nfr-comp-03"></a>
## NFR-COMP-03 — No double loading across harnesses

With the plugin installed in two or more harnesses on one machine, each workflow piece shall be loaded
exactly 1 time per session in each harness.

| Attribute | Value |
| --- | --- |
| Rationale | Research on 2026-10-02 reports that Cursor reads another harness's user directory and imports its plugins by default. A piece loaded twice costs context and can run a hook twice. |
| Source | Analysis 2026-10-02; Cursor documentation on third-party hooks, not re-verified |
| Priority | Must |
| Status | approved |
| Milestone | M2 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-COMP-03.1** — Given the plugin installed in two harnesses on one machine, when a session starts
  in either, then each skill, command, and hook is loaded exactly 1 time and the contract is in context
  exactly 1 time.
