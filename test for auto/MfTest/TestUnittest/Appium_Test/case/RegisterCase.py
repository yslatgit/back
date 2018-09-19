#coding:utf-8

from page.LoginPage import LoginPage
from page.RegisterPage import RegisterPage
import unittest

class RegisterCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_register(self):
        Lo = LoginPage()
        Lo.login_mf_app("18153599998")
        Re = RegisterPage()
        Re.skip_pause_page_one()
        Re.skip_pause_page_two()
        Re.skip_pause_page_three()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()