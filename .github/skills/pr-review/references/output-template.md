# PR Review Output Template

When saving as an artifact document, prepend YAML frontmatter before the report body:

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

## Report Body

```markdown
# Pull Request Review

**Report saved to:** `.reports/pr-reviews/{filename}.md`

## Overview

**PR Title:** {title}
**Author:** @{author}
**Branch:** `{branch}` -> `{target}`
**Date:** {YYYY-MM-DD} | **Commit:** `{short_hash}`

| Metric | Value |
|--------|-------|
| Files Changed | {n} |
| Additions | +{n} |
| Deletions | -{n} |
| Commits | {n} |

## Overall Assessment

**Status:** Approved | Approved with Comments | Changes Requested

**Summary:**
{2-3 sentences on overall quality and key concerns}

---

## Required Changes (Blockers)

### RC-{N}: {Title}
**File:** `{path}:{line}`
**Category:** {Security | Reliability | Correctness}

{Description of the issue}

```diff
- {problematic code}
+ {suggested fix}
```

**Why this matters:**
{Impact explanation}

---

## Suggestions (Non-Blocking)

### S-{N}: {Title}
**File:** `{path}:{line}`
**Category:** {Performance | Maintainability}

{Description and suggested alternative with code example}

---

## Nits (Optional)

### N-{N}: {Title}
**File:** `{path}:{line}`

```diff
- {current}
+ {suggested}
```

---

## Positive Highlights

1. {What the PR does well}

---

## Testing Recommendations

- [ ] {Suggested test to add}

---

## Questions for Author

1. {Clarifying questions}

---

## Summary

{Final assessment and next steps}

## Checklist

- [ ] Required changes addressed
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Ready for merge
```
