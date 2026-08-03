from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class Capability:
    name: str
    description: str


class Plugin(ABC):

    name: str = ""
    version: str = "0.1"

    capabilities: List[Capability] = []

    def initialize(self):
        """Called when ForgeAI starts."""
        pass