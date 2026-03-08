from __future__ import annotations
from pathlib import Path
import yaml
from mcp_to_cli.models import MappingResult, ToolDefinition

_MAPPINGS_DIR = Path(__file__).parent / "mappings"


class MappingLoader:
    def __init__(self, mappings_dir: Path | None = None):
        self._dir = mappings_dir or _MAPPINGS_DIR
        self._mappings: dict[str, dict] = {}
        self._load_all()

    def _load_all(self) -> None:
        if not self._dir.exists():
            return
        for yaml_file in self._dir.glob("*.yaml"):
            with open(yaml_file) as f:
                data = yaml.safe_load(f)
            for tool_name, mapping in data.get("tools", {}).items():
                self._mappings[tool_name] = mapping

    def find_mapping(self, tool: ToolDefinition) -> MappingResult | None:
        mapping = self._mappings.get(tool.name)
        if not mapping:
            return None
        boto3_info = mapping.get("boto3", {})
        cli_info = mapping.get("cli", {})
        return MappingResult(
            tool_name=tool.name,
            boto3_client=boto3_info.get("client", ""),
            boto3_method=boto3_info.get("method", ""),
            boto3_params=boto3_info.get("params", {}),
            cli_command=cli_info.get("command", ""),
            cli_params=cli_info.get("params", {}),
            source="static",
        )
