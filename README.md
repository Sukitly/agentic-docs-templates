# Agentic Docs Templates

A language-agnostic, framework-agnostic repository template for document-driven AI coding agent development.

AI coding agents are powerful but undisciplined by default. They skip context, forget architecture rules, and produce code that drifts from your design. This template provides a structured documentation system that keeps agents in line: read docs before writing code, plan before executing, write tests before implementation, and keep documentation in sync with code.

## Table of Contents

- [Quick Start](#quick-start)
- [Adopting in Existing Projects](#adopting-in-existing-projects)
- [Repository Structure](#repository-structure)
- [Core Concepts](#core-concepts)
- [Documentation Integrity Check](#documentation-integrity-check)
- [Customization](#customization)
- [Compatibility](#compatibility)
- [Inspiration](#inspiration)
- [License](#license)

## Quick Start

1. Click "Use this template" on GitHub to create a new repo
2. Edit `AGENTS.md` and fill in the `<!-- CUSTOMIZE -->` sections with your tech stack, commands, and coding rules
3. Edit `ARCHITECTURE.md` to document your project's structure and layering rules
4. Start developing. The agent will follow the workflow defined in `AGENTS.md`

## Adopting in Existing Projects

If you already have a project and want to adopt this documentation framework, use the bootstrap prompt. An AI agent will analyze your project and generate all documentation files pre-filled with real content (not empty templates).

```bash
# Claude Code
claude "Read https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md and follow the instructions to set up agentic docs for this project."
```

Or download first:

```bash
curl -sO https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md
claude "Read bootstrap.md and follow the instructions to set up agentic docs for this project."
```

The bootstrap prompt works with any AI coding agent. It will analyze your project (tech stack, architecture, conventions, existing docs), confirm findings with you, generate all documentation files with real content, and verify documentation integrity automatically.

See [`bootstrap.md`](bootstrap.md) for details.

## Repository Structure

```
├── AGENTS.md                      # Agent instructions (rules, workflow, checklists)
├── ARCHITECTURE.md                # Architecture map (customize per project)
├── bootstrap.md                   # Bootstrap prompt for existing projects
├── docs/
│   ├── STATE.md                   # Application state snapshot
│   ├── DECISIONS.md               # Decision log
│   ├── QUALITY_SCORE.md           # Module quality ratings
│   ├── TESTING.md                 # Testing strategy
│   ├── product-specs/
│   │   ├── knowledge-base.md      # Feature descriptions, file paths, data model
│   │   ├── glossary.md            # Canonical terms and definitions
│   │   └── product-roadmap.md     # Product direction
│   ├── design-docs/
│   │   └── index.md               # Design document index
│   ├── exec-plans/
│   │   ├── index.md               # Execution plan index
│   │   ├── active/                # In-progress plans
│   │   ├── completed/             # Done plans
│   │   └── tech-debt.md           # Tech debt tracker
│   ├── templates/
│   │   ├── design-doc.md          # Template for design documents
│   │   └── exec-plan.md           # Template for execution plans
│   └── references/                # External guides and references
├── scripts/
│   └── check-docs.py             # Documentation integrity checker
└── .gitignore
```

## Core Concepts

### The Five Rules

The agent is bound by five rules defined in `AGENTS.md`:

1. **Read docs first.** Understand context before touching code.
2. **Docs before code.** Create a Design Doc or Exec Plan when the criteria are met.
3. **Plan before execute.** Present the planned changes and wait for approval.
4. **Self-review and update docs.** Run the checklist and keep docs in sync after every change.
5. **Tests first.** Use TDD for core business logic.

### Document Types

| Type       | When to Create                                                          | Template                       |
| ---------- | ----------------------------------------------------------------------- | ------------------------------ |
| Design Doc | New module, cross-module refactor, new dependency, 2+ viable approaches | `docs/templates/design-doc.md` |
| Exec Plan  | ≥3 modules affected, DB migrations, ordered dependencies                | `docs/templates/exec-plan.md`  |

### Workflow

```
Task received
  → Read relevant docs
  → Create Design Doc / Exec Plan if needed
  → Get user approval
  → Write tests (TDD for core logic)
  → Implement
  → Run self-review checklist
  → Update affected docs
  → Done ✅
```

## Documentation Integrity Check

The included Python script verifies documentation health:

```bash
python3 scripts/check-docs.py

# or via uv
uv run scripts/check-docs.py
```

It checks that all relative Markdown links point to existing files, that `index.md` files cover all docs in their directories, that exec plans have the required frontmatter fields and sections, and that paths referenced in `ARCHITECTURE.md` actually exist.

No dependencies required. Just Python 3.

## Customization

Search for `<!-- CUSTOMIZE -->` comments across all files to find sections you need to fill in:

- `AGENTS.md`: commands, tech stack, coding rules, testing rules
- `ARCHITECTURE.md`: directory structure, layering rules, conventions
- `docs/TESTING.md`: test categories, directories, commands, coverage goals
- `docs/product-specs/knowledge-base.md`: features, data model, file paths

## Compatibility

`AGENTS.md` is natively supported by most AI coding agents, including **Codex**, **Cursor**, **Gemini CLI**, **pi**, and others.

> **Note**: **Claude Code** uses `CLAUDE.md` instead — simply rename or symlink from `AGENTS.md`.

## Inspiration

This template is heavily inspired by OpenAI's [Harness Engineering](https://openai.com/index/harness-engineering/) approach to AI-assisted development, combined with practical lessons from real-world projects.

## License

MIT
