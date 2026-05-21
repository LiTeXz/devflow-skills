# DevFlow Skills

[简体中文](README.md) | English

DevFlow Skills is a set of Codex engineering workflow skills. It organizes DDD, TDD, planning, execution, debugging, review, verification, and branch finishing into a composable workflow system.

## Installation

Install all skills from the repository root:

```bash
npx skills add https://github.com/one-eyed-fish/devflow-skills.git -g -a codex --skill engineering-workflow-router ddd-event-storming-design ddd-to-tdd-handoff implementation-planning executing-implementation-plan systematic-debugging verification-before-completion requesting-code-review receiving-code-review finishing-development-branch parallel-agent-orchestration tdd-skill spring-web-boundaries
```

Install a single skill:

```bash
npx skills add https://github.com/one-eyed-fish/devflow-skills/tree/main/engineering-workflow-router -g -a codex
```

Restart Codex after installation so the new skills are loaded.

## Skills

- `engineering-workflow-router`: entry router for development, refactor, bug fix, modeling, review, verification, and branch finishing.
- `ddd-event-storming-design`: pure DDD modeling from Event Storming and CQRS.
- `ddd-to-tdd-handoff`: converts confirmed DDD outputs into executable TDD slices.
- `implementation-planning`: writes small, verifiable implementation plans before coding.
- `executing-implementation-plan`: reviews and executes a plan one checked task at a time.
- `systematic-debugging`: reproduces failures, proves root cause, and protects fixes with regression coverage.
- `verification-before-completion`: completion gate for requirements, changed files, command evidence, skipped checks, and remaining risk.
- `requesting-code-review`: performs a bug-focused self-review after implementation.
- `receiving-code-review`: classifies and resolves review feedback with verification.
- `finishing-development-branch`: prepares a branch for commit, push, PR, or handoff.
- `parallel-agent-orchestration`: splits independent work across agents with non-overlapping ownership.
- `tdd-skill`: project-agnostic RED/GREEN/REFACTOR TDD workflow and protocol validation.
- `spring-web-boundaries`: Spring Web boundary guardrails for controllers, endpoints, validation, security, uploads/downloads, exports, and service layering.

## Workflow Map

```text
user request
  -> engineering-workflow-router
    -> domain complexity: ddd-event-storming-design
    -> confirmed design to implementation: ddd-to-tdd-handoff
    -> multi-step work: implementation-planning
    -> coding: executing-implementation-plan
      -> behavior slice: tdd-skill
      -> Spring Web change: spring-web-boundaries
      -> failure or unknown root cause: systematic-debugging
    -> implementation complete: requesting-code-review
    -> review feedback: receiving-code-review
    -> final claim: verification-before-completion
    -> commit or PR: finishing-development-branch
```

## Repository Layout

```text
engineering-workflow-router/
ddd-event-storming-design/
ddd-to-tdd-handoff/
implementation-planning/
executing-implementation-plan/
systematic-debugging/
verification-before-completion/
requesting-code-review/
receiving-code-review/
finishing-development-branch/
parallel-agent-orchestration/
tdd-skill/
spring-web-boundaries/
```

Each directory is an independent Codex skill with a required `SKILL.md` and optional `agents/`, `references/`, `scripts/`, and `templates/`.

## Validation

Format validation:

```bash
python -X utf8 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py engineering-workflow-router
```

TDD protocol regression:

```bash
python -X utf8 tdd-skill/scripts/run_protocol_examples.py
```

DDD design guardrail regression:

```bash
python -X utf8 ddd-event-storming-design/scripts/run_design_examples.py
```

## Commit Message

Use Chinese Conventional Commits:

```text
feat: 新增工程工作流入口调度器
fix: 修复 DDD 校验脚本编码问题
docs: 更新技能组合说明
```
