"""Tests for the MCP connector module.
MCP 커넥터 모듈 테스트."""

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from mcp_to_cli.connector import MCPConnector
from mcp_to_cli.models import ServerConfig


def test_build_stdio_command_npx():
    """Test building a stdio command for npx runtime.
    npx 런타임용 stdio 명령 생성을 테스트합니다."""
    connector = MCPConnector()
    cmd, args = connector._build_command("npx", "@awslabs/core-mcp-server", [])
    assert cmd == "npx"
    # npx should include -y flag for auto-confirm / npx는 자동 확인을 위해 -y 플래그를 포함해야 함
    assert "-y" in args
    assert "@awslabs/core-mcp-server" in args


def test_build_stdio_command_uvx():
    """Test building a stdio command for uvx runtime.
    uvx 런타임용 stdio 명령 생성을 테스트합니다."""
    connector = MCPConnector()
    cmd, args = connector._build_command("uvx", "awslabs.aws-dynamodb-mcp-server", [])
    assert cmd == "uvx"
    assert "awslabs.aws-dynamodb-mcp-server" in args


def test_build_server_params():
    """Test building server parameters from config.
    구성에서 서버 파라미터 생성을 테스트합니다."""
    connector = MCPConnector()
    config = ServerConfig(
        name="test", package="test-pkg", runtime="uvx",
        transport="stdio", category="Test",
    )
    params = connector._build_server_params(config)
    assert params.command == "uvx"
    assert "test-pkg" in params.args


def test_build_server_params_with_env():
    """Test building server parameters with environment variables.
    환경 변수가 있는 서버 파라미터 생성을 테스트합니다."""
    connector = MCPConnector()
    config = ServerConfig(
        name="test", package="test-pkg", runtime="npx",
        transport="stdio", category="Test", env={"FOO": "bar"},
    )
    params = connector._build_server_params(config)
    # Environment variables should be passed through / 환경 변수가 전달되어야 함
    assert params.env is not None
    assert params.env["FOO"] == "bar"
