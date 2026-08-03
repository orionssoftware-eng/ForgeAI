from __future__ import annotations

from typing import Any

from mcp.client.session import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters,
)

from forge.config import settings


class BlenderClient:
    """
    Client MCP per Blender.

    Espone un'interfaccia semplice al resto del programma.
    Il resto dell'app NON deve conoscere MCP.
    """

    def __init__(self):

        self.session: ClientSession | None = None
        self._stdio = None
        self.connected = False

    async def connect(self):

        if self.connected:
            return

        params = StdioServerParameters(
            command=settings.mcp_command,
            args=settings.mcp_args,
        )

        self._stdio = stdio_client(params)

        read_stream, write_stream = await self._stdio.__aenter__()

        self.session = ClientSession(
            read_stream,
            write_stream,
        )

        await self.session.__aenter__()

        await self.session.initialize()

        self.connected = True

        print("✓ Blender MCP Connected")

    async def disconnect(self):

        if not self.connected:
            return

        await self.session.__aexit__(None, None, None)

        await self._stdio.__aexit__(None, None, None)

        self.connected = False

        print("✓ Blender MCP Disconnected")

    async def list_tools(self):

        return await self.session.list_tools()

    async def execute_code(self, code: str):

        return await self.session.call_tool(
            "execute_blender_code",
            {
                "code": code
            }
        )

    async def get_scene(self):

        return await self.session.call_tool(
            "get_scene_info",
            {}
        )

    async def get_object(self, name: str):

        return await self.session.call_tool(
            "get_object_info",
            {
                "name": name
            }
        )

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ):

        return await self.session.call_tool(
            tool_name,
            arguments,
        )