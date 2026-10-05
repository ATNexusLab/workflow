# Spec templates

Two profiles. Pick one at the start of `{{command:spec}}` — the profile is a header field, not a guess made later.

- **UI** — the feature has a screen, a modal, or a form a human operates.
- **API** — the feature is an endpoint, a job, or a service contract with no screen of its own.

A feature that has both gets **two** specs (one per profile) linked to the same epic — never one hybrid
document, because the field-level detail of each profile is what makes the spec testable.

Document language follows the repo's doc language. In a repository whose docs are not in English, the
status values, the header fields, the headings, and the Gherkin keywords below are written in that
language. **Identifiers, routes, table and column names stay in English** — they are code.

Every section is mandatory. A section that does not apply is written as `N/A` with one line saying why.
`N/A` proves it was considered; a missing section proves nothing.

---

## Profile: UI

````markdown
# <ID> — <Infinitive verb> <object> (<actor>)

> **Status:** draft
> **Profile:** UI
> **Module:** <where it lives in the repo>
> **Epic:** —
> **Requirements:** FR-<AREA>-NN, NFR-<CHAR>-NN
> **Sprint:** <N>

## Acceptance Criteria

### Visual reference

<Link to the prototype/mock, or `N/A — no prototype; layout defined by the rules below`>

### Screen specification

<Description of what the screen is: page, modal, drawer; what it shows on opening; what it lists.>

### Menu path

`Menu` → `Submenu` → `Feature`

### Roles and permissions

| Role / Action | Permission | Note |
| --- | --- | --- |
| <role that sees the feature> | `<PERMISSION>` | — |
| <specific action> | `<ACTION_PERMISSION>` | <what the permission unlocks> |

---

## Business rules

Numbered, one per behavior. Each rule closes three things: **when** it fires, **what** the system
does, and **which literal message** appears (in quotes, exact text). Numeric limits are numbers, never
"a reasonable limit".

### 1. Access restriction

- Access is restricted to users with the permission `<PERMISSION>`.
- **Validation:** <at which exact moment the permission is checked>. Without the permission, processing
  is blocked and the system shows:
  > "<literal message>"

  with a redirect to <destination>.

#### Flow origin

<Where the user arrives at this screen from — the listing, the menu action, the previous story.>

### 2. <Next rule>

### N. Persistence and audit

- **User boundary (visual):** <the action the user clicks>.
- **System action (internal):** writes to the audit log *who did it* (user/IP), *what they did*
  (<description of the operation and of the data changed>), and *when they did it* (UTC).

---

## Acceptance scenarios (Gherkin)

Minimum coverage: **1 happy path**, **1 alternative per dynamic behavior**, and **1 exception per
rule that can fail**. A business rule with no matching scenario is an untestable rule.

### Scenario 1 — <name> (happy path)

```gherkin
Given <initial state and permission>
And <precondition>
When <user action>
Then <observable result>
And <side effect: persistence, message, redirect>
```

### Scenario 2 — <name> (alternative path)

### Scenario 3 — <name> (exception path)

---

## Screen data dictionary (fields)

| Field name | Type | Enabled | Required | Rule / Validation |
| --- | --- | --- | --- | --- |
| `<Displayed label>` | <Dropdown / Text (N) / Date / Checkbox> | Yes / No / Conditional (<condition>) | Yes / No / Conditional | <data source, domain, ordering, limit, mask> |

## Screen actions

| Action name | Destination / Action | Activation rule | Associated messages |
| --- | --- | --- | --- |
| <Button label> | <what it runs and where it goes> | <always enabled / condition / permission required> | Success: "<literal>" · Error: "<literal>" |

---

## Architecture impact

<The building blocks, runtime scenarios, deployment, and concepts of `docs/architecture/` that this
feature creates or changes — each by the name the map uses.>

## Data model impact

<The entities, attributes, relations, and files/tables of `docs/data-model/` that this feature creates or
changes, or `N/A — <why>`.>

## Out of scope

