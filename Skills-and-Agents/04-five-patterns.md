# Five Skill Implementation Patterns

Skills range from simple instruction sets to complex multi-step workflows. These five patterns progress from simple to powerful:

```
    Pattern 1        Pattern 2        Pattern 3        Pattern 4        Pattern 5
    Basic Router     Asset Util.      Few-Shot         Procedural       Orchestration
    ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │           │    │           │    │           │    │           │    │           │
    │ SKILL.md  │    │ SKILL.md  │    │ SKILL.md  │    │ SKILL.md  │    │ SKILL.md  │
    │  (only)   │    │ + assets/ │    │ + examples│    │ + scripts/│    │ + all of  │
    │           │    │           │    │           │    │           │    │   above   │
    └───────────┘    └───────────┘    └───────────┘    └───────────┘    └───────────┘
         │                │                │                │                │
    Instructions     Static content   Demonstrate      Executable       Full
    only             loaded on        desired output   logic for        multi-step
                     demand           via examples     deterministic    workflow
                                                       tasks

    USE FOR:         USE FOR:         USE FOR:         USE FOR:         USE FOR:
    Coding style     License text     Code gen         Validation       Scaffolding
    Naming rules     Config           patterns         API calls        Release
    Commit format    templates        Data transforms  Calculations     pipelines
```

---

## Pattern 1: Basic Router — Instructions Only

The simplest pattern. Just a `SKILL.md` with rules the agent applies directly.

**Best for:** Coding standards, naming conventions, commit messages, PR templates.

```
commit-format/
└── SKILL.md
```

```yaml
---
name: commit-format
description: >
  Formats git commit messages using Conventional Commits.
  Use when committing or creating commit messages.
---

When creating commit messages, follow Conventional Commits:
- Format: <type>(<scope>): <description>
- Types: feat, fix, docs, style, refactor, test, chore
- Subject line max 72 chars, imperative mood, no trailing period
```

---

## Pattern 2: Asset Utilization — Static Content On Demand

`SKILL.md` plus reference/asset files. Offloads static content to separate files so the agent reads them only when needed. Prevents hallucination of critical text.

**Best for:** License headers, boilerplate templates, config schemas, legal text.

```
license-header/
├── SKILL.md
└── assets/
    ├── mit-header.txt
    ├── apache-header.txt
    └── proprietary-header.txt
```

```yaml
---
name: license-header
description: >
  Adds license headers to source files. Use when creating new files
  or when the user mentions license headers or copyright notices.
---

# License Header Adder

1. Ask which license type if not specified (MIT, Apache, Proprietary)
2. Read the appropriate template from [assets/](assets/)
3. Add the header as the first lines of each specified file
4. Adjust comment syntax for the file type (// for JS/TS, # for Python)
```

---

## Pattern 3: Few-Shot Learning — Show, Don't Just Tell

`SKILL.md` plus input/output example pairs. Shows the agent what good output looks like.

**Best for:** Code generation, data format conversions, documentation styles, migration patterns.

```
json-to-pydantic/
├── SKILL.md
└── examples/
    ├── input.json
    └── output_model.py
```

```yaml
---
name: json-to-pydantic
description: >
  Converts JSON schemas or sample JSON into Pydantic v2 models.
  Use when the user needs Python data models from JSON structures.
---

# JSON to Pydantic Converter

1. Analyze the input JSON structure
2. Follow the pattern demonstrated in [examples/](examples/)
3. Generate Pydantic v2 models with:
   - Field validators where appropriate
   - Optional fields for nullable values
   - Nested models for complex objects
```

**`examples/input.json`:**
```json
{
  "user": {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
    "roles": ["admin", "editor"],
    "profile": {
      "bio": "Developer",
      "avatar_url": null
    }
  }
}
```

**`examples/output_model.py`:**
```python
from pydantic import BaseModel, EmailStr, Field

class UserProfile(BaseModel):
    """User profile information."""
    bio: str
    avatar_url: str | None = None

class User(BaseModel):
    """User account data."""
    id: int
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    roles: list[str] = Field(default_factory=list)
    profile: UserProfile
```

---

## Pattern 4: Procedural Logic — Execute Scripts

`SKILL.md` plus executable scripts. Delegates deterministic work to scripts the agent runs and interprets.

**Best for:** Schema validation, linting, data integrity checks, environment setup.

```
db-schema-validator/
├── SKILL.md
└── scripts/
    └── validate_schema.py
```

```yaml
---
name: db-schema-validator
description: >
  Validates database schema files against team conventions.
  Use when the user creates or modifies migration files or SQL schemas.
allowed-tools: Bash(python *)
---

# Database Schema Validator

1. Identify the schema file to validate
2. Run: `python scripts/validate_schema.py <path-to-schema>`
3. Interpret the output:
   - Exit code 0 = all checks passed
   - Exit code 1 = issues found, report each one
4. Suggest fixes for any violations

## Conventions enforced:
- Every table must have a primary key named `id`
- All foreign keys must have an index
- Column names must be snake_case
- Timestamps must use `timestamptz`, not `timestamp`
```

---

## Pattern 5: Complex Orchestration — Full Workflow

Combines all patterns: instructions, references, examples, and scripts. Multi-step workflows.

**Best for:** Scaffolding components/services, release pipelines, full test suite generation.

```
react-component/
├── SKILL.md
├── examples/
│   ├── Example.tsx
│   └── Example.test.tsx
├── references/
│   └── component-conventions.md
└── scripts/
    └── check-exports.sh
```

```yaml
---
name: react-component
description: >
  Scaffolds a new React component with TypeScript, test file,
  Storybook story, and barrel export. Use when creating a new
  component or scaffolding UI elements.
allowed-tools: Read Glob Write Bash(npx *)
---

# React Component Scaffolder

## Steps
1. Determine the component location (check src/components/ or components/)
2. Create the component directory
3. Generate component file following [examples/Example.tsx](examples/Example.tsx)
4. Generate test file following [examples/Example.test.tsx](examples/Example.test.tsx)
5. Generate Storybook story (CSF 3.0 format)
6. Create barrel export (index.ts)
7. Update parent barrel if it exists
```

---

## Choosing Your Pattern

```
  Just instructions?                → Pattern 1: Basic Router
  Need templates or reference docs? → Pattern 2: Asset Utilization
  Need input/output examples?       → Pattern 3: Few-Shot Learning
  Need to run scripts?              → Pattern 4: Procedural Logic
  All of the above?                 → Pattern 5: Orchestration
```
