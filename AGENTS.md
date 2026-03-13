# AGENTS.md

## ⛔ Hard Rules (Must follow on every task, no exceptions)

1. **STOP — Do NOT write code directly.** After receiving any development task, the first step is to read the relevant docs from the "Repository Knowledge Map" below to understand existing architecture and context.
2. **Docs before code.** If a task requires a Design Doc or Exec Plan (see criteria below), you must **create it and get user confirmation first** before writing any code.
3. **Plan before execute.** Present what files you plan to change, why, and how. **Wait for explicit user approval** before making changes.
4. **Self-review + update docs after completion.** After code changes, you must run the "Pre-delivery Self-review" checklist and show results, then update all affected docs (see "Development Workflow" section). Skipping either step means the task is incomplete.
5. **Tests first.** When working on core business logic, you must write tests first, confirm they fail, then write the implementation (see "TDD Discipline" section).

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

**After completing a task — must update docs:**

- **Product feature changes** → Update [knowledge-base.md](docs/product-specs/knowledge-base.md) (feature descriptions, key file paths, data model)
- **Architecture/layering changes** → Update [ARCHITECTURE.md](ARCHITECTURE.md)
- **New design proposals** → Create new doc in `docs/design-docs/` (use [template](docs/templates/design-doc.md)), update [index.md](docs/design-docs/index.md)
- **New execution plans** → Create new doc in `docs/exec-plans/active/` (use [template](docs/templates/exec-plan.md)), update [index.md](docs/exec-plans/index.md)
- **Plan completed** → Move doc from `active/` to `completed/`, update [index.md](docs/exec-plans/index.md), append decision record to [DECISIONS.md](docs/DECISIONS.md), and update affected entries in [STATE.md](docs/STATE.md)
- **New tech debt discovered** → Record in [tech-debt.md](docs/exec-plans/tech-debt.md)
- **Quality score changes** → Update [QUALITY_SCORE.md](docs/QUALITY_SCORE.md)

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
