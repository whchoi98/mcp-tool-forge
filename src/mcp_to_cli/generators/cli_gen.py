from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition

class CliGenerator:
    def __init__(self):
        self._env = get_template_env()

    def generate_function(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        template = self._env.get_template("cli_command.sh.j2")
        return template.render(tool=tool, mapping=mapping)

    def generate_module(self, server_name: str, tools: list[tuple[ToolDefinition, MappingResult]]) -> str:
        functions = [self.generate_function(t, m) for t, m in tools]
        template = self._env.get_template("cli_module.sh.j2")
        return template.render(server_name=server_name, functions=functions)
