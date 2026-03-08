"""Base template environment for code generators.
코드 생성기를 위한 기본 템플릿 환경."""
from __future__ import annotations
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Template directory path / 템플릿 디렉터리 경로
_TEMPLATE_DIR = Path(__file__).parent.parent / "templates"


def get_template_env() -> Environment:
    """Create and return a Jinja2 template environment.
    Jinja2 템플릿 환경을 생성하고 반환한다."""
    return Environment(
        loader=FileSystemLoader(str(_TEMPLATE_DIR)),
        keep_trailing_newline=True,  # Preserve trailing newlines in templates / 템플릿의 후행 줄바꿈 유지
        trim_blocks=True,  # Remove first newline after block tags / 블록 태그 뒤 첫 줄바꿈 제거
        lstrip_blocks=True,  # Strip leading whitespace from block lines / 블록 줄 앞 공백 제거
    )
