# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/12 10:00
@Author : qin863
@File   : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    """自定义异常"""

    code: HttpCode = HttpCode.FAIL
    msg: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, msg: str = None, data: Any = None):
        super().__init__()
        self.msg = msg or self.msg
        self.data = data or self.data


class FailException(CustomException):
    """通用失败异常"""

    pass


class NotFoundException(CustomException):
    """资源未找到异常"""

    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    """未授权异常"""

    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    """禁止访问异常"""

    code = HttpCode.FORBIDDEN


class InternalServerError(CustomException):
    """服务器内部错误"""

    code = HttpCode.INTERNAL_SERVER_ERROR


class BadRequestException(CustomException):
    """请求参数错误"""

    code = HttpCode.BAD_REQUEST


class ValidationException(CustomException):
    """验证异常"""

    code = HttpCode.VALIDATION_ERROR
