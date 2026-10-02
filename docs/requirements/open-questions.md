# Open questions

Undecided items. Each one leaves this file for a link to the spec or decision that settled it.

Questions OQ-08 to OQ-11 rest on research done on 2026-10-02 that was not re-verified; the first step of
each is to check the fact against the harness's documentation and installed version.

| ID | Question | Affects | Settled by |
| --- | --- | --- | --- |
| <a id="oq-02"></a>OQ-02 | Why did an adopter's agent take them for the maintainer? Ruled out so far: the 46 tracked files of the pre-plugin workflow contain no name, email, or home path of the maintainer, and the adopter uses a vault of their own. | [NFR-SEC-01](non-functional/security.md#nfr-sec-01) | Reproduction on the adopter's machine |
| <a id="oq-06"></a>OQ-06 | What is the role of the vault template's preferences file? Its text calls it the canonical cross-tool contract that every harness renders from, which contradicts [BR-02](business-rules.md#br-02). | [FR-MEM-06](functional/memory.md#fr-mem-06), [BR-02](business-rules.md#br-02) | Maintainer |
| <a id="oq-07"></a>OQ-07 | What is the minimum supported version of each harness? | [NFR-FLEX-01](non-functional/flexibility.md#nfr-flex-01) to [NFR-FLEX-04](non-functional/flexibility.md#nfr-flex-04) | Each harness's spec |
| <a id="oq-08"></a>OQ-08 | Cursor: is the target the editor, the command-line agent, or both? Whether a plugin's always-on rule loads in the command-line agent is not documented. | [NFR-FLEX-02](non-functional/flexibility.md#nfr-flex-02), [FR-CTR-01](functional/contract.md#fr-ctr-01) | M2 spec |
| <a id="oq-09"></a>OQ-09 | Antigravity CLI: it has no session-start and no prompt-submit event, a 24,000-byte cap per rule file, no version field in its plugin manifest, and no documented catalog other than its curated one. How are the memory context, the checkpoint, the whole contract, release identification, and installation delivered? | [NFR-FLEX-03](non-functional/flexibility.md#nfr-flex-03), [FR-CTR-01](functional/contract.md#fr-ctr-01), [FR-MEM-01](functional/memory.md#fr-mem-01), [FR-MEM-02](functional/memory.md#fr-mem-02), [FR-INS-01](functional/install.md#fr-ins-01), [FR-INS-04](functional/install.md#fr-ins-04) | M3 spec |
| <a id="oq-10"></a>OQ-10 | Codex: a subagent is a file outside the plugin, plugin hooks run only after the adopter trusts them, and a plugin carries no always-on text. How are the verifier, the hooks, and the contract delivered? | [NFR-FLEX-04](non-functional/flexibility.md#nfr-flex-04), [FR-VER-01](functional/verifier.md#fr-ver-01), [FR-CTR-01](functional/contract.md#fr-ctr-01) | M4 spec |
| <a id="oq-11"></a>OQ-11 | Can Cursor, Antigravity CLI, and Codex show a status line a plugin provides? | [FR-STL-01](functional/status-line.md#fr-stl-01) | Each harness's spec |

## Settled

| ID | Question | Settled by |
| --- | --- | --- |
| <a id="oq-01"></a>OQ-01 | What is the plugin's name? | [Epic 1 spec](../specs/installable-core.md): `tightship`, installed as `tightship@atnexuslab` |
| OQ-03 | In which state does each optional component start when the adopter makes no choice? | [FR-INS-02.3](functional/install.md#fr-ins-02): enabled, when the harness could not ask |
| <a id="oq-04"></a>OQ-04 | Are the commands authored as skills in the canonical content? | [ADR 0001](../decisions/0001-canonical-content-rendered-into-one-plugin-per-harness.md): no, a command is authored as a command, and each harness decides how to package it |
| <a id="oq-05"></a>OQ-05 | How does the canonical content name a capability that is native to one harness, and where is each harness's equivalent stated? | [ADR 0001](../decisions/0001-canonical-content-rendered-into-one-plugin-per-harness.md): as a `{{harness:<key>}}` token, with each harness's equivalent in `adapters/<harness>/terms/<key>.md` |
| OQ-12 | Is the vault's location fixed or chosen by the adopter? | [FR-MEM-08](functional/memory.md#fr-mem-08): chosen by the adopter |
