# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/12 10:06
@Author : qin863
@File   : http_code.py
"""

from enum import Enum


class HttpCode(str, Enum):
    """http业务状态吗"""

    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    INTERNAL_SERVER_ERROR = "internal server error"
    BAD_REQUEST = "bad request"
    VALIDATION_ERROR = "validation error"
    NOT_IMPLEMENTED = "not implemented"
    TIMEOUT = "timeout"
