import logging
import sys

from app.core.config import get_settings


def setup_logging() -> None:
    settings = get_settings()
    level = logging.DEBUG if settings.APP_ENV == "development" else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
