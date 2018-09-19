#coding:utf-8
from driver.Driver import get_driver
from BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import unittest
class TestPage(BasePage):
    option_loc = (By.LINK_TEXT,u"设置")
    input_loc = (By.ID,'kw')

    def mouse_hover_c(self):
        self.mouse_hover(*self.option_loc)
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver('cc',0)

    @unittest.skip(u"1<-->跳过前进后退页面")
    def test_back_or_forward(self):
        tp = TestPage(self.driver)
        tp.open_url("http://www.baidu.com")
        tp.open_url("http://www.hao123.com")
        tp.back()
        time.sleep(2)
        tp.forward()
        time.sleep(5)

    @unittest.skip(u"2<-->跳过鼠标悬停测试")
    def test_mouse_hover(self):
        tp = TestPage(self.driver)
        tp.open_url("http://www.baidu.com")
        tp.mouse_hover(*tp.option_loc)
        time.sleep(2)

    @unittest.skip(u"3<-->跳过鼠标右击测试")
    def test_mouse_context_click(self):
        tp = TestPage(self.driver)
        tp.open_url("http://www.baidu.com")
        tp.mouse_context_click(*tp.option_loc)
        time.sleep(2)


    def test_keyboard(self):
        tp = TestPage(self.driver)
        tp.open_url("http://www.baidu.com")
        tp.key_event('lala',*tp.input_loc)
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
