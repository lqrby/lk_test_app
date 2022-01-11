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
    reward_center = (Mb.ID, "com.ourydc.yuebaobao:id/v_rewards") 
    # 游戏大厅
    game_hall = (Mb.ID, "com.ourydc.yuebaobao:id/v_game_layout")
    # 我的等级
    my_level = (Mb.ID, "com.ourydc.yuebaobao:id/v_vip_level")
    # 活动中心
    activity_center = (Mb.ID, "com.ourydc.yuebaobao:id/v_activity") 
    # 申请家族
    apply_family = (Mb.ID, "com.ourydc.yuebaobao:id/v_family") 
    # 设置
    setUpBtn=(Mb.ID,'com.ourydc.yuebaobao:id/v_setting') 
    

    ############################二级元素#############################
    # 设置
    protector_head = (Mb.ID,'com.ourydc.yuebaobao:id/iv_protector_head') 
    
    # 编辑资料页我的昵称
    v_nick = (Mb.ID,'com.ourydc.yuebaobao:id/v_nick')  
    nick_name_text = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/v_nick']/child::com.ourydc.yuebaobao:id/tv_content")
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
    # 派对足迹列表
    iv_room_head = (Mb.ID,'com.ourydc.yuebaobao:id/iv_room_head') 



    # 我的动态
    #我的动态列表
    # my_dynamic_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv']/child::android.view.ViewGroup")
    my_dynamic_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_msg']")
    tv_read_count = (Mb.ID,'com.ourydc.yuebaobao:id/tv_read_count') #阅读数量
    comment_input = (Mb.ID,'com.ourydc.yuebaobao:id/et_comment') #评论输入框
    sendButton = (Mb.ID,'com.ourydc.yuebaobao:id/btn_comment') #发送按钮



    #我的背包
    all_gifts_list = (Mb.ID,'com.ourydc.yuebaobao:id/cl') #全部礼物列表
    all_gifts = (Mb.ID,'com.ourydc.yuebaobao:id/layout_msg_panel_red_outer') #背包tap下礼物列表
    use_now = (Mb.ID,'com.ourydc.yuebaobao:id/tv_btn4') #立即使用
    gifts_list = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='礼物']")
    prop_list = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='道具']")
    decorate_list = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='装饰']")
    sweet_flower = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gift_name' and @text='甜蜜小花']")
    

    # 奖励中心
    receive_an_award = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn_action' and @text='领奖']") #领奖按钮
    receive = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn' and @text='领取']") #领取按钮
    receive_ok = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn' and @text='确定']") #领取按钮
    onlineRecycle = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/onlineRecycle']/child::android.view.ViewGroup") #已上线

    # #立即签到
    sign_in = (Mb.ID, "com.ourydc.yuebaobao:id/button")

    #活动中心
    imageView7 = (Mb.ID,'com.ourydc.yuebaobao:id/imageView7') #活动中心游戏列表

    #申请家族
    application_family = (Mb.XPATH, "//*[@class='android.widget.ListView']/child::android.view.View")
    
    # 设置
    account_and_security = (Mb.ID,'com.ourydc.yuebaobao:id/layout_account_security') #账号与安全
    '''二级元素'''
    layout_bind_phone = (Mb.ID,'com.ourydc.yuebaobao:id/layout_bind_phone') #修改绑定手机
    changePhoneBtn = (Mb.ID,'com.ourydc.yuebaobao:id/changePhoneBtn') #更换绑定手机号
    get_verification_code = (Mb.ID,'com.ourydc.yuebaobao:id/tv_get_validate') #获取验证码
    bound_wechat = (Mb.ID,'com.ourydc.yuebaobao:id/layout_reset_third_login') #已绑定微信
    set_password = (Mb.ID,'com.ourydc.yuebaobao:id/layout_reset_password') #设置密码
    identity_authentication = (Mb.ID,'com.ourydc.yuebaobao:id/layout_identity_attestation') #身份认证
    bind_official_account = (Mb.ID,'com.ourydc.yuebaobao:id/layout_bind_wechat') #绑定公众号
    rl_root = (Mb.ID,'com.ourydc.yuebaobao:id/rl_root') #绑定公众号title
    # official_account_text = (Mb.XPATH,"//*[@class='android.view.View' and @text='第一步：关注公众号']") #绑定公众号断言
    set_payment_password = (Mb.ID,'com.ourydc.yuebaobao:id/layout_pay_pwd') #设置支付密码
    layout_black_list = (Mb.ID,'com.ourydc.yuebaobao:id/layout_black_list') #黑名单
    blacklist_no_data = (Mb.ID,'com.ourydc.yuebaobao:id/tv_empty_text') #黑名单页面无数据
    blacklist_data = (Mb.ID,'com.ourydc.yuebaobao:id/iv_head_view') #黑名单页面有数据
    cancel_account = (Mb.ID,'com.ourydc.yuebaobao:id/layout_account_unregister') #注销账号
    protection_of_minors = (Mb.ID,'com.ourydc.yuebaobao:id/layout_child_model') #未成年人保护模式
    # on_state = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/layout_child_model']/child::com.ourydc.yuebaobao:id/tv_content")
    on_state = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/layout_child_model']//node()[contains(@resource-id,'com.ourydc.yuebaobao:id/tv_content')]")
    turn_on_protection = (Mb.ID,'com.ourydc.yuebaobao:id/btn_open') #开启保护模式
    password_input = (Mb.ID,'com.ourydc.yuebaobao:id/password_1') #密码输入框
    confirm_password_input = (Mb.ID,'com.ourydc.yuebaobao:id/password_2') #确认密码输入框
    confirm_button = (Mb.ID, "com.ourydc.yuebaobao:id/btn_sure") #确定按钮
    # confirm_button = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn_sure' and @text='确定']") #确定按钮
    turn_off_protection = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn_open' and @text='关闭保护模式']") #关闭保护模式
    message_settings = (Mb.ID,'com.ourydc.yuebaobao:id/layout_msg_setting') #消息设置
    currency = (Mb.ID,'com.ourydc.yuebaobao:id/layout_common_use') #通用
    cash_capacity_management = (Mb.ID,'com.ourydc.yuebaobao:id/layout_money_setting') #钞能力管理
    speed_chat_room = (Mb.ID,'com.ourydc.yuebaobao:id/conciseLayout') #聊天室极速模式
    about_lika = (Mb.ID,'com.ourydc.yuebaobao:id/layout_about_lika') #关于哩咔
    #检查更新
    checkVersion= (Mb.ID,'com.ourydc.yuebaobao:id/layout_checkVersion') 
    #立即更新
    btn_confirm = (Mb.ID, "com.ourydc.yuebaobao:id/btn_confirm")
    #稍后更新
    update_later = (Mb.ID, "com.ourydc.yuebaobao:id/tv_cancel")
    #隐私政策
    layout_privacy = (Mb.ID,'com.ourydc.yuebaobao:id/layout_privacy') 
    #帮助中心
    layout_helper = (Mb.ID,'com.ourydc.yuebaobao:id/layout_helper') 
    #充值&消费
    recharge_consumption = (Mb.XPATH, "//*[@class='android.view.View' and @text='充值&消费']") 
    #提现
    withdrawal = (Mb.XPATH, "//*[@class='android.view.View' and @text='提现']") 
    #聊天室
    chat_room = (Mb.XPATH, "//*[@class='android.view.View' and @text='聊天室']") 
    #订单
    order = (Mb.XPATH, "//*[@class='android.view.View' and @text='订单']") 
    #家族问题
    family_problems = (Mb.XPATH, "//*[@class='android.view.View' and @text='家族问题']") 
    #账号
    account_number = (Mb.XPATH, "//*[@class='android.view.View' and @text='账号']") 
    #会员/爵位/守护
    membership_title = (Mb.XPATH, "//*[@class='android.view.View' and @text='会员/爵位/守护']") 
    #违规、封号、举报
    reporting_seal = (Mb.XPATH, "//*[@class='android.view.View' and @text='违规、封号、举报']") 
    #其他
    other = (Mb.XPATH, "//*[@class='android.view.View' and @text='其他']") 

    problem_classification = [(recharge_consumption,"充值&消费"),(withdrawal,"提现"),(chat_room,"聊天室"),(order,"订单"),(family_problems,"家族问题"),
        (account_number,"账号"),(membership_title,"会员/爵位/守护"),(reporting_seal,"违规、封号、举报"),(other,"其他")]

    #分类列表
    classification_list = (Mb.XPATH, "//*[@class='android.view.View' and @index='1']") 
    #意见反馈
    layout_feedback = (Mb.ID,'com.ourydc.yuebaobao:id/layout_feedback') 
    #关于我们
    layout_about = (Mb.ID,'com.ourydc.yuebaobao:id/layout_about') 
    
    tv_nick_name = (Mb.ID,'com.ourydc.yuebaobao:id/tv_nick_name') #我的昵称
    btn_submit = (Mb.ID,'com.ourydc.yuebaobao:id/btn_submit') #去发布动态按钮
    et_content = (Mb.ID,'com.ourydc.yuebaobao:id/et_content') #动态输入框
    iv_extra = (Mb.ID,'com.ourydc.yuebaobao:id/iv_extra') #发布按钮
    deleteButton = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv' and @text='删除']") #删除按钮
    zuojia = (Mb.XPATH, "//*[@class='android.view.View' and @text='座驾']") #商城》装扮》座驾
    qipao = (Mb.XPATH, "//*[@class='android.view.View' and @text='气泡']") #商城》装扮》气泡
    vipzs = (Mb.XPATH, "//*[@class='android.view.View' and @text='VIP专属']") #商城》VIP专属
    jifen = (Mb.XPATH, "//*[@class='android.view.View' and @text=contains(text(),'积分')]") #商城》VIP专属》积分
    dhjl = (Mb.XPATH, "//*[@class='android.view.View' and @text='兑换记录']") #商城》VIP专属》兑换记录
    xhjf = (Mb.XPATH, "//*[@class='android.view.View' and @text='消耗积分']") #商城》VIP专属》兑换记录》消耗积分
    shuoming = (Mb.XPATH, "//*[@class='android.view.View' and @text='说明']") #商城》VIP专属》说明
    jrsx = (Mb.XPATH, "//*[@class='android.view.View' and @text='说明']") #商城》VIP专属》今日寿星
    