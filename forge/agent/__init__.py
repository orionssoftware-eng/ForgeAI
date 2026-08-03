from forge.core.execution_engine import ExecutionEngine

class Agent:

    def __init__(self):

        self.llm = OllamaProvider()

        self.plugins = PluginManager()

        self.engine = None