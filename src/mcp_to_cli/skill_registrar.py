from __future__ import annotations
import json
import shutil
from pathlib import Path
from rich.console import Console

console = Console()

# Default plugin directory for Claude Code
DEFAULT_PLUGIN_DIR = Path.home() / ".claude" / "plugins" / "mcp-to-cli-tools"


class SkillRegistrar:
    def __init__(self, plugin_dir: Path | None = None):
        self._plugin_dir = plugin_dir or DEFAULT_PLUGIN_DIR

    def register_skills(self, skills_dir: Path, server_name: str) -> int:
        """Copy generated skills into Claude Code plugin structure."""
        if not skills_dir.exists():
            console.print(f"[red]Error:[/] Skills directory not found: {skills_dir}")
            return 0

        # Create plugin structure
        plugin_skills_dir = self._plugin_dir / "skills" / server_name
        plugin_skills_dir.mkdir(parents=True, exist_ok=True)

        # Create plugin.json if it doesn't exist
        plugin_json = self._plugin_dir / "plugin.json"
        if not plugin_json.exists():
            self._create_plugin_json(plugin_json)

        # Copy skill files
        count = 0
        for skill_file in skills_dir.glob("*.md"):
            dest = plugin_skills_dir / skill_file.name
            shutil.copy2(skill_file, dest)
            count += 1

        console.print(f"  [green]Registered:[/] {count} skills for {server_name}")
        return count

    def _create_plugin_json(self, path: Path) -> None:
        """Create a minimal plugin.json for Claude Code."""
        plugin_config = {
            "name": "mcp-to-cli-tools",
            "version": "0.1.0",
            "description": "Auto-generated AWS CLI/boto3 tools from MCP servers",
            "skills": {
                "auto_discover": True
            }
        }
        path.write_text(json.dumps(plugin_config, indent=2))
        console.print(f"  [green]Created:[/] {path}")

    def list_registered(self) -> dict[str, int]:
        """List registered skill servers and counts."""
        result = {}
        skills_dir = self._plugin_dir / "skills"
        if skills_dir.exists():
            for server_dir in skills_dir.iterdir():
                if server_dir.is_dir():
                    count = len(list(server_dir.glob("*.md")))
                    result[server_dir.name] = count
        return result
