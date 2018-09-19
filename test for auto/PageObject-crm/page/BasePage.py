#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from function.Screen_shot import *
from selenium.webdriver.support.wait import WebDriverWait
class BasePage(object):

    #初始化方法
    def __init__(self,driver):
        self.driver = driver
        self.base_url = "http://account.mofanghr.com/login.action"
        #self.my_customer_url = "http://crm1.mofanghr.com/manager/customerClue/list.action"

    #打开网址的私有化方法
    def _open(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()


    #打开网址--->调用私有化方法
    def open(self):
        self._open()

    #打开自定义url的方法
    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    #重写查找某个元素的方法
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print u"%s页面中未找到%s元素"%(self,loc)

    #重写查找某组元素的方法
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda x:x.find_elements(*loc).is_dispalyed())
            return self.driver.find_elements(*loc)
        except:
            print u"%s页面上没找到%s组元素"%(self,loc)

    #执行js的方法
    def script(self,js):
        self.driver.execute_script(js)

    #切换窗口的方法
    def switch_to_new_window(self):
        #获取当前页的句柄
        h = self.driver.current_window_handle
        #获取所有句柄
        all_h = self.driver.window_handles
        for i in all_h:
            if i != h:
                self.driver.switch_to_window(i)

    #切换iframe的方法
    def switch_frame(self,frame_id):
        return self.driver.switch_to_frame(frame_id)

    #浏览器后退
    def back(self):
        return self.driver.back()

    #浏览器前进
    def forward(self):
        return self.driver.forward()

    #截图方法--->重写function.Screen_shot中的方法
    def screen_shot(self):
        screen_shot(self.driver,filename='1')

    #鼠标悬停事件
    def mouse_hover(self,*loc):
        return ActionChains(self.driver).move_to_element(self.driver.find_element(*loc)).perform()

    #鼠标右击操作
    def mouse_context_click(self,*loc):
        return ActionChains(self.driver).context_click(self.driver.find_element(*loc)).perform()

    #鼠标双击事件
    def mouse_double_click(self,*loc):
        return ActionChains(self.driver).double_click(self.driver.find_element(*loc)).perform()

    #键盘操作事件
    def key_event(self,value,*loc):
        return self.driver.find_element(*loc).send_keys(value)











