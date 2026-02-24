# AI Workshop: Skills & Agents for Developer Productivity

A hands-on workshop series teaching developers how to build **reusable AI skills** that work across Claude Code, Cursor, GitHub Copilot, Google Antigravity, and OpenCode — plus how AI agents actually reason and act.

> This repo is both the **learning material** and a **working skills library** you can use immediately.

---

## What You'll Learn

```
   Prompts are conversations.        Skills are infrastructure.
   ┌─────────────────────┐           ┌─────────────────────┐
   │  Typed once          │           │  Version-controlled  │
   │  Lost in chat history│    →→→    │  Shared across team  │
   │  Inconsistent        │           │  Works in 30+ tools  │
   │  One person, one time│           │  Automated discovery │
   └─────────────────────┘           └─────────────────────┘
```

- **Skills vs Prompts** — Why reusable skills beat one-off prompts for consistency and team productivity
- **The Agent Skills Standard** — One open format ([agentskills.io](https://agentskills.io)) that works across 30+ AI coding tools
- **Five Skill Patterns** — From simple instruction sets to full orchestration workflows
- **The Agentic Loop** — How AI agents observe, plan, act, and reflect autonomously
- **Hands-On Building** — Create, test, and share your own skills during the session

---

## Prerequisites

Before the workshop, please complete these steps:

### 1. Install at least one AI coding tool

| Tool                          | Install                                          |
| ----------------------------- | ------------------------------------------------ |
| **Claude Code** (recommended) | `npm install -g @anthropic-ai/claude-code`       |
| Cursor                        | [cursor.com](https://cursor.com)                 |
| GitHub Copilot                | VS Code extension marketplace                    |
| Google Antigravity            | [antigravity.google](https://antigravity.google) |
| OpenCode                      | `npm install -g opencode-ai`                     |

### 2. Clone this repo

```bash
git clone https://github.com/ritiksharma-tz/ai-workshop-agent-skills.git
cd ai-workshop-agent-skills
```

### 3. Prepare your task list

Write down **3 repetitive tasks** from your daily work that could become skills. Examples:

- "Every time I create a new API endpoint, I write the same boilerplate..."
- "I always forget the commit message format our team uses..."
- "Setting up test files follows the same pattern every time..."

You'll convert one of these into a working skill during the session.

---

## Session 2: Skills vs Prompts & Introduction to Agents

The session is split into standalone topic docs. Open each one, walk through it, demo, move on.

| #   | Topic                                | Doc                                                                                              | Demo                 |
| --- | ------------------------------------ | ------------------------------------------------------------------------------------------------ | -------------------- |
| 1   | Why skills beat one-off prompts      | [`01-skills-vs-prompts.md`](skills-and-agents/01-skills-vs-prompts.md)                           | —                    |
| 2   | The open standard & SKILL.md anatomy | [`02-agent-skills-standard.md`](skills-and-agents/02-agent-skills-standard.md)                   | Show a SKILL.md file |
| 3   | How agents load skills efficiently   | [`03-progressive-disclosure.md`](skills-and-agents/03-progressive-disclosure.md)                 | —                    |
| 4   | Five implementation patterns         | [`04-five-patterns.md`](skills-and-agents/04-five-patterns.md)                                   | Show each skill dir  |
| 5   | Who triggers a skill and when        | [`05-invocation-control.md`](skills-and-agents/05-invocation-control.md)                         | —                    |
| 6   | Setup in every tool                  | [`06-setup-guide.md`](skills-and-agents/06-setup-guide.md)                                       | Create a skill dir   |
| 7   | The Agentic Loop                     | [`07-agentic-loop.md`](skills-and-agents/07-agentic-loop.md)                                     | —                    |
| 8   | Common problems + cheat sheet        | [`08-common-problems-and-cheatsheet.md`](skills-and-agents/08-common-problems-and-cheatsheet.md) | —                    |

---

## Repo Structure

```
ai-workshop-agent-skills/
│
├── README.md                              ← You are here
│
├── skills-and-agents/                     ← Workshop topic docs (read & explain)
│   ├── 01-skills-vs-prompts.md
│   ├── 02-agent-skills-standard.md
│   ├── 03-progressive-disclosure.md
│   ├── 04-five-patterns.md
│   ├── 05-invocation-control.md
│   ├── 06-setup-guide.md
│   ├── 07-agentic-loop.md
│   └── 08-common-problems-and-cheatsheet.md
│
├── .claude/skills/                        ← Skills for Claude Code, Cursor, Copilot, OpenCode
│   ├── commit-format/                        Pattern 1: Basic Router
│   ├── pr-description/                       Pattern 2: Asset Utilization
│   ├── react-component/                      Pattern 5: Orchestration
│   ├── api-test-generator/                   Pattern 4: Procedural Logic
│   ├── code-review/                          Deep multi-pass code review
│   ├── pr-review/                            Pull request review
│   ├── security-scan/                        OWASP + secrets scanner
│   ├── test-generator/                       Multi-language test generation
│   ├── project-context/                      Project documentation generator
│   ├── module-context/                       Per-module documentation
│   ├── qa-feature-docs/                      QA feature documentation
│   └── skill-creator/                        Meta-skill: helps create new skills
│
├── .cursor/skills/                        ← Same skills for Cursor
├── .github/skills/                        ← Same skills for GitHub Copilot
├── .agent/skills/                         ← Same skills for Google Antigravity
└── .opencode/skills/                      ← Same skills for OpenCode
```

> All 5 directories contain the same 12 skills — so the repo works regardless of which AI tool you use.

---

## 12 Ready-to-Use Skills

This repo ships with working skills you can use immediately. Just clone the repo and your AI tool discovers them automatically.

| Skill                | What It Does                                                     | Pattern           |
| -------------------- | ---------------------------------------------------------------- | ----------------- |
| `commit-format`      | Enforces Conventional Commits format                             | Basic Router      |
| `pr-description`     | Generates structured PR descriptions from branch diff            | Asset Utilization |
| `react-component`    | Scaffolds component + test + story + barrel export               | Orchestration     |
| `api-test-generator` | Generates API integration tests with validation script           | Procedural Logic  |
| `code-review`        | Multi-pass review: security, logic, performance, maintainability | Asset Utilization |
| `pr-review`          | Structured PR feedback across 6 dimensions                       | Asset Utilization |
| `security-scan`      | OWASP Top 10, hardcoded secrets, insecure patterns               | Asset Utilization |
| `test-generator`     | Unit tests with edge cases (Python, TS, Go, Java, C#)            | Few-Shot          |
| `project-context`    | Generates CONTEXT.md, ARCHITECTURE.md, README                    | Asset Utilization |
| `module-context`     | Per-module CONTEXT.md + OVERVIEW.md                              | Asset Utilization |
| `qa-feature-docs`    | Feature specs for QA automation                                  | Asset Utilization |
| `skill-creator`      | Meta-skill that helps you create new skills                      | Basic Router      |

### Try one right now

```bash
# In Claude Code
/commit-format
/code-review src/
/react-component UserProfile

# Or just describe the task — the agent auto-discovers the right skill:
"Review this file for security issues"
"Create a new SearchBar component"
"Generate tests for the auth module"
```

---

## Quick Start: Create Your Own Skill

```bash
# 1. Create the skill directory
mkdir -p .claude/skills/my-skill

# 2. Write the SKILL.md
cat > .claude/skills/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: >
  What this skill does and when to use it.
  Be specific — the agent matches tasks by this description.
---

# My Skill

## Steps
1. First, do this...
2. Then, do that...
3. Finally, verify the result
EOF

# 3. Test it
# Direct invocation:
/my-skill

# Or natural language (agent auto-discovers):
"do the thing my skill does"

# 4. Share it
git add .claude/skills/my-skill
git commit -m "feat: add my-skill"
git push
```

### The Five Patterns (pick the one that fits)

```
  Just instructions?              → Pattern 1: Basic Router
  Need templates/reference docs?  → Pattern 2: Asset Utilization
  Need input/output examples?     → Pattern 3: Few-Shot Learning
  Need to run scripts?            → Pattern 4: Procedural Logic
  All of the above?               → Pattern 5: Orchestration
```

---

## Cross-Tool Compatibility

Skills placed in `.claude/skills/` are automatically discovered by:

| Tool               | Reads `.claude/skills/`? | Native directory    |
| ------------------ | :----------------------: | ------------------- |
| Claude Code        |     **Yes** (native)     | `.claude/skills/`   |
| Cursor             |         **Yes**          | `.cursor/skills/`   |
| GitHub Copilot     |         **Yes**          | `.github/skills/`   |
| OpenCode           |         **Yes**          | `.opencode/skills/` |
| Google Antigravity |            No            | `.agent/skills/`    |

This repo includes skills in **all five directories** so it works everywhere out of the box.

---

## Resources

| Resource                  | Link                                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Agent Skills Standard     | [agentskills.io](https://agentskills.io)                                                                                               |
| Specification             | [agentskills.io/specification](https://agentskills.io/specification)                                                                   |
| Claude Code Skills Docs   | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)                                                               |
| Cursor Skills Docs        | [cursor.com/docs/context/skills](https://cursor.com/docs/context/skills)                                                               |
| GitHub Copilot Skills     | [docs.github.com/.../about-agent-skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)                        |
| Google Antigravity Skills | [codelabs.developers.google.com/...antigravity-skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills) |
| OpenCode Skills           | [opencode.ai/docs/skills](https://opencode.ai/docs/skills/)                                                                            |
| Example Skills Library    | [github.com/anthropics/skills](https://github.com/anthropics/skills)                                                                   |

---
