# Changelog

## 1.1.0 — 2026-10-03

Handoff and sync commands. Change request [#12](https://github.com/ATNexusLab/workflow/issues/12). The
maintainer approved every requirement added in the validation of the same day, so each one enters with
Status `approved`.

**Added**

- FR-MEM-09 and FR-MEM-10: release a handoff to the vault's remote, and fetch the latest one from it.
- FR-MEM-11 and FR-MEM-12: one sync that synchronizes the vault with its remote and sends the commits of
  the project's current branch.
- FR-MEM-07.3: with memory disabled, none of the three functions runs.
- NFR-SEC-03.2 and NFR-SEC-04.2.
- OQ-13: how the sync reconciles a note changed on both sides.

**Changed**

- NFR-SEC-03: the plugin's only network connections are those to the git remotes of the vault and of the
  project, made by the three functions on the adopter's invocation. It was 0 connections.
- NFR-SEC-04: the git data of the project repository becomes the fourth location the plugin writes to,
  during a sync. It was 3 locations.
- Scope and glossary: the memory layer includes the functions that reach a remote; a command is no longer
  only a step of the development loop.

## 1.0.1 — 2026-10-02

Wording. Change request [#6](https://github.com/ATNexusLab/workflow/issues/6).

**Changed**

- BR-03: the rationale names the four pre-plugin pieces that carry Portuguese, where it counted one. The
  rule is unchanged.

**Settled**

- OQ-01, OQ-04, and OQ-05, by the [spec of epic #1](../specs/installable-core.md) and
  [ADR 0001](../decisions/0001-canonical-content-rendered-into-one-plugin-per-harness.md).

## 1.0.0 — 2026-10-02

Kickoff. First version of the SRS, from the elicitation and analysis held with the maintainer on
2026-10-02. The maintainer approved every requirement in the validation of the same day, so each one
enters with Status `approved`.

**Added**

- Contract: FR-CTR-01 to FR-CTR-05.
- Skills and commands: FR-SKL-01 to FR-SKL-03.
- Verifier: FR-VER-01, FR-VER-02.
- Memory: FR-MEM-01 to FR-MEM-08.
- Installation: FR-INS-01 to FR-INS-07.
- Status line: FR-STL-01 to FR-STL-03.
- Flexibility: NFR-FLEX-01 to NFR-FLEX-07.
- Compatibility: NFR-COMP-01 to NFR-COMP-03.
- Security: NFR-SEC-01 to NFR-SEC-04.
- Maintainability: NFR-MNT-01.
- Reliability: NFR-REL-01, NFR-REL-02.
- Performance efficiency: NFR-PERF-01, NFR-PERF-02.
- Business rules: BR-01 to BR-05.
- Open questions: OQ-01 to OQ-12. OQ-03 and OQ-12 were settled during validation.
