import logging


def error_logger():
    logger = logging.getLogger("Step_Errors")
    handler = logging.FileHandler("logs/test_log_errors.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def info_logger():
    logger = logging.getLogger("Step_Info")
    handler = logging.FileHandler("logs/test_log_info.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
