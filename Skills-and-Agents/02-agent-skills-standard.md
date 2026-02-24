# The Agent Skills Open Standard

## What Is It?

[**Agent Skills**](https://agentskills.io) is an open standard developed by Anthropic and adopted by the ecosystem. It defines a portable format for giving AI agents new capabilities.

A skill is a **folder** with a **`SKILL.md`** file. No build step. No compilation. No runtime dependency. Just files.

## Who Supports It?

Over **30+ tools** have adopted the standard:

```
    Claude Code    Cursor         GitHub Copilot   Google Antigravity
    OpenCode       Junie          Amp              Roo Code
    OpenAI Codex   Gemini CLI     VS Code Agent    Goose
    Spring AI      Factory        Piebald          Databricks
    TRAE           Firebender     Letta            OpenHands
    Autohand       Mux            Command Code     Qodo
    Laravel Boost  Emdash         Agentman         Mistral Vibe
    ...and growing
```

Write a skill once → it works across most of the tools your team already uses.

## Anatomy of a SKILL.md

Every skill has two parts: **YAML frontmatter** (metadata) + **Markdown body** (instructions).

```
    ┌──────────────────────────────────────────────────────────┐
    │                        SKILL.md                          │
    ├──────────────────────────────────────────────────────────┤
    │                                                          │
    │  ---  (frontmatter start)                                │
    │                                                          │
    │  name: api-test-generator         ← Identity (1-64 ch)  │
    │  description: Generates API...    ← Discovery trigger    │
    │  license: MIT                     ← Optional             │
    │  compatibility: Python 3.9+       ← Optional             │
    │  metadata:                        ← Optional key-value   │
    │    author: platform-team                                 │
    │    version: "2.1"                                        │
    │  allowed-tools: Bash(python *)    ← Optional tool access │
    │                                                          │
    │  ---  (frontmatter end)                                  │
    │                                                          │
    ├──────────────────────────────────────────────────────────┤
    │                                                          │
    │  # API Test Generator             ← Markdown body        │
    │                                     (instructions)       │
    │  ## When to use                                          │
    │  Activate when the user needs...                         │
    │                                                          │
    │  ## Steps                                                │
    │  1. Read the OpenAPI spec from                           │
    │     references/openapi-guide.md   ← File reference       │
    │  2. Identify all endpoints...                            │
    │  3. Generate pytest test files...                        │
    │  4. Run the generated tests...                           │
    │                                                          │
    └──────────────────────────────────────────────────────────┘
```

## Minimal Example

```yaml
---
name: commit-format
description: >
  Formats git commit messages using Conventional Commits specification.
  Use when the user asks to commit or create a commit message.
---

When creating commit messages, follow Conventional Commits:
- Format: <type>(<scope>): <description>
- Types: feat, fix, docs, style, refactor, test, chore
- Subject line max 72 chars, imperative mood, no trailing period
```

That's it. A folder named `commit-format/` with this `SKILL.md` inside it — and every AI tool that supports the standard will discover it.

## Full Example with Optional Fields

```yaml
---
name: api-test-generator
description: >
  Generates API integration tests from OpenAPI/Swagger specs.
  Use when the user needs to create tests for REST endpoints,
  mentions API testing, or references OpenAPI specifications.
license: MIT
compatibility: Requires Python 3.9+, pytest, and requests library
metadata:
  author: platform-team
  version: "2.1"
allowed-tools: Bash(python *) Bash(pytest *) Read Glob
---

# API Test Generator

## When to use
Activate when the user needs integration tests for REST API endpoints.

## Steps
1. Read the OpenAPI spec from [references/openapi-guide.md](references/openapi-guide.md)
2. Identify all endpoints and their request/response schemas
3. Generate pytest test files using the template pattern
4. Run the generated tests to verify they pass

## Edge cases to handle
- Authentication headers
- Pagination parameters
- Error response codes (4xx, 5xx)
```

## Frontmatter Field Reference

```
    STANDARD FIELDS (agentskills.io)
    ═════════════════════════════════
    name           1-64 chars, lowercase + hyphens only, must match folder name
                   Valid:   commit-format, api-test-generator, db-migrate
                   Invalid: Commit-Format, -deploy, my--skill

    description    1-1024 chars, what it does + when to use it
                   Good:  "Formats git commit messages using Conventional Commits.
                           Use when committing, creating commit messages, or
                           when team conventions are needed."
                   Bad:   "Helps with commits."

    license         License name or reference to LICENSE file
    compatibility   Environment requirements (tools, packages, network)
    metadata        Arbitrary key-value pairs (author, version, etc.)
    allowed-tools   Space-delimited list of pre-approved tools

    TOOL-SPECIFIC EXTENSIONS (Claude Code, Cursor)
    ═══════════════════════════════════════════════
    disable-model-invocation   true = only user can invoke via /name
    user-invocable             false = only agent can invoke
    context                    "fork" = run in isolated subagent
    agent                      Subagent type: Explore, Plan, general-purpose
    argument-hint              Autocomplete hint: [issue-number], [filename]
    model                      Override model for this skill
    hooks                      Lifecycle hooks scoped to this skill
```

## Skill Directory Structure

A skill can be as simple as a single file, or carry supporting resources:

```
my-skill/
├── SKILL.md           ← Main instructions (required)
├── scripts/           ← Executable code (optional)
│   └── validate.py
├── references/        ← Detailed docs (optional)
│   └── api-guide.md
├── examples/          ← Input/output pairs (optional)
│   ├── input.json
│   └── output.py
└── assets/            ← Templates, data (optional)
    └── template.txt
```
