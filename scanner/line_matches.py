import re
from collections.abc import Iterator
from pathlib import Path


def line_matches(
    root: Path, directory: str, patterns: list[re.Pattern[str]]
) -> Iterator[tuple[str, int, str]]:
    for file in sorted((root / directory).rglob("*")):
        if not file.is_file():
            continue
        relative = file.relative_to(root).as_posix()
        lines = file.read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines, start=1):
            for pattern in patterns:
                for match in pattern.finditer(line):
                    yield relative, number, match.group()
