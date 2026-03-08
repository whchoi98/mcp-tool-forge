from __future__ import annotations
import asyncio
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from mcp_to_cli.pipeline import Pipeline
from mcp_to_cli.registry import ServerRegistry

console = Console(width=200)


@click.group()
@click.version_option(version="0.1.0", prog_name="mcp-to-cli")
def main():
    """MCP-to-CLI: Convert MCP server tools to boto3/CLI/schema/skill outputs."""
    pass


@main.command()
@click.option("--category", "-c", help="Filter by category")
def list_servers(category):
    """List all registered MCP servers."""
    registry = ServerRegistry()
    if category:
        servers = registry.list_by_category(category)
    else:
        servers = registry.list_servers()

    table = Table(title="Registered MCP Servers")
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="green")
    table.add_column("Runtime", style="yellow")
    table.add_column("Package", style="dim")

    for s in sorted(servers, key=lambda x: (x.category, x.name)):
        table.add_row(s.name, s.category, s.runtime, s.package)

    console.print(table)
    console.print(f"\nTotal: {len(servers)} servers")


@main.command()
@click.option("--server", "-s", required=True, help="Server name from registry")
def list_tools(server):
    """List tools from an MCP server (connects to server)."""
    registry = ServerRegistry()
    config = registry.get(server)
    if not config:
        console.print(f"[red]Error:[/] Server '{server}' not found in registry")
        raise SystemExit(1)

    from mcp_to_cli.connector import MCPConnector

    async def _list():
        connector = MCPConnector()
        tools = await connector.list_tools_from_config(config)
        table = Table(title=f"Tools from {server}")
        table.add_column("Name", style="cyan")
        table.add_column("Description")
        table.add_column("Params", style="yellow")
        for t in tools:
            params = ", ".join(t.get("inputSchema", {}).get("properties", {}).keys())
            table.add_row(t["name"], t.get("description", "")[:80], params)
        console.print(table)
        console.print(f"\nTotal: {len(tools)} tools")

    asyncio.run(_list())


@main.command()
@click.option("--server", "-s", help="Server name (or --all-servers)")
@click.option("--all-servers", "all_flag", is_flag=True, help="Convert all servers")
@click.option("--output", "-o", default="all", help="Output formats: boto3,cli,schema,skill,all")
@click.option("--llm-assist", is_flag=True, help="Use LLM for unmapped tools (Phase 3)")
@click.option("--output-dir", "-d", default="output", help="Output directory")
def convert(server, all_flag, output, llm_assist, output_dir):
    """Convert MCP tools to boto3/CLI/schema/skill outputs."""
    if not server and not all_flag:
        console.print("[red]Error:[/] Specify --server or --all-servers")
        raise SystemExit(1)

    outputs = ["boto3", "cli", "schema", "skill"] if output == "all" else output.split(",")
    registry = ServerRegistry()
    out_path = Path(output_dir)

    if all_flag:
        configs = registry.list_servers()
    else:
        config = registry.get(server)
        if not config:
            console.print(f"[red]Error:[/] Server '{server}' not found")
            raise SystemExit(1)
        configs = [config]

    async def _convert():
        pipeline = Pipeline(output_dir=out_path)
        results = []
        for cfg in configs:
            try:
                result = await pipeline.run(cfg, outputs=outputs, llm_assist=llm_assist)
                results.append(result)
            except Exception as e:
                console.print(f"[red]Error[/] converting {cfg.name}: {e}")
                results.append({"server": cfg.name, "error": str(e)})

        console.print("\n[bold]Summary:[/]")
        table = Table()
        table.add_column("Server", style="cyan")
        table.add_column("Tools")
        table.add_column("Static")
        table.add_column("LLM")
        table.add_column("Unmapped")
        for r in results:
            if "error" in r:
                table.add_row(r["server"], "[red]ERROR[/]", "", "", "")
            else:
                table.add_row(
                    r["server"], str(r["tools_count"]),
                    str(r["static_mapped"]), str(r["llm_mapped"]), str(r["unmapped"]),
                )
        console.print(table)

    asyncio.run(_convert())


if __name__ == "__main__":
    main()
