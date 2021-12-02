# -*- codeing = utf-8 -*-
# @Time : 2021-11-18 10:09
# @Author 胡智

import time

from appium.webdriver.common.touch_action import TouchAction

from BasePage.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

class Edit(BasePage):
    # 更新待办名称

    # el_work = (MobileBy.XPATH, "//*[@text='工作台']")
    # el_date = (MobileBy.XPATH, "//*[@text='日程']")
    # el_todolist = (MobileBy.XPATH,"//*[@text='待办']")
    el_todo1 = (MobileBy.XPATH,"//*[@text='待办1']")
    el_todo2 = (MobileBy.XPATH,"//*[@text='待办1']")
    el_back = (MobileBy.ID,"com.tencent.wework:id/ivv")  # 返回


    def update_(self):
        # self.click(self.el_work)
        # self.click(self.el_date)
        # self.click(self.el_todolist)
        self.click(self.el_todo1)
        self.click(self.el_todo2)
        time.sleep(3)
        self.input(self.el_todo2, "-update")
        time.sleep(3)
        self.click(self.el_back)





