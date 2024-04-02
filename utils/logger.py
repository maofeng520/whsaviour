import logging
import os
import time
from config.setting import log_path


def log(file_path):
    loggers = logging.getLogger("log")
    loggers.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    fh = logging.FileHandler(file_path, mode='a', encoding='utf-8')

    sh.setLevel(logging.INFO)
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter(fmt='%(asctime)s | %(levelname)s | %(filename)s: %(lineno)d|%(message)s')

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    loggers.addHandler(sh)
    loggers.addHandler(fh)

    return loggers


logger = log(file_path=log_path)

if __name__ == '__main__':
    pass
    # logger = log(file_path='../log/test.log')
    # logger.debug('debug')
    # logger.info('info')
    # logger.warning('warning')
    # logger.error('error')
    # logger.critical('critical')
