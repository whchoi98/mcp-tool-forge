# MCP-to-CLI Converter

MCP 서버의 tool schema를 추출하여 boto3/CLI/schema/agentcore/skill 5가지 형식으로 변환하는 Python CLI 도구.

## Tech Stack

- **Language**: Python 3.11
- **CLI**: Click 8.x + Rich (terminal UI)
- **MCP Client**: MCP SDK 1.26.0 (`stdio_client` + `ClientSession`)
- **AWS**: boto3 (API calls + Bedrock LLM inference)
- **Templates**: Jinja2 (code generation)
- **Config**: PyYAML (registry, mappings)
- **Build**: Hatchling
- **Test**: pytest + pytest-asyncio

## Project Structure

```
mcp-to-cli/
├── src/mcp_to_cli/
│   ├── cli.py              # Click CLI entry point
│   ├── pipeline.py          # 3-phase orchestrator (extract -> map -> generate)
│   ├── connector.py         # MCP SDK stdio_client connection
│   ├── parser.py            # MCP tool schema -> ToolDefinition
│   ├── registry.py          # Server registry loader
│   ├── registry.yaml        # 63 servers (package names, runtime, category)
│   ├── mapping_loader.py    # Static YAML mapping loader
│   ├── llm_mapper.py        # Bedrock Claude LLM mapping (Phase 3)
│   ├── cache.py             # Schema cache (~/.mcp-to-cli/cache/)
│   ├── validator.py         # Generated code syntax validator/fixer
│   ├── skill_registrar.py   # Claude Code skill registration
│   ├── models.py            # Dataclasses (ToolParam, ToolDefinition, etc.)
│   ├── generators/          # 5 output generators
│   │   ├── boto3_gen.py     # Python boto3 functions
│   │   ├── cli_gen.py       # Bash AWS CLI functions
│   │   ├── schema_gen.py    # OpenAPI tool schema JSON
│   │   ├── agentcore_gen.py # AgentCore Gateway toolSpec
│   │   └── skill_gen.py     # Claude Code skill markdown
│   ├── mappings/            # Static YAML mappings (iam.yaml, dynamodb.yaml)
│   └── templates/           # Jinja2 templates (6 .j2 files)
├── tests/                   # 38 pytest tests
├── docs/plans/              # Design and implementation plans
└── output/                  # Generated code (gitignored)
```

## Key Commands

```bash
# Install
pip3.11 install -e ".[dev]"

# Test
python3.11 -m pytest tests/ -v

# CLI usage
python3.11 -m mcp_to_cli.cli list-servers
python3.11 -m mcp_to_cli.cli list-servers --category "Data & Analytics"
python3.11 -m mcp_to_cli.cli list-tools --server aws-iam-mcp-server
python3.11 -m mcp_to_cli.cli convert --server aws-iam-mcp-server --output all
python3.11 -m mcp_to_cli.cli convert --server <name> --llm-assist
python3.11 -m mcp_to_cli.cli register --server <name> -d output
```

## Conventions

### Pipeline Phases
1. **Extract**: MCP SDK `tools/list` (cached in ~/.mcp-to-cli/cache/)
2. **Map - Static**: `mappings/*.yaml` for known boto3/CLI mappings
3. **Map - LLM**: Bedrock Haiku (`us.anthropic.claude-3-5-haiku-20241022-v1:0`)
4. **Generate**: Jinja2 templates -> 5 output formats

### Registry
- Package names from PyPI (differ from server names)
- ECS uses split-package: `"--from awslabs-ecs-mcp-server ecs-mcp-server"`
- Some servers need `AWS_REGION` env var

### Testing
- All tests use mocks (no real AWS/MCP calls)
- `pytest-asyncio` for async tests

## Auto-Sync Rules

When exiting Plan Mode after making changes:
1. Update this CLAUDE.md if architecture or commands changed
2. Update `docs/architecture.md` if components changed
