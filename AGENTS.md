# AGENTS.md

## Communication Rules

Your reader is a senior engineer with full context on the project. They don't need background, encouragement, or restatements of what they just said.

1. **No repetition.** State each conclusion once. Don't rephrase the same point.
2. **Skip obvious reasoning.** If evidence directly implies a conclusion, give the conclusion. Don't walk through steps unless the chain is non-obvious.
3. **Use tables for structured comparison, not prose.** Bad: "A is P0 because X. B is P1 because Y." Good: markdown table with columns Item | Priority | Reason.
4. **No decorative formatting.** No horizontal rules, no box-drawing characters, no headers on every paragraph. Use headers only when sections genuinely need separation.
5. **Conclusion first.** Lead with the decision / conclusion / action item, then supporting evidence.
6. **No meta-narration.** Don't say "if you agree just reply X and I'll start." Don't narrate what you're about to do. Either do it, or propose it.
7. **Density check.** Ask yourself: "if I cut half of this, would the information content stay the same?" If yes, cut. Replies to a code review should not exceed 30% of the review's own length.
8. **Anti-quota principle for report-style output.** When asked to produce findings / issues / risks / improvement suggestions / alternatives as lists, report only what you **actually found**. Empty lists are a valid and common output. Specifically forbidden:
   - Tagging issues with P0/P1/P2, 🔴🟡🟢, or severity buckets — these pressure you to fill each bucket
   - Picking one of fixed options (a/b/c, yes/no/pending) as a verdict when reality falls outside them
   - Filler rows like "no issues found in category X" / "this section is empty"
   - Giving an "overall assessment / summary judgment" when there are no actual findings
   - Promoting uncertain nits to real issues so the report looks productive

   Underlying distinction: **enumerating internal state** ("what decisions did I make", "what alternatives did I consider") is bounded and required; **filling external categories** ("classify by severity", "list one per category in four failure types") triggers hallucinated bucket-filling and must be refused. When you catch yourself padding, stop and delete the padding.

## ⛔ Hard Rules (Must follow on every task, no exceptions)

> **Task starting frame.** Your role is not to ship code — it's to find the right abstraction. If the right abstraction requires changing 10 files, change 10 files. If you can only determine the abstraction by asking, ask first. "Ship fast" is not the goal; "produce something that holds up 6 months from now" is. Read this on the first step of every task. Don't rely on the 200 lines of rules below to correct a wrong starting point.

1. **STOP — Do NOT write code directly.** After receiving any development task, the first step is to read the relevant docs from the "Repository Knowledge Map" below to understand existing architecture and context.
2. **Docs before code.** If a task requires a Design Doc or Exec Plan (see criteria below), you must **create it and get user confirmation first** before writing any code.
3. **Plan before execute.** Present what files you plan to change, why, and how. **Wait for explicit user approval** before making changes.
4. **Self-review + update docs after completion.** After code changes, you must run the "Pre-delivery Self-review" checklist and show results, then update all affected docs (see "Development Workflow" section). Skipping either step means the task is incomplete.
5. **Tests first.** When working on core business logic, you must write tests first, confirm they fail, then write the implementation (see "TDD Discipline" section).
6. **No "minimal runnable loop" feature development.** For any real feature work, you must directly implement the final end-to-end path that faces the user. Forbidden as delivery strategies: scaffolding first, mock-run-through, placeholder-then-fill, dual-path-transition. Unless the user explicitly requests prototype / spike / placeholder / research, the following are all forbidden: passing off a mock backend as feature-complete, introducing temporary orchestration that will not reach the final architecture, keeping manual and real paths coexisting as a transition, submitting half-baked work justified by "we'll wire up real capability later".
7. **No "minimum viable / shortest path" solutions.** During solution design, forbidden to cut requirements with "let's just do MVP", "take the shortest path", or "good enough". The proposal must directly target the final form of the goal. When you catch yourself producing "trimmed / simplified / POC version" code, stop and return to the complete proposal. This kind of cutting only produces garbage.
8. **No mid-flight checks during Exec Plan execution.** During Exec Plan execution, forbidden to do phase-by-phase or step-by-step acceptance, forbidden to run lint / test / typecheck / build as "phase passes" criteria before the entire Plan is done. Mid-flight checks trick the LLM into producing placeholder code, empty implementations, temporary mocks etc. as garbage intermediate states to pass checks. Acceptance happens only once, after all code in the Plan is written, against the "Pre-delivery Self-review" checklist.
9. **No code written just to pass checks.** Only write code the final product actually needs. Forbidden to add, in order to make lint / test / typecheck pass: placeholder implementations, empty function bodies, `@ts-ignore` / `eslint-disable`, branches that will never be called, try-catch added only to suppress errors, tests written only to bump coverage. If a check failure's root cause is a design problem, go back and fix the design — don't paper over at the code layer.
10. **No silent decisions.** Any Design Doc / Exec Plan / non-trivial change must contain a `## Decisions Made Without Asking` section listing: (a) decisions I made without asking you; (b) what alternatives existed for each; (c) whether I chose this because "most convenient / smallest change" or "right abstraction". If any rationale is the former, stop and ask, do not proceed. Forbidden to bury decisions in implementation code and let the user discover them via diff. Agents lack calibrated uncertainty (they don't know what they don't know), so you cannot rely on "I'll ask when I feel uncertain"; you must use forced enumeration to make implicit choices explicit.
11. **No minimum-diff thinking.** Rule #7 bans "MVP" at the feature granularity; this rule extends it to single-file / single-function / single-interface granularity. Before implementing any change, answer: "is this the smallest-diff approach, or the right-abstraction approach?" If they differ, you must choose the latter and explain why the former is wrong. When you catch yourself producing code like "just change two lines and it works", "add a parameter to bypass it", "reuse a semantically-mismatched existing function to avoid creating a new file" — stop immediately. "Small diff = small risk" is an illusion; "small diff = design got bypassed" is the norm.
12. **Force enumeration of alternatives.** Any non-trivial technical decision (proposal choice in a Design Doc, implementation path in an Exec Plan, single-point choices for data structure / API shape / abstraction level / module boundary etc.) must, before implementation, list at least 2 approaches and write down "why rejected" for the rejected one. Even if one is obviously better, you must write it. The goal is not to produce a comparison conclusion — it is to expose the model's default prior for review. When you don't compare, the model just walks the prior, and the prior is usually minimum-diff.

