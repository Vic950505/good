#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = 9
desired_caps['deviceName'] = '69db3e32'
desired_caps['appPackage'] = 'com.dianping.v1'
desired_caps['appActivity'] = 'com.dianping.main.guide.SplashScreenActivity'
desired_caps['app'] = '/Users/wanghao/Desktop/dazhongdianping_101911.apk'
desired_caps['noReset'] = True
desired_caps['autoLaunch'] = False
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)


def test_app():

    launch_app = driver.launch_app()
    if launch_app:
        return "启动成功"
    else:
        return "启动失败"
        pass


# test_app()


def inform():
    driver.open_notifications()
    sleep(2)
    driver.save_screenshot("123123.png")
    sleep(1)
    driver.press_keycode('4')


# inform()


def browser():
    try:
        driver.start_activity('com.android.browser', 'com.android.browser.BrowserActivity')
        print("成功")
    except:
        print("失败")
    a = driver.current_activity
    print(driver.network_connection)
    driver.start_activity('com.android.camera', 'com.android.camera.CameraPreferenceActivity')
    b = driver.current_activity
    if a == b:
        print("相同")
    else:
        print("不同")
        print(a, b)
    driver.save_screenshot("456456.png")


# browser()


def install():
    a = driver.is_app_installed("com.dianping.v1")
    if a:
        driver.remove_app("com.dianping.v1")
        print("正在卸载")
        sleep(5)
    else:
        print("未安装")
        driver.install_app('/Users/wanghao/Desktop/dazhongdianping_101911.apk')
        print("正在安装")
        b = driver.is_app_installed("com.dianping.v1")
        if b:
            print("安装成功")
        else:
            print("安装失败")


install()


