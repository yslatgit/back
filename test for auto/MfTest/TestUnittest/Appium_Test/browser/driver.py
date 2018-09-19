#coding:utf-8

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '45c44733'
#desired_caps['udid'] = 'NX529J'  苹果手机要填
# desired_caps['app'] = r'D:\Appium\Appium\node_modules\appium\mfhr_3_6_0824_1714.apk'
desired_caps['platforVersion'] = '6.0.1'
desired_caps['appPackage'] = 'com.mf.mfhr'
desired_caps['appActivity'] = 'com.mf.mfhr.ui.activity.SplashActivity'
desired_caps['noReset'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['automationName'] = 'Uiautomator2'
desired_caps['unicodeKeyboard'] = 'True'



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

