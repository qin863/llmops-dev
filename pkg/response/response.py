# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/12 10:06
@Author : qin863
@File   : response.py
"""
from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from pkg.response.http_code import HttpCode


@dataclass
class Response:
    """基础Http接口响应格式"""

    code: HttpCode = HttpCode.SUCCESS
    msg: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """基础响应的接口"""
    return jsonify(data), 200


def success_json(data: Any = None):
    """成功数据的响应"""
    return json(Response(code=HttpCode.SUCCESS, msg="", data=data))


# 定义一个函数fail_json，参数data为任意类型，默认值为None
def fail_json(data: Any = None):
    """失败数据响应"""
    return json(Response(code=HttpCode.FAIL, msg="", data=data))


def validate_json(errors: dict = None):
    """验证失败响应"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATE, msg=msg, data=errors))


def message(code: HttpCode = None, msg: str = None):
    """基础的消息响应，固定返回消息提示，数据固定为空字典"""
    return json(Response(code=code, msg=msg, data={}))


# 定义一个函数success_message，用于返回成功信息
# 参数msg为字符串类型，默认值为None
def success_message(msg: str = None):
    # 调用message函数，传入参数code和msg，返回成功信息
    return message(code=HttpCode.SUCCESS, msg=msg)


# 定义一个函数fail_message，用于返回一个失败的消息
def fail_message(msg: str = None):
    # 返回一个message函数，参数为code和msg
    return message(code=HttpCode.FAIL, msg=msg)


# 定义一个函数，用于返回404错误信息
def not_found_message(msg: str = None):
    # 返回一个message对象，其中code为HttpCode.NOT_FOUND，msg为传入的参数msg
    return message(code=HttpCode.NOT_FOUND, msg=msg)


# 定义一个函数，用于返回未授权的消息
def unauthorized_message(msg: str = None):
    # 如果msg参数为空，则返回一个未授权的消息，否则返回一个包含msg参数的未授权消息
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


# 定义一个函数，用于返回禁止访问的消息
def forbidden_message(msg: str = None):
    # 如果msg参数为空，则返回一个禁止访问的消息，否则返回一个带有msg参数的禁止访问的消息
    return message(code=HttpCode.FORBIDDEN, msg=msg)
