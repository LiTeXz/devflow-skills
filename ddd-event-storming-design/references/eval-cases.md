# DDD Skill Eval Cases

Use these cases to evaluate whether `ddd-event-storming-design` preserves event-storming discipline.

## Case 1: Table-First Input

Prompt: "Design order, order_item, product tables and aggregates for order submission."

Expected guardrail:

- Reject table-first modeling as the starting point.
- Reframe around business facts, commands, events, invariants, and read models.
- Derive aggregates only after event-command coherence.

## Case 2: Technical Event Pollution

Prompt: "When the API sends an MQ message and refreshes cache, model events for those."

Expected guardrail:

- Exclude MQ/cache facts unless the business cares about them.
- Keep them as integration or infrastructure concerns.

## Case 3: Policy Hides Invariant

Prompt: "Use a policy to prevent submitting an order when stock is insufficient."

Expected guardrail:

- Identify stock sufficiency as a command precondition or aggregate invariant when inside the consistency boundary.
- Use policy only for event-to-command reactions.

## Case 4: Missing Production Path

Prompt: "Event: 订单已取消. No command or actor is provided."

Expected guardrail:

- Require a producing command, policy, process manager, or external system fact.
- Mark the missing path in the conclusion confirmation list.

## Case 5: Unconfirmed Persistence

Prompt: "Create event-storming files for this new vague requirement immediately."

Expected guardrail:

- Produce a design draft and conclusion confirmation list first.
- Do not create or update `event-storming/` files before explicit confirmation.

## Case 6: Read Model Cannot Project

Prompt: "Order details page shows risk score, but no event carries risk data."

Expected guardrail:

- Identify the projection gap.
- Adjust events, command fields, or external-system relationship instead of polluting aggregate state.
