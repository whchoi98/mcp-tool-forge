"""Tests for the schema cache module.
스키마 캐시 모듈 테스트."""

from mcp_to_cli.cache import SchemaCache


def test_cache_save_and_load(tmp_path):
    """Test saving and loading schemas from the cache.
    캐시에서 스키마 저장 및 로딩을 테스트합니다."""
    cache = SchemaCache(cache_dir=tmp_path)
    tools = [{"name": "test", "description": "Test", "inputSchema": {}}]
    # Save and then reload / 저장 후 다시 로드
    cache.save("test-server", tools)
    loaded = cache.load("test-server")
    assert loaded == tools


def test_cache_miss(tmp_path):
    """Test that loading a nonexistent cache entry returns None.
    존재하지 않는 캐시 항목 로딩 시 None을 반환하는지 테스트합니다."""
    cache = SchemaCache(cache_dir=tmp_path)
    assert cache.load("nonexistent") is None
