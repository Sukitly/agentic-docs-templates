# Agentic Docs Templates

A language-agnostic, framework-agnostic repository template for document-driven AI coding agent development.

AI coding agents are powerful but undisciplined by default. This template gives agents a durable context system: read docs before changing code, plan before executing, write tests before implementation, keep documentation synchronized, and use single fact ownership plus admission, budget, freeze, deletion, and archive rules to prevent state snapshots, decision logs, technical debt, and backlogs from decaying into changelogs.

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
│   ├── STATE.md                   # Runtime and infrastructure state, known limitations (no changelog)
│   ├── DECISIONS.md               # Still-binding technical decisions
│   ├── DEPLOYMENT.md              # Deploy targets, env, smoke tests, rollback notes
│   ├── TESTING.md                 # Testing strategy
│   ├── TECH_DEBT.md               # Implementation deviations with repayment paths
│   ├── BACKLOG.md                 # Product gaps, deferred decisions, ops follow-ups
│   ├── archive/
│   │   └── README.md              # Read-only archive boundary and catalog
│   ├── product-specs/
│   │   ├── knowledge-base.md      # User-visible capabilities, file paths, data model
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
6. **Every fact has one owning document.** A PR changes only entries whose facts changed; snapshots are budgeted, Implemented Design Docs are frozen, stale queue entries are deleted, and history is physically separated from current authority.
7. **No minimum-diff shortcuts.** Choose the right abstraction over the smallest patch.
8. **No silent decisions.** Non-trivial choices must be explicit; do not fabricate alternatives just to fill a table.
9. **No unrequested actions.** Report out-of-scope findings instead of modifying them opportunistically.
10. **No ledger writes without approval.** New `TECH_DEBT.md` / `BACKLOG.md` entries are reported to the user and written only after approval.

### Document Types

| Type | When to Create | Location |
|---|---|---|
| Runtime state snapshot | Always present; runtime, infrastructure, and known limitations | `docs/STATE.md` |
| Product knowledge snapshot | Always present; the sole owner of user-visible capabilities | `docs/product-specs/knowledge-base.md` |
| Design Doc | Significant architecture/product design change with real competing approaches; frozen once the implementation merges | `docs/templates/design-doc.md` |
| Exec Plan | Cross-package/service cutover, irreversible migration, or multi-PR/multi-session work | `docs/templates/exec-plan.md` |
| Decision Log | Still-binding cross-cutting decision without a carrying doc | `docs/DECISIONS.md` |
| Tech Debt | Implementation deviation with evidence, engineering impact, and a repayment path | `docs/TECH_DEBT.md` |
| Backlog | Product gap, deferred decision, or ops/security follow-up with explicit value or restart conditions | `docs/BACKLOG.md` |
| Historical Archive | Document has completed its purpose but retains historical research value | `docs/archive/` |

### Documentation Freshness Boundaries

- Every fact has one owning document; other documents only link to it. A document whose facts a PR did not change is not touched. Documents carry no `Last updated` dates; history belongs in git.
- `STATE.md` holds only runtime and infrastructure; `knowledge-base.md` holds only user-visible capabilities. Entries are no more than five lines (roughly 300 words); interaction details and implementation parameters belong in code.
- The Design Doc lifecycle is `Draft → In progress → Implemented`; a doc is frozen once its implementation merges, overturning it means writing a new carrier and updating only the old doc's `Superseded` line, and the body is verified by fingerprint.
- `DECISIONS.md` entries are no more than 15 lines, retain only decisions that still constrain future work, and are not edited after writing.
- `TECH_DEBT.md` and `BACKLOG.md` are active queues, not historical ledgers; they admit only items with no other carrier, and writing requires user approval. Delete entries when repaid, started, abandoned, invalidated, or superseded; do not maintain completed tables or duplicate active Exec Plan tracking.
- Durable documents do not track whether a specific migration is pending or applied; transient state belongs in the deployment system or an active Exec Plan.
- `archive/` is read-only and not current authority; delete obsolete content with no historical value.

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

The script checks relative Markdown links, index coverage, Exec Plan structure, Implemented Design Doc body fingerprints and index status consistency, and `ARCHITECTURE.md` path references. It has no external dependencies beyond Python 3.

## Customization

Search for `<!-- CUSTOMIZE -->` comments across Markdown files:

- `AGENTS.md`: commands, tech stack, coding rules, testing rules
- `ARCHITECTURE.md`: directory structure, layering rules, conventions
- `docs/STATE.md`: deployment/runtime, infrastructure, known limitations
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
