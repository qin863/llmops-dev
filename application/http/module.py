# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/12 11:00
@Author : qin863
@File   : module.py
"""
from flask_migrate import Migrate
from injector import Binder, Module

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
