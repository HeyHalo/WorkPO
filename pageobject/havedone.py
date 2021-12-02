# -*- codeing = utf-8 -*-
# @Time : 2021-11-18 9:21
# @Author 胡智
import time

from BasePage.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

# 创建完成待办
class Havedone(BasePage):
    # 点击完成按钮
    el_havedone = (MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView")
    el_show = (MobileBy.ID,"com.tencent.wework:id/csi")
    def havedone(self):
        self.click(self.el_havedone)
        time.sleep(3)
        self.click(self.el_show)