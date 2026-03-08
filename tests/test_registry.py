import tempfile
import os
from pathlib import Path
from mcp_to_cli.registry import ServerRegistry


def test_load_registry():
    registry = ServerRegistry()
    servers = registry.list_servers()
    assert len(servers) > 0


def test_get_server_config():
    registry = ServerRegistry()
    config = registry.get("aws-dynamodb-mcp-server")
    assert config is not None
    assert config.runtime in ("npx", "uvx")
    assert config.transport in ("stdio", "sse")


def test_get_nonexistent_server():
    registry = ServerRegistry()
    config = registry.get("nonexistent-server")
    assert config is None


def test_list_by_category():
    registry = ServerRegistry()
    data_servers = registry.list_by_category("Data & Analytics")
    assert len(data_servers) > 0


def test_load_custom_registry():
    yaml_content = """
servers:
  test-server:
    package: "test-package"
    runtime: npx
    transport: stdio
    category: Test
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(yaml_content)
        f.flush()
        registry = ServerRegistry(path=Path(f.name))
        config = registry.get("test-server")
        assert config is not None
        assert config.package == "test-package"
    os.unlink(f.name)
