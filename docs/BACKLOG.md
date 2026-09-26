# Backlog

> This file tracks product gaps, deferred decisions, and operational/security follow-ups. It is distinct from `TECH_DEBT.md`.
>
> ### Write Prerequisite
>
> **Get explicit user approval before writing any entry** (`AGENTS.md` Hard Rule #13). Deleting invalidated entries needs no approval.
>
> **Reverse criterion: if the line describes how things are now rather than what should be done, it belongs in `STATE.md`.**
>
> ### Scope
>
> Record an item when it is a capability or follow-up that should exist but is not currently scheduled and has explicit value or restart conditions.
>
> - ✅ Include: deferred product capabilities, restartable capabilities, operational/security follow-ups, and deferred decisions with trigger conditions
> - ❌ Exclude: dead code, wrong abstractions, implementation bugs, or missing quality gates → use `TECH_DEBT.md`
> - ❌ Exclude: speculative ideas without explicit value or restart conditions
> - ❌ Exclude: work already tracked by an active Exec Plan
>
> ### Lifecycle
>
> - Revalidate affected entries when changing the related domain or syncing docs; do not only append new rows
> - Once work formally starts and a Design Doc or active Exec Plan carries it, delete the item immediately; never duplicate tracking. Work with only a `Deferred` Design Doc and no active implementation may remain
> - Delete an item when it is abandoned, invalidated, or superseded by a new design
> - Record an abandonment in `DECISIONS.md` only when it still constrains future work
> - Do not maintain completed or abandoned tables; history belongs in git and carrying documents

---

## Items

| # | Domain | Description | Restart Condition / Notes | Link | Created |
|---|---|---|---|---|---|
| <!-- B1 --> | <!-- area --> | <!-- product gap / deferred decision / ops follow-up --> | <!-- trigger or notes --> | <!-- related doc/issue --> | <!-- YYYY-MM-DD --> |
