#coding:utf-8
from page.LoginPage import LoginPage
from selenium import webdriver
import unittest
import time
import ddt

testdata = [{"username":"zhaoxiaowei@mofanghr.com","password":"1234","assert_text":u"魔方微猎客户管理系统"}]
            #{"username":"yuanqing@mofanghr.com","password": "123","assert_text":u"魔方微猎综合管理平台"},]

@ddt.ddt
class Login_crm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    @ddt.data(*testdata)
    def test_login_crm(self,data):
        Lo = LoginPage(self.driver)
        Lo.login_action(data['username'],data['password'])
        time.sleep(2)
        self.assertEqual(data['assert_text'],self.driver.title)
        # text = self.driver.page_source
        # print text

    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()