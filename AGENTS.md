# AGENTS.md

## Communication Rules

Your reader is a senior engineer with full context on the project. They do not need background, encouragement, or restatements of what they just said.

1. **No repetition.** State each conclusion once. Do not rephrase the same point.
2. **Skip obvious reasoning.** If evidence directly implies a conclusion, give the conclusion. Do not walk through steps unless the chain is non-obvious.
3. **Use tables for structured comparison, not prose.** Bad: "A is high because X. B is medium because Y." Good: a markdown table with columns `Item | Decision | Reason`.
4. **No decorative formatting.** Do not use horizontal rules, box-drawing characters, or headers on every paragraph. Use headers only when sections genuinely need separation.
5. **Conclusion first.** Lead with the decision / conclusion / action item, then supporting evidence.
6. **No meta-narration.** Do not say "if you agree, reply X and I will start." Do not narrate what you are about to do. Either do it, or propose it.
7. **Density check.** Ask yourself: "if I cut half of this, would the information content stay the same?" If yes, cut.
8. **Concrete references.** When referring to a module, file, component, variable, plan, or concept, write the concrete name. Avoid vague references like "it", "this", "that one", "the previous one", or temporary labels across messages.
9. **Anti-quota principle for report-style output.** When asked to produce findings / issues / risks / suggestions / alternatives, report only what you actually found. Empty lists are valid. Specifically forbidden:
   - Inventing severity buckets or forcing every bucket to contain something
   - Choosing from fixed options when reality falls outside the options
   - Filler rows like "no issues found in category X"
   - Giving an overall judgment when there are no findings
   - Promoting uncertain nits into issues so the report looks productive

   Distinction: enumerating internal state ("what decisions did I make") is bounded and required; filling external categories ("list one issue in each failure mode") encourages hallucinated bucket-filling.

## UI/UX Rules

- Express information through UI structure, hierarchy, state, affordance, disabled/loading/selected/empty states, and direct manipulation. Do not compensate for an unclear interaction model with explanatory copy. Copy is for labels, errors, confirmations, and necessary accessibility support.

## ⛔ Hard Rules (Must follow on every task, no exceptions)

> **Task starting frame.** Your role is not to ship code — it is to find the right abstraction. If the right abstraction requires changing 10 files, change 10 files. If you can only determine the abstraction by asking, ask first. "Ship fast" is not the goal; "produce something that holds up 6 months from now" is.

1. **STOP — do not write code directly.** After receiving any development task, first read the relevant docs from the Repository Knowledge Map below.
2. **Docs before code when criteria are met.** If the task requires a Design Doc or Exec Plan, create the doc and get user confirmation before coding.
3. **Plan before execute.** Present what files you plan to change, why, and how. Wait for explicit user approval before making changes.
4. **Self-review + doc sync after completion.** After code changes, run the Pre-delivery Self-review checklist, then update affected docs. Skipping either step means the task is incomplete.
5. **Tests first.** When working on core business logic, write tests first, confirm they fail, then implement.
6. **No "minimal runnable loop" feature delivery.** For real feature work, implement the final user-facing path. Do not deliver scaffolding, mock backends, placeholders, or dual-path transition code unless the user explicitly asks for a prototype/spike/placeholder.
7. **No "minimum viable / shortest path" solutions.** The proposal must target the complete form of the goal. If you catch yourself trimming requirements for convenience, stop and return to the complete proposal.
8. **No mid-flight checks during Exec Plan execution.** During Exec Plan execution, do not use phase-by-phase lint/test/typecheck/build as acceptance gates. Acceptance happens once after the whole plan is implemented. The project's full CI command, as defined under Common Commands, is expensive and must run only once per task at final delivery state; use targeted tests or single-module checks for development feedback.
9. **No code written only to pass checks.** Do not add placeholder implementations, empty branches, `@ts-ignore`, `eslint-disable`, generic catch-all wrappers, or coverage-only tests to make checks pass. Fix the design instead.
10. **No silent decisions.** Any Design Doc, Exec Plan, or non-trivial change proposal must contain a `## Decisions Made Without Asking` section listing: (a) decisions made without asking the user; (b) whether the choice was made because it is the right abstraction or merely the smallest change. If the reason is smallest change / convenience, stop and ask. Enumerate decisions themselves; do not fabricate alternatives just to fill a comparison table.
11. **No unrequested actions.** Do only what the user explicitly requested. Do not opportunistically modify, clean up, or expand scope beyond the request; report issues discovered along the way without acting on them. Suggestions must not be implemented without explicit user approval. If the user says stop, stop immediately without cleanup actions.
12. **No minimum-diff thinking.** Before implementing, answer: "is this the smallest-diff approach, or the right-abstraction approach?" If they differ, choose the right abstraction and explain why the smallest diff is wrong.
13. **No ledger writes without approval.** Before adding or rewriting any entry in `TECH_DEBT.md` or `BACKLOG.md`, present the entry and the reason for admitting it to the user and get explicit approval. When you find an issue, report it; do not log it yourself. Deleting repaid, invalidated, or superseded entries needs no approval.

