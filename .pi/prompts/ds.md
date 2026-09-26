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

Check every row. Do not skip rows because the change feels small. Hitting a row does not by itself require a doc edit: change a document only when this change really alters a fact that document states (Fact Ownership in `AGENTS.md`).

| Trigger Event | Must check / update |
|---|---|
| Exec Plan completed | `docs/exec-plans/index.md` (move plan to `completed/`); check `docs/product-specs/knowledge-base.md`, `docs/STATE.md`, and `ARCHITECTURE.md` against Fact Ownership |
| Design Doc implementation merged | Set status to `Implemented`, add the `Body fingerprint` line reported by `python3 scripts/check-docs.py`, sync the status column in `docs/design-docs/index.md` |
| Design Doc enters implementation | `ARCHITECTURE.md` if architecture changed; `docs/DECISIONS.md` only if the decision crosses the Design Doc boundary |
| User-visible capability added/removed/changed | The matching entry in `docs/product-specs/knowledge-base.md`; interaction details are not recorded |
| An implemented Design Doc or an existing decision is overturned | Write the rationale in a new carrier (a new Design Doc, an `AD` entry that meets the admission criteria, otherwise the PR description); the old Design Doc only updates its `Superseded` line, and the old decision entry is deleted |
| Architecture/layering changed | `ARCHITECTURE.md` |
| Technical decision made without a carrying doc | `docs/DECISIONS.md`, after applying the file's admission criteria |
| New infrastructure/dependency/deployment target introduced | `docs/STATE.md`, `docs/DEPLOYMENT.md`, `ARCHITECTURE.md` |
| New design proposal | Create doc in `docs/design-docs/`, update `docs/design-docs/index.md` |
| New execution plan | Create doc in `docs/exec-plans/active/`, update `docs/exec-plans/index.md` |
| New tech debt discovered | Report it to the user; write it to `docs/TECH_DEBT.md` only after approval (Hard Rule #13), applying the file's admission criteria |
| New product gap / deferred decision / operational follow-up discovered | Report it to the user; write it to `docs/BACKLOG.md` only after approval (Hard Rule #13), applying the file's admission criteria |
| Document has completed its purpose but retains historical value | Move it to `docs/archive/` and record its original location and archive reason; delete it if it has no historical value |

## Step 2.5: Exec Plan lifecycle check

If this change is associated with an Exec Plan:

1. Read the Exec Plan file.
2. If all implementation work is done, set header status to `✅ Completed`.
3. Move the file from `docs/exec-plans/active/` to `docs/exec-plans/completed/`.
4. Update `docs/exec-plans/index.md`: remove from Active Plans, add to Completed Plans.
5. If a Design Doc this plan implements is not yet `Implemented`, set it to `Implemented`, add its `Body fingerprint`, and sync the status column in `docs/design-docs/index.md`.
6. Verify with `ls docs/exec-plans/active/`, `ls docs/exec-plans/completed/`, and re-read `docs/exec-plans/index.md`.

## Step 3: Read affected docs before editing

For each doc hit in Step 2, read the current file first. Do not update from memory.

## Step 4: Execute updates

Rules:

- Change only entries whose facts actually changed, and only the part that changed; never opportunistically reword, reorder, compress, or extend unaffected entries.
- `docs/STATE.md`: runtime, infrastructure, and known limitations only; product capabilities do not belong here. Each entry is no more than five lines (roughly 300 words).
- `docs/product-specs/knowledge-base.md`: only the purpose, current behavior, authoritative docs, key paths, and known gaps of user-visible capabilities; no interaction micro-details or implementation parameters. Each entry is no more than five lines (roughly 300 words).
- Design Docs: never rewrite the body of an Implemented doc; when overturning it, write a new carrier and update only the old doc's `Superseded` line.
- `docs/DECISIONS.md`: record only decisions that pass admission criteria and still constrain future work; each entry is no more than 15 lines and its body is not edited after writing. Delete expired or superseded entries, or archive them when they retain historical research value.
- `docs/TECH_DEBT.md`: record only implementation deviations with evidence, engineering impact, and repayment paths; report to the user and get approval before writing.
- `docs/BACKLOG.md`: record only product gaps, deferred decisions, and ops/security follow-ups with explicit value or restart conditions; report to the user and get approval before writing.
- When changing a related domain, revalidate affected existing Decision, Tech Debt, and Backlog entries. Delete entries that are repaid, started, abandoned, invalidated, or superseded instead of only appending new rows.
- `TECH_DEBT.md` and `BACKLOG.md` do not maintain resolved/completed tables or duplicate active Exec Plan tracking.
- Durable documents must not track whether a specific migration is pending or applied; transient state belongs in the deployment system or an active Exec Plan.
- `docs/DEPLOYMENT.md`: record only deployment targets, environments, smoke tests, rollback, and deployment mechanism facts.
- `ARCHITECTURE.md`: update module structure, layering rules, and dependency directions.
- `docs/archive/`: store only documents that have completed their purpose but retain historical research value; archives are read-only and not current authority.
- Index files: keep indexes synchronized with actual docs.
- Cross-references: fix only the fact's owning document; other docs reference it by link, so check the links still point to the right place instead of restating the fact.

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
- Documents and entries whose facts did not change were left untouched: ✅
- No Implemented Design Doc was rewritten, and `check-docs.py` passes: ✅
- STATE / knowledge-base entry budgets: ✅
- DECISIONS entry budget: ✅
- Existing debt / backlog / decisions revalidated: ✅
- No migration application state in durable documents: ✅
- Archives not treated as current authority: ✅
```
