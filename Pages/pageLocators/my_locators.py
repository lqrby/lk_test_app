'''
Author: your name
Date: 2021-09-06 15:59:48
LastEditTime: 2021-11-02 14:12:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/my_locators.py
'''
'''
@File    :  my_locators.py    
@Contact :  fangfang.song@asiainnovations.com

@Modify Time    2021/4/1 9:29 下午    
@Author  :  songfang  
@Version :  1.0
@Desciption : 
'''

from appium.webdriver.common.mobileby import MobileBy as Mb


class MyLocators:

    #=================我的一级页面元素===========
    # 【我的】模块按钮元素
    meBtn=(Mb.ID,'com.ourydc.yuebaobao:id/iv_tab_mine') 
    
    logoutBtn=(Mb.ID,'com.ourydc.yuebaobao:id/btn_logo_out') # 退出登录按钮
    logoutOkBtn=(Mb.ID,'com.ourydc.yuebaobao:id/tv_cancel') # 确认退出

    # 个人头像
    sdVipCover = (Mb.ID, "com.ourydc.yuebaobao:id/iv_avatar")
    # 身份认证
    authentication = (Mb.ID, "com.ourydc.yuebaobao:id/iv_authentication")
    # 创建房间入口
    iv_open_room = (Mb.ID, "com.ourydc.yuebaobao:id/iv_open_room")
    # 个人资料编辑入口
    iv_edit = (Mb.ID, "com.ourydc.yuebaobao:id/iv_eidt")
    # 我的好友
    v_user_friends = (Mb.ID, "com.ourydc.yuebaobao:id/v_user_friends")
    # 谁看过我
    v_look_me = (Mb.ID, "com.ourydc.yuebaobao:id/v_look_me")
    # 派对足迹
    v_footprint = (Mb.ID, "com.ourydc.yuebaobao:id/v_footprint")
    # 充值
    iv_recharge = (Mb.ID, "com.ourydc.yuebaobao:id/iv_recharge")
    # 商城
    iv_dress_store = (Mb.ID, "com.ourydc.yuebaobao:id/iv_dress_store")
    # 会员
    iv_vip = (Mb.ID, "com.ourydc.yuebaobao:id/iv_vip")
    # 我的动态
    my_dynamic = (Mb.ID, "com.ourydc.yuebaobao:id/v_dynamic") 
    # 我的背包
    my_knapsack = (Mb.ID, "com.ourydc.yuebaobao:id/v_backpack") 
    # 奖励中心
    reward_center = (Mb.XPATH, "com.ourydc.yuebaobao:id/v_rewards") 
    # 游戏大厅
    game_hall = (Mb.ID, "com.ourydc.yuebaobao:id/v_game_layout")
    # 活动中心
    activity_center = (Mb.ID, "com.ourydc.yuebaobao:id/v_activity") 
    # 申请家族
    apply_family = (Mb.ID, "com.ourydc.yuebaobao:id/v_family") 
    # 申请家族
    apply_family = (Mb.ID, "com.ourydc.yuebaobao:id/v_family") 
    # 设置
    setUpBtn=(Mb.ID,'com.ourydc.yuebaobao:id/v_setting') 
    

    ############################二级元素#############################
    # 设置
    protector_head = (Mb.ID,'com.ourydc.yuebaobao:id/iv_protector_head') 
    # 编辑资料页我的昵称
    v_nick = (Mb.ID,'com.ourydc.yuebaobao:id/v_nick') 
    # 我的昵称,签名输入框
    et_nick = (Mb.ID,'com.ourydc.yuebaobao:id/et_nick') 
    # 审核中
    it_audit_state = (Mb.ID,'com.ourydc.yuebaobao:id/it_audit_state') 
    # 保存按钮
    tv_save = (Mb.ID,'com.ourydc.yuebaobao:id/tv_save') 
    # 取消按钮
    tv_cancel = (Mb.ID,'com.ourydc.yuebaobao:id/tv_cancel') 
    # 点击我的签名
    v_describe = (Mb.ID,'com.ourydc.yuebaobao:id/v_describe') 


    
    # 我的好友
    # 关注
    tv_title_one = (Mb.ID,'com.ourydc.yuebaobao:id/tv_title_one') 
    # 粉丝
    tv_title_two = (Mb.ID,'com.ourydc.yuebaobao:id/tv_title_two') 
    # 好友
    tv_title_three = (Mb.ID,'com.ourydc.yuebaobao:id/tv_title_three') 
    # 好友
    tv_title_three = (Mb.ID,'com.ourydc.yuebaobao:id/tv_title_three') 
    # 关注列表、粉丝列表、好友列表通用
    avatar = (Mb.ID,'com.ourydc.yuebaobao:id/avatar') 
    


    # 谁看过我列表元素
    iv_head = (Mb.ID,'com.ourydc.yuebaobao:id/iv_head') 
    # 派对足迹
    iv_room_head = (Mb.ID,'com.ourydc.yuebaobao:id/iv_room_head') 


