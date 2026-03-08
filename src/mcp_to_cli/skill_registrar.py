"""Skill registrar for Claude Code plugin integration.
Claude Code 플러그인 통합을 위한 스킬 등록기."""
from __future__ import annotations
import json
import shutil
from pathlib import Path
from rich.console import Console

console = Console()

# Default plugin directory for Claude Code / Claude Code 기본 플러그인 디렉터리
DEFAULT_PLUGIN_DIR = Path.home() / ".claude" / "plugins" / "mcp-to-cli-tools"


class SkillRegistrar:
    """Manages registration of generated skills into the Claude Code plugin directory.
    생성된 스킬을 Claude Code 플러그인 디렉터리에 등록하는 것을 관리한다."""

    def __init__(self, plugin_dir: Path | None = None):
        self._plugin_dir = plugin_dir or DEFAULT_PLUGIN_DIR  # Target plugin directory / 대상 플러그인 디렉터리

    def register_skills(self, skills_dir: Path, server_name: str) -> int:
        """Copy generated skills into Claude Code plugin structure.
        생성된 스킬을 Claude Code 플러그인 구조에 복사한다."""
        if not skills_dir.exists():
            console.print(f"[red]Error:[/] Skills directory not found: {skills_dir}")
            return 0

        # Create plugin directory structure / 플러그인 디렉터리 구조 생성
        plugin_skills_dir = self._plugin_dir / "skills" / server_name
        plugin_skills_dir.mkdir(parents=True, exist_ok=True)

        # Create plugin.json if it doesn't exist / plugin.json이 없으면 생성
        plugin_json = self._plugin_dir / "plugin.json"
        if not plugin_json.exists():
            self._create_plugin_json(plugin_json)

        # Copy skill markdown files to plugin directory / 스킬 마크다운 파일을 플러그인 디렉터리에 복사
        count = 0
        for skill_file in skills_dir.glob("*.md"):
            dest = plugin_skills_dir / skill_file.name
            shutil.copy2(skill_file, dest)
            count += 1

        console.print(f"  [green]Registered:[/] {count} skills for {server_name}")
        return count

    def _create_plugin_json(self, path: Path) -> None:
        """Create a minimal plugin.json for Claude Code.
        Claude Code용 최소 plugin.json을 생성한다."""
        plugin_config = {
            "name": "mcp-to-cli-tools",
            "version": "0.1.0",
            "description": "Auto-generated AWS CLI/boto3 tools from MCP servers",
            "skills": {
                "auto_discover": True  # Enable automatic skill discovery / 자동 스킬 탐색 활성화
            }
        }
        path.write_text(json.dumps(plugin_config, indent=2))
        console.print(f"  [green]Created:[/] {path}")

    def list_registered(self) -> dict[str, int]:
        """List registered skill servers and counts.
        등록된 스킬 서버와 개수를 나열한다."""
        result = {}
        skills_dir = self._plugin_dir / "skills"
        if skills_dir.exists():
            for server_dir in skills_dir.iterdir():
                if server_dir.is_dir():
                    count = len(list(server_dir.glob("*.md")))
                    result[server_dir.name] = count
        return result
