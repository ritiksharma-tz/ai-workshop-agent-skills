# QA Feature Documentation Templates

## FEATURE.md Template

```markdown
# {Feature Name}

> Last updated: {YYYY-MM-DD} | Commit: {7-char hash}

## Business Value

{Specific business problem this solves. Not generic "improves UX" but concrete
outcomes like "reduces password reset support tickets by enabling self-service"}

## Feature Summary

{2-3 sentences describing what the feature does from user perspective}

## User Stories

- As a {role}, I want to {action} so that {benefit}
- As a {role}, I want to {action} so that {benefit}

## Acceptance Criteria

- [ ] {Specific, testable criterion}
- [ ] {Specific, testable criterion}
- [ ] {Specific, testable criterion}

## Dependencies

- **Features:** {Features this depends on, e.g., "User Authentication"}
- **External Services:** {Third-party APIs, payment processors, etc.}
- **Data:** {Required data state, e.g., "User must have verified email"}

## Related Modules

| Module | Role | Context Link |
|--------|------|--------------|
| {path} | {responsibility} | [CONTEXT.md]({relative-path}) |
```

---

## SCOPE.md Template

```markdown
# {Feature Name} — Test Scope

## In Scope

### Must Test (P0)
- {Critical user path}
- {Core functionality}
- {Security-sensitive operation}

### Should Test (P1)
- {Secondary scenario}
- {Common edge case}

### Could Test (P2)
- {Rare edge case}
- {Performance under load}

## Out of Scope

- {Explicitly excluded scenarios}
- {Adjacent feature boundaries}
- {Infrastructure concerns tested elsewhere}

## Test Environment Requirements

| Requirement | Details |
|-------------|---------|
| Auth State | {e.g., "Logged in as admin"} |
| Test Data | {e.g., "User with 3+ orders"} |
| Services | {e.g., "Payment gateway in sandbox"} |
| Feature Flags | {e.g., "new_checkout=enabled"} |

## Risk Areas

| Area | Risk | Reason | Mitigation |
|------|------|--------|------------|
| {Component} | High | {Why risky} | {Extra test coverage} |
| {Integration} | Medium | {Why risky} | {Mock strategy} |

## Coverage Targets

| Category | Target | Notes |
|----------|--------|-------|
| Happy path | 100% | All primary flows |
| Error handling | 80% | All user-facing errors |
| Edge cases | 60% | Based on risk assessment |
| Integration | 70% | With mocked externals |
```

---

## FLOWS.md Template

```markdown
# {Feature Name} — User Flows

## Flow: {Primary Flow Name}

### Preconditions
- {Required state 1}
- {Required state 2}

### Steps

| Step | User Action | Input | Expected Result |
|------|-------------|-------|-----------------|
| 1 | {Action} | {Data} | {Response} |
| 2 | {Action} | {Data} | {Response} |
| 3 | {Action} | {Data} | {Response} |

### Postconditions
- {Resulting state 1}
- {Resulting state 2}

### Automation Notes
- {Selector hints}
- {Wait conditions}
- {Data cleanup}

---

## Flow: {Alternative Flow Name}

{Same structure as above}

---

## Flow: {Error Flow Name}

### Trigger
{What condition causes this error path}

### Steps

| Step | User Action | Input | Expected Error |
|------|-------------|-------|----------------|
| 1 | {Action} | {Invalid data} | {Error message/code} |

### Recovery Path
{How user recovers — retry, redirect, etc.}

---

## Test Scenario Matrix

| ID | Scenario | Flow | Priority | Preconditions | Key Assertions |
|----|----------|------|----------|---------------|----------------|
| TC-{FTR}-001 | {Name} | Primary | P0 | {State} | {What to verify} |
| TC-{FTR}-002 | {Name} | Alt | P1 | {State} | {What to verify} |
| TC-{FTR}-003 | {Name} | Error | P1 | {State} | {What to verify} |

<!-- QA CUSTOM -->
## Additional Scenarios (QA-Added)

{QA team can add custom scenarios here — preserved across regeneration}

<!-- /QA CUSTOM -->
```

---

## TECHNICAL.md Template

```markdown
# {Feature Name} — Technical Specifications

## API Endpoints

### {Operation Name}

| Property | Value |
|----------|-------|
| Method | `{GET/POST/PUT/PATCH/DELETE}` |
| Path | `{/api/v1/resource/:id}` |
| Auth | `{Bearer token / API key / None}` |
| Rate Limit | `{X requests/minute}` |

**Request Headers:**
```
Authorization: Bearer {token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "field_name": "string — description (required)",
  "optional_field": "number — description (optional, default: 0)"
}
```

**Response — 200 OK:**
```json
{
  "id": "string — resource identifier",
  "created_at": "string — ISO 8601 timestamp",
  "data": {}
}
```

**Error Responses:**

| Status | Code | Message | Cause |
|--------|------|---------|-------|
| 400 | `VALIDATION_ERROR` | "Email is required" | Missing field |
| 401 | `UNAUTHORIZED` | "Invalid token" | Expired/invalid auth |
| 404 | `NOT_FOUND` | "Resource not found" | Invalid ID |
| 409 | `CONFLICT` | "Email already exists" | Duplicate |
| 422 | `UNPROCESSABLE` | "Invalid email format" | Bad format |

---

## Database

### Tables Affected

| Table | Operation | Fields |
|-------|-----------|--------|
| `{table}` | INSERT/UPDATE/DELETE | `{field1}`, `{field2}` |

### Verification Queries

```sql
-- Verify record created
SELECT id, status, created_at
FROM {table}
WHERE {condition};

