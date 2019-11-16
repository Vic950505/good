#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml
import requests

f = open('data2.yaml')
data = yaml.safe_load(f)
print(data)
# print(data[len(data) - 1]['assert'])

# print(a['request'])
# for i in data:
#     for key, value in i.items():
#         print(key, value)


# @pytest.fixture()
# def data(request):
#     file = open('data2.yaml')
#     data = yaml.safe_load(file)
#     case_name = request.function.__name__
#     return data.get(case_name)


# def test_add1(data):
#     print('执行test_add1')
#     print(data)
#
#
# def test_add2(data):
#     print('执行test_add2')
#     print(data)


# if __name__ == '__main__':
#     pytest.main(['test_demo8_9.py', '-vs'])
