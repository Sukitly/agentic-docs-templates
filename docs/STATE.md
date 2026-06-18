# Application State

> **Last updated**: 2026-06-18
>
> This document is the application's current-state snapshot. Keep only current facts, not history.
>
> ### Update Rules
>
> - Update the affected section in place when state changes
> - Do not append changelog entries or plan-by-plan completion notes
> - Keep the header date as a date only; history belongs in git, Design Docs, Exec Plans, and `DECISIONS.md`

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
