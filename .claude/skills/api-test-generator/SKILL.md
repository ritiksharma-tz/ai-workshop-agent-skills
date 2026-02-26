---
name: api-test-generator
description: >
  Generates API integration tests from endpoint definitions or OpenAPI specs.
  Use when the user needs to create tests for REST endpoints, mentions API
  testing, or wants to add test coverage for HTTP routes.
license: MIT
compatibility: Requires Python 3.9+ with pytest and requests, or Node.js with vitest and supertest
metadata:
  author: platform-team
  version: "1.1"
allowed-tools: Read Glob Write Bash(python *) Bash(pytest *) Bash(npx vitest *)
---

# API Test Generator

Generate API integration tests and save a summary report as a persistent document artifact.

## Output Structure

```
.reports/
├── api-tests/
│   └── {YYYY-MM-DD}-{target-slug}.md    # API test generation summary
└── metadata.json                          # Report tracking

# Test files are written to the project's test directory
```

## When to Use

Activate when the user needs integration tests for REST API endpoints,
wants to test HTTP routes, or mentions API testing.

## Steps

1. **Detect the project's test framework**
   - Python: look for `pytest.ini`, `pyproject.toml`, or `conftest.py`
   - Node.js: look for `vitest.config.*`, `jest.config.*`, or test scripts in `package.json`

2. **Find the API endpoints**
   - Look for route definitions (Express routers, FastAPI/Flask routes, etc.)
   - Or read an OpenAPI/Swagger spec if available

3. **For each endpoint, generate tests covering:**
   - Happy path (200/201 response with valid input)
   - Validation errors (400 with invalid/missing fields)
   - Not found (404 for non-existent resources)
   - Authentication (401/403 if auth is required)

4. **Run the validation script** to check test structure:
   ```
   python scripts/validate_tests.py <test-file-path>
   ```

5. **Run the generated tests** to verify they pass against the actual API

6. **Save Artifact**

   **MANDATORY: Always save an API test generation summary as a document artifact.**

   1. Create `.reports/api-tests/` directory if it doesn't exist
   2. Generate filename: `{YYYY-MM-DD}-{target-slug}.md` (e.g., `2025-03-15-api-users.md`)
   3. Write the summary report with YAML frontmatter metadata:

   ```yaml
   ---
   type: api-test-generation
   target: "{route_or_spec_path}"
   test_files:
     - "{test_file_1}"
     - "{test_file_2}"
   date: "{YYYY-MM-DD}"
   commit: "{current_HEAD_short_hash}"
   framework: "{pytest | vitest | jest}"
   endpoints_tested: {n}
   tests:
     total: {n}
     happy_path: {n}
     validation: {n}
     not_found: {n}
     auth: {n}
   validation_passed: {true | false}
   tests_passing: {true | false}
   ---
   ```

   4. Write the report body after the frontmatter containing:
      - Endpoint discovery summary (routes found, methods, auth requirements)
      - Test coverage matrix (endpoint × test category)
      - Generated test file paths and overview
      - Validation script results
      - Test execution results (pass/fail counts)
      - Run instructions
   5. Update `.reports/metadata.json` — merge this report entry into the `reports` array:

   ```json
   {
     "reports": [
       {
         "type": "api-test-generation",
         "file": "api-tests/{filename}.md",
         "target": "{path}",
         "test_files": ["{test_file_1}"],
         "date": "{ISO timestamp}",
         "commit": "{hash}",
         "endpoints_tested": 8,
         "tests_generated": 24,
         "tests_passing": true
       }
     ]
   }
   ```

   6. Display to the user: the generated test files + summary + report file path

   **If `--no-artifact` is passed, skip the summary report (test files are still generated).**

## Test Structure Guidelines

- One test file per route/resource (e.g., `test_users.py` for `/api/users`)
- Group tests by endpoint using `describe`/`class`
- Use fixtures for test data setup and teardown
- Never hardcode URLs — use base URL from config/env
- Clean up created resources in teardown

## Arguments

- `$1` — Path to route file or OpenAPI spec
- `--framework` — Force: `pytest`, `vitest`, `jest`
- `--output` — Output directory for test files
- `--no-artifact` — Skip saving summary report (test files still generated)
