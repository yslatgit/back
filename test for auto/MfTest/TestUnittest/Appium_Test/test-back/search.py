#coding:utf-8
from appium import webdriver
import time

#配置信息
desired_caps = {
    'platformName':'Android',
    'deviceName':'45c44733',
    'platformVersion':'6.0.1',
    #'appPackage':'com.taobao.taobao',
    'appPackage':'com.mf.mfhr',
    #'appActivity':'com.taobao.tao.welcome.Welcome'
    'appActivity':'com.mf.mfhr.ui.activity.SplashActivity',
    'unicodeKeyboard':'True',
    'resetKeyboard':'True'

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(2)
print "1"
driver.find_element_by_id("com.mf.mfhr:id/et_login_phone").clear()
driver.find_element_by_id("com.mf.mfhr:id/et_login_phone").send_keys('18153529186')
driver.find_element_by_id("com.mf.mfhr:id/et_login_sms_code").send_keys('0000')
driver.find_element_by_id("com.mf.mfhr:id/fl_login_submit").click()
time.sleep(5)
driver.find_element_by_id("com.mf.mfhr:id/tv_search").click()
driver.find_element_by_id("com.mf.mfhr:id/et_search_content").send_keys(u"小程序")



