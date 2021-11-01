'''
Author: your name
Date: 2021-08-30 10:24:04
LastEditTime: 2021-11-01 10:19:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/conftest.py
'''
import time
from Common.splicing import caps
import os
import yaml
import pytest
from appium import webdriver
from Common.log import get_logger
from Pages.pageObjects.login_page import LoginPage
from Pages.pageObjects.Common_Buss import CommonBus
from TestDatas.login import login_success
from Pages.pageObjects.sign_pop_page import SignPopPage


log = get_logger(logger_name="前置-日志")

'''运行前-前置条件-打开App-关闭应用，关闭会话'''


@pytest.fixture(scope="function")
def start_app():
    driver = basedriver()
    print("检测用户是否已登录")
    CommonBus(driver).check_loggedIn_signOut()
    yield driver
    # 后置
    # 关闭应用，关闭会话
    driver.close_app()
    driver.quit()


'''前置条件-获取toast时候-把默认UiAutomator1改成UiAutomator2'''
@pytest.fixture(scope="function")
def start_app_toast():
    driver = base_driver(automationName="UiAutomator2")
    time.sleep(2)
    # driver.implicitly_wait(8)
    yield driver
    driver.close_app()
    driver.quit()


'''前置条件-打开App时候判断是否登录，如果没登录先登录如果已登录打开App后关闭广告'''
@pytest.fixture(scope="function")
def startApp_keepUserData():
    driver = base_driver()
    # driver.implicitly_wait(8)
    time.sleep(2)
    if check_notLogin_SignIn(driver, login_success[0]["username"], login_success[0]["password"], login_success[0]["expected"]):
        pass
    else:
        log.info("登录失败")
        driver.close_app()
        driver.quit()
    yield driver
    time.sleep(3)
    driver.close_app()
    driver.quit()

# 是否登录状态，未登录则登录
def check_notLogin_SignIn(driver,user, password, expected):
    if CommonBus(driver).get_userStatus():
        log.info("===========当前已是登录状态，无需登录========")
        time.sleep(1)
        return True
    else:
        log.info("===========开始登录========")
        loginStatus = LoginPage(driver).login_mobile_passWord(user, password, expected)
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



'''  启动浏览器会话
     与appium server进行连接，并发送要操作的设备对象信息。'''
def basedriver(noReset=None, automationName=None, server_port=4723):
    with open(os.path.join(caps, "desired_caps.yaml"), encoding="utf-8") as file:
        desired_capsArr = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps = desired_capsArr[0]
        log.info("设备信息:{}".format(desired_caps))
    driver=webdriver.Remote('http://{}:{}/wd/hub'.format(desired_caps["ip"], server_port), desired_caps)
    return driver


def base_driver(noReset=None, automationName=None, port=4723):
    # 读取全局的一个caps选项。
    with open(os.path.join(caps, "desired_caps.yaml"), encoding="utf-8") as file:
        desired_capsArr = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps = desired_capsArr[0]
    driver=webdriver.Remote('http://{}:{}/wd/hub'.format(desired_caps["ip"], port), desired_caps)
    # 根据参数来定制化启动选项
    # if noReset is not None and noReset in [True, False]:
    #     desired_caps["noReset"] = noReset
    # if automationName is not None:
    #     desired_caps["automationName"] = automationName
    # driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(server_port), desired_caps)
    return driver





        