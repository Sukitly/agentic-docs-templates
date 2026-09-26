# Bootstrap: Set Up Agentic Docs for an Existing Project

> **Version**: 2.3.0
> **This file is an AI agent prompt.** Do not read it as documentation.
> Copy the content below to your AI coding agent or instruct the agent to read this file directly.

## Usage

```bash
# Option 1 (recommended): Download and run locally
curl -sO https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md
claude "Read bootstrap.md and follow the instructions to set up agentic docs for this project."
# rm bootstrap.md  # clean up after done

# Option 2: Let the agent read from URL directly
claude "Read https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md and follow the instructions to set up agentic docs for this project."
```

---

## Agent Instructions

You are setting up a document-driven development framework for an existing project. The framework gives AI coding agents structured rules, documentation templates, and workflows.

**Mission**: analyze the project, copy this template's structure, then fill every customizable file with real project-specific content.

Follow the phases in order. Do not skip phases.

---

## Phase 1: Project Analysis

Scan the project systematically.

> Large project guidance: for projects with more than 100 source files or monorepos, focus on entry points, configuration files, top-level module boundaries, and representative modules. Do not read every file.

### 1.1 Project Identity

- Project name and description
- Primary programming languages
- Package manager / build system
- Repository type: application, library, monorepo, infrastructure, content, etc.

### 1.2 Tech Stack

- Runtime environment
- Frameworks
- Database and data access layer
- Authentication and authorization
- External services / APIs
- Build tools
- Deployment platform if discoverable

### 1.3 Project Structure

- Top-level directory layout
- Source organization pattern
- Key entry points
- Configuration files
- Generated code / migration directories / public assets

### 1.4 Development Workflow

- Dev server command
- Build command
- Lint / format commands
- Test commands
- CI workflows
- Deployment workflow

### 1.5 Testing

- Test framework(s)
- Test directory structure
- Unit / integration / E2E boundaries
- Coverage or quality gate configuration
- External dependency fake/mocking strategy

### 1.6 Architecture Analysis

Identify:

- Module/layer boundaries
- Dependency directions
- Request/action/data flow
- Cross-cutting concerns: auth, validation, errors, logging, metrics, i18n
- Naming and import conventions
- Known anti-patterns or risky seams

### 1.7 Existing Documentation

Read existing agent instructions and docs:

- `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`, etc.
- `docs/` and subdirectory READMEs
- ADRs, RFCs, design docs, product docs, deployment docs, testing docs

Preserve project-specific rules by integrating them into the generated docs.

### 1.8 Deployment & Infrastructure

Best-effort discovery:

- Hosting platform(s)
- DNS/custom domains
- Secrets/environment management
- Infrastructure-as-code
- Monitoring/logging/analytics
- Operational runbooks

---

## Phase 2: Present Analysis Results

Present a concise structured summary with two sections:

- **Confirmed** — facts supported by code/config/docs
- **Needs input** — items not discoverable from the repository

Ask the user to review:

1. Are confirmed findings incorrect?
2. Can the user fill or clarify the unknowns?
3. Are there architectural rules or conventions the repository does not reveal?
4. Are there coding/testing/deployment rules the user wants enforced?

Wait for user confirmation before Phase 3.

---

## Phase 3: Copy Template & Generate Files

### 3.1 Obtain the Template

If this `bootstrap.md` is not already inside the template checkout, clone the template repository:

```bash
git clone --depth 1 https://github.com/Sukitly/agentic-docs-templates.git /tmp/agentic-docs-templates
```

Read the template files before writing. The template structure is the source of truth.

### 3.2 Conflict Resolution & Documentation Migration

Be decisive. The project is under version control; duplicate authoritative docs are worse than migrated docs.

**Agent instruction files**

- If an agent instruction file exists, read it carefully.
- Merge project-specific rules into the new `AGENTS.md`.
- Delete superseded old instruction files unless the file is required by a different tool (`.cursorrules`, `.github/copilot-instructions.md`, etc.).

**Existing docs — migrate, do not duplicate**

Classify and migrate docs:

