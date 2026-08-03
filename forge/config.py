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

    mcp_command: str = os.getenv(
        "MCP_COMMAND",
        "python"
    )

    mcp_args: list = None

    def __post_init__(self):

        if self.mcp_args is None:

            self.mcp_args = [
                "-m",
                "blender_mcp.server"
            ]


settings = Settings()