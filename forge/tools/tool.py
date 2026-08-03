from dataclasses import dataclass
from typing import Callable


@dataclass
class Tool:

    name: str

    description: str

    handler: Callable

    category: str = "generic"

    async_tool: bool = False