"""Orchestration pipeline for MCP-to-CLI conversion.
MCP-to-CLI 변환을 위한 오케스트레이션 파이프라인."""
from __future__ import annotations
import json
from pathlib import Path
from rich.console import Console
from mcp_to_cli.cache import SchemaCache
from mcp_to_cli.connector import MCPConnector
from mcp_to_cli.generators import AgentCoreGenerator, Boto3Generator, CliGenerator, SchemaGenerator, SkillGenerator
from mcp_to_cli.llm_mapper import LLMMapper
from mcp_to_cli.mapping_loader import MappingLoader
from mcp_to_cli.models import MappingResult, ServerConfig, ToolDefinition
from mcp_to_cli.parser import parse_tools_list

console = Console()


class Pipeline:
    """Main pipeline that extracts, maps, and generates outputs from MCP servers.
    MCP 서버에서 도구를 추출, 매핑, 출력물을 생성하는 메인 파이프라인."""

    def __init__(self, output_dir: Path | None = None):
        self._output_dir = output_dir or Path("output")  # Default output directory / 기본 출력 디렉터리
        self._connector = MCPConnector()  # MCP server connector / MCP 서버 커넥터
        self._cache = SchemaCache()  # Tool schema cache / 도구 스키마 캐시
        self._mapping_loader = MappingLoader()  # Static mapping loader / 정적 매핑 로더
        self._llm_mapper = LLMMapper()  # LLM-based mapper / LLM 기반 매퍼
        # Output generators / 출력 생성기
        self._boto3_gen = Boto3Generator()
        self._cli_gen = CliGenerator()
        self._schema_gen = SchemaGenerator()
        self._skill_gen = SkillGenerator()
        self._agentcore_gen = AgentCoreGenerator()

    async def _extract_tools(self, config: ServerConfig, use_cache: bool = True) -> list[dict]:
        """Extract tool definitions from an MCP server, using cache if available.
        MCP 서버에서 도구 정의를 추출하며, 가능하면 캐시를 사용한다."""
        if use_cache:
            cached = self._cache.load(config.name)
            if cached:
                console.print(f"  [dim]Using cached schema ({len(cached)} tools)[/]")
                return cached
        tools = await self._connector.list_tools_from_config(config)
        self._cache.save(config.name, tools)
        return tools

    def _resolve_mapping(self, tool: ToolDefinition) -> MappingResult | None:
        """Resolve a tool mapping using static YAML mappings.
        정적 YAML 매핑을 사용하여 도구 매핑을 해결한다."""
        return self._mapping_loader.find_mapping(tool)

    async def _resolve_mapping_with_llm(self, tool: ToolDefinition) -> MappingResult | None:
        """Resolve a tool mapping using LLM assistance.
        LLM 지원을 사용하여 도구 매핑을 해결한다."""
        return await self._llm_mapper.map_tool(tool)

    async def run(
        self,
        config: ServerConfig,
        outputs: list[str] | None = None,
        llm_assist: bool = False,
    ) -> dict:
        """Run the full extraction-mapping-generation pipeline.
        추출-매핑-생성 전체 파이프라인을 실행한다."""
        outputs = outputs or ["boto3", "cli", "schema", "skill", "agentcore"]
        server_dir = self._output_dir / config.name

        # Phase 1: Extract tools from MCP server / 1단계: MCP 서버에서 도구 추출
        console.print(f"[bold blue]Phase 1:[/] Extracting tools from {config.name}...")
        raw_tools = await self._extract_tools(config)
        tools = parse_tools_list(raw_tools, config.name)
        console.print(f"  Found {len(tools)} tools")

        # Phase 2 & 3: Map tools to AWS services / 2·3단계: 도구를 AWS 서비스에 매핑
        mapped: list[tuple[ToolDefinition, MappingResult | None]] = []
        static_count = 0
        llm_count = 0

        for tool in tools:
            # Try static mapping first / 정적 매핑을 먼저 시도
            mapping = self._resolve_mapping(tool)
            if mapping:
                static_count += 1
            elif llm_assist:
                # Fall back to LLM-based mapping / LLM 기반 매핑으로 대체
                console.print(f"  [yellow]LLM mapping:[/] {tool.name}")
                mapping = await self._resolve_mapping_with_llm(tool)
                if mapping:
                    llm_count += 1
            mapped.append((tool, mapping))

        console.print(f"  Mapped: {static_count} static, {llm_count} LLM, {len(tools) - static_count - llm_count} unmapped")

        # Generate outputs for each requested format / 요청된 각 형식에 대한 출력 생성
        for output_type in outputs:
            if output_type == "boto3":
                self._write_boto3(server_dir, config.name, mapped)
            elif output_type == "cli":
                self._write_cli(server_dir, config.name, mapped)
            elif output_type == "schema":
                self._write_schema(server_dir, config.name, tools)
            elif output_type == "skill":
                self._write_skills(server_dir, mapped)
            elif output_type == "agentcore":
                self._write_agentcore(server_dir, config.name, tools)

        return {
            "server": config.name,
            "tools_count": len(tools),
            "static_mapped": static_count,
            "llm_mapped": llm_count,
            "unmapped": len(tools) - static_count - llm_count,
            "outputs": outputs,
        }

    def _write_boto3(self, server_dir: Path, server_name: str, mapped: list[tuple]) -> None:
        """Write generated boto3 Python module to disk.
        생성된 boto3 Python 모듈을 디스크에 기록한다."""
        out_dir = server_dir / "boto3"
        out_dir.mkdir(parents=True, exist_ok=True)
        # Filter only tools with successful mappings / 매핑에 성공한 도구만 필터링
        with_mapping = [(t, m) for t, m in mapped if m is not None]
        if not with_mapping:
            return
        code = self._boto3_gen.generate_module(server_name, with_mapping)
        (out_dir / "tools.py").write_text(code)
        (out_dir / "__init__.py").write_text("")
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.py'}")

    def _write_cli(self, server_dir: Path, server_name: str, mapped: list[tuple]) -> None:
        """Write generated CLI shell script to disk.
        생성된 CLI 셸 스크립트를 디스크에 기록한다."""
        out_dir = server_dir / "cli"
        out_dir.mkdir(parents=True, exist_ok=True)
        # Filter only tools with successful mappings / 매핑에 성공한 도구만 필터링
        with_mapping = [(t, m) for t, m in mapped if m is not None]
        if not with_mapping:
            return
        code = self._cli_gen.generate_module(server_name, with_mapping)
        (out_dir / "tools.sh").write_text(code)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.sh'}")

    def _write_schema(self, server_dir: Path, server_name: str, tools: list[ToolDefinition]) -> None:
        """Write generated JSON schema to disk.
        생성된 JSON 스키마를 디스크에 기록한다."""
        out_dir = server_dir / "schema"
        out_dir.mkdir(parents=True, exist_ok=True)
        code = self._schema_gen.generate_module(server_name, tools)
        (out_dir / "tools.json").write_text(code)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.json'}")

    def _write_agentcore(self, server_dir: Path, server_name: str, tools: list[ToolDefinition]) -> None:
        """Write generated AgentCore Gateway config to disk.
        생성된 AgentCore Gateway 구성을 디스크에 기록한다."""
        out_dir = server_dir / "agentcore"
        out_dir.mkdir(parents=True, exist_ok=True)
        config = self._agentcore_gen.generate_tool_config(server_name, tools)
        (out_dir / "tool_config.json").write_text(config)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tool_config.json'}")

    def _write_skills(self, server_dir: Path, mapped: list[tuple]) -> None:
        """Write generated skill markdown files to disk.
        생성된 스킬 마크다운 파일을 디스크에 기록한다."""
        out_dir = server_dir / "skill"
        out_dir.mkdir(parents=True, exist_ok=True)
        for tool, mapping in mapped:
            skill_content = self._skill_gen.generate_skill(tool, mapping)
            # Convert underscores to hyphens for filename / 파일명에서 밑줄을 하이픈으로 변환
            filename = tool.name.replace("_", "-") + ".md"
            (out_dir / filename).write_text(skill_content)
        console.print(f"  [green]Wrote:[/] {len(mapped)} skills to {out_dir}")
