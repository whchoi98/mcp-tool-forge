from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition

class SkillGenerator:
    def __init__(self):
        self._env = get_template_env()

    def generate_skill(self, tool: ToolDefinition, mapping: MappingResult | None = None) -> str:
        template = self._env.get_template("skill_tool.md.j2")
        return template.render(tool=tool, mapping=mapping)
