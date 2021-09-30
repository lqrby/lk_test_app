'''
Author: your name
Date: 2021-08-30 10:24:04
LastEditTime: 2021-09-30 14:38:28
LastEditors: Please set LastEditors
Description: In User Settings Edit  
FilePath: /lk_test_app/main.py
'''
import os, yaml
import pytest
import datetime
from Common.splicing import caps

ts = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
if __name__ == '__main__':
    # pytest.main(['-s', './Test_Cases/test_login.py', '--alluredir', "./allure_result/allure_temp"])
    # pytest.main(['-s', './Test_Cases/test_room.py', '--alluredir', "./allure_result/allure_temp"])
    # pytest.main(['-s', './Test_Cases', '--alluredir', "./allure_result/allure_temp"])
    for i in range(2):
        pytest.main(['-s', './Test_Cases/test_homeMakeFriends.py', '--alluredir', "./allure_result/allure_temp"])
        
        desired_capsArr = []
        with open(os.path.join(caps, "desired_caps.yaml"),"r", encoding="utf-8") as file:
            desired_capsArr = yaml.load(file, Loader=yaml.FullLoader)
            print("设备配置列表======",desired_capsArr)
        
        with open(os.path.join(caps, "desired_caps.yaml"),"w+", encoding="utf-8") as file:
            desired_capsArr.append(desired_capsArr.pop(0))
            desired_capsArr = yaml.dump(desired_capsArr, file, default_flow_style=False,allow_unicode=True)
            print("写入完毕")
    # os.system("allure generate ./allure_result/allure_temp -o ./allure_result/allure_report --clean")
    # os.system("D:/myObject/lk_test_app/sendMail.py")
    # os.system("allure open ./allure_result/allure_report")