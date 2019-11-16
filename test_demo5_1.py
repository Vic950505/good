#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep


def find_element_by_value(driver,value):
    # css_selector = f'[value="{value}"]'
    css_selector = '[value="%s"]' % value
    return driver.find_element_by_css_selector(css_selector)


driver = webdriver.Chrome()
url = "http://115.28.108.130/control.html"
driver.get(url)
find_element_by_value(driver,"alert").click()
# a = driver.find_elements_by_xpath('/html/body/div[4]')
# b = driver.find_element_by_xpath('//td[text()="李四"]/../td[4]/a').click()
# sleep(1)
# c = driver.switch_to.alert.accept()



