from forge.plugins.base import Plugin, Capability
from forge.tools.tool import Tool
from forge.connectors.blender.blender_client import BlenderClient


class BlenderPlugin(Plugin):

    name = "Blender"
    version = "1.0"

    capabilities = [
        Capability("3d_modeling", "Create and edit meshes"),
        Capability("materials", "Materials"),
    ]

    def __init__(self):

        self.client = BlenderClient()

    async def initialize(self):

        await self.client.connect()

        print("✓ Blender initialized")

    async def execute_code(self, code: str):

        return await self.client.execute_code(code)

    def register_tools(self, registry):

        registry.register(

            Tool(
                name="execute_blender_code",
                description="Execute Python inside Blender",
                handler=self.execute_code,
            )

        )