from __future__ import annotations
import json
from pathlib import Path


class SchemaCache:
    def __init__(self, cache_dir: Path | None = None):
        self._dir = cache_dir or Path.home() / ".mcp-to-cli" / "cache"
        self._dir.mkdir(parents=True, exist_ok=True)

    def save(self, server_name: str, tools: list[dict]) -> None:
        path = self._dir / f"{server_name}.json"
        path.write_text(json.dumps(tools, indent=2))

    def load(self, server_name: str) -> list[dict] | None:
        path = self._dir / f"{server_name}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text())

    def clear(self, server_name: str | None = None) -> None:
        if server_name:
            path = self._dir / f"{server_name}.json"
            if path.exists():
                path.unlink()
        else:
            for f in self._dir.glob("*.json"):
                f.unlink()
