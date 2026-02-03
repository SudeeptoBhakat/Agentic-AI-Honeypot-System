from loguru import logger
import sys

def setup_logging():
    logger.remove()
    logger.add("logs/app.log", rotation="10 MB")
    logger.add("logs/error.log", level="ERROR")
    logger.add(sys.stdout)