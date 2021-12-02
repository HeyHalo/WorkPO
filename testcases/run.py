# -*- codeing = utf-8 -*-
# @Time : 2021-11-15 16:16
# @Author 胡智
# 生成测试报告  用例数据
import os

import pytest
if __name__ == '__main__':
    #执行用例生成测试报告
    pytest.main(['-s','-v','test_01.py','--alluredir','./result'])
    # 生成测试报告
    os.system('allure generate ./result -o ./reports')
