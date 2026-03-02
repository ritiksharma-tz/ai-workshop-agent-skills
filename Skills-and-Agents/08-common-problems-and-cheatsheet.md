# Common Problems Skills Solve

## 10 Developer Pain Points → Skill Solutions

| Problem                              | Pattern                | Skill Name            |
| ------------------------------------ | ---------------------- | --------------------- |
| Inconsistent commit messages         | Basic Router           | `commit-format`       |
| Missing license headers in new files | Asset Utilization      | `license-header`      |
| New devs writing non-standard code   | Few-Shot Learning      | `code-style-guide`    |
| Manual database migration validation | Procedural Logic       | `db-schema-validator` |
| Repetitive component scaffolding     | Orchestration          | `react-component`     |
| Inconsistent PR descriptions         | Basic Router           | `pr-description`      |
| Forgotten test edge cases            | Few-Shot Learning      | `test-patterns`       |
| Manual deployment checklists         | Orchestration + Manual | `deploy-checklist`    |
| Onboarding new team members          | Asset Utilization      | `codebase-guide`      |
| Repetitive API client generation     | Procedural + Few-Shot  | `api-client-gen`      |

---

## Skill Creation Cheat Sheet

```
    1. Create directory
       mkdir -p .claude/skills/my-skill

    2. Create SKILL.md with frontmatter
       ---
       name: my-skill
       description: What it does and when to use it.
       ---
       Your instructions here...

    3. (Optional) Add supporting files
       scripts/    → executable code
       references/ → detailed docs
       examples/   → input/output pairs
       assets/     → templates, data

    4. Test it
       /my-skill                    (direct invocation)
       "do the thing my skill does" (auto-discovery)

    5. Share it
       git add .claude/skills/my-skill
       git commit -m "feat: add my-skill"
       git push
```

---

## Quick Pattern Picker

```
    Just instructions?                → Pattern 1: Basic Router
    Need templates or reference docs? → Pattern 2: Asset Utilization
    Need input/output examples?       → Pattern 3: Few-Shot Learning
    Need to run scripts?              → Pattern 4: Procedural Logic
    All of the above?                 → Pattern 5: Orchestration
```

---

## Resources

| Resource              | Link                                                                                                                                   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Agent Skills Standard | [agentskills.io](https://agentskills.io)                                                                                               |
| Specification         | [agentskills.io/specification](https://agentskills.io/specification)                                                                   |
| Example Skills        | [github.com/anthropics/skills](https://github.com/anthropics/skills)                                                                   |
| Awesome Claude Skills | [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)                                    |
| Remotion AI Skills    | [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills)                                                                 |
| Frontend Design Skill | [Claude Code frontend-design plugin](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) |
| UI/UX Pro Max Skill   | [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)                            |
| Claude Code Docs      | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)                                                               |
| Cursor Docs           | [cursor.com/docs/context/skills](https://cursor.com/docs/context/skills)                                                               |
| Copilot Docs          | [docs.github.com/.../about-agent-skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)                        |
| Antigravity Docs      | [codelabs.developers.google.com/...antigravity-skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills) |
| OpenCode Docs         | [opencode.ai/docs/skills](https://opencode.ai/docs/skills/)                                                                            |
| Vercel Agent Skills   | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main)                                           |
| Skills.sh             | [skills.sh](https://skills.sh/) — browse and discover community-built skills                                                           |

> **Tip:** Use [skills.sh](https://skills.sh/) to find new skills and explore what the community has built. It's the easiest way to discover ready-made skills you can drop into your project.
