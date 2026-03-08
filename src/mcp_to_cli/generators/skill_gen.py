"""Generator for Claude Code skill markdown files.
Claude Code 스킬 마크다운 파일 생성기."""
from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition


class SkillGenerator:
    """Generates markdown skill documents for Claude Code plugin registration.
    Claude Code 플러그인 등록을 위한 마크다운 스킬 문서를 생성한다."""

    def __init__(self):
        self._env = get_template_env()  # Jinja2 template environment / Jinja2 템플릿 환경

    def generate_skill(self, tool: ToolDefinition, mapping: MappingResult | None = None) -> str:
        """Generate a skill markdown document for a single tool.
        단일 도구의 스킬 마크다운 문서를 생성한다."""
        template = self._env.get_template("skill_tool.md.j2")
        return template.render(tool=tool, mapping=mapping)
