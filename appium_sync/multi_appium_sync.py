'''
Author: your name
Date: 2021-09-24 13:28:32
LastEditTime: 2021-09-24 13:35:08
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/appium_sync/multi_appium_sync.py
'''
import subprocess
from time import  ctime
import multiprocessing

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' %(cmd,ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_sync/appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

appium_process=[]

for i in range(2):
    host='127.0.0.1'
    port=4723+2*i 

    appium=multiprocessing.Process(target=appium_start,args=(host,port))
    appium_process.append(appium)

if __name__ == '__main__':
    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()