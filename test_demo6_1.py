#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep


# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'
# desired_caps['deviceName'] = '127.0.0.1:62001'
# desired_caps['appPackage'] = 'com.lqr.wechat'
# desired_caps['appActivity'] = 'com.lqr.wechat.ui.activity.SplashActivity'
# desired_caps['app'] = '/Users/wanghao/Downloads/app-debug(1).apk'
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(20)
# el1 = driver.find_element_by_id("com.lqr.wechat:id/btnLogin")
# el1.click()
# el1 = driver.find_element_by_id("com.lqr.wechat:id/etPhone")
# el1.send_keys("18911946041")
# el2 = driver.find_element_by_id("com.lqr.wechat:id/etPwd")
# el2.send_keys("123456")
# el3 = driver.find_element_by_id("com.lqr.wechat:id/btnLogin")
# el3.click()


def android_ui():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.android.androidui'
    desired_caps['appActivity'] = 'com.android.androidui.MainActivity'
    desired_caps['app'] = '/Users/wanghao/Downloads/AndroidUI.apk'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    el1 = driver.find_element_by_id("com.android.androidui:id/buttonAlert")
    el1.click()
    el2 = driver.find_element_by_id("android:id/button1")
    el2.click()


# android_ui()


def android_ui2():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = 9
    desired_caps['deviceName'] = '69db3e32'
    desired_caps['appPackage'] = 'com.lqr.wechat'
    desired_caps['appActivity'] = 'com.lqr.wechat.ui.activity.SplashActivity'
    desired_caps['app'] = '/Users/wanghao/Downloads/app-debug(1).apk'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(4)
    driver.find_element_by_id('com.lqr.wechat:id/etPhone').send_keys('18010181267')
    driver.find_element_by_id('com.lqr.wechat:id/etPwd').send_keys('12332432')
    driver.find_element_by_id('com.lqr.wechat:id/btnLogin').click()
    result = driver.find_elements_by_xpath("//*[@text='登录失败1001']")
    if result:
        print("Yes")
        print(result[0])
    else:
        print('no')
    # driver.tap([(244, 2028)])
    # 页面截图
    # driver.get_screenshot_as_file("123123.png")
    # driver.save_screenshot()
    # driver.tap([(190, 2020)])


android_ui2()


def android_ui3():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = 9
    desired_caps['deviceName'] = '69db3e32'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = 'com.android.settings.MainSettings'
    # desired_caps['app'] = '/Users/wanghao/Downloads/app-debug(1).apk'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(3)
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    print(width, height)
    x1 = x2 = width / 2
    y1 = height * 0.95
    y2 = height * 0.1
    driver.swipe(x1, y1, x2, y2, duration=2000)
    sleep(3)
    # for i in range(5):
    #     result = driver.find_elements_by_android_uiautomator('new UiSelector().text("更多设置")')
    #     if result:
    #         break
    #     driver.flick(x1, y1, x2, y2)
    # if result:
    #     result[0].click()
    result = driver.find_elements_by_android_uiautomator('new UiSelector().text("更多设置")')
    try:
        result[0].click()
    except:
        driver.flick(x1, y1, x2, y2)
        pass
    result = driver.find_elements_by_android_uiautomator('new UiSelector().text("更多设置")')
    result[0].click()


# android_ui3()

