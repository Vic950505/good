#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from time import sleep
@pytest.fixture()
def driver():
    print("启动浏览器")
    driver = webdriver.Chrome()
    yield driver
    print("关闭浏览器")
    driver.quit()


@pytest.fixture()
def url(driver):
    driver.get("https://www.baidu.com/")
    driver.maximize_window()


@pytest.fixture()
def url2(driver):
    driver.get("https://www.163.com/")
    driver.maximize_window()


class TestFunc(object):
    def test1(self, driver, url):
        sleep(2)
        driver.find_element_by_id("kw").send_keys('hello world')
        sleep(2)
        # 截图
        try:
            driver.save_screenshot('123123.png')
            print("截图成功")
        except:
            print("截图失败")
        assert "hello world_百度搜索" == driver.title

    def test2(self, driver, url2):
        sleep(2)
        driver.find_element_by_css_selector("#js_index2017_wrap > div:nth-child(2) > div.ne_area.ne_index_area >"
                                            " div.cm_area.ns_area_top > div.bd > ul > li:nth-child(1) > a:nth-child(2)")\
            .click()
        assert "网易" == driver.title


if __name__ == '__main__':
    pytest.main(['test_demo8_6.py', '-vs'])










