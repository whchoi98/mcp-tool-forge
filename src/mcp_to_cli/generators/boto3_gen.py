from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition

class Boto3Generator:
    def __init__(self):
        self._env = get_template_env()

    def _param_signature(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        parts = []
        type_map = {"string": "str", "object": "dict", "integer": "int", "boolean": "bool", "array": "list"}
        for p in tool.params:
            if p.required:
                parts.append(f"{p.name}: {type_map.get(p.type, 'Any')}")
        for p in tool.params:
            if not p.required:
                parts.append(f"{p.name}: {type_map.get(p.type, 'Any')} | None = None")
        parts.append("**kwargs")
        return ", ".join(parts)

    def generate_function(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        template = self._env.get_template("boto3_func.py.j2")
        return template.render(
            tool=tool, mapping=mapping,
            param_signature=self._param_signature(tool, mapping),
        )

    def generate_module(self, server_name: str, tools: list[tuple[ToolDefinition, MappingResult]]) -> str:
        functions = [self.generate_function(t, m) for t, m in tools]
        template = self._env.get_template("boto3_module.py.j2")
        return template.render(server_name=server_name, functions=functions)