| Existing doc type | Destination |
|---|---|
| Architecture/system design | `ARCHITECTURE.md` |
| Runtime/infrastructure state, known limitations | `docs/STATE.md` |
| Deployment operations, environment configuration, smoke tests, rollback | `docs/DEPLOYMENT.md` |
| Feature specs, PRDs, user-visible capabilities, data model docs | `docs/product-specs/knowledge-base.md` |
| Glossary/terminology | `docs/product-specs/glossary.md` |
| Testing docs | `docs/TESTING.md` |
| ADRs/RFCs/technical proposals | `docs/design-docs/` and `docs/design-docs/index.md`; mark shipped ones `Implemented` with a `Body fingerprint`, and unshipped ones `Draft` or `Deferred` |
| Multi-step implementation plans | `docs/exec-plans/active/` or `docs/exec-plans/completed/` and `docs/exec-plans/index.md` |
| Technical debt with repayment path | `docs/TECH_DEBT.md` |
| Product gaps/deferred decisions/ops follow-ups | `docs/BACKLOG.md` |
| External references/API docs/guides | `docs/references/` |
| Documents that have completed their purpose but retain historical value | `docs/archive/`; record the original location and archive reason |

After migrating content, delete the superseded original file. Do not keep two docs with the same authority. Delete obsolete content with no historical value; archive documents are read-only and must not serve as current authority.

Do not modify or delete the root `README.md` unless it contains stale links to moved docs.

### 3.3 Generation Rules

1. Copy the template files to the project at the same relative paths.
2. Replace every `<!-- CUSTOMIZE: ... -->` comment with real project-specific content.
3. Keep fixed framework sections in `AGENTS.md` intact unless the user explicitly asked to customize the framework itself.
4. If a section does not apply, write `N/A — [brief reason]`.
5. Omit commands that do not exist instead of writing placeholders.
6. Keep docs concise and factual.
7. Write each fact into exactly one owning document (Fact Ownership in `AGENTS.md`); other documents only link to it. `STATE.md` holds only runtime, infrastructure, and known limitations; `knowledge-base.md` holds only user-visible capabilities, without interaction micro-details or implementation parameters. Each entry is no more than five lines (roughly 300 words) and retains only the current conclusion, authoritative document, and key paths.
8. Keep each `DECISIONS.md` entry to no more than 15 lines and retain only decisions that still constrain future work. Delete expired decisions; archive them only when they retain historical research value.
9. Keep only active entries with no other carrier in `TECH_DEBT.md` and `BACKLOG.md`, and confirm migrated entries with the user in Phase 2. Delete entries that are repaid, started, abandoned, invalidated, or superseded; do not create completed tables or duplicate active Exec Plan tracking.
10. Durable documents do not track whether a specific migration is pending or applied; transient execution state belongs in the deployment system or an active Exec Plan.
11. Documents carry no `Last updated` dates; history belongs in git.
12. Use real paths in `ARCHITECTURE.md` and `knowledge-base.md`; every backtick-quoted path that looks local should exist.

### 3.4 Required Structure

Create missing directories:

```text
docs/
├── archive/
│   └── README.md
├── design-docs/
├── exec-plans/
│   ├── active/
│   └── completed/
├── product-specs/
├── references/
└── templates/
scripts/
```

If `active/`, `completed/`, or `references/` is empty, add `.gitkeep`. `archive/` must contain the template's `README.md`, which defines the read-only boundary and maintains the archive catalog.

### 3.5 Files to Generate

**Copy verbatim from template:**

- `docs/archive/README.md`
- `docs/templates/design-doc.md`
- `docs/templates/exec-plan.md`
- `scripts/check-docs.py`

**Customize with project facts:**

| File | Fill with |
|---|---|
| `AGENTS.md` | Commands, tech stack, coding rules, testing rules, project-specific agent rules |
| `ARCHITECTURE.md` | Architecture map, directory responsibilities, layering rules, cross-cutting concerns |
| `docs/STATE.md` | Deployment/runtime summary, infrastructure, known limitations; no product capabilities |
| `docs/DEPLOYMENT.md` | Deploy targets, env/secrets, smoke tests, rollback notes |
| `docs/TESTING.md` | Test categories, layout, commands, guidelines, coverage/quality gates |
| `docs/product-specs/knowledge-base.md` | Features, key files, data model, user-visible behavior |
| `docs/product-specs/glossary.md` | Canonical project terms |
| `docs/DECISIONS.md` | Existing still-binding decisions; remove expired/superseded entries and archive historical snapshots only when needed |
| `docs/TECH_DEBT.md` | Real implementation deviations with evidence, engineering impact, and repayment paths; active entries only |
| `docs/BACKLOG.md` | Product gaps, deferred decisions, and ops/security follow-ups with explicit value or restart conditions; active entries only |
| `docs/design-docs/index.md` | Existing design docs/RFCs/ADRs migrated into `docs/design-docs/`, with their lifecycle status |
| `docs/exec-plans/index.md` | Existing active/completed plans migrated into `docs/exec-plans/` |

