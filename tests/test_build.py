import json
from pathlib import Path

import pytest

import build
from builder.errors import BuildError

GENERATED_AGENT = "plugins/claude-code/agents/adversarial-verifier.md"


@pytest.fixture
def repository(tmp_path: Path) -> Path:
    files = {
        "canonical/agents/adversarial-verifier.md": (
            "---\nname: adversarial-verifier\ndescription: Disproves one claim.\n---\n\nBody.\n"
        ),
        "canonical/skills/grilling/SKILL.md": (
            "---\nname: grilling\ndescription: States assumptions.\n---\n\n"
            "Published by `{{command:spec}}`.\n"
        ),
        "canonical/skills/grilling/notes.md": "Kept beside `{{skill:grilling}}`.\n",
        "canonical/commands/spec.md": (
            "---\ndescription: Writes a spec.\n---\n\n"
            "Run a `{{skill:grilling}}` session, then dispatch {{harness:general-agent}}.\n"
        ),
        "adapters/claude-code/plugin.json": json.dumps({"name": "tightship"}),
        "adapters/claude-code/terms/general-agent.md": "`general-purpose`\n",
        "adapters/claude-code/frontmatter.json": json.dumps(
            {"agents/adversarial-verifier": ["tools: Read, Grep, Glob, Bash"]}
        ),
        ".claude-plugin/marketplace.json": json.dumps({"plugins": [{"name": "tightship"}]}),
    }
    for path, content in files.items():
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content.encode())
    return tmp_path


def test_build_packages_the_agent_with_its_adapter_frontmatter(
    repository: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    build.build(repository)
    build.check(repository)

    assert capsys.readouterr().out == (
        "Built plugins/claude-code: 2 skills, 1 agent.\nplugins/claude-code is up to date.\n"
    )
    skills = repository / "plugins/claude-code/skills"
    assert (skills / "grilling/SKILL.md").read_bytes() == (
        b"---\nname: grilling\ndescription: States assumptions.\n---\n\n"
        b"Published by `/tightship:spec`.\n"
    )
    assert (skills / "grilling/notes.md").read_bytes() == b"Kept beside `tightship:grilling`.\n"
    assert (skills / "spec/SKILL.md").read_bytes() == (
        b"---\ndescription: Writes a spec.\n---\n\n"
        b"Run a `tightship:grilling` session, then dispatch `general-purpose`.\n"
    )
    assert (repository / GENERATED_AGENT).read_bytes() == (
        b"---\nname: adversarial-verifier\ndescription: Disproves one claim.\n"
        b"tools: Read, Grep, Glob, Bash\n---\n\nBody.\n"
    )
    assert (repository / "plugins/claude-code/.claude-plugin/plugin.json").read_bytes() == (
        repository / "adapters/claude-code/plugin.json"
    ).read_bytes()


def test_unknown_piece_in_the_adapter_stops_the_build(repository: Path) -> None:
    build.build(repository)
    built = (repository / GENERATED_AGENT).read_bytes()
    (repository / "canonical/agents/adversarial-verifier.md").write_bytes(b"---\n---\nChanged.\n")
    (repository / "adapters/claude-code/frontmatter.json").write_bytes(
        json.dumps({"agents/adversarial-verifer": ["tools: Read"]}).encode()
    )

    with pytest.raises(BuildError) as failure:
        build.build(repository)

    assert str(failure.value) == (
        'adapters/claude-code/frontmatter.json: "agents/adversarial-verifer" '
        "names no canonical piece"
    )
    assert (repository / GENERATED_AGENT).read_bytes() == built


def test_unresolved_reference_stops_the_build(repository: Path) -> None:
    build.build(repository)
    built = (repository / "plugins/claude-code/skills/spec/SKILL.md").read_bytes()
    (repository / "canonical/commands/spec.md").write_bytes(
        b"---\ndescription: Writes a spec.\n---\n\n\n\n\nPublished by `{{command:epik}}`.\n"
    )

    with pytest.raises(BuildError) as failure:
        build.build(repository)

    assert str(failure.value) == (
        "canonical/commands/spec.md:8: {{command:epik}} resolves to nothing"
    )
    assert (repository / "plugins/claude-code/skills/spec/SKILL.md").read_bytes() == built


def test_stale_plugin_fails_the_check(repository: Path) -> None:
    build.build(repository)
    (repository / "canonical/agents/adversarial-verifier.md").write_bytes(
        b"---\nname: adversarial-verifier\n---\nChanged.\n"
    )

    with pytest.raises(BuildError) as failure:
        build.check(repository)

    assert str(failure.value) == (
        f"{GENERATED_AGENT}: differs from a fresh build\n"
        "Run python3 build.py and commit the result."
    )


def test_catalog_entry_with_another_name_fails_the_check(repository: Path) -> None:
    build.build(repository)
    (repository / ".claude-plugin/marketplace.json").write_bytes(
        json.dumps({"plugins": [{"name": "tight-ship"}]}).encode()
    )

    with pytest.raises(BuildError) as failure:
        build.check(repository)

    assert str(failure.value) == (
        '.claude-plugin/marketplace.json: plugin entry "tight-ship" does not match '
        '"tightship" in adapters/claude-code/plugin.json'
    )


def test_piece_without_frontmatter_stops_the_build(repository: Path) -> None:
    (repository / "canonical/agents/adversarial-verifier.md").write_bytes(
        b"Body.\n\n---\n\nMore.\n"
    )

    with pytest.raises(BuildError) as failure:
        build.build(repository)

    assert str(failure.value) == (
        'adapters/claude-code/frontmatter.json: "agents/adversarial-verifier" has no frontmatter'
    )
    assert not (repository / "plugins").exists()