> Violating any of the above = failure. Better to ask one more question than to skip documentation.

---

## Repository Knowledge Map

> Give the agent a map, not a 1000-page manual. Read the map first, dive deeper as needed.

### Architecture & Quality

- **[ARCHITECTURE.md](ARCHITECTURE.md)** — Architecture map: module structure, layering rules, dependency directions, cross-cutting concerns
- **[docs/STATE.md](docs/STATE.md)** — Application state snapshot: deployment, infrastructure, known limitations (**must-read for new sessions to avoid wrong assumptions**)
- **[docs/DECISIONS.md](docs/DECISIONS.md)** — Decision log: key decisions and trade-offs from all completed plans (must-read for new sessions)
- **[docs/QUALITY_SCORE.md](docs/QUALITY_SCORE.md)** — Quality scores: rating and known gaps per module
- **[docs/TESTING.md](docs/TESTING.md)** — Testing strategy

### Product Knowledge

- **[docs/product-specs/knowledge-base.md](docs/product-specs/knowledge-base.md)** — Core feature descriptions, key file paths, data model
- **[docs/product-specs/glossary.md](docs/product-specs/glossary.md)** — Canonical terms and definitions used across the project
- **[docs/product-specs/product-roadmap.md](docs/product-specs/product-roadmap.md)** — Product roadmap

### Design Documents

- **[docs/design-docs/index.md](docs/design-docs/index.md)** — Design document index (technical proposals & architecture decisions)

### Execution Plans

- **[docs/exec-plans/index.md](docs/exec-plans/index.md)** — Execution plan index (active/completed plans, priority overview)
- **[docs/exec-plans/tech-debt.md](docs/exec-plans/tech-debt.md)** — Centralized tech debt tracking

### Document Templates

- **[docs/templates/exec-plan.md](docs/templates/exec-plan.md)** — Must use this template when creating new execution plans
- **[docs/templates/design-doc.md](docs/templates/design-doc.md)** — Must use this template when creating new design documents

### References

- **[docs/references/](docs/references/)** — External guides, configuration docs, reference articles

---

## Common Commands

<!-- CUSTOMIZE: Fill in your project's common commands -->

```bash
# Development
# <your dev command>

# Code Quality
# <your lint/format command>
# <your ci command>

# Testing
# <your test commands>
```

## Tech Stack

<!-- CUSTOMIZE: Describe your tech stack here -->

## Coding Rules

<!-- CUSTOMIZE: Define your project-specific coding rules here -->

## Testing

<!-- CUSTOMIZE: Define your project-specific testing rules and conventions here -->

Detailed testing strategy: [docs/TESTING.md](docs/TESTING.md)

