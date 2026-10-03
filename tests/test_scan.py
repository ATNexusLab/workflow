import os
import subprocess
from pathlib import Path

import pytest

import scan

CANONICAL_AGENT = "canonical/agents/adversarial-verifier.md"
GENERATED_AGENT = "plugins/claude-code/agents/adversarial-verifier.md"


def write(repository: Path, path: str, content: str) -> None:
    target = repository / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content.encode())


def git(repository: Path, *arguments: str, committer: str = "Marina Albuquerque Tavares") -> None:
    emails = {"Marina Albuquerque Tavares": "mat@example.org", "GitHub": "noreply@github.com"}
    subprocess.run(
        ["git", "-C", str(repository), *arguments],
        check=True,
        capture_output=True,
        env={
            **os.environ,
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_AUTHOR_NAME": "Marina Albuquerque Tavares",
            "GIT_AUTHOR_EMAIL": "mat@example.org",
            "GIT_COMMITTER_NAME": committer,
            "GIT_COMMITTER_EMAIL": emails[committer],
        },
    )


@pytest.fixture
def repository(tmp_path: Path) -> Path:
    write(tmp_path, "adapters/neutrality-terms.txt", "(?i)claude\n/code-review\n")
    write(tmp_path, CANONICAL_AGENT, "Body.\n" * 10)
    write(tmp_path, GENERATED_AGENT, "Body.\n" * 3)
    write(
        tmp_path,
        "plugins/claude-code/.claude-plugin/plugin.json",
        '{"repository": "https://github.com/example/workflow"}\n',
    )
    write(tmp_path, ".env.example", "TOKEN=\n")
    git(tmp_path, "init")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "--message", "feat: add the content")
    write(tmp_path, "README.md", "Merged on GitHub.\n")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "--message", "docs: add the readme", committer="GitHub")
    return tmp_path


def test_clean_content_has_no_finding(repository: Path) -> None:
    assert scan.findings(repository) == []


def test_harness_name_in_canonical_content_is_a_finding(repository: Path) -> None:
    write(repository, CANONICAL_AGENT, "Body.\n" * 10 + "Runs in Claude Code.\n")

    assert scan.findings(repository) == [
        f'{CANONICAL_AGENT}:11: harness term "Claude" (NFR-FLEX-06)'
    ]


def test_home_directory_in_the_plugin_is_a_finding(repository: Path) -> None:
    write(repository, GENERATED_AGENT, "Body.\n" * 3 + "Notes live in `/Users/someone/notes`.\n")

    assert scan.findings(repository) == [
        f'{GENERATED_AGENT}:4: personal identity "/Users/someone" (NFR-SEC-01)'
    ]


def test_name_and_email_from_the_history_in_the_plugin_are_findings(repository: Path) -> None:
    write(repository, GENERATED_AGENT, "Written by albuquerque <mat@example.org>.\n")

    assert scan.findings(repository) == [
        f'{GENERATED_AGENT}:1: personal identity "mat@example.org" (NFR-SEC-01)',
        f'{GENERATED_AGENT}:1: personal identity "albuquerque" (NFR-SEC-01)',
    ]


def test_tracked_environment_file_and_vault_note_are_findings(repository: Path) -> None:
    write(repository, ".env.local", "TOKEN=fictitious\n")
    write(repository, "mem-0001-example.md", "A note.\n")
    git(repository, "add", ".")

    assert scan.findings(repository) == [
        ".env.local: environment file with values is tracked (NFR-SEC-02)",
        "mem-0001-example.md: vault note is tracked (NFR-SEC-02)",
    ]
