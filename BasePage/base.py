# -*- codeing = utf-8 -*-
# @Time : 2021-11-16 8:51
# @Author 胡智

from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage:


    # 实例属性 构造函数
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    # 点击
    def click(self,loc):
        self.locator(loc).click()

    # 滑动向下
    def swipe_up(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        start_x = 0.63 * width
        start_y = height * 0.87
        end_x = start_x
        end_y = height * 0.3
        duration = 2000
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 下拉
    def xiala(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        start_x = 0.63 * width
        start_y = height * 0.3
        end_x = start_x
        end_y = height * 0.87
        duration = 2000
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 滑动向右
    def swipe_right(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        start_x = 0.83 * width
        start_y = height * 0.63
        end_x = 0.3 * width
        end_y = start_y
        duration = 2000
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)







