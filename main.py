'''
Author: your name
Date: 2021-08-30 10:24:04
LastEditTime: 2021-09-03 18:03:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/main.py
'''
import os

import pytest
import datetime

ts = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
if __name__ == '__main__':
    # pytest.main(['-s', './Test_Cases/test_login.py', '--alluredir', "./Outputs/allure/allure_temp"])
    pytest.main(['-s', './Test_Cases/test_room.py', '--alluredir', "./Outputs/allure/allure_temp"])
    # pytest.main(['-s', './Test_Cases/test_homeMakeFriends.py', '--alluredir', "./Outputs/allure/allure_temp"])
    # pytest.main(['-s', './Test_Cases', '--alluredir', "./Outputs/allure/allure_temp"])
    os.system("allure generate ./Outputs/allure/allure_temp -o ./Outputs/allure/allure_report --clean")
    os.system("D:/myObject/lk_test_app/sendMail.py.py")
    os.system("allure open ./Outputs/allure/allure_report")
