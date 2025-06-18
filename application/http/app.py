# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/11 16:23
@Author : qin863
@File   : application.py
"""
import dotenv
from flask_migrate import Migrate
from injector import Injector

from application.http.module import ExtensionModule
from config import Config
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy


# 加载环境变量
dotenv.load_dotenv()
# 创建配置对象
conf = Config()


# 创建一个注入器，并传入一个扩展模块
injector = Injector([ExtensionModule])

app = Http(
    __name__,
    conf=conf,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router),
)

if __name__ == "__main__":
    app.run(debug=True)
