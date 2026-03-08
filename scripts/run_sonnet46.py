"""Run Sonnet 4.6 LLM mapping on all cached servers.
캐시된 모든 서버에 대해 Sonnet 4.6 LLM 매핑을 실행합니다."""

import asyncio
import time
from pathlib import Path

from mcp_to_cli.pipeline import Pipeline
from mcp_to_cli.registry import ServerRegistry
from mcp_to_cli.cache import SchemaCache


async def main():
    registry = ServerRegistry()
    pipeline = Pipeline(output_dir=Path("output"))
    cache = SchemaCache()

    to_process = []
    for s in registry.list_servers():
        tools = cache.load(s.name)
        if tools and len(tools) > 0:
            to_process.append((s, len(tools)))

    to_process.sort(key=lambda x: x[1])
    total = sum(c for _, c in to_process)
    print(f"Sonnet 4.6 mapping: {len(to_process)} servers, {total} tools")
    print()

    start = time.time()
    ts, tl, tu, tt = 0, 0, 0, 0

    for config, tc in to_process:
        try:
            r = await pipeline.run(config, outputs=["boto3", "cli"], llm_assist=True)
            s = r["static_mapped"]
            l = r["llm_mapped"]
            u = r["unmapped"]
            ts += s
            tl += l
            tu += u
            tt += r["tools_count"]
            tc_val = r["tools_count"]
            print(f"OK [{config.name}]: {tc_val}t -> {s}s/{l}l/{u}u")
        except Exception as e:
            err = str(e)[:80]
            print(f"ERR [{config.name}]: {err}")

    elapsed = time.time() - start
    print()
    print("=" * 60)
    print("Sonnet 4.6 Results:")
    print(f"  Tools: {tt}, Static: {ts}, LLM: {tl}, Unmapped: {tu}")
    rate = tl / (tl + tu) * 100 if (tl + tu) > 0 else 0
    print(f"  LLM rate: {tl}/{tl+tu} = {rate:.1f}%")
    print(f"  Time: {elapsed:.0f}s")


if __name__ == "__main__":
    asyncio.run(main())
