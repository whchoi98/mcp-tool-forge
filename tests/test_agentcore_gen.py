import json
from mcp_to_cli.models import ToolDefinition, ToolParam
from mcp_to_cli.generators.agentcore_gen import AgentCoreGenerator


def test_agentcore_tool_spec():
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

    assert "toolSpec" in spec
    assert spec["toolSpec"]["name"] == "list_users"
    assert spec["toolSpec"]["description"] == "List IAM users in the account."
    assert "json" in spec["toolSpec"]["inputSchema"]
    assert "path_prefix" in spec["toolSpec"]["inputSchema"]["json"]["properties"]


def test_agentcore_tool_config():
    tools = [
        ToolDefinition(server="test", name="tool1", description="Tool 1", params=[]),
        ToolDefinition(server="test", name="tool2", description="Tool 2",
                      params=[ToolParam(name="p1", type="string", description="", required=True)]),
    ]
    gen = AgentCoreGenerator()
    config = gen.generate_tool_config("test-server", tools)
    data = json.loads(config)
    assert len(data["tools"]) == 2
    assert data["tools"][1]["toolSpec"]["inputSchema"]["json"]["required"] == ["p1"]
