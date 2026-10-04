import re
from collections.abc import Mapping
from pathlib import PurePosixPath


def render(
    source: PurePosixPath, text: bytes, references: Mapping[str, str]
) -> tuple[bytes, list[str]]:
    token = re.compile(r"\{\{.*?(?:\}\}|$)")
    rendered: list[str] = []
    unresolved: list[str] = []
    for number, line in enumerate(text.decode().splitlines(keepends=True), start=1):
        unresolved += [
            f"{source}:{number}: {written} resolves to nothing"
            for written in token.findall(line)
            if written not in references
        ]
        rendered.append(token.sub(lambda found: references.get(found.group(), found.group()), line))
    return "".join(rendered).encode(), unresolved
