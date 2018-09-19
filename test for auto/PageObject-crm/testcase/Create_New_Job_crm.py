#coding:utf-8
from page.Create_New_Job import Create_New_Job
from page.LoginPage import LoginPage
from selenium import webdriver
import unittest
import time

class Create_New_Job_crm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_new_job(self):
        Lo = LoginPage(self.driver)
        Lo.login_action("yangsonglin@mofanghr.com","1234")

        Cnj = Create_New_Job(self.driver)
        Cnj.click_list_button()
        Cnj.switch_to_new_window()
        Cnj.click_customer_management_3_button()
        Cnj.switch_frame()
        Cnj.choice_company()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()