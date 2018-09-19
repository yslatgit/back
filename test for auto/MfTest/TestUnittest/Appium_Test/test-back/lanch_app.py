#coding:utf-8
from appium import webdriver
import time
desired_caps = {
    'platformName':'Android',
    'deviceName':'NX529J',
    'platformVersion':'5.1.1',
    #'appPackage':'com.taobao.taobao',
    'appPackage':'com.mf.mfhr',
    #'appActivity':'com.taobao.tao.welcome.Welcome'
    'appActivity':'com.mf.mfhr.ui.activity.SplashActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

def double(fun):
    def inner(a):
        print "123"
        fun(a)
        fun(a)
    return inner

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)
@double
def swipe_left(t):
    time.sleep(10)
    screen = get_size()
    print screen
    print "1"
    time.sleep(10)
    driver.swipe(screen[0]*0.75,screen[1]*0.5,screen[0]*0.05,screen[1]*0.5,t)
    print "2"


