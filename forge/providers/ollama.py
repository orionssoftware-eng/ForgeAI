import ollama

from forge.config import settings
from forge.providers.base import LLMProvider


SYSTEM_PROMPT = """
You are an expert Blender Python developer.

Your job is to generate ONLY executable Python code for Blender.

Rules:

- Output ONLY Python code.
- Never use Markdown.
- Never use ```python.
- Never explain.
- Never apologize.
- Never answer in natural language.
- Use only the bpy API.
- Assume the code is executed inside Blender.
"""


class OllamaProvider(LLMProvider):

    def __init__(self):

        self.client = ollama.Client(
            host=settings.ollama_host
        )

        self.model = settings.ollama_model

    def generate(self, prompt: str) -> str:

        print("\n==============================")
        print("OLLAMA")
        print("==============================")
        print("HOST :", settings.ollama_host)
        print("MODEL:", self.model)
        print()

        response = self.client.chat(

            model=self.model,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        )

        print("RAW RESPONSE")
        print(response)
        print()

        return response["message"]["content"]