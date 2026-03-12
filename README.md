# Agentic Docs Templates

A **language-agnostic, framework-agnostic** repository template for document-driven AI coding agent development.

This template provides a structured documentation system that guides AI coding agents (Claude, Cursor, Copilot, etc.) to follow disciplined development workflows: read docs first, plan before coding, write tests before implementation, and keep documentation in sync with code.

## Why?

AI coding agents are powerful but undisciplined by default. They skip context, forget architecture rules, and produce code that drifts from your design. This template solves that by giving the agent:

- **A knowledge map** — so it reads before it writes
- **Hard rules** — so it plans before it executes
- **Document templates** — so decisions are captured, not lost in chat
- **Self-review checklists** — so quality is enforced, not hoped for

## Quick Start

1. **Create a new repo** from this template (click "Use this template" on GitHub)
2. **Customize `AGENTS.md`** — fill in the `<!-- CUSTOMIZE -->` sections with your tech stack, commands, and coding rules
3. **Customize `ARCHITECTURE.md`** — document your project's structure and layering rules
4. **Start developing** — the agent will follow the workflow defined in `AGENTS.md`

## Existing Projects

Already have a project and want to adopt this documentation framework? Use the bootstrap prompt — an AI agent will analyze your project and generate all documentation files pre-filled with real content.

```bash
# Claude Code
claude "Read https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md and follow the instructions to set up agentic docs for this project."

# Or download first
curl -sO https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md
claude "Read bootstrap.md and follow the instructions to set up agentic docs for this project."
```

The bootstrap prompt works with any AI coding agent. It will:

1. **Analyze** your project — tech stack, architecture, conventions, existing docs
2. **Confirm** findings with you before generating anything
3. **Generate** all documentation files with real, project-specific content (not empty templates)
4. **Verify** documentation integrity automatically

See [`bootstrap.md`](bootstrap.md) for the full prompt.

## Structure

```
├── AGENTS.md                      # Agent instructions (hard rules, workflow, checklists)
├── ARCHITECTURE.md                # Architecture map (customize per project)
├── docs/
│   ├── QUALITY_SCORE.md           # Module quality ratings
│   ├── TESTING.md                 # Testing strategy
│   ├── product-specs/
│   │   ├── knowledge-base.md      # Feature descriptions, file paths, data model
│   │   └── product-roadmap.md     # Product direction
│   ├── design-docs/
│   │   └── index.md               # Design document index
│   ├── exec-plans/
│   │   ├── index.md               # Execution plan index
│   │   ├── active/                # In-progress plans
│   │   ├── completed/            # Done plans
│   │   └── tech-debt.md          # Tech debt tracker
│   ├── templates/
│   │   ├── design-doc.md         # Template for design documents
│   │   └── exec-plan.md          # Template for execution plans
│   └── references/               # External guides and references
└── .gitignore
```

## Core Concepts

### Hard Rules

The agent is bound by 5 non-negotiable rules (in `AGENTS.md`):

1. **Read docs first** — understand context before touching code
2. **Docs before code** — create Design Doc or Exec Plan when criteria are met
3. **Plan before execute** — present changes and wait for approval
4. **Self-review + update docs** — run checklist and keep docs in sync
5. **Tests first** — TDD for core business logic

### Document Types

| Type           | When to Create                                                          | Template                       |
| -------------- | ----------------------------------------------------------------------- | ------------------------------ |
| **Design Doc** | New module, cross-module refactor, new dependency, 2+ viable approaches | `docs/templates/design-doc.md` |
| **Exec Plan**  | ≥3 modules affected, DB migrations, ordered dependencies                | `docs/templates/exec-plan.md`  |

### Workflow

```
Task received
  → Read relevant docs (Knowledge Map)
  → Create Design Doc / Exec Plan if needed
  → Get user approval
  → Write tests (TDD for core logic)
  → Implement
  → Run self-review checklist
  → Update affected docs
  → Done ✅
```

## Documentation Integrity Check

A Python script is included to verify documentation health:

```bash
python3 scripts/check-docs.py

# or via uv
uv run scripts/check-docs.py
```

It checks:

1. **Broken links** — all relative markdown links point to existing files
2. **Index coverage** — `index.md` files list all docs in their directories
3. **Exec plan structure** — required frontmatter fields and sections are present
4. **Architecture references** — paths referenced in `ARCHITECTURE.md` exist

No dependencies required — just Python 3.

## Customization Guide

Search for `<!-- CUSTOMIZE -->` comments across all files to find sections you need to fill in for your project:

- **`AGENTS.md`** — Commands, tech stack, coding rules, testing rules
- **`ARCHITECTURE.md`** — Directory structure, layering rules, conventions
- **`docs/TESTING.md`** — Test categories, directories, commands, coverage goals
- **`docs/product-specs/knowledge-base.md`** — Features, data model, file paths

## Compatibility

This template works with any AI coding agent that reads repository files for context:

- **Claude Code** (CLI) — reads `CLAUDE.md` / `AGENTS.md` automatically
- **Cursor** — reads project rules files
- **GitHub Copilot** — reads `.github/copilot-instructions.md`
- **Other agents** — most can be pointed to read `AGENTS.md`

> **Tip**: If your agent uses a different instructions file (e.g., `.cursorrules`), simply copy or symlink the content from `AGENTS.md`.

## Inspiration

This template is heavily inspired by OpenAI's [Harness Engineering](https://openai.com/index/harness-engineering/) approach to AI-assisted development, combined with practical lessons learned from real-world projects.

## License

MIT
