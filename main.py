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
from Common.splicing import caps

# ts = datetime.datetime.now().strftime("%Y%m%d %X")
ts = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

if __name__ == '__main__':
    pytest.main(['-s', './Test_Cases/test_square.py', '--alluredir', "./allure_result/allure_temp"])
    os.system("allure generate ./allure_result/allure_temp -o ./allure_result/{} --clean".format(ts))
    os.system("allure generate ./allure_result/allure_temp -o ./allure_result/allure_report --clean")
    os.system("7z a ./allure_result/{}.zip ./allure_result/{}".format(ts,ts))
    os.system("allure open ./allure_result/allure_report")
    #======================================================================================================
















    
    # pytest.main(['-s', './Test_Cases/test_login.py', '--alluredir', "./allure_result/allure_temp"])
    # pytest.main(['-s', './Test_Cases/test_room.py', '--alluredir', "./allure_result/allure_temp"])
    # pytest.main(['-s', './Test_Cases/test_homeMakeFriends.py', '--alluredir', "./allure_result/allure_temp"])
    # pytest.main(['-s', './Test_Cases', '--alluredir', "./allure_result/allure_temp"])
    
    # for i in range(1):
    #     # pytest.main(['-s', './Test_Cases/test_homeMakeFriends.py', '--alluredir', "./allure_result/allure_temp"])
    #     pytest.main(['-s', './Test_Cases', '--alluredir', "./allure_result/allure_temp"])
    #     desired_capsArr = []
    #     with open(os.path.join(caps, "desired_caps.yaml"),"r", encoding="utf-8") as file:
    #         desired_capsArr = yaml.load(file, Loader=yaml.FullLoader)
    #         print("设备配置列表======",desired_capsArr)
        
    #     with open(os.path.join(caps, "desired_caps.yaml"),"w+", encoding="utf-8") as file:
    #         desired_capsArr.append(desired_capsArr.pop(0))
    #         desired_capsArr = yaml.dump(desired_capsArr, file, default_flow_style=False,allow_unicode=True)
    #         print("写入完毕")
    # os.system("allure generate ./allure_result/allure_temp -o ./allure_result/allure_report")
    # os.system("allure open ./allure_result/allure_report")
    # os.system("allure generate ./allure_result/allure_temp -o ./allure_result/allure_report/{} --clean".format(ts))
    # os.system("D:/myObject/lk_test_app/sendMail.py")
    # os.system("allure open ./allure_result/allure_report")
    