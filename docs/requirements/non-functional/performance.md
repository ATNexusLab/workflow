# Performance efficiency — `PERF`

Time the plugin adds to a session. Baseline, measured on 2026-10-02 on macOS with a vault of 210 notes:
the pre-plugin memory script takes 0.04 s at session start and 0.03 s per prompt.

<a id="nfr-perf-01"></a>
## NFR-PERF-01 — Session-start overhead

The plugin's session-start scripts shall complete in at most 1 second in total, with a vault of 1,000
notes.

| Attribute | Value |
| --- | --- |
| Rationale | The scripts run before the adopter can type. The threshold leaves room for a vault five times the measured one and for the contract's delivery. |
| Source | Pre-plugin contract, "Definition of done" (performance sanity); threshold proposed in analysis, 2026-10-02 |
| Priority | Should |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-PERF-01.1** — Given every optional component enabled and a vault of 1,000 notes, when a session
  starts, then the plugin's session-start scripts complete in at most 1 second in total.

<a id="nfr-perf-02"></a>
## NFR-PERF-02 — Per-prompt overhead

The script the plugin runs on each prompt shall complete in at most 200 milliseconds.

| Attribute | Value |
| --- | --- |
| Rationale | It runs on every prompt of every session, so its cost is paid more often than any other. |
| Source | Pre-plugin contract, "Definition of done" (performance sanity); threshold proposed in analysis, 2026-10-02 |
| Priority | Should |
| Status | approved |
| Milestone | M1 |
| Since | v1.0.0 |

**Acceptance criteria**
- **NFR-PERF-02.1** — Given memory enabled, when a prompt is submitted, then the plugin's per-prompt
  script completes in at most 200 milliseconds.
