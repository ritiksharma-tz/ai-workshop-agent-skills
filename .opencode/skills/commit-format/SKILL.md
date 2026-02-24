---
name: commit-format
description: >
  Formats git commit messages using Conventional Commits specification.
  Use when the user asks to commit, create a commit message, or
  mentions conventional commits.
---

# Conventional Commit Formatter

When creating commit messages, follow the Conventional Commits specification.

## Format

```
<type>(<optional-scope>): <description>

[optional body]

[optional footer(s)]
```

## Types

| Type | When to Use |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Formatting, missing semicolons, etc. (no code change) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or correcting tests |
| `build` | Changes to build system or external dependencies |
| `ci` | Changes to CI configuration files and scripts |
| `chore` | Other changes that don't modify src or test files |
| `revert` | Reverts a previous commit |

## Rules

1. Subject line must not exceed 72 characters
2. Use imperative mood ("add" not "added" or "adds")
3. Do not end the subject line with a period
4. Separate subject from body with a blank line
5. Wrap body at 72 characters
6. Use the body to explain *what* and *why* vs. *how*
7. Reference issue numbers in the footer: `Fixes #123` or `Closes #456`

## Breaking Changes

- Add `!` after type/scope: `feat!: remove deprecated API`
- Or add `BREAKING CHANGE:` in the footer

## Examples

Good:
```
feat(auth): add OAuth2 login with Google provider

Implements Google OAuth2 flow using passport.js. Users can now
sign in with their Google accounts alongside email/password.

Closes #234
```

Bad:
```
updated the login page and fixed some stuff
```
