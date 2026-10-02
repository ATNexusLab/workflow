# Non-functional requirements

One file per ISO/IEC 25010:2023 characteristic that has a requirement.

| Characteristic | Code | Covers |
| --- | --- | --- |
| [Flexibility](flexibility.md) | `FLEX` | The four harnesses, the three operating systems, harness-neutral content |
| [Compatibility](compatibility.md) | `COMP` | Companion plugins, one vault across harnesses, no double loading |
| [Security](security.md) | `SEC` | Identity, secrets, network access, where the plugin writes |
| [Maintainability](maintainability.md) | `MNT` | One authored copy per piece |
| [Reliability](reliability.md) | `REL` | Behavior when a prerequisite or the vault is missing |
| [Performance efficiency](performance.md) | `PERF` | Time the plugin adds to a session |

Characteristics with no requirement:

- **Functional suitability (`FUNC`)** — covered by the [functional requirements](../functional/README.md).
- **Interaction capability (`INTR`)** — the product has no interface of its own; what it tells the adopter
  on failure is [NFR-REL-02](reliability.md#nfr-rel-02).
- **Safety (`SAFE`)** — the product controls nothing that can harm people or property.
