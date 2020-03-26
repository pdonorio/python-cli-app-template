import sys
from loguru import logger
from devtools import debug  # noqa


def reset_level(verbose: bool = False):
    if verbose:
        logger_level_name = "DEBUG"
    else:
        logger_level_name = "INFO"

    logger.remove()  # remove defaults
    logger.add(
        sys.stdout,
        colorize=True,
        # colorize=False,
        level=logger_level_name,
        # enqueue=True,  # NOTE: handle async context
        # format="<green>{time}</green> <level>{message}</level>",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{message}</level>",
    )
