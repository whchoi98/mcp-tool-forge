"""Validate and fix generated boto3 code."""
from __future__ import annotations

import ast
import re
from pathlib import Path

from rich.console import Console

console = Console()


def validate_python_file(path: Path) -> tuple[bool, str]:
    """Check if a Python file has valid syntax. Returns (ok, error_msg)."""
    try:
        with open(path) as f:
            ast.parse(f.read())
        return True, ""
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"


def fix_function_names(code: str) -> str:
    """Replace hyphens in function names with underscores."""
    # Fix: def some-name(...) -> def some_name(...)
    code = re.sub(
        r'^(def\s+)([a-zA-Z_][a-zA-Z0-9_-]*?)(\s*\()',
        lambda m: m.group(1) + m.group(2).replace('-', '_') + m.group(3),
        code,
        flags=re.MULTILINE,
    )
    return code


def _is_invalid_if_line(stripped: str) -> bool:
    """Detect if an 'if X is not None:' line has invalid X."""
    m = re.match(r'if\s+(.+?)\s+is\s+not\s+None:', stripped)
    if not m:
        return False
    expr = m.group(1)
    # Valid: simple Python identifier like my_var
    if re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', expr):
        return False
    # Everything else is invalid (SQL, paths, commas, spaces, empty, etc.)
    return True


def fix_invalid_if_statements(code: str) -> str:
    """Remove if-statements with literal/invalid values (LLM hallucinations)."""
    lines = code.split('\n')
    fixed = []
    skip_next_params_line = False

    for line in lines:
        stripped = line.strip()

        # Catch all invalid if-patterns (use stripped version)
        if _is_invalid_if_line(stripped):
            skip_next_params_line = True
            continue

        # Also catch: if  is not None: (empty expression) or "if is not None:"
        if re.match(r'if\s+is\s+not\s+None:', stripped) or re.match(r'if\s{2,}\S', stripped):
            skip_next_params_line = True
            continue

        # Skip the params['X'] = Y line that follows an invalid if
        if skip_next_params_line and re.match(r"\s+params\[", stripped):
            skip_next_params_line = False
            continue

        skip_next_params_line = False
        fixed.append(line)

    return '\n'.join(fixed)


def fix_boto3_file(path: Path) -> tuple[bool, str]:
    """Attempt to fix common LLM generation errors in boto3 code."""
    with open(path) as f:
        original = f.read()

    code = original
    code = fix_function_names(code)
    code = fix_invalid_if_statements(code)

    if code != original:
        with open(path, 'w') as f:
            f.write(code)

    # Validate after fix
    return validate_python_file(path)


def validate_and_fix_all(output_dir: Path) -> dict:
    """Validate and fix all generated boto3 files."""
    results = {"ok": 0, "fixed": 0, "failed": 0, "errors": []}

    for boto3_file in sorted(output_dir.glob("*/boto3/tools.py")):
        server = boto3_file.parts[-3]

        # First check
        ok, err = validate_python_file(boto3_file)
        if ok:
            results["ok"] += 1
            continue

        # Try to fix
        ok, err = fix_boto3_file(boto3_file)
        if ok:
            results["fixed"] += 1
            console.print(f"  [yellow]Fixed:[/] {server}")
        else:
            results["failed"] += 1
            results["errors"].append((server, err))
            console.print(f"  [red]Failed:[/] {server}: {err}")

    return results
