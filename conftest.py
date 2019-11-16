#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml


# def pytest_addoption(parser):
#     parser.addoption("--data", action="store", help="data file")
#
#
# @pytest.fixture
# def data(request):
#     file_path = request.config.getoption("--data")  # 获取--data参数传的文件路径
#     with open(file_path) as f:   # 加载所有数据
#         all_data = yaml.safe_load(f)
#
#     test_case_name = request.function.__name__  # 获取调用的data这个fixture方法的测试方法名称
#
#     return all_data.get(test_case_name)   # 只返回指定用例的数据
@pytest.fixture()
def data(request):
    file = open('data2.yaml')
    data = yaml.safe_load(file)
    case_name = request.function.__name__
    return data.get(case_name)