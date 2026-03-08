from __future__ import annotations

import json

import boto3

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

Rules:
- boto3_client is the AWS service name used in boto3.client('<service>')
- boto3_method is the snake_case method name on the client
- boto3_params maps PascalCase boto3 parameter names to the MCP parameter names
- cli_command is the full AWS CLI command prefix
- cli_params maps --kebab-case CLI flags to MCP parameter names
- Skip MCP-internal params like 'ctx' that don't map to AWS APIs
- If the tool does not map to a single boto3/CLI call (e.g. it's a helper, guide, or composite), set all values to empty strings."""


class LLMMapper:
    def __init__(self, model_id: str = "us.anthropic.claude-3-5-haiku-20241022-v1:0", region: str = "us-east-1"):
        self._model_id = model_id
        self._region = region

    def _build_prompt(self, tool: ToolDefinition) -> str:
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
        """Map a single tool using Bedrock Claude."""
        return self._map_tool_sync(tool)

    def _map_tool_sync(self, tool: ToolDefinition) -> MappingResult | None:
        """Synchronous mapping using Bedrock converse API."""
        client = boto3.client("bedrock-runtime", region_name=self._region)

        try:
            response = client.converse(
                modelId=self._model_id,
                system=[{"text": _SYSTEM_PROMPT}],
                messages=[
                    {"role": "user", "content": [{"text": self._build_prompt(tool)}]}
                ],
                inferenceConfig={"maxTokens": 512, "temperature": 0.0},
            )

            text = response["output"]["message"]["content"][0]["text"]

            # Extract JSON from response
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
        except Exception:
            return None
