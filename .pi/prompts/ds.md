---
description: Check and sync all docs based on current branch changes
---

Perform a complete documentation sync check and update based on the current branch changes.

> Important prerequisite: when the user triggers this command, manual verification that only the user can perform is already complete. If an associated Exec Plan has all implementation work completed and the user triggers this command, treat the plan as complete and proceed with status/index/file migration.

## Step 1: Understand the scope of changes

Confirm the current branch and change scope:

```bash
branch=$(git branch --show-current)
if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  git diff --stat
  git diff --cached --stat
else
  git diff main --stat
  git log main..HEAD --oneline
fi
```

## Step 2: Check the Doc Sync Matrix line by line

Check every row. Do not skip rows because the change feels small.

| Trigger Event | Must check / update |
|---|---|
| Exec Plan completed | `docs/STATE.md`, `docs/exec-plans/index.md` (move plan to `completed/`), `docs/product-specs/knowledge-base.md` if product behavior changed, `ARCHITECTURE.md` if architecture changed |
| Design Doc adopted | `ARCHITECTURE.md` if architecture changed; `docs/DECISIONS.md` only if the decision crosses the Design Doc boundary |
| Product feature added/changed | `docs/product-specs/knowledge-base.md`, `docs/STATE.md` |
| Architecture/layering changed | `ARCHITECTURE.md` |
| Technical decision made without a carrying doc | `docs/DECISIONS.md`, after applying the file's admission criteria |
| New infrastructure/dependency/deployment target introduced | `docs/STATE.md`, `docs/DEPLOYMENT.md`, `ARCHITECTURE.md` |
| New design proposal | Create doc in `docs/design-docs/`, update `docs/design-docs/index.md` |
| New execution plan | Create doc in `docs/exec-plans/active/`, update `docs/exec-plans/index.md` |
| New tech debt discovered | `docs/TECH_DEBT.md`, after applying the file's admission criteria |
| New product gap / deferred decision / operational follow-up discovered | `docs/BACKLOG.md`, after applying the file's admission criteria |
| Document has completed its purpose but retains historical value | Move it to `docs/archive/` and record its original location and archive reason; delete it if it has no historical value |

## Step 2.5: Exec Plan lifecycle check

If this change is associated with an Exec Plan:

1. Read the Exec Plan file.
2. If all implementation work is done, set header status to `✅ Completed`.
3. Move the file from `docs/exec-plans/active/` to `docs/exec-plans/completed/`.
4. Update `docs/exec-plans/index.md`: remove from Active Plans, add to Completed Plans.
5. Verify with `ls docs/exec-plans/active/`, `ls docs/exec-plans/completed/`, and re-read `docs/exec-plans/index.md`.

## Step 3: Read affected docs before editing

For each doc hit in Step 2, read the current file first. Do not update from memory.

## Step 4: Execute updates

Rules:

- `docs/STATE.md`: rewrite affected entries in place, retaining only the current conclusion and authoritative links; each entry is no more than five lines (roughly 300 words).
- `docs/product-specs/knowledge-base.md`: rewrite affected feature entries in place, retaining only purpose, current behavior, authoritative docs, key paths, and known gaps; each entry is no more than five lines (roughly 300 words).
- `docs/DECISIONS.md`: record only decisions that pass admission criteria and still constrain future work; each entry is no more than 15 lines. Delete expired or superseded entries, or archive them when they retain historical research value.
- `docs/TECH_DEBT.md`: record only implementation deviations with evidence, engineering impact, and repayment paths.
- `docs/BACKLOG.md`: record only product gaps, deferred decisions, and ops/security follow-ups with explicit value or restart conditions.
- When changing a related domain, revalidate affected existing Decision, Tech Debt, and Backlog entries. Delete entries that are repaid, started, abandoned, invalidated, or superseded instead of only appending new rows.
- `TECH_DEBT.md` and `BACKLOG.md` do not maintain resolved/completed tables or duplicate active Exec Plan tracking.
- Durable documents must not track whether a specific migration is pending or applied; transient state belongs in the deployment system or an active Exec Plan.
- `docs/DEPLOYMENT.md`: record only deployment targets, environments, smoke tests, rollback, and deployment mechanism facts.
- `ARCHITECTURE.md`: update module structure, layering rules, and dependency directions.
- `docs/archive/`: store only documents that have completed their purpose but retain historical research value; archives are read-only and not current authority.
- Index files: keep indexes synchronized with actual docs.
- Cross-references: docs are not updated in isolation.

## Step 5: Present evidence checklist

Do not only check boxes. Provide concrete evidence.

```markdown
## Doc Sync Results

### Exec Plan Lifecycle
- Associated plan: E{N}-xxx / N/A
- Status updated: ✅ / N/A
- File moved to completed/: ✅ / N/A
- Index entry migrated: ✅ / N/A

### Document Updates

| Document | Needs update? | Change summary |
|---|---|---|
| STATE.md | ✅ Updated / No | ... |
| DECISIONS.md | ✅ Updated / No | ... |
| ARCHITECTURE.md | ✅ Updated / No | ... |
| DEPLOYMENT.md | ✅ Updated / No | ... |
| knowledge-base.md | ✅ Updated / No | ... |
| exec-plans/index.md | ✅ Updated / No | ... |
| TECH_DEBT.md | ✅ Updated / No | ... |
| BACKLOG.md | ✅ Updated / No | ... |
| archive/ | ✅ Archived / No | ... |

### Governance Constraints
- STATE / knowledge-base entry budgets: ✅
- DECISIONS entry budget: ✅
- Existing debt / backlog / decisions revalidated: ✅
- No migration application state in durable documents: ✅
- Archives not treated as current authority: ✅
```
