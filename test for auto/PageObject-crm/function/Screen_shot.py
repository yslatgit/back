#coding:utf-8
from selenium import webdriver
from PIL import Image
import datetime
import os
def switch_path():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    report_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
    report_path = report_path + "\\screenshot"
    os.chdir(report_path)
    print os.getcwd()
    return now_time

def screen_shot(driver,filename):
    now_time = switch_path()
    screen_name = now_time + filename
    driver.get_screenshot_as_file('%s.png' % screen_name)
    """
    driver .get("https://www.baidu.com")
    try:
        driver.find_element_by_id("lalal")
    except Exception as msg:
        print u"异常%s"%msg
        driver.get_screenshot_as_file('%s.png'%screen_name)
    finally:
        driver.quit()
    """
def screen_element_shot(driver,filename):
    now_time = switch_path()
    screen_element_name = now_time + filename
    driver.get("https://www.baidu.com")
    driver.save_screenshot('%s.png'%screen_element_name)
    element = driver.find_element_by_id("su")
    print element.location
    print element.size

    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    im = Image.open('%s.png'%screen_element_name)
    im = im.crop((left, top, right, bottom))
    im.save('%s.png'%screen_element_name)

    driver.quit()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    screen_shot(driver,'123')