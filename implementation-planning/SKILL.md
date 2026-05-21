---
name: implementation-planning
description: "Write a concrete, small-step implementation plan before coding. Use for multi-step features, bug fixes, refactors, DDD-to-TDD handoffs, risky behavior changes, or any engineering task that needs files, commands, expected RED/GREEN results, verification steps, and completion criteria before implementation."
---

# Implementation Planning

Use this skill to turn a requirement, confirmed DDD handoff, bug investigation result, or refactor goal into a plan that another agent can execute.

Do not edit production code while using this skill.

## Planning Workflow

1. Restate the goal and scope.
2. List constraints:
   - behaviors that must not change
   - public contracts
   - data, persistence, ordering, pagination, security, or side-effect risks
   - user-owned worktree changes to avoid
3. Identify behavior slices.
4. For each task, specify:
   - objective
   - files or modules likely involved
   - test or verification command
   - expected RED, GREEN, or unchanged result
   - completion standard
5. Keep each task small enough to complete and verify independently.
6. Mark steps that require `tdd-skill`, `spring-web-boundaries`, or `systematic-debugging`.
7. State whether user confirmation is required before execution.

## Step Size

Prefer 2-5 minute execution steps. Split a step when it combines:

- creating tests and implementing production code
- unrelated behavior slices
- multiple modules with separate risks
- refactor and behavior change
- debugging and fixing
- code changes and commit/PR work

## Output Format

Use `templates/implementation-plan.md` when a file artifact is useful. In chat, use the same structure:

```markdown
# <Name> Implementation Plan

## 目标

## 约束

## 行为切片

## 任务列表

1. 写失败测试：<behavior>
   - 文件：
   - 命令：
   - 预期 RED：
   - 完成标准：

2. 最小实现：<behavior>
   - 文件：
   - 命令：
   - 预期 GREEN：
   - 完成标准：

3. 重构：<design cleanup>
   - 文件：
   - 命令：
   - 必须保持：
   - 完成标准：

## 验证矩阵

## 需要用户确认
```

## Non-Negotiable Rules

- Do not write production code in this phase.
- Do not produce vague steps such as "implement feature" or "run tests".
- Do not omit commands when the project has discoverable test commands.
- Do not plan a fix before a reproducible failure and root-cause evidence exists for unclear bugs.
- Do not mix behavior change and broad cleanup in the same step.
- Do not assume approval for risky scope expansion; call it out.
