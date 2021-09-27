'''
Author: your name
Date: 2021-09-06 15:59:47
LastEditTime: 2021-09-27 18:18:59
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Common/splicing.py
'''

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# TestDatas测试数据
testdatas_dir = os.path.join(base_dir, "TestDatas")
# TestCases测试脚本
testcases_dir = os.path.join(base_dir, "TestCases")
# Outputs/reports
htmlreport_dir = os.path.join(base_dir, "allure_result/allure_report")
# Outputs/logs
logs_dir = os.path.join(base_dir, "allure_result/logs")
# Outputs/screenshots 存放错误截图
screenshot_dir = os.path.join(base_dir, "allure_result/screenshots")
# Desired_Caps
caps = os.path.join(base_dir, "Desired_Caps")
# lika.log存放日志的路径
reports_log = os.path.join(logs_dir, "lika.log")

dir = os.path.join(base_dir, "Common")
