# Skills and commands — `SKL`

The skills, the commands, and the names they are invoked by.

<a id="fr-skl-01"></a>
## FR-SKL-01 — Skills available

> As an adopter, I want the workflow's skills in my harness, so that the agent loads the right method when
> a task calls for it.

The plugin shall make each of the workflow's skills available to the agent, together with every
supporting file of the skill.

| Skill | Covers |
| --- | --- |
| `api-design` | Designing and reviewing an API contract |
| `architecture-reading` | Reading an unfamiliar codebase before changing it |
| `database-design` | Modeling data, schemas, migrations, queries |
| `frontend-architecture` | Structuring UI code |
| `grilling` | Stating the assumptions a plan rests on |
| `grill-me` | The adopter-invoked entry point to `grilling` |
| `hexagonal-architecture` | Structuring an app with real domain logic |
| `performance-analysis` | Investigating slowness |
| `project-docs` | The project's docs folder, global docs, and diagrams |
| `requirements-engineering` | The versioned SRS and its change control |
| `security-audit` | Auditing code or a diff for vulnerabilities |
| `spec-writing` | Writing a spec or an ADR before implementation |
| `technical-writing` | Writing a README, a docs page, or a runbook |
| `testing-contract` | Deciding whether a change earns a test and how to write it |

| Attribute | Value |
| --- | --- |
| Rationale | The skills hold the methods the contract and the commands defer to. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin workflow at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-SKL-01.1** — Given the plugin installed, when the adopter lists the skills the harness has
  available, then each skill in the table is listed.
- **FR-SKL-01.2** — Given a skill with supporting files, when the agent loads the skill, then it can read
  each supporting file.
- **FR-SKL-01.3** — Given `grill-me`, when a session runs without the adopter invoking it by name, then
  the agent does not load it.

<a id="fr-skl-02"></a>
## FR-SKL-02 — Commands invocable

> As an adopter, I want each step of the development loop as a command, so that I start it by name.

The plugin shall make each of the workflow's commands invocable by name, passing the adopter's argument
text to it.

| Command | Step |
| --- | --- |
| `requirements` | Elicit, change, or validate the project's requirements |
| `bootstrap` | Set a repository up for the workflow |
| `sprint` | Plan a sprint or close the current one |
| `spec` | Map a feature into a closed spec |
| `epic` | Turn a closed spec into an epic issue with sub-issues |
| `audit` | Audit a path or the current diff |
| `closeout` | Check what the delivery gate does not, before the commit |
| `pr-review` | Review someone else's pull request |

| Attribute | Value |
| --- | --- |
| Rationale | The commands are how the adopter drives the development loop the contract describes. |
| Source | Maintainer, elicitation 2026-10-02; pre-plugin workflow at the baseline |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-SKL-02.1** — Given the plugin installed, when the adopter lists the commands the harness has
  available, then each command in the table is listed.
- **FR-SKL-02.2** — Given the plugin installed, when the adopter invokes a command by the name the
  harness lists for it, followed by argument text, then the command's instructions run with that text.

<a id="fr-skl-03"></a>
## FR-SKL-03 — References resolve

> As an adopter, I want every command the contract or a skill mentions to work as written, so that
> following the text never ends in an unknown command.

Every reference to a skill, a command, the verifier, or a memory function in delivered content shall be
the name by which the harness invokes it.

| Attribute | Value |
| --- | --- |
| Rationale | A plugin changes the name a command is invoked by, and the pre-plugin content writes script paths under one harness's user directory. A reference that stopped resolving fails only when someone follows it. |
| Source | Analysis 2026-10-02, from the plugin naming rules of each harness |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-SKL-03.1** — Given the content a harness plugin delivers, when each skill name, command name,
  subagent name, and script invocation written in it is invoked as written, then it resolves in that
  harness.
