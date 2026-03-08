# MCP-to-CLI Converter Design

## Problem

MCP (Model Context Protocol) consumes excessive tokens due to:
- Tool definitions (JSON Schema) loaded into every conversation
- Request/response JSON payloads for each tool call
- 66+ AWS MCP servers with hundreds of tools = massive token overhead

Agents (AgentCore Gateway Lambda, AgentCore Interpreter, Claude Code, Kiro-CLI) can achieve the same functionality via boto3/AWS CLI with far fewer tokens.

## Solution

A Python CLI tool that:
1. Connects to any MCP server via stdio/SSE
2. Extracts tool schemas via `tools/list`
3. Converts each tool to 4 output formats:
   - **Python boto3 functions** - for Lambda, AgentCore Interpreter
   - **AWS CLI commands** - for shell-based agents
   - **OpenAPI/Tool Schema (JSON)** - for AgentCore Gateway tool definitions
   - **Claude Code Skills (.md)** - for Claude Code / Kiro-CLI

## Architecture: 3-Phase Hybrid Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                    MCP-to-CLI Converter                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Phase 1: Schema Extraction (Approach A)                │
│  ┌───────────┐    tools/list    ┌──────────────────┐   │
│  │ MCP Server ├────────────────►│ Tool Schema Cache │   │
│  │ (stdio/SSE)│                 │ (JSON files)      │   │
│  └───────────┘                  └────────┬─────────┘   │
│                                          │              │
│  Phase 2: Static Mapping (Approach B)    │              │
│  ┌──────────────────┐                    │              │
│  │ Mapping Registry  │◄─────────────────┘              │
│  │ (YAML/JSON)       │  known service → boto3 mapping   │
│  │ aws_api_call →    │                                  │
│  │   boto3.client()  │                                  │
│  └────────┬─────────┘                                  │
│           │ unmapped tools                              │
│  Phase 3: LLM-Assisted (Approach C)                    │
│  ┌────────▼─────────┐                                  │
│  │ LLM Inference     │  tool description + schema →    │
│  │ (Claude API)      │  boto3/CLI code generation      │
│  └────────┬─────────┘                                  │
│           │                                             │
│  Code Generation                                        │
│  ┌────────▼─────────┐                                  │
│  │ Output Generator  │                                  │
│  │ ├── boto3 (.py)   │                                  │
│  │ ├── cli (.sh)     │                                  │
│  │ ├── schema (.json)│                                  │
│  │ └── skill (.md)   │                                  │
│  └──────────────────┘                                  │
└─────────────────────────────────────────────────────────┘
```

## Target MCP Servers (66 servers, 9 categories)

Source: https://awslabs.github.io/mcp/

### Essential Setup
- AWS MCP Server (preview) - comprehensive AWS API, docs, Agent SOPs

### Documentation
- AWS Documentation MCP Server
- AWS Knowledge MCP Server

### Core
- AWS API MCP Server
- Core MCP Server (orchestration)

### Infrastructure & Deployment
- AWS Cloud Control API MCP Server
- AWS CloudFormation MCP Server
- AWS CDK MCP Server (DEPRECATED → AWS IaC MCP Server)
- AWS Terraform MCP Server
- Amazon EKS MCP Server
- Amazon ECS MCP Server
- Finch MCP Server
- AWS Serverless MCP Server (SAM CLI)
- AWS Lambda Tool MCP Server
- AWS Support MCP Server

### AI & Machine Learning
- Amazon Bedrock Knowledge Bases Retrieval MCP Server
- Amazon Kendra Index MCP Server
- Amazon Q Business Anonymous MCP Server
- Amazon Q Index MCP Server
- Document Loader MCP Server
- Amazon Nova Canvas MCP Server
- Amazon Bedrock Data Automation MCP Server
- Amazon Bedrock Custom Model Import MCP Server
- Amazon SageMaker AI MCP Server
- Amazon Bedrock AgentCore MCP Server

### Data & Analytics
- Amazon DynamoDB MCP Server
- Amazon Aurora PostgreSQL MCP Server
- AWS S3 Tables MCP Server
- Amazon Aurora MySQL MCP Server
- Amazon Aurora DSQL MCP Server
- Amazon DocumentDB MCP Server
- Amazon Neptune MCP Server
- Amazon Keyspaces MCP Server
- Amazon Timestream for InfluxDB MCP Server
- Amazon ElastiCache MCP Server
- Amazon ElastiCache / MemoryDB for Valkey MCP Server
- Amazon ElastiCache for Memcached MCP Server
- AWS AppSync MCP Server
- AWS IoT SiteWise MCP Server
- Amazon Data Processing MCP Server (Glue + EMR)
- Amazon Redshift MCP Server
- Amazon SageMaker Unified Studio MCP (Spark Troubleshooting)
- Amazon SageMaker Unified Studio MCP (Spark Upgrade)

### Developer Tools & Support
- Git Repo Research MCP Server
- Code Documentation Generation MCP Server
- AWS Diagram MCP Server
- Frontend MCP Server
- Synthetic Data MCP Server
- AWS IAM MCP Server
- AWS MSK MCP Server

### Integration & Messaging
- OpenAPI MCP Server
- Amazon SNS / SQS MCP Server
- Amazon MQ MCP Server
- AWS Step Functions MCP Server
- Amazon Location Service MCP Server

### Cost & Operations
- AWS Billing and Cost Management MCP Server
- AWS Pricing MCP Server
- AWS Cost Explorer MCP Server
- AWS Managed Prometheus MCP Server
- Amazon CloudWatch Application Signals MCP Server
- Amazon CloudWatch MCP Server
- AWS CloudTrail MCP Server
- AWS Well-Architected Security Assessment Tool MCP Server

### Healthcare & Lifesciences
- AWS HealthOmics MCP Server
- HealthImaging MCP Server
- HealthLake MCP Server

**Excluded**: AWS CDK MCP Server (deprecated, replaced by AWS IaC MCP Server)

## Component Design

### 1. MCP Connector (`connector.py`)

Connects to MCP servers and calls `tools/list`.

```python
class MCPConnector:
    async def connect_stdio(self, command: str, args: list[str], env: dict) -> None
    async def connect_sse(self, url: str) -> None
    async def list_tools(self) -> list[ToolSchema]
    async def disconnect(self) -> None
