# Knowledge Base

> A feature-organized snapshot of what users can and cannot do now, plus authoritative docs, key file paths, and the data model.
> The agent uses this to understand what the product does and where things live. This file is the sole owner of product capabilities; `STATE.md` and Design Docs do not restate its content.
>
> ### Update Rules (Hard Constraints)
>
> - Rewrite an entry only when a capability it states is added, removed, or changed, and change only the part that changed; never append implementation process to an old entry
> - Admission criteria: do not record anything whose implementation could change without changing user-visible behavior, interaction micro-details (icons, animation durations, tooltip copy, zoom ratios, styling), or implementation parameters (timeouts, retries, refresh intervals, page sizes); these belong in code and tests
> - Each feature entry contains only its purpose/current behavior, authoritative document, key paths, and known gaps, and is no more than five lines (roughly 300 words)
> - Push excess detail into a Design Doc or Exec Plan instead of copying proposal text here
> - Do not include dates, revision history, plan-by-plan history, migration identifiers, or transient states such as "pending" or "applied"

---

## Features

<!-- CUSTOMIZE: Describe each major feature -->
<!-- Example:
### Feature Name
- **Description**: What it does
- **Key files**: `src/modules/feature/`
- **Status**: Active / In Development / Deprecated
-->

---

## Data Model

<!-- CUSTOMIZE: Document your data model (database schema, file formats, API contracts, etc.) -->

---

## Key File Paths

<!-- CUSTOMIZE: Map important files/directories for quick agent navigation -->
<!-- Example:
| Purpose | Path |
|---------|------|
| Entry point | `src/main.ts` |
| Config | `src/config/` |
-->
