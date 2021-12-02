# -*- codeing = utf-8 -*-
# @Time : 2021-11-16 10:21
# @Author 胡智
import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction

from pageobject.cancel import Cancel
from pageobject.delete import Delete
from pageobject.edit import Edit
from pageobject.havedone import Havedone
from pageobject.todolist_1 import Todo_1
from pageobject.todolist_2 import Todo_2


class Test01:
    def setup(self):
    # Capability设置
        desire_cap = {
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "appPackage": " com.tencent.wework",
            "platformName": "android",
            "deviceName": "emulator-5554",
            "noReset": True,  # 保存之前的的搜索登录信息等
            "skipDeviceInitialization": True,  # 跳过设备的初始化
            "dontStopAppOnReset": True,  # 不对应用进行关闭操作
            "unicodeKeyBooed": True,  # 设置中文输入
            "resetKeyBooed": True  # 设置中文输入
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        # 隐式等待
        self.driver.implicitly_wait(20)


    def test_todo1(self):
        """
        测试添加第一个待办"待办1"（通过按钮完成）
        断言添加的待办的名称是否为“待办1”
        :return:
        """
        todo1 =Todo_1(driver=self.driver)
        time.sleep(3)
        todo1.click_()
        todo1.works_()  # 添加待办
        todo1.works1_()
        time.sleep(5)
        # 断言
        current_text1 = self.driver.find_element_by_xpath("//*[@text='待办1']").text
        assert current_text1 == '待办1'

    def test_todo2(self):
        """
        测试添加第二个待办“待办2”（通过下拉框完成）
        :return:
        """
        todo1 = Todo_1(driver=self.driver)
        todo2 = Todo_2(driver=self.driver)
        todo2.work2_()
        todo1.works1_()
        self.driver.implicitly_wait(20)

    def test_havedone(self):
        """
        测试已完成的待办
        断言完成的待办的名称是否为“待办2”
        :return:
        """
        hd = Havedone(driver=self.driver)
        hd.havedone()
        # 断言
        self.driver.implicitly_wait(20)
        current_text = self.driver.find_element_by_xpath("//*[@text='待办2']").text
        assert current_text == '待办2'

    def test_delete(self):
        """
        测试删除待办
        :return:
        """
        de = Delete()
        de = Delete(driver=self.driver)
        de.long_press()

    def test_cancel(self):
        """
        测试在消息列表取消展示待办
        :return:
        """
        ca = Cancel()
        ca = Cancel(driver=self.driver)
        ca.cancel()

    def test_edit(self):
        """
        测试更新待办为“待办1-update”
          首先创建一个待办1
          在更新待办1
        断言添加的待办的名称是否为“待办1-update”
        :return:
        """
        # 更新 待办1
        ed = Todo_1(driver=self.driver)
        ed1 = Edit(driver=self.driver)
        time.sleep(3)
        ed.click_()
        ed.works_()
        ed.works1_()
        time.sleep(5)
        ed1.update_()
        time.sleep(10)
        current_text = self.driver.find_element_by_xpath("//*[@text='待办1-update']").text
        assert current_text == '待办1-update'


if __name__ == '__main__':
    pytest.main()