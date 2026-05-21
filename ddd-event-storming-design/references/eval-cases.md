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

## Case 7: CRUD-Looking Admin Nouns

Prompt: "My backend admin system has company, department, position, and employee. Redesign this part."

Expected guardrail:

- Mark the request as a CRUD-template risk instead of directly creating one aggregate for each noun.
- Identify actors such as HR, tenant admin, department manager, employee, external OA system, and downstream account/permission domain when relevant.
- Produce actor-command-event-impact chains before aggregate design.
- Separate login account `User` from roster person `Employee` as a boundary candidate when both meanings may exist.
- Treat employment/assignment/position holding as a candidate behavior concept instead of assuming employee has only one current position.
- Put uncertain rules in conclusion items with affected events, commands, aggregates, read models, or relationships.

## Case 8: Vague Data Change Events

Prompt: "The event list includes 公司信息已变更, 部门信息已变更, 岗位信息已变更, 员工个人信息已变更."

Expected guardrail:

- Reject or split vague `信息已变更` events when specific business facts drive rules or projections.
- Ask which changes are business-significant, such as name, parent department, responsible person, status, or contact channel.
- Keep a generic change event only with an explicit justification.

## Case 9: External Master Data Sync

Prompt: "OA synchronizes companies, departments, positions, and employees."

Expected guardrail:

- Model OA as an external system actor when it is outside the current domain.
- Distinguish received external facts, accepted/applied local facts, dependency-waiting states, conflicts, and failures when the business cares.
- Do not model sync as simple upsert if parent-child ordering, missing dependencies, retries, or conflict resolution matter.

## Case 10: Brainstormed Events Become Final Too Early

Prompt: "Let's brainstorm all events for a recruitment workflow. Candidates include 简历已上传, 面试提醒已发送, 候选人资料已更新, Offer已审批, 邮件已投递成功, 入职已确认. Turn them into the DDD model."

Expected guardrail:

- Treat the list as a candidate event pool, not the final event list.
- Screen candidates by business meaning, production path, affected subject, policy/read-model impact, and current-domain boundary.
- Reject or downgrade technical facts such as email delivery unless the business explicitly cares.
- Split or rename vague data-change events such as `候选人资料已更新` when specific business facts matter.
- Compare plausible modeling approaches when approval, offer, and onboarding boundaries could be aggregate, process manager, or external-system responsibilities.
- Move only accepted candidates into `领域事件清单` and put unresolved screening decisions into the conclusion confirmation list.

## Case 11: Duplicated Final Confirmation

Prompt: "During the conversation I confirmed the boundary, actors, candidate event screening, and aggregate choice section by section. Now persist the model."

Expected guardrail:

- Do not ask the user to reconfirm sections already confirmed during the conversation.
- Treat `结论确认清单` as a delta list for unconfirmed, newly changed, or still ambiguous conclusions.
- If all persistence-relevant conclusions were confirmed, state that no additional confirmation items remain before writing files.
- If later edits changed a previously confirmed conclusion, list only that changed conclusion and explain the affected events, commands, aggregates, policies, read models, or relationships.

## Case 12: Full Draft Skips Confirmation Gates

Prompt: "We have company, department, position, employee, OA sync, and account linkage. Redesign with DDD."

Expected guardrail:

- Mark the request as CRUD-looking and boundary-sensitive.
- Do not output a full boundary + actors + events + commands + policies + aggregates + read models draft before confirming upstream gates.
- First present the problem-domain gate and ask one focused confirmation question, such as whether this is `组织任职域`, whether OA sync and account linkage are included, and which responsibilities are excluded.
- After the problem-domain gate is confirmed, confirm the actor and authority gate before accepted events and policies, especially whether OA is authoritative.
- Confirm key rules such as single/multiple positions, manager eligibility, deletion/archive semantics, and conflict precedence before finalizing events, commands, invariants, and policies.
- Confirm the modeling alternative gate before finalizing aggregate boundaries and read models.

## Case 13: User Speaks Data Model

Prompt: "We have company, department, position, employee tables with create/update/delete pages. Convert them to DDD aggregates and events."

Expected guardrail:

- Treat tables, fields, CRUD pages, and entity names as raw discovery input, not as the modeling frame.
- Briefly state that the model must be translated into business events, actor goals, lifecycle decisions, rules, and read-model needs.
- Do not produce events such as `CompanyCreatedEvent`, `DeptUpdatedEvent`, `PositionDeletedEvent`, or `EmployeeEditedEvent`.
- Do not create one aggregate per table unless each noun is proven to be a lifecycle and consistency boundary.
- Start with the problem-domain gate and ask a focused business question before deriving events, commands, or aggregates.
- Translate fields and foreign keys into possible invariants, ownership/dependency questions, or projection needs rather than aggregate fields.

## Case 14: Key Decision Confirmation UX

Prompt: "We need to decide whether OA is authoritative, whether employees can hold multiple positions, and whether employee deletion means archive or hard delete."

Expected guardrail:

- Treat each item as a high-impact business decision that shapes downstream events, commands, policies, and aggregates.
- If `request_user_input` is available, use it for the current gate with 2-3 mutually exclusive options and put the recommended option first.
- If `request_user_input` is unavailable, do not finalize downstream design. State that user confirmation is required before continuing and ask one focused confirmation question in normal text.
- Do not ask all high-impact decisions at once in the final answer.
- Confirm decisions sequentially at the relevant gates: authority first, then assignment cardinality, then deletion/archive semantics.
