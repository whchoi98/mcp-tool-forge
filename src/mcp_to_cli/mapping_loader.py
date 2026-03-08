"""Static mapping loader for MCP tool to AWS API mappings.
MCP 도구에서 AWS API로의 정적 매핑 로더."""

from __future__ import annotations
from pathlib import Path
import yaml
from mcp_to_cli.models import MappingResult, ToolDefinition

# Default directory for YAML mapping files / YAML 매핑 파일의 기본 디렉터리
_MAPPINGS_DIR = Path(__file__).parent / "mappings"


class MappingLoader:
    """Loads static MCP-to-AWS mappings from YAML files.
    YAML 파일에서 MCP-to-AWS 정적 매핑을 로드합니다."""

    def __init__(self, mappings_dir: Path | None = None):
        self._dir = mappings_dir or _MAPPINGS_DIR
        self._mappings: dict[str, dict] = {}
        self._load_all()

    def _load_all(self) -> None:
        """Load all mapping YAML files from the mappings directory.
        매핑 디렉터리에서 모든 매핑 YAML 파일을 로드합니다."""
        if not self._dir.exists():
            return
        # Iterate over all YAML files in mappings directory / 매핑 디렉터리의 모든 YAML 파일 순회
        for yaml_file in self._dir.glob("*.yaml"):
            with open(yaml_file) as f:
                data = yaml.safe_load(f)
            # Register each tool mapping by name / 각 도구 매핑을 이름으로 등록
            for tool_name, mapping in data.get("tools", {}).items():
                self._mappings[tool_name] = mapping

    def find_mapping(self, tool: ToolDefinition) -> MappingResult | None:
        """Find a static mapping for the given tool, or None if not found.
        주어진 도구에 대한 정적 매핑을 찾거나, 없으면 None을 반환합니다."""
        mapping = self._mappings.get(tool.name)
        if not mapping:
            return None
        # Extract boto3 and CLI mapping info / boto3 및 CLI 매핑 정보 추출
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
