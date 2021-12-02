# -*- codeing = utf-8 -*-
# @Time : 2021-11-18 9:44
# @Author 胡智
import time

from appium.webdriver.common.touch_action import TouchAction

from BasePage.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

class Cancel(BasePage):

    el_info = (MobileBy.XPATH, "//*[@text='消息']")
    el_todo = (MobileBy.ID,"com.tencent.wework:id/itp")
    el_1 =(MobileBy.ID,"com.tencent.wework:id/iwm")
    el_can =(MobileBy.XPATH,"//*[@text='取消在聊天列表顶部展示']")
    el_back = (MobileBy.ID,"com.tencent.wework:id/ivv")

    # 取消取消在聊天列表顶部展示
    def cancel(self):
        self.click(self.el_info)
        self.click(self.el_todo)
        self.click(self.el_1)
        self.click(self.el_can)
        time.sleep(3)
        self.click(self.el_back)




