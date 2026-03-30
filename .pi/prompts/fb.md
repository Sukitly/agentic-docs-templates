---
description: Handle PR comments and address feedback
---

Check the comments on the current PR. Carefully evaluate whether these comments are reasonable. If they are, provide a fix plan and suggestions first — I will then tell you whether to proceed with code changes.

## Important: When fetching PR comments, you must retrieve both the review body AND inline review comments

`gh pr view --json reviews` only returns the top-level review body and **does not include** inline comments annotated on specific code lines.

You must additionally call:
```bash
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments
```
to fetch all inline comments, otherwise important feedback will be missed.
