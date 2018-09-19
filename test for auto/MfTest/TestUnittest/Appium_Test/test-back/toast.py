#coding=utf-8
from driver import *

"""
def is_toast_exist():
    try:
        toast_loc = ("xpath", "//*[@text='请输入手机号']")
        WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False
print is_toast_exist()
"""
try:
    driver.find_element_by_id('com.mf.mfhr:id/tv_login_voice_code').click()
    toast_loc = ("xpath", "//*[@text='请输入手机号']")
    WebDriverWait(driver, 1, 0.2).until(EC.presence_of_element_located(toast_loc))
    print "1"
except:
    print "2"