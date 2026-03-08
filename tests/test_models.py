from mcp_to_cli.models import ToolParam, ToolDefinition, MappingResult


def test_tool_param_creation():
    param = ToolParam(name="table_name", type="string", description="The DynamoDB table name", required=True)
    assert param.name == "table_name"
    assert param.required is True


def test_tool_definition_creation():
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put an item into a DynamoDB table",
        params=[
            ToolParam(name="table_name", type="string", description="Table name", required=True),
            ToolParam(name="item", type="object", description="Item to put", required=True),
        ],
    )
    assert tool.name == "dynamodb_put_item"
    assert len(tool.params) == 2
    assert tool.aws_service is None


def test_tool_definition_with_aws_mapping():
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server", name="dynamodb_put_item",
        description="Put an item", params=[], aws_service="dynamodb", aws_api_action="put_item",
    )
    assert tool.aws_service == "dynamodb"
    assert tool.aws_api_action == "put_item"


def test_mapping_result():
    result = MappingResult(
        tool_name="dynamodb_put_item", boto3_client="dynamodb", boto3_method="put_item",
        boto3_params={"TableName": "table_name", "Item": "item"},
        cli_command="aws dynamodb put-item", cli_params={"--table-name": "table_name", "--item": "item"},
        source="static",
    )
    assert result.source == "static"
    assert result.boto3_client == "dynamodb"
