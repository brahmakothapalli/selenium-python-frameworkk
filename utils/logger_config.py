import inspect
import logging
from pathlib import Path


def get_logger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    console_handle = logging.StreamHandler()

    root_dir = Path().cwd().parent

    logs_file_path = str(root_dir)+"/logs/logs.log"

    file_handle = logging.FileHandler(logs_file_path)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    console_handle.setFormatter(formatter)
    print("Sample test code")
    file_handle.setFormatter(formatter)
    logger.addHandler(console_handle)
    logger.addHandler(file_handle)
    return logger
