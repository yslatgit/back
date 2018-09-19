#coding:utf-8
from selenium import webdriver

def choice_driver(name):
    if name == "firefox" or name == "Firefox" or name == "ff":
        driver = webdriver.Firefox()
        return driver
    elif name == "chrome" or name == "Chrome" or name == "ch":
        driver = webdriver.Chrome()
        return driver
    else:
        print u"没找到可以使用的浏览器，您可以使用 Firefox、Chrome"



if __name__ == '__main__':
    print choice_driver("ff").name

