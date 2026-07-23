# Technical Debt

> **Last updated**: 2026-07-23
>
> This file tracks only implementation deviations from the known-correct shape that have a concrete repayment path. It is not a product backlog.
>
> ### Admission Criteria
>
> Record an item only when all conditions are true:
>
> - The current implementation differs from the known-correct shape
> - The deviation has concrete engineering impact and verifiable evidence
> - There is a plausible, describable repayment path
>
> ✅ Include: dead code/columns, wrong abstractions, latent footguns, missing engineering quality gates, and known behavior bugs.
>
> ❌ Exclude: product gaps, enhancement ideas, deferred features, operational follow-ups, unsupported concerns, or work already tracked by an active Exec Plan. Put these in `BACKLOG.md`, the carrying plan, or nowhere, according to their nature.
>
> ### Lifecycle
>
> - Revalidate affected entries when changing the related domain or syncing docs; do not only append new rows
> - Delete an entry when the debt is repaid, invalidated, or superseded by a new design
> - Remove an entry when an active Exec Plan starts carrying the work; never duplicate tracking
> - Do not maintain a resolved table; history belongs in git, Design Docs, and completed Exec Plans

---

## Active Technical Debt

| # | Domain | Description | Impact & Repayment Path | Link | Created |
|---|---|---|---|---|---|
| <!-- 1 --> | <!-- area --> | <!-- implementation deviation --> | <!-- impact and repayment path --> | <!-- related doc/issue --> | <!-- YYYY-MM-DD --> |