> Violating any of the above = failure. Better to ask one more question than to skip documentation.

---

## Repository Knowledge Map

> Give the agent a map, not a 1000-page manual. Read the map first, dive deeper as needed.

### Architecture & Quality

- **[ARCHITECTURE.md](ARCHITECTURE.md)** — Architecture map: module structure, layering rules, dependency directions, cross-cutting concerns
- **[docs/STATE.md](docs/STATE.md)** — Runtime and infrastructure state, known limitations (**must-read for new sessions to avoid wrong assumptions**)
- **[docs/DECISIONS.md](docs/DECISIONS.md)** — Still-binding technical decisions and trade-offs
- **[docs/TESTING.md](docs/TESTING.md)** — Testing strategy
- **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** — Deployment targets, runtime config, smoke tests, rollback notes

### Product Knowledge

- **[docs/product-specs/knowledge-base.md](docs/product-specs/knowledge-base.md)** — Core feature descriptions, key file paths, data model
- **[docs/product-specs/glossary.md](docs/product-specs/glossary.md)** — Canonical terms and definitions used across the project

### Design Documents

- **[docs/design-docs/index.md](docs/design-docs/index.md)** — Design document index (technical proposals & architecture decisions)

### Execution Plans & Work Tracking

- **[docs/exec-plans/index.md](docs/exec-plans/index.md)** — Execution plan index (active/completed plans)
- **[docs/TECH_DEBT.md](docs/TECH_DEBT.md)** — Technical debt: implementation deviations from the known-correct shape
- **[docs/BACKLOG.md](docs/BACKLOG.md)** — Product gaps, deferred decisions, and operational/security follow-ups

### Archive

- **[docs/archive/](docs/archive/README.md)** — Documents that have completed their purpose; read-only and never authoritative for current work

### Document Templates

- **[docs/templates/exec-plan.md](docs/templates/exec-plan.md)** — Must use this template when creating new execution plans
- **[docs/templates/design-doc.md](docs/templates/design-doc.md)** — Must use this template when creating new design documents

### References

- **[docs/references/](docs/references/)** — External guides, configuration docs, reference articles

---

## Common Commands

<!-- CUSTOMIZE: Fill in your project's common commands. Omit commands that do not exist. -->

```bash
# Development
# <your dev command>

# Code Quality
# <your lint/format command>
# <your full CI command>  # Expensive; run once at final delivery state

# Testing
# <your test commands>
```

## Tech Stack

<!-- CUSTOMIZE: Describe your tech stack here. -->

## Coding Rules

<!-- CUSTOMIZE: Define project-specific coding rules here. -->

## Testing

<!-- CUSTOMIZE: Define project-specific testing rules and conventions here. -->

