'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-09-07 19:22:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/room_locator.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb

'''首页的页面元素'''


class RoomPageLocator:

    
    # 设置未成年人保护弹窗
    btn_know = (Mb.ID, "com.ourydc.yuebaobao:id/btn_iknow")
    # 关闭女神开播引导弹窗按钮
    close_back = (Mb.ID, "com.ourydc.yuebaobao:id/back") 
    
    # 房间模块
    room_module = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_live") 
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
    

    '''list列表面类型元素'''
    # 房间list
    room_list = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/tv_charroom_label']") 
    room_list_kaiHei = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/iv_room_cover']") 
    def get_goddess_type(number):
        goddessType = (Mb.XPATH, "//*[@class='android.widget.ImageView' and @resource-id='com.ourydc.yuebaobao:id/tv_charroom_label' and @index='{}']".format(number)) 
        return goddessType

    '''房间内部元素'''
    goddess_type = (Mb.ID, "com.ourydc.yuebaobao:id/iv_check_all") # 全麦
    masterAvatarView = (Mb.ID,'com.ourydc.yuebaobao:id/masterAvatarView') #礼物入口弹框1
    tv_heat = (Mb.ID,'com.ourydc.yuebaobao:id/tv_heat') # 房间热度值2
    follow = (Mb.ID,'com.ourydc.yuebaobao:id/attentionIv') # 关注
    # ranking_list = (Mb.ID,'com.ourydc.yuebaobao:id/guardAvatarView') #排行榜3
    ranking_list = (Mb.ID,'com.ourydc.yuebaobao:id/rv_top') #排行榜3
    #《排行榜-3》
    contribution_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='贡献榜']") # 贡献榜
    popularity_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='人气榜']") # 人气榜
    guardian_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='守护榜']") # 守护榜	
    tv_title_ri = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='日榜']") # 日榜	
    tv_title_week = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='周榜']") # 周榜	
    tv_title_yue = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='月榜']") # 月榜	

    
    room_menu = (Mb.ID,'com.ourydc.yuebaobao:id/menu') #菜单4
    
    tv_introduce = (Mb.ID,'com.ourydc.yuebaobao:id/tv_introduce') #玩法介绍5
    closeIv = (Mb.ID,'com.ourydc.yuebaobao:id/closeIv') #关闭玩法介绍
    
    layout_people = (Mb.ID,'com.ourydc.yuebaobao:id/layout_people') #麦下6
    iv_head_view = (Mb.ID,'com.ourydc.yuebaobao:id/iv_head_view') #麦下收缩列表
    
    rv = (Mb.ID,'com.ourydc.yuebaobao:id/rv') #点击房间内部用户头像查看用户列表7
    
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
    iv_send_text = (Mb.ID,'com.ourydc.yuebaobao:id/iv_send_text') #input
    iv_more = (Mb.ID,'com.ourydc.yuebaobao:id/iv_more') #更多
    iv_msg = (Mb.ID,'com.ourydc.yuebaobao:id/iv_msg') #消息
    iv_game = (Mb.ID,'com.ourydc.yuebaobao:id/iv_game') #游戏
    lucky_bag_iv = (Mb.ID,'com.ourydc.yuebaobao:id/lucky_bag_iv') #福袋
    iv_first_recharge = (Mb.ID,'com.ourydc.yuebaobao:id/iv_first_recharge') #礼物入口底部
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
    msg_backBtn = (Mb.ID,'com.ourydc.yuebaobao:id/iv_back_new') # 聊天返回
    sendBtn = (Mb.ID,'com.ourydc.yuebaobao:id/sendBtn') # 打赏
    


    
    #================================================================
    #===================开播房间内二级元素定位开始=====================
    #==================================================================
    
    #不同礼物类型的tap按钮
    gift_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='0']") #礼物按钮
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
    goldCoins_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='10']") #金币按钮
    knapsack_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='11']") #背包按钮

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
    vip_seat = (Mb.XPATH,"//*[@class='android.widget.TextView' and @index='0']") #贵宾席位按钮



    #================================================================
    #===================开播房间内二级元素定位结束=====================
    #==================================================================

    
    #=============================房间菜单===================================
    #交友房间菜单
    minimize = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='最小化']") # 最小化
    exit_room = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='退出房间']") # 退出房间
    report = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='举报']") # 举报
    more_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='更多分享']") # 更多分享
    wechat_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至微信']") # 分享至微信
    qq_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至QQ']") # 分享至QQ
    micro_blog_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至微博']") # 分享至微博

    #小窝房间菜单
    room_menu_btn = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/gv']/child::android.widget.RelativeLayout")	
    #确定关闭按钮
    close_ok = (Mb.ID,'com.ourydc.yuebaobao:id/tv_sure') 
    


    
    



