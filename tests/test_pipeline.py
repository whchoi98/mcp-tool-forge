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
