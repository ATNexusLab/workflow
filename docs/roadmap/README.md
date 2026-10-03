# Roadmap

Live status: the GitHub Project [workflow](https://github.com/orgs/ATNexusLab/projects/15) and the
[milestones](https://github.com/ATNexusLab/workflow/milestones).

## M1 — Claude Code

The Claude Code plugin, built from the canonical content, with everything the pre-plugin workflow holds.
GitHub Milestone: [M1](https://github.com/ATNexusLab/workflow/milestone/1).

Epics are built in the order listed.

| Epic | Issue | Covers |
| --- | --- | --- |
| Installable core: skills, commands and the verifier | [#1](https://github.com/ATNexusLab/workflow/issues/1) | FR-INS-01, FR-SKL-01 to FR-SKL-03, FR-VER-01, FR-VER-02, NFR-MNT-01, NFR-FLEX-06, NFR-SEC-01, NFR-SEC-02, BR-02, BR-03 |
| Contract in every session, on or off | [#2](https://github.com/ATNexusLab/workflow/issues/2) | FR-CTR-01 to FR-CTR-04, FR-INS-02, FR-INS-03, NFR-COMP-01, BR-04, BR-05 |
| Memory layer | [#3](https://github.com/ATNexusLab/workflow/issues/3) | FR-MEM-01 to FR-MEM-12, NFR-REL-01, NFR-REL-02, NFR-PERF-01, NFR-PERF-02, NFR-SEC-03, NFR-SEC-04 |
| Opt-in status line | [#4](https://github.com/ATNexusLab/workflow/issues/4) | FR-STL-01 to FR-STL-03 |
| Lifecycle and the M1 release | [#5](https://github.com/ATNexusLab/workflow/issues/5) | FR-INS-04 to FR-INS-07, FR-CTR-05, NFR-FLEX-01, NFR-FLEX-05, BR-01 |

Decisions behind the split, agreed on 2026-10-02:

- The architecture decision — how the canonical content becomes a plugin, with
  [OQ-01](../requirements/open-questions.md#oq-01), [OQ-04](../requirements/open-questions.md#oq-04), and
  [OQ-05](../requirements/open-questions.md#oq-05) — is an ADR inside the spec of #1, not an epic of its
  own.
- The mechanism that turns an optional component on or off is built in #2, with the first optional
  component. #3 and #4 reuse it.
- A requirement that cuts across epics belongs to the epic that builds its mechanism. Every later epic
  keeps it passing.

## Later milestones

Not split into epics yet. Each is planned when the previous harness's plugin is released
([BR-01](../requirements/business-rules.md#br-01)).

| Milestone | Harness | Requirements |
| --- | --- | --- |
| M2 | Cursor | NFR-FLEX-02, NFR-FLEX-07, NFR-COMP-02, NFR-COMP-03 |
| M3 | Antigravity CLI | NFR-FLEX-03 |
| M4 | Codex | NFR-FLEX-04 |

## Requirement coverage

Every approved requirement of a planned milestone maps to exactly one epic.

| Requirement | Epic | Milestone |
| --- | --- | --- |
| [FR-CTR-01](../requirements/functional/contract.md#fr-ctr-01) | #2 | M1 |
| [FR-CTR-02](../requirements/functional/contract.md#fr-ctr-02) | #2 | M1 |
| [FR-CTR-03](../requirements/functional/contract.md#fr-ctr-03) | #2 | M1 |
| [FR-CTR-04](../requirements/functional/contract.md#fr-ctr-04) | #2 | M1 |
| [FR-CTR-05](../requirements/functional/contract.md#fr-ctr-05) | #5 | M1 |
| [FR-SKL-01](../requirements/functional/skills.md#fr-skl-01) | #1 | M1 |
| [FR-SKL-02](../requirements/functional/skills.md#fr-skl-02) | #1 | M1 |
| [FR-SKL-03](../requirements/functional/skills.md#fr-skl-03) | #1 | M1 |
| [FR-VER-01](../requirements/functional/verifier.md#fr-ver-01) | #1 | M1 |
| [FR-VER-02](../requirements/functional/verifier.md#fr-ver-02) | #1 | M1 |
| [FR-MEM-01](../requirements/functional/memory.md#fr-mem-01) | #3 | M1 |
| [FR-MEM-02](../requirements/functional/memory.md#fr-mem-02) | #3 | M1 |
| [FR-MEM-03](../requirements/functional/memory.md#fr-mem-03) | #3 | M1 |
| [FR-MEM-04](../requirements/functional/memory.md#fr-mem-04) | #3 | M1 |
| [FR-MEM-05](../requirements/functional/memory.md#fr-mem-05) | #3 | M1 |
| [FR-MEM-06](../requirements/functional/memory.md#fr-mem-06) | #3 | M1 |
| [FR-MEM-07](../requirements/functional/memory.md#fr-mem-07) | #3 | M1 |
| [FR-MEM-08](../requirements/functional/memory.md#fr-mem-08) | #3 | M1 |
| [FR-MEM-09](../requirements/functional/memory.md#fr-mem-09) | #3 | M1 |
| [FR-MEM-10](../requirements/functional/memory.md#fr-mem-10) | #3 | M1 |
| [FR-MEM-11](../requirements/functional/memory.md#fr-mem-11) | #3 | M1 |
| [FR-MEM-12](../requirements/functional/memory.md#fr-mem-12) | #3 | M1 |
| [FR-INS-01](../requirements/functional/install.md#fr-ins-01) | #1 | M1 |
| [FR-INS-02](../requirements/functional/install.md#fr-ins-02) | #2 | M1 |
| [FR-INS-03](../requirements/functional/install.md#fr-ins-03) | #2 | M1 |
| [FR-INS-04](../requirements/functional/install.md#fr-ins-04) | #5 | M1 |
| [FR-INS-05](../requirements/functional/install.md#fr-ins-05) | #5 | M1 |
| [FR-INS-06](../requirements/functional/install.md#fr-ins-06) | #5 | M1 |
| [FR-INS-07](../requirements/functional/install.md#fr-ins-07) | #5 | M1 |
| [FR-STL-01](../requirements/functional/status-line.md#fr-stl-01) | #4 | M1 |
| [FR-STL-02](../requirements/functional/status-line.md#fr-stl-02) | #4 | M1 |
| [FR-STL-03](../requirements/functional/status-line.md#fr-stl-03) | #4 | M1 |
| [NFR-FLEX-01](../requirements/non-functional/flexibility.md#nfr-flex-01) | #5 | M1 |
| [NFR-FLEX-05](../requirements/non-functional/flexibility.md#nfr-flex-05) | #5 | M1 |
| [NFR-FLEX-06](../requirements/non-functional/flexibility.md#nfr-flex-06) | #1 | M1 |
| [NFR-COMP-01](../requirements/non-functional/compatibility.md#nfr-comp-01) | #2 | M1 |
| [NFR-SEC-01](../requirements/non-functional/security.md#nfr-sec-01) | #1 | M1 |
| [NFR-SEC-02](../requirements/non-functional/security.md#nfr-sec-02) | #1 | M1 |
| [NFR-SEC-03](../requirements/non-functional/security.md#nfr-sec-03) | #3 | M1 |
| [NFR-SEC-04](../requirements/non-functional/security.md#nfr-sec-04) | #3 | M1 |
| [NFR-MNT-01](../requirements/non-functional/maintainability.md#nfr-mnt-01) | #1 | M1 |
| [NFR-REL-01](../requirements/non-functional/reliability.md#nfr-rel-01) | #3 | M1 |
| [NFR-REL-02](../requirements/non-functional/reliability.md#nfr-rel-02) | #3 | M1 |
| [NFR-PERF-01](../requirements/non-functional/performance.md#nfr-perf-01) | #3 | M1 |
| [NFR-PERF-02](../requirements/non-functional/performance.md#nfr-perf-02) | #3 | M1 |
| [BR-01](../requirements/business-rules.md#br-01) | #5 | M1 |
| [BR-02](../requirements/business-rules.md#br-02) | #1 | M1 |
| [BR-03](../requirements/business-rules.md#br-03) | #1 | M1 |
| [BR-04](../requirements/business-rules.md#br-04) | #2 | M1 |
| [BR-05](../requirements/business-rules.md#br-05) | #2 | M1 |

## Sprints

- [Sprint 1](sprints/sprint-01.md) — an adopter installs the plugin in Claude Code from this repository
  and has the 14 skills, the 8 commands, and the verifier.
