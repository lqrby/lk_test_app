'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-09-26 10:08:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/home_locators.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb

'''首页的页面元素'''


class HomePageLocator:
    ###########################哩咔首页交友模块元素定位开始##########################
    # 隐私政策弹窗
    dating_module = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_home") # 交友模块
    
    message_moduke = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_message") # 消息模块
    my_module = (Mb.ID, "com.ourydc.yuebaobao:id/iv_tab_mine") # 我的模块
    
    
    
    
    
    
    
    # ###########################哩咔首页交友模块元素定位结束##########################
    # tv_play = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/tv_play']") # 发现》点击开播用户
    # tv_close = (Mb.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ourydc.yuebaobao:id/des']") # 发现》点击未播用户
    # no_more = (Mb.XPATH, "//*[@class='android.widget.TextView' and @text='没有更多']") # 主播列表底部的没有更多按钮元素
    # roomIdTv = (Mb.ID, "com.ourydc.yuebaobao:id/roomIdTv") # 获取开播房间的id
    # tv_nick = (Mb.ID, "com.ourydc.yuebaobao:id/tv_nick") # 获取用户昵称

    # #================================================================
    # #===================开播房间内一级元素定位开始=====================
    # #==================================================================
    # masterAvatarView = (Mb.ID,'com.ourydc.yuebaobao:id/masterAvatarView') #礼物入口弹框1
    # tv_heat = (Mb.ID,'com.ourydc.yuebaobao:id/tv_heat') # 房间热度值2
    # follow = (Mb.ID,'com.ourydc.yuebaobao:id/attentionIv') # 关注
    # ranking_list = (Mb.ID,'com.ourydc.yuebaobao:id/guardAvatarView') #排行榜3
    # menu = (Mb.ID,'com.ourydc.yuebaobao:id/menu') #菜单4
    
    # tv_introduce = (Mb.ID,'com.ourydc.yuebaobao:id/tv_introduce') #玩法介绍5
    # closeIv = (Mb.ID,'com.ourydc.yuebaobao:id/closeIv') #关闭玩法介绍
    
    # layout_people = (Mb.ID,'com.ourydc.yuebaobao:id/layout_people') #麦下6
    # iv_head_view = (Mb.ID,'com.ourydc.yuebaobao:id/iv_head_view') #麦下收缩列表
    
    # rv = (Mb.ID,'com.ourydc.yuebaobao:id/rv') #点击房间内部用户头像查看用户列表7
    
    # #=======页面底部按钮========
    # findBtn = (Mb.ID,'com.ourydc.yuebaobao:id/iv_sel') #发现按钮
    
    # layout_input_msg = (Mb.ID,'com.ourydc.yuebaobao:id/layout_input_msg') #表情
    # iv_send_text = (Mb.ID,'com.ourydc.yuebaobao:id/iv_send_text') #input
    # iv_more = (Mb.ID,'com.ourydc.yuebaobao:id/iv_more') #更多
    # iv_msg = (Mb.ID,'com.ourydc.yuebaobao:id/iv_msg') #消息
    # iv_game = (Mb.ID,'com.ourydc.yuebaobao:id/iv_game') #游戏
    # lucky_bag_iv = (Mb.ID,'com.ourydc.yuebaobao:id/lucky_bag_iv') #福袋
    # iv_first_recharge = (Mb.ID,'com.ourydc.yuebaobao:id/iv_first_recharge') #礼物入口底部
    # #=======================开播房间内元素结束===================

    # #个人资料元素定位
    # personIdView = (Mb.ID,'com.ourydc.yuebaobao:id/personIdView') #个人id
    # nick = (Mb.ID,'com.ourydc.yuebaobao:id/nick') #昵称
    # sexAndAge = (Mb.ID,'com.ourydc.yuebaobao:id/sexAndAge') #性别
    # locationTv = (Mb.ID,'com.ourydc.yuebaobao:id/locationTv') #位置
    # descTv = (Mb.ID,'com.ourydc.yuebaobao:id/descTv') #个性签名
    # tv_week_gift_num = (Mb.ID,'com.ourydc.yuebaobao:id/tv_week_gift_num') #本周收到的礼物
    # reference = (Mb.ID,'com.ourydc.yuebaobao:id/reference') # @她
    # attentionBtn = (Mb.ID,'com.ourydc.yuebaobao:id/attentionBtn') # 关注
    # msgBtn = (Mb.ID,'com.ourydc.yuebaobao:id/msgBtn') # 聊天
    # msg_backBtn = (Mb.ID,'com.ourydc.yuebaobao:id/iv_back_new') # 聊天返回
    # sendBtn = (Mb.ID,'com.ourydc.yuebaobao:id/sendBtn') # 打赏
    


    
    # #================================================================
    # #===================开播房间内二级元素定位开始=====================
    # #==================================================================
    
    # #不同礼物类型的tap按钮
    # gift_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='0']") #礼物按钮
    # Halloween_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='1']") #万圣节按钮
    # lover_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='2']") #七夕按钮
    # # lover_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='2']") #七夕按钮
    # year_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='3']") #年度盛典按钮
    # anniversary_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='4']") #周年盛典按钮
    # magic_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='5']") #魔法按钮
    # teacher_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='6']") #教师节按钮
    # guard_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='7']") #守护按钮
    # suit_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='8']") #套装按钮
    # special_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='9']") #特殊按钮
    # goldCoins_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='10']") #金币按钮
    # knapsack_button = (Mb.XPATH,"//*[@class='android.widget.RelativeLayout' and @index='11']") #背包按钮

    # gift_list = [
    #     gift_button,Halloween_button,lover_button,year_button,
    #     anniversary_button,magic_button,teacher_button,guard_button,
    #     suit_button,special_button,goldCoins_button,knapsack_button
    # ]
    
    
    

    # homeowner_data = (Mb.ID,'com.ourydc.yuebaobao:id/iv_user_profile') #查看房主资料
    
    # #《礼物tap下的所有礼物-礼物按钮-list-1》
    # # gift_pages = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer' and @index='0']") #礼物按钮
    # gift_pages = (Mb.XPATH,"//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer']") #当前页所有礼物元素
    # def get_gift(number):
    #     gift = (Mb.XPATH,"//*[@class='android.view.ViewGroup' and @resource-id='com.ourydc.yuebaobao:id/layout_msg_panel_red_outer' and @index='{}']".format(number)) #礼物元素
    #     return gift
    # btn_send_gift = (Mb.ID,"com.ourydc.yuebaobao:id/btn_send_gift") #赠送按钮

    # # 《房间热度值-2》
    # heat_value = (Mb.XPATH,"//*[@class='android.widget.TextView' and @index='0']") #在线列表按钮
    # vip_seat = (Mb.XPATH,"//*[@class='android.widget.TextView' and @index='0']") #贵宾席位按钮


    # #《守护榜-3》
    # contribution_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='贡献榜']") # 贡献榜
    # popularity_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='人气榜']") # 人气榜
    # guardian_list = (Mb.XPATH,"//*[@class='android.widget.TextView' and @text='守护榜']") # 守护榜






    # #================================================================
    # #===================开播房间内二级元素定位结束=====================
    # #==================================================================

    
    # #=============================更多===================================
    # minimize = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='最小化']") # 最小化
    # exit_room = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='退出房间']") # 退出房间
    # report = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='举报']") # 举报
    # more_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='更多分享']") # 更多分享
    # wechat_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至微信']") # 分享至微信
    # qq_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至QQ']") # 分享至QQ
    # micro_blog_sharing = (Mb.XPATH,"//*[@resource-id='com.ourydc.yuebaobao:id/view_share' and @text='分享至微博']") # 分享至微博

