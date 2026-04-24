# Document Pack

A repo is ready for document-driven autonomy when it has five durable documents with distinct responsibilities.

## 1. AGENT.md

Purpose:
- operating rules
- implementation guardrails
- architecture boundaries that always apply

Should answer:
- how to behave in this repo
- what not to do
- what priorities outrank others

## 2. BLUEPRINT.md

Purpose:
- stable target architecture
- system responsibilities
- anti-patterns to avoid

Should answer:
- what the system is becoming
- what each major component owns
- what must not be allowed to drift

## 3. IMPLEMENTATION_PLAN.md

Purpose:
- current milestone execution plan
- ordered tasks
- acceptance criteria

Should answer:
- what to do next
- what files or modules are involved
- how to know each task is done

Best practice:
- keep this focused on the current milestone, not the whole roadmap
- make tasks small and sequential
- include explicit verification steps

## 4. EVALS.md

Purpose:
- quality gates
- scenarios
- metrics

Should answer:
- what tests or evals must pass
- what regressions are blocking
- what output quality bar matters

## 5. DECISIONS.md

Purpose:
- append-only record of meaningful architecture choices
- rationale for non-obvious constraints

Should answer:
- what was decided
- why it was decided
- what alternatives were rejected

## Readiness Check

A repo is ready when:
- these docs exist
- they do not obviously contradict each other
- the implementation plan has a clear next task
- eval expectations are concrete enough to run
- the decision log explains the major architectural constraints

If these conditions are not met, the repo is not ready for long autonomous execution yet.
