#coding=utf-8
from login_mf import check_canceBtn,driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
check_canceBtn()
text=u'退出登录成功'
driver.find_element_by_id('com.mf.mfhr:id/ll_main_user').click()
driver.find_element_by_id('com.mf.mfhr:id/llSetting').click()
driver.find_element_by_id('com.mf.mfhr:id/tv_settings_logout').click()
#message='//*[@text=\'{}\']'.format(message)
#toast_element=WebDriverWait(driver,1,0.2).until(lambda x:x.find_element_by_xpath(message))

