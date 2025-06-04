# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/30 17:07
@Author : qin863
@File   : router.py
"""
from injector import inject
from flask import Flask,Blueprint
from internal.handler.app_handler import AppHandler


@inject
class Router:
    """路由"""
    app_handler = AppHandler()

    def register_router(self, app: Flask):
        """注册路由"""
        # 创建一个蓝图

        bp = Blueprint("llmops",__name__,url_prefix="")
        #  将url与对应的控制器方法绑定
        bp.add_url_rule("/ping",view_func=self.app_handler.ping)
        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)