'''
Author: your name
Date: 2021-09-06 15:59:48
LastEditTime: 2021-09-27 15:45:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageObjects/sign_pop_page.py
'''

import time
from Common.basepage import BasePage
from selenium.common.exceptions import NoSuchElementException
from Pages.pageLocators.pop_locators import PopUpLocator as poploc
from Pages.pageLocators.login_locators import LoginPageLocator
from Common.log import get_logger

log = get_logger(logger_name="弹窗操作日志")

class SignPopPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    #检查是否有用户协议
    def check_agreement_one(self):
        log.info("检查用户协议弹窗按钮")
        time.sleep(2)
        try:
            agreementBtn = self.find_element(LoginPageLocator.agree)
        except NoSuchElementException:
            log.info("无用户协议弹窗按钮")
        else:
            agreementBtn.click()

    #检查是否有用户协议2
    def check_agreement_two(self):
        log.info("检查用户协议确认按钮")
        try:
            determineBtn = self.find_element(LoginPageLocator.determine)
        except NoSuchElementException:
            log.info("无用户协议确认按钮")
        else:
            determineBtn.click()

    #检查并关闭异常弹窗            
    def check_error_popup(self):
        self.exist_be_click(poploc.iv_cancel)


    #检查并关闭未成年设置弹窗            
    def check_MinorSettings(self):
        time.sleep(2)
        self.exist_be_click(poploc.setting_minors)

    #检查关闭女神开播引导弹窗       
    def check_goddess_Popup(self):
        self.exist_be_click(poploc.close_back)

    #检查关闭各种弹窗通用方法       
    def check_close_Popup(self,loc):
        self.exist_be_click(loc)

    #充值弹窗取消充值       
    def check_recharge_Popup(self):
        if self.is_element_exist(poploc.recharge):
            self.exist_be_click(poploc.cancel_close)
        else:
            pass


    #检查关闭提升魅力弹的方法       
    def check_close_EnhanceCharm(self):
        if self.is_element_exist(poploc.tv_to_profile):
            self.click_element(poploc.iv_close, model="关闭提升魅力弹窗")
        else:
            pass

    
