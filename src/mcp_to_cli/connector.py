from __future__ import annotations

import asyncio
import os
import tempfile

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

from mcp_to_cli.models import ServerConfig


class MCPConnector:
    """Connects to MCP servers and extracts tool schemas via MCP SDK."""

    def _build_command(
        self, runtime: str, package: str, extra_args: list[str]
    ) -> tuple[str, list[str]]:
        if runtime == "npx":
            return "npx", ["-y", package] + extra_args
        elif runtime == "uvx":
            return "uvx", package.split() + extra_args
        else:
            raise ValueError(f"Unknown runtime: {runtime}")

    def _build_server_params(self, config: ServerConfig) -> StdioServerParameters:
        cmd, args = self._build_command(config.runtime, config.package, config.args)
        env = {**os.environ, **config.env} if config.env else None
        return StdioServerParameters(command=cmd, args=args, env=env)

    async def list_tools_from_config(
        self, config: ServerConfig, timeout: float = 60
    ) -> list[dict]:
        """Connect to MCP server, list tools, return raw dicts."""
        params = self._build_server_params(config)

        async def _connect() -> list[dict]:
            errfile = tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False)
            try:
                async with stdio_client(params, errlog=errfile) as (read, write):
                    async with ClientSession(read, write) as session:
                        await session.initialize()
                        result = await session.list_tools()
                        return [
                            {
                                "name": tool.name,
                                "description": tool.description or "",
                                "inputSchema": tool.inputSchema,
                            }
                            for tool in result.tools
                        ]
            finally:
                errfile.close()
                try:
                    os.unlink(errfile.name)
                except OSError:
                    pass

        try:
            return await asyncio.wait_for(_connect(), timeout=timeout)
        except asyncio.TimeoutError:
            raise TimeoutError(
                f"Timed out connecting to {config.name} after {timeout}s"
            )

    async def list_tools(self) -> list[dict]:
        """Legacy interface - use list_tools_from_config instead."""
        return await self._call_tools_list()

    async def _call_tools_list(self) -> list[dict]:
        """Legacy raw JSON-RPC - kept for tests that mock this."""
        raise NotImplementedError("Use list_tools_from_config with MCP SDK")
