# Skills vs Prompts

## The Problem

Every developer has done this:

1. Spend 10 minutes crafting the perfect prompt
2. Get exactly the output you wanted
3. Close the chat
4. Two weeks later, need the same thing
5. Can't find it. Re-type from memory. It comes out different.
6. Your teammate writes their own version. Now there are three.

This is the **Prompt Graveyard** — where good prompts go to die.

## Four Failure Modes of Ad-Hoc Prompting

```
    1. EPHEMERAL                  2. INCONSISTENT
    ┌──────────────────────┐      ┌──────────────────────┐
    │  Chat history         │      │  Dev A:              │
    │  Session 47           │      │  "write a test"      │
    │  (deleted)            │      │                      │
    │                       │      │  Dev B:              │
    │  "That perfect prompt │      │  "create unit test   │
    │   I wrote last        │      │   with mocks and..." │
    │   month..."           │      │                      │
    └──────────────────────┘      └──────────────────────┘

    3. NON-COMPOSABLE             4. CONTEXT-STARVED
    ┌──────────────────────┐      ┌──────────────────────┐
    │  Can't build on       │      │  A single prompt     │
    │  each other            │      │  can't carry:        │
    │                       │      │                      │
    │  Prompt A             │      │  - Scripts           │
    │  Prompt B             │      │  - Templates         │
    │  (no relation)        │      │  - Reference docs    │
    │                       │      │  - Examples          │
    │  No shared knowledge  │      │  - Assets            │
    └──────────────────────┘      └──────────────────────┘
```

## A Skill Is a Prompt That Grew Up

```
    ONE-OFF PROMPT                              REUSABLE SKILL
    ══════════════                              ══════════════

    Developer types prompt                      Repository: .claude/skills/my-skill/
         │                                           │
         ▼                                           ▼
    Chat history (ephemeral)                    SKILL.md (version-controlled)
         │                                      + scripts/ + references/ + examples/
         ▼                                           │
    Works once, for one person                       ▼
         │                                      Works for entire team, every time
         ▼                                           │
    Lost forever                                     ▼
                                                Discoverable by any AI agent
                                                     │
                                                     ▼
                                                Portable across 30+ tools
```

## What Makes a Skill Different

| | Prompt | Skill |
|---|--------|-------|
| **Lives in** | Chat history | Version-controlled repo |
| **Shared with** | Nobody | Entire team via git |
| **Discovered by** | Whoever remembers it | Any AI agent, automatically |
| **Can carry** | Text only | Scripts, templates, examples, references |
| **Consistency** | Varies every time | Same result, every time |
| **Reviewed** | Never | In pull requests, like any code |
