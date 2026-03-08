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
    description: str = ""
    env: dict[str, str] = field(default_factory=dict)
    args: list[str] = field(default_factory=list)
