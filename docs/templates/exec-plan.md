# [Plan Title]

> **Created**: YYYY-MM-DD
> **Last updated**: YYYY-MM-DD
> **Status**: 📋 Proposal | ⏳ Pending | 🔄 In Progress | ✅ Completed
> **Priority**: 🔴 High | 🟡 Medium | 🟢 Low
> **Goal**: [One-sentence goal description]
> **Related PR**: TBD

---

## Background

[Why are we doing this? What is the current problem?]

## AS-IS Analysis

### Current Behavior

- [Describe existing behavior relevant to this plan, with code pointers]

### Key Files

- `path/to/file.ts`: [Why relevant, current responsibility]

### Known Unknowns

- [Explicitly list uncertain items to avoid planning based on assumptions]

## Proposal

[Technical approach overview]

### Phase 1: [Phase Name]

[Specific task description]

### Phase 2: [Phase Name]

[Specific task description]

---

## Decisions Made Without Asking

> ⛔ See [AGENTS.md Hard Rule #10](../../../AGENTS.md). This section lists non-trivial choices the agent made without asking the user during plan creation. The user must review this section before approving the plan. Forbidden to bury decisions in ## Proposal and let the user discover them via diff.
>
> If no such decisions exist, write: "None — all non-trivial choices are explicitly discussed in ## Proposal above, or were pre-aligned with the user."

| # | Decision | Alternatives | My choice | Rationale (✅ right abstraction / ⚠️ smallest change) | User confirmation needed? |
|---|----------|--------------|-----------|----------------------------------------------------|---------------------------|
| 1 | <!-- e.g., New dedicated service vs extending existing --> | <!-- (a) New EmailService (b) Extend NotificationService with sendEmail --> | <!-- (a) --> | <!-- ✅ Clear responsibility — NotificationService should not own SMTP details --> | <!-- Yes --> |

> Any row with ⚠️ in Rationale **must stop and ask the user** — do not proceed to implementation. A ⚠️ decision = a shortcut taken without user approval, equivalent to minimum-diff thinking (rule #11).

> Distinction from "Decision Log" below: this section lists **planning-stage** silent decisions for user review before approval; Decision Log is the **after-the-fact** record of decisions that arose during execution.

---

## Docs Impact

> ⛔ **Must fill on plan creation.** Use the [Doc Sync Matrix](../../AGENTS.md#doc-sync-matrix) to identify affected docs.
> On plan completion, every row must be checked off — unchecked items mean the plan is NOT complete.

| Document | What to update | Updated? |
|---|---|---|
| [STATE.md](../../docs/STATE.md) | <!-- e.g., Add Feature X to Core Features --> | ☐ |
| [ARCHITECTURE.md](../../ARCHITECTURE.md) | <!-- e.g., Add module Y to diagram --> | ☐ |
| [DECISIONS.md](../../docs/DECISIONS.md) | <!-- e.g., Record choice of Z over W --> | ☐ |
| [knowledge-base.md](../../docs/product-specs/knowledge-base.md) | <!-- e.g., Add feature description --> | ☐ |
| [exec-plans/index.md](../../docs/exec-plans/index.md) | Move to completed | ☐ |
<!-- Remove rows that don't apply. Add rows for any other affected docs. -->

---

## Verification Metrics

[How do we measure success? List quantifiable metrics]

---

## Final Phase: Documentation Sync

> This phase is always the last phase of any plan. Do NOT mark the plan as completed until all items are checked.

- [ ] Update all docs listed in "Docs Impact" table above
- [ ] Verify cross-references between updated docs are consistent
- [ ] Append decision record to [DECISIONS.md](../../docs/DECISIONS.md)
- [ ] Move this plan from `active/` to `completed/`
- [ ] Update [exec-plans/index.md](../../docs/exec-plans/index.md)

---

## Implementation Deviation Log

| Date | Phase | Plan vs Actual | Reason | Impact |
| ---- | ----- | -------------- | ------ | ------ |
| —    | —     | —              | —      | —      |

## Progress Log

| Date       | Progress              | Notes |
| ---------- | --------------------- | ----- |
| YYYY-MM-DD | Created plan document | —     |

## Decision Log

| Date | Decision | Rationale | Alternatives |
| ---- | -------- | --------- | ------------ |
| —    | —        | —         | —            |