Detailed testing strategy: [docs/TESTING.md](docs/TESTING.md)

### TDD Discipline (Agent-enforced)

For any task involving core business logic, follow Red → Green → Refactor:

1. **Write tests first** based on the Design Doc / Exec Plan / approved conversation plan behavioral contract
2. **Confirm red**: run tests and confirm they fail for the intended reason
3. **Implement** the final product code required by the spec
4. **Refactor** once tests pass

<!-- CUSTOMIZE: Define which scenarios are exempt from strict TDD, if any. -->

### Comments Do Not Cite Doc Anchors

Code and tests **do not** carry anchors into design docs such as `@spec`, `D1 §4`, or `P8`. Docs get reorganized and sections renamed, but these anchors do not follow; a stale pointer is worse than none. A comment explains **why the code is written this way**; it does not tell the reader which section of which document to look up.

## Development Workflow

### Document-Driven Principle (Mandatory)

> Knowledge the agent cannot see does not exist. Durable decisions, proposals, and context must live in `docs/`, not only in conversation or memory.

**Before starting a task:** read the relevant docs from the Repository Knowledge Map.

**After completing a task:** update docs according to Fact Ownership and the Doc Sync Matrix.

#### Fact Ownership

Every fact has exactly one owning document; other documents link to it instead of restating it.

