# [Design Document Title]

> **Created**: YYYY-MM-DD
> **Last updated**: YYYY-MM-DD
> **Status**: Draft | Adopted | Deprecated
> **Impact scope**: [Affected modules/domains]

---

## Problem Statement

[What is the current problem? Why is a design needed?]

## Behavioral Contract

### Preconditions

- [What must be true before invoking this functionality? e.g., user is authenticated, resource exists, sufficient quota]

### Postconditions

- **P1**: [On success — system state change. e.g., record written to database]
- **P2**: [On success — return value. e.g., returns `ApiResult<Entity>`]
- **P3**: [On failure — system state. e.g., operation rolled back, returns error]

### Invariants

- [What conditions hold true throughout the entire operation?]

## Edge Case Catalog

| ID   | Scenario               | Input                                 | Expected Behavior                    |
| ---- | ---------------------- | ------------------------------------- | ------------------------------------ |
| B1   | Empty input            | `null` / `""`                         | Return validation error              |
| B2   | Oversized input        | Exceeds limit                         | Reject with message                  |
| B3   | No permission          | Unauthorized caller                   | Return permission error              |
| B4   | Concurrent operation   | Same resource modified simultaneously | Later writer receives conflict error |
| B5   | Resource not found     | Invalid ID                            | Return not-found error               |
| _B6_ | _[Add more as needed]_ |                                       |                                      |

## Error Patterns

| Error Type             | Trigger Condition      | Caller-facing Response | System Behavior                   |
| ---------------------- | ---------------------- | ---------------------- | --------------------------------- |
| Validation error       | Input fails schema     | Error message returned | Request rejected, no side effects |
| Permission error       | Caller lacks access    | Permission denied      | Request rejected, logged          |
| Not found              | Resource doesn't exist | Not-found response     | Request rejected                  |
| _[Add more as needed]_ |                        |                        |                                   |

## Proposal

[Detailed technical proposal]

## Alternatives Considered

[Approaches considered but not adopted, and reasons for rejection]

## Decisions Made Without Asking

> ⛔ See [AGENTS.md Hard Rule #10](../../AGENTS.md). This section lists non-trivial choices the agent made without asking the user, for user review before adopting this doc. Forbidden to bury decisions in the "Proposal" prose and let the user discover them via diff.
>
> If no such decisions exist, write: "None — all non-trivial choices are explicitly discussed in ## Proposal / ## Alternatives Considered above, or were pre-aligned with the user."

| # | Decision | Alternatives | My choice | Rationale (✅ right abstraction / ⚠️ smallest change) | User confirmation needed? |
|---|----------|--------------|-----------|----------------------------------------------------|---------------------------|
| 1 | <!-- e.g., Chapter draft persistence form --> | <!-- (a) JSONB column (b) New chapter_drafts table --> | <!-- (b) --> | <!-- ✅ Clear schema, supports partial query, index-friendly --> | <!-- Yes --> |

> Any row with ⚠️ in Rationale **must stop and ask the user** — do not proceed to implementation. A ⚠️ decision = a shortcut taken without user approval, equivalent to minimum-diff thinking (rule #11).

## Acceptance Criteria

[How to determine success? Each criterion should map to a behavioral contract postcondition or edge case above]

1. [ ] [Criterion 1 — maps to P1]
2. [ ] [Criterion 2 — maps to B1, B2]
3. [ ] ...
