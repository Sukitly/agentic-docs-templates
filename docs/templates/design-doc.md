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

- **On success**: [How does system state change? What is returned?]
- **On failure**: [What is the system state? What error type is returned?]

### Invariants

- [What conditions hold true throughout the entire operation?]

## Edge Case Catalog

| Scenario               | Input                                 | Expected Behavior                    |
| ---------------------- | ------------------------------------- | ------------------------------------ |
| Empty input            | `null` / `""`                         | Return validation error              |
| Oversized input        | Exceeds limit                         | Reject with message                  |
| No permission          | Unauthorized caller                   | Return permission error              |
| Concurrent operation   | Same resource modified simultaneously | Later writer receives conflict error |
| Resource not found     | Invalid ID                            | Return not-found error               |
| _[Add more as needed]_ |                                       |                                      |

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

## Acceptance Criteria

[How to determine success? Each criterion should map to a behavioral contract postcondition or edge case above]

1. [ ] [Criterion 1 — maps to which postcondition]
2. [ ] [Criterion 2 — maps to which edge case scenario]
3. [ ] ...
