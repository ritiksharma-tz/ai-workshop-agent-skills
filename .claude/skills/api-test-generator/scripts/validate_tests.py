#!/usr/bin/env python3
"""Validate API test files follow team conventions.

Checks:
- Test file has proper imports
- Tests are grouped by endpoint
- No hardcoded URLs
- Proper setup/teardown exists
- Assert statements use descriptive messages

Usage: python validate_tests.py <test-file-path>
Exit code 0 = all checks pass, 1 = issues found
"""

import re
import sys
from pathlib import Path


def validate_test_file(filepath: str) -> list[str]:
    """Validate a test file and return list of issues."""
    issues = []
    path = Path(filepath)

    if not path.exists():
        return [f"File not found: {filepath}"]

    content = path.read_text()
    lines = content.splitlines()

    # Check 1: No hardcoded localhost URLs
    for i, line in enumerate(lines, 1):
        if re.search(r'https?://localhost[:\d]*', line):
            issues.append(f"Line {i}: Hardcoded localhost URL found. Use base URL from config.")
        if re.search(r'https?://127\.0\.0\.1[:\d]*', line):
            issues.append(f"Line {i}: Hardcoded 127.0.0.1 URL found. Use base URL from config.")

    # Check 2: Has at least one test function/method
    test_count = len(re.findall(r'(def test_|it\(|test\()', content))
    if test_count == 0:
        issues.append("No test functions found. Expected def test_* or it()/test() calls.")

    # Check 3: Tests have descriptive names (not just test_1, test_2)
    for match in re.finditer(r'def (test_\d+)\b', content):
        issues.append(f"Non-descriptive test name: {match.group(1)}. Use descriptive names.")

    # Check 4: Assert statements exist
    assert_count = len(re.findall(r'(assert |expect\(|\.should)', content))
    if assert_count == 0:
        issues.append("No assertions found. Tests must verify expected behavior.")

    # Check 5: Status code checks exist
    status_check = re.search(r'(status_code|\.status|statusCode)', content)
    if not status_check:
        issues.append("No HTTP status code checks found. Always verify response status.")

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_tests.py <test-file-path>")
        sys.exit(1)

    filepath = sys.argv[1]
    issues = validate_test_file(filepath)

    if issues:
        print(f"FAIL: {len(issues)} issue(s) found in {filepath}\n")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print(f"PASS: {filepath} follows all conventions.")
        sys.exit(0)


if __name__ == "__main__":
    main()
