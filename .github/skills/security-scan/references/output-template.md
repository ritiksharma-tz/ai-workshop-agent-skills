# Security Scan Output Template

When saving as an artifact document, prepend YAML frontmatter before the report body:

```yaml
---
type: security-scan
target: "{scanned_path}"
date: "{YYYY-MM-DD}"
commit: "{current_HEAD_short_hash}"
focus: "{focus_area}"
risk_level: "{Critical | High | Medium | Low}"
files_scanned: {n}
vulnerabilities:
  critical: {n}
  high: {n}
  medium: {n}
  low: {n}
secrets_found: {n}
owasp_compliance:
  A01: "{pass | fail | warning}"
  A02: "{pass | fail | warning}"
  A03: "{pass | fail | warning}"
  A04: "{pass | fail | warning}"
  A05: "{pass | fail | warning}"
  A06: "{pass | fail | warning}"
  A07: "{pass | fail | warning}"
  A08: "{pass | fail | warning}"
  A09: "{pass | fail | warning}"
  A10: "{pass | fail | warning}"
---
```

## Report Body

```markdown
# Security Scan Report: {project_path}

**Report saved to:** `.reports/security-scans/{filename}.md`

## Executive Summary
**Scan Date:** {date}
**Commit:** `{short_hash}`
**Files Scanned:** {count}
**Risk Level:** Critical | High | Medium | Low

| Severity | Count |
|----------|-------|
| Critical | {n} |
| High | {n} |
| Medium | {n} |
| Low | {n} |

## Critical Vulnerabilities

### VULN-{N}: {Title}
**CWE:** CWE-{id} ({name})
**CVSS:** {score} (Critical)
**OWASP:** {category}
**File:** `{path}:{line}`

**Vulnerable Code:**
```{lang}
{code}
```

**Attack Vector:**
{How it can be exploited}

**Impact:**
{Consequences}

**Remediation:**
```{lang}
{secure code}
```

**References:**
- https://cwe.mitre.org/data/definitions/{id}.html

---

## High Severity Issues
{Same format}

## Medium Severity Issues
{Reduced detail}

## Low Severity Issues
{Summary format}

---

## OWASP Top 10 Compliance

| Category | Status | Issues |
|----------|--------|--------|
| A01: Broken Access Control | {status} | {n} |
| A02: Cryptographic Failures | {status} | {n} |
| A03: Injection | {status} | {n} |
| A04: Insecure Design | {status} | {n} |
| A05: Security Misconfiguration | {status} | {n} |
| A06: Vulnerable Components | {status} | {n} |
| A07: Auth Failures | {status} | {n} |
| A08: Integrity Failures | {status} | {n} |
| A09: Logging Failures | {status} | {n} |
| A10: SSRF | {status} | {n} |

---

## Secrets Found

| Type | File | Line | Status |
|------|------|------|--------|
| {type} | {file} | {line} | Exposed |

**Immediate Actions:**
1. Rotate all exposed credentials
2. Add files to `.gitignore`
3. Use environment variables or secrets manager

---

## Dependency Vulnerabilities

| Package | Version | CVE | Severity | Fixed In |
|---------|---------|-----|----------|----------|
| {pkg} | {ver} | {cve} | {sev} | {fix_ver} |
```
