# Forward Testing

Use this guide to evaluate whether the skill is community-ready.

## Goal

Demonstrate that the skill:
- triggers in the right circumstances
- does not over-trigger on small or underspecified tasks
- handles different repo document layouts
- stops cleanly on missing-doc and contradiction scenarios

## Recommended Test Matrix

Test the skill on at least three repo shapes:

1. Product repo
- has operating rules, blueprint, plan, evals, decisions
- expected result: executes the next documented task

2. Infra or tooling repo
- uses different doc names or locations
- expected result: maps document roles correctly without exact filename dependence

3. Incomplete repo
- missing one or more required document roles
- expected result: refuses full autonomy and identifies the missing roles or performs a narrow repair if appropriate

## Example Test Prompts

- `Use $document-driven-autonomy to continue implementation from the repo docs.`
- `Use $document-driven-autonomy to resume the active milestone until blocked.`
- `Use $document-driven-autonomy to assess whether this repo is ready for long autonomous execution.`

## What To Observe

- whether the skill identifies the correct documents
- whether it chooses the right next task
- whether it emits short checkpoints
- whether it updates plan and decisions when appropriate
- whether it labels blockers clearly

## Failure Signals

The skill needs more work if it:
- hard-fails because filenames differ but document roles are present
- starts coding before determining the next planned task
- ignores contradictions between plan and blueprint
- over-triggers on trivial edits
- rewrites architecture under the guise of repair

## Publication Bar

Treat the skill as community-ready only after:
- structural validation passes
- at least three repo-shape forward tests pass
- at least one incomplete-repo scenario shows a clean stop or narrow repair
