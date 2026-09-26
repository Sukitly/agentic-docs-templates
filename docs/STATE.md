# Application State

> This document answers one question: **what the runtime and infrastructure are now, and which constraints still hold.** Product capabilities belong in [knowledge-base.md](product-specs/knowledge-base.md), and test strategy and quality gates belong in [TESTING.md](TESTING.md); do not restate them here.
>
> ### Update Rules (Hard Constraints)
>
> - Reverse criterion: **if a line describes a decision or proposal rather than the current state, it belongs in a Design Doc**; only what still makes sense after deleting that Design Doc is state
> - Reverse criterion: **if a line describes what users can do, it belongs in the knowledge base**; change this file only when a resource, binding, deployment topology, or known limitation changes
> - Change only entries whose facts changed, and only the part that changed; never append to an old entry
> - Each entry contains only the current conclusion plus an authoritative Design Doc, Exec Plan, or source entry point, and is no more than five lines (roughly 300 words)
> - Push excess detail into the authoritative document instead of repeating implementation details here
> - Do not include dates, revision history, plan-by-plan completion notes, migration identifiers, or transient states such as "pending" or "applied"

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

## Current Work

- Active Exec Plans: see `docs/exec-plans/index.md`
- Technical debt: see `docs/TECH_DEBT.md`
- Product / operations backlog: see `docs/BACKLOG.md`

## Known Limitations

| Limitation | Impact | Reference |
|---|---|---|
| [Limitation] | [Impact] | [Doc / issue / plan] |
