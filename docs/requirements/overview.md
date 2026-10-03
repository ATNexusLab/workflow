# Overview

## Stakeholders

| Role | Who | Interest |
| --- | --- | --- |
| Maintainer | The author of the workflow and the only editor of this repository | Edits each piece once and uses the same workflow in all four harnesses |
| Adopter | Anyone who installs the plugin, the maintainer included | Installs with the harness's own mechanism, chooses the optional components, and is never taken for the maintainer |
| Harness vendors | Anthropic, Cursor, Google, OpenAI | Define the plugin formats and limits the product must follow; not consulted |

## Operating environment

- **Operating systems:** macOS, Linux, Windows.
- **Harnesses**, with the version observed on 2026-10-02:

  | Harness | Version observed | Milestone |
  | --- | --- | --- |
  | Claude Code | 2.1.287 | M1 |
  | Cursor | 3.21.18 (editor); its command-line agent not installed | M2 |
  | Antigravity CLI | 1.2.14 | M3 |
  | Codex | 0.160.0 | M4 |

  The minimum supported version of each harness is [OQ-07](open-questions.md#oq-07).
- **Prerequisites carried over from the pre-plugin workflow:** Python 3.10 or newer and git for the
  memory layer; for the status line, `jq` on macOS and Linux and PowerShell 7 or newer on Windows.
- **The vault:** a git repository on the adopter's machine, at a location the adopter chooses
  ([FR-MEM-08](functional/memory.md#fr-mem-08)). The pre-plugin workflow fixes it at `~/ai-memory`. A git
  remote for it is optional; without one, the functions that reach a remote say so
  ([FR-MEM-11](functional/memory.md#fr-mem-11)).

## Constraints

Each constraint was read in the vendor's documentation on 2026-10-02. Those marked *tested* were also
reproduced on the version above.

| Constraint | Source |
| --- | --- |
| Claude Code does not load an instruction file placed at a plugin's root. | [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) |
| Claude Code caps each text a hook places in context at 10,000 characters. Over the cap, the agent receives a preview of at most 2,000 characters and a file path it is not asked to read. The cap is measured per hook output, and the agent receives every output. *Tested:* three outputs of 9,797 characters arrived whole; one of 11,997 arrived cut. | [Hooks reference](https://code.claude.com/docs/en/hooks) |
| The pre-plugin contract is 20,137 characters, so one hook output cannot carry it. | Measured at the baseline below |
| From a Claude Code plugin's settings, only the default agent and the subagent status line take effect. A plugin cannot set the session status line or permissions. | [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) |
| A Claude Code plugin's component paths cannot leave the plugin root. | [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) |
| Claude Code asks the adopter for the values a plugin declares as user configuration when the plugin is enabled. | [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) |
| Claude Code shows the user-configuration dialog in an interactive install. An install from the shell never prompts and leaves the options unset. | [Plugin components](https://code.claude.com/docs/en/plugins/components) |
| A Claude Code marketplace other than the official ones has auto-update off until the adopter turns it on. | [Install plugins](https://code.claude.com/docs/en/plugins/install) |

The limits of Cursor, Antigravity CLI, and Codex were researched on 2026-10-02 and not re-verified.
They are recorded as [open questions](open-questions.md), each settled by that harness's spec.

## Assumptions and dependencies

- **Baseline of the pre-plugin workflow:** commit `519cc2a` (2026-10-01) of the maintainer's private
  configuration repository. It holds the contract, 14 skills, 8 commands, the verifier, the memory
  script, the status line scripts, and the vault template. Every parity requirement refers to it.
- Each harness keeps the plugin format its documentation describes on the day its milestone starts.
- An adopter can reach this public repository.
- The companion plugins are maintained by third parties and can change without notice.
