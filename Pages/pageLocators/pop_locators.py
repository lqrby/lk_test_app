'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-10-28 16:33:49
LastEditors: Please set LastEditors
Description: In User Settings Edit  
FilePath: /lk_test_app/Pages/pageLocators/pop_locators.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb


# import conftest


# 处理弹窗
class PopUpLocator:

    #启动app弹出用户协议同意按钮元素
    agree=(Mb.ID,'com.ourydc.yuebaobao:id/btn_ok') 

    #登录时弹出的确认用户协议确定按钮元素2
    determine = (Mb.ID,'com.ourydc.yuebaobao:id/tv_sure') 
    
    # 关闭入房邀请弹框 / 关闭女神开播引导弹窗按钮
    close_back = (Mb.ID, "com.ourydc.yuebaobao:id/back") 
    
    #关闭异常退厅弹框
    iv_cancel = (Mb.ID, "com.ourydc.yuebaobao:id/iv_cancel") # 异常退厅弹框no按钮
    iv_confirm = (Mb.ID, "com.ourydc.yuebaobao:id/iv_confirm") # 异常退厅弹框yes按钮

    # 设置未成年人保护弹窗
    setting_minors = (Mb.ID, "com.ourydc.yuebaobao:id/btn_iknow")
    
    #进入房间弹出马上点单弹窗元素
    order_now = (Mb.ID, "com.ourydc.yuebaobao:id/btn_pay")
   
    #聊天室已关闭
    close_broadcast = (Mb.ID, "com.ourydc.yuebaobao:id/iv_finish_close") 

    #打招呼弹窗
    say_hello = (Mb.ID, "com.ourydc.yuebaobao:id/tv_btn4") 	
    #跳过
    skip = (Mb.ID, "com.ourydc.yuebaobao:id/skip") 	

    #放弃奖励弹窗
    give_up_reward = (Mb.ID, "com.ourydc.yuebaobao:id/tv_cancle") 

    #允许哩咔语音拨打电话权限弹窗
    call_permission = (Mb.ID, "com.android.packageinstaller:id/permission_allow_button") 	
    #不再询问选择框	
    not_ask = (Mb.ID, "com.android.packageinstaller:id/do_not_ask_checkbox") 		

    # 立即提升魅力元素
    tv_to_profile = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_to_profile']") 
    # 关闭立即提升魅力元素
    # iv_close = (Mb.ID, "com.ourydc.yuebaobao:id/iv_close")
    iv_close = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/iv_close']")
    
    
    # 充值弹窗-充值按钮元素
    recharge = (Mb.ID, "com.ourydc.yuebaobao:id/tv_sure")
    cancel_close = (Mb.ID, "com.ourydc.yuebaobao:id/tv_cancel") #取消/稍后更新

    #立即更新
    btn_confirm = (Mb.ID, "com.ourydc.yuebaobao:id/btn_confirm")


    #关闭邀请连麦弹窗
    close_microphone = (Mb.ID, "com.ourydc.yuebaobao:id/closeIv")
    #连麦聊天按钮
    connect_microphone = (Mb.ID, "com.ourydc.yuebaobao:id/btn")
    
    #普通拍一拍按钮
    take_pat = (Mb.ID, "com.ourydc.yuebaobao:id/layout_replay")
    #关注并回拍
    back_shot = (Mb.ID, "com.ourydc.yuebaobao:id/layout_attention")

    #全部模式(聊天室弹出加入队伍弹窗)
    close_all_mode = (Mb.ID, "com.ourydc.yuebaobao:id/scroll_view")

    # #立即签到
    # sign_in = (Mb.ID, "com.ourydc.yuebaobao:id/button")

    #奖励中心-确定领取按钮
    confirm_to_receive = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn' and @text='确定']")





    

    popList = [
        close_back, iv_cancel, setting_minors, order_now,close_broadcast,skip,
        give_up_reward,say_hello,call_permission,iv_close,cancel_close,agree,
        close_microphone,take_pat
        ]

    # popList = [closeInvitInRoom[1], closeGameInvit[1], skipAD[1], allowpop1[1], allowpop2[1], onlyappallow[1],
    #            "允许定位", dialog[1], close_AD[1], check_shut[1], got_in[1], txtSkip[1], Adolescent[1]]
