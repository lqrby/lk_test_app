'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-11-02 10:37:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/room_locator.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb

'''首页的页面元素'''


class RoomPageLocator:
    ##################################公共元素######################################
    #确定关闭按钮
    close_ok = (Mb.ID,'com.ourydc.yuebaobao:id/tv_sure') 
    # 取消按钮
    cancel_btn = (Mb.ID, "com.ourydc.yuebaobao:id/tv_cancel") 
    give_up_reward = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='放弃奖励']")



    # 设置未成年人保护弹窗
    btn_know = (Mb.ID, "com.ourydc.yuebaobao:id/btn_iknow")
    # 关闭女神开播引导弹窗按钮
    close_back = (Mb.ID, "com.ourydc.yuebaobao:id/back") 
    #聊天室已关闭
    close_broadcast = (Mb.ID, "com.ourydc.yuebaobao:id/iv_finish_close") 
    
    

    ###########################哩咔首页交友模块元素定位结束##########################
    tv_play = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_play']") # 发现-进入聊天室的用户列表元素
    tv_close = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/des']") # 发现-用户未进聊天室列表元素
    layout_info = (Mb.XPATH, "//*[@class='android.widget.LinearLayout' and @resource-id='com.ourydc.yuebaobao:id/layout_info']") # 发现-用户未进聊天室列表元素-带语音
    
    
    
    no_more = (Mb.ID, "com.ourydc.yuebaobao:id/load_more_load_end_view") # 主播列表底部的没有更多按钮元素
    roomIdTv = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/roomIdTv']") # 获取开播房间的id
    ignore1 = (Mb.ID, "//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/ignore1']") # 获取开播房间的id
    # no_one_nearby = (Mb.ID, "com.ourydc.yuebaobao:id/tv_empty_text") # 获取附近的人列表、派对聊天室列表、守护榜列表为空元素
   



    ###########################房间模块下的元素############################
    # 房间模块
    room_module = (Mb.ID, 'com.ourydc.yuebaobao:id/iv_tab_live') 
    #房间列表元素（聊天室通用元素）
    '''list列表面类型元素'''
    # 房间list
    room_list = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/tv_charroom_label']") 
    #聊天室列表
    chat_room_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/layout_chat_room_enter_round'][not(.//@resource-id='com.ourydc.yuebaobao:id/iv_lock')]") 
    
    
    def get_goddess_type(number):
        goddessType = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/tv_charroom_label' and @index='{}']".format(number)) 
        return goddessType
    
    # 密码房间输入框
    room_text = (Mb.ID, 'com.ourydc.yuebaobao:id/container_et') 
    closeRoomText = (Mb.ID, 'com.ourydc.yuebaobao:id/iv_close') 
    iv_lock = (Mb.ID, 'com.ourydc.yuebaobao:id/iv_lock') 
    





    #------创建聊天室------

    #创建聊天室按钮
    menuIv = (Mb.ID, "com.ourydc.yuebaobao:id/menuIv") 
    #房间类型
    room_type = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rv']/child::android.view.ViewGroup") 
    #==================小窝类型，萌新接待=====================
    #房间标签
    room_label = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rv_label']/child::android.view.ViewGroup") 
    #房间话题
    room_name = (Mb.ID, "com.ourydc.yuebaobao:id/et_tag") 
    #换一换房间话题
    room_name_refresh = (Mb.ID, "com.ourydc.yuebaobao:id/tv_tag_refresh") 
    #房间座位
    room_seat = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv_seat_num']/child::android.view.ViewGroup") 
    #进入房间按钮
    entry_room = (Mb.ID, "com.ourydc.yuebaobao:id/btn_enter") 
    # #创建房间id，断言使用
    # room_id = (Mb.ID, "com.ourydc.yuebaobao:id/tv_title_desc") 
    layout_room_info_top = (Mb.ID, "com.ourydc.yuebaobao:id/layout_room_info_top") 
    
    '''
    房间tap页元素
    '''
    # 关注tap
    follow_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='关注']") 
    # 推荐tap
    recommend_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='推荐']") 
    # 派对tap
    party_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='派对']") 
    # 扩列tap
    Expansion_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='扩列']") 
    # 开黑
    open_black_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='开黑']") 
    # 萌新接待tap
    reception_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='萌新接待']")
    # 速配tap
    speed_dating_tap = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='速配']") 
    

    
    
    #女神天团标识
    goddess_logo = (Mb.ID, "com.ourydc.yuebaobao:id/svg_chat_room_top") 
    	


    '''房间内部元素'''
    goddess_type = (Mb.ID, "com.ourydc.yuebaobao:id/iv_check_all") # 全麦
    masterAvatarView = (Mb.ID,'com.ourydc.yuebaobao:id/masterAvatarView') #礼物入口弹框1
    v_empty_avatar = (Mb.ID,'com.ourydc.yuebaobao:id/v_empty_avatar') #礼物入口弹框(不同)
    tv_heat = (Mb.ID,'com.ourydc.yuebaobao:id/tv_heat') # 房间热度值2
    follow = (Mb.ID,'com.ourydc.yuebaobao:id/attentionIv') # 关注
    ranking_kuoLie = (Mb.ID,'com.ourydc.yuebaobao:id/layout_chat_room_income') #扩列-排行榜
    ranking_list = (Mb.ID,'com.ourydc.yuebaobao:id/rv_top') #排行榜3
    head_picture = (Mb.ID,'com.ourydc.yuebaobao:id/iv_master_head') #萌新接待聊天室头像
    
    #《排行榜-3》
    contribution_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='贡献榜']") # 贡献榜
    popularity_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='人气榜']") # 人气榜
    guardian_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='守护榜']") # 守护榜
    phb_group = [ranking_list,popularity_list,guardian_list]	
    tv_title_ri = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='日榜']") # 日榜	
    tv_title_week = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='周榜']") # 周榜	
    tv_title_yue = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='月榜']") # 月榜	
    day_week_month_assert2 = (Mb.XPATH,"//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/lottie_border']") #守护榜断言
    
    day_week_month_assert = (Mb.XPATH,"//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/iv_avatar']") #贡献榜、人气榜断言
    # day_week_month_assert = (Mb.XPATH,"//*[@class='android.view.ViewGroup']") #排行榜公共断言-有数据
    	
    #菜单4
    room_menu = (Mb.ID,'com.ourydc.yuebaobao:id/menu') 
    #房间菜单元素list元素(最小化、关闭房间、更多分享、分享微信、qq、微博)
    room_menu_btn = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/gv']/child::android.widget.RelativeLayout")	
    
    tv_introduce = (Mb.ID,'com.ourydc.yuebaobao:id/tv_introduce') #推荐--玩法介绍5
    tv_introduce_assert = (Mb.ID,'com.ourydc.yuebaobao:id/contentTv') #推荐--玩法介绍断言
    
    closeIv = (Mb.ID,'com.ourydc.yuebaobao:id/closeIv') #关闭玩法介绍
    #麦下
    layout_people = (Mb.ID,'com.ourydc.yuebaobao:id/layout_people') #麦下6
    iv_head_view = (Mb.ID,'com.ourydc.yuebaobao:id/iv_head_view') #麦下收缩列表ist
                            	
    
    rv = (Mb.ID,'com.ourydc.yuebaobao:id/rv') #点击房间内部用户头像查看用户列表7


    #领取-为ta点赞
    
    receive_identifying = (Mb.ID,'com.ourydc.yuebaobao:id/layout_task') #领取标识
    receive = (Mb.ID,'com.ourydc.yuebaobao:id/iv_receive') #点击房间内领取入口-领取
    count_down_receive = (Mb.ID,'com.ourydc.yuebaobao:id/tv_task_countdown') #点击房间内领取入口-倒计时
    for_her = (Mb.ID,'com.ourydc.yuebaobao:id/iv_light_up') #为ta点亮tap
    sign_in = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_desc' and (@text='签到' or @text='领取')]") # 签到/领取
    # sign_in = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_desc']") # 签到/领取
    # receiveList = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/rv_task']/child::android.view.ViewGroup") # 签到、领取气泡
    receiveBtn = (Mb.XPATH,"//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/iv_reward' and @index='2']") # 领取按钮
    play_instructions = (Mb.ID,'com.ourydc.yuebaobao:id/iv_description') #玩法说明

    #领取-抽奖
    luck_draw = (Mb.ID,'com.ourydc.yuebaobao:id/iv_lottery') # 抽奖tap
    
    lucky_text = (Mb.XPATH,"//*[@class='android.view.View' and @text='幸运之神眷顾着您！']") # 幸运之神眷顾着您！
    okBtn = (Mb.XPATH,"//*[@class='android.view.View' and @text='确定']") # 确定
    smoke_again = (Mb.XPATH,"//*[@class='android.view.View' and @text='再抽一次']") # 再抽一次
     

    #福袋
    # blessing_bag = (Mb.ID,'com.ourydc.yuebaobao:id/vp_chat_room_party') #点击房间内幸运福袋入口
    
    
    #=======页面底部按钮========
    # 开黑tay-聊天室-创建团队
    tv_create = (Mb.ID,'com.ourydc.yuebaobao:id/tv_create') #创建按钮
    spinner_mode = (Mb.ID,'com.ourydc.yuebaobao:id/spinner_mode') #模式选择下拉菜单按钮
    spinner_dw = (Mb.ID,'com.ourydc.yuebaobao:id/spinner_dw') #段位选择下拉菜单按钮
    et_desc = (Mb.ID,'com.ourydc.yuebaobao:id/et_desc') #要求输入框
    rv_reward = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rv_reward']/child::android.view.ViewGroup") # 悬赏list
    btn_create = (Mb.ID,'com.ourydc.yuebaobao:id/btn_create') #创建队伍确定按钮
    create_assert = (Mb.ID,'com.ourydc.yuebaobao:id/layout_gangup_squad') #创建队伍断言
    mantle = (Mb.ID,'com.ourydc.yuebaobao:id/rv_chat_room_msg') #蒙层元素
    
    # 开黑tay-聊天室-发车
    tv_departure = (Mb.ID,'com.ourydc.yuebaobao:id/tv_departure') #发车
    tv_disband = (Mb.ID,'com.ourydc.yuebaobao:id/tv_disband') # 解散

    # 开黑tay-聊天室-队列
    tv_queue = (Mb.ID,'com.ourydc.yuebaobao:id/tv_queue') #队列按钮
    iv_join = (Mb.ID,'com.ourydc.yuebaobao:id/iv_join') #连麦按钮

    findBtn = (Mb.ID,'com.ourydc.yuebaobao:id/iv_sel') #发现按钮
    
    layout_input_msg = (Mb.ID,'com.ourydc.yuebaobao:id/layout_input_msg') #表情
    iv_send_text = (Mb.ID,'com.ourydc.yuebaobao:id/iv_send_text') #input,聊天入口（来聊天啊）

    iv_more = (Mb.ID,'com.ourydc.yuebaobao:id/iv_more') #更多
    gd_game = (Mb.ID,'com.ourydc.yuebaobao:id/layout_game') #游戏冒险
    iv_game = (Mb.ID,'com.ourydc.yuebaobao:id/iv_game') #游戏入口
    game_assert = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rv']/child::android.view.ViewGroup") # 游戏列表断言	
    game_ymbb = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and text='一毛不拔']") # 断言一毛不拔	
    game_ybzj = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and text='一本正经']") # 断言一本正经

    gig_adventure = (Mb.XPATH, "//*[@class='android.widget.TextView' and text='大冒险']") # 大冒险tap
    wash_and_sing = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and text='边刷牙边唱歌']") # 断言边刷牙边唱歌
    water_reading = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and text='含一口水读绕口令']") # 断言含一口水读绕口令

    mask_message = (Mb.ID,'com.ourydc.yuebaobao:id/layout_shielding_msg') #屏蔽消息
    privilege_card = (Mb.ID,'com.ourydc.yuebaobao:id/layout_privilegecard') #特权卡管理
    red_envelope = (Mb.ID,'com.ourydc.yuebaobao:id/redPackLay') #红包
    total_amount = (Mb.ID, "com.ourydc.yuebaobao:id/tv_monty_desc") # 断言总金额
    count_down = (Mb.ID, "com.ourydc.yuebaobao:id/tv_countdown") # 断言倒计时

    diamond_red_envelope = (Mb.ID, "com.ourydc.yuebaobao:id/tv_redpacket") # 钻石红包tap
    btn_send = (Mb.ID, "com.ourydc.yuebaobao:id/btn_send") # 发送红包按钮
    
    

    task = (Mb.ID,'com.ourydc.yuebaobao:id/taskLay') #任务
    # daily_login = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/title' and text='日常任务']") # 日常任务
    daily_login = (Mb.ID, "com.ourydc.yuebaobao:id/title") # 日常任务
    gold_coin_lucky_draw = (Mb.ID, "com.ourydc.yuebaobao:id/luckyDrawTv") # 金币抽奖
    receive_button = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/btn' and @text='领取']") # 领取按钮
    # not_claimed = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/btn' and text='未领取']") # 未领取按钮
    task_description = (Mb.ID, "com.ourydc.yuebaobao:id/taskInstructions") # 任务说明
    collectable = (Mb.ID, "@resource-id='com.ourydc.yuebaobao:id/lightIv") # 可领取奖品
    claim_button = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/lightIv']") # 领奖按钮
    invitation = (Mb.ID,'com.ourydc.yuebaobao:id/invitefriends') #邀请
    mixer = (Mb.ID,'com.ourydc.yuebaobao:id/layout_ear_return') #调音台
    iv_msg = (Mb.ID,'com.ourydc.yuebaobao:id/iv_msg') #消息
    msg_input = (Mb.ID,'com.ourydc.yuebaobao:id/editTextMessage') #消息输入框
    send_message = (Mb.ID,'com.ourydc.yuebaobao:id/tv_send_msg') #点击发送按钮
    
    lucky_bag_iv = (Mb.ID,'com.ourydc.yuebaobao:id/lucky_bag_iv') #福袋
    no_hair_message = (Mb.XPATH,"//*[@class='android.view.View' and @text='不发送消息给好友']") # 福袋断言
    
    Lucky_bag = (Mb.ID,'com.ourydc.yuebaobao:id/layout_chat_room_party') #
    cash_back_assert = (Mb.ID,'com.ourydc.yuebaobao:id/layout_web_view') #钻石返现页面断言
    open_black_recharge = (Mb.ID,'com.ourydc.yuebaobao:id/layout_gift') #开黑tap房间礼物入口-底部
    
    #=======================开播房间内元素结束===================

    #个人资料元素定位
    personIdView = (Mb.ID,'com.ourydc.yuebaobao:id/personIdView') #个人id
    nick = (Mb.ID,'com.ourydc.yuebaobao:id/nick') #昵称
    sexAndAge = (Mb.ID,'com.ourydc.yuebaobao:id/sexAndAge') #性别
    locationTv = (Mb.ID,'com.ourydc.yuebaobao:id/locationTv') #位置
    descTv = (Mb.ID,'com.ourydc.yuebaobao:id/descTv') #个性签名
    tv_week_gift_num = (Mb.ID,'com.ourydc.yuebaobao:id/tv_week_gift_num') #本周收到的礼物
    reference = (Mb.ID,'com.ourydc.yuebaobao:id/reference') # @她
    attentionBtn = (Mb.ID,'com.ourydc.yuebaobao:id/attentionBtn') # 关注
    msgBtn = (Mb.ID,'com.ourydc.yuebaobao:id/msgBtn') # 聊天
    backBtn = (Mb.ID,'com.ourydc.yuebaobao:id/iv_back') # 详情页返回
    msg_backBtn = (Mb.ID,'com.ourydc.yuebaobao:id/iv_back_new') # 聊天返回
    sendBtn = (Mb.ID,'com.ourydc.yuebaobao:id/sendBtn') # 打赏
    
    ############################未进入开播用户资料相关元素###########################
    nearby_people = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and @text='附近的人']") # 附近的人按钮
    cc_layout = (Mb.XPATH, "//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/cc_layout']") # 附近的人列表元素
    tv_nick = (Mb.ID,'com.ourydc.yuebaobao:id/tv_nick') #昵称
    tv_nick_name = (Mb.ID,'com.ourydc.yuebaobao:id/tv_nick_name') #我的昵称
    say_hello = (Mb.ID, "com.ourydc.yuebaobao:id/btn_chat") # 打招呼元素
    more_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/view_share']") #更多列表
    
    # gv_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/gv']/child::com.ourydc.yuebaobao:id/share_root") #动态列表
    gv_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/gv']/child::android.view.ViewGroup") #动态列表
    cancel_follow = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='取消关注']") #取消关注
    Confirm_cancellation = (Mb.ID, "com.ourydc.yuebaobao:id/tv_cancel") # 取消关注用户按钮
    #---资料---
    user_material = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='资料']") #用户资料中的资料
    liKa_id = (Mb.ID,"com.ourydc.yuebaobao:id/tv_id_value") #用户哩咔id
    materialAssert = (Mb.ID,"com.ourydc.yuebaobao:id/sv") #资料tap页断言
    
    #---动态tap---
    # dynamic_tap_assert = (Mb.ID,"com.ourydc.yuebaobao:id/rcv") #动态tap断言
    user_dynamic = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='动态']") #用户资料中的动态
    dynamic_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv']/child::android.view.ViewGroup") #动态列表
    
    #---守护tap---
    
    guard_tap_assert = (Mb.ID,"com.ourydc.yuebaobao:id/rv_guard") #守护tap断言
    user_guard = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='守护']") #用户资料中的守护index
    guard_list = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_username' and not(@text='虚位以待')]") #用户守护
    
    #----展墙tap---
    War_wall = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='展墙']") #用户资料中的展墙
    War_wall_list = (Mb.ID,"com.ourydc.yuebaobao:id/layout_gift") #展墙断言
    #---展墙>贡献榜
    contribution = (Mb.ID,'com.ourydc.yuebaobao:id/click_contribute') #贡献榜
    contributionlist = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv']/child::com.ourydc.yuebaobao:id/layout_contribute_diamond") #贡献榜列表
    # masonry_list = (Mb.ID, "com.ourydc.yuebaobao:id/guardIv") #默认钻石榜列表  com.ourydc.yuebaobao:id/guardIv
    no_data = (Mb.ID,'com.ourydc.yuebaobao:id/tv_empty_text') #暂无数据
    masonry_list = (Mb.XPATH, "//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/avatar']") #展墙》贡献榜》钻石榜列表、魅力榜列表、守护榜列表通用
    #---礼物展墙---
    gift_wall = (Mb.ID,'com.ourydc.yuebaobao:id/click_gift') #礼物展墙
    giftWallList = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_gift_num']") #礼物展墙列表
    # giftWallList = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_profile_red_envelope']") #礼物展墙列表 com.ourydc.yuebaobao:id/layout_gift
    # giftWallList = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/rv']/child::android.widget.RelativeLayout") #礼物展墙列表 
    giftWallNameList = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_gift_name']") #礼物名字列表
    giftWallNumberList = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/tv_gift_num']") #礼物列表
    Diamond_number_text = (Mb.ID,'com.ourydc.yuebaobao:id/tv_content') #确定弹窗中text
    #---装扮展墙---
    # decorate_wall = (Mb.ID,'com.ourydc.yuebaobao:id/click_mount') #装扮展墙
    decorate_wall = (Mb.ID,'com.ourydc.yuebaobao:id/iv_mount_next') #装扮展墙
    Decorate_wall_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rv_item']/child::android.widget.RelativeLayout") # 装扮展墙礼物列表


    #---守护者---
    guardian = (Mb.ID,'com.ourydc.yuebaobao:id/iv_protector_border') #守护者按钮元素
    guardian_nickname = (Mb.ID,'com.ourydc.yuebaobao:id/tv_nickname_1') #守护者昵称

    
    #================================================================
    #===================开播房间内二级元素定位开始=====================
    #==================================================================
    
    #不同礼物类型的tap按钮
    gift_button = (Mb.XPATH,"//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_tab_title' and @text='礼物']") #礼物tap
    Halloween_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='1']") #万圣节按钮
    lover_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='2']") #七夕按钮
    # lover_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='2']") #七夕按钮
    year_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='3']") #年度盛典按钮
    anniversary_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='4']") #周年盛典按钮
    magic_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='5']") #魔法按钮
    teacher_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='6']") #教师节按钮
    guard_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='7']") #守护按钮
    suit_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='8']") #套装按钮
    special_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='9']") #特殊按钮
    
    goldCoins_button = (Mb.XPATH,"//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_tab_title' and @text='金币']") #金币tap按钮
    goldCoins_list = (Mb.XPATH,"//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer']") #金币礼物列表
    goldCoins_balance = (Mb.ID,"com.ourydc.yuebaobao:id/tv_balance") #金币余额
    # knapsack_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='11']") #背包按钮
    knapsack_button = (Mb.XPATH,"//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_tab_title' and @text='背包']") #背包tap
    backpack_gift = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer']") #背包中的礼物列表
    gift_list = [
        gift_button,Halloween_button,lover_button,year_button,
        anniversary_button,magic_button,teacher_button,guard_button,
        suit_button,special_button,goldCoins_button,knapsack_button
    ]
    

    homeowner_data = (Mb.ID,'com.ourydc.yuebaobao:id/iv_user_profile') #查看房主资料
    
    #《礼物tap下的所有礼物-礼物按钮-list-1》
    # gift_pages = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer' and @index='0']") #礼物按钮
    gift_pages = (Mb.XPATH,"//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer']") #当前页所有礼物元素
    def get_gift(number):
        gift = (Mb.XPATH,"//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer' and @index='{}']".format(number)) #礼物元素
        return gift
    btn_send_gift = (Mb.ID,"com.ourydc.yuebaobao:id/btn_send_gift") #赠送按钮

    # 《房间热度值-2》
    heat_value = (Mb.XPATH,"//*[@class='android.widget.TextView' and @index='0']") #在线列表按钮
    #列表list元素
    user_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rv']/child::android.widget.RelativeLayout") 
    vip_seat = (Mb.XPATH,"//*[@class='android.widget.TextView' and @index='1']") #贵宾席位按钮
    iv_empty = (Mb.ID,'com.ourydc.yuebaobao:id/iv_empty') #贵宾席位列表断言是否为空



    #================================================================
    #===================开播房间内二级元素定位结束=====================
    #==================================================================

    
    #=============================房间菜单===================================
    #交友房间更多菜单
    minimize = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='最小化']") # 最小化
    exit_room = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='退出房间']") # 退出房间
    close_room = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='关闭房间']")
    report = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='举报']") # 举报
    more_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='更多分享']") # 更多分享
    wechat_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至微信']") # 分享至微信
    qq_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至QQ']") # 分享至QQ
    micro_blog_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至微博']") # 分享至微博
    
    ####################################附近动态元素####################################### 
    tv_content = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_content' and @text='附近动态']") # 附近动态按钮
    
    
    # nearby_dynamics_list = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_nickname']") # 附近动态列表元素
    # nearby_dynamics_list2 = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_tag_name']") # 附近动态*人参与
    # nearby_dynamics_list = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/rcv']") # 附近动态列表元素
    # nearby_dynamics_list = (Mb.XPATH, "//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/layout_dynamic']/child::com.ourydc.yuebaobao:id/tv_content") # 装扮展墙礼物列表
    iv_prise = (Mb.ID, "com.ourydc.yuebaobao:id/iv_prise") #点赞
    all_mode = (Mb.ID, "com.ourydc.yuebaobao:id/mvp") #全部模式（聊天室的一个蒙层）
    playLottie = (Mb.ID, "playLottie") #全部模式（聊天室的一个蒙层）


    
    
    jbtq = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='金币套圈']") #金币套圈游戏
    trap = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='套圈圈']") #套圈圈游戏
    taoquan_btn = (Mb.XPATH, "//*[@class='android.view.View' and @index='4']") #套圈按钮


    slingshot = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='进击的弹弓手']") #进击的弹弓手游戏
    Koi_blind_box = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='锦鲤盲盒']") #锦鲤盲盒游戏
    purchase_btn = (Mb.XPATH, "//*[@class='android.view.View' and @index='5' and @text='购买']") #断言锦鲤盲盒购买按钮


    gold_coin_car = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='金币造车']") #金币造车游戏
    
    jungle_hunt = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='丛林狩猎']") #丛林狩猎游戏
    hemp_rope = (Mb.XPATH, "//*[@class='android.view.View' and @text='尼龙绳']") #丛林狩猎麻绳元素


    
    



