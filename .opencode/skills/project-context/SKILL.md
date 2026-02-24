---
name: project-context
description: Generate and keep up-to-date project-level "Source of Truth" documentation inside a `.context/` folder — CONTEXT.md (AI/agent system context), ARCHITECTURE.md (system blueprint with diagrams), and the root README.md. Detects stale docs via git diff and updates only what changed. Use when initializing AI context for a project, onboarding new contributors, creating project documentation, updating project docs after changes, or when asked to document the overall project structure and architecture.
---

# Project Documentation

Generate and maintain project-level documentation inside `.context/` at the repo root, plus keep the root `README.md` in sync with the codebase.

## Output Structure

```
<project-root>/
├── .context/
│   ├── CONTEXT.md        # AI/agent system context (agent-agnostic)
│   ├── ARCHITECTURE.md   # System blueprint with diagrams
│   └── metadata.json     # Version tracking for staleness detection
└── README.md             # Human onboarding
```

## Execution

### Phase 0: Staleness Check

Always run this first — avoid unnecessary regeneration.

1. Read `.context/metadata.json` if it exists (read `last_commit` from the top-level field)
2. Compare stored `last_commit` hash against current HEAD: `git diff --name-only {stored_hash} HEAD`
3. **If no changes detected** and `--force` not passed, report "docs are up to date" and stop
4. **If changes detected**, note which top-level directories/files changed — use this to scope updates in Phase 2
5. Cross-check `modules_documented` and `modules_pending` against actual directories on disk — if new modules appeared or old ones were removed, mark as changed
6. Capture current commit hash for metadata update at the end

### Phase 1: Reconnaissance

1. Identify build system, language, database, and entry points from config files. Look for:
   - **JavaScript/TypeScript**: `package.json`, `tsconfig.json`, `next.config.*`, `vite.config.*`, `angular.json`
   - **Python**: `pyproject.toml`, `setup.py`, `setup.cfg`, `requirements.txt`, `Pipfile`, `poetry.lock`
   - **Java/Kotlin**: `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle`
   - **Go**: `go.mod`, `go.sum`
   - **Rust**: `Cargo.toml`, `Cargo.lock`
   - **C# / .NET**: `*.csproj`, `*.sln`, `Directory.Build.props`, `nuget.config`
   - **Ruby**: `Gemfile`, `*.gemspec`, `Rakefile`
   - **PHP**: `composer.json`
   - **Swift**: `Package.swift`, `*.xcodeproj`
   - **Infrastructure**: `Dockerfile`, `docker-compose.yml`, `Makefile`, `Terraform (*.tf)`, `helm/`, `k8s/`
   - **General**: `.env.example`, `CI configs (.github/workflows, .gitlab-ci.yml, Jenkinsfile)`
2. Map top-level modules via directory listing (depth 2)
3. **Discover all `.context/` folders** across the repo to build the context navigation tree
4. Read the existing `.context/CONTEXT.md`, `.context/ARCHITECTURE.md`, and `README.md` to understand current state

### Phase 2: Generate or Update Documents

Create `.context/` directory at project root if missing. Use templates in [references/templates.md](references/templates.md) for structure.

| File | Location | Audience | Purpose |
|------|----------|----------|---------|
| `CONTEXT.md` | `.context/` | AI agents / tools | Full system context: architecture, module map with links to per-folder `.context/CONTEXT.md`, dev standards, quick-reference snippets |
| `ARCHITECTURE.md` | `.context/` | Both | System blueprint: Mermaid diagrams, data flows, security design |
| `README.md` | repo root | Humans | Landing page: what it is, prerequisites, quick start, links to service docs |

**Update behavior (when docs already exist):**
- Read the existing document first
- Compare against current codebase state
- **Preserve** the existing structure and custom content
- **Update** sections that are stale (e.g., new modules missing from module map, changed endpoints, new env vars, updated commands)
- **Add** sections that are missing but should exist
- **Do not** remove custom content the user may have added
- For `README.md` specifically: update API endpoints, env vars, project structure, commands, and tech stack if they've changed. Preserve custom prose, badges, and sections the user authored.

