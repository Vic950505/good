#!/usr/bin/env python
# -*- coding:utf-8 -*-
# test_fixture.py
import pytest
@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('\n-----------------')
    print('我是module fixture')
    print('-----------------')


@pytest.fixture(scope='class')
def class_fixture():
    print('\n-----------------')
    print('我是class fixture')
    print('-------------------')


@pytest.fixture(scope='function', autouse=True)
def func_fixture():
    print('\n-----------------')
    print('我是function fixture')
    print('-------------------')


@pytest.fixture()
def func_fixture2():
    print('\n-----------------')
    print('我是function fixture2')
    yield True
    print('-------------------')


def test_1(func_fixture2):
    print('\n 我是test1')
    print("我调用了：%s" % func_fixture2)


@pytest.mark.usefixtures('class_fixture')
class TestFixture1(object):
    def test_2(self):
        print('\n我是class1里面的test2')

    def test_3(self):
        print('\n我是class1里面的test3')


@pytest.mark.usefixtures('class_fixture')
class TestFixture2(object):
    def test_4(self):
        print('\n我是class2里面的test4')

    def test_5(self):
        print('\n我是class2里面的test5')


if __name__ == '__main__':
    pytest.main(['-vs', 'test_demo8_7.py'])













