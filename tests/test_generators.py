"""Tests for the code generator modules.
코드 생성기 모듈 테스트."""

import json
from mcp_to_cli.models import ToolDefinition, ToolParam, MappingResult
from mcp_to_cli.generators.boto3_gen import Boto3Generator
from mcp_to_cli.generators.cli_gen import CliGenerator
from mcp_to_cli.generators.schema_gen import SchemaGenerator
from mcp_to_cli.generators.skill_gen import SkillGenerator


def _make_tool():
    """Create a sample ToolDefinition for testing.
    테스트용 샘플 ToolDefinition을 생성합니다."""
    return ToolDefinition(
        server="aws-dynamodb-mcp-server",
        name="dynamodb_put_item",
        description="Put an item into a DynamoDB table",
        params=[
            ToolParam(name="table_name", type="string", description="Table name", required=True),
            ToolParam(name="item", type="object", description="Item to put", required=True),
            ToolParam(name="condition", type="string", description="Condition expression", required=False),
        ],
    )


def _make_mapping():
    """Create a sample MappingResult for testing.
    테스트용 샘플 MappingResult를 생성합니다."""
    return MappingResult(
        tool_name="dynamodb_put_item",
        boto3_client="dynamodb",
        boto3_method="put_item",
        boto3_params={"TableName": "table_name", "Item": "item", "ConditionExpression": "condition"},
        cli_command="aws dynamodb put-item",
        cli_params={"--table-name": "table_name", "--item": "item", "--condition-expression": "condition"},
        source="static",
    )


def test_boto3_generator_produces_valid_python():
    """Test that Boto3Generator produces valid Python code.
    Boto3Generator가 유효한 Python 코드를 생성하는지 테스트합니다."""
    gen = Boto3Generator()
    code = gen.generate_function(_make_tool(), _make_mapping())
    # Verify function definition and boto3 session/client call / 함수 정의와 boto3 세션/클라이언트 호출 확인
    assert "def dynamodb_put_item(" in code
    assert "boto3.Session(profile_name=profile_name)" in code
    assert "session.client('dynamodb')" in code
    assert "put_item(" in code
    assert "profile_name: str | None = None" in code


def test_boto3_generator_module():
    """Test that Boto3Generator produces a complete module with imports.
    Boto3Generator가 import가 포함된 완전한 모듈을 생성하는지 테스트합니다."""
    gen = Boto3Generator()
    code = gen.generate_module("aws-dynamodb-mcp-server", [(_make_tool(), _make_mapping())])
    assert "import boto3" in code


def test_cli_generator_produces_bash():
    """Test that CliGenerator produces valid bash commands.
    CliGenerator가 유효한 bash 명령을 생성하는지 테스트합니다."""
    gen = CliGenerator()
    code = gen.generate_function(_make_tool(), _make_mapping())
    assert "aws dynamodb put-item" in code


def test_schema_generator_produces_json():
    """Test that SchemaGenerator produces valid JSON schema.
    SchemaGenerator가 유효한 JSON 스키마를 생성하는지 테스트합니다."""
    gen = SchemaGenerator()
    output = gen.generate_schema(_make_tool())
    data = json.loads(output)
    assert data["name"] == "dynamodb_put_item"
    # Check that parameters are included in the schema / 파라미터가 스키마에 포함되어 있는지 확인
    assert "table_name" in data["parameters"]["properties"]


def test_skill_generator_produces_markdown():
    """Test that SkillGenerator produces a markdown skill definition.
    SkillGenerator가 마크다운 스킬 정의를 생성하는지 테스트합니다."""
    gen = SkillGenerator()
    output = gen.generate_skill(_make_tool(), _make_mapping())
    # Verify skill metadata and code references / 스킬 메타데이터와 코드 참조 확인
    assert "name: dynamodb-put-item" in output
    assert "boto3" in output
    assert "aws dynamodb put-item" in output
