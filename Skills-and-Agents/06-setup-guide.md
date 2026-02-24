# Setup Skills in Every Tool

## Skill Directory Locations

```
    TOOL               PROJECT SCOPE                   PERSONAL / GLOBAL SCOPE
    ═══════════════    ════════════════════════════    ═══════════════════════════════
    Claude Code        .claude/skills/<name>/          ~/.claude/skills/<name>/
    Cursor             .cursor/skills/<name>/          ~/.cursor/skills/<name>/
                       (also reads .claude/skills/)    (also reads ~/.claude/skills/)
    GitHub Copilot     .github/skills/<name>/          ~/.copilot/skills/<name>/
                       (also reads .claude/skills/)    (also reads ~/.claude/skills/)
    Antigravity        .agent/skills/<name>/           ~/.gemini/antigravity/skills/
    OpenCode           .opencode/skills/<name>/        ~/.config/opencode/skills/
                       (also reads .claude/skills/)    (also reads ~/.claude/skills/)
```

---

## Claude Code

```bash
# Project-level skill
mkdir -p .claude/skills/my-skill
# Create SKILL.md inside

# Personal skill (works across all your projects)
mkdir -p ~/.claude/skills/my-skill

# Invoke
/my-skill                    # direct
"do the task my skill does"  # auto-discovery

# Check what's loaded
/context
# Or ask: "What skills are available?"
```

---

## Cursor

```bash
# Project-level skill
mkdir -p .cursor/skills/my-skill
# Or use .claude/skills/ — Cursor reads it too

# Invoke: type / in Agent chat, search for skill name
/my-skill

# View discovered skills:
# Cursor Settings (Ctrl+Shift+J) → Rules → "Agent Decides" section
```

---

## GitHub Copilot

```bash
# Project-level skill
mkdir -p .github/skills/my-skill
# Or use .claude/skills/ — Copilot reads it too

# Works with:
# - Copilot Coding Agent (in PRs)
# - GitHub Copilot CLI
# - Agent mode in VS Code
```

---

## Google Antigravity

```bash
# Workspace-level skill
mkdir -p .agent/skills/my-skill

# Global skill
mkdir -p ~/.gemini/antigravity/skills/my-skill

# Antigravity uses semantic matching —
# describe your task and the agent auto-discovers relevant skills
```

---

## OpenCode

```bash
# Project-level skill
mkdir -p .opencode/skills/my-skill
# Or use .claude/skills/ — OpenCode reads it too

# Permission control via opencode.json:
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

---

## Cross-Tool Portability Strategy

```
    Commit skills to .claude/skills/ in your repository.

    ┌──────────────────────────────────┐
    │  your-project/                   │
    │  └── .claude/                    │
    │      └── skills/                 │
    │          ├── commit-format/      │
    │          │   └── SKILL.md        │
    │          ├── react-component/    │
    │          │   ├── SKILL.md        │
    │          │   └── examples/       │
    │          └── api-test-gen/       │
    │              ├── SKILL.md        │
    │              └── scripts/        │
    └──────────────────────────────────┘
              │
              ▼  Discovered automatically by:
    ┌──────────────────────────────────┐
    │  ✅  Claude Code  (native)       │
    │  ✅  Cursor       (reads .claude)│
    │  ✅  Copilot      (reads .claude)│
    │  ✅  OpenCode     (reads .claude)│
    │  ⚠️  Antigravity  (needs .agent) │
    │      → symlink or duplicate      │
    └──────────────────────────────────┘
```

For Antigravity compatibility:
```bash
ln -s .claude/skills .agent/skills
```

---

## Priority When Same Skill Exists at Multiple Levels

```
    Enterprise / Managed  (highest — overrides everything)
           │
           ▼
    Personal / Global     (your personal skills)
           │
           ▼
    Project               (repo-level skills)
           │
           ▼
    Plugin / Package      (namespaced as plugin:skill-name)
```
