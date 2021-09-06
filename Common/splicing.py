import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# TestDatas测试数据
testdatas_dir = os.path.join(base_dir, "TestDatas")
# TestCases测试脚本
testcases_dir = os.path.join(base_dir, "TestCases")
# Outputs/reports
htmlreport_dir = os.path.join(base_dir, "Outputs/reports")
# Outputs/logs
logs_dir = os.path.join(base_dir, "Outputs/logs")
# Outputs/screenshots 存放错误截图
screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")
# Desired_Caps
caps = os.path.join(base_dir, "Desired_Caps")
# lika.log存放日志的路径
reports_log = os.path.join(logs_dir, "lika.log")

dir = os.path.join(base_dir, "Common")
