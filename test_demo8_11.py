#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import requests
import yaml
file = open('data2.yaml')
data = yaml.safe_load(file)
print(data)
@pytest.mark.parametrize('api', data)
def test_a(api):
    request = api.get('request')  # 请求数据
    print(api)
    res = requests.request(**request)
    print("请求数据", request)
    print("响应数据", res.status_code)
    ass = api.get('assert')
    print(ass)
    if type(ass) is list:
        for line in ass:
            assert line == res.status_code


if __name__ == '__main__':
    pytest.main(['test_demo8_11.py', '-vs'])




