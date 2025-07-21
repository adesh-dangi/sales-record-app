import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

path_dir_log = "logs"

def setup_logger(log_name=None):
    if log_name is None:
        log_name = "sales_app"+"_"+str(datetime.now().date()).replace("-", "_")
    log_dir = path_dir_log
    os.makedirs(log_dir, exist_ok=True)
    print(log_name)
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    # File handler with daily rotation
    file_handler = TimedRotatingFileHandler(
        filename=f"{log_dir}/{log_name}.log",
        when='midnight',
        interval=1,
        backupCount=30,
        encoding='utf-8'
    )
    file_handler.suffix = "%Y-%m-%d"
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
logger = setup_logger()

# test = setup_logger()

# test.info("Info log test")
# test.error("Error log test")
# test.debug("Debug log test")