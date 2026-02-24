# Per-Folder Document Templates

## .context/CONTEXT.md Template

```markdown
<!-- AUTO-GENERATED: Header -->
# {Folder Name} — Module Context
**Version**: {commit_hash}
**Generated**: {timestamp}
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: File Inventory -->
## File Inventory

> Complete map of every file in this module. AI agents should use this instead of scanning the filesystem.

| File | Role | Key Exports / Responsibility |
|------|------|------------------------------|
| `{file_path}` | {Entry point / Service / Model / Config / Test / Util / Type / Route / Middleware / ...} | {Brief: what it exports or does, e.g., "Exports `UserService` class — handles CRUD + password hashing"} |
| `{file_path}` | {role} | {description} |

**File count**: {N} files
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Architecture -->
## Architectural Mental Model

### Core Responsibility
{Deep explanation — not "Handles logic", but "Manages the state machine for user onboarding, enforcing valid transitions and persisting side-effects to the DB".}

### Design Patterns
- **{Pattern}**: {Usage context, e.g., "Singleton for DB connection to ensure pool limit"}

### Data Flow
1. Input enters via `{entry_point}`
2. Validated by `{validator}`
3. Transformed by `{transformer}`
4. Persisted via `{repository}`
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Type System -->
## Type Definitions / Models

> Only exported or critical types.

```{language}
{type definitions with inline comments on constraints}
```
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: API -->
## Public Interfaces

### `{Service.method(arg)}`
- **Input**: `{Type}`
- **Output**: `{Type}`
- **Behavior**: {validation, errors, side-effects}
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Dependencies -->
## Dependencies

- **Internal**: [{Module}](../../{module}/.context/CONTEXT.md) — {purpose}
- **External**: `{package}` — {purpose}
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Backend (include only for backend/API modules) -->
## Backend Details

### API Surface
| Method | Path | Auth | Request Body | Response | Errors |
|--------|------|------|-------------|----------|--------|
| `{GET/POST/...}` | `{/api/path}` | {required/public/role} | `{schema or N/A}` | `{response shape}` | `{error codes}` |

### Database / ORM
- **Tables / Collections owned**: {list with key columns/fields}
- **Relationships**: {foreign keys, joins, references to other modules' tables}
- **Migrations**: `{path to migrations}` — {strategy: auto-generated / hand-written}
- **Query Patterns**: {raw SQL / ORM queries / repository pattern / query builder}

### Middleware / Request Pipeline
1. {Auth middleware} — {what it does}
2. {Validation} — {schema validation approach}
3. {Rate limiting} — {if applicable}
4. {Error handler} — {catch-all error formatting}

### Background Jobs
| Job / Worker | Trigger | Side-Effects |
|-------------|---------|-------------|
| `{job_name}` | {cron / queue / event} | {what it does} |

### External Integrations
| Service | Purpose | Retry Strategy | Timeout |
|---------|---------|---------------|---------|
| `{service}` | {why it's called} | {retry count / backoff} | `{ms}` |

### Caching
- **Layer**: {Redis / in-memory / CDN / ...}
- **Cached**: {what data, e.g., "user sessions, product catalog"}
- **TTL**: {expiration strategy}
- **Invalidation**: {event-driven / time-based / manual}
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Frontend (include only for frontend/UI modules) -->
## Frontend Details

### Component Catalog
| Component | Props / Slots | Variants | Used In |
|-----------|--------------|----------|---------|
| `{ComponentName}` | `{key props with types}` | {variants, e.g., "primary, secondary, ghost"} | {parent components or pages} |

### Design Tokens / Theme
- **Source**: `{path to theme/tokens file}`
- **Colors**: {primary, secondary, semantic colors}
- **Spacing**: {scale system, e.g., "4px base, 8/12/16/24/32/48"}
- **Typography**: {font families, scale}
- **Breakpoints**: {sm/md/lg/xl values}

### State Management
- **Library**: {Redux / Zustand / Context / Pinia / NgRx / signals / ...}
- **Store Structure**: {key slices or stores and what they hold}
- **Key Selectors / Actions**: {most-used state accessors and mutators}

### Routing
| Route | Component | Guard / Middleware | Lazy Loaded |
|-------|-----------|-------------------|-------------|
| `{path}` | `{Component}` | {auth guard, role check, etc.} | {yes/no} |

### Styling Approach
- **Method**: {CSS Modules / Tailwind / styled-components / SCSS / ...}
- **Conventions**: {naming patterns, e.g., "BEM for class names", "co-located .module.css files"}
- **Global Styles**: `{path to global stylesheet}`

### Reusable vs. Page Components
- **Shared/Generic**: {list of components designed for reuse across features}
- **Page-Specific**: {list of components tied to a single page/feature}

### Assets
- **Icons**: {icon system — SVG sprites, icon font, react-icons, etc.} at `{path}`
- **Images**: `{path}` — {handling: optimized, lazy-loaded, CDN, etc.}
- **Fonts**: {self-hosted / Google Fonts / etc.} loaded via `{mechanism}`

### Accessibility (a11y)
- **ARIA Patterns**: {patterns used, e.g., "role=dialog for modals, aria-live for toasts"}
- **Keyboard Navigation**: {tab order strategy, focus traps, shortcut keys}
- **Screen Reader**: {announcements, skip links, landmark roles}
<!-- END AUTO-GENERATED -->

<!-- CUSTOM SECTION: Insights -->
## Developer Insights
{Manual notes — preserved across regeneration}
<!-- END CUSTOM SECTION -->
```

