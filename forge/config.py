from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:

    ollama_host: str = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434"
    )

    ollama_model: str = os.getenv(
        "OLLAMA_MODEL",
        "qwen2.5-coder:7b"
    )

    log_level: str = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )


settings = Settings()