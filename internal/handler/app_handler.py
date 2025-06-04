# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/30 17:03
@Author : qin863
@File   : app_handler.py
"""


class AppHandler:
    """应用控制器"""

    def ping(self) -> dict[str, str]:
        return {"ping": "pong"}
