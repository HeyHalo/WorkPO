# -*- codeing = utf-8 -*-
# @Time : 2021-11-16 9:05
# @Author 胡智
import time

from appium.webdriver.common.touch_action import TouchAction

from BasePage.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

#新建待办2（下拉方式）

class Todo_2(BasePage):
    el_in =(MobileBy.ID,"com.tencent.wework:id/bqv")
    el_people = (MobileBy.ID,"com.tencent.wework:id/bfm") # 参与人
    el_search = (MobileBy.ID,"com.tencent.wework:id/iwm")
    el_search1 = (MobileBy.XPATH, "//*[@text='搜索']")  # 点击搜索框
    el_hogwarts = (MobileBy.ID, "com.tencent.wework:id/e4j")
    el_queding = (MobileBy.ID,"com.tencent.wework:id/hkb")
    el_cunchu = (MobileBy.XPATH,"//*[@text='保存']")

    def work2_(self):
        # 隐式等待
        self.driver.implicity_wait(10)
        self.xiala()  # 下拉创建待办
        self.input(self.el_in,"待办2")
    def work3_(self):
        # 隐式等待
        self.xiala()  # 下拉创建待办
        self.input(self.el_in,"待办1")






