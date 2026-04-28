# Contributing

Thanks for helping improve Document-Driven Autonomy.

This repository contains a Codex skill. Changes should keep the installable skill small, explicit, and easy for an agent to follow.

## Development Loop

1. Make the smallest change that improves the skill.
2. Run the local validation:

   ```bash
   python3 scripts/validate_skill.py .
   python3 -m unittest discover -s tests
   ```

3. If the trigger behavior or execution model changes, update `SKILL.md`, related files under `references/`, and `agents/openai.yaml` together.
4. If a change affects publication readiness, update `references/forward-testing.md` or add a forward-test result under `tests/forward/`.

## Pull Request Checklist

- [ ] The skill validator passes.
- [ ] Unit tests pass.
- [ ] Local links in `SKILL.md` still resolve.
- [ ] Trigger behavior remains explicit and narrow.
- [ ] Any behavior change is reflected in the release policy or forward-test evidence.

## Style

- Keep `SKILL.md` focused on the workflow an agent must follow.
- Put longer guidance in `references/` and link to it from `SKILL.md`.
- Prefer concrete examples over broad claims.
- Avoid adding dependencies unless the validation or packaging benefit is clear.
