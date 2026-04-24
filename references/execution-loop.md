# Execution Loop

Use this loop to continue implementation for long periods without drifting from the documented path.

## Startup

1. Find the files that satisfy the five document roles.
2. Read the operating rules.
3. Read the blueprint or architecture target.
4. Read the current implementation plan.
5. Read eval criteria.
6. Read the decision log.
7. Assess document health.
8. Identify the next unfinished task.

If no task is clearly next, stop and repair the plan before coding.

## Per-Task Loop

1. Restate the next task in one sentence.
2. Confirm that it still matches the blueprint.
3. Implement the smallest change that completes the task.
4. Run only the verification required for that task first.
5. If green, run broader regression checks as required by the repo.
6. Update the plan status immediately.
7. If the task introduced a durable architecture choice, append a decision entry.
8. Emit a short checkpoint if the task is complete or blocked.
9. Move to the next unfinished task.

## Task Selection Rules

Choose tasks in this order:
1. first unfinished task in the active milestone
2. first dependency-unblocking task
3. smallest task that materially advances the milestone

Avoid later tasks unless earlier ones are truly blocked.

## Verification Levels

- `task-level`: required for every task
- `milestone-level`: required when the plan or repo expects milestone stability
- `release-level`: required for external-behavior or deployment-sensitive work

Use the smallest sufficient verification first, but do not stop below the documented quality bar.

## Blocker Rules

Stop and surface a blocker when:
- required repository docs are missing or contradictory
- the next step requires human approval
- external credentials, services, or APIs are unavailable
- the work would require changing the blueprint rather than implementing it
- the plan does not expose a safe next task

Do not silently workaround these blockers by inventing scope or architecture.

## Definition Of Progress

Real progress means:
- the next documented task is complete
- verification actually ran
- plan status reflects reality
- any architecture change is recorded
- the next task is still clear after the checkpoint

Work that changes code without updating the plan is incomplete.
