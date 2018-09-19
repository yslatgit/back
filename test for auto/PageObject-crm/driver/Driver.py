#coding:utf-8
from selenium import webdriver
import time
class Driver():
    """firefox 0 普通浏览器  1  加载配置文件的浏览器
       chrome  0 普通浏览器  1  无界面浏览器
    """
    def __init__(self,parameter='ff',option=0):
        self.parameter = parameter
        self.option = option


    def driver(self):
        try:
            if self.parameter == 'ff' or self.parameter == 'firefox' or self.parameter == 'Firefox':
                if self.option == 0:
                    driver = webdriver.Firefox()
                    return driver
                elif self.option == 1:
                    profile_directory = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\xe5qiy45.default"
                    profile = webdriver.FirefoxProfile(profile_directory)
                    driver = webdriver.Firefox(profile)
                    return driver
                else:
                    print u"传入的参数%s有误"%self.option

            elif self.parameter == 'cc' or self.parameter == 'chrome':
                if self.option == 0:
                    driver = webdriver.Chrome()
                    return driver
                elif self.option == 1:
                    cc = webdriver.ChromeOptions()
                    cc.add_argument('headless')
                    driver = webdriver.Chrome(chrome_options=cc)
                    return driver
                else:
                    print u"传入的参数%s有误"%self.option

        except Exception as msg:
            print u"传入的参数%s有误"%self.parameter
            print u"异常日志如下%s"%msg

def get_driver(parameter='ff',option=0):
    cc = Driver(parameter,option)
    return cc.driver()

if __name__ == '__main__':
    driver = get_driver()
    driver.get("http://www.baidu.com")
    print driver.name
    print driver.title
    time.sleep(10)