-- Verify state change
SELECT * FROM {table} WHERE id = :id AND status = 'expected';
```

---

## UI Elements

### Page: {Page Name}

| Element | Selector | Type | Actions |
|---------|----------|------|---------|
| {Name} | `[data-testid="{id}"]` | Button | click |
| {Name} | `#email-input` | Input | type, clear |
| {Name} | `.error-message` | Text | assertVisible, getText |

### Wait Conditions
- After submit: Wait for `[data-testid="success-toast"]`
- Loading: Wait for `.spinner` to disappear
- Navigation: Wait for URL to match `/dashboard`

---

## Integration Points

| Service | Protocol | Purpose | Mock Strategy |
|---------|----------|---------|---------------|
| {Service} | REST | {Purpose} | Intercept `/api/external/*` |
| {Service} | WebSocket | {Purpose} | Mock server on port XXXX |
| {Service} | Queue | {Purpose} | Use test queue prefix |

---

## Test Data

### Factory: Valid {Entity}

```json
{
  "email": "test+{{$randomUUID}}@example.com",
  "password": "Test@123456",
  "name": "Test User {{$timestamp}}"
}
```

### Factory: Invalid Cases

```json
// Empty required field
{ "email": "", "password": "valid" }

// Invalid format
{ "email": "not-an-email", "password": "valid" }

// Too short
{ "email": "a@b.co", "password": "123" }

// SQL injection attempt
{ "email": "test@test.com'; DROP TABLE users;--", "password": "valid" }

// XSS attempt
{ "email": "<script>alert('xss')</script>@test.com", "password": "valid" }
```

### Fixtures

| Fixture | Purpose | Setup |
|---------|---------|-------|
| `user_with_orders` | Test order history | Create user + 3 orders |
| `expired_session` | Test session timeout | Create session with past expiry |

<!-- QA CUSTOM -->
## Custom Test Data (QA-Added)

{QA team can add project-specific test data here}

<!-- /QA CUSTOM -->
```

---

## CHANGELOG.md Template

```markdown
# QA Feature Changelog

Track feature changes to maintain automation scripts.

---

## [{YYYY-MM-DD}] — Commit: {full 40-char hash}

### ✨ Added
- **{Feature Name}**
  - {What was added}
  - Docs: [`features/{slug}/`](./features/{slug}/FEATURE.md)
  - Modules: `{paths}`

### 🔄 Modified
- **{Feature Name}**
  - Change: {What changed}
  - Files: `{changed files}`
  - Impact: {How existing tests are affected}
  - **Action Required:** {What QA must do}

### 🗑️ Removed
- **{Feature Name}**
  - Reason: {Why deprecated/removed}
  - **Action Required:** Remove automation in `{test paths}`

### 📝 Docs Only
- **{Feature Name}** — {Clarification that doesn't affect tests}

---
```

---

## _index.md Template

```markdown
# Feature Catalog

> Last updated: {YYYY-MM-DD} | Commit: {hash}

## Status Legend
- ✅ Automation Complete
- 🔄 Automation In Progress
- ❌ Automation Not Started
- ⏸️ Automation Skipped (deprecated/low priority)

## Features

| Feature | Status | Priority | Automation | Last Updated |
|---------|--------|----------|------------|--------------|
| [{Name}](./{slug}/FEATURE.md) | Active | P0 | ✅ | {date} |
| [{Name}](./{slug}/FEATURE.md) | Active | P1 | 🔄 | {date} |
| [{Name}](./{slug}/FEATURE.md) | Deprecated | P2 | ⏸️ | {date} |

## By Domain

### {Domain 1}
- [{Feature}](./{slug}/FEATURE.md) — {one-line description}
- [{Feature}](./{slug}/FEATURE.md) — {one-line description}

### {Domain 2}
- [{Feature}](./{slug}/FEATURE.md) — {one-line description}

## Quick Links

- [Changelog](../CHANGELOG.md)
- [Project Context](../../.context/CONTEXT.md)
- [Architecture](../../.context/ARCHITECTURE.md)
```

---

## metadata.json Template

```json
{
  "version": "1.0",
  "last_commit": "{40-char hash}",
  "last_commit_date": "{ISO 8601}",
  "generated_at": "{ISO 8601}",
  "feature_count": 0,
  "features": {
    "{slug}": {
      "status": "active|deprecated|removed",
      "created_at": "{ISO 8601}",
      "updated_at": "{ISO 8601}",
      "files": ["FEATURE.md", "SCOPE.md", "FLOWS.md", "TECHNICAL.md"]
    }
  },
  "last_run": {
    "added": [],
    "modified": [],
    "removed": []
  }
}
```
