"""Tests for the CLI interface module.
CLI 인터페이스 모듈 테스트."""

from click.testing import CliRunner
from mcp_to_cli.cli import main


def test_cli_help():
    """Test that the CLI help message displays correctly.
    CLI 도움말 메시지가 올바르게 표시되는지 테스트합니다."""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "MCP-to-CLI" in result.output


def test_list_servers():
    """Test the list-servers command output.
    list-servers 명령 출력을 테스트합니다."""
    runner = CliRunner()
    result = runner.invoke(main, ["list-servers"])
    assert result.exit_code == 0
    assert "aws-dynamodb-mcp-server" in result.output


def test_list_servers_by_category():
    """Test filtering servers by category via CLI.
    CLI를 통한 카테고리별 서버 필터링을 테스트합니다."""
    runner = CliRunner()
    result = runner.invoke(main, ["list-servers", "--category", "Data & Analytics"])
    assert result.exit_code == 0
    assert "aws-dynamodb-mcp-server" in result.output
