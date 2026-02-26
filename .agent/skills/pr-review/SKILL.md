---
name: pr-review
description: Professional pull request review with structured feedback across correctness, security, performance, testing, maintainability, and compatibility. Use when asked to review a PR, check changes, analyze a diff, or review pull request code quality.
---

# PR Review

Perform a thorough, constructive pull request review and save the report as a persistent document artifact.

## Output Structure

```
.reports/
├── pr-reviews/
│   └── {YYYY-MM-DD}-PR-{number-or-branch}.md    # Full PR review report
└── metadata.json                                  # Report tracking
```

## Execution

### Phase 1: Context

1. Read PR title, description, and linked issues to understand the problem being solved
2. Analyze scope: count changed files, identify change type (feature, fix, refactor, docs)
3. Check existing tests and related files that might need updates

### Phase 2: Six-Dimension Review

**Correctness:** Does it work? Edge cases handled? Error handling? Async correctness? State management?

**Security:** No injection vulnerabilities, hardcoded secrets, or IDOR. Input validation present. Sensitive data not logged. Secure defaults.

**Performance:** No N+1 queries, unnecessary DB calls, or blocking operations in hot paths. Caching considered. Memory efficient.

**Testing:** New code has tests. Happy path, error cases, and edge cases covered. Tests are not flaky.

**Maintainability:** Readable, appropriately sized functions, clear naming, follows project conventions, DRY.

**Compatibility:** No undocumented breaking API changes. Migrations reversible. Dependencies updated appropriately.

For PR-type-specific checklists, see [references/pr-type-checklists.md](references/pr-type-checklists.md).

### Phase 3: Write Review

Use the output template in [references/output-template.md](references/output-template.md).

**Review etiquette:**
- Be specific — "This query could cause X. Consider Y instead." not "This is wrong."
- Explain why — "Using X prevents Y because Z" not "Use X instead."
- Offer alternatives with code examples
- Severity levels: Blocker (must fix) → Suggestion (non-blocking) → Nit (optional)
- Acknowledge good work

### Phase 4: Save Artifact

**MANDATORY: Always save the full PR review as a document artifact.**

1. Create `.reports/pr-reviews/` directory if it doesn't exist
2. Generate filename: `{YYYY-MM-DD}-PR-{number-or-branch}.md` (e.g., `2025-03-15-PR-142.md` or `2025-03-15-PR-feat-auth.md`)
3. Write the full review report with YAML frontmatter metadata:

```yaml
---
type: pr-review
pr_number: "{number_or_branch}"
pr_title: "{title}"
pr_author: "{author}"
branch: "{source_branch} -> {target_branch}"
date: "{YYYY-MM-DD}"
commit: "{current_HEAD_short_hash}"
focus: "{focus_area}"
status: "{Approved | Approved with Comments | Changes Requested}"
stats:
  files_changed: {n}
  additions: {n}
  deletions: {n}
findings:
  blockers: {n}
  suggestions: {n}
  nits: {n}
---
```

4. Write the full review report body after the frontmatter
5. Update `.reports/metadata.json` — merge this report entry into the `reports` array:

```json
{
  "reports": [
    {
      "type": "pr-review",
      "file": "pr-reviews/{filename}.md",
      "pr": "{number_or_branch}",
      "date": "{ISO timestamp}",
      "commit": "{hash}",
      "status": "{Approved | Changes Requested}",
      "findings": { "blockers": 0, "suggestions": 2, "nits": 1 }
    }
  ]
}
```

6. Display to the user: the summary + the file path where the full report was saved

**If `--no-artifact` is passed, skip artifact generation and only display to conversation.**

## Large PRs

1. Request split if scope is too large
2. Prioritize: security-sensitive → core business logic → public APIs
3. Use checkpoint with `/pr-review --continue` for continuation

## Arguments

- `$1` — PR URL or reference (defaults to current diff)
- `--focus` — `security`, `performance`, `tests`, or `all`
- `--strict` — Stricter review for production code
- `--continue` — Resume large PR review
- `--no-artifact` — Skip saving report as document (display only)
