import re
from pathlib import Path

from scanner.line_matches import line_matches


def findings(root: Path) -> list[str]:
    terms = (root / "adapters" / "neutrality-terms.txt").read_text(encoding="utf-8").splitlines()
    patterns = [re.compile(term) for term in terms if term]
    return [
        f'{file}:{line}: harness term "{match}" (NFR-FLEX-06)'
        for file, line, match in line_matches(root, "canonical", patterns)
    ]
