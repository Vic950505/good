#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()


def login():
    url = "http://39.104.14.232/ecshop/wwwroot/admin/privilege.php?act=login"
    driver.get(url)
    driver.maximize_window()
    sleep(2)
    user_name = driver.find_element_by_xpath("/html/body/div[1]/form[@name='theForm']/table[@class='login_dl']//td[@class='dl']/table//input[@name='username']").send_keys('admin')
    sleep(1)
    pass_word = driver.find_element_by_xpath("/html/body/div[1]/form[@name='theForm']/table[@class='login_dl']//td[@class='dl']/table//input[@name='password']").send_keys(123456)
    sleep(1)
    btn_login = driver.find_element_by_xpath("/html/body//form[@name='theForm']/table[@class='login_dl']//td[@class='dl']/table/tbody/tr[4]/td/input[@value='登 录']").click()
    sleep(3)
    # driver.save_screenshot("123.png")
    # driver.quit()


# login()


def test_add_classification():
    login()
    sleep(3)
    frame1 = driver.find_element_by_id("menu-frame")
    driver.switch_to.frame(frame1)
    sleep(1)
    goods_contal = driver.find_element_by_xpath("//ul[@id='menu-ul']/li/ul/li[1]/a[@href='javascript:void(0);']").click()
    sleep(1)
    goods_clsss = driver.find_element_by_link_text("商品分类")
    goods_clsss.click()
    sleep(3)
    driver.switch_to.default_content()
    frame2 = driver.find_element_by_xpath('//*[@id="main-frame"]')
    driver.switch_to.frame(frame2)
    sleep(1)
    add_class = driver.find_element_by_link_text("添加分类").click()
    sleep(3)
    class_name = driver.find_element_by_xpath("/html//table[@id='general-table']//textarea[@name='cat_name']").send_keys("阿浩的商品1")
    catlog_name = driver.find_element_by_xpath("/html//table[@id='general-table']//input[@name='path_name']").send_keys("wanghao")
    superior_name = driver.find_element_by_xpath("/html//table[@id='general-table']//select[@name='parent_id']").click()
    sleep(1)
    superior_choose = driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[3]/td[2]/select/option[2]').click()
    sleep(2)
    num_uint = driver.find_element_by_xpath("//tr[@id='measure_unit']//input[@name='measure_unit']").send_keys("件")
    sort = driver.find_element_by_xpath("/html//table[@id='general-table']//input[@name='sort_order']")
    sort.clear()
    sort.send_keys("999")
    sleep(2)
    boutique = driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[8]/td[2]/input[1]').click()
    nature_screen = driver.find_element_by_xpath("/html//table[@id='tbody-attr']//td/select[1]").click()
    sleep(1)
    big_baby = driver.find_element_by_xpath('//*[@id="tbody-attr"]/tbody/tr/td/select[1]/option[9]').click()
    sleep(1)
    price_num = driver.find_element_by_xpath("/html//table[@id='general-table']//input[@name='grade']")
    price_num.clear()
    price_num.send_keys("3")
    keyword = driver.find_element_by_xpath("/html//table[@id='general-table']//input[@name='keywords']").send_keys("哈哈哈")
    describe = driver.find_element_by_xpath("/html//table[@id='general-table']//textarea[@name='cat_desc']").send_keys("我是一个大好人，哈哈哈哈哈")
    btn_show = driver.find_element_by_xpath("/html//table[@id='general-table']/tbody/tr[14]/td[2]/input[1]").click()
    btn_ensure = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[1]").click()
    sleep(4)
    driver.switch_to.default_content()
    driver.switch_to.frame(frame1)
    goods_clsss.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.switch_to.frame(frame2)
    sleep(1)
    search_class_name = driver.find_element_by_xpath("/html//form[@name='searchForm']/input[@name='cat_name']").send_keys("阿浩")
    sleep(1)
    btn_search = driver.find_element_by_xpath("/html//form[@name='searchForm']/input[@value=' 搜索 ']").click()
    sleep(1)
    value = driver.find_element_by_xpath("//table[@id='list-table']//tr[@class='1']/td[@class='first-cell']//a[@href='goods.php?act=list&cat_id=778&supp=-1']").text
    # driver.quit()
    assert "阿浩的商品1" == value