### 3.6 Design Doc / Exec Plan Criteria

Do not create Design Docs or Exec Plans just because many files were touched during bootstrap.

Create a Design Doc only for major architecture/product design changes with real competing approaches and expensive rollback.

Create an Exec Plan only for cross-package/service cutovers, irreversible migrations, or multi-PR/multi-session work. A single-PR migration into this documentation framework does not need its own plan unless the user asks.

### 3.7 `.gitignore` Update

Append only missing entries:

```gitignore
.DS_Store
*.swp
*.swo
*~
```

### 3.8 Cleanup

- Search for stale docs outside the new structure.
- Remove duplicate, invalidated, or superseded docs with no historical value after migration.
- Move obsolete documents that retain historical research value to `docs/archive/`, update the archive catalog, and confirm current docs no longer treat archived content as authority.
- Revalidate every existing `DECISIONS.md`, `TECH_DEBT.md`, and `BACKLOG.md` entry; delete entries that are no longer active or binding.
- Update stale links in the root `README.md` if needed.
- Remove `/tmp/agentic-docs-templates` if cloned.

---

## Phase 4: Verification & Wrap-up

### 4.1 File Completeness

Verify these files exist:

- `AGENTS.md`
- `ARCHITECTURE.md`
- `docs/STATE.md`
- `docs/DEPLOYMENT.md`
- `docs/archive/README.md`
- `docs/TESTING.md`
- `docs/DECISIONS.md`
- `docs/TECH_DEBT.md`
- `docs/BACKLOG.md`
- `docs/product-specs/knowledge-base.md`
- `docs/product-specs/glossary.md`
- `docs/design-docs/index.md`
- `docs/exec-plans/index.md`
- `docs/templates/design-doc.md`
- `docs/templates/exec-plan.md`
- `scripts/check-docs.py`

### 4.2 No Unfilled Placeholders

Run:

```bash
grep -r "CUSTOMIZE" --include="*.md" .
```

For a bootstrapped project, zero results should remain except in intentionally retained template documentation.

### 4.3 Governance Constraints

Check manually:

- No fact appears in two documents; `STATE.md` contains no product capabilities
- `STATE.md` / `knowledge-base.md` entries meet the five-line budget and do not repeat Design Doc / Exec Plan details
- `DECISIONS.md` entries meet the 15-line budget and retain only still-binding constraints
- `TECH_DEBT.md` / `BACKLOG.md` contain no completed tables, stale entries, or active-plan duplicates
- Durable documents do not track specific migration application state
- `archive/` documents are not treated as authority by current docs

### 4.4 Documentation Integrity

Run:

```bash
python3 scripts/check-docs.py
```

Fix reported issues.

### 4.5 Present Summary

List generated/modified/deleted files and one-line content summaries. Also list unknowns the user still needs to fill.

### 4.6 Next Steps

- Claude Code users: copy/symlink `AGENTS.md` to `CLAUDE.md` if the tool does not read `AGENTS.md`.
- Cursor users: copy relevant rules into `.cursorrules` or project settings if needed.
- GitHub Copilot users: copy relevant rules into `.github/copilot-instructions.md` if needed.
- Review and refine `AGENTS.md`, `ARCHITECTURE.md`, `STATE.md`, and `DEPLOYMENT.md` first; those have the largest effect on agent behavior.
- Periodically compare `scripts/check-docs.py` and fixed framework sections against the template repo for updates.

---

## Important Reminders

- Be honest, not optimistic. If there are no tests or unclear architecture, say so.
- Runtime-state and product-knowledge docs are budgeted snapshots, not changelogs or Design Doc copies; every fact has one owning document.
- `TECH_DEBT.md` tracks implementation deviations with repayment paths; `BACKLOG.md` tracks product/deferred/ops follow-ups with explicit value or restart conditions. Both are active queues, not historical ledgers.
- Do not fabricate alternatives, issues, technical debt, or backlog entries to fill a report.
- Preserve existing project-specific rules, but do not preserve obsolete docs as competing sources of truth; archived content exists only for historical research.
