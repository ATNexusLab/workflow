# Content scan

`scan.py` and `scanner/` — Python, standard library only. Milestone: M1.

## Job

`python3 scan.py` is the Content scan gate. It prints one line per finding and exits 1, or exits 0 with
`Scan passed: 0 harness terms, 0 personal identities, 0 environment files, 0 vault notes.`

| It looks for | In | Requirement |
| --- | --- | --- |
| A match of a line of `adapters/neutrality-terms.txt` | Every file under `canonical/` | [NFR-FLEX-06](../../requirements/non-functional/flexibility.md#nfr-flex-06) |
| An email address, a home-directory path, and the names and emails of the repository's history | Every file under `plugins/` | [NFR-SEC-01](../../requirements/non-functional/security.md#nfr-sec-01) |
| An environment file with values, and a vault note, by file name | Every tracked file | [NFR-SEC-02](../../requirements/non-functional/security.md#nfr-sec-02) |

## What it never does

- It writes nothing.
- It does not look for credentials. That is the Secret scan gate, which runs detect-secrets over every
  tracked file.
- It keeps no list of people. The names and emails come from `git log` each time it runs.

## Inner blocks

| Module | Responsibility |
| --- | --- |
| `scan.py` | Orchestrates: asks each module for its findings and reports. It holds no scanning logic |
| `scanner/line_matches.py` | Reads every file of a directory and returns each match of each pattern, with its file and line |
| `scanner/harness_terms.py` | Matches the neutrality terms against `canonical/` |
| `scanner/personal_identity.py` | Builds the identity patterns, the history's names and emails included, and matches them against `plugins/` |
| `scanner/tracked_files.py` | Names the tracked files that are environment files with values or vault notes |

## To change it safely

- A harness-native name found in the content is added to `adapters/neutrality-terms.txt`, one Python
  regular expression per line, in the commit that removes it from the content.
- Every author and committer of the history counts, except `GitHub <noreply@github.com>`: GitHub writes
  it on a commit made on its site, and the plugin names GitHub.
- A module of `scanner/` never prints and never exits. Both belong to `scan.py`.
- A failure of `git` is not caught: the scan stops with git's own error.
- The tests in `tests/test_scan.py` run the scan on a small git repository built in a temporary
  directory.