## .context/OVERVIEW.md Template

```markdown
<!-- AUTO-GENERATED: Header -->
# {Folder Name}
> {One-line summary}
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Business Context -->
## Business Context

### Problem Statement
{What real-world problem does this module solve? Who are the end-users or stakeholders? E.g., "This module handles invoice reconciliation for finance teams, ensuring payments match purchase orders within configurable tolerance thresholds."}

### Business Rules
{Key domain rules encoded in this module. E.g., "An order cannot be fulfilled if inventory < requested quantity. Partial fulfillment requires manager approval."}

### Domain Terminology
| Term | Meaning |
|------|---------|
| `{Term}` | {Definition in plain language, clarifying any ambiguity with programming terms} |
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Purpose -->
## Purpose & Motivation

### Why This Module Exists
{The architectural or domain need that led to its creation. What would break or be missing without it.}

### User Stories / Use Cases
- **{Scenario}**: When {trigger}, the system {action} so that {outcome}
- **{Scenario}**: When {trigger}, the system {action} so that {outcome}

### Key Design Decisions
| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| {decision} | {why this was chosen} | {what else was evaluated} |
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Overview -->
## Overview
{Human-readable explanation with analogies. Explain the "Why" and the "How" at a conceptual level. E.g., "Think of this module as a post office — it receives messages (requests), sorts them by type, routes them to the right handler, and sends back a receipt (response)."}
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Usage -->
## Usage

### Setup
```bash
{installation commands if applicable}
```

### Example
```{language}
{Real, runnable example}
```
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: API Reference -->
## API Summary

| Method | Description |
|--------|-------------|
| `{method}` | {description} |
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Backend Guide (include only for backend/API modules) -->
## Backend Guide

### Request Lifecycle
1. Request arrives at `{entry point}`
2. Passes through middleware: {list}
3. Routed to `{handler/controller}`
4. Business logic in `{service}`
5. Data access via `{repository/ORM}`
6. Response formatted and returned

### Data Model
```
{Entity relationships — Mermaid ER diagram or simple table}
```

### Error Handling
- **Standard Error Format**: `{shape, e.g., { code, message, details }}`
- **Propagation**: {how errors bubble up — exceptions / Result types / error codes}
- **Common Scenarios**: {list of expected error cases and how they're handled}

### Environment & Config
| Variable / Config Key | Purpose | Default | Required |
|----------------------|---------|---------|----------|
| `{VAR_NAME}` | {what it controls} | `{default}` | {yes/no} |
<!-- END AUTO-GENERATED -->

<!-- AUTO-GENERATED: Frontend Guide (include only for frontend/UI modules) -->
## Visual Guide

### What the User Sees
{Describe the screens, layouts, and key visual elements. Reference Storybook, Figma, or design files if they exist.}

### Component Hierarchy
```
{PageComponent}
├── {Header}
│   ├── {Logo}
│   └── {NavMenu}
├── {MainContent}
│   ├── {FeatureWidget}
│   └── {DataTable}
└── {Footer}
```

### User Interaction Flows
1. **{Flow Name}**: User clicks {X} → `{Component}` renders → API call to `{endpoint}` → state updates in `{store}` → UI re-renders with {result}

### Responsive Behavior
| Breakpoint | Layout Change |
|------------|--------------|
| `< {sm}` | {mobile layout description} |
| `{sm} - {md}` | {tablet layout description} |
| `> {lg}` | {desktop layout description} |

### Using Shared Components
```{language}
{Import and usage example for key reusable components with props}
```
<!-- END AUTO-GENERATED -->

<!-- CUSTOM SECTION: Troubleshooting -->
## Troubleshooting
{Manual section — preserved across regeneration}
<!-- END CUSTOM SECTION -->
```

## .context/metadata.json Structure

```json
{
  "version": "1.1",
  "last_commit": "{current_HEAD_hash}",
  "generated_at": "{ISO timestamp}",
  "context_files": ["CONTEXT.md", "OVERVIEW.md"],
  "source_files": {
    "total": 15,
    "files": [
      "index.ts",
      "service.ts",
      "models.ts",
      "routes.ts",
      "...all source files in module"
    ]
  },
  "history": [
    {
      "commit": "{current_HEAD_hash}",
      "timestamp": "{ISO timestamp}",
      "action": "updated",
      "changed_source_files": ["service.ts", "models.ts"],
      "context_files_modified": ["CONTEXT.md"],
      "summary": "Updated API surface — added createUser method, updated User model with email field"
    },
    {
      "commit": "{previous_HEAD_hash}",
      "timestamp": "{ISO timestamp}",
      "action": "generated",
      "changed_source_files": [],
      "context_files_modified": ["CONTEXT.md", "OVERVIEW.md"],
      "summary": "Initial generation"
    }
  ]
}
```

**Notes:**
- `last_commit` and `generated_at` always reflect the most recent run (used by staleness check)
- `source_files.files` must list **every** source file the context covers — this is cross-checked during staleness detection to catch added/deleted files
- `history` is append-to-front (newest first), capped at 50 entries to prevent unbounded growth
- `action` is `"generated"` for first run, `"updated"` for subsequent runs
- `summary` is a one-line human-readable description of what changed
