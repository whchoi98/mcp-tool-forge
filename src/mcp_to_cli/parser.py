"""Schema parser for MCP tool definitions.
MCP 도구 정의를 위한 스키마 파서."""

from __future__ import annotations

from mcp_to_cli.models import ToolDefinition, ToolParam


def parse_mcp_tool_schema(raw: dict, server: str) -> ToolDefinition:
    """Parse a raw MCP tool schema dict into a ToolDefinition.
    원시 MCP 도구 스키마 딕셔너리를 ToolDefinition으로 파싱합니다."""
    # Extract basic tool metadata / 기본 도구 메타데이터 추출
    name = raw["name"]
    description = raw.get("description", "")
    # Extract input schema and properties / 입력 스키마 및 속성 추출
    input_schema = raw.get("inputSchema", {})
    properties = input_schema.get("properties", {})
    required_names = set(input_schema.get("required", []))

    # Build parameter list from schema properties / 스키마 속성에서 파라미터 목록 구성
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
    """Parse a full tools/list response into ToolDefinitions.
    전체 tools/list 응답을 ToolDefinition 목록으로 파싱합니다."""
    return [parse_mcp_tool_schema(t, server) for t in tools_response]
