import json
from mcp_to_cli.models import ToolDefinition, ToolParam, MappingResult
from mcp_to_cli.generators.boto3_gen import Boto3Generator
from mcp_to_cli.generators.cli_gen import CliGenerator
from mcp_to_cli.generators.schema_gen import SchemaGenerator
from mcp_to_cli.generators.skill_gen import SkillGenerator


def _make_tool():
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
    gen = Boto3Generator()
    code = gen.generate_function(_make_tool(), _make_mapping())
    assert "def dynamodb_put_item(" in code
    assert "boto3.client('dynamodb')" in code
    assert "put_item(" in code


def test_boto3_generator_module():
    gen = Boto3Generator()
    code = gen.generate_module("aws-dynamodb-mcp-server", [(_make_tool(), _make_mapping())])
    assert "import boto3" in code


def test_cli_generator_produces_bash():
    gen = CliGenerator()
    code = gen.generate_function(_make_tool(), _make_mapping())
    assert "aws dynamodb put-item" in code


def test_schema_generator_produces_json():
    gen = SchemaGenerator()
    output = gen.generate_schema(_make_tool())
    data = json.loads(output)
    assert data["name"] == "dynamodb_put_item"
    assert "table_name" in data["parameters"]["properties"]


def test_skill_generator_produces_markdown():
    gen = SkillGenerator()
    output = gen.generate_skill(_make_tool(), _make_mapping())
    assert "name: dynamodb-put-item" in output
    assert "boto3" in output
    assert "aws dynamodb put-item" in output
