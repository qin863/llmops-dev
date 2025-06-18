# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/14 10:58
@Author : qin863
@File   : conftest.py
"""
import pytest


@pytest.fixture
def client():
    from application.http.app import app

    """获取flask应用的测试应用，并返回"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
