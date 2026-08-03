from forge.mcp.registry import MCPRegistry


class MCPManager:

    def __init__(self):

        self.registry = MCPRegistry()

    def register(self, connection):

        self.registry.register(connection)

    def list(self):

        return list(self.registry.all())