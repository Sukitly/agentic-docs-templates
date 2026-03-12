# Bootstrap: Set Up Agentic Docs for an Existing Project

> **Version**: 2.0.0
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

**Your mission**: Analyze this project, clone the template repository, then fill in every template file with real, project-specific content.

Follow the phases below **in order**. Do NOT skip any phase.

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

**Important**: If agent instruction files already exist, read them carefully. Any project-specific rules and conventions from those files MUST be preserved and integrated into the generated `AGENTS.md`.

#### 1.8 Deployment & Infrastructure 🟡

- Hosting platform
- Infrastructure configuration (Docker, Terraform, etc.)
- Environment management
- Monitoring / logging services

---

### Phase 2: Present Analysis Results

After completing the analysis, present a **structured summary** to the user. Clearly separate findings into:

- **✅ Confirmed** — information with concrete evidence from the code
- **❓ Needs your input** — information you couldn't determine from code alone (e.g., deployment platform, roadmap priorities). Explain what you looked for and why you couldn't determine it.

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

### Phase 3: Clone Template & Generate Files

#### 3.1 Clone the Template Repository

```bash
git clone --depth 1 https://github.com/Sukitly/agentic-docs-templates.git /tmp/agentic-docs-templates
```

After cloning, read every file in the template to understand the exact structure, file names, and content format. The template is the **single source of truth** — your generated files must match its structure exactly.

#### 3.2 Conflict Resolution & Document Migration

> **Mindset: Be bold, not cautious.** The project is under git version control — every change can be reverted. Your job is to fully migrate the project into our framework structure, not to hedge by keeping duplicate files "just in case". Keeping both old and new versions of the same content is **worse** than migrating, because it creates confusion about which is authoritative.

**Agent instruction files:**

