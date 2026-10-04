---
name: grilling
description: Use before planning anything non-trivial or ambiguous, or on any 'grill' trigger — state the assumptions the plan rests on so the user corrects the ones that change the work.
---

# Grilling

Decide everything that can be decided, then show where you might be wrong.

**This is not an interview.** The output is a short list of assumptions the user corrects in one pass.
A question is what happens *after* a correction leaves a fork you genuinely cannot settle.

## Triage — three buckets, and only one of them is a question
| Bucket | What to do |
|---|---|
| **A fact** | Look it up — the repo, the history, the tools. Never ask what the environment can answer. |
| **A routine call** | Decide it, list it as an assumption, move on. Reversible, cheap, or with an obvious default. |
| **Changes the shape of the work** | This, and only this, goes on the list. |

## What earns a place on the list
One test: **would a different answer change what gets built** — the work itself, its size, or its
structure? If two answers lead to the same code, it does not go on the list.

**A preference is not a shape.** "Which wording do you prefer" and "which colour" change nothing about
the work; decide them and move on. "Does this export the current page or the whole result set" changes
whether a background job exists — that is a shape.

## The list
Three to seven items. Each one is a **statement, not a question**, and carries a line saying what
changes if it is wrong:

```
1. Export is CSV, not a spreadsheet format.
   If wrong: a library, cell formatting, and a different test surface.
2. Exports the current page, not the whole result set.
   If wrong: needs a background job and a delivery path — different size of work.
3. Columns are fixed, not user-configurable.
4. Permission is the same one that grants seeing the list.
```

The consequence line is what makes the list correctable in ten seconds. Without it the user has to
reconstruct your reasoning before they can disagree with it.

## After the list
- **Only what the user contests becomes a question.** One at a time, and only when the correction
  leaves a fork you cannot settle yourself.
- **A second round happens only if a correction opened a new shape-changing unknown.** Two rounds is
  the normal ceiling. When nothing remaining can change the shape, the grilling is over — say so and
  move to the plan.

## An answer is not a requirement
This is the rule that keeps a grilling from manufacturing scope.

- **"That would be nice" is not scope.** Only what the user states as required becomes required.
  Everything else stays out and can be added later, deliberately, as its own piece of work.
- **Never invent an option just to have something to ask about.** A question that exists to look
  thorough costs a decision the user then has to live with.
- The point of a grilling is to *remove* uncertainty, not to accumulate commitments.

## The output
The confirmed list becomes the header of the plan or the spec — written down, not left in the
conversation. It survives compaction, and nothing on it gets asked twice.

## Never do
- Ask what you could have looked up.
- Ask a question you would answer the same way regardless of the reply.
- Put a preference on the list, or let the list run past ~7 items.
- Keep going after the shape stopped moving.
- Turn an answer into scope.
- Walk a decision tree branch by branch — that extracts a decision per branch, including branches the
  work would never reach.
