from mcp_to_cli.mapping_loader import MappingLoader
from mcp_to_cli.models import ToolDefinition, ToolParam


def test_load_static_mapping():
    loader = MappingLoader()
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put item",
        params=[ToolParam(name="table_name", type="string", description="", required=True)],
    )
    result = loader.find_mapping(tool)
    assert result is not None
    assert result.boto3_client == "dynamodb"
    assert result.source == "static"


def test_no_mapping_returns_none():
    loader = MappingLoader()
    tool = ToolDefinition(server="unknown-server", name="unknown_tool", description="Unknown", params=[])
    result = loader.find_mapping(tool)
    assert result is None
