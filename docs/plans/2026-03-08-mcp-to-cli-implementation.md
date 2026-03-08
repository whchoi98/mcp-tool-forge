# MCP-to-CLI Converter Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Python CLI tool that extracts MCP tool schemas and converts them to boto3 functions, AWS CLI commands, OpenAPI schemas, and Claude Code skills.

**Architecture:** 3-Phase hybrid pipeline — (1) MCP tools/list extraction, (2) static YAML mappings for known services, (3) LLM-assisted inference for unmapped tools. Output to 4 formats via Jinja2 templates.

**Tech Stack:** Python 3.11, Click, MCP SDK, boto3, anthropic, Jinja2, Rich, PyYAML, pytest

---

### Task 1: Project Scaffold and Dependencies

**Files:**
- Create: `pyproject.toml`
- Create: `CLAUDE.md`
- Create: `src/mcp_to_cli/__init__.py`
- Create: `src/mcp_to_cli/generators/__init__.py`
- Create: `tests/__init__.py`

**Step 1: Create pyproject.toml**

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.backends"

[project]
name = "mcp-to-cli"
version = "0.1.0"
description = "Convert MCP server tools to boto3/CLI/schema/skill outputs"
requires-python = ">=3.11"
dependencies = [
    "mcp>=1.0.0",
    "boto3>=1.35.0",
    "click>=8.1.0",
    "pyyaml>=6.0",
    "anthropic>=0.40.0",
    "jinja2>=3.1.0",
    "rich>=13.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.24",
]

[project.scripts]
mcp-to-cli = "mcp_to_cli.cli:main"
```

**Step 2: Create CLAUDE.md**

```markdown
# MCP-to-CLI Converter

Python CLI that converts MCP server tools into boto3/CLI/schema/skill outputs.

## Tech Stack
- Python 3.11, Click CLI, MCP SDK, boto3, anthropic, Jinja2, Rich

## Key Commands
- Run: `python -m mcp_to_cli.cli`
- Test: `python -m pytest tests/ -v`
- Install dev: `pip install -e ".[dev]"`

## Project Structure
- `src/mcp_to_cli/` - main package
- `src/mcp_to_cli/generators/` - 4 output generators
- `src/mcp_to_cli/mappings/` - static YAML mappings
- `src/mcp_to_cli/templates/` - Jinja2 templates
- `tests/` - pytest tests
```

**Step 3: Create package init files**

`src/mcp_to_cli/__init__.py`:
```python
"""MCP-to-CLI: Convert MCP server tools to boto3/CLI/schema/skill outputs."""
__version__ = "0.1.0"
```

`src/mcp_to_cli/generators/__init__.py`:
```python
"""Code generators for different output formats."""
```

`tests/__init__.py`: empty file

**Step 4: Create directories and install**

Run:
```bash
mkdir -p src/mcp_to_cli/generators src/mcp_to_cli/mappings src/mcp_to_cli/templates tests
pip install -e ".[dev]"
```

**Step 5: Verify installation**

Run: `python3.11 -c "import mcp_to_cli; print(mcp_to_cli.__version__)"`
Expected: `0.1.0`

**Step 6: Initialize git and commit**

```bash
cd /home/ec2-user/my-project/mcp-to-cli
git init
git add pyproject.toml CLAUDE.md src/ tests/ docs/
git commit -m "feat: project scaffold with dependencies"
```

---

### Task 2: Data Models

**Files:**
- Create: `src/mcp_to_cli/models.py`
- Create: `tests/test_models.py`

**Step 1: Write the failing test**

`tests/test_models.py`:
```python
from mcp_to_cli.models import ToolParam, ToolDefinition, MappingResult


def test_tool_param_creation():
    param = ToolParam(
        name="table_name",
        type="string",
        description="The DynamoDB table name",
        required=True,
    )
    assert param.name == "table_name"
    assert param.required is True


def test_tool_definition_creation():
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put an item into a DynamoDB table",
        params=[
            ToolParam(name="table_name", type="string", description="Table name", required=True),
            ToolParam(name="item", type="object", description="Item to put", required=True),
        ],
    )
    assert tool.name == "dynamodb_put_item"
    assert len(tool.params) == 2
    assert tool.aws_service is None


def test_tool_definition_with_aws_mapping():
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put an item",
        params=[],
        aws_service="dynamodb",
        aws_api_action="put_item",
    )
    assert tool.aws_service == "dynamodb"
    assert tool.aws_api_action == "put_item"


def test_mapping_result():
    result = MappingResult(
        tool_name="dynamodb_put_item",
        boto3_client="dynamodb",
        boto3_method="put_item",
        boto3_params={"TableName": "table_name", "Item": "item"},
        cli_command="aws dynamodb put-item",
        cli_params={"--table-name": "table_name", "--item": "item"},
        source="static",
    )
    assert result.source == "static"
    assert result.boto3_client == "dynamodb"
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_models.py -v`
Expected: FAIL with `ModuleNotFoundError`

**Step 3: Write minimal implementation**

`src/mcp_to_cli/models.py`:
```python
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


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
    aws_service: str | None = None
    aws_api_action: str | None = None


@dataclass
class MappingResult:
    tool_name: str
    boto3_client: str
    boto3_method: str
    boto3_params: dict[str, str]
    cli_command: str
    cli_params: dict[str, str]
    source: str  # "static" | "llm" | "unknown"


@dataclass
class ServerConfig:
    name: str
    package: str
    runtime: str  # "npx" | "uvx"
    transport: str  # "stdio" | "sse"
    category: str
    env: dict[str, str] = field(default_factory=dict)
    args: list[str] = field(default_factory=list)
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_models.py -v`
Expected: 4 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/models.py tests/test_models.py
git commit -m "feat: add data models (ToolParam, ToolDefinition, MappingResult, ServerConfig)"
```

---

### Task 3: Schema Parser

**Files:**
- Create: `src/mcp_to_cli/parser.py`
- Create: `tests/test_parser.py`

**Step 1: Write the failing test**

