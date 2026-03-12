# Bootstrap: Set Up Agentic Docs for an Existing Project

> **Version**: 1.0.0
> **This file is an AI agent prompt.** Do not read it as documentation.
> Copy the content below to your AI coding agent (Claude Code, Cursor, etc.) or instruct it to read this file directly.

## Usage

```bash
# Option 1 (recommended): Download and run locally
curl -sO https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md
claude "Read bootstrap.md and follow the instructions to set up agentic docs for this project."
# rm bootstrap.md  # clean up after done

# Option 2: Let the agent read from URL directly (requires network access)
# NOTE: Update the URL below if the repo is renamed or the default branch changes.
claude "Read https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md and follow the instructions to set up agentic docs for this project."
```

---

## Agent Instructions

You are about to set up a document-driven development framework for an existing project. This framework gives AI coding agents (including yourself) structured rules, documentation templates, and workflows to follow.

**Your mission**: Analyze this project thoroughly, then generate a complete set of documentation files — pre-filled with real content based on what you discover, NOT empty templates with placeholder comments.

Follow the phases below **in order**. Do NOT skip any phase. Do NOT start generating files until you have completed the analysis and received user confirmation.

---

### Phase 1: Project Analysis

Scan the project systematically. Items are marked by priority:

- 🔴 **Must** — always gather this information
- 🟡 **Best effort** — gather if discoverable, don't spend excessive effort

> **Large project guidance**: For projects with >100 source files or monorepo structures, focus on entry points, configuration files, and top-level directory structure. Do NOT try to read every source file — analyze the main modules and infer the rest from patterns.

#### 1.1 Project Identity 🔴

- Project name and description (from README, package manifest, or repo metadata)
- Primary programming language(s)
- Package manager (npm/yarn/pnpm/pip/uv/poetry/cargo/go modules/etc.)

#### 1.2 Tech Stack 🔴

- Runtime environment (Node.js, Python, Go, Rust, JVM, etc.)
- Framework(s) (Next.js, FastAPI, Gin, Actix, Spring, etc.)
- Database(s) and ORM(s)
- Authentication mechanism
- External services / APIs
- Build tool(s) (webpack, vite, turbopack, esbuild, etc.)

#### 1.3 Project Structure 🔴

- Top-level directory layout
- Source code organization pattern (by feature, by layer, monorepo, etc.)
- Key entry points (main files, route definitions, etc.)
- Configuration file locations

#### 1.4 Development Workflow 🔴

- Dev server command
- Build command
- Lint / format commands (and tools: ESLint, Prettier, Ruff, Black, etc.)
- CI pipeline (GitHub Actions, etc.) — read workflow files if present
- Deployment method (if discoverable)

#### 1.5 Testing 🔴

- Test framework(s) (Jest, Vitest, pytest, go test, etc.)
- Test directory structure
- Test run commands
- Existing coverage configuration

#### 1.6 Architecture Analysis 🔴

This is the most important part. Analyze the source code to understand:

- **Module/layer boundaries** — What are the major modules or layers? How is the code organized?
- **Dependency directions** — Which modules depend on which? Are there clear layering rules?
- **Cross-cutting concerns** — How are auth, error handling, logging, validation handled?
- **Data flow** — How does a request/action flow through the system?
- **Key conventions** — Naming patterns, file organization patterns, import conventions

#### 1.7 Existing Documentation 🔴

