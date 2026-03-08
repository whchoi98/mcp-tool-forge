"""Local file cache for MCP tool schemas.
MCP 도구 스키마를 위한 로컬 파일 캐시."""

from __future__ import annotations
import json
from pathlib import Path


class SchemaCache:
    """Caches tool schemas as JSON files on disk to avoid repeated server queries.
    반복적인 서버 조회를 피하기 위해 도구 스키마를 디스크에 JSON 파일로 캐싱합니다."""

    def __init__(self, cache_dir: Path | None = None):
        # Use default cache directory if not specified / 지정되지 않으면 기본 캐시 디렉터리 사용
        self._dir = cache_dir or Path.home() / ".mcp-to-cli" / "cache"
        self._dir.mkdir(parents=True, exist_ok=True)

    def save(self, server_name: str, tools: list[dict]) -> None:
        """Save tool schemas for a server to cache.
        서버의 도구 스키마를 캐시에 저장합니다."""
        path = self._dir / f"{server_name}.json"
        path.write_text(json.dumps(tools, indent=2))

    def load(self, server_name: str) -> list[dict] | None:
        """Load cached tool schemas for a server, or None if not cached.
        서버의 캐시된 도구 스키마를 로드하거나, 캐시가 없으면 None을 반환합니다."""
        path = self._dir / f"{server_name}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text())

    def clear(self, server_name: str | None = None) -> None:
        """Clear cache for a specific server or all servers.
        특정 서버 또는 모든 서버의 캐시를 삭제합니다."""
        if server_name:
            # Clear single server cache / 단일 서버 캐시 삭제
            path = self._dir / f"{server_name}.json"
            if path.exists():
                path.unlink()
        else:
            # Clear all cached schemas / 모든 캐시된 스키마 삭제
            for f in self._dir.glob("*.json"):
                f.unlink()