### TDD Discipline (Agent-enforced)

For any task involving core business logic, follow Red → Green → Refactor:

1. **Write tests first**: Generate test cases based on the Design Doc's behavioral contract and edge case catalog
2. **Confirm red**: Run tests, confirm all fail. If any test passes unexpectedly, the test is wrong — fix the test first
3. **Minimal implementation**: Write the minimum code to make tests pass one by one
4. **Refactor**: Once all tests pass, refactor with the test suite as your safety net

<!-- CUSTOMIZE: Define which scenarios are exempt from strict TDD -->

### Test-to-Spec Traceability

Test file headers must reference the associated spec source, ensuring every test is traceable to a specific spec entry:

```
/**
 * @spec docs/design-docs/xxx.md — P1, P3, B1, B2
 */
```

## Development Workflow

### Document-Driven Principle (Mandatory)

> ⛔ This is not a suggestion — it is a hard requirement. Skipping documentation steps = task failure.

> Knowledge the agent can't see doesn't exist. All decisions, proposals, and context must live in `docs/`, not in conversation or memory.

**Before starting a task — read docs first:** Check the "Repository Knowledge Map" above, find and read relevant docs before starting work.

**After completing a task — must update docs (see Doc Sync Matrix below).**

#### Doc Sync Matrix

> Use this table to determine which docs need updating. When filling the Exec Plan's "Docs Impact" section, reference this matrix.