`tests/test_parser.py`:
```python
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
    assert tool.params[0].name == "table_name"
    assert tool.params[0].required is True
    assert tool.params[1].name == "item"


def test_parse_tool_with_optional_params():
    raw_schema = {
        "name": "list_tables",
        "description": "List DynamoDB tables",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Max results"},
            },
            "required": [],
        },
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert len(tool.params) == 1
    assert tool.params[0].required is False


def test_parse_tool_no_params():
    raw_schema = {
        "name": "get_status",
        "description": "Get status",
        "inputSchema": {"type": "object", "properties": {}},
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert len(tool.params) == 0


def test_parse_tool_nested_properties():
    raw_schema = {
        "name": "complex_tool",
        "description": "A tool with nested params",
        "inputSchema": {
            "type": "object",
            "properties": {
                "config": {
                    "type": "object",
                    "description": "Configuration object",
                    "properties": {
                        "key": {"type": "string"},
                    },
                },
            },
            "required": ["config"],
        },
    }
    tool = parse_mcp_tool_schema(raw_schema, server="test-server")
    assert tool.params[0].type == "object"
    assert tool.params[0].required is True
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_parser.py -v`
Expected: FAIL

**Step 3: Write minimal implementation**

`src/mcp_to_cli/parser.py`:
```python
from __future__ import annotations

from mcp_to_cli.models import ToolDefinition, ToolParam


def parse_mcp_tool_schema(raw: dict, server: str) -> ToolDefinition:
    """Parse a raw MCP tool schema dict into a ToolDefinition."""
    name = raw["name"]
    description = raw.get("description", "")
    input_schema = raw.get("inputSchema", {})
    properties = input_schema.get("properties", {})
    required_names = set(input_schema.get("required", []))

    params = []
    for param_name, param_info in properties.items():
        params.append(
            ToolParam(
                name=param_name,
                type=param_info.get("type", "string"),
                description=param_info.get("description", ""),
                required=param_name in required_names,
                default=param_info.get("default"),
            )
        )

    return ToolDefinition(
        server=server,
        name=name,
        description=description,
        params=params,
    )


def parse_tools_list(tools_response: list[dict], server: str) -> list[ToolDefinition]:
    """Parse a full tools/list response into ToolDefinitions."""
    return [parse_mcp_tool_schema(t, server) for t in tools_response]
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_parser.py -v`
Expected: 4 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/parser.py tests/test_parser.py
git commit -m "feat: add MCP schema parser"
```

---

### Task 4: Server Registry

**Files:**
- Create: `src/mcp_to_cli/registry.yaml`
- Create: `src/mcp_to_cli/registry.py`
- Create: `tests/test_registry.py`

**Step 1: Write the failing test**

`tests/test_registry.py`:
```python
import tempfile
import os
from pathlib import Path
from mcp_to_cli.registry import ServerRegistry


def test_load_registry():
    registry = ServerRegistry()
    servers = registry.list_servers()
    assert len(servers) > 0


def test_get_server_config():
    registry = ServerRegistry()
    config = registry.get("aws-dynamodb-mcp-server")
    assert config is not None
    assert config.runtime in ("npx", "uvx")
    assert config.transport in ("stdio", "sse")


def test_get_nonexistent_server():
    registry = ServerRegistry()
    config = registry.get("nonexistent-server")
    assert config is None


def test_list_by_category():
    registry = ServerRegistry()
    data_servers = registry.list_by_category("Data & Analytics")
    assert len(data_servers) > 0


