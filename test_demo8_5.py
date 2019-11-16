#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pytest


# @pytest.fixture(scope='function', autouse=True)
# def my():
#     print("启动浏览器")
#     driver = webdriver.Chrome()
#     yield driver
#     print("退出浏览器")
#     driver.quit()


# @pytest.mark.usefixture('my')
# def my():
#     print("启动浏览器")
#     driver = webdriver.Chrome()
#     yield driver
#     print("退出浏览器")
#     driver.quit()

@pytest.fixture
def driver():
    print("启动浏览器")
    driver = webdriver.Chrome()
    yield driver
    print("退出浏览器")
    driver.quit()


@pytest.fixture
def login(driver):
    print("登录")
    driver.get('http://qaschool.cn:8000/admin/')
    driver.find_element_by_id('id_username').send_keys('hanzhichao')
    driver.find_element_by_id('id_password').send_keys('hanzhichao123')
    driver.find_element_by_xpath('//input[@type="submit"]').click()


class TestCourse(object):
    def test1(self, login, driver):
        driver.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[1]/a').click()
        driver.find_element_by_xpath('//*[@id="id_title"]').send_keys("PYTHON")
        sleep(2)
        driver.find_element_by_css_selector('input[type=submit]:nth-child(2)').click()
        rusult = driver.find_element_by_css_selector('#subject_form > div > fieldset > div.fo'
                                                          'rm-row.errors.field-slug > ul > li').text
        print("测试结果1：%s" % rusult)
        assert "具有 链接 的 Subject 已存在。" == rusult

    def test2(self, login, driver):
        driver.find_element_by_link_text('Subjects').click()
        result = driver.find_element_by_link_text('PYTHON').text
        print("测试结果：%s" % result)
        assert "PYTHON" == result


if __name__ == '__main__':
    pytest.main(['test_demo8_5.py', '-vs'])
















