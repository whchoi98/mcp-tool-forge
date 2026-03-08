import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from mcp_to_cli.connector import MCPConnector
from mcp_to_cli.models import ServerConfig


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


def test_build_server_params():
    connector = MCPConnector()
    config = ServerConfig(
        name="test", package="test-pkg", runtime="uvx",
        transport="stdio", category="Test",
    )
    params = connector._build_server_params(config)
    assert params.command == "uvx"
    assert "test-pkg" in params.args


def test_build_server_params_with_env():
    connector = MCPConnector()
    config = ServerConfig(
        name="test", package="test-pkg", runtime="npx",
        transport="stdio", category="Test", env={"FOO": "bar"},
    )
    params = connector._build_server_params(config)
    assert params.env is not None
    assert params.env["FOO"] == "bar"
