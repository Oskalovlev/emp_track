import os
import logging
import logging.handlers

# from django.conf import settings
from services.constants.logger import (
    LOG_DIR,
    LOG_FILE,
    LOG_FORMAT,
    LOG_MESSAGE,
    LOG_PASS_FILTER,
)


def password_filter(log: logging.LogRecord) -> int:
    if LOG_PASS_FILTER in str(log.msg):
        return 0
    return 1


def create_file_log(file):
    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)
    os.open(LOG_FILE, flags=os.O_CREAT)
    return file


def init_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(LOG_FORMAT, encoding="UTF-8"))
    sh.setLevel(logging.DEBUG)
    sh.addFilter(password_filter)

    fh = logging.handlers.RotatingFileHandler(
        filename=create_file_log(file=LOG_FILE)
    )
    fh.setFormatter(logging.Formatter(LOG_FORMAT, encoding="UTF-8"))
    fh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug(LOG_MESSAGE)
