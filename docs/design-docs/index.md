# Design Document Index

> Directory of technical proposals and architecture decisions. The agent checks here to understand existing designs and avoid duplication.
>
> Keep this index synchronized with files under `docs/design-docs/`. This repository template should not ship with any design docs beyond this index.

---

## Organization

**Each document records the approach and rationale of one design; it is not the current specification of a domain.** Current capabilities belong in the [knowledge base](../product-specs/knowledge-base.md), and runtime state belongs in [STATE](../STATE.md).

Lifecycle: `Draft → In progress → Implemented`. The body of a Draft or In progress doc changes only through the Exec Plan or PR that implements it; once the implementation merges, the doc becomes `Implemented` and its body is frozen, and deviations found during acceptance go into the plan's implementation deviation log. When part of the design is later overturned, the rationale goes into a new carrier (a new Design Doc, an `AD` entry, or the PR description), the old doc maintains only one line, `**Superseded**: §x → carrier`, and this index's status column is updated to match. `Deferred` means the design is complete but unscheduled; `Current` is for current-boundary documents that are rewritten in place as the user adjusts them. `python3 scripts/check-docs.py` uses the `Body fingerprint` header line to verify that Implemented bodies are unchanged and checks that this index's status column matches each doc's status line.

---

## Documents

| ID | Document | Domain | Status | Summary |
|---|---|---|---|---|
| — | (none) | — | — | — |
