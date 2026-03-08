# Architecture

## System Overview

MCP-to-CLI is a Python CLI tool that connects to AWS MCP servers, extracts tool schemas, and converts them to multiple output formats for use in different agent runtimes.

```
MCP Server (stdio)  -->  Connector  -->  Parser  -->  Pipeline  -->  Generators
     |                                      |            |              |
     v                                      v            v              v
 tools/list                           ToolDefinition   Mapping     5 formats:
 (JSON-RPC)                           (dataclass)      (static     boto3, cli,
                                                       + LLM)      schema, agentcore,
                                                                   skill
```

## Components

### CLI Layer (`cli.py`)
- Click-based CLI with commands: `list-servers`, `list-tools`, `convert`, `register`
- Rich tables for terminal output

### Pipeline (`pipeline.py`)
- Orchestrates 3-phase process: Extract -> Map -> Generate
- Manages cache for extracted schemas

### Connector (`connector.py`)
- MCP SDK `stdio_client` + `ClientSession`
- Supports uvx and npx runtimes
- 60s timeout with graceful cleanup

### Registry (`registry.py` + `registry.yaml`)
- 63 AWS MCP server configurations
- Package names, runtimes, categories
- Verified against PyPI

### Mapping (`mapping_loader.py` + `llm_mapper.py`)
- Static: YAML files for known services (IAM 29, DynamoDB 6)
- LLM: Bedrock Claude 3.5 Haiku for unmapped tools

### Generators (`generators/`)
- boto3: Python functions with type hints
- cli: Bash shell functions
- schema: OpenAPI-compatible JSON
- agentcore: AgentCore Gateway toolSpec format
- skill: Claude Code skill markdown

### Validator (`validator.py`)
- Post-generation syntax validation
- Auto-fix LLM hallucination patterns

## Data Flow

1. User runs `mcp-to-cli convert --server <name>`
2. Pipeline checks cache -> connects to MCP server -> extracts tools
3. Parser converts raw schemas to `ToolDefinition` objects
4. Mapping loader checks static YAML, then optionally LLM mapper
5. Generators produce output files in `output/<server>/<format>/`

## Infrastructure

- Python 3.11 package (hatchling build)
- Schema cache: `~/.mcp-to-cli/cache/`
- Plugin output: `~/.claude/plugins/mcp-to-cli-tools/`
- LLM: Bedrock `us.anthropic.claude-3-5-haiku` in us-east-1
