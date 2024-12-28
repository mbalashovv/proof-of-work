import logging

from src.config import Config

__all__ = (
    "get_logger",
)

LOGGING_FORMAT = "%(asctime)s - [%(levelname)s] - %(name)s: %(message)s"

# ANSI escape codes for colors
LOG_COLORS = {
    "DEBUG": "\033[36m",  # Cyan
    "INFO": "\033[34m",  # Blue
    "WARNING": "\033[33m",  # Yellow
    "ERROR": "\033[31m",  # Red
    "CRITICAL": "\033[1;31m",  # Bold Red
    "RESET": "\033[0m",  # Reset to default
}


class ColorFormatter(logging.Formatter):
    def format(self, record):
        # Add color to the level name
        log_color = LOG_COLORS.get(record.levelname, LOG_COLORS["RESET"])
        record.levelname = f"{log_color}{record.levelname}{LOG_COLORS['RESET']}"

        return super().format(record)


def _get_stream_handler():
    formatter = ColorFormatter(LOGGING_FORMAT)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    handler = _get_stream_handler()
    logger.addHandler(handler)
    logger.setLevel(Config.LOGGING_LEVEL)
    return logger
