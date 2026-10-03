import argparse
import json
import shutil
import sys
from pathlib import Path, PurePosixPath


class BuildError(Exception):
    pass


def package_claude_code(root: Path) -> dict[PurePosixPath, bytes]:
    canonical = root / "canonical"
    adapter = root / "adapters" / "claude-code"
    files = {PurePosixPath(".claude-plugin/plugin.json"): (adapter / "plugin.json").read_bytes()}
    pieces: dict[str, PurePosixPath] = {}
    errors: list[str] = []

    for agent in sorted(canonical.glob("agents/*.md")):
        pieces[f"agents/{agent.stem}"] = PurePosixPath("agents", agent.name)
        files[pieces[f"agents/{agent.stem}"]] = agent.read_bytes()

    for skill in sorted(canonical.glob("skills/*/SKILL.md")):
        name = skill.parent.name
        pieces[f"skills/{name}"] = PurePosixPath("skills", name, "SKILL.md")
        for supporting in sorted(skill.parent.rglob("*")):
            if supporting.is_file():
                inside_skill = supporting.relative_to(skill.parent).as_posix()
                files[PurePosixPath("skills", name, inside_skill)] = supporting.read_bytes()

    for command in sorted(canonical.glob("commands/*.md")):
        packaged = PurePosixPath("skills", command.stem, "SKILL.md")
        if packaged in files:
            errors.append(
                f'canonical/commands/{command.name}: a skill is already named "{command.stem}"'
            )
        pieces[f"commands/{command.stem}"] = packaged
        files[packaged] = command.read_bytes()

    additions: dict[str, list[str]] = json.loads((adapter / "frontmatter.json").read_bytes())
    for key, lines in additions.items():
        if key not in pieces:
            errors.append(
                f'adapters/claude-code/frontmatter.json: "{key}" names no canonical piece'
            )
            continue
        opening, closing, body = files[pieces[key]].partition(b"\n---\n")
        if not (opening.startswith(b"---\n") and closing):
            errors.append(f'adapters/claude-code/frontmatter.json: "{key}" has no frontmatter')
            continue
        files[pieces[key]] = opening + b"\n" + "\n".join(lines).encode() + closing + body

    if errors:
        raise BuildError("\n".join(errors))
    return files


def build(root: Path) -> None:
    def counted(count: int, noun: str) -> str:
        return f"{count} {noun}" if count == 1 else f"{count} {noun}s"

    files = package_claude_code(root)
    plugin = root / "plugins" / "claude-code"
    if plugin.exists():
        shutil.rmtree(plugin)
    for path, content in files.items():
        target = plugin / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)

    skills = sum(path.name == "SKILL.md" for path in files)
    agents = sum(path.parts[0] == "agents" for path in files)
    print(f"Built plugins/claude-code: {counted(skills, 'skill')}, {counted(agents, 'agent')}.")


def check(root: Path) -> None:
    fresh = package_claude_code(root)
    plugin = root / "plugins" / "claude-code"
    committed = {
        PurePosixPath(path.relative_to(plugin).as_posix())
        for path in plugin.rglob("*")
        if path.is_file()
    }

    failures = []
    for path in sorted(fresh.keys() | committed):
        if path not in committed:
            failures.append(f"plugins/claude-code/{path}: is missing")
        elif path not in fresh:
            failures.append(f"plugins/claude-code/{path}: is not produced by the build")
        elif (plugin / path).read_bytes() != fresh[path]:
            failures.append(f"plugins/claude-code/{path}: differs from a fresh build")
    if failures:
        failures.append("Run python3 build.py and commit the result.")

    catalog = json.loads((root / ".claude-plugin" / "marketplace.json").read_bytes())
    entry_name = catalog["plugins"][0]["name"]
    plugin_name = json.loads(fresh[PurePosixPath(".claude-plugin/plugin.json")])["name"]
    if entry_name != plugin_name:
        failures.append(
            f'.claude-plugin/marketplace.json: plugin entry "{entry_name}" does not match '
            f'"{plugin_name}" in adapters/claude-code/plugin.json'
        )

    if failures:
        raise BuildError("\n".join(failures))
    print("plugins/claude-code is up to date.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build plugins/ from canonical/ and adapters/.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when the committed plugin differs from a fresh build",
    )
    repository = Path(__file__).resolve().parent
    try:
        if parser.parse_args().check:
            check(repository)
        else:
            build(repository)
    except BuildError as error:
        sys.exit(str(error))
