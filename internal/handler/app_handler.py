# -*- coding: utf-8 -*-
"""
@Time   : 2025/5/30 17:03
@Author : qin863
@File   : app_handler.py
"""
import uuid
from dataclasses import dataclass

from decouple import config
from injector import inject
from openai import OpenAI

from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_message
from pkg.response.response import success_json
from pkg.response.response import validate_json


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def create_app(self):
        """调用读物创建新的App记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建id={app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功创建id={app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用修改成功，名称为{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用删除成功id={app.id}")

    def ping(self) -> dict[str, str]:
        return {"ping": "pong"}

    def completion(self):
        """聊天接口"""
        # 1.从聊天接口中获取的输出，post
        req = CompletionReq()
        if not req.validate():
            return validate_json(req.errors)
        # 2.构建OpenAI客户端，将OpenAI的响应返回给前端
        client = OpenAI(
            api_key=config("ZHIPU_API_KEY"), base_url=config("ZHIPU_API_URL")
        )
        # 3.得到响应
        completion = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {"role": "system", "concent": "你是一个python无敌工程师，精通python。"},
                {"role": "user", "content": req.query.data},
            ],
        )

        content = completion.choices[0].message.content
        return success_json({"content": content})
