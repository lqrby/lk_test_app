'''
Author: your name
Date: 2021-09-24 13:28:32
LastEditTime: 2021-09-24 14:42:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/appium_sync/multi_devices_sync.py
'''
from appium import webdriver
import yaml
from time import ctime
import multiprocessing


with open('./appium_sync/desired_caps.yaml','r') as file:
    data=yaml.load(file)

devices_list=['127.0.0.1:21503','127.0.0.1:7555']

def appium_desired(udid,port):
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=udid
    # desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    print('appium port:%s start run %s at %s' %(port,udid,ctime()))
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
    driver.implicitly_wait(5)
    return driver

desired_process=[]

for i in range(len(devices_list)):
    port=4723+2*i
    desired=multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
    desired_process.append(desired)

if __name__ == '__main__':
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
    # appium_desired(devices_list[0],4723)
    # appium_desired(devices_list[1],4725)