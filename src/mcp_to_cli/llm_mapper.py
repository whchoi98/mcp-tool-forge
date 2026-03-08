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
