# Flexibility — `FLEX`

The four harnesses, the three operating systems, and harness-neutral content.

<a id="nfr-flex-01"></a>
## NFR-FLEX-01 — Claude Code is supported

The product shall provide a plugin for Claude Code that meets 100% of the acceptance criteria of the
approved Must functional requirements.

| Attribute | Value |
| --- | --- |
| Rationale | Claude Code is where the workflow runs today and is the first harness ([BR-01](../business-rules.md#br-01)). |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-01.1** — Given Claude Code at its supported version, when the plugin is installed by the
  install guide, then 100% of the acceptance criteria of the approved Must functional requirements pass.

<a id="nfr-flex-02"></a>
## NFR-FLEX-02 — Cursor is supported

The product shall provide a plugin for Cursor that meets 100% of the acceptance criteria of the approved
Must functional requirements.

| Attribute | Value |
| --- | --- |
| Rationale | The maintainer works in four harnesses and wants one workflow in all of them. What Cursor cannot do with its documented mechanisms is [OQ-08](../open-questions.md#oq-08), settled by its spec through change control. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M2 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-02.1** — Given Cursor at its supported version, when the plugin is installed by the install
  guide, then 100% of the acceptance criteria of the approved Must functional requirements pass.

<a id="nfr-flex-03"></a>
## NFR-FLEX-03 — Antigravity CLI is supported

The product shall provide a plugin for Antigravity CLI that meets 100% of the acceptance criteria of the
approved Must functional requirements.

| Attribute | Value |
| --- | --- |
| Rationale | Same need as NFR-FLEX-02. What Antigravity CLI cannot do with its documented mechanisms is [OQ-09](../open-questions.md#oq-09). |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M3 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-03.1** — Given Antigravity CLI at its supported version, when the plugin is installed by the
  install guide, then 100% of the acceptance criteria of the approved Must functional requirements pass.

<a id="nfr-flex-04"></a>
## NFR-FLEX-04 — Codex is supported

The product shall provide a plugin for Codex that meets 100% of the acceptance criteria of the approved
Must functional requirements.

| Attribute | Value |
| --- | --- |
| Rationale | Same need as NFR-FLEX-02. What Codex cannot do with its documented mechanisms is [OQ-10](../open-questions.md#oq-10). |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M4 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-04.1** — Given Codex at its supported version, when the plugin is installed by the install
  guide, then 100% of the acceptance criteria of the approved Must functional requirements pass.

<a id="nfr-flex-05"></a>
## NFR-FLEX-05 — Three operating systems

Each released harness plugin shall meet its acceptance criteria on 3 of 3 operating systems: macOS, Linux,
and Windows.

| Attribute | Value |
| --- | --- |
| Rationale | The maintainer's machines run all three. The pre-plugin workflow already holds that a change is verified on each system it touches, after three faults that only running on the other systems revealed. |
| Source | Pre-plugin README, "How cross-platform works" |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-05.1** — Given a released harness plugin, when its acceptance criteria are run on macOS, on
  Linux, and on Windows, then 100% pass on each of the three.

<a id="nfr-flex-06"></a>
## NFR-FLEX-06 — Harness-neutral canonical content

The canonical content shall contain 0 harness product names, 0 harness configuration paths, and 0 names
of a harness's own tools or commands.

| Attribute | Value |
| --- | --- |
| Rationale | The first plugin is for Claude Code, and nothing may be built so that it only works there. The pre-plugin contract, three commands, the memory script, the verifier definition, and the vault template name Claude Code, its paths, or its native tools and commands. How a harness-native capability is named neutrally is [OQ-05](../open-questions.md#oq-05). |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-06.1** — Given the canonical content, when it is scanned for the names, configuration paths,
  and native tool and command names of the four harnesses, then the scan finds 0 matches.

<a id="nfr-flex-07"></a>
## NFR-FLEX-07 — A new harness leaves the canonical content untouched

Adding a harness plugin shall modify 0 files of the canonical content.

| Attribute | Value |
| --- | --- |
| Rationale | It is the proof that NFR-FLEX-06 held: a harness that needs a canonical file changed shows the content was shaped for the earlier ones. |
| Source | Derived from NFR-FLEX-06 in analysis, 2026-10-02 |
| Priority | Should |
| Status | approved |
| Milestone | M2 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-FLEX-07.1** — Given the change that adds the plugin of a new harness, when its diff is listed,
  then it modifies 0 files of the canonical content.
