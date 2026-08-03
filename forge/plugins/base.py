from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import List




@dataclass
class Capability:
    name: str
    description: str


class Plugin(ABC):

    name = ""

    version = "0.1"

    capabilities = []

    tools = []

    def initialize(self):
        pass

    def register_tools(self, registry):
        pass