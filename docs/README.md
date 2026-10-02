# Documentation

| Folder | Holds |
| --- | --- |
| [requirements/](requirements/README.md) | The versioned SRS: what the product must do |
| [architecture/](architecture/README.md) | The map of the system: context, strategy, and what is still undecided |
| [data-model/](data-model/README.md) | The entities the product stores and how they relate |
| [roadmap/](roadmap/README.md) | Milestones, their epics, requirement coverage, and each sprint's plan and result |
| [specs/](specs/README.md) | One spec per epic, written before its code |
| [decisions/](decisions/README.md) | The architecture decisions, one ADR each |
| [diagrams/](diagrams/README.md) | Every diagram, as an editable `.drawio.svg` |

## Local site

From the repository root:

```
uvx zensical==0.0.67 serve --open
```

It serves the same folders at `http://localhost:8000`, with a sidebar and search. In VS Code, the task
`docs: serve` runs the same command. The site is never deployed.