```

Supports two transport modes:
- **stdio**: spawn process (npx/uvx) and communicate via stdin/stdout
- **SSE**: connect to HTTP SSE endpoint

### 2. Server Registry (`registry.py`)

Maps server names to their execution configs.

```yaml
# registry.yaml
servers:
  aws-core-mcp-server:
    package: "@awslabs/core-mcp-server"
    runtime: npx
    transport: stdio
    category: Core

  aws-dynamodb-mcp-server:
    package: "awslabs.dynamodb-mcp-server"
    runtime: uvx
    transport: stdio
    category: Data & Analytics
```

### 3. Schema Parser (`parser.py`)

Parses MCP tool schemas into an intermediate representation.

```python
@dataclass
class ToolParam:
    name: str
    type: str
    description: str
    required: bool
    default: Any = None

@dataclass
class ToolDefinition:
    server: str
    name: str
    description: str
    params: list[ToolParam]
    aws_service: str | None = None    # detected AWS service
    aws_api_action: str | None = None # detected API action
```

### 4. Static Mapping Registry (`mappings/`)

Known MCP tool → boto3/CLI mappings.

```yaml
# mappings/dynamodb.yaml
tools:
  dynamodb_put_item:
    boto3:
      client: dynamodb
      method: put_item
      params:
        TableName: table_name
        Item: item
    cli:
      command: "aws dynamodb put-item"
      params:
        --table-name: table_name
        --item: item
```

### 5. LLM Mapper (`llm_mapper.py`)

For tools without static mappings, uses Claude API to infer boto3/CLI equivalents.

```python
class LLMMapper:
    async def map_tool(self, tool: ToolDefinition) -> MappingResult:
        """Send tool schema to Claude, get boto3/CLI mapping back."""
```

Prompt template:
```
Given this MCP tool:
- Name: {name}
- Description: {description}
- Parameters: {params}

Generate the equivalent:
1. boto3 function call
2. AWS CLI command
```

### 6. Code Generators (`generators/`)

#### boto3 Generator (`generators/boto3_gen.py`)
```python
# Output example:
def dynamodb_put_item(table_name: str, item: dict, **kwargs) -> dict:
    """Put an item into a DynamoDB table."""
    client = boto3.client('dynamodb')
    return client.put_item(TableName=table_name, Item=item, **kwargs)
