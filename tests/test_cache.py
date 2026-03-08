from mcp_to_cli.cache import SchemaCache


def test_cache_save_and_load(tmp_path):
    cache = SchemaCache(cache_dir=tmp_path)
    tools = [{"name": "test", "description": "Test", "inputSchema": {}}]
    cache.save("test-server", tools)
    loaded = cache.load("test-server")
    assert loaded == tools


def test_cache_miss(tmp_path):
    cache = SchemaCache(cache_dir=tmp_path)
    assert cache.load("nonexistent") is None
