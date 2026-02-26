# Code Review Output Template

When saving as an artifact document, prepend YAML frontmatter before the report body:

```yaml
---
type: code-review
target: "{file_or_directory_path}"
date: "{YYYY-MM-DD}"
commit: "{current_HEAD_short_hash}"
focus: "{focus_area}"
severity_filter: "{severity}"
findings:
  critical: {n}
  major: {n}
  minor: {n}
  suggestions: {n}
overall: "{Ready to merge | Needs minor changes | Needs significant work}"
---
```

## Report Body

```markdown
# Code Review: {file_or_directory}

**Report saved to:** `.reports/code-reviews/{filename}.md`

## Summary
**Overall Assessment:** {emoji} Ready to merge | Needs minor changes | Needs significant work
**Files Reviewed:** {count}
**Issues Found:** {critical} critical, {major} major, {minor} minor
**Date:** {YYYY-MM-DD} | **Commit:** `{short_hash}`

## Critical Issues ({count})

### CR-{N}: {Title}
**File:** `{path}:{lines}`
**Severity:** Critical
**Category:** {Security | Logic | Performance | Maintainability}

**Problem:**
{Description of the issue}

**Current Code:**
```{lang}
{problematic code}
```

**Recommended Fix:**
```{lang}
{fixed code}
```

**Why This Matters:**
{Impact explanation}

---

## Major Issues ({count})
{Same format, reduced detail}

## Minor Issues ({count})
{Brief format: file, current, suggested}

## Suggestions ({count})
{Brief improvement ideas}

## Positive Observations
{What the code does well}

## Review Statistics

| Category | Count |
|----------|-------|
| Security | {n} |
| Logic | {n} |
| Performance | {n} |
| Style | {n} |
```
