# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/14 11:06
@Author : qin863
@File   : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""

    # 必填长度为20000
    query = StringField(
        "query",
        validators=[
            DataRequired(message="用户的提问是必填"),
            Length(max=2000, message="最大提问长度为2000"),
        ],
    )
