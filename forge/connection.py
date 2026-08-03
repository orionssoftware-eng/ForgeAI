from dataclasses import dataclass


@dataclass
class MCPConnection:

    id: str

    name: str

    transport: str

    command: list[str]

    connected: bool = False