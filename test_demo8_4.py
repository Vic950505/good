#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pytest


class TestAdd(object):

    def setup_method(self):
        self.driver = webdriver.Chrome()
        url = 'http://qaschool.cn:8000/admin/login/?next=/admin/'
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        print("方法准备准备")

    def teardown_method(self):
        self.driver.quit()
        print("方法拆卸")

    def login(self):
        sleep(2)
        self.driver.find_element_by_name('username').send_keys('hanzhichao')
        sleep(2)
        self.driver.find_element_by_name('password').send_keys('hanzhichao123')
        sleep(2)
        self.driver.find_element_by_css_selector('input[type=submit]').click()

    def test1(self):
        self.login()
        self.driver.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="id_title"]').send_keys("PYTHON")
        sleep(2)
        self.driver.find_element_by_css_selector('input[type=submit]:nth-child(2)').click()
        rusult = self.driver.find_element_by_css_selector('#subject_form > div > fieldset > div.fo'
                                                          'rm-row.errors.field-slug > ul > li').text
        print("测试结果1：%s" % rusult)
        assert "具有 链接 的 Subject 已存在。" == rusult

    def test2(self):
        self.login()
        self.driver.find_element_by_link_text('Subjects').click()
        result = self.driver.find_element_by_link_text('PYTHON').text
        print("测试结果：%s" % result)
        assert "PYTHON" == result


if __name__ == '__main__':
    pytest.main(['test_demo8_4.py::TestAdd', '-vs'])




