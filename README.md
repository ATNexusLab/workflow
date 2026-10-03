# Workflow

A development workflow for coding agents: skills, a command for each step of the development loop, and a
read-only verifier. It installs as the plugin `tightship`.

## Install in Claude Code

In a Claude Code session:

```
/plugin marketplace add ATNexusLab/workflow
/plugin install tightship@atnexuslab
```

Or from a shell:

```
claude plugin marketplace add ATNexusLab/workflow
claude plugin install tightship@atnexuslab
```

Until the first release reaches `main`, add the catalog from a branch instead:
`ATNexusLab/workflow#<branch>`.

`claude plugin list` then shows `tightship@atnexuslab`, enabled. Every component is reached under the
plugin's name, such as the subagent `tightship:adversarial-verifier`.

## Documentation

What the workflow must do, how it is built, and what is planned: [docs/](docs/README.md).