- Does the project already have an `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or similar agent instruction file?
- Is there existing documentation in `docs/` or elsewhere?
- Are there README files in subdirectories?

**Important**: If agent instruction files already exist, read them carefully. The generated `AGENTS.md` should preserve any project-specific rules and conventions from those files.

#### 1.8 Deployment & Infrastructure 🟡

- Hosting platform
- Infrastructure configuration (Docker, Terraform, etc.)
- Environment management
- Monitoring / logging services

---

### Phase 2: Present Analysis Results

After completing the analysis, present a **structured summary** to the user with all findings. Clearly separate your findings into two categories:

- **✅ Confirmed** — information you found concrete evidence for in the code
- **❓ Needs your input** — information you couldn't determine from code alone (e.g., deployment platform, roadmap priorities, certain architectural intentions)

Format the summary clearly under the Phase 1 categories. For each "Needs your input" item, explain what you looked for and why you couldn't determine it, so the user knows exactly what to fill in.

At the end, ask the user:

> I've completed my analysis of your project. Here's what I found: [summary]
>
> **Items that need your input** are marked with ❓. Please:
> 1. Review the confirmed findings — is anything incorrect?
> 2. Fill in or clarify the ❓ items as much as you can
> 3. Are there any architectural rules or conventions I didn't pick up from the code?
> 4. Are there any specific coding rules you want enforced?

**Wait for user confirmation before proceeding to Phase 3.**
- If the user says "LGTM", "looks good", or similar — proceed directly to Phase 3.
- If the user provides partial corrections — update your analysis accordingly and proceed. No need to re-present the full summary.

---

### Phase 3: Generate Documentation Files

#### Pre-generation: Conflict Resolution

**Before writing any file**, check if it already exists in the project:

- **If `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or similar agent instruction file exists**: Read it carefully. Merge any project-specific rules into the new `AGENTS.md`. Do NOT discard existing rules — integrate them into the appropriate sections.
- **If `ARCHITECTURE.md` exists**: Read it. Use its content to enrich your generated version. Preserve any information that isn't captured by your analysis.
- **If `docs/` directory exists**: Check each file. If a file already has real content (not just placeholders), preserve that content and merge it into the new structure.
- **For any other conflicting file**: Ask the user how to handle it before overwriting.

#### Generation Rules

Create all files listed below. **Every file must contain real, project-specific content** — not placeholder comments or `<!-- CUSTOMIZE -->` markers.

- If a section genuinely doesn't apply to this project, write "N/A — [brief reason]" instead of leaving it empty.
- If a command or tool was not found during analysis (e.g., no linter configured, no test framework), **omit that entry entirely** rather than leaving a placeholder. Only include what actually exists.
- If the user explicitly stated in Phase 2 that a certain document type doesn't apply (e.g., a library project doesn't need `product-roadmap.md` or `STATE.md` deployment sections), **skip that file entirely**.
- **Keep files concise.** `knowledge-base.md`: each feature description ≤ 5 lines. `ARCHITECTURE.md`: aim for ≤ 200 lines total. Other docs: proportional to actual project complexity — don't pad.
- **Common Commands in `AGENTS.md`**: only list commands actually found. If an entire category (e.g., Testing) has no commands, omit that category. Never write placeholder text. Example of a properly filled section:
  ```bash
  # Development
  pnpm dev

  # Code Quality
  pnpm lint && pnpm format

  # Testing
  pnpm test
  ```

#### File Generation Order

Generate files in this exact order (dependencies flow top-down):

1. `docs/` directory structure (empty dirs with `.gitkeep`)
2. `docs/templates/design-doc.md`
3. `docs/templates/exec-plan.md`
4. `docs/product-specs/glossary.md`
5. `docs/product-specs/knowledge-base.md`
6. `docs/product-specs/product-roadmap.md`
7. `docs/design-docs/index.md`
8. `docs/exec-plans/index.md`
9. `docs/exec-plans/tech-debt.md`
10. `docs/DECISIONS.md`
11. `docs/QUALITY_SCORE.md`
12. `docs/TESTING.md`
13. `docs/STATE.md`
14. `ARCHITECTURE.md`
15. `AGENTS.md`
16. `scripts/check-docs.py`

---

#### 3.1 Directory Structure

Create the following directories (use `.gitkeep` for empty ones). If a directory already exists, skip it and only create missing subdirectories. Do NOT overwrite or remove existing files in existing directories.

```
docs/
├── design-docs/
├── exec-plans/
│   ├── active/
│   └── completed/
├── product-specs/
├── references/
└── templates/
```

`docs/references/` is for storing external guides, configuration references, and third-party documentation relevant to the project. If you discovered any notable external references during analysis (e.g., framework docs, API specs, style guides), create short markdown files linking to them. Otherwise, leave the directory with just `.gitkeep`.

---

#### 3.2 Template Files

