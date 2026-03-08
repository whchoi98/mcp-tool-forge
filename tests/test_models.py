"""Tests for the models module.
모델 모듈 테스트."""

from mcp_to_cli.models import ToolParam, ToolDefinition, MappingResult


def test_tool_param_creation():
    """Test creating a ToolParam instance.
    ToolParam 인스턴스 생성을 테스트합니다."""
    # Create a param with required=True / required=True로 파라미터 생성
    param = ToolParam(name="table_name", type="string", description="The DynamoDB table name", required=True)
    assert param.name == "table_name"
    assert param.required is True


def test_tool_definition_creation():
    """Test creating a ToolDefinition with parameters.
    파라미터가 있는 ToolDefinition 생성을 테스트합니다."""
    # Build a tool with two required params / 필수 파라미터 2개로 도구 생성
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
    # AWS service should be None when not specified / AWS 서비스는 미지정 시 None이어야 함
    assert tool.aws_service is None


def test_tool_definition_with_aws_mapping():
    """Test creating a ToolDefinition with AWS service mapping.
    AWS 서비스 매핑이 있는 ToolDefinition 생성을 테스트합니다."""
    tool = ToolDefinition(
        server="aws-dynamodb-mcp-server", name="dynamodb_put_item",
        description="Put an item", params=[], aws_service="dynamodb", aws_api_action="put_item",
    )
    assert tool.aws_service == "dynamodb"
    assert tool.aws_api_action == "put_item"


def test_mapping_result():
    """Test creating a MappingResult with boto3 and CLI info.
    boto3 및 CLI 정보가 있는 MappingResult 생성을 테스트합니다."""
    result = MappingResult(
        tool_name="dynamodb_put_item", boto3_client="dynamodb", boto3_method="put_item",
        boto3_params={"TableName": "table_name", "Item": "item"},
        cli_command="aws dynamodb put-item", cli_params={"--table-name": "table_name", "--item": "item"},
        source="static",
    )
    # Verify source and client are set correctly / source와 client가 올바르게 설정되었는지 확인
    assert result.source == "static"
    assert result.boto3_client == "dynamodb"
