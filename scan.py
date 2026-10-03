import sys
from pathlib import Path

from scanner import harness_terms, personal_identity, tracked_files


def findings(root: Path) -> list[str]:
    return [
        *harness_terms.findings(root),
        *personal_identity.findings(root),
        *tracked_files.findings(root),
    ]


if __name__ == "__main__":
    found = findings(Path(__file__).resolve().parent)
    if found:
        sys.exit("\n".join(found))
    print(
        "Scan passed: 0 harness terms, 0 personal identities, 0 environment files, 0 vault notes."
    )
