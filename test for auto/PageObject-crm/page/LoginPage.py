#coding:utf-8
from BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
class LoginPage(BasePage):
    username_loc = (By.NAME,'account')
    password_loc = (By.NAME,'password')
    submit_loc = (By.CLASS_NAME,'login-action')

    #输入用户名
    def input_username(self,username):
        self.find_element(*self.username_loc).clear()
        time.sleep(1)
        self.find_element(*self.username_loc).send_keys(username)

    #输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
        self.find_element(*self.password_loc).send_keys(Keys.TAB)

    #点击登录按钮
    def click_submit_button(self):
        self.find_element(*self.submit_loc).click()

    #登录函数
    def login_action(self,username,password):
        self.open()
        self.input_username(username)
        #time.sleep(1)
        self.input_password(password)
        self.click_submit_button()


