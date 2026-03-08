import json
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from mcp_to_cli.llm_mapper import LLMMapper
from mcp_to_cli.models import ToolDefinition, ToolParam


@pytest.mark.asyncio
async def test_llm_mapper_returns_mapping():
    tool = ToolDefinition(
        server="test-server", name="eks_describe_cluster",
        description="Describe an EKS cluster",
        params=[ToolParam(name="cluster_name", type="string", description="Cluster name", required=True)],
    )
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = json.dumps({
        "boto3_client": "eks", "boto3_method": "describe_cluster",
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
    tool = ToolDefinition(server="test-server", name="s3_list_buckets", description="List S3 buckets", params=[])
    mapper = LLMMapper()
    prompt = mapper._build_prompt(tool)
    assert "s3_list_buckets" in prompt
    assert "List S3 buckets" in prompt