| Trigger Event | Must check / update |
|---|---|
| **Exec Plan completed** | [STATE.md](docs/STATE.md), [DECISIONS.md](docs/DECISIONS.md), [exec-plans/index.md](docs/exec-plans/index.md) (move to `completed/`), [knowledge-base.md](docs/product-specs/knowledge-base.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| **Design Doc adopted** | [DECISIONS.md](docs/DECISIONS.md) (record adoption decision), [ARCHITECTURE.md](ARCHITECTURE.md) (if architecture changes) |
| **Product feature added/changed** | [knowledge-base.md](docs/product-specs/knowledge-base.md), [STATE.md](docs/STATE.md) (Feature Status) |
| **Architecture/layering changed** | [ARCHITECTURE.md](ARCHITECTURE.md) |
| **Technical decision made (in conversation, design doc, or plan)** | [DECISIONS.md](docs/DECISIONS.md) — decisions are not limited to plan completion; any meaningful trade-off or choice must be recorded |
| **New infrastructure/dependency introduced** | [STATE.md](docs/STATE.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| **New design proposal** | Create doc in `docs/design-docs/` (use [template](docs/templates/design-doc.md)), update [index.md](docs/design-docs/index.md) |
| **New execution plan** | Create doc in `docs/exec-plans/active/` (use [template](docs/templates/exec-plan.md)), update [index.md](docs/exec-plans/index.md) |
| **New tech debt discovered** | [tech-debt.md](docs/exec-plans/tech-debt.md) |
| **Quality score changes** | [QUALITY_SCORE.md](docs/QUALITY_SCORE.md) |

**Cross-reference rule:** When updating any document, check whether related documents also need syncing. Documents are never updated in isolation.

**Index maintenance:** After adding or moving any doc under `docs/`, you must update the corresponding `index.md` to keep the index consistent with actual files.

**When to create a Design Doc** — When any of the following apply, create one in `docs/design-docs/` (use [template](docs/templates/design-doc.md)):

- Adding a new module or subsystem
- Cross-module refactoring or changing dependency directions
- Introducing a new external dependency or technology choice
- 2+ viable approaches that need comparison

**When to create an Exec Plan** — When any of the following apply, create one in `docs/exec-plans/active/` (use [template](docs/templates/exec-plan.md)):

- Expected to modify ≥ 3 modules/directories
- Involves database migrations or irreversible changes
- Implementation steps have explicit ordering dependencies

**Document Naming Conventions:**

| Document Type | Format                              | Location                      | Example            |
| ------------- | ----------------------------------- | ----------------------------- | ------------------ |
| Design Doc    | `D{序号}-{kebab-case-描述}.md`       | `docs/design-docs/`           | `D1-auth-flow.md`  |
| Exec Plan     | `E{序号}-{kebab-case-描述}.md`       | `docs/exec-plans/active/`     | `E1-db-migration.md` |

- **序号**必须递增，从对应 `index.md` 表格中获取下一个可用编号
- **描述**使用 kebab-case（小写英文，单词间用 `-` 连接），简短概括主题
- Exec Plan 完成后，文件从 `active/` 移至 `completed/`，文件名不变

**No doc needed:** Single-file bug fixes, style tweaks, copy changes, and other localized modifications.

### Self-Rationalization Check (Agent self-check)

> When you catch yourself thinking any of the following, **stop** and follow the process.

| If you're thinking...                                   | The reality is...                                                                          |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| "This change is simple, no need for the full process"   | Simple changes are where assumptions break most easily. The short process runs fast        |
| "I already know how it works"                           | You know how you _think_ it works. Verify with evidence                                    |
| "TDD is too heavy for this fix"                         | Simple code breaks too. A test takes only 30 seconds                                       |
| "I'll add docs later"                                   | Later never comes. Write them now                                                          |
| "This time is different"                                | Every time is different, but the process always applies                                    |
| "Let me code first to confirm it works, then add tests" | Tests first = "what should happen"; tests after = "what happened". Fundamentally different |
| "This decision is obvious, no need to list alternatives"            | "Obvious" means your prior is strong, not that the option space is small. Rule #12 requires enumeration precisely so your prior can be reviewed |
| "Just change these two lines and it'll work, no need to touch other code" | This is minimum-diff thinking (rule #11). Ask "is the abstraction right" first, then "how big is the diff" — order matters |
| "This choice isn't important, not worth asking"                      | Importance is the user's call, not the agent's. Per rule #10, list it in Decisions Made Without Asking and let the user decide |

### Pre-delivery Self-review (Mandatory)

After code is written and CI passes, the agent must run the following checklist and show results to the user:

**Spec Alignment Check:**

- [ ] Every postcondition in the behavioral contract has a corresponding test
- [ ] Every scenario in the edge case catalog has a corresponding test
- [ ] Are there behaviors in the implementation not described in the spec? (If so, add to spec or remove implementation)

**Test Quality Check:**

- [ ] Any tautological tests (tests that just repeat implementation logic)?
- [ ] Over-mocking (mocking away core logic that should be tested)?
- [ ] Testing only happy paths while ignoring error paths?

**Implementation Quality Check:**

- [ ] Any placeholder comments (TODO / FIXME / HACK) left unhandled?
- [ ] Error handling using generic catch-all instead of specific error types?
- [ ] Any implicit external state dependencies (should be passed as parameters)?
- [ ] Does the implementation follow ARCHITECTURE.md layering rules?

**Security Check:**

- [ ] User input validated at the boundary?
- [ ] Operations verify caller permissions where applicable?
- [ ] Any sensitive information that could leak to unauthorized contexts?

**Doc Sync Check (show diff or summary of each updated doc as evidence):**

- [ ] Does this change complete an Exec Plan? → Updated STATE.md, DECISIONS.md, index.md, moved plan to `completed/`
- [ ] Does this change alter architecture or layering? → Updated ARCHITECTURE.md
- [ ] Does this change add/modify a product feature? → Updated knowledge-base.md, STATE.md (Feature Status)
- [ ] Were any technical decisions or trade-offs made during this task (in conversation, design, or implementation)? → Recorded in DECISIONS.md
- [ ] Do the updated documents have cross-references that need syncing? → Verified consistency
- [ ] **Evidence**: List each doc updated and a one-line summary of the change (do NOT just check boxes)

### Task Completion Criteria

A development task is considered "complete" only when ALL of the following are met:

1. ✅ CI checks all pass
2. ✅ Self-review checklist all checked (no remaining items, or reasons noted)
3. ✅ Affected docs updated
4. ✅ New/modified code is traceable to a spec (specific entry in Design Doc or Exec Plan)
5. ✅ Self-review results summary shown to the user

## Git Workflow

- **Never commit directly to the main branch** — verify current branch with `git branch` before committing
- Merge via feature branch + PR. Naming: `feat/xxx`, `fix/xxx`, `refactor/xxx`, `test/xxx`
- **Never run `git checkout -- .`, `git checkout <branch> -- .`, or `git restore .` with uncommitted changes in the working tree** — these irreversibly drop working-tree changes. To verify an older code state, use `git worktree` or a new branch — do not touch the current working tree.
- **Prefix any git command that opens an editor with `GIT_EDITOR=true`** (non-interactive environments hang the command otherwise, causing timeouts / aborted runs). Common cases:
  - `git rebase --continue` / `git rebase -i` → `GIT_EDITOR=true git rebase --continue`
  - `git commit --amend` (without `-m`) → add `-m "..."` or `--no-edit`
  - `git merge` (with merge commit and no `-m`) → add `--no-edit` or `-m "..."`
  - `git tag -a` / `git revert` (without `-m`) → add `-m "..."`
