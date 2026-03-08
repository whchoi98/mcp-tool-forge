"""Tests for the mapping loader module.
매핑 로더 모듈 테스트."""

from mcp_to_cli.mapping_loader import MappingLoader
from mcp_to_cli.models import ToolDefinition, ToolParam


def test_load_static_mapping():
    """Test loading a static mapping for a known tool.
    알려진 도구의 정적 매핑 로딩을 테스트합니다."""
    loader = MappingLoader()
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put item",
        params=[ToolParam(name="table_name", type="string", description="", required=True)],
    )
    result = loader.find_mapping(tool)
    assert result is not None
    # Should map to dynamodb client with static source / dynamodb 클라이언트에 정적 소스로 매핑되어야 함
    assert result.boto3_client == "dynamodb"
    assert result.source == "static"


def test_no_mapping_returns_none():
    """Test that an unknown tool returns no mapping.
    알 수 없는 도구가 매핑 없음을 반환하는지 테스트합니다."""
    loader = MappingLoader()
    tool = ToolDefinition(server="unknown-server", name="unknown_tool", description="Unknown", params=[])
    result = loader.find_mapping(tool)
    assert result is None
