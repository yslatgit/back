#coding:utf-8
from browser.driver import driver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):

    def __init__(self):
        self.driver = driver

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda x:x.find_element(*loc))
            return self.driver.find_element(*loc)
        except:
            print u"%s页面中未找到%s元素" % (self, loc)

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda x:x.find_element(*loc))
            return self.driver.find_elements(*loc)
        except:
            print u"%s页面中未找到%s元素" % (self, loc)


