---
name: document-driven-autonomy
description: Continue substantial engineering work autonomously after a repository has explicit governance and execution documents in place. Use when the repo has durable operating rules, a target architecture or blueprint, an active implementation plan, explicit eval or verification criteria, and a decision log, and the goal is to keep implementing on the recommended path for extended periods without human interruption.
---

# Document-Driven Autonomy

Continue implementation autonomously from durable repository documents instead of re-deriving direction from the latest chat turn.

## Use This Skill Only When The Repo Is Ready

Use this skill when the repository already has a durable planning package that defines the work.

Required document roles:
- operating rules
- target architecture or blueprint
- active implementation plan
- eval or verification criteria
- decision log

These roles do not need exact filenames. Accept equivalent names and locations.

Common examples:
- `AGENT.md`, `CLAUDE.md`, `COPILOT.md` for operating rules
- `BLUEPRINT.md`, `ARCHITECTURE.md`, `SYSTEM.md` for the target architecture
- `IMPLEMENTATION_PLAN.md`, `PLAN.md`, milestone docs under `planning/` for the active plan
- `EVALS.md`, `TESTING.md`, `QUALITY_GATES.md` for verification criteria
- `DECISIONS.md`, `ADRS.md`, `docs/adr/` for decisions

Do not use this skill when:
- the repo has no durable docs yet
- the architecture is still undecided
- the user is still brainstorming the product direction
- the next work item depends on human approval or missing external information

If the required document roles are missing, the repo is not ready for full document-driven autonomy yet.

## Operating Principle

Treat the repository documents as the source of truth.

Do not improvise major architecture changes from the latest request alone. Prefer continuing the documented path unless the docs are clearly stale, contradictory, or missing key execution detail.

When the docs conflict, resolve them in this order:
1. operating rules document
2. current implementation plan
3. blueprint or architecture target
4. eval criteria
5. decision log

If the conflict cannot be resolved safely, stop and ask for human clarification.

## Bootstrap Sequence

1. Find the files that satisfy the five required document roles.
2. Read the operating rules first.
3. Read the blueprint or architecture target.
4. Read the active implementation plan.
5. Read the eval criteria.
6. Read the decision log.
7. Assess document health before making changes.
8. Summarize the current mission, the active milestone, and the next unfinished task.
9. Execute only the next task on the documented path.

If there is no clear next task, repair the plan before implementing more code.

## Document Health Check

Before autonomous execution, check:
- are the required document roles present
- do the docs agree on the current architecture
- does the plan clearly identify the active milestone and next task
- are eval expectations concrete enough to run
- does the decision log explain major constraints still in force
- are any docs obviously stale relative to the current codebase

Treat a document as stale when:
- it references architecture or files that no longer exist
- it describes a plan whose early tasks are already complete but never updated
- it conflicts with the current decision log or codebase shape
- it cannot identify the current milestone or next action

If the docs are healthy, proceed.
If the docs are incomplete but repairable, repair them first.
If the docs are contradictory in a way that changes scope or architecture, stop and escalate to the human.

## Minimum Repair Path

When the repo is close to ready but not yet stable enough for autonomy:

1. Identify which document roles are missing or stale.
2. Create or refresh the minimum document needed to restore continuity.
3. Keep the repair narrow and factual.
4. Record the repair in the decision log if it changes the operating model.
5. Resume the normal execution loop.

Examples of acceptable repair:
- create an implementation plan from an approved blueprint
- update the active milestone and next task in the plan
- add a short eval checklist when the repo has tests but no documented gate
- append a decision entry clarifying an already-implemented architectural constraint

Do not use repair as an excuse to redesign the system.

## Active Task Selection Rules

To choose the next task:
1. prefer the first unfinished task in the current milestone
2. prefer tasks that unblock later work over side optimizations
3. prefer the smallest task that materially advances the plan
4. avoid jumping to a later task unless the earlier one is truly blocked

If the plan uses statuses, respect them.
Expected useful states include:
- `pending`
- `in_progress`
- `blocked`
- `done`
- `deferred`

Do not pick from `deferred` unless the plan explicitly changes.
Do not skip `blocked` tasks without recording why.

## Execution Loop

Repeat this loop until blocked:

1. Identify the next unfinished task from the implementation plan.
2. Confirm the task still aligns with the blueprint and decision log.
3. Make the smallest change that advances the task.
4. Run the required verification for that task.
5. Update the implementation plan status.
6. Record any meaningful architecture change in the decision log.
7. Continue to the next task.

Never claim success without running the documented verification.

## Checkpoint Cadence

At minimum, create a checkpoint when:
- a task is completed
- a blocker is encountered
- the architecture meaningfully changes
- the implementation plan changes status or ordering
- a long-running execution session needs a clean resume point

A useful checkpoint includes:
- task completed or blocked
- verification run
- plan status update
- any decision entry added
- next task

Keep checkpoints short. The goal is resumability and continuity.

## Eval Severity Model

Use three verification levels:

1. task-level
- the smallest tests or checks needed to prove the task is complete

2. milestone-level
- broader regression checks needed before declaring the milestone stable

3. release-level
- cross-cutting checks for anything that changes external behavior, deployment, or major interfaces

Default rule:
- always run task-level verification
- run milestone-level verification whenever the plan or repo expects it
- run release-level verification only when the work crosses that threshold

Do not overtest every tiny edit. Do not under-test changes that affect core behavior.

## Blocker Taxonomy

Stop and surface a blocker when the next step depends on:
- missing required document roles
- contradictory docs that change architecture or scope
- missing credentials, external services, or APIs
- required human approval
- unresolved product decisions
- unsafe assumptions about production behavior

Classify blockers clearly as one of:
- `document blocker`
- `external dependency blocker`
- `approval blocker`
- `architecture blocker`
- `product decision blocker`

Do not silently workaround blockers by inventing scope, architecture, or fake data.

## Guardrails

- Keep implementation aligned with the blueprint.
- Do not reintroduce rejected patterns recorded in the decision log.
- Do not bypass eval gates just because the local change looks small.
- Do not silently change scope; update the plan if the scope changes.
- Do not treat temporary scaffolding as the new architecture.
- Prefer explicit blockers over hidden assumptions.

## Documentation Maintenance Rules

When executing autonomously:
- update the implementation plan as tasks start and finish
- append short decision entries when architecture or workflow changes materially
- update eval criteria if the definition of done changes
- keep blueprint edits rare and deliberate

Do not rewrite the blueprint casually. The blueprint is the stable target, not a scratchpad.

## Recommended Repo Document Set

Use the guidance in [references/document-pack.md](references/document-pack.md) to assess whether the repo is ready.

Use the execution behavior in [references/execution-loop.md](references/execution-loop.md) to keep long-running work aligned and resumable.

Use the blocker and checkpoint guidance in [references/autonomy-governance.md](references/autonomy-governance.md) to keep autonomous sessions stable.

## Output Expectations

At the start of autonomous execution, briefly state:
- the active milestone
- the next task
- the verification you expect to run

At natural checkpoints, briefly state:
- what task was completed or blocked
- what verification passed or failed
- what doc was updated
- what the next task is

Keep updates short. The value of this skill is continuity and alignment, not verbose narration.
