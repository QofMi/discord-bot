import os
import logging
from bot.bot import *
from bot.config import *


# Построение путей внутри проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f"{BASE_DIR}/bot.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    run()
