# Document-Driven Autonomy

A Codex skill for continuing substantial engineering work from durable repository documents instead of from the latest chat turn.

This skill is meant for repos that already have:
- operating rules
- a target architecture or blueprint
- an active implementation plan
- eval or verification criteria
- a decision log

The skill helps Codex:
- assess whether a repo is ready for long autonomous execution
- continue from the next documented task
- keep execution aligned with the blueprint and decision log
- checkpoint progress and stop clearly when blocked

## Skill Layout

- [SKILL.md](./SKILL.md): trigger conditions and execution behavior
- [agents/openai.yaml](./agents/openai.yaml): UI-facing metadata
- [references/document-pack.md](./references/document-pack.md): required document roles
- [references/execution-loop.md](./references/execution-loop.md): per-task operating loop
- [references/autonomy-governance.md](./references/autonomy-governance.md): blockers, checkpoints, and repair rules
- [references/examples.md](./references/examples.md): trigger and non-trigger examples
- [references/forward-testing.md](./references/forward-testing.md): publication-readiness test guidance

## Installation

If you have access to the repository, install it with the Codex skill installer and then restart Codex.

Example shape:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo rongjiwang/document-driven-autonomy \
  --path .
```

After installation, restart Codex so the skill is discovered.

## Usage

Example prompt:

```text
Use $document-driven-autonomy to continue implementation from the repo governance and planning docs.
```

This skill is intentionally configured for explicit invocation.

## When Not To Use It

Do not use this skill when:
- the repo is still in brainstorming mode
- the architecture is not settled
- the repo has no durable planning documents yet
- the task is a tiny local edit that does not need long-running autonomous execution

## Versioning

This repository uses lightweight semantic versioning:

- patch: wording fixes, examples, metadata polish
- minor: stronger guidance, broader compatibility, new references
- major: breaking changes to trigger behavior or execution model

See [RELEASE_POLICY.md](./RELEASE_POLICY.md).
