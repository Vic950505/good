#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select


# driver.back()  #  后退
# driver.forward()  #  前进
# print(driver.title)  #  打印title
# print(driver.page_source)  # 打印页面元素
# driver.quit()
# driver.set_window_size(880,600)  #  设置尺寸
# driver.save_screenshot()  #  截图
# get_attribue('属性名')
# tag_name
# text
# is_displayed()  # 是否显示
# is_enabled()  # 是否可用，按钮
# is_selected()  # 是否已选择
# switch_to.parent_frame()
# switch_to.default_content()
# assert "***" in driver.title


def test1():
    driver = webdriver.Chrome()
    driver.get('http://115.28.108.130/control.html')
    driver.maximize_window()
    sleep(3)
    # driver.save_screenshot('search.png')
    driver.find_element_by_id('accountID').send_keys('张三')
    sleep(3)
    driver.find_element_by_id('passwordID').send_keys('123456')
    sleep(3)
    driver.find_element_by_partial_link_text('百度首页走起~').click()
    print(driver.title)
    sleep(3)
    driver.back()
    sleep(3)
    driver.find_element_by_id('check').send_keys("hello")
    driver.find_element_by_xpath('//body/div[3]/input').send_keys("张三")


def test2():
    driver = webdriver.Chrome()
    driver.get('http://115.28.108.130/control.html')
    driver.maximize_window()
    sleep(3)
    element1 = driver.find_element_by_xpath('//body/div[1]/form/div[3]')
    print(element1.text)
    sleep(3)
    elements1 = driver.find_elements_by_id('u')
    print(elements1)
    for elementc in elements1:
        elementc.click()
    sleep(3)
    driver.save_screenshot('qq.png')
    sleep(3)
    element2 = driver.find_elements_by_xpath("/html//select[@id='areaID']")
    if len(element2) > 0:
        print("True")
    else:
        print("False")


# test2()


def test3():
    driver = webdriver.Chrome()
    driver.get('http://115.28.108.130/control.html')
    driver.maximize_window()
    sleep(3)
    driver.find_element_by_xpath("/html//input[@id='accountID']").send_keys("张三")
    driver.find_element_by_xpath("/html//input[@id='passwordID']").send_keys("12345")
    sleep(1)
    driver.find_element_by_xpath("/html//input[@id='passwordID']").clear()
    sleep(1)
    driver.find_element_by_xpath("/html//input[@id='passwordID']").send_keys("111111")
    a = driver.find_element_by_xpath("/html//input[@id='accountID']").get_attribute("value")
    print(a)
    b = driver.find_element_by_xpath("//div[@id='firstdiv']/form/table/tbody/tr[8]/td/a[1]").get_attribute("href")
    print(b)


# test3()
def test4():
    driver = webdriver.Chrome()
    driver.get('http://115.28.108.130/control.html')
    driver.maximize_window()
    sleep(3)
    a = driver.find_element_by_xpath("/html//select[@id='areaID']")
    b = Select(a)
    b.select_by_index(1)
    sleep(2)
    b.select_by_value("2")
    sleep(2)
    b.select_by_visible_text("北京")


# test4()


def test5():
    driver = webdriver.Chrome()
    driver.get('http://115.28.108.130/control.html')
    driver.maximize_window()
    sleep(3)
    driver.find_elements_by_id('alert').click()
    sleep(3)
    driver.switch_to.alert.dismiss()  # 取消
    driver.switch_to.alert.accept()  # 同意
    sleep(3)
    driver.quit()


# test5()


def test6():
    driver = webdriver.Chrome()
    driver.get('http://bj.ganji.com/')
    driver.maximize_window()
    sleep(3)
    driver.find_element_by_link_text("租房").click()
    sleep(3)
    window = driver.window_handles
    driver.switch_to.window(window[1])
    print(driver.current_window_handle)
    driver.find_element_by_link_text("海淀").click()
    driver.find_element_by_link_text("2000-3000元").click()
    sleep(3)
    driver.save_screenshot('ganji.png')


# test6()


def test7():
    driver = webdriver.Chrome()
    driver.get('http://115.28.108.130/control.html')
    driver.maximize_window()
    sleep(3)
    iframe1 = driver.find_element_by_name("parent_frame")
    driver.switch_to.frame(iframe1)
    sleep(2)
    left = driver.find_element_by_name("left")
    driver.switch_to.frame(left)
    driver.find_element_by_link_text("链接1").click()
    sleep(2)
    driver.switch_to.parent_frame()
    right = driver.find_element_by_name("main")
    driver.switch_to.frame(right)
    a = driver.find_element_by_xpath("/html/body/h2").text
    print(a)


test7()










































