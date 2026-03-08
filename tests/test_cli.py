from click.testing import CliRunner
from mcp_to_cli.cli import main


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "MCP-to-CLI" in result.output


def test_list_servers():
    runner = CliRunner()
    result = runner.invoke(main, ["list-servers"])
    assert result.exit_code == 0
    assert "aws-dynamodb-mcp-server" in result.output


def test_list_servers_by_category():
    runner = CliRunner()
    result = runner.invoke(main, ["list-servers", "--category", "Data & Analytics"])
    assert result.exit_code == 0
    assert "aws-dynamodb-mcp-server" in result.output
