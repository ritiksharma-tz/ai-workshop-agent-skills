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
  version: "1.0"
allowed-tools: Read Glob Write Bash(python *) Bash(pytest *) Bash(npx vitest *)
---

# API Test Generator

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

## Test Structure Guidelines

- One test file per route/resource (e.g., `test_users.py` for `/api/users`)
- Group tests by endpoint using `describe`/`class`
- Use fixtures for test data setup and teardown
- Never hardcode URLs — use base URL from config/env
- Clean up created resources in teardown
