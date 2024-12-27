import logging

from src.config import Config

__all__ = (
    "get_logger",
)

LOGGING_FORMAT = "%(asctime)s - [%(levelname)s] - %(name)s: %(message)s "


def _get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    handler = _get_stream_handler()
    logger.addHandler(handler)
    logger.setLevel(Config.LOGGING_LEVEL)
    return logger
