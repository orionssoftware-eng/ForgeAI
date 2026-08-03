import ollama

from forge.config import settings
from forge.providers.base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self):

        self.client = ollama.Client(
            host=settings.ollama_host
        )

        self.model = settings.ollama_model

    def generate(self, prompt: str) -> str:

        response = self.client.chat(

            model=self.model,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        )

        return response["message"]["content"]