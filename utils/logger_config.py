import inspect
import logging
import sys


def get_logger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    console_handle = logging.StreamHandler()
    file_handle = logging.FileHandler("../logs/logs.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    console_handle.setFormatter(formatter)
    file_handle.setFormatter(formatter)
    logger.addHandler(console_handle)
    logger.addHandler(file_handle)

    # print("\n File Path: ", sys.path[0] + "\\logs\\report.log")
    # logging.basicConfig(filename=sys.path[0] + "\\logs\\report.log",
    #                     format='%(asctime)s - %(levelname)s - %(message)s',
    #                     level=logging.INFO)
    # logger_instance = logging.getLogger()
    return logger