```

#### CLI Generator (`generators/cli_gen.py`)
```bash
# Output example:
# dynamodb_put_item: Put an item into a DynamoDB table
aws dynamodb put-item --table-name "$TABLE_NAME" --item "$ITEM"
```

#### Schema Generator (`generators/schema_gen.py`)
```json
{
  "name": "dynamodb_put_item",
  "description": "Put an item into a DynamoDB table",
  "parameters": {
    "type": "object",
    "properties": {
      "table_name": {"type": "string"},
      "item": {"type": "object"}
    },
    "required": ["table_name", "item"]
  }
}
```

#### Skill Generator (`generators/skill_gen.py`)
```markdown
---
name: dynamodb-put-item
description: Put an item into a DynamoDB table
---
## Usage
\`\`\`bash
aws dynamodb put-item --table-name <TABLE> --item '<JSON>'
\`\`\`
## boto3
\`\`\`python
boto3.client('dynamodb').put_item(TableName=table, Item=item)
\`\`\`
```

## CLI Interface

```bash
# Convert all tools from a specific MCP server
mcp-to-cli convert --server aws-dynamodb-mcp-server --output all

# Convert specific output formats
mcp-to-cli convert --server aws-core-mcp-server --output boto3,cli

# Convert all registered servers
mcp-to-cli convert --all --output all

# List available servers
mcp-to-cli list-servers

# List tools from a server (without converting)
mcp-to-cli list-tools --server aws-dynamodb-mcp-server

# Convert with LLM assistance (Phase 3)
mcp-to-cli convert --server aws-eks-mcp-server --output all --llm-assist

# Export server registry
mcp-to-cli registry --export
```

## Output Directory Structure

```
output/
├── aws-core-mcp-server/
│   ├── boto3/
│   │   ├── __init__.py
│   │   └── tools.py
│   ├── cli/
│   │   └── tools.sh
│   ├── schema/
│   │   └── tools.json
│   └── skill/
│       ├── aws-api-call.md
│       ├── cost-explorer-query.md
│       └── ...
├── aws-dynamodb-mcp-server/
│   ├── boto3/
│   │   └── tools.py
│   └── ...
└── _index/
    ├── all-tools.json          # consolidated tool index
    ├── category-map.json       # category → server → tools
    └── mapping-coverage.json   # static vs LLM-mapped stats
```

## Dependencies

- `mcp` - MCP Python SDK (for stdio/SSE transport)
- `boto3` - AWS SDK (for validation of generated code)
- `click` - CLI framework
- `pyyaml` - YAML parsing for registry/mappings
- `anthropic` - Claude API (for Phase 3 LLM mapping)
- `jinja2` - Template engine for code generation
- `rich` - Terminal output formatting

## Project Structure

```
mcp-to-cli/
├── pyproject.toml
├── README.md
├── CLAUDE.md
├── src/
│   └── mcp_to_cli/
│       ├── __init__.py
│       ├── cli.py              # Click CLI entry point
│       ├── connector.py        # MCP server connection
│       ├── parser.py           # Schema parsing
│       ├── registry.py         # Server registry management
│       ├── llm_mapper.py       # LLM-assisted mapping
│       ├── generators/
│       │   ├── __init__.py
│       │   ├── base.py         # Base generator class
│       │   ├── boto3_gen.py    # boto3 code generator
│       │   ├── cli_gen.py      # AWS CLI generator
│       │   ├── schema_gen.py   # OpenAPI/Tool schema generator
│       │   └── skill_gen.py    # Claude Code skill generator
│       ├── mappings/
│       │   ├── dynamodb.yaml
│       │   ├── s3.yaml
│       │   ├── ec2.yaml
│       │   └── ...
│       ├── templates/
│       │   ├── boto3_func.py.j2
│       │   ├── cli_command.sh.j2
│       │   ├── schema_tool.json.j2
│       │   └── skill_tool.md.j2
│       └── registry.yaml       # Server execution configs
├── tests/
│   ├── test_connector.py
│   ├── test_parser.py
│   ├── test_generators.py
│   └── test_registry.py
└── docs/
    └── plans/
        └── 2026-03-08-mcp-to-cli-design.md
```

## Success Criteria

1. Can extract tools from any MCP server via `tools/list`
2. Generates valid, runnable boto3 code for all extracted tools
3. Generates correct AWS CLI commands
4. Generates valid OpenAPI tool schemas for AgentCore Gateway
5. Generates Claude Code skills that can be registered and used
6. Static mappings cover top AWS services (DynamoDB, S3, EC2, Lambda, etc.)
7. LLM fallback handles unmapped tools with >80% accuracy
8. CLI is easy to use: `mcp-to-cli convert --server <name> --output all`
