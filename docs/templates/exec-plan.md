# [Plan Title]

> **Created**: YYYY-MM-DD
> **Status**: 📋 Proposal | ⏳ Pending | 🔄 In Progress | ✅ Completed
> **Priority**: High | Medium | Low
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

> See `AGENTS.md` Hard Rule #10. This section lists non-trivial choices the agent made without asking the user during plan creation. The user must review this section before approving the plan. Do not bury decisions in Proposal and make the user discover them in the diff.
>
> If no such decisions exist, write: "None — all non-trivial choices are explicitly discussed in Proposal above, or were pre-aligned with the user."

| # | Decision | My choice | Rationale (✅ right abstraction / ⚠️ smallest change) | User confirmation needed? |
|---|---|---|---|---|
| 1 | <!-- e.g., Module ownership for email sending --> | <!-- New EmailService --> | <!-- ✅ Clear responsibility — NotificationService should not own SMTP details --> | <!-- Yes --> |

> Any row with ⚠️ in Rationale must stop and ask the user. A ⚠️ decision = a shortcut taken without user approval, equivalent to minimum-diff thinking.
>
> Distinction from Decision Log below: this section lists planning-stage silent decisions for user review before approval; Decision Log records decisions that arise during execution.

---

## Docs Impact

> Must fill on plan creation. Use Fact Ownership and the Doc Sync Matrix in `AGENTS.md` to identify affected docs; list only docs whose facts this plan really changes.
> On plan completion, every row must be checked off — unchecked items mean the plan is not complete.
> If this plan originates from a `TECH_DEBT.md` or `BACKLOG.md` entry, remove that entry from its source queue immediately when creating the plan and record the removal below; do not wait for plan completion or duplicate tracking.

| Document | What to update | Updated? |
|---|---|---|
| `docs/STATE.md` | <!-- Only runtime / infrastructure / known-limitation changes, e.g., add a storage bucket binding --> | ☐ |
| `ARCHITECTURE.md` | <!-- e.g., Add module Y to layering map --> | ☐ |
| `docs/DECISIONS.md` | <!-- Only if a decision meets the file's admission criteria --> | ☐ |
| `docs/product-specs/knowledge-base.md` | <!-- User-visible capability changes, e.g., add an "export report" feature entry --> | ☐ |
| `docs/DEPLOYMENT.md` | <!-- e.g., Add new deploy target / env / smoke test --> | ☐ |
| `docs/exec-plans/index.md` | Move this plan to completed | ☐ |
<!-- Remove rows that do not apply. Add rows for any other affected docs. If the plan originates from TECH_DEBT or BACKLOG, add the corresponding queue-removal record. -->

---

## Verification Metrics

[How do we measure success? List concrete checks / commands / manual verification items.]

---

## Final Phase: Documentation Sync

> This phase is always the last phase of any plan. Do not mark the plan as completed until all items are checked.

- [ ] Update all docs listed in the Docs Impact table above
- [ ] Verify cross-references between updated docs are consistent
- [ ] Documents and entries whose facts did not change were left untouched
- [ ] The corresponding Design Doc was marked `Implemented` with its `Body fingerprint` when the implementation merged
- [ ] Record any decisions that meet `docs/DECISIONS.md` admission criteria
- [ ] Move this plan from `docs/exec-plans/active/` to `docs/exec-plans/completed/`
- [ ] Update `docs/exec-plans/index.md`

---

## Implementation Deviation Log

| Date | Phase | Plan vs Actual | Reason | Impact |
|---|---|---|---|---|
| — | — | — | — | — |

## Progress Log

| Date | Progress | Notes |
|---|---|---|
| YYYY-MM-DD | Created plan document | — |

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| — | — | — |
