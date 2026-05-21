# DDD Modeling Anti-Patterns

- Table-first modeling: derive aggregates and events from database tables instead of business facts.
- CRUD masquerading as commands: name commands as create/update/delete operations without business intent.
- Technical event pollution: model MQ delivery, logs, cache refresh, HTTP calls, or notifications as domain events when the business does not care.
- Policy hides invariant: move aggregate rules into an event reaction to avoid modeling the consistency boundary.
- Aggregate by noun: create one aggregate per noun rather than by lifecycle, consistency, and behavior.
- Read model leakage: add page/report fields to aggregate state only because a query needs them.
- Framework-shaped domain: treat controllers, DTOs, repositories, or packages as the domain model.
- Unproduced event: keep a domain event without a command, policy, process, or external fact that can produce it.
- Unprojectable read model: define a read model that cannot be built from domain events without identifying the missing event or field.
- Premature bounded contexts: split contexts before the current problem domain has enough evidence.
