"""Generator for Python boto3 wrapper functions.
Python boto3 래퍼 함수 생성기."""
from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition


class Boto3Generator:
    """Generates boto3-based Python functions from MCP tool definitions.
    MCP 도구 정의에서 boto3 기반 Python 함수를 생성한다."""

    def __init__(self, default_profile: str | None = None):
        self._env = get_template_env()  # Jinja2 template environment / Jinja2 템플릿 환경
        self._default_profile = default_profile  # Default AWS profile for generated code / 생성 코드의 기본 AWS 프로필

    def _param_signature(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        """Build a Python function parameter signature string.
        Python 함수 매개변수 시그니처 문자열을 생성한다."""
        parts = []
        # JSON-to-Python type mapping / JSON-Python 타입 매핑
        type_map = {"string": "str", "object": "dict", "integer": "int", "boolean": "bool", "array": "list"}
        # Add required parameters first / 필수 매개변수를 먼저 추가
        for p in tool.params:
            if p.required:
                parts.append(f"{p.name}: {type_map.get(p.type, 'Any')}")
        # Add optional parameters with defaults / 기본값이 있는 선택적 매개변수 추가
        for p in tool.params:
            if not p.required:
                parts.append(f"{p.name}: {type_map.get(p.type, 'Any')} | None = None")
        # Add profile_name for AWS multi-profile support / AWS 다중 프로필 지원을 위한 profile_name 추가
        if self._default_profile:
            parts.append(f'profile_name: str | None = "{self._default_profile}"')
        else:
            parts.append("profile_name: str | None = None")
        # Allow extra keyword arguments / 추가 키워드 인수 허용
        parts.append("**kwargs")
        return ", ".join(parts)

    def generate_function(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        """Generate a single boto3 wrapper function.
        단일 boto3 래퍼 함수를 생성한다."""
        template = self._env.get_template("boto3_func.py.j2")
        return template.render(
            tool=tool, mapping=mapping,
            param_signature=self._param_signature(tool, mapping),
        )

    def generate_module(self, server_name: str, tools: list[tuple[ToolDefinition, MappingResult]]) -> str:
        """Generate a complete Python module with all boto3 functions.
        모든 boto3 함수가 포함된 완전한 Python 모듈을 생성한다."""
        functions = [self.generate_function(t, m) for t, m in tools]
        template = self._env.get_template("boto3_module.py.j2")
        return template.render(server_name=server_name, functions=functions)
