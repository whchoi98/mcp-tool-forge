"""Tests for the pipeline module.
파이프라인 모듈 테스트."""

import pytest
from pathlib import Path
from unittest.mock import AsyncMock, patch
from mcp_to_cli.pipeline import Pipeline
from mcp_to_cli.models import ServerConfig


@pytest.mark.asyncio
async def test_pipeline_extract_and_generate(tmp_path):
    """Test the full pipeline: extract tools and generate schema output.
    전체 파이프라인을 테스트합니다: 도구 추출 및 스키마 출력 생성."""
    # Mock MCP tool schemas / MCP 도구 스키마 모킹
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

    # Configure a test server / 테스트 서버 구성
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

    # Verify pipeline results / 파이프라인 결과 검증
    assert result["server"] == "aws-dynamodb-mcp-server"
    assert result["tools_count"] == 1
    schema_file = tmp_path / "aws-dynamodb-mcp-server" / "schema" / "tools.json"
    assert schema_file.exists()