These two files are used as-is (they are generic templates, not project-specific):

**`docs/templates/design-doc.md`**:

````markdown
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

## Acceptance Criteria

[How to determine success? Each criterion should map to a behavioral contract postcondition or edge case above]

1. [ ] [Criterion 1 — maps to P1]
2. [ ] [Criterion 2 — maps to B1, B2]
3. [ ] ...
````

**`docs/templates/exec-plan.md`**:

````markdown
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

## Verification Metrics

[How do we measure success? List quantifiable metrics]

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
````

---

#### 3.3 Product Specs

**`docs/product-specs/glossary.md`** — Fill in with actual domain terms discovered from the codebase (model names, key concepts, business entities). Format:

```markdown
# Glossary

> Canonical terms used across this project. All agents should use these terms consistently.
>
> **Last updated**: [today's date]

---

## Entries

- **[Term]**: [Definition based on how it's used in the code]
```

**`docs/product-specs/knowledge-base.md`** — Fill in with real features, real file paths, and real data models discovered from the code. Every feature should list its key files. The data model section should reflect actual database schemas, API contracts, or type definitions found in the code.

```markdown
# Knowledge Base

> Core feature descriptions, key file paths, and data model.
>
> **Last updated**: [today's date]

---

## Features

### [Feature Name]
- **Description**: [What it does — based on code analysis]
- **Key files**: `path/to/feature/`
- **Status**: Active

## Data Model

[Actual schemas, types, or data structures found in the project]

## Key File Paths

| Purpose | Path |
|---------|------|
| [Real purpose] | `real/path/` |
```

**`docs/product-specs/product-roadmap.md`** — If you can infer current focus from recent commits, open issues, or TODO comments, fill that in. Otherwise, write a brief "Current Focus" based on the project's apparent state and leave "Upcoming" and "Future Ideas" with a note that the user should fill these in.

---

#### 3.4 Index Files

**`docs/design-docs/index.md`** — Generate with the standard structure but empty table (no design docs exist yet):

```markdown
# Design Document Index

> Directory of technical proposals and architecture decisions.
>
> **Last updated**: [today's date]

---

## Documents

| ID | Document | Domain | Summary |
| -- | -------- | ------ | ------- |
```

**`docs/exec-plans/index.md`** — Same, empty table:

```markdown
# Execution Plan Index

> The agent checks here to understand all plan statuses and priorities.
>
> **Last updated**: [today's date]

---

## Active Plans

| ID | Priority | Plan | Status | Summary |
| -- | -------- | ---- | ------ | ------- |

---

## Completed Plans

| ID | Plan | Completed | Summary |
| -- | ---- | --------- | ------- |

---

## Related

- **[Tech Debt Tracking](tech-debt.md)** — Known tech debt and repayment priorities
```

---

#### 3.5 Tech Debt

**`docs/exec-plans/tech-debt.md`** — If you discovered any tech debt during analysis (TODO/FIXME comments, known issues, outdated dependencies, missing tests), list them here. Otherwise, generate the structure with an empty table.

```markdown
# Tech Debt Tracking

> Centralized record of known tech debt. Review and repay periodically.
> Priority: 🔴 High (blocks development) | 🟡 Medium (affects quality) | 🟢 Low (nice to improve)
>
> **Last updated**: [today's date]

---

## Active Tech Debt

| # | Priority | Domain | Description | Impact | Link | Created |
| - | -------- | ------ | ----------- | ------ | ---- | ------- |

---

## Resolved Tech Debt

| # | Domain | Description | Resolved | Resolution | Link |
| - | ------ | ----------- | -------- | ---------- | ---- |
```

---

#### 3.6 Project State Documents

**`docs/DECISIONS.md`** — Generate structure with empty records (no completed plans yet):

```markdown
# Decision Log

> Agent should read this file at the start of each new session to quickly understand historical decision context.
>
> **Last updated**: [today's date]

---

## Decision Records

<!-- Add one entry per completed Exec Plan. Format:

### E[N] — [Plan Title] (YYYY-MM-DD)
- **What changed**: [One sentence]
- **Why**: [Driving force]
- **Key trade-offs**: [What was traded off, or "None"]
- **Not done / Remaining**: [Explicitly out-of-scope items, or "None"]
- **Details**: [Link to completed Exec Plan]

-->
```

