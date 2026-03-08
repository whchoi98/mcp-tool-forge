from __future__ import annotations

import asyncio
import json
import os
from typing import Any

from mcp_to_cli.models import ServerConfig


class MCPConnector:
    """Connects to MCP servers and extracts tool schemas."""

    def __init__(self):
        self._process: asyncio.subprocess.Process | None = None

    def _build_command(
        self, runtime: str, package: str, extra_args: list[str]
    ) -> tuple[str, list[str]]:
        if runtime == "npx":
            return "npx", ["-y", package] + extra_args
        elif runtime == "uvx":
            return "uvx", [package] + extra_args
        else:
            raise ValueError(f"Unknown runtime: {runtime}")

    async def connect_stdio(self, config: ServerConfig) -> None:
        cmd, args = self._build_command(config.runtime, config.package, config.args)
        env = {**os.environ, **config.env}
        self._process = await asyncio.create_subprocess_exec(
            cmd, *args,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )

    async def _send_jsonrpc(self, method: str, params: dict | None = None) -> dict:
        if not self._process or not self._process.stdin or not self._process.stdout:
            raise RuntimeError("Not connected to any MCP server")
        request: dict[str, Any] = {"jsonrpc": "2.0", "id": 1, "method": method}
        if params:
            request["params"] = params
        msg = json.dumps(request)
        content = f"Content-Length: {len(msg)}\r\n\r\n{msg}"
        self._process.stdin.write(content.encode())
        await self._process.stdin.drain()
        headers: dict[str, str] = {}
        while True:
            line = await self._process.stdout.readline()
            line_str = line.decode().strip()
            if not line_str:
                break
            if ":" in line_str:
                key, value = line_str.split(":", 1)
                headers[key.strip()] = value.strip()
        content_length = int(headers.get("Content-Length", 0))
        if content_length > 0:
            body = await self._process.stdout.readexactly(content_length)
            return json.loads(body)
        return {}

    async def _call_tools_list(self) -> list[dict]:
        await self._send_jsonrpc("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "mcp-to-cli", "version": "0.1.0"},
        })
        notif = json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"})
        content = f"Content-Length: {len(notif)}\r\n\r\n{notif}"
        if self._process and self._process.stdin:
            self._process.stdin.write(content.encode())
            await self._process.stdin.drain()
        response = await self._send_jsonrpc("tools/list")
        return response.get("result", {}).get("tools", [])

    async def list_tools(self) -> list[dict]:
        return await self._call_tools_list()

    async def list_tools_from_config(self, config: ServerConfig) -> list[dict]:
        try:
            await self.connect_stdio(config)
            return await asyncio.wait_for(self.list_tools(), timeout=30)
        finally:
            await self.disconnect()

    async def disconnect(self) -> None:
        if self._process:
            try:
                self._process.terminate()
                await asyncio.wait_for(self._process.wait(), timeout=5)
            except (asyncio.TimeoutError, ProcessLookupError):
                self._process.kill()
            self._process = None
