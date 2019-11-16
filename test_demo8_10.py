#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import requests
import yaml


# @pytest.fixture()
# def test_add1(data):
#     print(data)
# fixture无法当作用例执行，下面用例无法获取数据
# -m "标签名" 根据标签筛选执行case
# -k case名 根据case名筛选case

f = open('data2.yaml')
data = yaml.safe_load(f)
# print(data)
data2 = list(data.values())
print(data2)


# 只有一组数据不可用？
@pytest.mark.parametrize('a, b, sum', data2)
def test_add3(a, b, sum):
    res = requests.get(f'http://115.28.108.130:5000/add/?a={a}&b={b}')
    print(f'{a} + {b} = {sum}')
    assert res.text == f'{sum}'


@pytest.mark.demo
def test_add(data):
    print(data)


@pytest.mark.demo
def test_add2(data):
    print(data)


if __name__ == '__main__':
    pytest.main(['test_demo8_10.py', '-vs', '-k', "test_add2"])



