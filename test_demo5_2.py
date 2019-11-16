#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
url = "http://115.28.108.130/control.html"
# driver.get(url)
# driver.implicitly_wait(20)隐式等待
# wait = WebDriverWait(driver, 10, 0.5).until(
# lambda driver:driver.find_element_by_xpath('//*[text()="王五"]/../td[4]/a'))  # 显示等待
# wait.click()
# document.getElementById("ro").removeAttribute("readonly") 移除属性
# document.querySelector("#ro").removeAttribute("readonly") CSS移除属性
# document.getElementById("ro").setAttribute("style","border: 2px solid red");
# document.documentElement.scrollTop=100; 向下拖动100像素
# document.documentElement.scrollHeight 获取页面高度

def keys():
    a = driver.find_element_by_css_selector('.stuname')
    a.send_keys("博客园博客")
    a.send_keys(Keys.BACK_SPACE)
    a.send_keys(Keys.BACK_SPACE)
    sleep(1)
    a.send_keys(Keys.CONTROL, 'a')
    sleep(1)
    a.send_keys(Keys.CONTROL, 'c')
    sleep(1)
    a.click()
    a.send_keys(Keys.CONTROL, 'v')


def actions():
    btn = driver.find_element_by_css_selector('.dropdown>input')
    ActionChains(driver).move_to_element(btn).perform()
    driver.find_element_by_link_text("163").click()


# actions()


def actions2():
    url = "https://www.baidu.com"
    driver.get(url)
    btn = driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(btn).perform()
    driver.find_element_by_link_text("高级搜索").click()
    sleep(2)
    driver.find_element_by_id("adv_keyword").send_keys("千与千寻")
    sleep(1)
    driver.find_element_by_css_selector("input[value=高级搜索]").click()
    window = driver.window_handles
    driver.switch_to.window(window[1])
    sleep(2)
    print(driver.title)

# actions2()


def wait1():
    driver.get("http://115.28.108.130/control.html")
    wait = WebDriverWait(driver, 10, 0.5).until(
        lambda driver: driver.find_element_by_xpath('//*[text()="王五"]/../td[4]/a'))
    wait.click()


# wait1()


def javascript():
    driver.get(url)
    ro = driver.find_element_by_css_selector("#ro")
    js = 'document.getElementById("ro").removeAttribute("readonly")'
    driver.execute_script(js)
    ro.clear()
    ro.send_keys("123123")


# javascript()


def js2():
    driver.get("http://115.28.108.130/date.html")
    sleep(5)
    dp = driver.find_element_by_css_selector("input[name=act_start_time]")
    dp2 = driver.find_element_by_css_selector("input[name=act_stop_time]")
    js2 = '''
    document.querySelector("input[name=act_start_time]").removeAttribute("readonly");
    document.querySelector("input[name=act_stop_time]").removeAttribute("readonly");
    '''
    driver.execute_script(js2)
    sleep(2)
    dp.send_keys("2019-09-08 00:00")
    dp2.send_keys("2019-09-10 00:00")
    sleep(1)
    driver.find_element_by_xpath('//button[text()="确定"]').click()


js2()
















