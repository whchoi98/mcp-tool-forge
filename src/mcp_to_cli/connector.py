"""MCP server connector for extracting tool schemas.
도구 스키마 추출을 위한 MCP 서버 커넥터."""

from __future__ import annotations

import asyncio
import os
import tempfile

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

from mcp_to_cli.models import ServerConfig


class MCPConnector:
    """Connects to MCP servers and extracts tool schemas via MCP SDK.
    MCP SDK를 통해 MCP 서버에 연결하고 도구 스키마를 추출합니다."""

    def _build_command(
        self, runtime: str, package: str, extra_args: list[str]
    ) -> tuple[str, list[str]]:
        """Build the command and arguments for the given runtime.
        주어진 런타임에 대한 명령어와 인자를 구성합니다."""
        if runtime == "npx":
            return "npx", ["-y", package] + extra_args
        elif runtime == "uvx":
            return "uvx", package.split() + extra_args
        else:
            raise ValueError(f"Unknown runtime: {runtime}")

    def _build_server_params(self, config: ServerConfig) -> StdioServerParameters:
        """Build server parameters from config.
        설정에서 서버 파라미터를 구성합니다."""
        # Build command and arguments / 명령어 및 인자 구성
        cmd, args = self._build_command(config.runtime, config.package, config.args)
        # Merge environment variables if provided / 환경 변수가 있으면 병합
        env = {**os.environ, **config.env} if config.env else None
        return StdioServerParameters(command=cmd, args=args, env=env)

    async def list_tools_from_config(
        self, config: ServerConfig, timeout: float = 60
    ) -> list[dict]:
        """Connect to MCP server, list tools, return raw dicts.
        MCP 서버에 연결하여 도구 목록을 조회하고 원시 딕셔너리로 반환합니다."""
        # Build server parameters / 서버 파라미터 구성
        params = self._build_server_params(config)

        async def _connect() -> list[dict]:
            # Create temp file for error logging / 에러 로깅용 임시 파일 생성
            errfile = tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False)
            try:
                # Establish stdio connection and session / stdio 연결 및 세션 설정
                async with stdio_client(params, errlog=errfile) as (read, write):
                    async with ClientSession(read, write) as session:
                        await session.initialize()
                        result = await session.list_tools()
                        # Convert tool objects to raw dicts / 도구 객체를 원시 딕셔너리로 변환
                        return [
                            {
                                "name": tool.name,
                                "description": tool.description or "",
                                "inputSchema": tool.inputSchema,
                            }
                            for tool in result.tools
                        ]
            finally:
                # Clean up temp error log / 임시 에러 로그 정리
                errfile.close()
                try:
                    os.unlink(errfile.name)
                except OSError:
                    pass

        try:
            # Apply timeout to connection attempt / 연결 시도에 타임아웃 적용
            return await asyncio.wait_for(_connect(), timeout=timeout)
        except asyncio.TimeoutError:
            raise TimeoutError(
                f"Timed out connecting to {config.name} after {timeout}s"
            )

    async def list_tools(self) -> list[dict]:
        """Legacy interface - use list_tools_from_config instead.
        레거시 인터페이스 - 대신 list_tools_from_config를 사용하세요."""
        return await self._call_tools_list()

    async def _call_tools_list(self) -> list[dict]:
        """Legacy raw JSON-RPC - kept for tests that mock this.
        레거시 원시 JSON-RPC - 이를 모킹하는 테스트를 위해 유지됩니다."""
        raise NotImplementedError("Use list_tools_from_config with MCP SDK")
