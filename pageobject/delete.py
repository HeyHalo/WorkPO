# -*- codeing = utf-8 -*-
# @Time : 2021-11-18 9:44
# @Author 胡智
from appium.webdriver.common.touch_action import TouchAction

from BasePage.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

class Delete(BasePage):
    # 删除待办事项
    #el_de1 = (MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView")
    el_del2 = (MobileBy.ID,"com.tencent.wework:id/ivv")  # 点击×
    el_del3 = (MobileBy.ID,"com.tencent.wework:id/ivv")

    def long_press(self):
        action = TouchAction(self.driver)
        el = self.driver.find_element_by_xpath("//*[@text='待办1']")
        # 5000是设置的长按时间（单位/毫秒）
        action.long_press(el).wait(5000).release().perform()
        self.click(self.el_del2)
        self.click(self.el_del3)


