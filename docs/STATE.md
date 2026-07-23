# Application State

> **Last updated**: 2026-07-23
>
> This document is the application's current-state snapshot organized by domain. Keep only current facts, not history or change process.
>
> ### Update Rules (Hard Constraints)
>
> - Rewrite the affected entry in place when state changes; never append to an old entry
> - Each entry contains only the current conclusion plus an authoritative Design Doc, Exec Plan, or source entry point, and is no more than five lines (roughly 300 words)
> - Push excess detail into the authoritative document instead of repeating implementation details here
> - Do not include dates, revision history, plan-by-plan completion notes, migration identifiers, or transient states such as "pending" or "applied"
> - Keep `Last updated` as a date only; history belongs in git, Design Docs, Exec Plans, and `DECISIONS.md`

---

<!-- CUSTOMIZE: Replace placeholder content with the project's actual current state. -->

## Project Positioning

[What this repository is, what product/system it owns, and what is explicitly out of scope.]

## Deployment & Runtime

| Component | Domain / Entry | Platform | Runtime | Deploy Source |
|---|---|---|---|---|
| [Component] | [Domain or entry point] | [Platform] | [Runtime] | [How it deploys] |

## Key Infrastructure

| Service | Provider | Purpose | Current State |
|---|---|---|---|
| Database | [Provider] | [Purpose] | [Current state] |
| Auth | [Provider] | [Purpose] | [Current state] |
| Storage | [Provider] | [Purpose] | [Current state] |
| Observability | [Provider] | [Purpose] | [Current state] |

## Domain State

### [Domain / Module]

- [Current fact with pointer to the authoritative Design Doc / Exec Plan if applicable]

## Testing & CI

- [Current test strategy summary. Link to `TESTING.md` for details.]
- [Current CI/quality gate state.]

## Current Work

- Active Exec Plans: see `docs/exec-plans/index.md`
- Technical debt: see `docs/TECH_DEBT.md`
- Product / operations backlog: see `docs/BACKLOG.md`

## Known Limitations

| Limitation | Impact | Reference |
|---|---|---|
| [Limitation] | [Impact] | [Doc / issue / plan] |
