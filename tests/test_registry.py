"""Tests for the server registry module.
서버 레지스트리 모듈 테스트."""

import tempfile
import os
from pathlib import Path
from mcp_to_cli.registry import ServerRegistry


def test_load_registry():
    """Test loading the default server registry.
    기본 서버 레지스트리 로딩을 테스트합니다."""
    registry = ServerRegistry()
    servers = registry.list_servers()
    assert len(servers) > 0


def test_get_server_config():
    """Test retrieving a known server configuration.
    알려진 서버 구성 조회를 테스트합니다."""
    registry = ServerRegistry()
    config = registry.get("aws-dynamodb-mcp-server")
    assert config is not None
    # Verify runtime and transport are valid values / 런타임과 전송 방식이 유효한 값인지 확인
    assert config.runtime in ("npx", "uvx")
    assert config.transport in ("stdio", "sse")


def test_get_nonexistent_server():
    """Test that a nonexistent server returns None.
    존재하지 않는 서버 조회 시 None을 반환하는지 테스트합니다."""
    registry = ServerRegistry()
    config = registry.get("nonexistent-server")
    assert config is None


def test_list_by_category():
    """Test filtering servers by category.
    카테고리별 서버 필터링을 테스트합니다."""
    registry = ServerRegistry()
    data_servers = registry.list_by_category("Data & Analytics")
    assert len(data_servers) > 0


def test_load_custom_registry():
    """Test loading a custom registry from a YAML file.
    YAML 파일에서 사용자 정의 레지스트리 로딩을 테스트합니다."""
    # Create a temporary YAML with a test server / 테스트 서버가 있는 임시 YAML 생성
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
    # Clean up temp file / 임시 파일 정리
    os.unlink(f.name)
