"""Generator for AWS CLI shell script commands.
AWS CLI 셸 스크립트 명령 생성기."""
from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition


class CliGenerator:
    """Generates shell script functions wrapping AWS CLI commands.
    AWS CLI 명령을 래핑하는 셸 스크립트 함수를 생성한다."""

    def __init__(self):
        self._env = get_template_env()  # Jinja2 template environment / Jinja2 템플릿 환경

    def generate_function(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        """Generate a single CLI shell function.
        단일 CLI 셸 함수를 생성한다."""
        template = self._env.get_template("cli_command.sh.j2")
        return template.render(tool=tool, mapping=mapping)

    def generate_module(self, server_name: str, tools: list[tuple[ToolDefinition, MappingResult]]) -> str:
        """Generate a complete shell script module with all CLI functions.
        모든 CLI 함수가 포함된 완전한 셸 스크립트 모듈을 생성한다."""
        functions = [self.generate_function(t, m) for t, m in tools]
        template = self._env.get_template("cli_module.sh.j2")
        return template.render(server_name=server_name, functions=functions)
