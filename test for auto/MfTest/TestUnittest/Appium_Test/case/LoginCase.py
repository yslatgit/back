#coding:utf-8


from page.LoginPage import LoginPage
import unittest

class LoginCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        Lo = LoginPage()
        Lo.login_mf_app("18153529186")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
