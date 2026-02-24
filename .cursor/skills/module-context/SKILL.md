---
name: module-context
description: Generate and keep up-to-date deep, inter-linked CONTEXT.md (AI/agent context) and OVERVIEW.md (human-readable guide) inside a `.context/` folder within each code module. Detects stale docs via git diff and updates only what changed. Use when documenting a specific module/folder, updating documentation after code changes, creating AI/agent context for a component, or when asked to generate per-folder documentation.
---

# Per-Folder Documentation

Generate and maintain a `.context/` folder inside the target module containing `CONTEXT.md` (AI/agent reference) and `OVERVIEW.md` (human-readable developer guide). The CONTEXT.md should make re-reading the source code unnecessary.

## Output Structure

```
<module>/
├── .context/
│   ├── CONTEXT.md       # AI/agent context — replaces need to read source
│   ├── OVERVIEW.md      # Human-readable module guide
│   └── metadata.json    # Version tracking for staleness detection
├── src files...
└── ...
```

## Execution

### Phase 0: Staleness Check

Always run this first — avoid unnecessary regeneration.

1. Read `.context/metadata.json` inside the target folder (read `last_commit` from the top-level field)
2. Compare stored `last_commit` hash against current state: `git diff --name-only {stored_hash} HEAD -- {target_folder}`
3. **If no changes detected** and `--force` not passed, report "docs are up to date" and stop
4. **If changes detected**, note which files changed — use this to scope the analysis in Phase 1 (focus on changed files but re-read dependencies if interfaces changed)
5. Cross-check `source_files.files` against actual files on disk — if files were added or deleted, mark as changed even if git diff is clean (handles rebased/squashed history)
6. Capture current commit hash for metadata update at the end

### Phase 1: Deep Analysis

Read the code — do not guess.

1. **Enumerate all files** in the module directory (recursively). Every file must appear in the file inventory — no file should be undocumented.
2. Map the folder structure, identify entry points, core logic, types/models
3. Read all interface/type definitions, complex business logic, and trace imports
4. Synthesize: core entities, public API (inputs/outputs/side-effects), internal state management, gotchas/edge cases

**For updates (docs already exist):** Read the existing `.context/CONTEXT.md` and `.context/OVERVIEW.md` first. Focus analysis on changed files but verify that unchanged sections are still accurate (e.g., a renamed function breaks the existing API table).

### Phase 2: Generate or Update Documents

Create `.context/` directory inside the target folder if missing. Use templates in [references/templates.md](references/templates.md).

**`.context/CONTEXT.md`** — replaces the need to read source code:
- **Complete file inventory**: Every file in the module listed with its role, responsibility, and key exports — so an AI agent has a full map of the module without scanning the filesystem
- Architectural mental model with design patterns
- Data flow description
- Critical type definitions (exported/critical types only)
- Public interfaces with inputs, outputs, behavior, side-effects
- Internal and external dependency links to other modules' `.context/CONTEXT.md` files

**`.context/OVERVIEW.md`** — human-readable developer guide:
- **Business Context**: What real-world problem this module solves, who the end-users/stakeholders are, and what business rules it encodes
- **Purpose & Motivation**: Why this module exists — the domain need, the architectural decision that led to its creation, and what would break without it
- **Domain Terminology**: Glossary of domain-specific terms used in the code (e.g., "A `Claim` represents a user-submitted reimbursement request, not a JWT claim")
- **User Stories / Use Cases**: Key scenarios this module supports, written as "When X happens, the system does Y so that Z"
- **Decision Log**: Why key design choices were made (e.g., "We use event sourcing here because audit trail is a regulatory requirement")
- Overview with analogies and "why"
- Setup and usage examples (real, runnable code)
- API summary table
- Troubleshooting section (preserved across updates via `CUSTOM SECTION` markers)

