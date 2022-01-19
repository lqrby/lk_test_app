'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-09-26 10:08:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/home_locators.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb

'''首页的页面元素'''


class HomePageLocator:
    ###########################哩咔首页交友模块元素定位开始##########################
    # 隐私政策弹窗
    dating_module = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_home") # 交友模块
    
    message_moduke = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_message") # 消息模块
    my_module = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_mine") # 我的模块
    
    
    
    
    
