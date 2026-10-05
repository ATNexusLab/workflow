---
description: Review someone else's PR — a briefing (what for / what / how) plus explained findings, without what another PR already solved
argument-hint: "[PR number or URL] [--only sec|perf|arch|maint]"
---

Review the PR: $ARGUMENTS

This command **explains the PR before judging it** and **never publishes anything on GitHub**. The output
is a briefing in the repository's doc language in the chat, for me to read and then comment on my own.
`gh pr review`, `gh pr comment`, `gh pr merge`, `gh pr edit`, and `git push` are forbidden here, even if
the output seems to ask for them.

## Phase 0 — prepare

1. Dirty tree (`git status --porcelain` not empty) → **stop** and say what is pending. Do not stash,
   do not discard.
2. `git fetch origin --prune`.
3. `gh pr view <n> --json number,title,body,author,baseRefName,headRefName,isDraft,commits,files,closingIssuesReferences,url`.
4. Signs of an experiment — draft, idle for days, no linked issue, automated author, a new isolated
   folder → ask in one line whether the PR is for real before auditing.
5. `gh pr checkout <n>`.
6. `BASE=origin/<baseRefName>` — the base is the one **the PR declares**, never an assumed `main`.
   `MERGE_BASE=$(git merge-base $BASE HEAD)`.
7. The review diff is **`git diff $MERGE_BASE...HEAD`** and nothing else. Nothing the base moved on to
   afterwards counts as the PR's authorship.

At the end of the command, I stay on the PR's branch — say so in one line, so I can already run the
application.

## Phase 1 — briefing

Written for someone who has never seen the PR. In this order:

**What for** — the goal in 2–3 lines, taken from the description, the linked issue
(`closingIssuesReferences`, read with `gh issue view`), and the commit messages. Each statement is
marked `[declared]` when it came from the author or `[inferred]` when it was deduced from the diff. Never
present a deduction from the diff as the author's declared intent.

**What changed** — by module or area, one line per group. Never a list of loose files.

**How** — the implementation decisions the author made: the pattern they chose, where they put the
code, what they reused against what they rewrote, and the points where doing it differently would have
been reasonable. This is the section I cannot extract on my own by reading the diff on GitHub.

**Risk profile** — number of files, layers crossed, and which sensitive surfaces the PR touches: auth,
authorization, database migration, money, env/secrets, upload, the server/client boundary.

## Phase 2 — base drift

`git log --oneline $MERGE_BASE..$BASE -- <the PR's files>`

Lists the files where the base moved on after the starting point. It serves two purposes: warning that
the PR needs a rebase, and feeding the filter of Phase 4.

## Phase 3 — findings

Dispatch the subagents of `{{command:audit}}` **in parallel, in a single message**, all with the same target:
`git diff $MERGE_BASE...HEAD`. `--only <axis>` narrows the round.

| Axis | Lens |
|---|---|
| **sec** | `{{skill:security-audit}}` |
| **perf** | `{{skill:performance-analysis}}` |
| **arch** | `{{skill:architecture-reading}}` |
| **maint** | **Code I write** of the contract |

One {{harness:general-agent}} per axis, read-only, each loading its lens before reading the diff.

The conditional lenses of `{{command:audit}}` apply: API contract → `{{skill:api-design}}`; data layer →
`{{skill:database-design}}`; UI surface → `{{skill:frontend-architecture}}`. The lens is the angle, never the ceiling.

## Phase 4 — time filter

**No finding reaches the report without passing both tests.** This is the point of the command: time
spent discussing what was already handled is time lost.

1. **Already solved on the current base** — did the finding's lines change between `$MERGE_BASE` and `$BASE`?
   `git log -L<start>,<end>:<file> $MERGE_BASE..$BASE`, with `git log -S'<snippet>' $MERGE_BASE..$BASE`
   as a net for code that moved. Read the change: if it covers the finding, discard it as
   *solved in `<sha>` (PR #N)*.
2. **Already being handled in an open PR** — `gh pr list --state open --json number,title,headRefName,files`.
   Cross by file with the finding's files; for each PR that crosses, read **only the overlapping hunks**
   of `gh pr diff <m>`. If it attacks the same point, discard it as *being handled in #M*.
   One open PR that already attacks the problem is enough — the problem is already moving elsewhere.

Discarded is not deleted: it goes to the **Discarded and why** section, at the end of the report, with
the reason and the reference. Out of the way, but auditable.

## Phase 5 — output

Each surviving finding, ranked by severity across axes and deduplicated (the same code often trips
more than one axis — kept once, marked with all of them):

- **what it is** — one sentence
- **why it matters in this PR** — the concrete effect, not the generic rule
- **where** — `path:line` with the snippet
- **ready comment** — the text in the repository's doc language for me to paste on GitHub, already in a
  review tone
- **scope** — `in scope` when the PR caused the problem or made it reachable; `adjacent` when it is
  pre-existing and the PR only brushed against it. Adjacent becomes an issue, and the one who decides is
  me — the command proposes.

Close with a **recommended verdict** in one line: approve · request changes · talk first. It is a
recommendation. The action on GitHub is always mine.
