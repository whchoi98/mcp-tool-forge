import pytest
from unittest.mock import AsyncMock, patch
from mcp_to_cli.connector import MCPConnector


@pytest.mark.asyncio
async def test_list_tools_returns_parsed_schemas():
    mock_tools = [
        {"name": "test_tool", "description": "A test tool",
         "inputSchema": {"type": "object", "properties": {"param1": {"type": "string"}}, "required": ["param1"]}}
    ]
    connector = MCPConnector()
    with patch.object(connector, "_call_tools_list", new_callable=AsyncMock) as mock:
        mock.return_value = mock_tools
        tools = await connector.list_tools()
        assert len(tools) == 1
        assert tools[0]["name"] == "test_tool"


def test_build_stdio_command_npx():
    connector = MCPConnector()
    cmd, args = connector._build_command("npx", "@awslabs/core-mcp-server", [])
    assert cmd == "npx"
    assert "-y" in args
    assert "@awslabs/core-mcp-server" in args


def test_build_stdio_command_uvx():
    connector = MCPConnector()
    cmd, args = connector._build_command("uvx", "awslabs.aws-dynamodb-mcp-server", [])
    assert cmd == "uvx"
    assert "awslabs.aws-dynamodb-mcp-server" in args
