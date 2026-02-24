---
name: pr-description
description: >
  Generates a well-structured pull request description from the current
  branch changes. Use when creating a PR, writing a PR description,
  or preparing code for review.
allowed-tools: Bash(git *) Bash(gh *) Read Glob
---

# Pull Request Description Generator

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

## Guidelines

- Keep the summary focused on *why*, not *what* (the diff shows *what*)
- Link related issues using `Closes #123` or `Related to #456`
- If the PR is large, suggest breaking it into smaller PRs
- Highlight anything that needs special reviewer attention
