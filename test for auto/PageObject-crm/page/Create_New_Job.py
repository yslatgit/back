#coding:utf-8
from BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class Create_New_Job(BasePage):
    list_loc = (By.XPATH,'html/body/div[1]/div[2]/ul/li[2]/a')
    #职位管理定位器
    position_management_loc = (By.XPATH,".//*[@id='id-4']/div/span")
    #职位管理--->职位列表定位器
    job_list_loc = (By.XPATH,".//*[@id='id-4']/ul/li[1]/span")
    #客户管理定位器
    customer_management_loc = (By.XPATH,".//*[@id='id-2']/div/span")
    #客户管理--->我的客户
    customer_management_3_loc = (By.XPATH,".//*[@id='id-2']/ul/li[3]/span")
    #客户管理--->我的客户--->公司列表
    customer_management_3_company_loc = (By.PARTIAL_LINK_TEXT,u'河南盛世伟业')
    #公司列表页的iframe
    company_list_iframe_loc = (By.TAG_NAME,'iframe')



    def click_list_button(self):
        """打开CRM管理系统"""
        self.find_element(*self.list_loc).click()
        time.sleep(1)

    def click_job_list_button(self):
        """打开职位列表"""
        self.find_element(*self.position_management_loc).click()
        self.find_element(*self.job_list_loc).click()
        time.sleep(1)

    def click_customer_management_3_button(self):
        """打开我的客户页面"""
        self.find_element(*self.customer_management_loc).click()
        self.find_element(*self.customer_management_3_loc).click()
        time.sleep(1)

    def switch_frame(self):
        """切换iframe"""
        frame = self.find_elements(*self.company_list_iframe_loc)
        print frame
        self.switch_frame(frame)


    def choice_company(self):
        """打开某公司页面"""
        self.find_element(*self.customer_management_3_company_loc).click()


