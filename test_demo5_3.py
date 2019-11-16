#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import re
driver = webdriver.Chrome()
driver.implicitly_wait(30)
# pytest test_demo-3-5.py --html=report4.html --self-contained-html


def login():
    url = "http://39.104.14.232/ecshop/wwwroot/user.php"
    driver.get(url)
    # sleep(2)
    driver.maximize_window()
    # sleep(2)
    driver.find_element_by_css_selector('input[id=username]').send_keys("admin")
    driver.find_element_by_css_selector('input[id=password]').send_keys("123456")
    driver.find_element_by_css_selector('input[name="submit"]').click()
    driver.find_element_by_link_text("首页").click()


# login()


def test_choice_goods():
    login()
    sleep(3)
    hot_btn = driver.find_element_by_xpath('//h3[text()="热销排行"]')
    ActionChains(driver).move_to_element(hot_btn).perform()
    iphone = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/li[2]/dl/dd[1]/a/img').click()
    sleep(3)
    window = driver.window_handles[1]
    driver.switch_to.window(window)
    sleep(4)
    join_car = driver.find_element_by_css_selector('#choose-btns > a.u-buy2').click()
    sleep(1)
    shopping_car = driver.find_element_by_css_selector('#mc-menu-hd').click()
    go_pay = driver.find_element_by_link_text("去结算").text
    assert "去结算" == go_pay


def test_shopping_adress():
    try:
        login()
    except:
        driver.get("http://39.104.14.232/ecshop/wwwroot/user.php")
    # sleep(3)
    driver.find_element_by_id("mc-menu-hd").click()
    # sleep(3)
    driver.find_element_by_link_text("去结算").click()
    sleep(3)
    driver.find_element_by_css_selector('div[class="address_jm_add"]').click()
    # sleep(1)
    driver.find_element_by_css_selector("input[name='consignee']").send_keys("Vic")
    driver.find_element_by_css_selector('select[id="selProvinces"]').click()
    driver.find_element_by_xpath('//option[text()="辽宁"]').click()
    driver.find_element_by_css_selector('select[name="city"]').click()
    driver.find_element_by_xpath('//option[text()="丹东"]').click()
    driver.find_element_by_css_selector('select[name="district"]').click()
    driver.find_element_by_xpath('//option[text()="振安区"]').click()
    driver.find_element_by_css_selector('input[name="address"]').send_keys("鸭绿江上")
    driver.find_element_by_css_selector('input[name="mobile"]').send_keys("18911998899")
    driver.find_element_by_css_selector('input[value=" 确定 "]').click()
    # sleep(2)
    phone_num = driver.find_element_by_xpath("//li[2]//td[contains(text(),'Vic')]").text
    get_phone_num = re.findall('\\d{10,11}', phone_num)
    for i in get_phone_num:
        print(i)
    assert "18911998899" == i




