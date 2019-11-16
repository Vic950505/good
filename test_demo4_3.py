#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep


def test1():
    driver = webdriver.Chrome()
    driver.get("http://39.104.14.232/ecshop/wwwroot/admin/privilege.php?act=login")
    driver.maximize_window()
    sleep(3)


test1()


