# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/11 16:38
@Author : qin863
@File   : http.py
"""
import os

from decouple import config
from flask import Flask
from flask_migrate import Migrate

from config import Config
from internal.exception.exception import CustomException
from internal.model import App
from pkg.response import HttpCode
from pkg.response.response import json, Response
from pkg.sqlalchemy import SQLAlchemy
from internal.router import Router


class Http(Flask):
    """Http引擎"""

    def __init__(
        self,
        name: str,
        conf: Config,
        db: SQLAlchemy,
        migrate: Migrate,
        router: Router,
        *args,
        **kwargs
    ):
        #  1.调用父类构造函数初始化
        super().__init__(name, *args, **kwargs)

        # 2.初始化应用配置
        self.config.from_object(conf)

        # 3.注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)
        # 4.初始化flask扩展
        db.init_app(self)
        # with self.app_context():
        #     _ = App()
        #     db.create_all()
        migrate.init_app(self, db, directory="internal/migration")
        # 5.注册路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        #     1. 判断异常信息是否是自定义异常，如果是，提取msg和code
        if isinstance(error, CustomException):
            return json(Response(code=HttpCode.FAIL, msg=str(error), data={}))
        #   2. 如果不是自定义异常，则可能是程序或数据库抛出异常，提取信息，设置状态吗
        if self.debug or config("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(code=HttpCode.FAIL, msg=str(error), data={}))
