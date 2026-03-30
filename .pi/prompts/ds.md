---
description: Check and sync all docs based on current branch changes
---

You need to perform a complete documentation sync check and update based on the current branch's code changes.

> **Important prerequisite:** When the user triggers this command, it means all work requiring manual verification (UI confirmation, manual testing, SQL script execution, deployment verification, etc.) is already complete. If the current Exec Plan has all Phases completed and the user triggers this command, treat the plan as complete — proceed directly with status updates and file migration. Do not ask the user "have you verified?".

## Step 1: Understand the scope of changes

First confirm the current branch, then get the change scope:

```bash
branch=$(git branch --show-current)
if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  # On main branch: check uncommitted changes
  git diff --stat
  git diff --cached --stat
else
  # On feature branch: check full diff against main (committed + uncommitted)
  git diff main --stat
  git log main..HEAD --oneline
fi
```

## Step 2: Check against the Doc Sync Matrix line by line

Compare against the matrix below to determine whether each trigger condition is hit by this change. **Check every row — do not skip any.**

| Trigger Event | Must check / update |
|---|---|
| **Exec Plan completed** | STATE.md, DECISIONS.md, exec-plans/index.md (move to `completed/`), knowledge-base.md, ARCHITECTURE.md |
| **Design Doc adopted** | DECISIONS.md (record adoption decision), ARCHITECTURE.md (if architecture changes) |
| **Product feature added/changed** | knowledge-base.md, STATE.md (Feature Status) |
| **Architecture/layering changed** | ARCHITECTURE.md |
| **Technical decision made (in conversation, design doc, or plan)** | DECISIONS.md — any meaningful trade-off or choice must be recorded |
| **New infrastructure/dependency introduced** | STATE.md, ARCHITECTURE.md |
| **New design proposal** | Create doc in `docs/design-docs/`, update index.md |
| **New execution plan** | Create doc in `docs/exec-plans/active/`, update index.md |
| **New tech debt discovered** | tech-debt.md |
| **Quality score changes** | QUALITY_SCORE.md |

## Step 2.5: Exec Plan lifecycle check (frequently missed — must verify separately)

If this change is associated with an Exec Plan, perform the following checks:

1. **Confirm plan status**: Read the Exec Plan file and check if all Phases are completed. If all are done:
2. **Update plan document status**: Change the `**Status**` in the file header to `✅ Completed`
3. **Move the file**: Move from `docs/exec-plans/active/` to `docs/exec-plans/completed/`
   ```bash
   git mv docs/exec-plans/active/E{N}-xxx.md docs/exec-plans/completed/E{N}-xxx.md
   ```
4. **Update index.md**: Read `docs/exec-plans/index.md`, move the plan's entry from the "Active" table to the "Completed" table. **Read the current content of index.md first, confirm the position and format of both tables, then modify.**

> ⚠️ Steps 3 and 4 are the most commonly missed operations. Even if you think you've already done them, verify with `ls docs/exec-plans/active/` and `ls docs/exec-plans/completed/` that the file has actually been moved, and re-read index.md to confirm the entry has been migrated.

## Step 3: Read the current content of affected documents

For each document hit in Step 2, **read its current content first** to understand the existing structure and context before deciding how to update. Do not modify from memory.

## Step 4: Execute updates

For each document that needs updating, make the specific changes. Follow these rules:

- **DECISIONS.md**: Use the correct prefix (`E[N]` for plan decisions / `AD[N]` for ad-hoc decisions / `D[N]` for design doc decisions). Record "what changed, why, key trade-offs, what was deferred/remaining". If someone joining the project tomorrow would ask "why did you do it this way?", it should be recorded
- **STATE.md**: Only update current state, not history (history goes in DECISIONS.md)
- **knowledge-base.md**: Update feature descriptions, key file paths, database schema
- **ARCHITECTURE.md**: Update module structure, layering rules, dependency directions
- **exec-plans/index.md**: If plan is completed, move the entry from Active to Completed
- **Cross-references**: When updating any document, check whether related documents also need syncing. Documents are never updated in isolation

## Step 5: Present evidence checklist

After completion, present the following evidence checklist. **Do not just check boxes — you must write specific content.**

```
## Doc Sync Results

### Exec Plan Lifecycle (if applicable)
- Associated plan: E{N}-xxx
- Plan status updated: ✅ / N/A
- File moved from active/ to completed/: ✅ (verified: `ls docs/exec-plans/completed/E{N}-*`) / N/A
- index.md entry migrated: ✅ / N/A

### Document Updates

| Document | Needs update? | Change summary |
|---|---|---|
| STATE.md | ✅ Updated | Added Feature X to core features list |
| DECISIONS.md | ✅ Updated | Added AD7 — chose approach A over B |
| ARCHITECTURE.md | ⬜ No update needed | This change did not involve architecture |
| knowledge-base.md | ✅ Updated | Updated file paths for XX module |
| exec-plans/index.md | ✅ Updated | E{N} moved from Active to Completed |
| tech-debt.md | ⬜ No update needed | — |
| QUALITY_SCORE.md | ⬜ No update needed | — |
```