**Update behavior (when docs already exist):**
- Read existing documents first
- **Preserve** `<!-- CUSTOM SECTION -->` blocks — these contain manual notes that must survive regeneration
- **Update** `<!-- AUTO-GENERATED -->` blocks with current codebase state
- **Add** new sections for new public interfaces, types, or dependencies
- **Remove** sections for deleted interfaces or types (don't leave stale references)
- Verify all dependency links still point to valid `.context/CONTEXT.md` files

### Phase 3: Metadata Update

Write `.context/metadata.json` inside the target folder. The metadata tracks a **history of every generation run** so changes to the context can be traced per commit.

```json
{
  "version": "1.1",
  "last_commit": "{current_HEAD_hash}",
  "generated_at": "{ISO timestamp}",
  "context_files": ["CONTEXT.md", "OVERVIEW.md"],
  "source_files": {
    "total": 15,
    "files": ["service.py", "models.py", "routes.py", "...all files in module"]
  },
  "history": [
    {
      "commit": "{current_HEAD_hash}",
      "timestamp": "{ISO timestamp}",
      "action": "updated",
      "changed_source_files": ["service.py", "models.py"],
      "context_files_modified": ["CONTEXT.md"],
      "summary": "Updated API surface — added POST /users endpoint, updated UserService interface"
    },
    {
      "commit": "{previous_hash}",
      "timestamp": "{ISO timestamp}",
      "action": "generated",
      "changed_source_files": [],
      "context_files_modified": ["CONTEXT.md", "OVERVIEW.md"],
      "summary": "Initial generation"
    }
  ]
}
```

**Fields:**
- `last_commit` / `generated_at` — latest run info (used by staleness check)
- `context_files` — list of `.context/` files managed by this skill
- `source_files.total` — count of source files in the module
- `source_files.files` — complete list of all source files the context covers (so agents can verify completeness)
- `history[]` — array of generation runs, newest first. Each entry records:
  - `commit` — the HEAD hash at time of run
  - `action` — `"generated"` (first run) or `"updated"` (subsequent runs)
  - `changed_source_files` — source files that triggered this regeneration
  - `context_files_modified` — which context docs were actually changed
  - `summary` — brief description of what changed in this update

## Quality Rules

- Never use: "Contains logic", "Standard implementation", "Helper functions"
- **Utility files** (e.g., `utils.py`, `helpers.go`, `StringUtils.java`, `utils.ts`): list every function and what it solves
- **Type/model files** (e.g., `models.py`, `types.ts`, `entities.rs`, `Models.cs`): paste the core schemas/structs with field constraints
- **API/controller files** (e.g., `views.py`, `controller.go`, `api.ts`, `Controller.java`): explain the error handling strategy, auth requirements, and response shapes
- **Config files** (e.g., `settings.py`, `config.yaml`, `application.properties`): document every config key and its effect

## Module Type Strategies

> The skill auto-detects the module type and includes the relevant extra sections. Multiple strategies can apply (e.g., a full-stack module gets both backend and frontend sections).

### Backend / API Module Strategy

When the target module is a backend/API module, additionally document:

**In CONTEXT.md:**
- **API Surface**: Every endpoint/RPC method with HTTP method, path, auth requirement, request/response shapes, and error codes
- **Database / ORM**: Tables/collections owned by this module, relationships, migrations strategy, query patterns
- **Middleware / Interceptors**: Request pipeline — auth, validation, logging, rate limiting, error handling order
- **Background Jobs / Workers**: Scheduled tasks, queue consumers, cron jobs with their triggers and side-effects
- **External Service Integrations**: Third-party APIs called, retry/timeout strategy, circuit breaker patterns
- **Caching Strategy**: What's cached, TTLs, invalidation approach, cache layer (Redis, in-memory, CDN)

**In OVERVIEW.md:**
- **Request Lifecycle**: Step-by-step trace of a request from entry to response
- **Data Model Diagram**: Entity relationships (can be Mermaid ER diagram or table)
- **Error Handling Guide**: How errors propagate, standard error response format, common error scenarios
- **Environment / Config**: Required env vars, feature flags, config files and what they control

**Detection:**
Detect backend modules by: route/controller definitions, ORM/database imports, middleware chains, API framework usage (Express, FastAPI, Spring, Gin, ASP.NET, Rails, Django, Phoenix, etc.), presence of `migrations/`, `models/`, `controllers/`, `routes/`, `handlers/`, `services/` directories.

### Frontend Module Strategy

When the target module is a frontend/UI module, additionally document:

### In CONTEXT.md:
- **Component Catalog**: Every component with its props/slots interface, variants, and where it's used
- **Design Tokens / Theme**: Colors, spacing, typography, breakpoints — reference the design system source file
- **State Management**: What state library is used (Redux, Zustand, Context, signals, etc.), store structure, key selectors/actions
- **Routing**: Route definitions, guards/middleware, lazy-loaded chunks
- **Styling Approach**: CSS modules / Tailwind / styled-components / SCSS — conventions and naming patterns
- **Reusable Components vs. Page Components**: Clearly separate shared/generic components from page-specific ones
- **Asset Handling**: Icons, images, fonts — where they live and how they're imported
- **Accessibility (a11y)**: ARIA patterns used, keyboard navigation support, screen reader considerations

### In OVERVIEW.md:
- **Visual Guide**: Describe what the user sees — screens, layouts, interactions (reference Storybook/design files if they exist)
- **Component Hierarchy**: Parent → child composition tree for key pages
- **User Interaction Flows**: Step-by-step "user clicks X → component Y renders → API call Z fires → state updates → UI re-renders"
- **Responsive Behavior**: How layouts adapt across breakpoints
- **Reusable Component Usage**: How to import and use shared components with prop examples

### Detection:
Detect frontend modules by the presence of: `.tsx`/`.jsx`/`.vue`/`.svelte` files, `components/` or `pages/` directories, CSS/SCSS modules, UI framework config files (`next.config`, `vite.config`, `nuxt.config`, `angular.json`, etc.).

## Large Project Strategy

Document in order: leaf nodes (utils, models) → business logic → API controllers. For frontend: design tokens/theme → shared components → feature components → pages/views.

## Arguments

- `$1` — Target directory
- `--force` — Regenerate all docs regardless of staleness check
- `--recursive` — Document all subfolders
- `--deep` — Full-file reading mode (recommended for first run)
