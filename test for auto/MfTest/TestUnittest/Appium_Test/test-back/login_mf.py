#coding:utf-8
from driver import driver
from selenium.common.exceptions import NoSuchElementException
import time

#用下面函数确定是否已经登录
def check_canceBtn():
    print u"开始判断"
    try:
        canceBtn = driver.find_element_by_id("com.mf.mfhr:id/tv_city")
    except NoSuchElementException:
        print "no canceBtn"

        driver.find_element_by_id("com.mf.mfhr:id/et_login_phone").clear()
        time.sleep(1)

        #id定位
        driver.find_element_by_id("com.mf.mfhr:id/et_login_phone").send_keys('18153529186')

        #相对定位
        # root = driver.find_elements_by_class_name('android.widget.FrameLayout')[0]
        # root.find_element_by_class_name('android.widget.EditText').send_keys('18153529186')

        #xpath定位--一直失败

        # driver.find_element_by_xpath('//TextInputLayout[@Text="手机号"]').send_keys('18153529186')
        driver.find_element_by_id("com.mf.mfhr:id/et_login_sms_code").send_keys('0000')
        time.sleep(1)
        driver.find_element_by_id("com.mf.mfhr:id/fl_login_submit").click()
        print u"登录--"
    else:
        print u"已登录"
if __name__ == '__main__':

    check_canceBtn()
