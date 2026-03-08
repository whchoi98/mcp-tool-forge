from __future__ import annotations
import json
from pathlib import Path
from rich.console import Console
from mcp_to_cli.connector import MCPConnector
from mcp_to_cli.generators import Boto3Generator, CliGenerator, SchemaGenerator, SkillGenerator
from mcp_to_cli.llm_mapper import LLMMapper
from mcp_to_cli.mapping_loader import MappingLoader
from mcp_to_cli.models import MappingResult, ServerConfig, ToolDefinition
from mcp_to_cli.parser import parse_tools_list

console = Console()


class Pipeline:
    def __init__(self, output_dir: Path | None = None):
        self._output_dir = output_dir or Path("output")
        self._connector = MCPConnector()
        self._mapping_loader = MappingLoader()
        self._llm_mapper = LLMMapper()
        self._boto3_gen = Boto3Generator()
        self._cli_gen = CliGenerator()
        self._schema_gen = SchemaGenerator()
        self._skill_gen = SkillGenerator()

    async def _extract_tools(self, config: ServerConfig) -> list[dict]:
        return await self._connector.list_tools_from_config(config)

    def _resolve_mapping(self, tool: ToolDefinition) -> MappingResult | None:
        return self._mapping_loader.find_mapping(tool)

    async def _resolve_mapping_with_llm(self, tool: ToolDefinition) -> MappingResult | None:
        return await self._llm_mapper.map_tool(tool)

    async def run(
        self,
        config: ServerConfig,
        outputs: list[str] | None = None,
        llm_assist: bool = False,
    ) -> dict:
        outputs = outputs or ["boto3", "cli", "schema", "skill"]
        server_dir = self._output_dir / config.name

        # Phase 1: Extract
        console.print(f"[bold blue]Phase 1:[/] Extracting tools from {config.name}...")
        raw_tools = await self._extract_tools(config)
        tools = parse_tools_list(raw_tools, config.name)
        console.print(f"  Found {len(tools)} tools")

        # Phase 2 & 3: Map
        mapped: list[tuple[ToolDefinition, MappingResult | None]] = []
        static_count = 0
        llm_count = 0

        for tool in tools:
            mapping = self._resolve_mapping(tool)
            if mapping:
                static_count += 1
            elif llm_assist:
                console.print(f"  [yellow]LLM mapping:[/] {tool.name}")
                mapping = await self._resolve_mapping_with_llm(tool)
                if mapping:
                    llm_count += 1
            mapped.append((tool, mapping))

        console.print(f"  Mapped: {static_count} static, {llm_count} LLM, {len(tools) - static_count - llm_count} unmapped")

        # Generate outputs
        for output_type in outputs:
            if output_type == "boto3":
                self._write_boto3(server_dir, config.name, mapped)
            elif output_type == "cli":
                self._write_cli(server_dir, config.name, mapped)
            elif output_type == "schema":
                self._write_schema(server_dir, config.name, tools)
            elif output_type == "skill":
                self._write_skills(server_dir, mapped)

        return {
            "server": config.name,
            "tools_count": len(tools),
            "static_mapped": static_count,
            "llm_mapped": llm_count,
            "unmapped": len(tools) - static_count - llm_count,
            "outputs": outputs,
        }

    def _write_boto3(self, server_dir: Path, server_name: str, mapped: list[tuple]) -> None:
        out_dir = server_dir / "boto3"
        out_dir.mkdir(parents=True, exist_ok=True)
        with_mapping = [(t, m) for t, m in mapped if m is not None]
        if not with_mapping:
            return
        code = self._boto3_gen.generate_module(server_name, with_mapping)
        (out_dir / "tools.py").write_text(code)
        (out_dir / "__init__.py").write_text("")
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.py'}")

    def _write_cli(self, server_dir: Path, server_name: str, mapped: list[tuple]) -> None:
        out_dir = server_dir / "cli"
        out_dir.mkdir(parents=True, exist_ok=True)
        with_mapping = [(t, m) for t, m in mapped if m is not None]
        if not with_mapping:
            return
        code = self._cli_gen.generate_module(server_name, with_mapping)
        (out_dir / "tools.sh").write_text(code)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.sh'}")

    def _write_schema(self, server_dir: Path, server_name: str, tools: list[ToolDefinition]) -> None:
        out_dir = server_dir / "schema"
        out_dir.mkdir(parents=True, exist_ok=True)
        code = self._schema_gen.generate_module(server_name, tools)
        (out_dir / "tools.json").write_text(code)
        console.print(f"  [green]Wrote:[/] {out_dir / 'tools.json'}")

    def _write_skills(self, server_dir: Path, mapped: list[tuple]) -> None:
        out_dir = server_dir / "skill"
        out_dir.mkdir(parents=True, exist_ok=True)
        for tool, mapping in mapped:
            skill_content = self._skill_gen.generate_skill(tool, mapping)
            filename = tool.name.replace("_", "-") + ".md"
            (out_dir / filename).write_text(skill_content)
        console.print(f"  [green]Wrote:[/] {len(mapped)} skills to {out_dir}")
