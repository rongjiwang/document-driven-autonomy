# Forward Tests

Forward tests are manual or agent-assisted checks that show the skill works on realistic repository shapes.

These are not unit tests for the validator. They are publication-readiness evidence for the skill behavior described in `references/forward-testing.md`.

## Required Scenarios

Before claiming a community-ready release, collect passing evidence for:

| Scenario | Required evidence | Status |
| --- | --- | --- |
| Product repo | Finds the five document roles, selects the next planned task, executes it, verifies it, and checkpoints cleanly. | Pending |
| Infra or tooling repo | Maps equivalent document names and locations without relying on exact filenames. | Pending |
| Incomplete repo | Refuses full autonomy or performs only a narrow repair, with a clear blocker label. | Pending |

## Result Format

Create one Markdown file per run:

```text
tests/forward/results/YYYY-MM-DD-<scenario>.md
```

Each result should include:

- repo shape and anonymized file map
- prompt used
- expected behavior
- observed behavior
- verification run
- pass/fail status
- follow-up changes, if any

Do not include private source code, credentials, customer names, or proprietary logs.
