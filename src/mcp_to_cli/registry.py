"""Server registry for AWS MCP servers.
AWS MCP 서버를 위한 서버 레지스트리."""

from __future__ import annotations

from pathlib import Path

import yaml

from mcp_to_cli.models import ServerConfig

# Default path to the YAML registry file / YAML 레지스트리 파일의 기본 경로
_DEFAULT_REGISTRY = Path(__file__).parent / "registry.yaml"


class ServerRegistry:
    """Manages a registry of known MCP server configurations.
    알려진 MCP 서버 구성의 레지스트리를 관리합니다."""

    def __init__(self, path: Path | None = None):
        self._path = path or _DEFAULT_REGISTRY
        self._servers: dict[str, ServerConfig] = {}
        self._load()

    def _load(self) -> None:
        """Load server configurations from YAML file.
        YAML 파일에서 서버 구성을 로드합니다."""
        with open(self._path) as f:
            data = yaml.safe_load(f)
        # Parse each server entry into a ServerConfig / 각 서버 항목을 ServerConfig로 파싱
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
        """Get a server config by name, or None if not found.
        이름으로 서버 구성을 가져오거나, 없으면 None을 반환합니다."""
        return self._servers.get(name)

    def list_servers(self) -> list[ServerConfig]:
        """List all registered servers.
        등록된 모든 서버를 나열합니다."""
        return list(self._servers.values())

    def list_by_category(self, category: str) -> list[ServerConfig]:
        """List servers filtered by category.
        카테고리별로 필터링된 서버를 나열합니다."""
        return [s for s in self._servers.values() if s.category == category]

    def categories(self) -> list[str]:
        """Return sorted list of unique categories.
        고유 카테고리의 정렬된 목록을 반환합니다."""
        return sorted(set(s.category for s in self._servers.values()))
