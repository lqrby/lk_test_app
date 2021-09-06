from appium.webdriver.common.mobileby import MobileBy as Mb

'''设置的页面元素'''


class SetPageLocator:
    #     点击我的
    click_my = (Mb.ID, "com.asiainno.uplive:id/layoutProfile")
    #     点击设置
    click_set = (Mb.ID, "com.asiainno.uplive:id/layoutProfileSettings")
    # 点击返回
    click_back = (Mb.CLASS_NAME, "android.widget.ImageButton")

    '''-----------------------------账号绑定页面元素-----------------------------------------------------'''

    # 点击账号绑定
    click_Account_binding = (Mb.ID, "com.asiainno.uplive:id/bindMobileRL")
    #     获取账号绑定title
    get_title = (Mb.XPATH, "//*[contains(@text,'账号绑定')]")

    '''-----------------------------实名绑定页面元素-----------------------------------------------------'''

    # 点击实名认证
    click_real_name = (Mb.ID, "com.asiainno.uplive:id/authenticationRL")
    #     输入姓名：
    input_name = (Mb.ID, "com.asiainno.uplive:id/etRealName")
    # 点击开始认证
    click_authentication = (Mb.ID, "com.asiainno.uplive:id/btnCommit")
    #     输入身份证
    input_number = (Mb.ID, "com.asiainno.uplive:id/etIDNumber")
    #     输入错误的身份证获取页面内容
    get_text = (Mb.XPATH, "//*[@text='身份验证失败']")

    '''-----------------------------我的直播标签页面元素-----------------------------------------------------'''

    #     点击我的直播标签
    click_lable = (Mb.ID, "com.asiainno.uplive:id/layoutLabel")
    # 点击乖巧可爱
    click_cute = (Mb.XPATH, "//*[@text='乖巧可爱']")
    # 点击声音恋人
    click_Sound_lovers = (Mb.XPATH, "//*[@text='声音恋人']")
    #     点击保存
    click_save = (Mb.ID, "com.asiainno.uplive:id/tv_right")

    '''-----------------------------黑名单页面元素-----------------------------------------------------'''

    #     点击黑名单
    click_blacklist = (Mb.ID, "com.asiainno.uplive:id/layoutBlock")
    #     进入模块成功，获取文本
    get_text_blacklist = (Mb.XPATH, "//*[@text='暂无被拉黑用户']")

    '''-----------------------------消息提醒设置页面元素-----------------------------------------------------'''

    # 点击消息提醒
    click_message = (Mb.ID, "com.asiainno.uplive:id/notificationSettingsRL")
    #     点击主播推送消息
    click_host_to_push = (Mb.ID, "com.asiainno.uplive:id/pushSwitch")
    #     点击消息免打扰
    click_No_disturbing = (Mb.ID, "com.asiainno.uplive:id/dontDisturbSwitch")
    #     点击动态评论消息提醒
    click_dynamic = (Mb.ID, "com.asiainno.uplive:id/feedMessageSwitch")
    #     点击用户聊天消息免打扰
    click_user_to_chat = (Mb.ID, "com.asiainno.uplive:id/imNotificationSwitch")
    # 点击邀请入群确认
    click_invite = (Mb.ID, "com.asiainno.uplive:id/imGroupInvitationSwitch")
    #    点击游戏消息提醒
    click_game = (Mb.ID, "com.asiainno.uplive:id/gameNotificationSwitch")
    # 按钮关闭
    Button_closure = (Mb.XPATH, "//*[@text='开启']")
    #     按钮开启
    Button_open = (Mb.XPATH, "//*[@text='关闭']")

    '''-----------------------------隐私设置页面元素-----------------------------------------------------'''

    #     点击隐私设置
    click_privacy = (Mb.ID, "com.asiainno.uplive:id/privacySettingsRL")
    #     点击查看你的fa谁在up直播
    click_facebook = (Mb.ID, "com.asiainno.uplive:id/scFb")
    # 点击通讯录按钮
    click_address = (Mb.ID, "com.asiainno.uplive:id/scContacts")
    #     点击显示距离
    click_distance = (Mb.ID, "com.asiainno.uplive:id/privacyLocationSwitch")
    #     显示定位
    click_location = (Mb.ID, "com.asiainno.uplive:id/locationSwitch")
    # 按钮开关
    privacy_Button_closure = (Mb.XPATH, "//*[@text='开启']")
    #     按钮开启
    privacy_Button_open = (Mb.XPATH, "//*[@text='关闭']")

    '''-----------------------------礼物设置页面元素-----------------------------------------------------'''

    click_gift = (Mb.ID, "com.asiainno.uplive:id/giftSettingRL")
    #     点击直播间礼物公共
    click_direct_broadcasting = (Mb.ID, "com.asiainno.uplive:id/myMarqueeSwitch")
    #     点击礼物特效开关
    click_effects = (Mb.ID, "com.asiainno.uplive:id/giftSwitch")
    # 按钮开关
    gift_Button_closure = (Mb.XPATH, "//*[@text='开启']")
    #     按钮开启
    gift_Button_open = (Mb.XPATH, "//*[@text='关闭']")
    '''    ----------------------------- 其他按钮----------------------------------------------------'''
    # 悬浮窗播放开关
    floatWindowSwitch = (Mb.ID, "com.asiainno.uplive:id/floatWindowSwitch")
    # 设备性能优化开关
    broadcastHardwareSwitch = (Mb.ID, "com.asiainno.uplive:id/broadcastHardwareSwitch")
    # 关于Up直播
    aboutRL = (Mb.ID, "com.asiainno.uplive:id/aboutRL")
    # 关于Up直播页面title
    toolbar_title = (Mb.ID, "com.asiainno.uplive:id/toolbar_title")

