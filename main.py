'''
Author: your name
Date: 2021-08-30 10:24:04
LastEditTime: 2021-11-02 10:23:18
LastEditors: Please set LastEditors
Description: In User Settings Edit  
FilePath: /lk_test_app/main.py
'''
import os
import pytest
import datetime


# ts = datetime.datetime.now().strftime("%Y%m%d %X")
ts = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

import os,time,sys,multiprocessing
file_path = os.path.join(os.path.abspath('.'))
file_path = file_path.replace('\\', '/')
sys.path.append(file_path)
from Common.log import get_logger
# from Common.getCpuAndMemory import DevicePerformanceMonitoring
from Common.splicing import caps
log = get_logger(logger_name="移动设备硬件资源监控日志")

# class ProcessMethod():
#     def __init__(self):
#         self.off = 1
#     #ui自动化入口 
#     def ui_main(self,p_name):
#         pytest.main(['-s', './Test_Cases', '--alluredir', "./allure_result/allure_temp"])
#         os.system("allure generate ./allure_result/allure_temp -o ./allure_result/{} --clean".format(ts))
#         os.system("allure generate ./allure_result/allure_temp -o ./allure_result/allure_report --clean")
#         os.system("7z a ./allure_result/{}.zip ./allure_result/{}".format(ts,ts))
#         log.info("xxxxxxxxxxxxxxxxxxxxxx结束了xxxxxxxxxxxxxxxxxxx")
    #移动设备资源监控
    # def resource_monitoring(self,p_name):
    #     # dpm = DevicePerformanceMonitoring()
    #     while True:
    #         dpm.all_device_information() #获取cpu和内存
    
 
# class Life(multiprocessing.Process):
#     def __init__(self, life_type, p_name):
#         multiprocessing.Process.__init__(self)
#         self.life_type = life_type
#         self.p_name = p_name
 
#     def run(self):
#         self.life_type(self.p_name)
 

if __name__ == '__main__':
    # pytest.main(['-s', './Test_Cases/test_homeMakeFriends.py', '--alluredir', "./allure_result/allure_temp"])
    pytest.main(['-s', './Test_Cases', '--alluredir', "./allure_result/allure_temp"])
    os.system("allure generate ./allure_result/allure_temp -o ./allure_result/{} --clean".format(ts))
    os.system("allure generate ./allure_result/allure_temp -o ./allure_result/allure_report --clean")
    os.system("7z a ./allure_result/{}.zip ./allure_result/{}".format(ts,ts))
    # dpm = DevicePerformanceMonitoring()
    # while True:
    #     # log.info("#################################################################")
    #     dpm.getCpu() #获取cpu和内存
    #     # dpm.get_cpuAndMemory() #获取指定包的app使用cpu和内存的方法
    #     dpm.get_battery_temperature() #电池温度
    #     log.info("#################################################################")
    #     time.sleep(3)
    
 
# if __name__ == '__main__':
#     start = time.time()
#     pm = ProcessMethod()
#     p1 = Life(pm.ui_main, "p1") 
#     p2 = Life(pm.resource_monitoring, "p2") 
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.terminate()
#     end = time.time()
#     log.info("总共用时:{}".format(datetime.datetime.fromtimestamp(end)-datetime.datetime.fromtimestamp(start)))



    # import time
    # import datetime
    # t1=time.time()
    # time.sleep(0.5)
    # t2=time.time()
    # print("相差",(datetime.datetime.fromtimestamp(t2)-datetime.datetime.fromtimestamp(t1)),"秒")