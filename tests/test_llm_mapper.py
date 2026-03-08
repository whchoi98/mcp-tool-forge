"""Tests for the LLM mapper module.
LLM 매퍼 모듈 테스트."""

import json
import pytest
from unittest.mock import MagicMock, patch
from mcp_to_cli.llm_mapper import LLMMapper
from mcp_to_cli.models import ToolDefinition, ToolParam


@pytest.mark.asyncio
async def test_llm_mapper_returns_mapping():
    """Test that LLM mapper returns a valid mapping via Bedrock.
    LLM 매퍼가 Bedrock을 통해 유효한 매핑을 반환하는지 테스트합니다."""
    tool = ToolDefinition(
        server="test-server", name="eks_describe_cluster",
        description="Describe an EKS cluster",
        params=[ToolParam(name="cluster_name", type="string", description="Cluster name", required=True)],
    )
    # Mock Bedrock converse response / Bedrock converse 응답 모킹
    mock_response = {
        "output": {
            "message": {
                "content": [
                    {"text": json.dumps({
                        "boto3_client": "eks", "boto3_method": "describe_cluster",
                        "boto3_params": {"name": "cluster_name"},
                        "cli_command": "aws eks describe-cluster",
                        "cli_params": {"--name": "cluster_name"},
                    })}
                ]
            }
        }
    }
    with patch("mcp_to_cli.llm_mapper.boto3") as mock_boto3:
        mock_client = MagicMock()
        mock_client.converse.return_value = mock_response
        mock_boto3.client.return_value = mock_client
        mapper = LLMMapper()
        result = await mapper.map_tool(tool)
        assert result is not None
        assert result.boto3_client == "eks"
        # Source should be "llm" for LLM-generated mappings / LLM 생성 매핑의 소스는 "llm"이어야 함
        assert result.source == "llm"


def test_build_prompt():
    """Test that the prompt builder includes tool details.
    프롬프트 빌더가 도구 세부 정보를 포함하는지 테스트합니다."""
    tool = ToolDefinition(server="test-server", name="s3_list_buckets", description="List S3 buckets", params=[])
    mapper = LLMMapper()
    prompt = mapper._build_prompt(tool)
    # Prompt should contain tool name and description / 프롬프트에 도구 이름과 설명이 포함되어야 함
    assert "s3_list_buckets" in prompt
    assert "List S3 buckets" in prompt
