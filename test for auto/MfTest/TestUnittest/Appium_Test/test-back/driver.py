#coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tomorrow import threads
import threading
import os
import time
def app():
    os.system('adb install C:\Users\Administrator\Desktop\mfhr_3_6_0824_1714.apk')
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '45c44733'
#desired_caps['udid'] = 'NX529J'
# desired_caps['app'] = r'D:\Appium\Appium\node_modules\appium\mfhr_3_6_0824_1714.apk'
desired_caps['platforVersion'] = '6.0.1'
desired_caps['appPackage'] = 'com.mf.mfhr'
desired_caps['appActivity'] = 'com.mf.mfhr.ui.activity.SplashActivity'
desired_caps['noReset'] = 'False'
desired_caps['resetKeyboard'] = 'True'
desired_caps['automationName'] = 'Uiautomator2'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
def lanch_app():
    print "启动魔方APP"
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver
def ask_permission(driver):
    print "点击允许"
    loc = ("xpath","//*[@text='允许']")
    try:
        e = WebDriverWait(driver,2,0.5).until(EC.presence_of_element_located(loc))
        e.click()
    except:
        pass



def ask_pop_window(driver):
    loc = ("xpath","//*[@text='同意']")
    try:
        e = WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located(loc))
        e.click()
    except:
        pass

"""
if __name__ == '__main__':
    安装APP方法实践
    try:
        app()
    except Exception:
        print "已安装"
    finally:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        ask_permission()
"""


"""
#截屏
driver.save_screenshot("login.png")
driver.get_screenshot_as_file('./login1.png')
"""
# def double(fun):
#     def inner(a):
#         print "123"
#         fun(a)
#         fun(a)
#     return inner
#





#
# print u"首页面"
# swipe_left_1(1000)
# print u"第二页"
# # time.sleep(3)
# # swipe_left_1(1000)
# # print "end"
# driver.find_element_by_id('com.mf.mfhr:id/sdv_item_guide').click()

