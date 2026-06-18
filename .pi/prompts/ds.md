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

- `docs/STATE.md`: update current state in place; no changelog entries.
- `docs/DECISIONS.md`: record only decisions that pass admission criteria. Do not duplicate Design Doc / Exec Plan details.
- `docs/TECH_DEBT.md`: only implementation deviations with repayment paths.
- `docs/BACKLOG.md`: product gaps, deferred decisions, ops/security follow-ups.
- `docs/DEPLOYMENT.md`: deploy target/env/smoke/rollback facts only.
- `docs/product-specs/knowledge-base.md`: update user-visible feature behavior, key files, and data model.
- `ARCHITECTURE.md`: update module structure, layering rules, dependency directions.
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
```
