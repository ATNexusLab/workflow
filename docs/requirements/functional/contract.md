# Contract — `CTR`

Delivery of the working contract into the agent's context.

<a id="fr-ctr-01"></a>
## FR-CTR-01 — Contract in every session

> As an adopter, I want the contract in the agent's context without asking for it, so that every session
> follows the workflow's rules.

The plugin shall keep the complete text of the enabled contract in the agent's context for the whole of
every session, without any action by the adopter.

| Attribute | Value |
| --- | --- |
| Rationale | The contract is what turns a set of skills into a workflow. A plugin has no always-on instruction file in Claude Code, and Claude Code cuts any single injected text over 10,000 characters ([constraints](../overview.md#constraints)). |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-CTR-01.1** — Given the plugin installed with the contract enabled, when a session starts, then
  every section of the contract is in the agent's context before the first prompt is processed.
- **FR-CTR-01.2** — Given a running session, when the harness rebuilds the context by resume, clear, or
  compaction, then every section of the contract is in the context that follows.
- **FR-CTR-01.3** — Given the contract in context, when its text is compared with its source in this
  repository, then no section is shortened, replaced by a preview, or replaced by a pointer to a file.

<a id="fr-ctr-02"></a>
## FR-CTR-02 — Contract can be turned off

> As an adopter, I want to turn the contract off, so that I can use the skills and commands under my own
> rules.

The plugin shall deliver no contract text while the contract is disabled.

| Attribute | Value |
| --- | --- |
| Rationale | The contract is one person's rules. An adopter who works under other rules still gets the rest of the workflow. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-CTR-02.1** — Given the contract disabled, when a session starts, then no section of the contract is
  in the agent's context.

<a id="fr-ctr-03"></a>
## FR-CTR-03 — Contract matches the enabled components

> As an adopter without a vault, I want the contract free of memory rules, so that the agent is never told
> to use something I turned off.

The delivered contract shall contain the rules of an optional component only while that component is
enabled.

| Attribute | Value |
| --- | --- |
| Rationale | In the pre-plugin install, an adopter without a vault deletes the contract's memory section by hand. Left in place, it orders the agent to run a script that has nowhere to write. |
| Source | Pre-plugin install guide, section "Make it theirs"; maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-CTR-03.1** — Given memory disabled and the contract enabled, when a session starts, then the
  contract in context contains no rule that refers to the vault.
- **FR-CTR-03.2** — Given memory enabled and the contract enabled, when a session starts, then the
  contract in context contains every memory rule.

<a id="fr-ctr-04"></a>
## FR-CTR-04 — Every pre-plugin rule is carried over

> As the maintainer, I want every rule I work under today in the plugin's contract, so that moving to the
> plugin loses nothing.

The contract the Claude Code plugin delivers shall carry every rule of the pre-plugin contract at the
baseline.

| Attribute | Value |
| --- | --- |
| Rationale | The first release is everything the workflow holds today. A rule dropped in the move would go unnoticed until the agent stopped following it. Rules that only make sense in Claude Code are still delivered there, outside the harness-neutral canonical content ([NFR-FLEX-06](../non-functional/flexibility.md#nfr-flex-06)). |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-CTR-04.1** — Given the pre-plugin contract at the [baseline](../overview.md#assumptions-and-dependencies),
  when each of its rules is looked up in the contract the Claude Code plugin delivers with every optional
  component enabled, then the rule is present, or the spec that removed it names the rule and the reason.

<a id="fr-ctr-05"></a>
## FR-CTR-05 — Reduced mode is documented

> As an adopter who turned the contract off, I want to know which rules stopped applying, so that I do not
> expect a command to enforce them.

The install guide shall state which rule groups apply only while the contract is enabled.

| Attribute | Value |
| --- | --- |
| Rationale | Several commands apply rules that live only in the contract. With the contract off they still run, and the adopter needs to know what they no longer enforce. Copying those rules into the commands would give each rule two homes. |
| Source | Maintainer, analysis 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **FR-CTR-05.1** — Given the install guide of a harness, when the adopter reads its section on the
  contract, then it names every rule group that is absent with the contract disabled.
