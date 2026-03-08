"""Tests for the schema parser module.
스키마 파서 모듈 테스트."""

from mcp_to_cli.parser import parse_mcp_tool_schema


def test_parse_simple_tool():
    """Test parsing a simple MCP tool schema.
    간단한 MCP 도구 스키마 파싱을 테스트합니다."""
    # Create a raw schema with required params / 필수 파라미터가 있는 원시 스키마 생성
    raw_schema = {
        "name": "dynamodb_put_item",
        "description": "Put an item into a DynamoDB table",
        "inputSchema": {
            "type": "object",
            "properties": {
                "table_name": {"type": "string", "description": "The table name"},
                "item": {"type": "object", "description": "The item to put"},
            },
            "required": ["table_name", "item"],
        },
    }
    tool = parse_mcp_tool_schema(raw_schema, server="aws-dynamodb-mcp-server")
    assert tool.name == "dynamodb_put_item"
    assert tool.server == "aws-dynamodb-mcp-server"
    assert len(tool.params) == 2
    assert tool.params[0].required is True


def test_parse_tool_with_optional_params():
    """Test parsing a tool with optional parameters.
    선택적 파라미터가 있는 도구 파싱을 테스트합니다."""
    raw_schema = {
        "name": "list_tables", "description": "List DynamoDB tables",
        "inputSchema": {"type": "object", "properties": {"limit": {"type": "integer", "description": "Max results"}}, "required": []},
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert len(tool.params) == 1
    # Param not in required list should be optional / required 목록에 없는 파라미터는 선택적이어야 함
    assert tool.params[0].required is False


def test_parse_tool_no_params():
    """Test parsing a tool with no parameters.
    파라미터가 없는 도구 파싱을 테스트합니다."""
    raw_schema = {"name": "get_status", "description": "Get status", "inputSchema": {"type": "object", "properties": {}}}
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert len(tool.params) == 0


def test_parse_tool_nested_properties():
    """Test parsing a tool with nested object properties.
    중첩된 객체 속성이 있는 도구 파싱을 테스트합니다."""
    raw_schema = {
        "name": "complex_tool", "description": "A tool with nested params",
        "inputSchema": {
            "type": "object",
            "properties": {"config": {"type": "object", "description": "Configuration object", "properties": {"key": {"type": "string"}}}},
            "required": ["config"],
        },
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    # Nested object should retain its type / 중첩 객체는 타입을 유지해야 함
    assert tool.params[0].type == "object"
    assert tool.params[0].required is True
