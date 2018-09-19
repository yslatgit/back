from selenium import webdriver
class Login:

    def __init__(self,base_url,num):
        self.base_url = base_url
        self.num = num
        self.driver = self.choice_browser()
    def choice_browser(self):
        if self.num == 1:
            driver = webdriver.Firefox()
            return driver
        if self.num == 2:
            driver = webdriver.Chrome()
            return driver
    def go(self):
        self.driver.get(self.base_url)



LL = Login("http://i.mofanghr.com",1)
LL.go()



