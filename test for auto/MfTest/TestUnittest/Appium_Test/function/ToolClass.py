#coding=utf-8
from browser.driver import driver
import time,os
from Config import *
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

def insatll():
     install()

def get_window_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y

def swipe_left():
    screen = get_window_size()
    x1 = int(screen[0] * 0.8)
    x2 = int(screen[0] * 0.1)
    y1 = int(screen[1] * 0.5)
    driver.swipe(x1, y1, x2, y1, 1000)

def swipe_height(a,b1,b2):
    screen = get_window_size()
    x1 = int(screen[0] * a)
    y1 = int(screen[1] * b1)
    y2 = int(screen[1] * b2)
    driver.swipe(x1,y1,x1,y2,1000)

def zoom_zdy():
    screen = get_window_size()
    print screen
    x = screen[0]
    y = screen[1]
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)
    action1.press(x=x * 0.6,y=y *0.6).move_to(x=x *0.3,y=y *0.3).wait(1000).release()
    action2.press(x=x * 0.5,y=y *0.5).move_to(x=x *0.7,y=y *0.7).wait(1000).release()
    zoom_action.add(action1,action2)
    print u"页面放大操作--->"
    zoom_action.perform()

def pinch_zdy():
    screen = get_window_size()
    x = screen[0]
    y = screen[1]
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)
    action1.press(x=x * 0.1,y=y *0.1).move_to(x=x *0.7,y=y *0.7).wait(1000).release()
    action2.press(x=x * 0.9,y=y *0.9).move_to(x=x *0.4,y=y *0.4).wait(1000).release()
    pinch_action.add(action1,action2)
    print u"页面缩小操作--->"
    pinch_action.perform()


def skip_inerdict_page():
    allow_top()
    time.sleep(3)
    try:
        decision_element = driver.find_element_by_id("com.mf.mfhr:id/et_login_phone")
    except Exception:
        for i in range(2):
            print u"开始滑动 %s" % (i + 1)
            swipe_left()
            time.sleep(1)
        print u"滑动结束"
        driver.find_element_by_id('com.mf.mfhr:id/sdv_item_guide').click()
    else:
        print u"已经跳过滑动页"

def allow_top():
    try:
        decision_element = driver.find_element_by_xpath("//*[@text='允许']")
        decision_element.click()
    except Exception:
        print "不是第一次登录，不用勾选权限"


if __name__ == '__main__':
    install()