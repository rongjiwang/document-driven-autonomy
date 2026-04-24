# Examples

Use these examples to understand when the skill should trigger and how it should behave.

## Good Trigger Examples

### Example 1: Continue implementation from a documented milestone

User request:
`Proceed autonomously on the documented path until blocked.`

Repo state:
- has operating rules
- has blueprint
- has implementation plan with task status
- has eval criteria
- has decision log

Expected behavior:
- locate the docs that satisfy the required roles
- summarize the active milestone and next task
- execute the next unfinished task only
- run the documented verification
- update the plan and decision log as needed

### Example 2: Resume after an interrupted long-running session

User request:
`Resume autonomous implementation from the repo docs.`

Repo state:
- checkpointed implementation plan
- recent decision log entries
- clear unfinished tasks

Expected behavior:
- rebuild context from docs rather than from chat history
- identify the last completed task and next unfinished task
- continue from the checkpoint

### Example 3: Repair a nearly ready repo

User request:
`Set this repo up so autonomous implementation can continue cleanly.`

Repo state:
- blueprint exists
- no active implementation plan yet
- tests exist but no eval doc

Expected behavior:
- identify missing document roles
- create the minimum missing plan or eval guidance
- avoid redesigning the product
- stop once the repo is ready for document-driven execution

## Non-Trigger Examples

### Example 4: Brainstorming a new product

User request:
`What should I build for this hackathon?`

Why this should not trigger:
- no stable repo governance package yet
- architecture still undecided
- the work is still in design, not document-driven execution

### Example 5: Tiny local fix

User request:
`Rename this variable and update the test.`

Why this should not trigger:
- no long-running autonomy requirement
- no need to coordinate through repo planning docs

### Example 6: Repo without durable docs

User request:
`Keep coding until it works.`

Why this should not trigger directly:
- missing operating rules, plan, eval criteria, or decision log
- skill should stop and state that the repo is not ready for document-driven autonomy yet

## Evaluation Questions

When reviewing the skill on a real repo, ask:
- did it find the correct doc roles without relying on exact filenames
- did it refuse to over-trigger on a small local task
- did it stop cleanly when docs were missing or contradictory
- did it continue from the implementation plan rather than from chat momentum
- did it keep updates short and checkpoint-oriented
