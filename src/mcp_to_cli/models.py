"""Data models for MCP-to-CLI tool definitions and mappings.
MCP-to-CLI 도구 정의 및 매핑을 위한 데이터 모델."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolParam:
    """Represents a single parameter of an MCP tool.
    MCP 도구의 단일 파라미터를 나타냅니다."""

    name: str  # Parameter name / 파라미터 이름
    type: str  # Parameter type (string, number, etc.) / 파라미터 타입 (string, number 등)
    description: str  # Human-readable description / 사람이 읽을 수 있는 설명
    required: bool  # Whether parameter is required / 필수 파라미터 여부
    default: Any = None  # Default value if any / 기본값 (있는 경우)


@dataclass
class ToolDefinition:
    """Full definition of an MCP tool including its parameters.
    파라미터를 포함한 MCP 도구의 전체 정의."""

    server: str  # Source MCP server name / 소스 MCP 서버 이름
    name: str  # Tool name / 도구 이름
    description: str  # Tool description / 도구 설명
    params: list[ToolParam]  # List of tool parameters / 도구 파라미터 목록
    aws_service: str | None = None  # Mapped AWS service / 매핑된 AWS 서비스
    aws_api_action: str | None = None  # Mapped AWS API action / 매핑된 AWS API 액션


@dataclass
class MappingResult:
    """Result of mapping an MCP tool to AWS boto3/CLI equivalents.
    MCP 도구를 AWS boto3/CLI에 매핑한 결과."""

    tool_name: str  # Original MCP tool name / 원본 MCP 도구 이름
    boto3_client: str  # boto3 service client name / boto3 서비스 클라이언트 이름
    boto3_method: str  # boto3 method name / boto3 메서드 이름
    boto3_params: dict[str, str]  # boto3 parameter mapping / boto3 파라미터 매핑
    cli_command: str  # AWS CLI command / AWS CLI 명령어
    cli_params: dict[str, str]  # CLI flag mapping / CLI 플래그 매핑
    source: str  # Mapping source: "static" | "llm" | "unknown" / 매핑 출처: "static" | "llm" | "unknown"


@dataclass
class ServerConfig:
    """Configuration for an MCP server connection.
    MCP 서버 연결 구성."""

    name: str  # Server identifier / 서버 식별자
    package: str  # NPM or PyPI package name / NPM 또는 PyPI 패키지 이름
    runtime: str  # Runtime: "npx" | "uvx" / 런타임: "npx" | "uvx"
    transport: str  # Transport: "stdio" | "sse" / 전송 방식: "stdio" | "sse"
    category: str  # Server category / 서버 카테고리
    description: str = ""  # Optional description / 선택적 설명
    env: dict[str, str] = field(default_factory=dict)  # Environment variables / 환경 변수
    args: list[str] = field(default_factory=list)  # Additional arguments / 추가 인자