def test_load_custom_registry():
    yaml_content = """
servers:
  test-server:
    package: "test-package"
    runtime: npx
    transport: stdio
    category: Test
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(yaml_content)
        f.flush()
        registry = ServerRegistry(path=Path(f.name))
        config = registry.get("test-server")
        assert config is not None
        assert config.package == "test-package"
    os.unlink(f.name)
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_registry.py -v`
Expected: FAIL

**Step 3: Create registry.yaml**

Create `src/mcp_to_cli/registry.yaml` with all 65 servers organized by category.
Refer to https://github.com/awslabs/mcp for correct package names per server.

Each entry format:
```yaml
servers:
  server-name:
    package: "package-name"
    runtime: npx|uvx
    transport: stdio|sse
    category: "Category Name"
    description: "Brief description"
```

Include all servers from the design doc (Essential Setup, Documentation, Core,
Infrastructure & Deployment, AI & Machine Learning, Data & Analytics,
Developer Tools & Support, Integration & Messaging, Cost & Operations,
Healthcare & Lifesciences). Exclude AWS CDK MCP Server (deprecated).

**Step 4: Write registry.py**

`src/mcp_to_cli/registry.py`:
```python
from __future__ import annotations

from pathlib import Path

import yaml

from mcp_to_cli.models import ServerConfig

_DEFAULT_REGISTRY = Path(__file__).parent / "registry.yaml"


class ServerRegistry:
    def __init__(self, path: Path | None = None):
        self._path = path or _DEFAULT_REGISTRY
        self._servers: dict[str, ServerConfig] = {}
        self._load()

    def _load(self) -> None:
        with open(self._path) as f:
            data = yaml.safe_load(f)
        for name, info in data.get("servers", {}).items():
            self._servers[name] = ServerConfig(
                name=name,
                package=info["package"],
                runtime=info["runtime"],
                transport=info["transport"],
                category=info["category"],
                env=info.get("env", {}),
                args=info.get("args", []),
            )

    def get(self, name: str) -> ServerConfig | None:
        return self._servers.get(name)

    def list_servers(self) -> list[ServerConfig]:
        return list(self._servers.values())

    def list_by_category(self, category: str) -> list[ServerConfig]:
        return [s for s in self._servers.values() if s.category == category]

    def categories(self) -> list[str]:
        return sorted(set(s.category for s in self._servers.values()))
```

**Step 5: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_registry.py -v`
Expected: 5 PASSED

**Step 6: Commit**

```bash
git add src/mcp_to_cli/registry.py src/mcp_to_cli/registry.yaml tests/test_registry.py
git commit -m "feat: add server registry with 65 AWS MCP servers"
```

---

### Task 5: MCP Connector

**Files:**
- Create: `src/mcp_to_cli/connector.py`
- Create: `tests/test_connector.py`

**Step 1: Write the failing test**

`tests/test_connector.py`:
```python
import pytest
from unittest.mock import AsyncMock, patch
from mcp_to_cli.connector import MCPConnector


@pytest.mark.asyncio
async def test_list_tools_returns_parsed_schemas():
    mock_tools = [
        {
            "name": "test_tool",
            "description": "A test tool",
            "inputSchema": {
                "type": "object",
                "properties": {"param1": {"type": "string"}},
                "required": ["param1"],
            },
        }
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
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_connector.py -v`
Expected: FAIL

**Step 3: Write implementation**

`src/mcp_to_cli/connector.py`:
```python
from __future__ import annotations

import asyncio
import json
import os
from typing import Any

from mcp_to_cli.models import ServerConfig


class MCPConnector:
    """Connects to MCP servers and extracts tool schemas."""

    def __init__(self):
        self._process: asyncio.subprocess.Process | None = None

    def _build_command(
        self, runtime: str, package: str, extra_args: list[str]
    ) -> tuple[str, list[str]]:
        if runtime == "npx":
            return "npx", ["-y", package] + extra_args
        elif runtime == "uvx":
            return "uvx", [package] + extra_args
        else:
            raise ValueError(f"Unknown runtime: {runtime}")

    async def connect_stdio(self, config: ServerConfig) -> None:
        """Start MCP server as subprocess via stdio."""
        cmd, args = self._build_command(config.runtime, config.package, config.args)
        env = {**os.environ, **config.env}
        self._process = await asyncio.create_subprocess_exec(
            cmd,
            *args,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )

    async def _send_jsonrpc(self, method: str, params: dict | None = None) -> dict:
        """Send a JSON-RPC request and read the response."""
        if not self._process or not self._process.stdin or not self._process.stdout:
            raise RuntimeError("Not connected to any MCP server")

        request: dict[str, Any] = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
        }
        if params:
            request["params"] = params

        msg = json.dumps(request)
        content = f"Content-Length: {len(msg)}\r\n\r\n{msg}"
        self._process.stdin.write(content.encode())
        await self._process.stdin.drain()

        # Read response headers
        headers: dict[str, str] = {}
        while True:
            line = await self._process.stdout.readline()
            line_str = line.decode().strip()
            if not line_str:
                break
            if ":" in line_str:
                key, value = line_str.split(":", 1)
                headers[key.strip()] = value.strip()

        content_length = int(headers.get("Content-Length", 0))
        if content_length > 0:
            body = await self._process.stdout.readexactly(content_length)
            return json.loads(body)
        return {}

    async def _call_tools_list(self) -> list[dict]:
        """Call tools/list on the connected MCP server."""
        # First send initialize
        await self._send_jsonrpc("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "mcp-to-cli", "version": "0.1.0"},
        })
        # Send initialized notification
        notif = json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"})
        content = f"Content-Length: {len(notif)}\r\n\r\n{notif}"
        if self._process and self._process.stdin:
            self._process.stdin.write(content.encode())
            await self._process.stdin.drain()

        # Now list tools
        response = await self._send_jsonrpc("tools/list")
        return response.get("result", {}).get("tools", [])

    async def list_tools(self) -> list[dict]:
        """Get tool schemas from connected MCP server."""
        return await self._call_tools_list()

    async def list_tools_from_config(self, config: ServerConfig) -> list[dict]:
        """Connect to server, list tools, disconnect."""
        try:
            await self.connect_stdio(config)
            return await asyncio.wait_for(self.list_tools(), timeout=30)
        finally:
            await self.disconnect()

    async def disconnect(self) -> None:
        if self._process:
            try:
                self._process.terminate()
                await asyncio.wait_for(self._process.wait(), timeout=5)
            except (asyncio.TimeoutError, ProcessLookupError):
                self._process.kill()
            self._process = None
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_connector.py -v`
Expected: 3 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/connector.py tests/test_connector.py
git commit -m "feat: add MCP connector with stdio JSON-RPC transport"
```

---

### Task 6: Jinja2 Templates

**Files:**
- Create: `src/mcp_to_cli/templates/boto3_func.py.j2`
- Create: `src/mcp_to_cli/templates/boto3_module.py.j2`
- Create: `src/mcp_to_cli/templates/cli_command.sh.j2`
- Create: `src/mcp_to_cli/templates/cli_module.sh.j2`
- Create: `src/mcp_to_cli/templates/schema_tool.json.j2`
- Create: `src/mcp_to_cli/templates/skill_tool.md.j2`

**Step 1: Create all 6 template files**

See the design document for exact template content. Each template uses
Jinja2 syntax with `tool`, `mapping`, and helper variables.

Key templates:
- `boto3_func.py.j2` - Single boto3 function
- `boto3_module.py.j2` - Module wrapper with imports
- `cli_command.sh.j2` - Single bash function
- `cli_module.sh.j2` - Shell script wrapper
- `schema_tool.json.j2` - OpenAPI tool schema JSON
- `skill_tool.md.j2` - Claude Code skill markdown with YAML frontmatter

**Step 2: Commit**

```bash
git add src/mcp_to_cli/templates/
git commit -m "feat: add Jinja2 templates for all 4 output formats"
```

---

### Task 7: Code Generators

**Files:**
- Create: `src/mcp_to_cli/generators/base.py`
- Create: `src/mcp_to_cli/generators/boto3_gen.py`
- Create: `src/mcp_to_cli/generators/cli_gen.py`
- Create: `src/mcp_to_cli/generators/schema_gen.py`
- Create: `src/mcp_to_cli/generators/skill_gen.py`
- Modify: `src/mcp_to_cli/generators/__init__.py`
- Create: `tests/test_generators.py`

**Step 1: Write failing tests**

`tests/test_generators.py`:
```python
import json
from mcp_to_cli.models import ToolDefinition, ToolParam, MappingResult
from mcp_to_cli.generators.boto3_gen import Boto3Generator
from mcp_to_cli.generators.cli_gen import CliGenerator
from mcp_to_cli.generators.schema_gen import SchemaGenerator
from mcp_to_cli.generators.skill_gen import SkillGenerator


def _make_tool():
    return ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put an item into a DynamoDB table",
        params=[
            ToolParam(name="table_name", type="string", description="Table name", required=True),
            ToolParam(name="item", type="object", description="Item to put", required=True),
            ToolParam(name="condition", type="string", description="Condition expression", required=False),
        ],
    )


def _make_mapping():
    return MappingResult(
        tool_name="dynamodb_put_item",
        boto3_client="dynamodb",
        boto3_method="put_item",
        boto3_params={"TableName": "table_name", "Item": "item", "ConditionExpression": "condition"},
        cli_command="aws dynamodb put-item",
        cli_params={"--table-name": "table_name", "--item": "item", "--condition-expression": "condition"},
        source="static",
    )


def test_boto3_generator_produces_valid_python():
    gen = Boto3Generator()
    code = gen.generate_function(_make_tool(), _make_mapping())
    assert "def dynamodb_put_item(" in code
    assert "boto3.client('dynamodb')" in code
    assert "put_item(" in code


def test_boto3_generator_module():
    gen = Boto3Generator()
    code = gen.generate_module("aws-dynamodb-mcp-server", [(_make_tool(), _make_mapping())])
    assert "import boto3" in code


def test_cli_generator_produces_bash():
    gen = CliGenerator()
    code = gen.generate_function(_make_tool(), _make_mapping())
    assert "aws dynamodb put-item" in code


def test_schema_generator_produces_json():
    gen = SchemaGenerator()
    output = gen.generate_schema(_make_tool())
    data = json.loads(output)
    assert data["name"] == "dynamodb_put_item"
    assert "table_name" in data["parameters"]["properties"]


def test_skill_generator_produces_markdown():
    gen = SkillGenerator()
    output = gen.generate_skill(_make_tool(), _make_mapping())
    assert "name: dynamodb-put-item" in output
    assert "boto3" in output
    assert "aws dynamodb put-item" in output
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_generators.py -v`
Expected: FAIL

**Step 3: Write all generator files**

`src/mcp_to_cli/generators/base.py`:
```python
from __future__ import annotations
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

_TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

def get_template_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(_TEMPLATE_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
```

`src/mcp_to_cli/generators/boto3_gen.py`:
```python
from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition

class Boto3Generator:
    def __init__(self):
        self._env = get_template_env()

    def _param_signature(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        parts = []
        type_map = {"string": "str", "object": "dict", "integer": "int", "boolean": "bool", "array": "list"}
        for p in tool.params:
            if p.required:
                parts.append(f"{p.name}: {type_map.get(p.type, 'Any')}")
        for p in tool.params:
            if not p.required:
                parts.append(f"{p.name}: {type_map.get(p.type, 'Any')} | None = None")
        parts.append("**kwargs")
        return ", ".join(parts)

    def generate_function(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        template = self._env.get_template("boto3_func.py.j2")
        return template.render(
            tool=tool, mapping=mapping,
            param_signature=self._param_signature(tool, mapping),
        )

    def generate_module(self, server_name: str, tools: list[tuple[ToolDefinition, MappingResult]]) -> str:
        functions = [self.generate_function(t, m) for t, m in tools]
        template = self._env.get_template("boto3_module.py.j2")
        return template.render(server_name=server_name, functions=functions)
```

`src/mcp_to_cli/generators/cli_gen.py`:
```python
from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition

class CliGenerator:
    def __init__(self):
        self._env = get_template_env()

    def generate_function(self, tool: ToolDefinition, mapping: MappingResult) -> str:
        template = self._env.get_template("cli_command.sh.j2")
        return template.render(tool=tool, mapping=mapping)

    def generate_module(self, server_name: str, tools: list[tuple[ToolDefinition, MappingResult]]) -> str:
        functions = [self.generate_function(t, m) for t, m in tools]
        template = self._env.get_template("cli_module.sh.j2")
        return template.render(server_name=server_name, functions=functions)
```

`src/mcp_to_cli/generators/schema_gen.py`:
```python
from __future__ import annotations
import json
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import ToolDefinition

class SchemaGenerator:
    def __init__(self):
        self._env = get_template_env()

    def generate_schema(self, tool: ToolDefinition) -> str:
        template = self._env.get_template("schema_tool.json.j2")
        return template.render(tool=tool)

    def generate_module(self, server_name: str, tools: list[ToolDefinition]) -> str:
        schemas = [json.loads(self.generate_schema(t)) for t in tools]
        return json.dumps({"server": server_name, "tools": schemas}, indent=2)
```

`src/mcp_to_cli/generators/skill_gen.py`:
```python
from __future__ import annotations
from mcp_to_cli.generators.base import get_template_env
from mcp_to_cli.models import MappingResult, ToolDefinition

class SkillGenerator:
    def __init__(self):
        self._env = get_template_env()

    def generate_skill(self, tool: ToolDefinition, mapping: MappingResult | None = None) -> str:
        template = self._env.get_template("skill_tool.md.j2")
        return template.render(tool=tool, mapping=mapping)
```

Update `src/mcp_to_cli/generators/__init__.py`:
```python
"""Code generators for different output formats."""
from mcp_to_cli.generators.boto3_gen import Boto3Generator
from mcp_to_cli.generators.cli_gen import CliGenerator
from mcp_to_cli.generators.schema_gen import SchemaGenerator
from mcp_to_cli.generators.skill_gen import SkillGenerator

__all__ = ["Boto3Generator", "CliGenerator", "SchemaGenerator", "SkillGenerator"]
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_generators.py -v`
Expected: 5 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/generators/ tests/test_generators.py
git commit -m "feat: add 4 code generators (boto3, cli, schema, skill)"
```

---

### Task 8: Static Mapping Registry

**Files:**
- Create: `src/mcp_to_cli/mappings/dynamodb.yaml`
- Create: `src/mcp_to_cli/mapping_loader.py`
- Create: `tests/test_mapping_loader.py`

**Step 1: Write failing test**

`tests/test_mapping_loader.py`:
```python
from mcp_to_cli.mapping_loader import MappingLoader
from mcp_to_cli.models import ToolDefinition, ToolParam


def test_load_static_mapping():
    loader = MappingLoader()
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put item",
        params=[ToolParam(name="table_name", type="string", description="", required=True)],
    )
    result = loader.find_mapping(tool)
    assert result is not None
    assert result.boto3_client == "dynamodb"
    assert result.source == "static"


def test_no_mapping_returns_none():
    loader = MappingLoader()
    tool = ToolDefinition(
        server="unknown-server",
        name="unknown_tool",
        description="Unknown",
        params=[],
    )
    result = loader.find_mapping(tool)
    assert result is None
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_mapping_loader.py -v`
Expected: FAIL

**Step 3: Create dynamodb.yaml mapping and mapping_loader.py**

`src/mcp_to_cli/mappings/dynamodb.yaml`:
```yaml
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

  dynamodb_get_item:
    boto3:
      client: dynamodb
      method: get_item
      params:
        TableName: table_name
        Key: key
    cli:
      command: "aws dynamodb get-item"
      params:
        --table-name: table_name
        --key: key

  dynamodb_query:
    boto3:
      client: dynamodb
      method: query
      params:
        TableName: table_name
        KeyConditionExpression: key_condition
    cli:
      command: "aws dynamodb query"
      params:
        --table-name: table_name
        --key-condition-expression: key_condition

  dynamodb_scan:
    boto3:
      client: dynamodb
      method: scan
      params:
        TableName: table_name
    cli:
      command: "aws dynamodb scan"
      params:
        --table-name: table_name

  dynamodb_delete_item:
    boto3:
      client: dynamodb
      method: delete_item
      params:
        TableName: table_name
        Key: key
    cli:
      command: "aws dynamodb delete-item"
      params:
        --table-name: table_name
        --key: key

  dynamodb_update_item:
    boto3:
      client: dynamodb
      method: update_item
      params:
        TableName: table_name
        Key: key
        UpdateExpression: update_expression
    cli:
      command: "aws dynamodb update-item"
      params:
        --table-name: table_name
        --key: key
        --update-expression: update_expression
```

`src/mcp_to_cli/mapping_loader.py`:
```python
from __future__ import annotations
from pathlib import Path
import yaml
from mcp_to_cli.models import MappingResult, ToolDefinition

_MAPPINGS_DIR = Path(__file__).parent / "mappings"

class MappingLoader:
    def __init__(self, mappings_dir: Path | None = None):
        self._dir = mappings_dir or _MAPPINGS_DIR
        self._mappings: dict[str, dict] = {}
        self._load_all()

    def _load_all(self) -> None:
        if not self._dir.exists():
            return
        for yaml_file in self._dir.glob("*.yaml"):
            with open(yaml_file) as f:
                data = yaml.safe_load(f)
            for tool_name, mapping in data.get("tools", {}).items():
                self._mappings[tool_name] = mapping

    def find_mapping(self, tool: ToolDefinition) -> MappingResult | None:
        mapping = self._mappings.get(tool.name)
        if not mapping:
            return None
        boto3_info = mapping.get("boto3", {})
        cli_info = mapping.get("cli", {})
        return MappingResult(
            tool_name=tool.name,
            boto3_client=boto3_info.get("client", ""),
            boto3_method=boto3_info.get("method", ""),
            boto3_params=boto3_info.get("params", {}),
            cli_command=cli_info.get("command", ""),
            cli_params=cli_info.get("params", {}),
            source="static",
        )
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_mapping_loader.py -v`
Expected: 2 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/mapping_loader.py src/mcp_to_cli/mappings/ tests/test_mapping_loader.py
git commit -m "feat: add static mapping loader with DynamoDB mappings"
```

---

### Task 9: LLM Mapper (Phase 3)

**Files:**
- Create: `src/mcp_to_cli/llm_mapper.py`
- Create: `tests/test_llm_mapper.py`

**Step 1: Write failing test**

`tests/test_llm_mapper.py`:
```python
import json
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from mcp_to_cli.llm_mapper import LLMMapper
from mcp_to_cli.models import ToolDefinition, ToolParam


@pytest.mark.asyncio
async def test_llm_mapper_returns_mapping():
    tool = ToolDefinition(
        server="test-server",
        name="eks_describe_cluster",
        description="Describe an EKS cluster",
        params=[ToolParam(name="cluster_name", type="string", description="Cluster name", required=True)],
    )

    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = json.dumps({
        "boto3_client": "eks",
        "boto3_method": "describe_cluster",
        "boto3_params": {"name": "cluster_name"},
        "cli_command": "aws eks describe-cluster",
        "cli_params": {"--name": "cluster_name"},
    })

    with patch("mcp_to_cli.llm_mapper.anthropic") as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create = AsyncMock(return_value=mock_response)
        mock_anthropic.AsyncAnthropic.return_value = mock_client

        mapper = LLMMapper()
        result = await mapper.map_tool(tool)

        assert result is not None
        assert result.boto3_client == "eks"
        assert result.source == "llm"


def test_build_prompt():
    tool = ToolDefinition(
        server="test-server",
        name="s3_list_buckets",
        description="List S3 buckets",
        params=[],
    )
    mapper = LLMMapper()
    prompt = mapper._build_prompt(tool)
    assert "s3_list_buckets" in prompt
    assert "List S3 buckets" in prompt
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_llm_mapper.py -v`
Expected: FAIL

**Step 3: Write implementation**

`src/mcp_to_cli/llm_mapper.py`:
```python
from __future__ import annotations
import json
import anthropic
from mcp_to_cli.models import MappingResult, ToolDefinition

_SYSTEM_PROMPT = """You are an AWS API expert. Given an MCP tool definition, determine the equivalent boto3 and AWS CLI calls.

