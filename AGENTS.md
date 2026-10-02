# Workflow — repository contract

Additive to the global contract. What this repository must do is the SRS in
[docs/requirements/](docs/requirements/README.md); the map of the docs is [docs/README.md](docs/README.md).

## Stack

- Python 3.10 or newer for every script.
- Markdown for the workflow's content and for the docs.
- Docs site: Zensical 0.0.67.
- No package manager and no dependency manifest: the repository installs nothing.

## Language & scripts

- Application code is Python.
- A new script is Python, never shell or PowerShell: one copy of each script serves macOS, Linux, and
  Windows ([NFR-MNT-01](docs/requirements/non-functional/maintainability.md#nfr-mnt-01)).

## Conventions

- A Python tool is run as `uvx <tool>==<version>`, with the version pinned in the command. Nothing is
  installed with pip.
- In the SRS, every requirement heading is preceded by `<a id="<id in lowercase>"></a>`, and links to a
  requirement use that id.
- The backlog is the GitHub Project [workflow](https://github.com/orgs/ATNexusLab/projects/15), in
  one-week sprints.

## Commands

| Gate | Command |
| --- | --- |
| Static analysis | Pending: Ruff 0.16.10, from the first Python file |
| Type checking | Pending: mypy 2.4.0, from the first Python file |
| Formatting | Pending: Ruff 0.16.10, from the first Python file |
| Build | Pending: whether one exists is part of the architecture decision |
| Tests | Pending: pytest 9.1.1, from the first test |
| Docs site | `uvx zensical==0.0.67 build` |
| Run the docs site | `uvx zensical==0.0.67 serve --open` |

Both docs commands run from the repository root.

## Architecture

Not decided. How the canonical content becomes one plugin per harness is settled by an ADR in the M1
spec, and this section is written from that ADR. Until then, no canonical or plugin file has a place.

## Branches

- `develop` is the integration branch; every pull request targets it.
- `main` receives only releases from `develop`, as merge commits. It is the branch adopters install from.
- Neither branch has a protection rule on GitHub; both rules above are convention.
- A pull request into `develop` links no issue, so an issue's In Review and Staging are set with
  `gh project item-edit`.

## Language

Docs and everything a plugin installs are in English
([BR-03](docs/requirements/business-rules.md#br-03)).

## Gotchas

None observed yet.
