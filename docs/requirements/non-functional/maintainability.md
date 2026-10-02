# Maintainability — `MNT`

One authored copy per piece.

<a id="nfr-mnt-01"></a>
## NFR-MNT-01 — One authored copy per piece

An edit to a workflow piece shall reach every released harness plugin by changing exactly 1 authored copy
of that piece in this repository.

| Attribute | Value |
| --- | --- |
| Rationale | Four harness plugins maintained by hand are four copies that drift. The earlier manual port to a second harness already holds a contract of a different size from the original. |
| Source | Maintainer, elicitation 2026-10-02 |
| Priority | Must |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-MNT-01.1** — Given a change to one piece, when the commit's authored files are listed, then the
  piece is changed in exactly 1 place.
- **NFR-MNT-01.2** — Given that commit, when each released harness plugin is installed from it, then each
  delivers the changed piece.
