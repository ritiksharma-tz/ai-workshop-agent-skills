---
name: pr-description
description: >
  Generates a well-structured pull request description from the current
  branch changes. Use when creating a PR, writing a PR description,
  or preparing code for review.
allowed-tools: Bash(git *) Bash(gh *) Read Glob Write
---

# Pull Request Description Generator

Generate a structured PR description and save it as a persistent document artifact.

## Output Structure

```
.reports/
├── pr-descriptions/
│   └── {YYYY-MM-DD}-{branch-slug}.md    # Generated PR description
└── metadata.json                          # Report tracking
```

## Steps

1. **Gather context about the changes**
   - Run `git log main...HEAD --oneline` to see all commits
   - Run `git diff main...HEAD --stat` to see changed files
   - Run `git diff main...HEAD` to see the actual diff

2. **Analyze the changes**
   - Identify the primary purpose (feature, fix, refactor, etc.)
   - List all modified files and categorize them
   - Note any breaking changes or migration steps needed

3. **Generate the PR description** using this template:

   Read the template from [assets/pr-template.md](assets/pr-template.md)

4. **Fill in each section** based on the analysis:
   - Summary: 2-3 bullet points of what changed and why
   - Type of change: check the appropriate box
   - How to test: specific steps a reviewer can follow
   - Screenshots: note if UI changes need screenshots

5. **Save Artifact**

   **MANDATORY: Always save the PR description as a document artifact.**

   1. Create `.reports/pr-descriptions/` directory if it doesn't exist
   2. Generate filename: `{YYYY-MM-DD}-{branch-slug}.md` (e.g., `2025-03-15-feat-user-auth.md`)
   3. Write the PR description with YAML frontmatter metadata:

   ```yaml
   ---
   type: pr-description
   branch: "{current_branch}"
   base: "{target_branch}"
   date: "{YYYY-MM-DD}"
   commit: "{current_HEAD_short_hash}"
   change_type: "{feature | fix | refactor | docs | perf | test | build | ci}"
   stats:
     files_changed: {n}
     additions: {n}
     deletions: {n}
     commits: {n}
   breaking_changes: {true | false}
   ---
   ```

   4. Write the full PR description body after the frontmatter
   5. Update `.reports/metadata.json` — merge this report entry into the `reports` array:

   ```json
   {
     "reports": [
       {
         "type": "pr-description",
         "file": "pr-descriptions/{filename}.md",
         "branch": "{branch}",
         "date": "{ISO timestamp}",
         "commit": "{hash}",
         "change_type": "{type}"
       }
     ]
   }
   ```

   6. Display to the user: the PR description + file path where it was saved

   **If `--no-artifact` is passed, skip artifact generation and only display to conversation.**

## Guidelines

- Keep the summary focused on *why*, not *what* (the diff shows *what*)
- Link related issues using `Closes #123` or `Related to #456`
- If the PR is large, suggest breaking it into smaller PRs
- Highlight anything that needs special reviewer attention

## Arguments

- `--base` — Target branch (default: main)
- `--no-artifact` — Skip saving as document (display only)
