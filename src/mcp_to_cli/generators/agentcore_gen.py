"""Generator for Amazon Bedrock AgentCore Gateway tool configurations.
Amazon Bedrock AgentCore Gateway 도구 구성 생성기."""
from __future__ import annotations
import json
from mcp_to_cli.models import ToolDefinition


class AgentCoreGenerator:
    """Generates AgentCore Gateway toolSpec JSON from MCP tool definitions.
    MCP 도구 정의에서 AgentCore Gateway toolSpec JSON을 생성한다."""

    def generate_tool_spec(self, tool: ToolDefinition) -> dict:
        """Generate a single AgentCore Gateway toolSpec.
        단일 AgentCore Gateway toolSpec을 생성한다."""
        properties = {}
        required = []
        # Build parameter properties and required list / 매개변수 속성 및 필수 목록 구성
        for p in tool.params:
            properties[p.name] = {
                "type": p.type,
                "description": p.description,
            }
            if p.required:
                required.append(p.name)

        return {
            "toolSpec": {
                "name": tool.name,
                "description": tool.description.split('\n')[0].strip(),  # First line only / 첫 번째 줄만 사용
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": properties,
                        "required": required,
                    }
                }
            }
        }

    def generate_tool_config(self, server_name: str, tools: list[ToolDefinition]) -> str:
        """Generate complete AgentCore Gateway tool config JSON.
        완전한 AgentCore Gateway 도구 구성 JSON을 생성한다."""
        tool_specs = [self.generate_tool_spec(t) for t in tools]
        return json.dumps({"tools": tool_specs}, indent=2)