- **If `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or similar exists**: Read it carefully. Merge its project-specific rules into the new `AGENTS.md` (in the appropriate sections: Common Commands, Coding Rules, Git Workflow, etc.). After merging, **delete the old file** (except `.cursorrules` which serves a different tool).

**Existing documentation — migrate, don't duplicate:**

Scan the entire project for existing documentation (README files in subdirectories, `docs/` folder, wiki-style docs, design docs, ADRs, etc.). For each document found:

1. **Classify it** — determine which template file it maps to:
   - Architecture/system design docs → merge content into `ARCHITECTURE.md`
   - Feature specs, PRDs, product docs → merge into `docs/product-specs/knowledge-base.md`
   - Design docs, RFCs, ADRs, technical proposals → move to `docs/design-docs/` and list in `docs/design-docs/index.md`
   - API docs, external guides, reference material → move to `docs/references/`
   - State/status/deployment docs → merge into `docs/STATE.md`
   - Decision records → merge into `docs/DECISIONS.md`
   - Testing docs → merge into `docs/TESTING.md`
   - Roadmap/planning docs → merge into `docs/product-specs/product-roadmap.md`

2. **Migrate the content** — extract valuable information from the old doc and integrate it into the appropriate template file. Don't just copy-paste; restructure to fit the template's format.

3. **Delete the old file** — after migration is complete, remove the original file. Do NOT keep both the old doc and the new one. The template structure is the single source of truth.

4. **If a doc doesn't fit any template category**, move it to `docs/references/` as-is.

**What to delete outright:**

- Outdated documentation that describes a state of the project no longer true (e.g., old setup guides for deprecated tooling)
- Placeholder or stub docs with no real content
- Files that are fully superseded by the template structure (e.g., a bare `docs/README.md` that just lists doc links — the template's index files replace this)

**Root README.md** — do NOT modify or delete the project's root `README.md`. It serves a different purpose (GitHub landing page) and is not part of the agent docs framework.

#### 3.3 Generation Rules

For every file from the template:

1. **Copy the file to the project at the exact same relative path.** Do not rename files or change the directory structure.
2. **Replace every `<!-- CUSTOMIZE: ... -->` comment** with real, project-specific content based on your Phase 1 analysis and Phase 2 user input.
3. **Keep all non-CUSTOMIZE content exactly as-is.** Sections like Hard Rules, Development Workflow, Self-Rationalization Check, Pre-delivery Self-review, and Task Completion Criteria in `AGENTS.md` are **fixed framework content** — do NOT modify, summarize, or remove them.
4. If a CUSTOMIZE section doesn't apply to this project, replace the comment with "N/A — [brief reason]". Do NOT leave the `<!-- CUSTOMIZE -->` comment in place.
5. If a command or tool was not found during analysis (e.g., no linter configured), **omit that entry entirely** rather than writing placeholder text like `[your command here]`.
6. **Keep files concise.** `knowledge-base.md`: each feature ≤ 5 lines. `ARCHITECTURE.md`: aim for ≤ 200 lines. Don't pad.

#### 3.4 File-by-file Instructions

Process files in this order:

**Directory structure** — Create any missing directories. If a directory already exists, skip it. Only create missing subdirectories. Old files that have been migrated into the new structure should already be deleted per Phase 3.2.

```
docs/
├── design-docs/
├── exec-plans/
│   ├── active/        ← .gitkeep if empty
│   └── completed/     ← .gitkeep if empty
├── product-specs/
├── references/        ← .gitkeep if empty (for external guides, API specs, etc.)
└── templates/
```

**Template files (copy as-is, no customization needed):**

| Template file | Notes |
|---------------|-------|
| `docs/templates/design-doc.md` | Generic template, copy verbatim |
| `docs/templates/exec-plan.md` | Generic template, copy verbatim |

**Files to customize (replace `<!-- CUSTOMIZE -->` sections with real content):**

| File | What to fill in |
|------|----------------|
| `AGENTS.md` | Common Commands, Tech Stack, Coding Rules, Testing rules. **Keep all other sections (Hard Rules, Knowledge Map, Development Workflow, Self-review, etc.) exactly as-is from the template.** If the project has existing agent rules, merge them into the appropriate CUSTOMIZE sections. |
| `ARCHITECTURE.md` | High-level architecture, directory structure & responsibilities, layering rules, cross-cutting concerns, key conventions |
| `docs/STATE.md` | Deployment & runtime, key infrastructure, known limitations, feature status. Mark unknowns as "Unknown — user to fill in" |
| `docs/TESTING.md` | Overview, test categories, directory structure, commands, guidelines, coverage goals. If no tests exist, state that honestly |
| `docs/QUALITY_SCORE.md` | Module scores with honest ratings based on observed quality |
| `docs/product-specs/knowledge-base.md` | Features (with key file paths), data model, key file paths table |
| `docs/product-specs/glossary.md` | Domain terms discovered from the codebase |
| `docs/product-specs/product-roadmap.md` | Current focus, upcoming, future ideas. If unknown, note that user should fill in |

**Files to generate with structure only (no CUSTOMIZE markers, but fill in if you have data):**

| File | Notes |
|------|-------|
| `docs/DECISIONS.md` | Copy from template as-is (empty log structure) |
| `docs/design-docs/index.md` | Copy from template. If the project already has design docs, list them in the table |
| `docs/exec-plans/index.md` | Copy from template as-is (empty table) |
| `docs/exec-plans/tech-debt.md` | If you found TODO/FIXME/known issues during analysis, populate the table. Otherwise copy as-is |

**Script:**

| File | Notes |
|------|-------|
| `scripts/check-docs.py` | Copy from template verbatim. Requires Python 3.10+, no external dependencies |

#### 3.5 .gitignore Update

Read the existing `.gitignore` first. Append only entries that are not already present:

```
.DS_Store
*.swp
*.swo
*~
```

#### 3.6 Post-migration Cleanup

Review the project for any leftover documentation artifacts:

1. **Duplicate content** — Search for any remaining docs outside the template structure that overlap with generated files. If found, migrate remaining content and delete the old file.
2. **Empty directories** — If migrating docs left behind empty directories, remove them.
3. **Stale references** — If the root `README.md` links to docs that were moved or deleted, update those links to point to the new locations.

#### 3.7 Clean Up

```bash
rm -rf /tmp/agentic-docs-templates
```

---

### Phase 4: Verification & Wrap-up

1. **File completeness check** — Verify that ALL of the following files exist in the project. If any are missing, create them now:
   - `AGENTS.md`
   - `ARCHITECTURE.md`
   - `docs/STATE.md`
   - `docs/TESTING.md`
   - `docs/DECISIONS.md`
   - `docs/QUALITY_SCORE.md`
   - `docs/product-specs/knowledge-base.md`
   - `docs/product-specs/glossary.md`
   - `docs/product-specs/product-roadmap.md`
   - `docs/design-docs/index.md`
   - `docs/exec-plans/index.md`
   - `docs/exec-plans/tech-debt.md`
   - `docs/templates/design-doc.md`
   - `docs/templates/exec-plan.md`
   - `scripts/check-docs.py`

2. **No CUSTOMIZE markers remaining** — Run: `grep -r "CUSTOMIZE" --include="*.md" .` and verify zero results (excluding bootstrap.md if still present).

3. **Documentation integrity check** — Run:
   ```bash
   python3 scripts/check-docs.py
   ```
   Fix any issues it reports.

4. **Present summary** to the user — list all generated/modified files with a brief note on what each contains. Also list any files that were skipped and why.

5. **Next steps** guidance:
   - **Claude Code** users: `AGENTS.md` in the project root is automatically picked up. No extra config needed.
   - **Cursor** users: consider copying relevant rules from `AGENTS.md` into `.cursorrules` or Cursor's project settings.
   - **GitHub Copilot** users: consider copying relevant rules into `.github/copilot-instructions.md`.
   - **Other agents**: check the agent's documentation for how to point it at `AGENTS.md`.
   - Remind the user to review and refine the generated docs, especially `AGENTS.md` coding rules and `ARCHITECTURE.md` layering rules.
   - Note that `scripts/check-docs.py` comes from the template repo — periodically check for updated versions.

---

## Important Reminders

- **Be honest, not optimistic.** If the project has gaps (no tests, unclear architecture, missing docs), say so clearly in the generated files. The whole point is to give the agent an accurate picture.
- **Use today's date** for all "Last updated" fields.
- **Use real paths** in `ARCHITECTURE.md` and `knowledge-base.md`. Every backtick-quoted path must point to a file or directory that actually exists.
- **Preserve existing work.** If the project already has documentation, tests, or conventions, incorporate them — don't replace them.
- **The template structure is non-negotiable.** File names, directory paths, and fixed content sections must match the template exactly. Your job is to fill in the CUSTOMIZE sections, not to redesign the framework.
