"""Process remaining servers with Opus 4.6."""
import asyncio
from mcp_to_cli.pipeline import Pipeline
from mcp_to_cli.registry import ServerRegistry
from mcp_to_cli.cache import SchemaCache
from pathlib import Path

async def main():
    registry = ServerRegistry()
    pipeline = Pipeline(output_dir=Path("output"))
    cache = SchemaCache()
    done = set()
    for d in Path("output").iterdir():
        if d.is_dir() and (d / "boto3").exists():
            done.add(d.name)
    remaining = []
    for s in registry.list_servers():
        tools = cache.load(s.name)
        if tools and len(tools) > 0 and s.name not in done:
            remaining.append((s, len(tools)))
    remaining.sort(key=lambda x: x[1])
    print(f"Remaining: {len(remaining)} servers")
    for config, tc in remaining:
        try:
            r = await pipeline.run(config, outputs=["boto3", "cli"], llm_assist=True)
            s = r["static_mapped"]
            l = r["llm_mapped"]
            u = r["unmapped"]
            t = r["tools_count"]
            print(f"OK [{config.name}]: {t}t -> {s}s/{l}l/{u}u")
        except Exception as e:
            print(f"ERR [{config.name}]: {str(e)[:80]}")

asyncio.run(main())
