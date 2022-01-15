'''
Author: your name
Date: 2021-09-06 15:59:48
LastEditTime: 2021-10-15 10:25:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/social_locator.py
'''



from appium.webdriver.common.mobileby import MobileBy as Mb

'''游戏的页面元素'''


class NewsLocators:

    iv_msg_contact = (Mb.ID, "com.ourydc.yuebaobao:id/iv_msg_contact") #通讯录按钮
    tv_position = (Mb.ID, "com.ourydc.yuebaobao:id/tv_position") #关注列表
    tv_title_two = (Mb.ID, "com.ourydc.yuebaobao:id/tv_title_two") #粉丝列表
    tv_title_three = (Mb.ID, "com.ourydc.yuebaobao:id/tv_title_three") #好友列表
    buttonSendMessage = (Mb.ID, "com.ourydc.yuebaobao:id/buttonSendMessage") #发送按钮
    editTextMessage = (Mb.ID, "com.ourydc.yuebaobao:id/editTextMessage") #聊天输入框
    iv_extra = (Mb.ID, "com.ourydc.yuebaobao:id/iv_extra") #添加好友按钮
    et_input = (Mb.ID, "com.ourydc.yuebaobao:id/et_input") #搜索输入框
    
    