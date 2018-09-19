#coding:utf-8

from selenium.webdriver.common.by import By

from basepage.BasePage import BasePage
from function.ToolClass import *


class LoginPage(BasePage):

    userName_loc = (By.ID,'com.mf.mfhr:id/et_login_phone')
    password_loc = (By.ID,'com.mf.mfhr:id/et_login_sms_code')
    submit_loc = (By.ID,'com.mf.mfhr:id/fl_login_submit')

    def input_username(self,account):
        self.driver.find_element(*self.userName_loc).clear()
        self.driver.find_element(*self.userName_loc).send_keys(account)

    def input_password(self):
        self.driver.find_element(*self.password_loc).send_keys("0000")

    def click_login_action(self):
        self.driver.find_element(*self.submit_loc).click()

    def login_mf_app(self,account):
        skip_inerdict_page()
        self.input_username(account)
        self.input_password()
        self.click_login_action()