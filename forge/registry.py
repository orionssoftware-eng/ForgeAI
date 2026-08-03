class MCPRegistry:

    def __init__(self):

        self.connections = {}

    def register(self, connection):

        self.connections[connection.id] = connection

    def get(self, id):

        return self.connections.get(id)

    def all(self):

        return self.connections.values()