# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.3 (main, Jul 25 2022, 17:09:16) [Clang 13.0.0 (clang-1300.0.27.3)]
# Embedded file name: /boot/LBBridge/LBBridge/log.py
# Compiled at: 2021-09-14 06:45:12
# Size of source mod 2**32: 1233 bytes
import logging, sys, os, logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_PATH = None
LOG_FILE = None
__logger = None

def __no_log(_):
    pass


debug = __no_log
info = __no_log
warning = __no_log
error = __no_log
critical = __no_log
exception = __no_log
setLevel = __no_log

def init_logger(name):
    global __logger
    global critical
    global debug
    global error
    global exception
    global info
    global setLevel
    global warning
    __logger = logging.getLogger(name)
    formatter = logging.Formatter(fmt='%(asctime)s | %(levelname)s - %(message)s')
    __logger.handlers = []
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    __logger.addHandler(stream_handler)
    setLevel = __logger.setLevel
    debug, info, warning, error, critical, exception = (
     __logger.debug, __logger.info, __logger.warning, __logger.error, __logger.critical,
     __logger.exception)
    setLevel(INFO)


def show_user(msg):
    critical(msg)