# Document Pack

A repo is ready for document-driven autonomy when it has five durable document roles with distinct responsibilities.

Use document roles, not exact filenames.

## 1. Operating Rules

Purpose:
- operating rules
- implementation guardrails
- architecture boundaries that always apply

Common names:
- `AGENT.md`
- `CLAUDE.md`
- `COPILOT.md`

Should answer:
- how to behave in this repo
- what not to do
- what priorities outrank others

## 2. Target Architecture

Purpose:
- stable target architecture
- system responsibilities
- anti-patterns to avoid

Common names:
- `BLUEPRINT.md`
- `ARCHITECTURE.md`
- `SYSTEM.md`

Should answer:
- what the system is becoming
- what each major component owns
- what must not be allowed to drift

## 3. Active Implementation Plan

Purpose:
- current milestone execution plan
- ordered tasks
- acceptance criteria

Common names:
- `IMPLEMENTATION_PLAN.md`
- `PLAN.md`
- milestone docs under `planning/`

Should answer:
- what to do next
- what files or modules are involved
- how to know each task is done

Best practice:
- keep this focused on the current milestone, not the whole roadmap
- make tasks small and sequential
- include explicit verification steps
- expose task status clearly

## 4. Eval Criteria

Purpose:
- quality gates
- scenarios
- metrics

Common names:
- `EVALS.md`
- `TESTING.md`
- `QUALITY_GATES.md`

Should answer:
- what tests or evals must pass
- what regressions are blocking
- what output quality bar matters

## 5. Decision Log

Purpose:
- append-only record of meaningful architecture choices
- rationale for non-obvious constraints

Common names:
- `DECISIONS.md`
- `ADRS.md`
- ADR directories under `docs/adr/` or `adr/`

Should answer:
- what was decided
- why it was decided
- what alternatives were rejected

## Readiness Check

A repo is ready when:
- these document roles exist
- they do not obviously contradict each other
- the implementation plan has a clear next task
- eval expectations are concrete enough to run
- the decision log explains the major architectural constraints

If these conditions are not met, the repo is not ready for long autonomous execution yet.

## Minimum Repair Standard

A repo can still become autonomy-ready if the missing pieces are repairable.

Acceptable minimum repair:
- add the missing active implementation plan
- refresh the next-task status in the plan
- add a lightweight eval gate document
- append a decision entry that clarifies a binding architectural constraint

Do not attempt broad redesign under the banner of repair.
