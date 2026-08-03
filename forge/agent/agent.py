from forge.providers.ollama import OllamaProvider
from forge.plugins.manager import PluginManager

from forge.pipeline.cleaner import CodeCleaner
from forge.pipeline.validator import CodeValidator
from forge.pipeline.security import SecurityFilter

from forge.core.execution_engine import ExecutionEngine


class Agent:

    def __init__(self):

        self.llm = OllamaProvider()

        self.plugins = PluginManager()
        
        self.engine = None

    async def initialize(self):

        self.plugins.discover()

        await self.plugins.initialize()

        self.plugins.register_tools()
        
        tool = self.plugins.tool_registry.get(
            "execute_blender_code"
        )

        self.engine = ExecutionEngine(
            self.llm,
            tool
        )

    async def execute(self, prompt: str):

        print("\n==============================")
        print("Qwen...")
        print("==============================")

        code = self.llm.generate(prompt)

        code = CodeCleaner.clean(code)

        print(code)

        ok, err = CodeValidator.validate(code)

        if not ok:

            print(err)

            return

        ok, blocked = SecurityFilter.check(code)

        if not ok:

            print("Blocked:", blocked)

            return

        tool = self.plugins.tool_registry.get(
            "execute_blender_code"
        )

        if tool is None:

            print("Tool non trovato")

            return

        print("\n==============================")
        print("Blender...")
        print("==============================")

        result = await self.engine.execute(
            prompt,
            code
        )

        return result