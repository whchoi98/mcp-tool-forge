from __future__ import annotations
import json
from mcp_to_cli.models import ToolDefinition


class AgentCoreGenerator:
    def generate_tool_spec(self, tool: ToolDefinition) -> dict:
        """Generate a single AgentCore Gateway toolSpec."""
        properties = {}
        required = []
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
                "description": tool.description.split('\n')[0].strip(),  # First line only
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
        """Generate complete AgentCore Gateway tool config JSON."""
        tool_specs = [self.generate_tool_spec(t) for t in tools]
        return json.dumps({"tools": tool_specs}, indent=2)
