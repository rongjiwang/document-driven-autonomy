# Execution Loop

Use this loop to continue implementation for long periods without drifting from the documented path.

## Startup

1. Read `AGENT.md`.
2. Read the blueprint.
3. Read the current implementation plan.
4. Read eval criteria.
5. Read the decision log.
6. Identify the next unfinished task.

If no task is clearly next, stop and repair the plan before coding.

## Per-Task Loop

1. Restate the next task in one sentence.
2. Confirm that it still matches the blueprint.
3. Implement the smallest change that completes the task.
4. Run only the verification required for that task first.
5. If green, run broader regression checks as required by the repo.
6. Update the plan status immediately.
7. If the task introduced a durable architecture choice, append a decision entry.
8. Move to the next unfinished task.

## Blocker Rules

Stop and surface a blocker when:
- required repository docs are missing or contradictory
- the next step requires human approval
- external credentials, services, or APIs are unavailable
- the work would require changing the blueprint rather than implementing it

Do not silently workaround these blockers by inventing scope or architecture.

## Definition Of Progress

Real progress means:
- the next documented task is complete
- verification actually ran
- plan status reflects reality
- any architecture change is recorded

Work that changes code without updating the plan is incomplete.
