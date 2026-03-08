"""Tests for the AgentCore generator module.
AgentCore 생성기 모듈 테스트."""

import json
from mcp_to_cli.models import ToolDefinition, ToolParam
from mcp_to_cli.generators.agentcore_gen import AgentCoreGenerator


def test_agentcore_tool_spec():
    """Test generating a single AgentCore tool specification.
    단일 AgentCore 도구 사양 생성을 테스트합니다."""
    tool = ToolDefinition(
        server="test", name="list_users",
        description="List IAM users in the account.\n\nMore details here.",
        params=[
            ToolParam(name="path_prefix", type="string", description="Path prefix", required=False),
            ToolParam(name="max_items", type="integer", description="Max results", required=False),
        ],
    )
    gen = AgentCoreGenerator()
    spec = gen.generate_tool_spec(tool)

    # Verify toolSpec structure / toolSpec 구조 검증
    assert "toolSpec" in spec
    assert spec["toolSpec"]["name"] == "list_users"
    # Description should use only the first line / 설명은 첫 번째 줄만 사용해야 함
    assert spec["toolSpec"]["description"] == "List IAM users in the account."
    assert "json" in spec["toolSpec"]["inputSchema"]
    assert "path_prefix" in spec["toolSpec"]["inputSchema"]["json"]["properties"]


def test_agentcore_tool_config():
    """Test generating a complete AgentCore tool configuration.
    완전한 AgentCore 도구 구성 생성을 테스트합니다."""
    tools = [
        ToolDefinition(server="test", name="tool1", description="Tool 1", params=[]),
        ToolDefinition(server="test", name="tool2", description="Tool 2",
                      params=[ToolParam(name="p1", type="string", description="", required=True)]),
    ]
    gen = AgentCoreGenerator()
    config = gen.generate_tool_config("test-server", tools)
    data = json.loads(config)
    # Should contain both tools with correct required params / 올바른 필수 파라미터를 가진 두 도구를 포함해야 함
    assert len(data["tools"]) == 2
    assert data["tools"][1]["toolSpec"]["inputSchema"]["json"]["required"] == ["p1"]
