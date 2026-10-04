from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Literal


@dataclass(frozen=True)
class Piece:
    kind: Literal["agents", "skills", "commands"]
    name: str
    source: PurePosixPath
    text: bytes
    supporting: dict[PurePosixPath, bytes]


def read_pieces(canonical: Path) -> list[Piece]:
    def source(file: Path) -> PurePosixPath:
        return PurePosixPath(file.relative_to(canonical.parent).as_posix())

    agents = [
        Piece("agents", agent.stem, source(agent), agent.read_bytes(), {})
        for agent in sorted(canonical.glob("agents/*.md"))
    ]
    skills = [
        Piece(
            "skills",
            skill.parent.name,
            source(skill),
            skill.read_bytes(),
            {
                PurePosixPath(beside.relative_to(skill.parent).as_posix()): beside.read_bytes()
                for beside in sorted(skill.parent.rglob("*"))
                if beside.is_file() and beside != skill
            },
        )
        for skill in sorted(canonical.glob("skills/*/SKILL.md"))
    ]
    commands = [
        Piece("commands", command.stem, source(command), command.read_bytes(), {})
        for command in sorted(canonical.glob("commands/*.md"))
    ]
    return [*agents, *skills, *commands]
