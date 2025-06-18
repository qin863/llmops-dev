# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/11 10:04
@Author : qin863
@File   : config.py
"""
import os

from decouple import config


class Config:
    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = config("WTF_CSRF_ENABLED", False, cast=bool)
        # 数据库配置
        self.SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": config("SQLALCHEMY_POOL_SIZE", cast=int),
            "pool_recycle": config("SQLALCHEMY_POOL_RECYCLE", cast=int),
        }
        self.SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO", False, cast=bool)