| Fact | Sole owner | When to change |
|---|---|---|
| What users can and cannot do now; capability boundaries | [knowledge-base.md](docs/product-specs/knowledge-base.md) | A capability is added, removed, or changed |
| Runtime and infrastructure state; known limitations | [STATE.md](docs/STATE.md) | A resource, binding, deployment topology, or limitation changes |
| Module boundaries, dependency direction, state ownership | [ARCHITECTURE.md](ARCHITECTURE.md) | A boundary changes |
| Test strategy, layering, and quality gates | [TESTING.md](docs/TESTING.md) | The test strategy itself changes |
| Deployment targets, runtime configuration, smoke tests, rollback | [DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deployment or configuration changes |
| The approach and rationale of one design | Design Doc | Only while Draft or In progress (see the lifecycle below) |
| Cross-document decisions that constrain future work | [DECISIONS.md](docs/DECISIONS.md) | A new decision, or one replacing an old decision |
| Interaction details, styling, copy, parameters, implementation details | Code and tests | Never written into a durable document |

**Change only entries whose facts actually changed.** If a PR does not change a fact a document states, do not touch that document; never opportunistically reword, reorder, compress, or extend unaffected entries. Every documentation change in the diff must correspond to a fact that really changed in this change.

#### Doc Sync Matrix

| Trigger Event | Must check / update |
|---|---|
| **Exec Plan completed** | [exec-plans/index.md](docs/exec-plans/index.md) (move plan to `completed/`); check [knowledge-base.md](docs/product-specs/knowledge-base.md), [STATE.md](docs/STATE.md), and [ARCHITECTURE.md](ARCHITECTURE.md) against Fact Ownership |
| **Design Doc implementation merged** | Set status to `Implemented`, add the `Body fingerprint` line reported by `python3 scripts/check-docs.py`, and sync the status column in [design-docs/index.md](docs/design-docs/index.md) |
| **Design Doc enters implementation** | [ARCHITECTURE.md](ARCHITECTURE.md) if architecture changed; record in [DECISIONS.md](docs/DECISIONS.md) only if the decision crosses the Design Doc boundary |
| **User-visible capability added/removed/changed** | The matching entry in [knowledge-base.md](docs/product-specs/knowledge-base.md); interaction details are not recorded |
| **An implemented Design Doc or an existing decision is overturned** | Write the rationale in a new carrier (a new Design Doc, an `AD` entry that meets the admission criteria, otherwise the PR description); the old Design Doc only updates its `Superseded` line, and the old decision entry is deleted |
| **Architecture/layering changed** | [ARCHITECTURE.md](ARCHITECTURE.md) |
| **Technical decision made without a carrying doc** | [DECISIONS.md](docs/DECISIONS.md), after applying the admission criteria in that file |
| **New infrastructure/dependency/deployment target introduced** | [STATE.md](docs/STATE.md), [DEPLOYMENT.md](docs/DEPLOYMENT.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| **New design proposal** | Create a doc in `docs/design-docs/` using [design-doc.md](docs/templates/design-doc.md), update [design-docs/index.md](docs/design-docs/index.md) |
| **New execution plan** | Create a doc in `docs/exec-plans/active/` using [exec-plan.md](docs/templates/exec-plan.md), update [exec-plans/index.md](docs/exec-plans/index.md) |
| **New tech debt discovered** | Report it to the user; write it to [TECH_DEBT.md](docs/TECH_DEBT.md) only after approval (Hard Rule #13), applying the admission criteria in that file |
| **New product gap / deferred decision / operational follow-up discovered** | Report it to the user; write it to [BACKLOG.md](docs/BACKLOG.md) only after approval (Hard Rule #13), applying the admission criteria in that file |
| **Document has completed its purpose but retains historical value** | Move it to [archive/](docs/archive/README.md) and record its original location and archive reason; delete it if it has no historical value |

**Reverse criteria for durable docs (check before writing):** Each durable document answers exactly one question; if a line hits the criteria, it must not be written there. When unsure, do not write it: missing one line costs far less than turning the document into a dumping ground.

| Document | Answers | Do not write if |
|---|---|---|
| `ARCHITECTURE.md` | Boundaries, dependency direction, state ownership, cross-cutting choices, open questions | Renaming a file / adding a component / adding a route would invalidate the line; per-file inventories; install commands and operational steps |
| `docs/TESTING.md` | What to test, what not to test, how to run | Adding one test file would invalidate the line; concrete stubs, framework gotchas, restated configuration |
| `docs/STATE.md` | What the runtime and infrastructure are now, which constraints still hold | The line describes a decision or proposal and would lose its meaning if the Design Doc were deleted; the line describes a product capability (belongs in `knowledge-base.md`) |
| `knowledge-base.md` | What users can and cannot do now, and where the authoritative docs and key paths are | The implementation could change without changing user-visible behavior; interaction micro-details (icons, animation durations, tooltip copy, zoom ratios, styling); implementation parameters (timeouts, retries, refresh intervals, page sizes); restating rules from `AGENTS.md` |
| `docs/DECISIONS.md` | Which choices still constrain future work, and why | Fully contained in a Design Doc; narrates what it replaced or what happened afterwards |

**`STATE.md` / `knowledge-base.md` hard budget:** These files are current snapshots organized by domain and feature, respectively. Rewrite an entry only when a fact it states changes, and change only the part that changed; never append process detail to an old entry. Each entry must be no more than five lines (roughly 300 words) and contain only the conclusion plus links to the authoritative Design Doc, Exec Plan, or source entry point. Push excess detail into the authoritative document instead of expanding the snapshot. Dates, revision history, implementation process, and changelog language such as "superseded" or "pending application" are forbidden.

**`DECISIONS.md` hard budget:** Each decision must be no more than 15 lines and contain only the still-binding choice, rationale, trade-off, and link. An entry's body is not edited after it is written. Delete a decision when it expires, is superseded, or no longer constrains future work; the entry that replaces it does not narrate the old one. Move it to `docs/archive/` only when it retains historical research value.

**`TECH_DEBT.md` / `BACKLOG.md` lifecycle:** When changing a related domain or syncing docs, revalidate affected existing entries instead of only appending new rows. Delete entries that have been repaid, started, abandoned, invalidated, or superseded by a new design. History belongs in git, Design Docs, and completed Exec Plans. Never maintain resolved/completed tables or duplicate work tracked by an active Exec Plan.

**No-carrier principle (admission prerequisite for both ledgers):** `BACKLOG.md` / `TECH_DEBT.md` admit only items that **have no other carrier**. Decided approaches are carried by Design Docs and `ARCHITECTURE.md`; scheduled work is carried by its plan (an approved conversation plan or an Exec Plan); test-strategy facts are carried by `TESTING.md`. Writing to a ledger when one of these carriers exists is duplicate tracking and is forbidden. The ledgers are not the default destination for work notes; "logging it so we don't forget" is not an admission reason.

**Migration state rule:** Durable documents must not track whether a specific migration is pending or applied. Transient execution state belongs in the deployment system or an active Exec Plan; durable docs record only the current schema facts, deployment mechanism, and still-binding constraints.

**Cross-reference rule:** When a fact changes, fix only its owning document; other documents reference it by link, so check that those links still point to the right place instead of restating the fact elsewhere.

**Index and archive maintenance:** After adding or moving a Design Doc or Exec Plan under `docs/`, update the corresponding `index.md`. Move other documents that have completed their purpose but retain historical value to `docs/archive/`; archive documents are read-only and must not serve as authority for new work.

**When to create a Design Doc — default: do not create one.** Create a Design Doc only when both conditions are true:

- The change is materially significant: new module/subsystem, module boundary or dependency direction change, data model or external contract change, new external dependency choice, or user-visible interaction model redesign
- There are at least two real approaches with different structural consequences, and choosing wrong would cause multi-file or irreversible rework

Do **not** create a Design Doc for single-component UI adjustments, copy/parameter/threshold changes, implementation-path-obvious features, bug fixes, or single-point performance fixes.

**Design Doc lifecycle:** `Draft → In progress → Implemented`. The body of a Draft or In progress doc may change, but only through the Exec Plan or PR that implements it. Once the implementation merges, the status becomes `Implemented` and the body is frozen, without waiting for real-world acceptance; deviations found during acceptance go into the Exec Plan's implementation deviation log. `python3 scripts/check-docs.py` verifies frozen bodies through the `Body fingerprint` header line and checks that the index status column matches each doc's status line. No later work rewrites an Implemented Design Doc: behavior changes update only `knowledge-base.md`; when part of the design is overturned, the rationale goes into a new carrier and the old doc only adds or updates one line, `**Superseded**: §x → carrier`. A `Deferred` doc may change until it starts.

**When to create an Exec Plan — default: do not create one.** Create an Exec Plan only when any condition is true:

- Cross-package or cross-service cutover with ordering dependencies and an unsafe intermediate state
- Database migration or other irreversible change
- Multi-PR / multi-session work that needs durable resume state

A change touching many files is not by itself an Exec Plan trigger if the work can be completed safely in one PR.

**Document Naming Conventions:**

| Document Type | Format | Location | Example |
|---|---|---|---|
| Design Doc | `D{number}-{kebab-case-description}.md` | `docs/design-docs/` | `D1-auth-flow.md` |
| Exec Plan | `E{number}-{kebab-case-description}.md` | `docs/exec-plans/active/` | `E1-db-migration.md` |

- The number must increment from the corresponding `index.md`
- The description must be short kebab-case
- Completed Exec Plans move from `active/` to `completed/` without renaming

**No doc needed:** bug fixes, style/copy tweaks, single-PR features, and localized refactors that do not hit the criteria above. "No doc needed" does not mean "no plan needed": Hard Rule #3 and Hard Rule #10 still apply, with the conversation or PR description as the carrier.

### Self-Rationalization Check (Agent self-check)

| If you are thinking... | The reality is... |
|---|---|
| "This is simple; no process needed" | Simple changes are where assumptions break most easily |
| "I already know how it works" | Verify with evidence |
| "TDD is too heavy for this fix" | Simple code breaks too |
| "I will update docs later" | Later does not happen; update docs now |
| "Just change these two lines" | This is minimum-diff thinking (Rule #12); check the abstraction first |
| "This decision is not important" | Importance is the user's call; list the decision for review |

### Pre-delivery Self-review (Mandatory)

After code is written and CI passes, show the checklist results to the user.

**Spec Alignment Check:**

- [ ] Every postcondition in the behavioral contract has a corresponding test
- [ ] Every scenario in the edge case catalog has a corresponding test
- [ ] Implementation behavior is described in this change's spec source (a Draft / In progress Design Doc, an Exec Plan, or an approved plan); no Implemented Design Doc was rewritten

**Test Quality Check:**

- [ ] No tautological tests that only repeat implementation logic
- [ ] No over-mocking of core logic
- [ ] Error paths covered where relevant

**Implementation Quality Check:**

- [ ] No unresolved placeholder comments (`TODO`, `FIXME`, `HACK`) unless tracked in `TECH_DEBT.md`
- [ ] Error handling uses specific error types, not generic catch-all suppression
- [ ] External state dependencies are explicit
- [ ] Implementation follows `ARCHITECTURE.md` layering rules

**Security Check:**

- [ ] User input validated at the boundary
- [ ] Operations verify caller permissions where applicable
- [ ] No sensitive information leaks to unauthorized contexts

**Doc Sync Check (show evidence, not just checkboxes):**

- [ ] Every documentation change in the diff corresponds to a fact that really changed; documents and entries whose facts did not change were left untouched
- [ ] If this completed an Exec Plan, the plan moved to `completed/` and `exec-plans/index.md` was updated
- [ ] If a Design Doc's implementation merged, it is marked `Implemented` with its `Body fingerprint`
- [ ] If architecture/layering changed, `ARCHITECTURE.md` was updated
- [ ] If a user-visible capability changed, the matching `knowledge-base.md` entry was updated
- [ ] If deployment/infrastructure changed, `DEPLOYMENT.md`, `STATE.md`, and `ARCHITECTURE.md` were checked
- [ ] Decisions meeting `DECISIONS.md` admission criteria were recorded
- [ ] New tech debt and backlog items were reported to the user; only approved ones were written to `TECH_DEBT.md` / `BACKLOG.md`
- [ ] Affected existing decisions, tech debt, and backlog entries were revalidated; repaid, started, abandoned, invalidated, or superseded entries were removed
- [ ] `STATE.md` / `knowledge-base.md` entries meet the five-line budget, and `DECISIONS.md` entries meet the 15-line budget
- [ ] Durable documents do not track specific migration application state
- [ ] Cross-references between updated docs were verified, and archived documents were not treated as current authority
- [ ] Evidence: list each updated doc and a one-line summary

### Task Completion Criteria

A development task is complete only when all conditions are met:

1. ✅ CI checks pass
2. ✅ Self-review checklist shown to the user
3. ✅ Affected docs updated
4. ✅ New/modified code is traceable to a spec source (Design Doc, Exec Plan, or approved no-doc task plan)
5. ✅ Remaining gaps are either fixed or explicitly tracked in `TECH_DEBT.md` / `BACKLOG.md`

## Git Workflow

- **Never commit directly to the main branch** — verify current branch with `git branch` before committing
- Merge via feature branch + PR. Naming: `feat/xxx`, `fix/xxx`, `refactor/xxx`, `test/xxx`
- **Never run `git checkout -- .`, `git checkout <branch> -- .`, or `git restore .` with uncommitted changes in the working tree**
- **Prefix any git command that opens an editor with `GIT_EDITOR=true`**:
  - `git rebase --continue` / `git rebase -i` → `GIT_EDITOR=true git rebase --continue`
  - `git commit --amend` without `-m` → add `-m "..."` or `--no-edit`
  - `git merge` with a merge commit and no `-m` → add `--no-edit` or `-m "..."`
  - `git tag -a` / `git revert` without `-m` → add `-m "..."`