**First-time generation (when docs don't exist):**
- If `README.md` already exists and is comprehensive, preserve its structure — update stale sections only
- If `README.md` is missing or minimal, generate one using the template
- For the reference README structure of a well-documented project, see [references/readme-reference.md](references/readme-reference.md)

**Context Navigation Tree (required in CONTEXT.md):**

Generate a full tree of all `.context/` folders in the repo inside `CONTEXT.md`. This serves as the master index for both AI agents and humans to navigate to any module's documentation. Format:

```
.context/                          # Project-level context (you are here)
├── CONTEXT.md
├── ARCHITECTURE.md
└── metadata.json

src/
├── auth/.context/                 # Authentication module
│   ├── CONTEXT.md
│   └── OVERVIEW.md
├── users/.context/                # User management
│   ├── CONTEXT.md
│   └── OVERVIEW.md
├── payments/.context/             # Payment processing
│   ├── CONTEXT.md
│   └── OVERVIEW.md
└── ui/
    ├── components/.context/       # Shared UI components
    │   ├── CONTEXT.md
    │   └── OVERVIEW.md
    └── pages/.context/            # Page-level views
        ├── CONTEXT.md
        └── OVERVIEW.md
```

Each entry should link to the respective CONTEXT.md. When modules have no `.context/` folder yet, note them as `(not yet documented)`.

**Key principles:**
- Map, not territory — explain patterns, relationships, and intent. Never duplicate code.
- Link to per-folder `.context/CONTEXT.md` files for deep dives (create stubs if missing)
- Include only commands that actually exist in the project
- All generated files are agent-agnostic — no tool-specific naming

**Project-type-specific sections:**

> Detect the project type during Reconnaissance and include the matching sections. Multiple types can apply (e.g., a full-stack app gets both backend and frontend sections).

**Backend / API projects:**
Detect by: route/controller definitions, API framework usage (FastAPI, Django, Spring Boot, Express, Gin, ASP.NET, Rails, Phoenix, Actix, etc.), `migrations/` directory, ORM config, Dockerfile with server entrypoint.

When detected, additionally include:
- **CONTEXT.md**: Add a "Backend Architecture" section covering: API framework & version, ORM/database layer, authentication strategy, middleware pipeline, background job system, caching layer
- **ARCHITECTURE.md**: Add request lifecycle diagram (request → middleware → handler → service → repository → response), entity relationship diagram, and deployment topology
- **README.md**: Add database setup/migration commands, API documentation links, seed data instructions, and server run commands

**Frontend projects:**
Detect by: `package.json` with UI framework deps (React, Vue, Angular, Svelte, Next.js, Nuxt, etc.), `components/` or `pages/` directories, `.tsx`/`.jsx`/`.vue`/`.svelte` files, UI framework configs (`next.config`, `vite.config`, `angular.json`, etc.).

When detected, additionally include:
- **CONTEXT.md**: Add a "Frontend Architecture" section covering: UI framework & version, component library (MUI, Ant, Shadcn, etc.), styling strategy, state management approach, routing framework, build tool (Vite, Webpack, Turbopack), and design system/token source
- **ARCHITECTURE.md**: Add a Mermaid diagram showing the frontend component tree (pages → layouts → feature components → shared components), and a data flow diagram showing user interaction → state → API → re-render cycle
- **README.md**: Add frontend-specific quick start commands (dev server, storybook, build), environment variables for frontend (API URLs, feature flags), and browser support matrix if applicable

**CLI / Tool projects:**
Detect by: CLI argument parser imports (argparse, click, cobra, clap, commander, etc.), `main` entrypoint with command parsing, `bin/` directory.

When detected, additionally include:
- **CONTEXT.md**: Command tree with all subcommands, flags, and their effects
- **ARCHITECTURE.md**: Command dispatch flow diagram
- **README.md**: Installation methods (brew, pip, cargo, npm global, etc.), usage examples for every command

**Library / SDK projects:**
Detect by: library packaging config (`setup.py`, `Cargo.toml` with `[lib]`, `*.gemspec`, `*.csproj` with library output, etc.), public API exports, no server entrypoint.

When detected, additionally include:
- **CONTEXT.md**: Public API surface, versioning/compatibility policy, extension points
- **ARCHITECTURE.md**: Internal module dependency graph, plugin/extension architecture
- **README.md**: Installation for consumers, basic usage examples, link to full API docs

### Phase 3: Validation

1. Verify all relative links point to real files/folders
2. Confirm quick-start commands match actual scripts/targets in the project's build system (`package.json` scripts, `Makefile` targets, `gradle` tasks, `cargo` commands, `manage.py` commands, etc.)
3. Check that module navigation table includes all current top-level modules
4. Verify the context navigation tree matches the actual `.context/` folders on disk

### Phase 4: Metadata Update

Write `.context/metadata.json`. The metadata tracks a **history of every generation run** so changes to the project context can be traced per commit.

```json
{
  "version": "1.0",
  "last_commit": "{current_HEAD_hash}",
  "generated_at": "{ISO timestamp}",
  "project_type": ["backend", "frontend"],
  "context_files": ["CONTEXT.md", "ARCHITECTURE.md"],
  "readme_updated": true,
  "modules_documented": [
    "src/auth",
    "src/users",
    "src/payments"
  ],
  "modules_pending": [
    "src/notifications"
  ],
  "history": [
    {
      "commit": "{current_HEAD_hash}",
      "timestamp": "{ISO timestamp}",
      "action": "updated",
      "changed_top_level": ["src/auth", "src/payments", "README.md"],
      "context_files_modified": ["CONTEXT.md"],
      "readme_modified": true,
      "summary": "Added payments module to navigation tree, updated API endpoints in README"
    },
    {
      "commit": "{previous_hash}",
      "timestamp": "{ISO timestamp}",
      "action": "generated",
      "changed_top_level": [],
      "context_files_modified": ["CONTEXT.md", "ARCHITECTURE.md"],
      "readme_modified": true,
      "summary": "Initial generation"
    }
  ]
}
```

**Fields:**
- `last_commit` / `generated_at` — latest run info (used by staleness check)
- `project_type` — detected project types (e.g., `["backend", "frontend"]`, `["cli"]`, `["library"]`)
- `context_files` — list of `.context/` files managed by this skill
- `modules_documented` — modules that have their own `.context/` folder
- `modules_pending` — modules discovered but not yet documented (shown as "not yet documented" in the navigation tree)
- `history[]` — array of generation runs, newest first. Each entry records:
  - `commit` — the HEAD hash at time of run
  - `action` — `"generated"` (first run) or `"updated"` (subsequent runs)
  - `changed_top_level` — top-level directories/files that triggered this regeneration
  - `context_files_modified` — which project-level context docs were actually changed
  - `readme_modified` — whether README.md was updated in this run
  - `summary` — brief description of what changed in this update
- History is capped at 50 entries to prevent unbounded growth

## Arguments

- `$1` — Project root path
- `--deep` — Read deeper into submodules (slower, more thorough)
- `--skeleton` — Create file structure with TODOs only
- `--readme-only` — Only update the README.md
- `--force` — Regenerate all docs regardless of staleness check
