import importlib
import inspect
import pkgutil

from forge.plugins.base import Plugin


class PluginManager:

    def __init__(self):

        self.plugins = []

    def discover(self):

        package = importlib.import_module("forge.plugins")

        for _, module_name, ispkg in pkgutil.iter_modules(package.__path__):

            if not ispkg:
                continue

            try:

                module = importlib.import_module(
                    f"forge.plugins.{module_name}.plugin"
                )

            except ModuleNotFoundError:

                continue

            for _, obj in inspect.getmembers(module):

                if inspect.isclass(obj):

                    if issubclass(obj, Plugin) and obj is not Plugin:

                        self.plugins.append(obj())

    def initialize(self):

        for plugin in self.plugins:

            plugin.initialize()

    def capabilities(self):

        caps = []

        for plugin in self.plugins:

            caps.extend(plugin.capabilities)

        return caps