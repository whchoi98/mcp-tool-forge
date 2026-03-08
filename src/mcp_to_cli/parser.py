from __future__ import annotations

from mcp_to_cli.models import ToolDefinition, ToolParam


def parse_mcp_tool_schema(raw: dict, server: str) -> ToolDefinition:
    """Parse a raw MCP tool schema dict into a ToolDefinition."""
    name = raw["name"]
    description = raw.get("description", "")
    input_schema = raw.get("inputSchema", {})
    properties = input_schema.get("properties", {})
    required_names = set(input_schema.get("required", []))

    params = []
    for param_name, param_info in properties.items():
        params.append(
            ToolParam(
                name=param_name,
                type=param_info.get("type", "string"),
                description=param_info.get("description", ""),
                required=param_name in required_names,
                default=param_info.get("default"),
            )
        )

    return ToolDefinition(server=server, name=name, description=description, params=params)


def parse_tools_list(tools_response: list[dict], server: str) -> list[ToolDefinition]:
    """Parse a full tools/list response into ToolDefinitions."""
    return [parse_mcp_tool_schema(t, server) for t in tools_response]
