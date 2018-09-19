#coding:utf-8
from login_mf import *
from function.ToolClass import *
def choice_job():
    #登录
    check_canceBtn()
    #获得职位裂表
    job_list = driver.find_elements_by_id('com.mf.mfhr:id/recyclerView_o2o_item_ll')
    #选择第一个职位
    job_list[0].click()
    time.sleep(2)
    swipe_down()
    driver.find_element_by_xpath("//*[@text='查看路线']").click()
    zoom_zdy()
    pinch_zdy()

if __name__ == '__main__':
    choice_job()