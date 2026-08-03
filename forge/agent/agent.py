from forge.providers.ollama import OllamaProvider
from forge.plugins.manager import PluginManager
from forge.pipeline.cleaner import CodeCleaner
from forge.pipeline.validator import CodeValidator
from forge.pipeline.security import SecurityFilter


class Agent:

    def __init__(self):

        self.llm = OllamaProvider()

        self.plugins = PluginManager()

    async def initialize(self):

        self.plugins.discover()

        await self.plugins.initialize()

        self.plugins.register_tools()

    async def execute(self, prompt):

        code = self.llm.generate(prompt)

        code = CodeCleaner.clean(code)

        ok, error = CodeValidator.validate(code)

        if not ok:
            print(error)
            return

        ok, blocked = SecurityFilter.check(code)

        if not ok:
            print(blocked)
            return

        tool = self.plugins.tool_registry.get(
            "execute_blender_code"
        )

        return await tool.handler(code)