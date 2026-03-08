"""Server registry for AWS MCP servers."""

from __future__ import annotations

from pathlib import Path

import yaml

from mcp_to_cli.models import ServerConfig

_DEFAULT_REGISTRY = Path(__file__).parent / "registry.yaml"


class ServerRegistry:
    def __init__(self, path: Path | None = None):
        self._path = path or _DEFAULT_REGISTRY
        self._servers: dict[str, ServerConfig] = {}
        self._load()

    def _load(self) -> None:
        with open(self._path) as f:
            data = yaml.safe_load(f)
        for name, info in data.get("servers", {}).items():
            self._servers[name] = ServerConfig(
                name=name,
                package=info["package"],
                runtime=info["runtime"],
                transport=info["transport"],
                category=info["category"],
                description=info.get("description", ""),
                env=info.get("env", {}),
                args=info.get("args", []),
            )

    def get(self, name: str) -> ServerConfig | None:
        return self._servers.get(name)

    def list_servers(self) -> list[ServerConfig]:
        return list(self._servers.values())

    def list_by_category(self, category: str) -> list[ServerConfig]:
        return [s for s in self._servers.values() if s.category == category]

    def categories(self) -> list[str]:
        return sorted(set(s.category for s in self._servers.values()))
