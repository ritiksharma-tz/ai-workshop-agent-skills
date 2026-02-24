# Progressive Disclosure — How Agents Load Skills

## The Problem

AI agents have finite context windows. If you load every skill's full instructions at startup, you waste context on irrelevant knowledge. The agent becomes slower and less accurate.

## The Solution: Three-Tier Loading

Skills load information in three tiers, each triggered only when needed:

```
    TIER 1: METADATA  (~100 tokens per skill)
    ══════════════════════════════════════════
    Loaded: At startup, for ALL available skills
    Content: Only name + description

    ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐
    │ commit-   │  │ api-test  │  │ db-       │  │ deploy-   │
    │ format    │  │ generator │  │ migrate   │  │ check     │
    │ ───────── │  │ ───────── │  │ ───────── │  │ ───────── │
    │ name +    │  │ name +    │  │ name +    │  │ name +    │
    │ desc only │  │ desc only │  │ desc only │  │ desc only │
    └───────────┘  └───────────┘  └───────────┘  └───────────┘
          │               │
          │   User: "Generate tests for our REST API"
          │               │
          │               ▼

    TIER 2: INSTRUCTIONS  (<5,000 tokens recommended)
    ══════════════════════════════════════════════════
    Loaded: When skill is activated (description matched or /invoked)
    Content: Full SKILL.md markdown body

    ┌──────────────────────────────────────────┐
    │ api-test-generator/SKILL.md              │
    │ (full markdown body loaded into context) │
    │                                          │
    │ # API Test Generator                     │
    │ ## Step 1: Read the OpenAPI spec from    │
    │    references/openapi-guide.md  ──────┐  │
    │ ## Step 2: Identify endpoints         │  │
    │ ## Step 3: Generate tests             │  │
    │ ## Step 4: Run and verify             │  │
    └──────────────────────────────────────────┘
                                            │
          Agent reaches Step 1,             │
          needs the reference file          │
                                            ▼

    TIER 3: RESOURCES  (as needed)
    ══════════════════════════════
    Loaded: On demand, when agent needs a specific file
    Content: scripts/, references/, assets/

    ┌──────────────────────────────────────────┐
    │ references/openapi-guide.md              │
    │ (loaded only at this moment)             │
    └──────────────────────────────────────────┘
```

## Guidelines for Skill Authors

| Tier | What to Do | Why |
|------|-----------|-----|
| **Tier 1** | Write rich, keyword-heavy descriptions | Agents match tasks by description — vague = missed activation |
| **Tier 2** | Keep SKILL.md under 500 lines | Full body loads into context — bloat wastes tokens |
| **Tier 3** | Move detailed content to separate files | Reference docs, long examples, data files load only on demand |

## Good vs Bad Descriptions

```
BAD:   "Helps with commits."
        → Too vague. Agent can't distinguish from other commit-related skills.

GOOD:  "Formats git commit messages using Conventional Commits specification.
        Use when the user asks to commit, create a commit message, or
        mentions conventional commits."
        → Specific keywords. Agent knows exactly when to activate.

BAD:   "Database tools."
        → What tools? When? For what?

GOOD:  "Validates database schema files against team conventions.
        Use when the user creates or modifies migration files,
        SQL schemas, or mentions database validation."
        → Clear trigger conditions.
```
