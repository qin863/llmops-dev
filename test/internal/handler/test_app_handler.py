# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/14 10:40
@Author : qin863
@File   : test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:

    @pytest.mark.parametrize("query", ["你好,你是什么模型"])
    def test_completion(self, query, client):
        resp = client.post("/v1/completion", json={"query": query})
        assert resp.status_code == 200
        print(resp.json)
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
