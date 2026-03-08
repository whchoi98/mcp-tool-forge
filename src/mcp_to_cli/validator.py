"""Validate and fix generated boto3 code.
생성된 boto3 코드를 검증하고 수정합니다."""
from __future__ import annotations

import ast
import re
from pathlib import Path

from rich.console import Console

console = Console()


def validate_python_file(path: Path) -> tuple[bool, str]:
    """Check if a Python file has valid syntax. Returns (ok, error_msg).
    Python 파일의 구문이 유효한지 확인합니다. (성공 여부, 오류 메시지)를 반환합니다."""
    try:
        with open(path) as f:
            ast.parse(f.read())
        return True, ""
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"


def fix_function_names(code: str) -> str:
    """Replace hyphens in function names with underscores.
    함수 이름에서 하이픈을 밑줄로 교체합니다."""
    # Fix: def some-name(...) -> def some_name(...) / 수정: def some-name(...) -> def some_name(...)
    code = re.sub(
        r'^(def\s+)([a-zA-Z_][a-zA-Z0-9_-]*?)(\s*\()',
        lambda m: m.group(1) + m.group(2).replace('-', '_') + m.group(3),
        code,
        flags=re.MULTILINE,
    )
    return code


def _is_invalid_if_line(stripped: str) -> bool:
    """Detect if an 'if X is not None:' line has invalid X.
    'if X is not None:' 줄에서 X가 유효하지 않은지 감지합니다."""
    m = re.match(r'if\s+(.+?)\s+is\s+not\s+None:', stripped)
    if not m:
        return False
    expr = m.group(1)
    # Valid: simple Python identifier like my_var / 유효: my_var 같은 단순 Python 식별자
    if re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', expr):
        return False
    # Everything else is invalid (SQL, paths, commas, spaces, empty, etc.) / 나머지는 모두 유효하지 않음
    return True


def fix_invalid_if_statements(code: str) -> str:
    """Remove if-statements with literal/invalid values (LLM hallucinations).
    리터럴/유효하지 않은 값을 가진 if문을 제거합니다 (LLM 환각)."""
    lines = code.split('\n')
    fixed = []
    skip_next_params_line = False

    for line in lines:
        stripped = line.strip()

        # Catch all invalid if-patterns / 모든 유효하지 않은 if 패턴 포착
        if _is_invalid_if_line(stripped):
            skip_next_params_line = True
            continue

        # Also catch: if  is not None: (empty expression) / 빈 표현식도 포착
        if re.match(r'if\s+is\s+not\s+None:', stripped) or re.match(r'if\s{2,}\S', stripped):
            skip_next_params_line = True
            continue

        # Skip the params['X'] = Y line that follows an invalid if / 유효하지 않은 if 뒤의 params 할당 건너뛰기
        if skip_next_params_line and re.match(r"\s+params\[", stripped):
            skip_next_params_line = False
            continue

        skip_next_params_line = False
        fixed.append(line)

    return '\n'.join(fixed)


def fix_boto3_file(path: Path) -> tuple[bool, str]:
    """Attempt to fix common LLM generation errors in boto3 code.
    boto3 코드에서 일반적인 LLM 생성 오류 수정을 시도합니다."""
    with open(path) as f:
        original = f.read()

    # Apply fixes sequentially / 순차적으로 수정 적용
    code = original
    code = fix_function_names(code)
    code = fix_invalid_if_statements(code)

    # Write back only if changes were made / 변경 사항이 있을 때만 다시 기록
    if code != original:
        with open(path, 'w') as f:
            f.write(code)

    # Validate after fix / 수정 후 검증
    return validate_python_file(path)


def validate_and_fix_all(output_dir: Path) -> dict:
    """Validate and fix all generated boto3 files.
    생성된 모든 boto3 파일을 검증하고 수정합니다."""
    results = {"ok": 0, "fixed": 0, "failed": 0, "errors": []}

    for boto3_file in sorted(output_dir.glob("*/boto3/tools.py")):
        server = boto3_file.parts[-3]

        # First check syntax validity / 먼저 구문 유효성 확인
        ok, err = validate_python_file(boto3_file)
        if ok:
            results["ok"] += 1
            continue

        # Try to auto-fix common issues / 일반적인 문제 자동 수정 시도
        ok, err = fix_boto3_file(boto3_file)
        if ok:
            results["fixed"] += 1
            console.print(f"  [yellow]Fixed:[/] {server}")
        else:
            results["failed"] += 1
            results["errors"].append((server, err))
            console.print(f"  [red]Failed:[/] {server}: {err}")

    return results
