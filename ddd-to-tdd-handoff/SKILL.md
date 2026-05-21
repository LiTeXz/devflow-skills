---
name: ddd-to-tdd-handoff
description: "Convert confirmed DDD event-storming outputs into executable TDD implementation slices. Use after ddd-event-storming-design has produced confirmed commands, events, aggregates, policies, invariants, read models, or relationships and Codex needs tests, implementation planning, or development sequencing."
---

# DDD To TDD Handoff

Use this skill to bridge domain design into test-first development. It does not replace DDD modeling or TDD execution.

## Inputs

Read the confirmed DDD artifacts available in chat or in `event-storming/`:

- problem boundary and glossary
- domain events
- commands and actors
- policies and process managers
- aggregates, state, rules, and invariants
- read models and projection events
- relationships and external systems
- unresolved assumptions

If the DDD design is not confirmed, do not create implementation slices. Return to `ddd-event-storming-design` for confirmation.

## Mapping Rules

- Domain event -> expected observable behavior test.
- Command -> application service, use case, or aggregate command-handler test.
- Aggregate invariant -> domain unit test.
- Policy -> event-to-command orchestration test.
- Process manager -> stateful workflow test with waiting, resumption, and idempotency cases.
- Read model -> projection or query test.
- External system -> contract, adapter, or integration seam test.
- Relationship dependency -> precondition, prior fact, or state setup in tests.
- Failure event with business meaning -> explicit behavior slice; technical failure -> adapter or infrastructure slice.

Choose the narrowest test layer that protects the risk. Widen only when the behavior cannot be observed at a narrower boundary.

## Handoff Workflow

1. List the DDD inputs being used.
2. Identify implementation boundaries without inventing framework structure.
3. Create small TDD slices in business order.
4. For each slice, name:
   - behavior
   - source DDD artifact
   - test layer
   - first RED expectation
   - minimal GREEN implementation boundary
   - protected invariant or read model outcome
   - dependencies and unresolved facts
5. Mark slices that need `spring-web-boundaries`, persistence integration, contracts, or external-system seams.
6. Pass the slices to `implementation-planning` or `tdd-refactor`.

## Output Format

```markdown
# DDD to TDD Handoff

## 使用的 DDD 结论

## 实现边界

## TDD 切片

### Slice 1: <behavior>
- DDD 来源：
- 测试层：
- 预期 RED：
- 最小 GREEN：
- 保护的规则/读模型：
- 不应改变：
- 依赖/未决事实：

## 建议执行顺序

## 需要额外 skill
```

## Non-Negotiable Rules

- Do not write production code.
- Do not create tests directly unless the user explicitly asks to start implementation.
- Do not turn HTTP endpoints, database tables, DTOs, or pages into domain commands.
- Do not hide aggregate invariants inside policies or application services.
- Do not invent a read model that cannot be projected from events without calling out the gap.
- Do not proceed when a slice depends on an unconfirmed business conclusion that could change the model.

See `references/mapping-examples.md` for compact examples.
