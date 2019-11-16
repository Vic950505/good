#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import pytest
from selenium import webdriver
from time import sleep
# pytest test_demo8_1.py -v详细模式 -q安静模式  -s输出打印信息
# pytest test_demo-3-5.py --html=report4.html --self-contained-html 生成测试报告


def test1():
    print(1+1)
    assert 1+1 == 2


def test2():
    d = {"a": 1, "b": 2}
    print(d.get("a"))
    assert d.get("a") == 1
    assert d["a"] == True


def test_add():
    url = "http://115.28.108.130:5000/add/"
    param = {"a": 2, "b": 2}
    reponse = requests.get(url=url, params=param)
    a = int(reponse.text)
    b = int(reponse.status_code)
    print("运算结果：%s" % a)
    print("状态码：%s" % b)
    assert 4 == a
    assert 200 == b


def test_add2():
    url = "http://115.28.108.130:5000/add/"
    param = {"a": 2, "b": 2}
    reponse = requests.get(url=url, params=param)
    a = int(reponse.text)
    b = int(reponse.status_code)
    print("运算结果：%s" % a)
    print("状态码：%s" % b)
    assert 5 == a
    assert 200 == b


def test_add3():
    url = "http://115.28.108.130:5000/add/"
    param = {"a": -2, "b": 2}
    reponse = requests.get(url=url, params=param)
    a = int(reponse.text)
    b = int(reponse.status_code)
    print("运算结果：%s" % a)
    print("状态码：%s" % b)
    assert 0 == a
    assert 200 == b


# debug = TestAdd()
# debug.login()
# debug.test1()
# debug.test2()


# 执行脚本
if __name__ == '__main__':
    pytest.main(['test_demo8_1.py', '-vs'])






















