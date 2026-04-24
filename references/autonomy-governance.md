# Autonomy Governance

Use this reference to keep long-running autonomous execution safe, resumable, and aligned.

## Stale Document Signals

Treat documents as stale when:
- they reference files or architecture that no longer exist
- the plan still shows old tasks as pending even though the code has moved on
- the decision log and blueprint disagree about the current architecture
- the docs cannot identify the active milestone or the next task

Stale docs should be repaired before more implementation continues.

## Checkpoint Rules

Create a checkpoint when:
- a task finishes
- a task becomes blocked
- task ordering changes
- an architecture decision is made
- the session is about to pause

A checkpoint should capture:
- task status
- verification run
- document updates made
- next task

## Blocker Categories

Use one of these labels when stopping work:
- `document blocker`
- `external dependency blocker`
- `approval blocker`
- `architecture blocker`
- `product decision blocker`

The blocker label should make it obvious why autonomy cannot continue.

## Minimum Repair Path

Use narrow repairs only:
- add or refresh the plan
- add or refresh eval criteria
- append a decision entry
- update milestone or task status

Do not use a repair step to redesign the project.
