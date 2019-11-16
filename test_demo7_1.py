#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class Ui(object):
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = 9
        self.desired_caps['deviceName'] = '69db3e32'
        self.desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        self.desired_caps['appActivity'] = 'com.samsung.ui.FlashActivity'
        self.desired_caps['app'] = '/Users/wanghao/Downloads/shoushimimasuo.apk'
        self.desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def press_one(self):
        self.driver.find_element_by_id('cn.kmob.screenfingermovelock:id/lockerCheckBox').click()
        TouchAction(self.driver).press(x=185, y=389).move_to(x=185, y=737).wait(300).move_to(x=185, y=1075).wait(300).move_to(x=547, y=728).wait(300).move_to(x=904, y=366).release().perform()
        self.driver.save_screenshot("123123.png")


# demo = Ui()
# demo.press_one()


class Ui2(object):
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = 9
        self.desired_caps['deviceName'] = '69db3e32'
        self.desired_caps['appPackage'] = 'com.lqr.wechat'
        self.desired_caps['appActivity'] = 'com.lqr.wechat.ui.activity.SplashActivity'
        self.desired_caps['app'] = '/Users/wanghao/Downloads/app-debug(1).apk'
        self.desired_caps['noReset'] = True
        self.desired_caps['automationName'] = 'uiautomator2'
        # self.desired_caps['browserName'] = 'chrome'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def toast(self):
        sleep(3)
        self.driver.implicitly_wait(20)
        sleep(4)
        self.driver.find_element_by_id('com.lqr.wechat:id/etPhone').send_keys('18010181267')
        self.driver.find_element_by_id('com.lqr.wechat:id/etPwd').send_keys('12332432')
        self.driver.find_element_by_id('com.lqr.wechat:id/btnLogin').click()
        result = self.driver.find_elements_by_xpath("//*[@text='登录失败1001']")
        if result:
            print("Yes")
            print(result[0])
        else:
            print('no')


# demo2 = Ui2()
# demo2.toast()










