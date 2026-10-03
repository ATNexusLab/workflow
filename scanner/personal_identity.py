import re
import subprocess
from pathlib import Path

from scanner.line_matches import line_matches


def findings(root: Path) -> list[str]:
    log = subprocess.run(
        ["git", "-C", str(root), "log", "--format=%an%x00%ae%n%cn%x00%ce"],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout
    identities = set(log.splitlines()) - {"GitHub\0noreply@github.com"}

    patterns = [
        re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
        re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\)[\w.-]+"),
    ]
    for identity in sorted(identities):
        name, email = identity.split("\0")
        patterns.append(re.compile(re.escape(email)))
        patterns += [
            re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
            for word in re.findall(r"[^\W\d_]{4,}", name)
        ]

    found = [
        f'{file}:{line}: personal identity "{match}" (NFR-SEC-01)'
        for file, line, match in line_matches(root, "plugins", patterns)
    ]
    return list(dict.fromkeys(found))
