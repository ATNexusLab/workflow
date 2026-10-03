import argparse
import sys
from pathlib import Path

from builder import claude_code, plugin_directory
from builder.errors import BuildError


def build(root: Path) -> None:
    def counted(count: int, noun: str) -> str:
        return f"{count} {noun}" if count == 1 else f"{count} {noun}s"

    files = claude_code.package(root)
    plugin_directory.replace(root, "claude-code", files)

    skills = sum(path.name == "SKILL.md" for path in files)
    agents = sum(path.parts[0] == "agents" for path in files)
    print(f"Built plugins/claude-code: {counted(skills, 'skill')}, {counted(agents, 'agent')}.")


def check(root: Path) -> None:
    files = claude_code.package(root)
    failures = plugin_directory.differences(root, "claude-code", files)
    if failures:
        failures.append("Run python3 build.py and commit the result.")
    failures += claude_code.catalog_failures(root, files)

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
