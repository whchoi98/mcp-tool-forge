from mcp_to_cli.parser import parse_mcp_tool_schema


def test_parse_simple_tool():
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
    raw_schema = {
        "name": "list_tables", "description": "List DynamoDB tables",
        "inputSchema": {"type": "object", "properties": {"limit": {"type": "integer", "description": "Max results"}}, "required": []},
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert len(tool.params) == 1
    assert tool.params[0].required is False


def test_parse_tool_no_params():
    raw_schema = {"name": "get_status", "description": "Get status", "inputSchema": {"type": "object", "properties": {}}}
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert len(tool.params) == 0


def test_parse_tool_nested_properties():
    raw_schema = {
        "name": "complex_tool", "description": "A tool with nested params",
        "inputSchema": {
            "type": "object",
            "properties": {"config": {"type": "object", "description": "Configuration object", "properties": {"key": {"type": "string"}}}},
            "required": ["config"],
        },
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert tool.params[0].type == "object"
    assert tool.params[0].required is True