Respond ONLY with valid JSON in this exact format:
{
  "boto3_client": "<service-name>",
  "boto3_method": "<method_name>",
  "boto3_params": {"<BotoParamName>": "<mcp_param_name>", ...},
  "cli_command": "aws <service> <command>",
  "cli_params": {"--<flag>": "<mcp_param_name>", ...}
}

If the tool does not map to a single boto3/CLI call, set all values to empty strings."""

class LLMMapper:
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self._model = model

    def _build_prompt(self, tool: ToolDefinition) -> str:
        params_desc = "\n".join(
            f"  - {p.name} ({p.type}, {'required' if p.required else 'optional'}): {p.description}"
            for p in tool.params
        )
        return f"""MCP Tool:
- Name: {tool.name}
- Server: {tool.server}
- Description: {tool.description}
- Parameters:
{params_desc if params_desc else '  (none)'}

What is the equivalent boto3 and AWS CLI call?"""

    async def map_tool(self, tool: ToolDefinition) -> MappingResult | None:
        client = anthropic.AsyncAnthropic()
        response = await client.messages.create(
            model=self._model,
            max_tokens=1024,
            system=_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": self._build_prompt(tool)}],
        )

        try:
            text = response.content[0].text
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            data = json.loads(text.strip())

            if not data.get("boto3_client"):
                return None

            return MappingResult(
                tool_name=tool.name,
                boto3_client=data["boto3_client"],
                boto3_method=data["boto3_method"],
                boto3_params=data.get("boto3_params", {}),
                cli_command=data["cli_command"],
                cli_params=data.get("cli_params", {}),
                source="llm",
            )
        except (json.JSONDecodeError, KeyError, IndexError):
            return None
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_llm_mapper.py -v`
Expected: 2 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/llm_mapper.py tests/test_llm_mapper.py
git commit -m "feat: add LLM-assisted mapper using Claude API"
```

---

### Task 10: Pipeline Orchestrator

**Files:**
- Create: `src/mcp_to_cli/pipeline.py`
- Create: `tests/test_pipeline.py`

**Step 1: Write failing test**

`tests/test_pipeline.py`:
```python
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, patch
from mcp_to_cli.pipeline import Pipeline
from mcp_to_cli.models import ServerConfig


@pytest.mark.asyncio
async def test_pipeline_extract_and_generate(tmp_path):
    mock_tools = [
        {
            "name": "dynamodb_put_item",
            "description": "Put an item into DynamoDB",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "table_name": {"type": "string", "description": "Table"},
                    "item": {"type": "object", "description": "Item"},
                },
                "required": ["table_name", "item"],
            },
        }
    ]

    config = ServerConfig(
        name="aws-dynamodb-mcp-server",
        package="awslabs.aws-dynamodb-mcp-server",
        runtime="uvx",
        transport="stdio",
        category="Data & Analytics",
    )

    pipeline = Pipeline(output_dir=tmp_path)

    with patch.object(pipeline, "_extract_tools", new_callable=AsyncMock) as mock_extract:
        mock_extract.return_value = mock_tools
        result = await pipeline.run(config, outputs=["schema"], llm_assist=False)

    assert result["server"] == "aws-dynamodb-mcp-server"
    assert result["tools_count"] == 1
    schema_file = tmp_path / "aws-dynamodb-mcp-server" / "schema" / "tools.json"
    assert schema_file.exists()
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_pipeline.py -v`
Expected: FAIL

**Step 3: Write implementation**

`src/mcp_to_cli/pipeline.py`:
```python
from __future__ import annotations
import json
from pathlib import Path
from rich.console import Console
from mcp_to_cli.connector import MCPConnector
from mcp_to_cli.generators import Boto3Generator, CliGenerator, SchemaGenerator, SkillGenerator
from mcp_to_cli.llm_mapper import LLMMapper
from mcp_to_cli.mapping_loader import MappingLoader
from mcp_to_cli.models import MappingResult, ServerConfig, ToolDefinition
from mcp_to_cli.parser import parse_tools_list

console = Console()

class Pipeline:
    def __init__(self, output_dir: Path | None = None):
        self._output_dir = output_dir or Path("output")
        self._connector = MCPConnector()
        self._mapping_loader = MappingLoader()
        self._llm_mapper = LLMMapper()
        self._boto3_gen = Boto3Generator()
        self._cli_gen = CliGenerator()
        self._schema_gen = SchemaGenerator()
        self._skill_gen = SkillGenerator()

    async def _extract_tools(self, config: ServerConfig) -> list[dict]:
        return await self._connector.list_tools_from_config(config)

    def _resolve_mapping(self, tool: ToolDefinition) -> MappingResult | None:
        return self._mapping_loader.find_mapping(tool)

    async def _resolve_mapping_with_llm(self, tool: ToolDefinition) -> MappingResult | None:
        return await self._llm_mapper.map_tool(tool)

    async def run(
        self,
        config: ServerConfig,
        outputs: list[str] | None = None,
        llm_assist: bool = False,
    ) -> dict:
        outputs = outputs or ["boto3", "cli", "schema", "skill"]
        server_dir = self._output_dir / config.name

        # Phase 1: Extract
        console.print(f"[bold blue]Phase 1:[/] Extracting tools from {config.name}...")
        raw_tools = await self._extract_tools(config)
        tools = parse_tools_list(raw_tools, config.name)
        console.print(f"  Found {len(tools)} tools")

        # Phase 2 & 3: Map
        mapped: list[tuple[ToolDefinition, MappingResult | None]] = []
        static_count = 0
        llm_count = 0

        for tool in tools:
            mapping = self._resolve_mapping(tool)
            if mapping:
                static_count += 1
            elif llm_assist:
                console.print(f"  [yellow]LLM mapping:[/] {tool.name}")
                mapping = await self._resolve_mapping_with_llm(tool)
                if mapping:
                    llm_count += 1
            mapped.append((tool, mapping))

        console.print(f"  Mapped: {static_count} static, {llm_count} LLM, {len(tools) - static_count - llm_count} unmapped")

        # Generate outputs
        for output_type in outputs:
            if output_type == "boto3":
                self._write_boto3(server_dir, config.name, mapped)
            elif output_type == "cli":
                self._write_cli(server_dir, config.name, mapped)
            elif output_type == "schema":
                self._write_schema(server_dir, config.name, tools)
            elif output_type == "skill":
                self._write_skills(server_dir, mapped)

        return {
            "server": config.name,
            "tools_count": len(tools),
            "static_mapped": static_count,
            "llm_mapped": llm_count,
            "unmapped": len(tools) - static_count - llm_count,
            "outputs": outputs,
        }

    def _write_boto3(self, server_dir: Path, server_name: str, mapped: list[tuple]) -> None:
        out_dir = server_dir / "boto3"
        out_dir.mkdir(parents=True, exist_ok=True)
        with_mapping = [(t, m) for t, m in mapped if m is not None]
        if not with_mapping:
            return
        code = self._boto3_gen.generate_module(server_name, with_mapping)
        (out_dir / "tools.py").write_text(code)
        (out_dir / "__init__.py").write_text("")
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.py'}")

    def _write_cli(self, server_dir: Path, server_name: str, mapped: list[tuple]) -> None:
        out_dir = server_dir / "cli"
        out_dir.mkdir(parents=True, exist_ok=True)
        with_mapping = [(t, m) for t, m in mapped if m is not None]
        if not with_mapping:
            return
        code = self._cli_gen.generate_module(server_name, with_mapping)
        (out_dir / "tools.sh").write_text(code)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.sh'}")

    def _write_schema(self, server_dir: Path, server_name: str, tools: list[ToolDefinition]) -> None:
        out_dir = server_dir / "schema"
        out_dir.mkdir(parents=True, exist_ok=True)
        code = self._schema_gen.generate_module(server_name, tools)
        (out_dir / "tools.json").write_text(code)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.json'}")

    def _write_skills(self, server_dir: Path, mapped: list[tuple]) -> None:
        out_dir = server_dir / "skill"
        out_dir.mkdir(parents=True, exist_ok=True)
        for tool, mapping in mapped:
            skill_content = self._skill_gen.generate_skill(tool, mapping)
            filename = tool.name.replace("_", "-") + ".md"
            (out_dir / filename).write_text(skill_content)
        console.print(f"  [green]Wrote:[/] {len(mapped)} skills to {out_dir}")
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_pipeline.py -v`
Expected: 1 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/pipeline.py tests/test_pipeline.py
git commit -m "feat: add pipeline orchestrator (extract -> map -> generate)"
```

---

### Task 11: CLI Interface (Click)

**Files:**
- Create: `src/mcp_to_cli/cli.py`
- Create: `tests/test_cli.py`

**Step 1: Write failing test**

`tests/test_cli.py`:
```python
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
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_cli.py -v`
Expected: FAIL

**Step 3: Write implementation**

`src/mcp_to_cli/cli.py`:
```python
from __future__ import annotations
import asyncio
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from mcp_to_cli.pipeline import Pipeline
from mcp_to_cli.registry import ServerRegistry

console = Console()

@click.group()
@click.version_option(version="0.1.0", prog_name="mcp-to-cli")
def main():
    """MCP-to-CLI: Convert MCP server tools to boto3/CLI/schema/skill outputs."""
    pass

@main.command()
@click.option("--category", "-c", help="Filter by category")
def list_servers(category):
    """List all registered MCP servers."""
    registry = ServerRegistry()
    if category:
        servers = registry.list_by_category(category)
    else:
        servers = registry.list_servers()

    table = Table(title="Registered MCP Servers")
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="green")
    table.add_column("Runtime", style="yellow")
    table.add_column("Package", style="dim")

    for s in sorted(servers, key=lambda x: (x.category, x.name)):
        table.add_row(s.name, s.category, s.runtime, s.package)

    console.print(table)
    console.print(f"\nTotal: {len(servers)} servers")

@main.command()
@click.option("--server", "-s", required=True, help="Server name from registry")
def list_tools(server):
    """List tools from an MCP server (connects to server)."""
    registry = ServerRegistry()
    config = registry.get(server)
    if not config:
        console.print(f"[red]Error:[/] Server '{server}' not found in registry")
        raise SystemExit(1)

    from mcp_to_cli.connector import MCPConnector

    async def _list():
        connector = MCPConnector()
        tools = await connector.list_tools_from_config(config)
        table = Table(title=f"Tools from {server}")
        table.add_column("Name", style="cyan")
        table.add_column("Description")
        table.add_column("Params", style="yellow")
        for t in tools:
            params = ", ".join(t.get("inputSchema", {}).get("properties", {}).keys())
            table.add_row(t["name"], t.get("description", "")[:80], params)
        console.print(table)
        console.print(f"\nTotal: {len(tools)} tools")

    asyncio.run(_list())

@main.command()
@click.option("--server", "-s", help="Server name (or --all-servers)")
@click.option("--all-servers", "all_flag", is_flag=True, help="Convert all servers")
@click.option("--output", "-o", default="all", help="Output formats: boto3,cli,schema,skill,all")
@click.option("--llm-assist", is_flag=True, help="Use LLM for unmapped tools (Phase 3)")
@click.option("--output-dir", "-d", default="output", help="Output directory")
def convert(server, all_flag, output, llm_assist, output_dir):
    """Convert MCP tools to boto3/CLI/schema/skill outputs."""
    if not server and not all_flag:
        console.print("[red]Error:[/] Specify --server or --all-servers")
        raise SystemExit(1)

    outputs = ["boto3", "cli", "schema", "skill"] if output == "all" else output.split(",")
    registry = ServerRegistry()
    out_path = Path(output_dir)

    if all_flag:
        configs = registry.list_servers()
    else:
        config = registry.get(server)
        if not config:
            console.print(f"[red]Error:[/] Server '{server}' not found")
            raise SystemExit(1)
        configs = [config]

    async def _convert():
        pipeline = Pipeline(output_dir=out_path)
        results = []
        for cfg in configs:
            try:
                result = await pipeline.run(cfg, outputs=outputs, llm_assist=llm_assist)
                results.append(result)
            except Exception as e:
                console.print(f"[red]Error[/] converting {cfg.name}: {e}")
                results.append({"server": cfg.name, "error": str(e)})

        console.print("\n[bold]Summary:[/]")
        table = Table()
        table.add_column("Server", style="cyan")
        table.add_column("Tools")
        table.add_column("Static")
        table.add_column("LLM")
        table.add_column("Unmapped")
        for r in results:
            if "error" in r:
                table.add_row(r["server"], "[red]ERROR[/]", "", "", "")
            else:
                table.add_row(
                    r["server"],
                    str(r["tools_count"]),
                    str(r["static_mapped"]),
                    str(r["llm_mapped"]),
                    str(r["unmapped"]),
                )
        console.print(table)

    asyncio.run(_convert())

if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_cli.py -v`
Expected: 3 PASSED

**Step 5: Commit**

```bash
git add src/mcp_to_cli/cli.py tests/test_cli.py
git commit -m "feat: add Click CLI with list-servers, list-tools, convert commands"
```

---

### Task 12: Schema Cache Layer

**Files:**
- Create: `src/mcp_to_cli/cache.py`
- Create: `tests/test_cache.py`
- Modify: `src/mcp_to_cli/pipeline.py`

**Step 1: Write failing test**

`tests/test_cache.py`:
```python
from mcp_to_cli.cache import SchemaCache


def test_cache_save_and_load(tmp_path):
    cache = SchemaCache(cache_dir=tmp_path)
    tools = [{"name": "test", "description": "Test", "inputSchema": {}}]
    cache.save("test-server", tools)
    loaded = cache.load("test-server")
    assert loaded == tools


def test_cache_miss(tmp_path):
    cache = SchemaCache(cache_dir=tmp_path)
    assert cache.load("nonexistent") is None
```

**Step 2: Run test to verify it fails**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/test_cache.py -v`
Expected: FAIL

**Step 3: Write implementation**

`src/mcp_to_cli/cache.py`:
```python
from __future__ import annotations
import json
from pathlib import Path

class SchemaCache:
    def __init__(self, cache_dir: Path | None = None):
        self._dir = cache_dir or Path.home() / ".mcp-to-cli" / "cache"
        self._dir.mkdir(parents=True, exist_ok=True)

    def save(self, server_name: str, tools: list[dict]) -> None:
        path = self._dir / f"{server_name}.json"
        path.write_text(json.dumps(tools, indent=2))

    def load(self, server_name: str) -> list[dict] | None:
        path = self._dir / f"{server_name}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text())

    def clear(self, server_name: str | None = None) -> None:
        if server_name:
            path = self._dir / f"{server_name}.json"
            if path.exists():
                path.unlink()
        else:
            for f in self._dir.glob("*.json"):
                f.unlink()
```

**Step 4: Integrate cache into Pipeline**

In `src/mcp_to_cli/pipeline.py`, add cache import and modify `_extract_tools`:

```python
# Add import at top:
from mcp_to_cli.cache import SchemaCache

# In __init__, add:
self._cache = SchemaCache()

# Replace _extract_tools with:
async def _extract_tools(self, config: ServerConfig, use_cache: bool = True) -> list[dict]:
    if use_cache:
        cached = self._cache.load(config.name)
        if cached:
            console.print(f"  [dim]Using cached schema ({len(cached)} tools)[/]")
            return cached
    tools = await self._connector.list_tools_from_config(config)
    self._cache.save(config.name, tools)
    return tools
```

**Step 5: Run all tests**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/ -v`
Expected: All PASSED

**Step 6: Commit**

```bash
git add src/mcp_to_cli/cache.py tests/test_cache.py src/mcp_to_cli/pipeline.py
git commit -m "feat: add schema cache to avoid repeated MCP server connections"
```

---

### Task 13: Full Integration Test and Smoke Test

**Step 1: Run full test suite**

Run: `cd /home/ec2-user/my-project/mcp-to-cli && python3.11 -m pytest tests/ -v`
Expected: All tests pass

**Step 2: Smoke test CLI**

```bash
cd /home/ec2-user/my-project/mcp-to-cli
python3.11 -m mcp_to_cli.cli list-servers
python3.11 -m mcp_to_cli.cli list-servers --category "Data & Analytics"
python3.11 -m mcp_to_cli.cli --version
```

Expected: Tables printed with server listings

**Step 3: Test with a real MCP server (if available)**

```bash
python3.11 -m mcp_to_cli.cli list-tools --server aws-dynamodb-mcp-server
python3.11 -m mcp_to_cli.cli convert --server aws-dynamodb-mcp-server --output schema
ls -la output/aws-dynamodb-mcp-server/schema/
```

**Step 4: Final commit**

```bash
git add -A
git commit -m "feat: complete MCP-to-CLI converter v0.1.0"
```

---

## Dependency Order

```
Task 1 (scaffold)
  -> Task 2 (models)
    -> Task 3 (parser)          \
    -> Task 4 (registry)         |
    -> Task 5 (connector)        |-- can be parallel
    -> Task 6 (templates)        |
    -> Task 8 (static mappings)  |
    -> Task 9 (LLM mapper)      /
      -> Task 7 (generators) -- depends on 6
        -> Task 10 (pipeline) -- depends on 3,5,7,8,9
          -> Task 11 (CLI) -- depends on 10
            -> Task 12 (cache) -- depends on 10
              -> Task 13 (integration test) -- depends on all
```

Tasks 3, 4, 5, 6, 8, 9 can be developed in parallel after Task 2.
