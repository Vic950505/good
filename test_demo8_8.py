#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import requests
import yaml


class TestDemo(object):
    def test_a(self, data):  # 所有用例要带上data这个fixture参数
        print(data)

    def test_b(self, data):
        print(data)


if __name__ == '__main__':
    pytest.main(['test_demo8_8.py', '-vs', '--data=data.yaml'])



