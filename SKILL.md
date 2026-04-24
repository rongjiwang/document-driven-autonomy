---
name: document-driven-autonomy
description: Continue substantial engineering work autonomously after a repository has explicit governance and execution documents in place. Use when the repo already defines an AGENT.md, architecture or blueprint doc, implementation plan, eval criteria, and decision log, and the goal is to keep implementing on the recommended path for extended periods without human interruption.
---

# Document-Driven Autonomy

Continue implementation autonomously from repo-governance documents instead of re-deriving direction from the latest chat turn.

## Use This Skill Only When The Repo Is Ready

Use this skill when the repository already has a durable planning package that defines the work:
- `AGENT.md` or equivalent repo operating rules
- `BLUEPRINT.md`, architecture doc, or equivalent target-state doc
- `IMPLEMENTATION_PLAN.md` or equivalent active milestone/task plan
- `EVALS.md` or explicit verification criteria
- `DECISIONS.md` or ADR-style decision log

Do not use this skill when:
- the repo has no durable docs yet
- the architecture is still undecided
- the user is still brainstorming the product direction
- the next work item depends on human approval or missing external information

If the required docs are missing, stop and say that the repo is not ready for document-driven autonomy yet.

## Operating Principle

Treat the repository documents as the source of truth.

Do not improvise major architecture changes from the latest request alone. Prefer continuing the documented path unless the documents are clearly stale or contradictory.

When the docs conflict, resolve them in this order:
1. `AGENT.md`
2. current milestone plan
3. blueprint or architecture doc
4. eval criteria
5. decision log

If the conflict cannot be resolved safely, stop and ask for human clarification.

## Bootstrap Sequence

1. Read `AGENT.md` first.
2. Read the blueprint or architecture target doc.
3. Read the current implementation plan.
4. Read the eval criteria.
5. Read the decision log.
6. Summarize the current mission, the active milestone, and the next unfinished task.
7. Execute only the next task on the documented path.

If there is no clear next task, update the plan before implementing more code.

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

## Output Expectations

At the start of autonomous execution, briefly state:
- the active milestone
- the next task
- the verification you expect to run

At natural checkpoints, briefly state:
- what task was completed
- what verification passed
- what doc was updated
- what the next task is

Keep updates short. The value of this skill is continuity and alignment, not verbose narration.
