# Agentic Docs Templates

A language-agnostic, framework-agnostic repository template for document-driven AI coding agent development.

AI coding agents are powerful but undisciplined by default. This template gives agents a durable context system: read docs before changing code, plan before executing, write tests before implementation, keep documentation synchronized, and avoid low-quality "minimum diff" shortcuts.

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
3. Edit `ARCHITECTURE.md`, `docs/STATE.md`, `docs/TESTING.md`, and product specs with real project facts
4. Run `python3 scripts/check-docs.py`
5. Start developing. The agent will follow the workflow defined in `AGENTS.md`

## Adopting in Existing Projects

Use the bootstrap prompt. An AI agent will analyze your project and generate the documentation files with project-specific content.

```bash
# Claude Code
claude "Read https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md and follow the instructions to set up agentic docs for this project."
```

Or download first:

```bash
curl -sO https://raw.githubusercontent.com/Sukitly/agentic-docs-templates/main/bootstrap.md
claude "Read bootstrap.md and follow the instructions to set up agentic docs for this project."
```

The bootstrap prompt works with any AI coding agent. It analyzes the project, confirms findings with the user, generates docs with real content, and verifies documentation integrity.

## Repository Structure

```
├── AGENTS.md                      # Agent instructions (rules, workflow, checklists)
├── ARCHITECTURE.md                # Architecture map (customize per project)
├── bootstrap.md                   # Bootstrap prompt for existing projects
├── docs/
│   ├── STATE.md                   # Current-state snapshot (no changelog)
│   ├── DECISIONS.md               # Still-binding technical decisions
│   ├── DEPLOYMENT.md              # Deploy targets, env, smoke tests, rollback notes
│   ├── TESTING.md                 # Testing strategy
│   ├── TECH_DEBT.md               # Implementation deviations with repayment paths
│   ├── BACKLOG.md                 # Product gaps, deferred decisions, ops follow-ups
│   ├── product-specs/
│   │   ├── knowledge-base.md      # Feature descriptions, file paths, data model
│   │   └── glossary.md            # Canonical terms and definitions
│   ├── design-docs/
│   │   └── index.md               # Design document index
│   ├── exec-plans/
│   │   ├── index.md               # Execution plan index
│   │   ├── active/                # In-progress plans (empty in this template)
│   │   └── completed/             # Completed plans (empty in this template)
│   ├── templates/
│   │   ├── design-doc.md          # Template for design documents
│   │   └── exec-plan.md           # Template for execution plans
│   └── references/                # External guides and references
├── scripts/
│   └── check-docs.py              # Documentation integrity checker
└── .gitignore
```

## Core Concepts

### Core Rules

1. **Read docs first.** Understand current state and architecture before touching code.
2. **Create docs only when the criteria are met.** Design Docs and Exec Plans are durable carriers for significant design and multi-step work, not bureaucracy for every small change.
3. **Plan before execute.** Present planned file changes and wait for explicit approval.
4. **Tests first for core logic.** Use TDD for behavior that matters.
5. **Self-review and sync docs.** A task is not complete until checks pass and affected docs are updated.
6. **No minimum-diff shortcuts.** Choose the right abstraction over the smallest patch.
7. **No silent decisions.** Non-trivial choices must be explicit; do not fabricate alternatives just to fill a table.

### Document Types

| Type | When to Create | Template |
|---|---|---|
| Design Doc | Significant architecture/product design change with real competing approaches | `docs/templates/design-doc.md` |
| Exec Plan | Cross-package/service cutover, irreversible migration, or multi-PR/multi-session work | `docs/templates/exec-plan.md` |
| Decision Log | Still-binding cross-cutting decision without a carrying doc | `docs/DECISIONS.md` |
| Tech Debt | Implementation deviation from known-correct shape with repayment path | `docs/TECH_DEBT.md` |
| Backlog | Product gap, deferred decision, or ops/security follow-up | `docs/BACKLOG.md` |

### Workflow

```
Task received
  → Read relevant docs
  → Decide whether a Design Doc or Exec Plan is required
  → Present plan and get approval
  → Write tests first for core logic
  → Implement final path
  → Run checks
  → Run self-review
  → Update docs
  → Done
```

## Documentation Integrity Check

```bash
python3 scripts/check-docs.py

# or via uv
uv run scripts/check-docs.py
```

The script checks relative Markdown links, index coverage, Exec Plan structure, and `ARCHITECTURE.md` path references. It has no external dependencies beyond Python 3.

## Customization

Search for `<!-- CUSTOMIZE -->` comments across Markdown files:

- `AGENTS.md`: commands, tech stack, coding rules, testing rules
- `ARCHITECTURE.md`: directory structure, layering rules, conventions
- `docs/STATE.md`: deployment/runtime, infrastructure, current domain state
- `docs/DEPLOYMENT.md`: deploy targets, env vars, smoke tests, rollback notes
- `docs/TESTING.md`: test categories, directories, commands, coverage goals
- `docs/product-specs/knowledge-base.md`: features, data model, file paths
- `docs/product-specs/glossary.md`: project-specific terminology

## Compatibility

`AGENTS.md` is supported by many AI coding agents, including Codex, Cursor, Gemini CLI, pi, and others.

> **Note**: Claude Code uses `CLAUDE.md` by default. Rename, copy, or symlink `AGENTS.md` to `CLAUDE.md` if needed.

## Inspiration

This template is inspired by OpenAI's [Harness Engineering](https://openai.com/index/harness-engineering/) approach to AI-assisted development and practical lessons from real-world agent-driven projects.

## License

MIT
