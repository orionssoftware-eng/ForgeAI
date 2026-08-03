from pathlib import Path
import importlib
import inspect

from forge.plugins.base import Plugin
from forge.tools.registry import ToolRegistry


class PluginManager:

    def __init__(self):

        self.plugins = []

        self.tool_registry = ToolRegistry()

    def discover(self):

        plugins_dir = Path(__file__).parent

        for folder in plugins_dir.iterdir():

            if not folder.is_dir():
                continue

            if folder.name.startswith("__"):
                continue

            plugin_file = folder / "plugin.py"

            if not plugin_file.exists():
                continue

            module_name = f"forge.plugins.{folder.name}.plugin"

            try:

                module = importlib.import_module(module_name)

            except Exception as e:

                print(e)

                continue

            for _, obj in inspect.getmembers(module, inspect.isclass):

                if issubclass(obj, Plugin) and obj is not Plugin:

                    self.plugins.append(obj())

    def initialize(self):

        for plugin in self.plugins:

            plugin.initialize()

    def register_tools(self):

        for plugin in self.plugins:

            plugin.register_tools(self.tool_registry)

    def capabilities(self):

        capabilities = []

        for plugin in self.plugins:

            capabilities.extend(plugin.capabilities)

        return capabilities