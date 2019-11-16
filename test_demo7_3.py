#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep

caps = {
    "platformName": "Android",
    "platformVersion": 9,
    "deviceName": "69db3e32",
    "appPackage": "com.example.testapp",
    "appActivity": "com.example.testapp.MainActivity",
    "noReset": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.find_element_by_id("com.example.testapp:id/urlField").send_keys("http://m.baidu.com")
driver.find_element_by_id("com.example.testapp:id/goButton").click()

sleep(3)
print("所有环境：%s" % driver.contexts)
print("当前环境：%s" % driver.context)

driver.switch_to.context('WEBVIEW_com.example.testapp')

print("切换后环境：%s" % driver.context)

driver.find_element_by_id("index-kw").send_keys("Appium")
driver.find_element_by_id("index-bn").click()

driver.switch_to.context('NATIVE_APP')