**`docs/QUALITY_SCORE.md`** — Fill in with actual modules/areas discovered from the project. Give your best honest assessment of each area's quality based on what you observed (test coverage, code organization, documentation, type safety, etc.).

```markdown
# Quality Score

> Quality rating per module. Helps the agent judge which areas need extra care.
> Rating scale: A (Excellent) | B (Good) | C (Needs Improvement) | D (Problematic)
>
> **Last updated**: [today's date]

---

## Module Scores

| Module | Rating | Known Gaps |
| ------ | ------ | ---------- |
| [Real module name] | [Honest rating] | [Real gaps observed] |
```

**`docs/TESTING.md`** — Fill in with the actual test framework, directory structure, commands, and conventions found in the project. If testing is absent or minimal, note that honestly.

```markdown
# Testing Strategy

> **Last updated**: [today's date]

---

## Overview

[Actual testing approach based on what exists in the project]

## Test Categories

[What types of tests actually exist]

## Directory Structure

[Where tests actually live]

## Commands

[Actual test commands]

## Guidelines

[Conventions observed in existing tests]

## Coverage Goals

[Existing coverage config, or recommended goals if none exist]
```

**`docs/STATE.md`** — Fill in with real deployment/infrastructure information if discoverable. Include actual feature status based on the codebase.

```markdown
# Application State

> Snapshot of the application's current real state.
> Agent should read this at the start of each new session to avoid wrong assumptions.
>
> **Last updated**: [today's date]

---

## Deployment & Runtime

| Item | Current State |
| ---- | ------------- |
| **Platform** | [Real platform or "Unknown — user to fill in"] |
| **Runtime** | [Detected runtime] |
| **Output mode** | [If discoverable] |

---

## Key Infrastructure

| Service | Provider | Purpose |
| ------- | -------- | ------- |
| [Fill from analysis] |

---

## Known Production Limitations

| Limitation | Impact | Reference |
| ---------- | ------ | --------- |

---

## Current Feature Status

### Core Features (Live)

- ✅ [Real features discovered]

### Active Tech Debt

See [tech-debt.md](exec-plans/tech-debt.md) for details.
```

---

#### 3.7 ARCHITECTURE.md

This is one of the two most critical files. It must contain **real architectural information**, not placeholders.

Fill in based on your Phase 1 analysis:

```markdown
# Architecture

> Architecture map of the codebase. The agent should understand module structure
> and dependency rules here before diving into specific code.
>
> **Last updated**: [today's date]

---

## High-level Architecture

[Draw an ASCII diagram or describe the actual request/data flow through the system]

---

## Directory Structure & Responsibilities

[Map the ACTUAL directory structure with descriptions of what each directory does]

---

## Layering Rules

[Document the actual dependency directions you observed. Be specific:
 - Which layers can import from which
 - What is forbidden
 - Where shared utilities live]

---

## Cross-cutting Concerns

[How does THIS project handle: auth, error handling, logging, validation, etc.]

---

## Key Conventions

[Actual conventions observed: naming patterns, file organization, import style, etc.]
```

---

#### 3.8 AGENTS.md

This is the most critical file — it's the agent's operating manual. Generate it with **all sections filled in** using real project information.

The structure must follow this exact format:

````markdown
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

[Generate based on commands discovered in Phase 1 — see generation rules above]

## Tech Stack

[Actual tech stack description — language, framework, database, key libraries, etc.]

## Coding Rules

[Project-specific coding rules. Include:
 - Rules discovered from existing linter config
 - Patterns observed in the codebase
 - Any rules from existing agent instruction files
 - Language/framework-specific conventions the project follows]

## Testing

[Actual testing rules and conventions for this project]

Detailed testing strategy: [docs/TESTING.md](docs/TESTING.md)

### TDD Discipline (Agent-enforced)

For any task involving core business logic, follow Red → Green → Refactor:

