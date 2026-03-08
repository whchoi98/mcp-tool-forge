from __future__ import annotations
import json
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import ToolDefinition

class SchemaGenerator:
    def __init__(self):
        self._env = get_template_env()

    def generate_schema(self, tool: ToolDefinition) -> str:
        template = self._env.get_template("schema_tool.json.j2")
        return template.render(tool=tool)

    def generate_module(self, server_name: str, tools: list[ToolDefinition]) -> str:
        schemas = [json.loads(self.generate_schema(t)) for t in tools]
        return json.dumps({"server": server_name, "tools": schemas}, indent=2)
