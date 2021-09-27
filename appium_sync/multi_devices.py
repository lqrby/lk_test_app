'''
Author: your name
Date: 2021-09-24 10:27:37
LastEditTime: 2021-09-26 13:29:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/appium_sync/multi_devices.py
'''
from appium import webdriver
import yaml, pytest, time
from  time import  ctime
from appium_sync.kyb_test import KybTest
from TestDatas.login import login_success
from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageObjects.login_page import LoginPage
from Common.log import get_logger
from Pages.pageObjects.sign_pop_page import SignPopPage

log = get_logger(logger_name="登录")



# @pytest.fixture(scope="function")
# @pytest.mark.parametrize("loginData", login_success)
def appium_desired(udid,port,appiumData):
    print('appium port:%s start run %s at %s' %(port,udid,ctime()))
    driver=webdriver.Remote('http://'+str(appiumData['ip'])+':'+str(port)+'/wd/hub',appiumData)
    driver.implicitly_wait(5)
    status = check_notLogin_SignIn(driver, appiumData["username"], appiumData["password"])
    if status:
        # yield driver
        return driver
        time.sleep(3)
        driver.close_app()
        driver.quit()
    else:
        log.info("关闭app")
        driver.close_app()
        driver.quit()


# 是否登录状态，未登录则登录
def check_notLogin_SignIn(driver,user, password):
    if CommonBus(driver).get_userStatus():
        log.info("===========当前已是登录状态，无需登录========")
        time.sleep(1)
        return True
    else:
        log.info("===========开始登录========")
        loginStatus = LoginPage(driver).login_mobile_passWord(user, password)
        if loginStatus:
            log.info("===========登录成功========")
            time.sleep(1)
            SignPopPage(driver).check_error_popup()
            return True
        else:
            log.info("===========登录失败========")
            driver.close_app()
            driver.quit()
            return False

