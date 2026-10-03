import re
import subprocess
from pathlib import Path, PurePosixPath


def findings(root: Path) -> list[str]:
    tracked = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout.split("\0")

    found: list[str] = []
    for file in sorted(filter(None, tracked)):
        name = PurePosixPath(file).name
        if re.fullmatch(r"\.env(\..+)?", name) and name not in {".env.example", ".env.template"}:
            found.append(f"{file}: environment file with values is tracked (NFR-SEC-02)")
        elif re.fullmatch(r"mem-\d+-.+\.md", name):
            found.append(f"{file}: vault note is tracked (NFR-SEC-02)")
    return found
