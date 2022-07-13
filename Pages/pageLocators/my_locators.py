from appium.webdriver.common.mobileby import MobileBy as Mb


class MyLocators:

    #=================我的一级页面元素===========
    # 【我的】模块按钮元素
    meBtn=(Mb.ID,'com.ourydc.yuebaobao:id/iv_tab_mine') 
    #用户靓号id
    tv_identity = (Mb.ID,"com.ourydc.yuebaobao:id/tv_identity")
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
    '''充值'''
    # 充值
    iv_recharge = (Mb.ID, "com.ourydc.yuebaobao:id/iv_recharge")
    #钻石
    diamonds = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='钻石']") 
    #宝石
    gemstone = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='宝石']") 
    #金币
    gold_coins = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='金币']") 
    #钻石数量
    diamond_quantity = (Mb.ID, "com.ourydc.yuebaobao:id/tv_my_balance")
    #金币数量
    itv_gold = (Mb.ID, "com.ourydc.yuebaobao:id/itv_gold")
    #微信支付选项
    pay_wx = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/pay_tv' and @text='微信']")
    #支付宝选项
    pay_zfb = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/pay_tv' and @text='支付宝']")
    
    # layout_pay_alipay = (Mb.ID, "com.ourydc.yuebaobao:id/layout_pay_alipay")
    #充值档位
    recharge_gear = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/layout_recharge_item']") 
    #首充特惠
    first_charge_special = (Mb.ID, "com.ourydc.yuebaobao:id/iv_max_first_recharge")
    #在线客服
    online_service = (Mb.ID, "com.ourydc.yuebaobao:id/tv_helper")
    #在线客服2
    online_service2 = (Mb.XPATH, "//*[@class='android.view.View' and @text='在线客服']")
    #充值按钮
    recharge_button = (Mb.ID, "com.ourydc.yuebaobao:id/btn_recharge")
    #开具发票按钮
    invoice = (Mb.ID, "com.ourydc.yuebaobao:id/tv_invoice")
    #断言公司税号
    duty_paragraph = (Mb.XPATH, "//*[@class='android.view.View' and @text='公司税号']")
    #开票说明
    billing_description = (Mb.XPATH, "//*[@class='android.view.View' and @text='《开票说明》']")
    #发票说明-在线客服-客服昵称
    kefu_nick = (Mb.ID,'com.ourydc.yuebaobao:id/tv_nick_name')
    #开票记录
    invoicing_record = (Mb.XPATH,"//*[@class='android.view.View' and @text='开票记录']")
    
    #金币收入支出记录列表
    tv_count = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_count']") 
    #消费记录列表
    tv_money = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_money']") 
    #筛选选项
    tv_content = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content']") 
    #聊天输入框
    editTextMessage = (Mb.ID, "com.ourydc.yuebaobao:id/editTextMessage") #聊天输入框
    #哩咔每日签到标题
    mrqd_title = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_title' and @text='每日签到']") 
    
    #查看全部
    tv_see_all = (Mb.ID, "com.ourydc.yuebaobao:id/tv_see_all")
    
    #赚取金币
    btn_get_gold = (Mb.ID, "com.ourydc.yuebaobao:id/btn_get_gold")
    #立即签到、放入背包
    sign_in = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/button']") 
    #使用金币tap
    use_gold_coins = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='使用金币']") 
    #首充特惠
    scth_title = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_title' and @text='首充特惠']")
    #聊天页-心动
    tv_desc = (Mb.ID, "com.ourydc.yuebaobao:id/tv_desc")
    #点此处邀他玩-互动游戏
    interactive_games = ("//*[@class='android.widget.TextView' and @text='点此处邀ta玩「互动游戏」']")

    '''end'''
    # 商城
    iv_dress_store = (Mb.ID, "com.ourydc.yuebaobao:id/iv_dress_store")


    '''# 收入'''
    my_income= (Mb.ID, "com.ourydc.yuebaobao:id/iv_mine_income")
    # 宝宝币、游戏币、魅力值数量
    # bbbNumber = (Mb.ID, "com.ourydc.yuebaobao:id/tv_count")
    bbbNumber = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_count']") 
    # 宝宝币兑换钻石按钮
    exchange_diamonds = (Mb.ID,"com.ourydc.yuebaobao:id/iv_exchange_money")
    # 魅力值兑换按钮
    charm_value_exchange = (Mb.ID,"com.ourydc.yuebaobao:id/tv_exchange_money")
    # 宝宝币兑换说明按钮
    exchange_instructions = (Mb.ID,"com.ourydc.yuebaobao:id/iv_income_problem")
    #全部兑换按钮
    all_exchange = (Mb.ID,"com.ourydc.yuebaobao:id/tv_take_all")
    #兑换数量输入框
    et_input = (Mb.ID,"com.ourydc.yuebaobao:id/et_input")
    #兑换按钮
    tv_shift_to = (Mb.ID,"com.ourydc.yuebaobao:id/tv_shift_to")
    #再次确认按钮
    tv_confirm = (Mb.ID,"com.ourydc.yuebaobao:id/tv_confirm")
    #提现按钮
    btn_withdraw = (Mb.ID,"com.ourydc.yuebaobao:id/btn_withdraw")
    #身份证号码
    card_no = (Mb.XPATH,"//*[@class='android.view.View' and @text='身份证号码']") 
    #开户银行
    deposit_bank = (Mb.XPATH, "//*[@class='android.view.View' and @text='开户银行']") 
    #下一步
    nex_setp = (Mb.XPATH,"//*[@class='android.view.View' and @text='下一步']") 
    # 服务协议
    service_agreement = (Mb.XPATH, "//*[@class='android.view.View' and @text='《服务协议》']") 
    # 费用结算协议
    jsxy = (Mb.XPATH,"//*[@class='android.view.View' and @text='\"云账户\"费用结算服务协议']") 
    # 自由职业协议
    zyxy = (Mb.XPATH,"//*[@class='android.view.View' and @text='自由职业者服务协议']") 
    # 提现记录按钮/查看明细
    Withdrawal_record = (Mb.ID, "com.ourydc.yuebaobao:id/tv_right") 
    # 提现记录列表
    record_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/layout_withdraw_diamond']") 
    # 兑换钻石成功
    tv_withdraw_status = (Mb.ID, "com.ourydc.yuebaobao:id/tv_withdraw_status") 
    # 兑换钻石数量
    layout_withdraw_actual = (Mb.ID, "com.ourydc.yuebaobao:id/layout_withdraw_actual") 
    # 游戏币tap
    yxbtap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='游戏币']") 
    # 魅力值tap
    mlztap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='魅力值']") 
    # 宝宝币tap
    bbbTap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='宝宝币']")
    

    '''end''' 

    '''vip会员'''
    # 会员
    iv_vip = (Mb.ID, "com.ourydc.yuebaobao:id/iv_vip")
    #立即续费/立享特权
    ndzsbs = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='年费专属标识']") 
    #会员标识
    hybs = (Mb.XPATH, "//*[@class='android.view.View' and @text='会员标识']") 
    #专属装扮
    zszb = (Mb.XPATH, "//*[@class='android.view.View' and @text='专属装扮']") 
    #充值档位1
    gear = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/root']") 
    #再想想
    zxx = (Mb.XPATH, "//*[@class='android.view.View' and @text='再想想']") 
    #充值档位2
    gear_two = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/priceTv' and @text='12个月  ¥14.0/月']") 
    #更多支付
    morePayWayLay = (Mb.ID, 'com.ourydc.yuebaobao:id/morePayWayLay') 
    #微信支付
    weixin = (Mb.ID, 'com.ourydc.yuebaobao:id/payWayLay1') 
    #支付宝支付
    payWayLay = (Mb.ID, 'com.ourydc.yuebaobao:id/payWayLay2') 
    #支付
    # payment = (Mb.ID, 'com.ourydc.yuebaobao:id/payTv') 
    payment = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/sendPayTv' and @text='立即支付']") 
    #赠送
    give = (Mb.ID, 'com.ourydc.yuebaobao:id/sendTv') 
    #会员协议
    membership_agreement = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/agreementTv' and @text='2.成为会员即表示同意《哩咔会员协议》']") 
    #赠送好友
    gift_friends = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/sendFriendTv' and @text='赠送好友']") 
    #选择好友
    select_friends = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/cb']") 
    #确定（选择好友的确定按钮）
    confirmOK = (Mb.ID, "com.ourydc.yuebaobao:id/tv_extra")
    #用户id号
    sendIdTv = (Mb.ID, "com.ourydc.yuebaobao:id/sendIdTv")
    #确定支付
    tv_sure = (Mb.ID, "com.ourydc.yuebaobao:id/tv_sure")
    #续年费
    xf = (Mb.XPATH, "//*[@class='android.view.View' and @text='   续费 >  ']")
    #开年费
    knf = (Mb.XPATH, "//*[@class='android.view.View' and @text='开年费，更优惠 ! >']")
    #续年费
    xnfgyh = (Mb.XPATH, "//*[@class='android.view.View' and @text='	续年费，更优惠!>  ']")
    #续年费
    xnfhy = (Mb.XPATH, "//*[@class='android.view.View' and @text='续年费会员，每日仅需0.47元']")
    '''end'''
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
    
    free_barrage = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='免费弹幕']")
    list_stealth = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='榜单隐身']")
    anchor_level = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='主播等级']")
    begin_to_show = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='开播']")
    wish = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='心愿']")
    zhujianPK = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='PK']")
    rank = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='爵位等级']")
    count = (Mb.XPATH,"//*[@class='android.view.View' and @content-desc='含充值金额50元']")
    explain = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='说明']")
    VIP_dj = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='VIP等级']")



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

    # # #立即签到
    # sign_in = (Mb.ID, "com.ourydc.yuebaobao:id/button")

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
    set_payment_password = (Mb.ID,'com.ourydc.yuebaobao:id/layout_pay_pwd') #设置支付密码
    layout_black_list = (Mb.ID,'com.ourydc.yuebaobao:id/layout_black_list') #黑名单
    blacklist_no_data = (Mb.ID,'com.ourydc.yuebaobao:id/tv_empty_text') #黑名单页面无数据
    blacklist_data = (Mb.ID,'com.ourydc.yuebaobao:id/iv_head_view') #黑名单页面有数据
    cancel_account = (Mb.ID,'com.ourydc.yuebaobao:id/layout_account_unregister') #注销账号
    protection_of_no = (Mb.ID,'com.ourydc.yuebaobao:id/layout_child_model') #未成年人保护模式开关
    protection_of_minors = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_title_text' and @text='未成年人保护模式']") #未成年人保护模式
    on_state = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/layout_child_model']//node()[contains(@resource-id,'com.ourydc.yuebaobao:id/tv_content')]")
    turn_on_protection = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn_open' and @text='开启保护模式']") #开启保护模式
    password_input = (Mb.ID,'com.ourydc.yuebaobao:id/password_1') #密码输入框
    confirm_password_input = (Mb.ID,'com.ourydc.yuebaobao:id/password_2') #确认密码输入框
    confirm_button = (Mb.ID, "com.ourydc.yuebaobao:id/btn_sure") #确定按钮
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
    recharge_consumption = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='充值&消费']") 
    #提现
    withdrawal = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='提现']") 
    #聊天室
    chat_room = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='聊天室']") 
    #订单
    order = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='订单']") 
    #家族问题
    family_problems = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='家族问题']") 
    #账号
    account_number = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='账号']") 
    #会员/爵位/守护
    membership_title = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='会员/爵位/守护']") 
    #违规、封号、举报
    reporting_seal = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='违规、封号、举报']") 
    #其他
    other = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='其他']") 

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
    iv_extra = (Mb.ID,'com.ourydc.yuebaobao:id/iv_extra') #发布按钮/筛选按钮
    deleteButton = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv' and @text='删除']") #删除按钮
    zuojia = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='座驾']") #商城》装扮》座驾
    qipao = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='气泡']") #商城》装扮》气泡
    vipzs = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='VIP专属']") #商城》VIP专属
    jifen = (Mb.XPATH, "//*[@class='android.view.View' and @text=contains(text(),'积分')]") #商城》VIP专属》积分
    dhjl = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='兑换记录']") #商城》VIP专属》兑换记录
    xhjf = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='消耗积分']") #商城》VIP专属》兑换记录》消耗积分
    shuoming = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='说明']") #商城》VIP专属》说明
    jrsx = (Mb.XPATH, "//*[@class='android.view.View' and @content-desc='说明']") #商城》VIP专属》今日寿星
    