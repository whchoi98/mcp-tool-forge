"""LLM-based mapper for MCP tools to AWS API equivalents using Bedrock.
Bedrock을 사용하여 MCP 도구를 AWS API에 매핑하는 LLM 기반 매퍼."""

from __future__ import annotations

import json

import boto3

from mcp_to_cli.models import MappingResult, ToolDefinition

# System prompt instructing the LLM to produce boto3/CLI mappings / LLM에 boto3/CLI 매핑 생성을 지시하는 시스템 프롬프트
_SYSTEM_PROMPT = """You are an AWS API expert. Given an MCP tool definition, determine the equivalent boto3 and AWS CLI calls.

Respond ONLY with valid JSON in this exact format:
{
  "boto3_client": "<service-name>",
  "boto3_method": "<method_name>",
  "boto3_params": {"<BotoParamName>": "<mcp_param_name>", ...},
  "cli_command": "aws <service> <command>",
  "cli_params": {"--<flag>": "<mcp_param_name>", ...}
}

Rules:
- boto3_client is the AWS service name used in boto3.client('<service>')
- boto3_method is the snake_case method name on the client
- boto3_params maps PascalCase boto3 parameter names to the MCP parameter names
- cli_command is the full AWS CLI command prefix
- cli_params maps --kebab-case CLI flags to MCP parameter names
- Skip MCP-internal params like 'ctx' that don't map to AWS APIs
- If the tool does not map to a single boto3/CLI call (e.g. it's a helper, guide, or composite), set all values to empty strings."""


class LLMMapper:
    """Maps MCP tools to AWS API calls using an LLM via Amazon Bedrock.
    Amazon Bedrock을 통해 LLM을 사용하여 MCP 도구를 AWS API 호출에 매핑합니다."""

    def __init__(self, model_id: str = "us.anthropic.claude-3-5-haiku-20241022-v1:0", region: str = "us-east-1"):
        self._model_id = model_id  # Bedrock model identifier / Bedrock 모델 식별자
        self._region = region  # AWS region for Bedrock / Bedrock용 AWS 리전

    def _build_prompt(self, tool: ToolDefinition) -> str:
        """Build user prompt describing the MCP tool for the LLM.
        LLM에 전달할 MCP 도구 설명 프롬프트를 구성합니다."""
        # Format parameter descriptions / 파라미터 설명 포맷팅
        params_desc = "\n".join(
            f"  - {p.name} ({p.type}, {'required' if p.required else 'optional'}): {p.description[:200]}"
            for p in tool.params
        )
        return f"""MCP Tool:
- Name: {tool.name}
- Server: {tool.server}
- Description: {tool.description.split(chr(10))[0].strip()}
- Parameters:
{params_desc if params_desc else '  (none)'}

What is the equivalent boto3 and AWS CLI call?"""

    async def map_tool(self, tool: ToolDefinition) -> MappingResult | None:
        """Map a single tool using Bedrock Claude.
        Bedrock Claude를 사용하여 단일 도구를 매핑합니다."""
        return self._map_tool_sync(tool)

    def _map_tool_sync(self, tool: ToolDefinition) -> MappingResult | None:
        """Synchronous mapping using Bedrock converse API.
        Bedrock converse API를 사용한 동기 매핑."""
        # Create Bedrock runtime client / Bedrock 런타임 클라이언트 생성
        client = boto3.client("bedrock-runtime", region_name=self._region)

        try:
            # Call Bedrock converse API / Bedrock converse API 호출
            response = client.converse(
                modelId=self._model_id,
                system=[{"text": _SYSTEM_PROMPT}],
                messages=[
                    {"role": "user", "content": [{"text": self._build_prompt(tool)}]}
                ],
                inferenceConfig={"maxTokens": 512, "temperature": 0.0},
            )

            text = response["output"]["message"]["content"][0]["text"]

            # Extract JSON from markdown code block if present / 마크다운 코드 블록에서 JSON 추출
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]

            # Parse JSON response / JSON 응답 파싱
            data = json.loads(text.strip())

            # Return None if no valid boto3 client mapping / 유효한 boto3 클라이언트 매핑이 없으면 None 반환
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
            # Handle malformed LLM responses / 잘못된 LLM 응답 처리
            return None
        except Exception:
            # Handle API errors gracefully / API 오류를 우아하게 처리
            return None
