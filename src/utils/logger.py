# -*- coding: utf-8 -*-
"""Logger
This script will support a flexible event logging system for applications and libraries. 
Note: 
1) That logs can be formattable and are not limited to the string datatype.
2) The use of logging in your programs will not cause it to exit the code, it will raise these logs
in your CLI (sometimes in different colors depending on which logging method you've used)!

DEBUG: 
    This level is used for detailed information, typically of interest only when diagnosing problems.
INFO: 
    This level is used to confirm that things are working as expected.
WARNING: 
    This level is used to indicate that something unexpected happened, or indicative of some problem
    in the near future (e.g., 'disk space low'). The software is still working as expected.
ERROR: 
    This level indicates a more serious problem, due to which the software has not been able to perform
    some function.
CRITICAL: 
    This level is used to indicate a very serious error that might cause the program to stop running.
EXCEPTION: 
    This is a special level of ERROR, usually used in an exception handler. This logs an ERROR level 
    message along with the stack trace.
"""
import json
import logging
from typing import Any

LOG_FORMAT = json.dumps(
    {
        "level": "%(levelname)s",
        "line": "%(name)s:%(funcName)s:%(lineno)d",
        "message": "%(message)s",
        "time": "%(asctime)s.%(msecs)d",
    }
)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_NAME = "nl2sql"

HANDLER = logging.StreamHandler()
HANDLER.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

LOG = logging.getLogger(LOG_NAME)
LOG.setLevel(logging.INFO)
LOG.propagate = False
LOG.addHandler(HANDLER)

debug = LOG.debug
error = LOG.error
exception = LOG.exception
info = LOG.info
warning = LOG.warning
critical = LOG.critical


def log_raise(log_type: str, error_message: str, error_type: error = ValueError) -> Any:
  """This function will support raising an error message.

  Args:
    log_type (str): String indicating the type of log.
    error_message (str): String indicating the error message.
    error_type (Error): Built in Python exceptions.

  Raises:
    The assocaited exception passed in as error_type.
  """
    if log_type == 'error':
        LOG.error(error_message)
        raise error_type(error_message)

    elif log_type == 'critical':
        LOG.critical(error_message)
        raise error_type(error_message)
