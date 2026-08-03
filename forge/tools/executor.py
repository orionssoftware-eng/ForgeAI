import inspect


class ToolExecutor:

    async def execute(self, tool, **kwargs):

        if inspect.iscoroutinefunction(tool.handler):

            return await tool.handler(**kwargs)

        return tool.handler(**kwargs)