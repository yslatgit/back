#coding:utf-8

from selenium.webdriver.common.by import By
from basepage.BasePage import BasePage
from function.ToolClass import *
import random

class RegisterPage(BasePage):

    save_loc = (By.XPATH,"//*[@text='保存']")
    dialog_loc = (By.ID, 'com.mf.mfhr:id/tv_dialog_confirm')
    sure_loc = (By.ID, 'com.mf.mfhr:id/iv_right')
    #阻断页1--->上传头像、姓名、性别、出生年月日
    head_portrait_loc = (By.ID,'com.mf.mfhr:id/iv_basic_info_camera')
    photo_album_loc = (By.ID,'com.mf.mfhr:id/btn_options_album')
    photo_list_loc = (By.CLASS_NAME,'GLView')
    photo_choice_loc = (By.ID,'com.android.gallery3d:id/confirm_btn_in_crop')
    name_loc = (By.ID,'com.mf.mfhr:id/et_basic_info_name')
    gender_loc = (By.ID,'com.mf.mfhr:id/ll_basic_info_gender')
    birthday_loc = (By.ID,'com.mf.mfhr:id/ll_basic_info_dob')

    # 阻断页2--->学历、参加工作时间、所在城市、求职状态
    education_loc = (By.ID,'com.mf.mfhr:id/ll_person_info_education')
    join_work_date_loc = (By.ID,'com.mf.mfhr:id/ll_person_info_join_work_date')
    city_loc = (By.ID,'com.mf.mfhr:id/ll_person_info_city')
    status_loc = (By.ID,'com.mf.mfhr:id/ll_person_info_status')

    #阻断页3--->期望职位、期望行业、薪资、期望城市
    expected_position_loc = (By.ID,'com.mf.mfhr:id/ll_career_objective_positions')

    position_list = ["技术","金融"]
    position_list_loc = (By.XPATH,"//*[@text='%s']"%position_list[0])

    position_detail = ["后端开发","前端开发"]
    position_detail_loc = (By.XPATH,"//*[@text='%s']"%position_detail[0])

    position_layout = ["C","java"]
    position_layout_loc = (By.XPATH,"//*[@text='%s']"%position_layout[1])

    expection_industries_loc = (By.ID,'com.mf.mfhr:id/ll_career_objective_industries')
    industries_list_loc = (By.XPATH,"//*[@text='互联网']")
    salary_loc = (By.ID,'com.mf.mfhr:id/ll_career_objective_salary')
    expected_city_loc = (By.ID,'com.mf.mfhr:id/ll_career_objective_city')

    def swipe_once(self,b1=0.83,b2=0.85):
        time.sleep(0.5)
        swipe_height(0.4,b1,b2)
        time.sleep(0.5)

    def swipe_twice(self,b1=0.85,b2=0.9):
        time.sleep(0.5)
        swipe_height(0.3,b1,b2)
        time.sleep(0.5)
        swipe_height(0.7,b1,b2)
        time.sleep(0.5)

    def click_dialog(self):
        print "跳过dialog阻断页" + "\n"
        try:
            self.find_element(*self.dialog_loc).click()
        except:
            pass

    def click_save(self):
        print "点击保存按钮" + "\n"
        self.find_element(*self.save_loc).click()
        time.sleep(0.5)

    # ----第一阻断页----

    def update_head_portrait(self):
        print "上传头像" + "\n"
        self.find_element(*self.head_portrait_loc).click()
        self.find_element(*self.photo_album_loc).click()
        self.find_elements(*self.photo_list_loc)[26].click()
        self.find_elements(*self.photo_list_loc)[2].click()
        self.find_element(*self.photo_choice_loc).click()
        time.sleep(2)

    def input_name(self):
        print "填写名字" + "\n"
        # name_list = ["张学倩","张婷婷","徐婵媛","欧阳颖","高奇"]
        # i = random.randint(0,5)
        self.find_element(*self.name_loc).click()
        self.find_element(*self.name_loc).send_keys(u"张扬")
        time.sleep(1)

    def select_gender(self):
        print "选择性别" + "\n"
        self.find_element(*self.gender_loc).click()
        self.swipe_once()
        self.find_element(*self.sure_loc).click()

    def select_birthday(self):
        print "选择生日" + "\n"
        self.find_element(*self.birthday_loc).click()
        self.swipe_twice()
        self.find_element(*self.sure_loc).click()

    # ----第二阻断页----

    def select_education(self):
        print "选择学历" + "\n"
        self.find_element(*self.education_loc).click()
        self.swipe_once()
        self.find_element(*self.sure_loc).click()

    def select_join_work_date(self):
        print "选择参加工作时间" + "\n"
        self.find_element(*self.join_work_date_loc).click()
        self.swipe_twice()
        self.find_element(*self.sure_loc).click()

    def select_city(self):
        print "选择城市" + "\n"
        try:
            self.find_element(*self.city_loc).click()
            self.swipe_twice()
            self.find_element(*self.sure_loc).click()
        except Exception as msg:
            print "已自动定位"
            print "错误日志为%s"%msg

    def select_status(self):
        print "选择求职状态" + "\n"
        self.find_element(*self.status_loc).click()
        self.swipe_once()
        self.find_element(*self.sure_loc).click()

    # ----第二阻断页----

    def select_expected_position(self):
        print "选择期望职位" + "\n"
        self.find_element(*self.expected_position_loc).click()
        self.find_element(*self.position_list_loc).click()
        time.sleep(0.5)
        self.find_element(*self.position_detail_loc).click()
        self.find_element(*self.position_layout_loc).click()
        self.click_save()

    def select_expected_industries(self):
        print "选择期望行业" + "\n"
        time.sleep(0.5)
        self.find_element(*self.expection_industries_loc).click()
        print "1"
        self.find_element(*self.industries_list_loc).click()
        self.click_save()

    def select_salary(self):
        print "选择薪资" + "\n"
        self.find_element(*self.salary_loc).click()
        self.swipe_twice()
        self.find_element(*self.sure_loc).click()

    def select_expected_city(self):
        print "选择期望城市" + "\n"
        self.find_element(*self.expected_city_loc).click()
        self.swipe_twice()
        self.find_element(*self.sure_loc).click()

    #-----1-----2-----3-----

    def skip_pause_page_one(self):
        self.click_dialog()
        self.update_head_portrait()
        self.input_name()
        self.select_gender()
        self.select_birthday()
        self.click_save()

    def skip_pause_page_two(self):
        self.select_education()
        self.select_join_work_date()
        self.select_city()
        self.select_status()
        self.click_save()

    def skip_pause_page_three(self):
        self.select_expected_position()
        self.select_expected_industries()
        self.select_salary()
        self.select_expected_city()
        self.click_save()
        self.click_dialog()




