# -*- codeing = utf-8 -*-
# @Time : 2021-11-16 9:05
# @Author 胡智
import time

from appium.webdriver.common.touch_action import TouchAction

from BasePage.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

# 新建待办1
class Todo_1(BasePage):

    # 点击工作台
    el_work = (MobileBy.XPATH, "//*[@text='工作台']")
    el_date = (MobileBy.XPATH, "//*[@text='日程']")
    el_todolist = (MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    el_tianjia = (MobileBy.ID,"com.tencent.wework:id/iwf")
    el_in =(MobileBy.ID,"com.tencent.wework:id/bqv")
    el_people = (MobileBy.ID,"com.tencent.wework:id/bfm") # 参与人
    el_search = (MobileBy.ID,"com.tencent.wework:id/iwm") # 搜索
    el_search1 = (MobileBy.XPATH,"//*[@text='搜索']")  # 点击搜索框
    el_hogwarts = (MobileBy.ID,"com.tencent.wework:id/e4j")
    el_queding = (MobileBy.ID,"com.tencent.wework:id/hkb")
    el_cunchu = (MobileBy.ID,"com.tencent.wework:id/iv0")

    def click_(self):
        self.click(self.el_work)
        self.click(self.el_date)
        self.click(self.el_todolist)

    def works_(self):
        self.click(self.el_tianjia)
        self.input(self.el_in,"待办1")

    # 新建联系人
    def works1_(self):
        self.click(self.el_people)  # 参与人
        self.driver.implicity_wait(10)
        self.click(self.el_search)
        self.click(self.el_search1)
        self.input(self.el_search1,"hogwarts")
        time.sleep(10)
        self.click(self.el_hogwarts)
        time.sleep(3)
        self.click(self.el_queding)
        self.driver.implicity_wait(10)
        time.sleep(3)
        self.click(self.el_cunchu)




