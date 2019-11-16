#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

# setup_method/teatdown_method 方法准备,类中执行n遍
# setup_class/teardown_class 类准备，类中执行一遍
# setup_function/teardown_function 函数准备,函数中执行n遍
# ：：类名 只执行这个测试类


def setup_module():
    print("模块准备")


def teardown_module():
    print("模块拆卸")


def setup_function():
    print("准备")


def teardown_function():
    print("拆卸")


def test1():
    print("test1")


def test2():
    print("test2")


def test3():
    print("test3")


if __name__ == '__main__':
    pytest.main(['test_demo8_3.py', '-vs'])


















