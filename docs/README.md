# Documentation

| Folder | Holds |
| --- | --- |
| [requirements/](requirements/README.md) | The versioned SRS: what the product must do |
| [architecture/](architecture/README.md) | The map of the system: context, strategy, and what is still undecided |
| [data-model/](data-model/README.md) | The entities the product stores and how they relate |
| [diagrams/](diagrams/README.md) | Every diagram, as an editable `.drawio.svg` |

Not present yet:

- `roadmap/` is created by the first sprint planning.
- `specs/` and `decisions/` are created by the first spec.

## Local site

From the repository root:

```
uvx zensical==0.0.67 serve --open
```

It serves the same folders at `http://localhost:8000`, with a sidebar and search. In VS Code, the task
`docs: serve` runs the same command. The site is never deployed.
