# Decision Log

> Agent should read this file at the start of each new session to quickly understand historical decision context.
>
> **Last updated**: YYYY-MM-DD
>
> ### What to record here
>
> Record **any meaningful technical decision or trade-off**, not just plan completions. This includes:
> - Decisions from completed Exec Plans
> - Decisions made during conversation (e.g., "we chose X over Y because...")
> - Decisions from adopted Design Docs
> - Ad-hoc trade-offs during implementation
>
> **How to judge if something is a "decision":** If someone joining the project tomorrow would ask "why did you do it this way?", it should be recorded here.
>
> ### Format
>
> - Plan-related decisions: use `E[N]` prefix (N = Exec Plan number)
> - Conversation/ad-hoc decisions: use `AD[N]` prefix (AD = Ad-hoc Decision, N = sequential)
> - Design Doc decisions: use `D[N]` prefix (N = Design Doc number)

---

## Decision Records

<!-- EXAMPLE (remove when first real entry is added):

### E1 — Database Migration to PostgreSQL (2025-01-15)
- **What changed**: Migrated from SQLite to PostgreSQL for production
- **Why**: SQLite couldn't handle concurrent writes under load
- **Key trade-offs**: Added deployment complexity (need managed DB), but gained concurrent write support and better query performance
- **Not done / Remaining**: Read replicas deferred to E3
- **Details**: [E1-db-migration.md](exec-plans/completed/E1-db-migration.md)

### AD1 — Chose Zod over Joi for validation (2025-01-20)
- **What changed**: Adopted Zod as the project-wide validation library
- **Why**: Better TypeScript type inference, smaller bundle size
- **Key trade-offs**: Less mature ecosystem than Joi, but type safety benefit outweighs
- **Not done / Remaining**: None
- **Details**: Decided in conversation, no separate doc

-->
