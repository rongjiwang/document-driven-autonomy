# Release Policy

This repository uses lightweight semantic versioning for the skill as a reusable artifact.

## Versioning Rules

### Patch release

Use a patch release for:
- wording improvements
- example updates
- metadata cleanup
- non-breaking clarification of existing behavior

Examples:
- `v0.2.1`
- `v1.0.1`

### Minor release

Use a minor release for:
- new references
- stronger execution guidance
- broader repo compatibility
- forward-testing improvements
- non-breaking trigger refinement

Examples:
- `v0.3.0`
- `v1.1.0`

### Major release

Use a major release for:
- breaking trigger behavior changes
- changed assumptions about required document roles
- a materially different execution model
- compatibility-breaking invocation or governance changes

Examples:
- `v1.0.0`
- `v2.0.0`

## Release Checklist

Before tagging a release:

1. Ensure the skill validator passes.
2. Review `SKILL.md` for trigger and behavior changes.
3. Review references for consistency with `SKILL.md`.
4. Confirm the repo is clean.
5. Commit the release changes.
6. Create an annotated git tag.
7. Push the branch and tags.

## Forward-Testing Expectation

For minor or major releases, prefer forward-testing on multiple repo shapes before tagging.

Recommended minimum:
- one product repo
- one tooling or infra repo
- one incomplete-repo scenario

## Recommended Commands

Replace the version as needed.

```bash
git status --short
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
git add .
git commit -m "Prepare v0.2.0 release"
git tag -a v0.2.0 -m "Release v0.2.0"
git push
git push origin v0.2.0
```

## Current Recommendation

Treat the current skill as pre-1.0 software until it has broader forward-testing coverage across multiple real repositories.
