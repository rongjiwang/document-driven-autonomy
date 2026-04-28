# Document-Driven Autonomy

[![Validate](https://github.com/rongjiwang/document-driven-autonomy/actions/workflows/validate.yml/badge.svg)](https://github.com/rongjiwang/document-driven-autonomy/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Document-Driven Autonomy is a Codex skill for continuing substantial engineering work from durable repository documents instead of from the latest chat turn.

Use it when a repo already has:
- operating rules
- a target architecture or blueprint
- an active implementation plan
- eval or verification criteria
- a decision log

The skill teaches Codex to:
- assess whether a repo is ready for long autonomous execution
- continue from the next documented task
- keep execution aligned with the blueprint and decision log
- checkpoint progress and stop clearly when blocked

## Why This Exists

Long agent sessions drift when the only source of truth is chat history. This skill makes the repo's governance and planning documents the durable control plane for autonomous coding.

It is intentionally conservative. If the required documents are missing, stale, contradictory, or blocked on human approval, the skill should stop clearly instead of inventing scope.

## Quick Start

Install the skill from this repository, then restart Codex:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo rongjiwang/document-driven-autonomy \
  --path . \
  --name document-driven-autonomy
```

The explicit `--name document-driven-autonomy` is important because this repository stores the skill at the repository root.

Then invoke it explicitly:

```text
Use $document-driven-autonomy to assess whether this repo is ready for long autonomous execution from its governance and planning docs.
```

## Prompt Sequence

Use this sequence when applying the skill to a repo that is not already fully prepared for document-driven autonomy.

### 1. Inspect only

```text
Use $document-driven-autonomy to inspect this repo for autonomous execution readiness. Map any existing docs to these roles: operating rules, target architecture, active implementation plan, eval criteria, and decision log. Do not edit files. Report what is present, missing, stale, or contradictory.
```

### 2. Propose the minimum document pack

```text
Use $document-driven-autonomy to propose the minimum document pack needed to make this repo ready for future autonomous execution. Ground the proposal in the current codebase and existing docs. Do not edit files yet.
```

### 3. Create missing docs

```text
Use $document-driven-autonomy to create the approved minimal document pack for this repo: operating rules, target architecture, active implementation plan, eval criteria, and decision log. Keep the docs concise, factual, and aligned with the existing codebase. Do not start implementation work.
```

### 4. Validate readiness

```text
Use $document-driven-autonomy to assess whether the repo is now ready for autonomous execution. Confirm that the docs agree, the active milestone has a clear next task, eval criteria are runnable, and the decision log captures current constraints. Do not edit files unless a narrow doc repair is required.
```

### 5. Run one safe task

```text
Use $document-driven-autonomy to resume from the repo docs. Identify the active milestone, the next unfinished task, and the verification you expect to run. Complete only that task, run verification, update the plan/checkpoint docs, and stop with the next task clearly stated.
```

### 6. Continue until blocked

```text
Use $document-driven-autonomy to proceed autonomously from the repo docs until blocked or until the current milestone is complete. Follow the implementation plan order, keep changes aligned with the architecture and decision log, run task-level verification for every completed task, and create concise checkpoints as you go.
```

Best practice: run steps 1-5 the first time on a repo. Use step 6 only after the skill has completed one clean task successfully.

## Expected Behavior

At startup, the skill should:

1. Find the files that satisfy the five required document roles.
2. Read operating rules, architecture, implementation plan, eval criteria, and decisions.
3. Check whether those documents are healthy enough for autonomous work.
4. Identify the active milestone and next unfinished task.
5. Execute the next documented task, run verification, update docs, and checkpoint.

If the repo is not ready, it should label the blocker rather than continue on assumptions.

## Skill Layout

- [SKILL.md](./SKILL.md): trigger conditions and execution behavior
- [agents/openai.yaml](./agents/openai.yaml): UI-facing metadata
- [references/document-pack.md](./references/document-pack.md): required document roles
- [references/execution-loop.md](./references/execution-loop.md): per-task operating loop
- [references/autonomy-governance.md](./references/autonomy-governance.md): blockers, checkpoints, and repair rules
- [references/examples.md](./references/examples.md): trigger and non-trigger examples
- [references/forward-testing.md](./references/forward-testing.md): publication-readiness test guidance
- [tests/forward](./tests/forward): forward-test evidence and result templates
- [scripts/validate_skill.py](./scripts/validate_skill.py): repo-local validation used by CI

## Validation

```bash
python3 scripts/validate_skill.py .
python3 -m unittest discover -s tests
```

For local Codex development, you can also run the system validator:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Publication Status

The skill is structurally valid and should be treated as pre-1.0 software. Before claiming a community-ready 1.0 release, the project should collect forward-test evidence for:

- one product repo
- one infra or tooling repo
- one incomplete-repo scenario

See [tests/forward/README.md](./tests/forward/README.md).

## Versioning

This repository uses lightweight semantic versioning:

- patch: wording fixes, examples, metadata polish
- minor: stronger guidance, broader compatibility, new references
- major: breaking changes to trigger behavior or execution model

See [RELEASE_POLICY.md](./RELEASE_POLICY.md).

## Contributing

Issues and pull requests are welcome once the repository is public. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) and keep changes focused on the skill's execution behavior, trigger boundaries, validation, or forward-test evidence.

## License

MIT. See [LICENSE](./LICENSE).
