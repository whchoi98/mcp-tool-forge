# MCP-to-CLI Converter

Python CLI that converts MCP server tools into boto3/CLI/schema/skill outputs.

## Tech Stack
- Python 3.11, Click CLI, MCP SDK, boto3, anthropic, Jinja2, Rich

## Key Commands
- Run: `python3.11 -m mcp_to_cli.cli`
- Test: `python3.11 -m pytest tests/ -v`
- Install dev: `pip3.11 install -e ".[dev]"`

## Project Structure
- `src/mcp_to_cli/` - main package
- `src/mcp_to_cli/generators/` - 4 output generators
- `src/mcp_to_cli/mappings/` - static YAML mappings
- `src/mcp_to_cli/templates/` - Jinja2 templates
- `tests/` - pytest tests