1. **Write tests first**: Generate test cases based on the Design Doc's behavioral contract and edge case catalog
2. **Confirm red**: Run tests, confirm all fail. If any test passes unexpectedly, the test is wrong — fix the test first
3. **Minimal implementation**: Write the minimum code to make tests pass one by one
4. **Refactor**: Once all tests pass, refactor with the test suite as your safety net

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

| If you're thinking...                                    | The reality is...                                                                      |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| "This change is simple, no need for the full process"    | Simple changes are where assumptions break most easily. The short process runs fast     |
| "I already know how it works"                            | You know how you *think* it works. Verify with evidence                                |
| "TDD is too heavy for this fix"                          | Simple code breaks too. A test takes only 30 seconds                                   |
| "I'll add docs later"                                    | Later never comes. Write them now                                                      |
| "This time is different"                                 | Every time is different, but the process always applies                                 |
| "Let me code first to confirm it works, then add tests"  | Tests first = "what should happen"; tests after = "what happened". Fundamentally different |

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
````

---

#### 3.9 Documentation Integrity Script

**`scripts/check-docs.py`** — Create this script exactly as shown below. It validates documentation health (broken links, index coverage, exec plan structure, architecture path references). Requires Python 3.10+ with no external dependencies:

```python
#!/usr/bin/env python3
# Version: 1.0.0
# Source: https://github.com/Sukitly/agentic-docs-templates
"""
Documentation integrity checker.

Checks:
1. All relative markdown links in docs/, ARCHITECTURE.md, AGENTS.md point to existing files
2. exec-plans/index.md and design-docs/index.md cover all files in their directories
3. Exec plan structure validation (required frontmatter fields and sections)
4. ARCHITECTURE.md references existing paths
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


# ── Helpers ──────────────────────────────────────────────────────────


def strip_html_comments(content: str) -> str:
    """Remove HTML comment blocks from content."""
    return re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)


def extract_markdown_links(content: str) -> list[str]:
    """Extract relative markdown links from content, skipping external/anchor links and HTML comments."""
    content = strip_html_comments(content)
    links = []
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
        link = match.group(1)
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Strip anchor fragment and query string
        link = link.split("#")[0].split("?")[0]
        if link:
            links.append(link)
    return links


def relative(path: Path) -> str:
    """Return path relative to ROOT."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def check_links_in_file(file_path: Path) -> None:
    """Check all relative markdown links in a file point to existing targets."""
    content = file_path.read_text(encoding="utf-8")
    links = extract_markdown_links(content)
    file_dir = file_path.parent

    for link in links:
        resolved = (file_dir / link).resolve()
        if not resolved.exists():
            errors.append(
                f'Broken link in {relative(file_path)}: "{link}" → {relative(resolved)} not found'
            )


# ── Check 1: All markdown links ─────────────────────────────────────

print("📄 Checking markdown links...")

md_files = list(ROOT.glob("docs/**/*.md"))
for top_level in ["ARCHITECTURE.md", "AGENTS.md"]:
    p = ROOT / top_level
    if p.exists():
        md_files.append(p)

for f in md_files:
    check_links_in_file(f)


# ── Check 2: Index coverage ─────────────────────────────────────────

print("📋 Checking index coverage...")


def check_index_covers_dir(index_path: str, dir_path: str, label: str) -> None:
    full_index = ROOT / index_path
    full_dir = ROOT / dir_path

    if not full_index.exists():
        errors.append(f"Missing index: {index_path}")
        return
    if not full_dir.exists():
        return

    index_content = full_index.read_text(encoding="utf-8")
    md_files_in_dir = [
        f.name for f in full_dir.iterdir() if f.suffix == ".md" and f.name != "index.md"
    ]

    for file_name in md_files_in_dir:
        if (
            f"({file_name})" not in index_content
            and f"/{file_name})" not in index_content
        ):
            errors.append(f'{label}: "{file_name}" not listed in {index_path}')


check_index_covers_dir(
    "docs/exec-plans/index.md", "docs/exec-plans/active", "exec-plans/active"
)
check_index_covers_dir(
    "docs/exec-plans/index.md", "docs/exec-plans/completed", "exec-plans/completed"
)
check_index_covers_dir("docs/design-docs/index.md", "docs/design-docs", "design-docs")


# ── Check 3: Exec plan structure validation ──────────────────────────

print("📐 Checking exec-plan structure...")

REQUIRED_FRONTMATTER = ["Created", "Last updated", "Status"]
REQUIRED_FRONTMATTER_ACTIVE = ["Priority"]
REQUIRED_SECTIONS_ACTIVE = ["## Progress Log", "## Decision Log"]

for dir_name in ["docs/exec-plans/active", "docs/exec-plans/completed"]:
    full_dir = ROOT / dir_name
    if not full_dir.exists():
        continue
    is_active = "active" in dir_name
    for f in full_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8")
        file_name = relative(f)

        for field in REQUIRED_FRONTMATTER:
            if f"**{field}**" not in content:
                errors.append(
                    f'{file_name}: missing required frontmatter field "{field}"'
                )

        if is_active:
            for field in REQUIRED_FRONTMATTER_ACTIVE:
                if f"**{field}**" not in content:
                    errors.append(
                        f'{file_name}: missing required frontmatter field "{field}"'
                    )
            for section in REQUIRED_SECTIONS_ACTIVE:
                if section not in content:
                    errors.append(f'{file_name}: missing required section "{section}"')


# ── Check 4: ARCHITECTURE.md path references ────────────────────────

print("🏗️  Checking ARCHITECTURE.md path references...")

arch_file = ROOT / "ARCHITECTURE.md"
if arch_file.exists():
    arch_content = arch_file.read_text(encoding="utf-8")
    # Extract backtick-quoted paths (e.g., `src/server/`, `lib/utils.ts`)
    for match in re.finditer(r"`([a-zA-Z][a-zA-Z0-9_\-./]+/?)`", arch_content):
        path_ref = match.group(1)
        # Only check paths that look like file/directory references (contain /)
        if "/" not in path_ref:
            continue
        # Skip if inside a <!-- CUSTOMIZE --> comment block or example
        if path_ref.startswith("#"):
            continue
        full_path = ROOT / path_ref.rstrip("/")
        if not full_path.exists():
            errors.append(f'ARCHITECTURE.md references non-existent path: "{path_ref}"')


# ── Results ──────────────────────────────────────────────────────────

print()
if errors:
    print(f"❌ Found {len(errors)} documentation issue(s):\n", file=sys.stderr)
    for error in errors:
        print(f"  • {error}", file=sys.stderr)
    sys.exit(1)
else:
    print("✅ All documentation checks passed.")
```

