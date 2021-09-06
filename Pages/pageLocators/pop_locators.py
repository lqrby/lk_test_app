'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-09-03 11:25:19
LastEditors: Please set LastEditors
Description: In User Settings Edit  
FilePath: \lk_test_app\Pages\pageLocators\pop_locators.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb


# import conftest


# 处理弹窗
class PopUp:



    
    # 关闭入房邀请弹框
    closeInvitInRoom = (Mb.ID, "com.ourydc.yuebaobao:id/back")
    
    #关闭异常退厅弹框
    iv_cancel = (Mb.ID, "com.ourydc.yuebaobao:id/iv_cancel") 

    # 设置未成年人保护弹窗
    setting_minors = (Mb.ID, "com.ourydc.yuebaobao:id/btn_iknow")
    
    #进入房间弹出马上点单弹窗元素
    order_now = (Mb.ID, "com.ourydc.yuebaobao:id/btn_pay")
   

    popList = [closeInvitInRoom, iv_cancel, setting_minors, order_now]

    # popList = [closeInvitInRoom[1], closeGameInvit[1], skipAD[1], allowpop1[1], allowpop2[1], onlyappallow[1],
    #            "允许定位", dialog[1], close_AD[1], check_shut[1], got_in[1], txtSkip[1], Adolescent[1]]
