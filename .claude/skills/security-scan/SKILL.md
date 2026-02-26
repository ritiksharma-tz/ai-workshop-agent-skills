---
name: security-scan
description: Comprehensive security vulnerability scanner covering OWASP Top 10 (2021), hardcoded secrets, dependency CVEs, and insecure code patterns. Use when asked to check for security issues, find vulnerabilities, audit security, scan for secrets, or perform a security assessment of a codebase.
---

# Security Scan

Perform a systematic security audit of the target codebase and save the report as a persistent document artifact.

## Output Structure

```
.reports/
├── security-scans/
│   └── {YYYY-MM-DD}-{target-slug}.md    # Full security scan report
└── metadata.json                          # Report tracking
```

## Execution

### Phase 1: Reconnaissance

1. Identify attack surface: web endpoints (REST, GraphQL, WebSocket), CLI entry points, background workers, DB access, external integrations
2. Locate security configs: `.env` files, security headers, CSP, CORS, auth setup
3. Identify dependency files: `requirements.txt`, `package.json`, `go.mod`, `pom.xml`, etc.

### Phase 2: OWASP Top 10 (2021) Systematic Check

Check each category systematically. For detailed detection patterns with vulnerable/secure code examples, see [references/owasp-patterns.md](references/owasp-patterns.md).

| ID | Category | Key Checks |
|----|----------|------------|
| A01 | Broken Access Control | Missing auth/authz, IDOR, CORS misconfiguration, path traversal |
| A02 | Cryptographic Failures | Weak algorithms (MD5/SHA1 for passwords), hardcoded keys, missing TLS, PII in plaintext |
| A03 | Injection | SQL, NoSQL, command, LDAP, template (SSTI), log injection |
| A04 | Insecure Design | Missing rate limiting, no account lockout, predictable IDs, trust boundary violations |
| A05 | Security Misconfiguration | Debug mode in prod, default creds, missing security headers, verbose errors |
| A06 | Vulnerable Components | Known CVEs, outdated frameworks, unmaintained dependencies, missing lock files |
| A07 | Auth Failures | Weak passwords, missing MFA, session fixation, weak JWT config |
| A08 | Integrity Failures | Insecure deserialization (pickle, yaml.load), missing integrity checks |
| A09 | Logging Failures | Missing auth event logging, sensitive data in logs, no alerting |
| A10 | SSRF | User-controlled URLs, missing URL validation, cloud metadata exposure |

### Phase 3: Secret Detection

Scan for hardcoded secrets using patterns in [references/secret-patterns.md](references/secret-patterns.md). Categories: API keys, AWS/GCP/GitHub/Stripe/Slack credentials, JWT tokens, private keys, database URLs, generic passwords.

### Phase 4: Report

Use the output template in [references/output-template.md](references/output-template.md).

Each vulnerability must include: CWE ID, CVSS score, OWASP category, file:line, vulnerable code, attack vector, impact, and remediation with secure code.

### Phase 5: Save Artifact

**MANDATORY: Always save the full security scan report as a document artifact.**

1. Create `.reports/security-scans/` directory if it doesn't exist
2. Generate filename: `{YYYY-MM-DD}-{target-slug}.md` (e.g., `2025-03-15-src-api.md`)
3. Write the full report with YAML frontmatter metadata:

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

4. Write the full security scan report body after the frontmatter
5. Update `.reports/metadata.json` — merge this report entry into the `reports` array:

```json
{
  "reports": [
    {
      "type": "security-scan",
      "file": "security-scans/{filename}.md",
      "target": "{path}",
      "date": "{ISO timestamp}",
      "commit": "{hash}",
      "risk_level": "{Critical | High | Medium | Low}",
      "vulnerabilities": { "critical": 0, "high": 1, "medium": 3, "low": 2 },
      "secrets_found": 0
    }
  ]
}
```

6. Display to the user: the executive summary + the file path where the full report was saved
7. If `--fail-on` threshold is met, clearly indicate FAIL status in both the artifact and conversation output

**If `--no-artifact` is passed, skip artifact generation and only display to conversation.**

## Large Codebases

Prioritize by risk: auth/authz code → external-facing endpoints → data access layers → config files. Save progress to checkpoint JSON.

## Arguments

- `$1` — Path to scan
- `--focus` — `injection`, `secrets`, `auth`, `owasp`, `dependencies`, or `all`
- `--fail-on` — Exit with error if severity found: `critical`, `high`, `medium`
- `--continue` — Resume from checkpoint
- `--exclude` — Glob patterns to exclude
- `--no-artifact` — Skip saving report as document (display only)
