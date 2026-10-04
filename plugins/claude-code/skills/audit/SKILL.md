---
description: Full audit of a path or the current diff — security, performance, architecture, organization, maintainability
argument-hint: "[path, module, or 'diff' — defaults to the working diff] [--only sec|perf|arch|maint]"
---

Run a full audit on: $ARGUMENTS (if empty, audit the current working diff via `git diff`).

Dispatch one `general-purpose` subagent per axis, **in parallel, in one message**, each with the same
target and read-only (report findings, never edit). `--only <axis>` restricts the run to the named axes;
without it, all four run. Each agent loads its lens skill first.

| Axis | Lens |
|---|---|
| **sec** | `tightship:security-audit` — map each touched surface to its threat cases (auth, input/output, mutation/state, uploads, network, crypto/secrets, dependencies). |
| **perf** | `tightship:performance-analysis` — all three layers: frontend (critical path, interaction cost, what ships), backend (serial I/O, work inside the request, timeouts and retries), database (query count per row, plan at real volume, pool and lock waits). Evidence over speculation; no premature optimization. |
| **arch** | `tightship:architecture-reading` — adherence to the repo `AGENTS.md` Architecture section and its ADRs: layer/boundary violations, leaked dependencies, misplaced files. |
| **maint** | the contract's **Code I write** — organization and maintainability: duplication, mixed responsibility, god-objects, dead code, magic/hidden behavior, speculative abstraction, type-safety escapes, opaque names. |

`/tightship:audit` targets an arbitrary path or diff. For the current branch alone, `/security-review` and
`/code-review` cover sec and maint natively and run in this session instead.

**Conditional lenses.** Three more skills load when the target calls for them:

- **API contract** (HTTP/RPC endpoints, a GraphQL schema, webhook or event payloads) → **sec** and **arch**
  also load `tightship:api-design` and judge the contract itself: authz per endpoint, unknown-field rejection, error
  shape and leakage, bounded collections, idempotency and concurrency, breaking changes inside a version.
- **Data layer** (schema, migrations, or the code that queries them) → **sec**, **perf**, and **arch** also
  load `tightship:database-design`: invariants left to application code, predicates that can yield `NULL`, tenancy
  and privileges, indexes that no access pattern matches, and migrations that break the running version.
- **UI surface** (screens, components, forms, client-side routing) → **sec** and **maint** also load
  `tightship:frontend-architecture`: rules enforced only on the client, secrets past the server/client boundary,
  remote data copied into global state, shareable view state missing from the URL, async surfaces without
  all four states, and keyboard or focus gaps.

A skill is the lens, never the ceiling. It lists what is known to go wrong — it does not bound what can.
A real problem outside its checklist is still a finding, reported with the same weight.

Every agent reports findings ranked **Critical / High / Medium / Low / Informational**, each with:
location (`file:line`) · what is wrong · concrete fix · rough effort.

## Consolidate

Merge the four reports into one ranked list, deduped (the same code often trips more than one axis —
keep it once, tagged with every axis it hits). Rank by severity across axes, not per-axis.

## After the report

Deliver the consolidated report and stop. Nothing is fixed and nothing is filed until I say which
findings are fixed now, which become issues, and which are dropped — a comment on an existing issue
counts as filing.

- For each finding, say whether an issue already owns it (search the backlog via `gh`) or none does.
- What I send to a fix follows the dev loop (tests first where it matters).
- What I send to an issue: security findings → labeled `security-debt` (surface · risk · fix ·
  severity); the other axes → labeled `tech-debt`, same shape.
- A deliberate, documented trade-off is not debt — it becomes a decision note, not an issue.
- Once I have decided, summarize: fixed vs deferred (with issue numbers), broken out per axis.

If a finding needs an architectural change, flag it so a `/tightship:spec` ADR is written before implementing.
