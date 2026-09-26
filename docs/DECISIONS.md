# Decision Log

> This file records decisions that still constrain future work. It is not a changelog and not a place to duplicate Design Doc / Exec Plan details. Each entry must be no more than 15 lines.
>
> ### Admission Criteria
>
> Record a decision only when at least one condition is true:
>
> - Architecture boundary, dependency direction, data model, or external contract choice that constrains future implementation
> - Rejected approach that is likely to be proposed again and needs a durable "why not"
> - Cross-layer / cross-package engineering convention
> - Deferred decision with explicit restart conditions
>
> Do not record UI placement, one-off file/function naming, single-point implementation choices, or details already fully contained in a Design Doc / Exec Plan. In those cases, keep the decision in the carrying doc.
>
> ### Lifecycle
>
> - An entry's body is not edited after it is written; when a decision changes, delete the old entry and write a new one that does not narrate what it replaced or what happened afterwards
> - Revalidate existing entries when the related domain changes; do not only append new decisions
> - Delete a decision when it expires, is superseded, or no longer constrains future work
> - Move it to `docs/archive/` only when it retains historical research value; archived content is not current authority
> - Do not keep a retired-decisions list; history belongs in git, carrying documents, and archived snapshots
>
> ### Format
>
> - Ad-hoc / conversation decisions: `AD[N]`
> - Design Doc decisions: `D[N]` only when the decision crosses the document boundary
> - Exec Plan decisions: `E[N]` only when the decision crosses the plan boundary
> - Keep each entry short: what changed, why, trade-off, link.

---

## Decision Records

<!-- EXAMPLE (remove when first real entry is added):

### AD1 — Chose Zod over Joi for boundary validation (2025-01-20)

- **Decision**: Use Zod for all external input boundary schemas.
- **Why**: Better TypeScript inference and shared client/server schema reuse.
- **Trade-off**: Smaller ecosystem than Joi; accepted because type inference matters more for this codebase.
- **Link**: Conversation / PR / related doc.

-->
