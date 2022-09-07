"""Response Utils Module"""

from typing import Any, Dict, Tuple
from logging import Logger
import logging

logger: Logger = logging.getLogger("default")


def internal_server_error(error: Exception) -> Tuple[Dict, int]:
    """Default internal server error"""

    logger.exception(("%s", error))

    return {
        "message": "Internal server error",
    }, 500


def success_response(data: Any, status_code: int = 200) -> Tuple[Any, int]:
    """Default success response"""

    return data, status_code
