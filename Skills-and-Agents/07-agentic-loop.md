# The Agentic Loop — Observe, Plan, Act, Reflect

## Chatbot vs Agent

| | Chatbot | Agent |
|---|---------|-------|
| **Interaction** | One input → one output | Continuous loop until task complete |
| **Memory** | Conversation history only | Files, tools, skills, environment |
| **Actions** | Generates text | Reads files, runs commands, edits code, invokes skills |
| **Reasoning** | Single-pass | Multi-step: observe → plan → act → reflect → repeat |
| **Autonomy** | Passive (waits for input) | Proactive (decides next step) |

## The Four Phases

```
                         User Request
                              │
                              ▼
                     ┌──────────────────┐
                     │     OBSERVE      │
                     │                  │
                     │  • Read files    │
                     │  • Check errors  │
                     │  • Load skill    │
                     │    descriptions  │
                     │  • Read test     │
                     │    output        │
                     │  • Examine env   │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │      PLAN        │
                     │                  │
                     │  • Match task to │
                     │    skills        │
             ┌──────▶│  • Decompose     │
             │       │    into steps    │
             │       │  • Decide next   │
             │       │    action        │
             │       │  • Consider      │
             │       │    alternatives  │
             │       └────────┬─────────┘
             │                │
             │                ▼
             │       ┌──────────────────┐
             │       │      ACT         │
             │       │                  │
             │       │  • Edit files    │
             │       │  • Run commands  │
             │       │  • Execute skill │
             │       │    scripts       │
             │       │  • Load refs     │
             │       │  • Call APIs     │
             │       └────────┬─────────┘
             │                │
             │                ▼
             │       ┌──────────────────┐
             │       │     REFLECT      │
             │       │                  │
             │       │  • Did it work?  │
             │       │  • Tests pass?   │
             │       │  • Output right? │
             │       │  • Task done?    │
             │       └────────┬─────────┘
             │                │
             │       ┌────────┴────────┐
             │       │                 │
             │    Not done           Done
             │       │                 │
             └───────┘                 ▼
                                 Report to User
```

## How Skills Enhance Every Phase

| Phase | Without Skills | With Skills |
|-------|---------------|-------------|
| **Observe** | Reads files, guesses patterns | Sees skill descriptions — knows what capabilities exist |
| **Plan** | Improvises approach | Activates matching skill — has structured instructions |
| **Act** | Does its best guess | Follows skill's steps, runs scripts, reads references |
| **Reflect** | Checks if output "looks right" | Validates against skill's defined expectations |

## Example: The Loop in Action

```
User: "Create a new UserProfile component"

OBSERVE  → Reads project structure, sees react-component skill available
    │
PLAN     → Matches "create component" to skill description
    │       Activates skill, loads SKILL.md instructions
    │
ACT      → Step 1: Checks src/components/ exists ✓
    │
REFLECT  → Directory found, proceed
    │
ACT      → Step 2: Creates src/components/UserProfile/
    │
REFLECT  → Directory created ✓
    │
ACT      → Step 3: Reads examples/Example.tsx, generates UserProfile.tsx
    │
REFLECT  → Component follows pattern ✓
    │
ACT      → Step 4: Reads examples/Example.test.tsx, generates test
    │
REFLECT  → Test file created ✓
    │
ACT      → Step 5: Generates UserProfile.stories.tsx
    │
REFLECT  → Story file created ✓
    │
ACT      → Step 6: Creates index.ts barrel export
    │
REFLECT  → All files created, task complete ✓
    │
DONE     → "Created UserProfile component with tests and story"
```
