class ExecutionEngine:

    MAX_RETRY = 3

    def __init__(self, llm, tool):

        self.llm = llm
        self.tool = tool

    async def execute(self, prompt: str, code: str):

        current_code = code

        for attempt in range(self.MAX_RETRY):

            print()
            print("=" * 50)
            print(f"EXECUTION {attempt+1}/{self.MAX_RETRY}")
            print("=" * 50)

            result = await self.tool.handler(current_code)

            text = str(result)

            if "Error executing code" not in text:

                print("✓ Execution completed")

                return result

            print("✗ Execution failed")

            current_code = self.fix_code(
                prompt,
                current_code,
                text
            )

        return result

    def fix_code(self, prompt, code, error):

        repair_prompt = f"""
You previously generated Blender Python code.

The execution failed.

ORIGINAL REQUEST

{prompt}

GENERATED CODE

{code}

ERROR

{error}

Rewrite the COMPLETE script.

Rules:

- Blender 5.2
- bpy only
- Output ONLY python
- No markdown
- No explanations
"""

        return self.llm.generate(repair_prompt)