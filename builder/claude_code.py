import json
from pathlib import Path, PurePosixPath

from builder.errors import BuildError
from builder.frontmatter import MissingFrontmatterError, add_lines
from builder.pieces import read_pieces

MANIFEST = PurePosixPath(".claude-plugin/plugin.json")


def package(root: Path) -> dict[PurePosixPath, bytes]:
    adapter = root / "adapters" / "claude-code"
    files = {MANIFEST: (adapter / "plugin.json").read_bytes()}
    packaged: dict[str, PurePosixPath] = {}
    errors: list[str] = []

    for piece in read_pieces(root / "canonical"):
        if piece.kind == "agents":
            piece_file = PurePosixPath("agents", f"{piece.name}.md")
        else:
            piece_file = PurePosixPath("skills", piece.name, "SKILL.md")
        if piece_file in files:
            errors.append(
                f'canonical/commands/{piece.name}.md: a skill is already named "{piece.name}"'
            )
        packaged[f"{piece.kind}/{piece.name}"] = piece_file
        files[piece_file] = piece.text
        for inside_skill, content in piece.supporting.items():
            files[piece_file.parent / inside_skill] = content

    additions: dict[str, list[str]] = json.loads((adapter / "frontmatter.json").read_bytes())
    for key, lines in additions.items():
        if key not in packaged:
            errors.append(
                f'adapters/claude-code/frontmatter.json: "{key}" names no canonical piece'
            )
            continue
        try:
            files[packaged[key]] = add_lines(files[packaged[key]], lines)
        except MissingFrontmatterError:
            errors.append(f'adapters/claude-code/frontmatter.json: "{key}" has no frontmatter')

    if errors:
        raise BuildError("\n".join(errors))
    return files


def catalog_failures(root: Path, files: dict[PurePosixPath, bytes]) -> list[str]:
    catalog = json.loads((root / ".claude-plugin" / "marketplace.json").read_bytes())
    entry_name = catalog["plugins"][0]["name"]
    plugin_name = json.loads(files[MANIFEST])["name"]
    if entry_name == plugin_name:
        return []
    return [
        f'.claude-plugin/marketplace.json: plugin entry "{entry_name}" does not match '
        f'"{plugin_name}" in adapters/claude-code/plugin.json'
    ]
