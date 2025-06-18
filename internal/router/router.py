# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/30 17:07
@Author : qin863
@File   : router.py
"""
from crypt import methods
from dataclasses import dataclass

from injector import inject
from flask import Flask, Blueprint
from internal.handler.app_handler import AppHandler


@inject
@dataclass
# 定义一个名为Router的类
class Router:
    """路由"""

    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 创建一个蓝图

        bp = Blueprint("llmops", __name__, url_prefix="")
        #  将url与对应的控制器方法绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule(
            "/v1/completion", methods=["POST"], view_func=self.app_handler.completion
        )
        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule(
            "/app/<uuid:id>", methods=["GET"], view_func=self.app_handler.get_app
        )
        bp.add_url_rule(
            "/app/<uuid:id>", methods=["POST"], view_func=self.app_handler.update_app
        )
        bp.add_url_rule(
            "/app/<uuid:id>/delete",
            methods=["POST"],
            view_func=self.app_handler.delete_app,
        )
        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
