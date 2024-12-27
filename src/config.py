import os

__all__ = (
    "Config",
)


class Config:
    SERVER_HOST = os.getenv('SERVER_HOST', "localhost")
    SERVER_PORT = int(os.getenv('SERVER_PORT', 9000))
    POW_DIFFICULTY = int(os.getenv('POW_DIFFICULTY', 4))
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', "INFO")
