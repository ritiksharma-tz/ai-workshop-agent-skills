---
name: qa-feature-docs
description: Generate and maintain feature documentation for QA automation. Creates per-feature specs (FEATURE.md, SCOPE.md, FLOWS.md, TECHNICAL.md) with business value, test boundaries, user flows, and API/DB details. Maintains a changelog tracking feature evolution across commits. Syncs project context first to ensure accurate feature discovery. Use when QA needs documentation for automation scripts, when onboarding testers, or when features change and tests need updating.
---

# QA Feature Documentation Skill

Generate and maintain feature documentation optimized for QA automation scripts.

## When to Use

- When QA team needs documentation to write automation scripts
- When project documentation is incomplete, incorrect, or missing
- When onboarding QA engineers to a project
- When features have changed and automation needs updating
- When asked to document features for testing purposes

## What This Skill Does

1. **Syncs project context** — Ensures `.context/` folders are up-to-date via context-generator
2. **Discovers features** — Analyzes codebase to identify all testable features
3. **Generates feature docs** — Creates per-feature documentation optimized for automation
4. **Maintains changelog** — Tracks feature evolution with commit references

## Output Structure

```
.qa/
├── CHANGELOG.md              # Feature evolution tracking
├── metadata.json             # Version tracking
└── features/
    ├── _index.md             # Feature catalog
    └── {feature-name}/
        ├── FEATURE.md        # Business value & user stories
        ├── SCOPE.md          # Test boundaries & coverage
        ├── FLOWS.md          # User flows & test scenarios
        └── TECHNICAL.md      # API/DB specs for automation
```

## Usage

```
/qa-feature-docs                    # Full run: sync context + all features
/qa-feature-docs --skip-context-sync # Skip context sync, just update features
/qa-feature-docs --features-only    # Only feature docs, no changelog
/qa-feature-docs --changelog-only   # Only update changelog
/qa-feature-docs user-auth orders   # Document specific features only
```

## Execution

### Phase 1: Context Sync (MANDATORY unless --skip-context-sync)

**CRITICAL: You MUST delegate context generation to the context-generator agent. Do NOT attempt to create context files manually.**

#### Step 1.1: Invoke context-generator for Project-Level Context

Use the Task tool to spawn a context-generator agent:

```
Task(
  subagent_type: "context-generator",
  prompt: "Generate project-level context documentation using the project-context skill.
           Create .context/CONTEXT.md, .context/ARCHITECTURE.md, and update README.md at the project root.
           Use --force if context already exists but may be stale.
           Follow the full project-context skill specification."
)
```

**Wait for this task to complete before proceeding.**

#### Step 1.2: Invoke context-generator for Module-Level Context

After project context is complete, spawn another context-generator agent for module documentation:

```
Task(
  subagent_type: "context-generator",
  prompt: "Generate module-level context documentation using the module-context skill.

           First, discover all source modules by:
           1. Reading the project structure from .context/CONTEXT.md
           2. Listing directories in the main source folder (src/, lib/, app/, packages/, etc.)
           3. Identifying modules that contain business logic, routes, models, services

           Then create .context/CONTEXT.md and .context/OVERVIEW.md for EACH discovered module.

           Use --recursive to process all modules.
           Use --force if context already exists but may be stale.
           Follow the full module-context skill specification."
)
```

**Wait for this task to complete before proceeding.**

#### Step 1.3: Verify Context Generation

Before proceeding to Phase 2, verify that context was generated:

1. Check that `.context/CONTEXT.md` exists at project root
2. List source modules and verify each has `.context/CONTEXT.md`
3. If any are missing, the context-generator task failed — investigate and retry

**DO NOT proceed to feature discovery without verified context files.**

---

### Phase 2: Feature Discovery

Now that context is available, discover features:

1. **Read project context:** `.context/CONTEXT.md` and `.context/ARCHITECTURE.md`
2. **Read module contexts:** Each module's `.context/CONTEXT.md`
3. **Identify features from:**
   - API routes (each route group = potential feature)
   - Database entities (each entity with CRUD = potential feature)
   - UI components (user-facing functionality)
   - Event handlers (async features)
   - Scheduled jobs (background features)
4. **Build feature → modules mapping:**
   - Map each feature to the modules that implement it
   - Note dependencies between features

---

### Phase 3: Staleness Detection

1. Check `.qa/metadata.json` for `last_commit`
2. If exists, run: `git diff --name-only {last_commit} HEAD`
3. Map changed files to affected features
4. Mark features as "new", "modified", or "unchanged"
5. Capture current commit hash for metadata update

---

### Phase 4: Generate Feature Docs

For each discovered feature (prioritize new/modified, then unchanged):

Create directory: `.qa/features/{feature-slug}/`

Generate four files using templates from `references/templates.md`:

1. **FEATURE.md** — Business value, user stories, acceptance criteria
   - Every acceptance criterion MUST be automation-testable
   - Link to related module contexts

2. **SCOPE.md** — Test boundaries, risk areas, coverage targets
   - Define P0/P1/P2 priorities clearly
   - Identify security-sensitive operations

3. **FLOWS.md** — Step-by-step user flows with inputs/outputs
   - Include happy path, alternative paths, and error paths
   - Create test scenario matrix with IDs

4. **TECHNICAL.md** — API specs, DB queries, test data templates
   - Include REAL paths, methods, and response codes (read from source)
   - Include REAL database queries for verification
   - Include test data factories

---

### Phase 5: Update Index & Changelog

1. **Update `.qa/features/_index.md`:**
   - List all features with status and priority
   - Group by domain
   - Link to project context

2. **Append to `.qa/CHANGELOG.md`:**
   - Entry for current date and commit
   - List added/modified/removed features
   - Include "Action Required" for QA team

3. **Update `.qa/metadata.json`:**
   - Set `last_commit` to current HEAD
   - Update feature list and timestamps

---

## File Templates

See `references/templates.md` for detailed templates of each output file.

## Quality Checklist

Before completing, verify:

- [ ] **Context exists:** `.context/CONTEXT.md` at project root AND in each source module
- [ ] Every acceptance criterion is automation-testable
- [ ] API specs include real paths, methods, and response codes
- [ ] Flows include specific inputs and expected outputs
- [ ] Changelog entries include "Action required" for QA team
- [ ] All docs link to relevant module contexts

## Troubleshooting

### Context files are missing or empty

The context-generator agent may have failed. Common causes:
- Agent timed out on large codebase
- Module path was incorrect
- Staleness check skipped generation (use --force)

**Fix:** Re-run Phase 1 with explicit paths and --force flag.

### Feature discovery finds no features

Context files may be incomplete or generic.

**Fix:**
1. Verify module context files have specific API/DB documentation
2. Manually read route files to identify endpoints
3. Re-run context-generator with --deep flag for thorough analysis