- <What this spec deliberately does not cover, and where it will be handled.>

## Task breakdown

| # | Title | Scope | Acceptance criterion | Depends on |
| --- | --- | --- | --- | --- |
| 1 | <imperative issue title> | <files/layer the task touches> | <Scenario N, or rule N verified> | — |
| 2 | <...> | <...> | <...> | 1 |
````

---

## Profile: API

````markdown
# <ID> — <Infinitive verb> <resource>

> **Status:** draft
> **Profile:** API
> **Module:** <where it lives in the repo>
> **Epic:** —
> **Requirements:** FR-<AREA>-NN, NFR-<CHAR>-NN
> **Sprint:** <N>

## Acceptance Criteria

### Contract

| Method | Route | Auth / Role | Idempotent |
| --- | --- | --- | --- |
| `POST` | `/v1/<resource>` | `<ROLE>` | Yes / No |

### Request

| Field | Type | Required | Validation |
| --- | --- | --- | --- |
| `field` | `string` | Yes | <limit, format, domain> |

```json
{ "field": "example" }
```

### Response

**`201 Created`**

```json
{ "id": "uuid", "field": "example" }
```

| Status | When |
| --- | --- |
| `201` | <condition> |
| `400` | <condition> |
| `403` | <condition> |

### Roles and permissions

| Role | Permission | Note |
| --- | --- | --- |
| <role> | `<PERMISSION>` | <what it unlocks> |

---

## Business rules

Same discipline as the UI profile: numbered, with the trigger, the effect, and the literal error message.

### 1. Authorization

<Who can call, at which moment the check happens, what happens without the permission.>

### 2. <Domain rule>

### N. Persistence and audit

- **Tables/columns changed:** <list>.
- **Audit:** writes *who* (user/IP), *what* (<operation and data>), and *when* (UTC).
- **Events/integrations fired:** <list, or `N/A`>.

---

## Errors

| Code | HTTP | When | Message |
| --- | --- | --- | --- |
| `<ERROR_CODE>` | `400` | <exact condition> | "<literal message>" |

## Side effects

- **Persistence:** <what it writes, in which state>
- **Concurrency:** <what happens if the state changes between the read and the write>
- **Transaction:** <what is atomic with what>

---

## Acceptance scenarios (Gherkin)

Minimum coverage: **1 happy path**, **1 per error in the table above**, **1 for denied authorization**.

### Scenario 1 — <name> (happy path)

```gherkin
Given <actor> has the permission <PERMISSION>
And <state of the resource>
When they send `POST /v1/<resource>` with <payload>
Then the system responds `201`
And persists <what, in which state>
And writes the operation to the audit log
```

### Scenario 2 — <name> (exception)

---

## Architecture impact

<The building blocks, runtime scenarios, deployment, and concepts of `docs/architecture/` that this
feature creates or changes — each by the name the map uses.>

## Data model impact

<The entities, attributes, relations, and files/tables of `docs/data-model/` that this feature creates or
changes, or `N/A — <why>`.>

## Out of scope

- <What this spec deliberately does not cover.>

## Task breakdown

| # | Title | Scope | Acceptance criterion | Depends on |
| --- | --- | --- | --- | --- |
| 1 | <imperative issue title> | <files/layer the task touches> | <Scenario N verified> | — |
````

---

## Writing the task breakdown

The breakdown table is the contract `{{command:epic}}` publishes verbatim — it does not re-read the spec to invent
tasks. So the table has to hold up on its own:

- **One task = one delivery**: a sub-issue and one commit on the epic's branch, sized to be reviewed in
  one sitting. If a task cannot be verified without another task's code, it is half of one — merge
  them. A task too small to be worth its own review cycle joins its neighbour.
- **Order by dependency.** `Depends on` carries task numbers, never prose.
- **Every acceptance scenario in the spec maps to at least one task.** A scenario nobody owns is a feature
  nobody builds.
- Slice vertically along the repo's own architecture: one behavior through every part it crosses beats
  one part for every behavior.
