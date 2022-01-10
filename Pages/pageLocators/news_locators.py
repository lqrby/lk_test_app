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

    # square_module = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_dynamic") # 广场模块
    # dynamic_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv']/child::android.view.ViewGroup") #动态列表
    # iv_prise = (Mb.ID, "com.ourydc.yuebaobao:id/tv_praise") #点赞
    # follow = (Mb.ID, "com.ourydc.yuebaobao:id/btn_attention") # 关注用户元素
    # tvnick = (Mb.ID, "com.ourydc.yuebaobao:id/tv_nick") # 昵称
    # tv_content = (Mb.ID, "com.ourydc.yuebaobao:id/tv_content") #动态列表
    # # nearby_dynamics_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/viewpager']/descendant::com.ourydc.yuebaobao:id/tv_content") # 附近动态列表元素
    # # nearby_dynamics_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content']/parent::com.ourydc.yuebaobao:id/rcv") # 附近动态列表元素
    # # nearby_dynamics_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv']/descendant::com.ourydc.yuebaobao:id/tv_content") # 附近动态列表元素

    # nearby_dynamics_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/v_sex_age']") # 附近动态列表元素
    # # nearby_dynamics_list = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_nickname']") # 附近动态列表元素
    # nearby_dynamics_list2 = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_tag_name']") # 附近动态*人参与
    # all_mode = (Mb.ID, "com.ourydc.yuebaobao:id/mvp") #全部模式（聊天室的一个蒙层）
    # reportBtn = (Mb.ID,"com.ourydc.yuebaobao:id/tv") #举报
    # commitBtn = (Mb.ID,"com.ourydc.yuebaobao:id/btn_commit") #提交按钮

    # square_attention = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and @text='关注']") # 附近动态*人参与
    iv_msg_contact = (Mb.ID, "com.ourydc.yuebaobao:id/iv_msg_contact") #通讯录按钮
    tv_position = (Mb.ID, "com.ourydc.yuebaobao:id/tv_position") #关注列表
    tv_title_two = (Mb.ID, "com.ourydc.yuebaobao:id/tv_title_two") #粉丝列表
    tv_title_three = (Mb.ID, "com.ourydc.yuebaobao:id/tv_title_three") #好友列表
    buttonSendMessage = (Mb.ID, "com.ourydc.yuebaobao:id/buttonSendMessage") #发送按钮
    iv_extra = (Mb.ID, "com.ourydc.yuebaobao:id/iv_extra") #添加好友按钮
    et_input = (Mb.ID, "com.ourydc.yuebaobao:id/et_input") #搜索输入框
    
    