'''
Author: your name
Date: 2021-09-22 15:48:50
LastEditTime: 2021-09-26 10:43:33
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/appium_sync/appium_devices_sync.py
'''
import sys, yaml, pytest
sys.path.append("D:/myObject/lk_test_app")
from appium_sync.multi_appium import appium_start
from appium_sync.multi_devices import appium_desired
from TestDatas.login import login_success
from appium_sync.check_port import *
from time import sleep
import multiprocessing

# devices_list=['127.0.0.1:21503','127.0.0.1:7555']
# class appiumDevicesSync():

def start_appium_action(host,port):
    if check_port(host,port):
        appium_start(host,port)
        return True
    else:
        print('appium {} start fail'.format(port))
        return False
        

def start_devices_action(udid,port,data):
    host='127.0.0.1'
    if start_appium_action(host,port):
        appium_desired(udid,port,data)
    else:
        release_port(port)

def appium_start_sync():
    print('=====appium_start_sync=====')
    appium_process=[]
    for i in range(2):
        host = '127.0.0.1'
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        appium_process.append(appium)

    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()
    sleep(5)


# @pytest.mark.parametrize("loginData", login_success)
def devices_star_sync():
    print('======devices_star_sync===')
    desired_process = []
    with open('./appium_sync/desired_caps.yaml','r',encoding="utf-8") as file:
        appium_data=yaml.load(file)
    for i,data in enumerate(appium_data):
        port = 4723 + 2 * i
        desired = multiprocessing.Process(target=start_devices_action, args=(data["udid"], port, data))
        desired_process.append(desired)

    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

if __name__ == '__main__':
    # appium_start_sync()
    devices_star_sync()