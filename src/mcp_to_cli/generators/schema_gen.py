"""Generator for OpenAPI-style JSON tool schemas.
OpenAPI 스타일 JSON 도구 스키마 생성기."""
from __future__ import annotations
import json
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import ToolDefinition


class SchemaGenerator:
    """Generates JSON schema definitions for MCP tools.
    MCP 도구의 JSON 스키마 정의를 생성한다."""

    def __init__(self):
        self._env = get_template_env()  # Jinja2 template environment / Jinja2 템플릿 환경

    def generate_schema(self, tool: ToolDefinition) -> str:
        """Generate a JSON schema for a single tool.
        단일 도구의 JSON 스키마를 생성한다."""
        template = self._env.get_template("schema_tool.json.j2")
        return template.render(tool=tool)

    def generate_module(self, server_name: str, tools: list[ToolDefinition]) -> str:
        """Generate a combined JSON document with all tool schemas.
        모든 도구 스키마가 포함된 통합 JSON 문서를 생성한다."""
        schemas = [json.loads(self.generate_schema(t)) for t in tools]
        return json.dumps({"server": server_name, "tools": schemas}, indent=2)