---

### Phase 4: Verification & Wrap-up

After generating all files:

1. Update `.gitignore` — read the existing file first, then append only entries that are not already present:
   ```
   .DS_Store
   *.swp
   *.swo
   *~
   ```
2. Run the documentation integrity checker:
   ```bash
   python3 scripts/check-docs.py
   ```
3. Fix any issues it reports.
4. Present a **summary of all generated files** to the user (list skipped files too, with reasons).
5. Provide **next steps** guidance:
   - **Claude Code** users: `AGENTS.md` in the project root is automatically picked up. No extra config needed.
   - **Cursor** users: consider copying relevant rules from `AGENTS.md` into `.cursorrules` or Cursor's project settings.
   - **GitHub Copilot** users: consider copying relevant rules into `.github/copilot-instructions.md`.
   - **Other agents**: check the agent's documentation for how to point it at `AGENTS.md`.
   - Remind the user to review and refine the generated docs, especially `AGENTS.md` coding rules and `ARCHITECTURE.md` layering rules.
   - Note that `scripts/check-docs.py` has a version number and source URL in its header — periodically check the source repo for updates.

---

## Important Reminders

- **Be honest, not optimistic.** If the project has gaps (no tests, unclear architecture, missing docs), say so clearly in the generated files. The whole point is to give the agent an accurate picture.
- **Use today's date** for all "Last updated" fields.
- **Use real paths** in ARCHITECTURE.md and knowledge-base.md. Every backtick-quoted path must point to a file or directory that actually exists.
- **Preserve existing work.** If the project already has documentation, tests, or conventions, incorporate them — don't replace them.
