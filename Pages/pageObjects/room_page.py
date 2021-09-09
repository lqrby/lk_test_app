from re import M
from typing_extensions import ParamSpecArgs
from attr import s
from Common.basepage import BasePage
from Pages.pageObjects.Common_Buss import CommonBus
from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
import time, random

from Pages.pageLocators.pop_locators import PopUp
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from appium.webdriver.common.mobileby import MobileBy as Mb

log = get_logger(logger_name="首页操作日志")

'''首页-页面操作'''

class RoomPage(CommonBus):

    '''
    功能:创建聊天室
    房间类型:小窝类型
    '''
    def found_minNest_room(self):
        self.find_room() # 点击房间模块
        self.menuIv() #开房间
        self.room_type(num=0) #房间类型
        self.room_label() #房间标签
        self.room_name() #输入房间话题
        self.room_seat() #选择房间座位
        self.entry_room() #点击确认创建房间按钮
        self.driver.implicitly_wait(10)
        self.room_menu() #房间内的菜单
        self.close_room() #关闭房间
        return True

    '''
    功能:创建聊天室
    房间类型:萌新接待类型
    '''
    def found_reception_room(self):
        self.find_room() # 点击房间模块
        self.menuIv() #开房间
        self.room_type() #房间类型
        self.room_label() #房间标签
        self.room_name() #输入房间话题
        if self.entry_room(): #点击进入房间按钮
            self.driver.implicitly_wait(10)
            self.room_menu() #房间内的菜单
            self.close_room() #关闭房间
            return True
        else:
            return False

        # self.driver.press_keycode(4)

    #===================================开小窝/萌新接待房间子方法======================================     
    #创建聊天室入口
    def menuIv(self):
        self.wait_element_clickable(roomloc.menuIv)
        self.click_element(roomloc.menuIv, model="点击创建聊天室入口按钮")

    #选择房间类型
    def room_type(self,num=1):
        self.wait_element_presence(roomloc.room_type)
        room = self.find_elements(roomloc.room_type)
        room[num].click()

    #选择房间标签
    def room_label(self):
        self.wait_element_presence(roomloc.room_label)
        roomLabels = self.find_elements(roomloc.room_label)
        labelNum = random.randint(0,(len(roomLabels)-1))
        roomLabels[labelNum].click()
        
    #选择房间话题
    def room_name(self):
        roomName = "创建房间-{}".format(int(time.time()))
        self.wait_element_presence(roomloc.room_name)
        self.clear_input_text(roomloc.room_name, model="清除输入框默认文本")
        self.input_text(roomloc.room_name, roomName, model="输入房间话题")

    #选择房间座位数
    def room_seat(self):
        self.wait_element_presence(roomloc.room_seat)
        roomSeats = self.find_elements(roomloc.room_seat)
        seatNum = random.randint(0,(len(roomSeats)-1))
        roomSeats[seatNum].click()
        
    #点击确认创建房间按钮
    def entry_room(self):
        self.wait_element_clickable(roomloc.entry_room)
        self.click_element(roomloc.entry_room, model="点击确认创建房间按钮")
        message = "需官方授权可开启"
        message_toast = self.get_toast_exist(message)
        if message in message_toast:
            log.info("toast======={}".format(self.get_toast_exist(message)))
            # self.save_webImgs(model="创建聊天室失败截图")
            return False
        else:
            return True

    #房间菜单按钮
    def room_menu(self):
        self.wait_element_clickable(roomloc.room_menu)
        self.click_element(roomloc.room_menu, model="点击房间菜单按钮")
        
    #退出聊天室
    def close_room(self,num=1):
        self.wait_element_presence(roomloc.room_menu_btn)
        menuBtnArr = self.get_elements(roomloc.room_menu_btn)
        menuBtnArr[num].click()
        # self.wait_element_clickable(roomloc.close_ok)
        # self.click_element(roomloc.close_ok)
        self.exist_be_click(roomloc.close_ok)


    #=============进入房间============
    '''
    功能:进入推荐聊天室
    '''
    def enter_liveRoom(self):
        self.swipeDown()
        self.driver.implicitly_wait(8)
        room_list = self.get_elements(roomloc.room_list)
        if len(room_list) > 0:
            number = random.randint(0, (len(room_list)-1))
            # self.click_element(roomloc.get_goddess_type(number))
            room_list[number].click()
            self.click_blessing_bag() # 点击福袋
            self.click_rankingList() # 点击排行榜
            self.gift_entrance_top() #点击顶部礼物入口
            self.look_homeowner_data() #查看房主资料
            self.gift_entrance_bottom() # 点击底部礼物入口
            self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
            time.sleep(1)
            self.click_menu() #点击聊天室菜单
            self.close_room() #关闭房间
            return True
        else:
            return False
    

    '''
    功能:进入开黑聊天室
    '''
    def open_black_room(self):
        self.swipeDown()
        self.driver.implicitly_wait(8)
        #获取开黑房间list
        room_list = self.get_elements(roomloc.room_list_kaiHei)
        if len(room_list) > 0:
            number = random.randint(0, (len(room_list)-1))
            # self.click_element(roomloc.get_goddess_type(number))
            room_list[number].click()
            self.click_blessing_bag() # 点击福袋
            self.click_rankingList() # 点击排行榜
            self.gift_entrance_top() #点击顶部礼物入口
            self.look_homeowner_data() #查看房主资料
            self.open_black_bottom() # #开黑tap-礼物底部入口
            self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
            time.sleep(1)
            self.click_create_ranks() # 创建队伍 
            time.sleep(1)
            self.click_dissolution() # 解散队伍
            self.click_menu() #点击聊天室菜单
            self.close_room() #退出聊天室
            return True
        else:
            return False

    '''
    功能:进入派对聊天室
    '''
    def open_party_room(self):
        self.swipeDown()
        self.driver.implicitly_wait(8)
        room_list = self.get_elements(roomloc.room_list_kaiHei)
        if len(room_list) > 0:
            number = random.randint(0, (len(room_list)-1))
            # self.click_element(roomloc.get_goddess_type(number))
            room_list[number].click()
            self.click_blessing_bag() # 点击福袋
            self.click_rankingList() # 点击排行榜
            self.gift_entrance_top() #点击顶部礼物入口
            self.look_homeowner_data() #查看房主资料
            self.open_black_bottom() # 点击底部礼物入口
            self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
            self.click_receive() #领取按钮
            time.sleep(1)
            self.click_menu() #点击聊天室菜单
            self.close_room(num=2) # 退出聊天室
            return True
        else:
            return False

    def click_menu(self):
        self.wait_element_clickable(roomloc.room_menu, model="等待聊天室菜单可点击")
        self.click_element(roomloc.room_menu, model="点击聊天室菜单")#点击房间菜单
    
    #点击榜单
    def click_bangDan(self):
        self.wait_element_clickable(roomloc.room_module)
        self.click_element(roomloc.room_module, model="点击房间模块")#点击房间模块

    #点击房间模块
    def find_room(self):
        self.wait_element_clickable(roomloc.room_module)
        self.click_element(roomloc.room_module, model="点击房间模块")#点击房间模块

    #点击房间内的tap
    def room_tap(self, tap_element):
        self.wait_element_clickable(tap_element, model="检查tap")
        self.click_element(tap_element, model="点击tap") #点击tap


    #进入直播间
    def enter_liveRoom2(self, number = 1):
        while number > 0:
            tv_plays = self.get_elements(roomloc.tv_plays)
            log.info("列表数据有{}条".format(len(tv_plays)))
            if len(tv_plays) > 0:
                for no_play in tv_plays:
                    time.sleep(3)
                    no_play.click()
                    self.gift_entrance_top() #顶部礼物入口
                    self.look_homeowner_data() #查看房主资料
                    self.wait_eleVisible(roomloc.roomIdTv) # 断言用户资料
                    self.gift_entrance_bottom() # 底部礼物入口
                    self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
                    self.click_heat_value() # 房间用户及贵宾席
                    self.exist_be_click(roomloc.follow)#点击关注
                    self.click_introduce() #点击玩法介绍，关闭玩法介绍
                    self.click_wheat_lower() # 点击麦下  麦下取消功能
                    self.click_game() #点击游戏
                    self.driver.keyevent(4)
                    number = number - 1
                    if number == 0:
                        break
                if number > 0:
                    if self.is_element_exist(roomloc.no_more):
                        log.info("显示了没有更多")
                        number = 0
                        break
                    else:
                        log.info("向上滑动列表")
                        self.swipeUp()
            elif self.is_element_exist(roomloc.no_more):
                log.info("没有更多")
                number = 0
                break
            else:
                log.info("向上滑动列表")
                self.swipeUp()
        return len(tv_plays)



    # #点击未开播的用户
    def enter_notLiveRoom(self, number = 3):
        while number > 0:
            tv_desArr = self.get_elements(roomloc.tv_close)
            log.info("列表数据有{}条".format(len(tv_desArr)))
            if len(tv_desArr) > 0:
                for no_play in tv_desArr:
                    time.sleep(3)
                    no_play.click()
                    self.wait_eleVisible(roomloc.tv_nick)
                    time.sleep(random.randint(5,7))
                    self.driver.keyevent(4)
                    time.sleep(1)
                    number = number - 1
                    if number == 0:
                        break
                if number > 0:
                    if self.is_element_exist(roomloc.no_more):
                        log.info("显示了没有更多")
                        number = 0
                        break
                    else:
                        log.info("向上滑动列表")
                        self.swipeUp()
            elif self.is_element_exist(roomloc.no_more):
                log.info("没有更多")
                number = 0
                break
            else:
                log.info("向上滑动列表")
                self.swipeUp()
        return len(tv_desArr)


    #点击福袋
    def click_blessing_bag(self):
        self.wait_element_clickable(roomloc.lucky_bag_iv)
        self.click_element(roomloc.lucky_bag_iv, model="点击福袋")#点击福袋
        self.wait_eleVisible(roomloc.no_hair_message, model="等待显示‘不发送消息给好友’")
        self.assert_true(roomloc.no_hair_message) #福袋断言
        self.driver.keyevent(4)

    # 领取入口
    def click_receive(self):
        if self.is_element_exist(roomloc.receive):
            self.wait_eleVisible(roomloc.receive, model="等待领取按钮显示")
            self.click_element(roomloc.receive, model="点击领取按钮")
            self.wait_eleVisible(roomloc.for_her, model="等待显示为ta点亮tap")
            self.assert_true(roomloc.for_her,model="为ta点亮tap") #断言
            self.wait_element_clickable(roomloc.sign_in, model="等待气泡的签到或领取可点击")
            self.click_element(roomloc.sign_in, model="点击气泡的签到或领取")
            self.wait_element_clickable(roomloc.receiveBtn, model="等待领取按钮可点击")
            self.click_element(roomloc.receiveBtn,model="点击领取")
            result = self.get_toast_exist(message='领取成功')
            print("断言=====",result)
            assert "领取成功" in result
            self.wait_element_presence(roomloc.play_instructions)
            self.click_element(roomloc.play_instructions, model="玩法说明按钮-可领取")
            time.sleep(2)
            # resultData = self.driver.page_source
            # assert "用户通过完成" in resultData
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
        elif self.is_element_exist(roomloc.count_down_receive):
            self.click_element(roomloc.count_down_receive, model="点击领取倒计时按钮")
            self.wait_element_presence(roomloc.play_instructions)
            self.click_element(roomloc.play_instructions, model="点击玩法说明按钮-倒计时")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(1)
            self.driver.press_keycode(4)
            '''
            后续这里要写H5断言
            '''
            
        
    #抽奖tap
    def click_luck_draw(self):
        self.wait_element_clickable(roomloc.luck_draw)
        self.click_element(roomloc.luck_draw, model="点击抽奖tap")
        '''
        后续写H5脚本
        '''
    #礼物顶部入口
    def gift_entrance_top(self):
        self.wait_element_clickable(roomloc.masterAvatarView)
        self.click_element(roomloc.masterAvatarView)#点击礼物入口

    #推荐tap-礼物底部入口
    def gift_entrance_bottom(self):
        self.wait_element_clickable(roomloc.iv_first_recharge)
        self.click_element(roomloc.iv_first_recharge)#点击礼物入口
  

    #开黑tap-礼物底部入口
    def open_black_bottom(self):
        self.wait_element_clickable(roomloc.open_black_recharge)
        self.click_element(roomloc.open_black_recharge)#点击礼物入口
 
    #切换礼物tap
    def get_gift_tap(self):
        for i,tapBtn in enumerate(roomloc.gift_list):
            print("tapBtn=============",tapBtn)
            self.click_gift_tap(tapBtn) # 点击礼物tap
            self.driver.implicitly_wait(5)
            self.select_gift() # 选中某个礼物
            self.give_gifts() # 赠送礼物
            if i >= 2:
                break
        self.driver.press_keycode(4)
        time.sleep(1)

    #点击礼物tap
    def click_gift_tap(self,tapBtn):
        self.wait_element_clickable(tapBtn, model="等待元素显示")
        self.click_element(tapBtn,model="点击礼物tap") #点击礼物tap
        self.driver.implicitly_wait(5)


    #选中某个礼物
    def select_gift(self):
        giftPages = self.get_elements(roomloc.gift_pages) #某tap下当前页的所有礼物元素
        if giftPages.__len__() > 0:
            number = random.randint(0, (len(giftPages)-1))
            # self.click_element(roomloc.get_gift(number))
            giftPages[number].click()
            time.sleep(1)
            
    #赠送礼物
    def give_gifts(self):
        self.wait_element_clickable(roomloc.btn_send_gift, model="查找赠送按钮")
        self.click_element(roomloc.btn_send_gift,model="点击赠送") #点击赠送

    #查看房主资料
    def look_homeowner_data(self):
        self.wait_element_clickable(roomloc.homeowner_data)
        self.click_element(roomloc.homeowner_data,model="点击房主资料") #点击房主资料
        self.wait_element_presence(roomloc.personIdView, model="查看房间资料")
        assert self.is_element_exist(roomloc.personIdView) == True #房间id
        # assert self.is_element_exist(roomloc.nick) == True #昵称
        self.follow_ta() #关注
        self.chat() #聊天
        self.reward() #打赏，进入礼物页，点击资料再进入资料页
        self.ait_ta() #@ ta，然后返回，返回到了列表页
        # self.driver.press_keycode(4)

    #@ta
    def ait_ta(self):
        self.wait_element_clickable(roomloc.reference)
        self.click_element(roomloc.reference,model="点击@ta") # 点击@ta
        time.sleep(1)
        self.driver.press_keycode(4)

    #资料内点击关注
    def follow_ta(self):
        if self.is_clickable(roomloc.attentionBtn):
            self.click_element(roomloc.attentionBtn,model="点击关注") # 点击关注
        else:
            pass


    #资料内点击打赏
    def reward(self):
        self.wait_element_clickable(roomloc.sendBtn)
        self.click_element(roomloc.sendBtn,model="点击打赏") # 点击打赏
        self.wait_element_clickable(roomloc.homeowner_data)
        self.click_element(roomloc.homeowner_data,model="点击房主资料") #点击房主资料


    #资料内点击聊天
    def chat(self):
        self.wait_element_clickable(roomloc.msgBtn)
        self.click_element(roomloc.msgBtn,model="点击聊天") # 点击聊天
        self.wait_element_clickable(roomloc.msg_backBtn)
        self.click_element(roomloc.msg_backBtn,model="点击返回") # 点击返回


    # 点击房间热度值
    def click_heat_value(self):
        self.wait_element_clickable(roomloc.tv_heat)
        self.click_element(roomloc.tv_heat,model="点击礼物tap") #点击某个礼物tap
        time.sleep(2)
        self.wait_element_clickable(roomloc.heat_value)
        self.click_element(roomloc.heat_value,model="点击在线列表") #在线列表
        time.sleep(2)
        self.wait_element_clickable(roomloc.vip_seat)
        self.click_element(roomloc.vip_seat,model="点击贵宾席位") #贵宾席位列表
        self.driver.press_keycode(4)
        time.sleep(2)

    #点击排行榜
    def click_rankingList(self):
        if self.is_element_exist(roomloc.ranking_list):
            self.wait_element_clickable(roomloc.ranking_list)
            self.click_element(roomloc.ranking_list,model="点击排行榜") #点击排行榜
            self.assert_true(roomloc.day_week_month_assert) # 断言
            self.wait_eleVisible(roomloc.tv_title_week, model="等待周榜显示")
            self.click_element(roomloc.tv_title_week, model="点击周榜")
            self.assert_true(roomloc.day_week_month_assert) # 断言
            self.wait_eleVisible(roomloc.tv_title_yue, model="等待月榜显示")
            self.click_element(roomloc.tv_title_yue, model="点击月榜")
            self.assert_true(roomloc.day_week_month_assert) # 断言
            self.wait_element_clickable(roomloc.popularity_list, model="等待人气榜可点击")
            self.click_element(roomloc.popularity_list,model="点击人气榜") #点击人气榜
            self.assert_true(roomloc.day_week_month_assert) # 断言
            self.wait_eleVisible(roomloc.tv_title_week, model="等待周榜显示")
            self.click_element(roomloc.tv_title_week, model="点击周榜")
            self.assert_true(roomloc.day_week_month_assert) # 断言
            self.wait_eleVisible(roomloc.tv_title_yue, model="等待月榜显示")
            self.click_element(roomloc.tv_title_yue, model="点击月榜")
            self.assert_true(roomloc.day_week_month_assert) # 断言
            self.wait_element_clickable(roomloc.guardian_list, model="等待守护榜可点击")
            self.click_element(roomloc.guardian_list,model="点击守护榜") #点击守护榜
            if self.is_element_exist(roomloc.guard_assert):
                sh_list = self.get_elements(roomloc.guard_assert)
                assert len(sh_list) > 0
            else:
                log.info("==========暂无守护========")
            time.sleep(1)
            self.click_element(roomloc.msg_backBtn, model="点击返回按钮") #返回
        

    #点击玩法介绍
    def click_introduce(self):
        time.sleep(2)
        self.click_element(roomloc.tv_introduce,model="点击玩法介绍")#点击玩法介绍  
        time.sleep(1)
        result = self.driver.page_source
        assert "一" in result
        self.click_element(roomloc.closeIv,model="关闭玩法介绍")#关闭玩法介绍
    

    #点击麦下
    def click_wheat_lower(self):
        time.sleep(1)
        self.click_wheatList()
        self.click_element(roomloc.layout_people,model="点击麦下") #点击麦下
        time.sleep(1)
        self.click_wheatList()
    

    # 点击麦下用户列表
    def click_wheatList(self):
        if self.is_element_exist(roomloc.iv_head_view):
            self.click_element(roomloc.iv_head_view,model="点击麦下收缩列表") #点击麦下收缩列表
            time.sleep(2)
            self.driver.keyevent(4)
        else:
            pass


    # 点击游戏
    def click_game(self):
        self.click_element(roomloc.iv_game,model="点击游戏") #点击游戏
        time.sleep(2)


    # 开黑tay-聊天室-创建队伍
    def click_create_ranks(self):
        if self.is_element_exist(roomloc.tv_disband):
            self.click_dissolution()
        self.click_element(roomloc.tv_create,model="点击创建队伍") #点击创建队伍
        self.wait_element_clickable(roomloc.spinner_mode, model="检查模式下拉选择框")
        # self.click_element(roomloc.spinner_mode,model="点击下拉选择框") #点击模式下拉选择框
        self.input_text(roomloc.et_desc, "能歌善舞。", model="输入要求")
        xsList = self.get_elements(roomloc.rv_reward) # 获取悬赏list元素
        xsList[0].click() # 点击某悬赏
        self.click_element(roomloc.btn_create, model="点击创建团队确定按钮")  #点击创建团队确定按钮
        self.assert_true(roomloc.create_assert) #断言创建团队是否成功
        self.exist_be_click(roomloc.mantle)
        

    # 解散队伍
    def click_dissolution(self):
        self.wait_element_clickable(roomloc.tv_disband, model="检查解散按钮是否存在")
        self.click_element(roomloc.tv_disband, model="点击解散按钮")
        assert "解散成功" in self.get_toast_exist("解散成功")
    
    
            

   #===================================更多======================================  


   
        
    























    '''登录成功后获取首页的title做断言'''
    '''在首页判断完成广告，获取title做断言'''
    def success_title(self):
        time.sleep(3)

        self.click_element(loc.btnSocial, model="点击探索")
        # else:
            # self.close_pop()
        self.wait_eleVisible(loc.loginsuccess, model="获取探索")
        assertlogin = self.get_text(loc.loginsuccess, model="获取探索")
        # CommonBus(self.driver).quit_login()
        return assertlogin

    

    
        

    '''处理所有弹窗'''

    def close_pop(self):
        s = time.time()
        self.advertising()
        self.close_language()
        self.closeGameInvit()
        self.test_ad()
        self.check_bounced()
        self.close_ivClose()
        self.close_tvTip()
        e = time.time()

    '''注册成功后获取首页title做断言'''

    def register_title(self):
        self.Adolescent_model()
        self.wait_eleVisible(loc.title, model="获取title")
        return self.get_text(loc.title, model="获取title")

    '''判断首页是否有广告'''

    def test_ad(self):
        if self.is_element_exist(loc.close_AD[1]):
            self.click_element(loc.close_AD, model="关闭首页广告")
        else:
            pass

    '''进入首页判断是否有临时广告'''

    def advertising(self):
        if self.is_element_exist(loc.AD[1], 1):
            self.click_element(loc.AD, model="临时点击跳过广告")
        else:
            pass

    '''进入首页判断是否有青少年模式'''

    def Adolescent_model(self):
        if self.is_element_exist(loc.Adolescent[1]):
            self.click_element(loc.Adolescent, model="关闭青少年模式")
        else:
            pass

    '''进入首页判断是否有签到'''

    def check_bounced(self):

        if self.is_element_exist(loc.check_shut[1]):
            self.click_element(loc.check_shut, model="点击签到弹框关闭按钮")
        else:
            pass

        # log.info("判断页面签到按钮")
        # try:
        #     bounced = self.get_element(loc.check, model="判断是否有签到按钮")
        # except NoSuchElementException:
        #     log.info("没有签到按钮")
        # else:
        #     bounced.click()
        #     self.click_element(loc.check_shut, model="点击签到弹框关闭按钮")

    '''关闭邀请弹窗'''

    def closeGameInvit(self):
        if self.is_element_exist(loc.closeGameInvit[1]):
            # self.wait_element_clickable(PopLoc.closeGameInvit, model="关闭游戏推荐")
            self.click_element(loc.closeGameInvit, model="点击关闭游戏推荐")
        else:
            pass

    def clickMy(self):
        self.wait_element_clickable(loc.click_me)
        self.click_element(loc.click_me, model="点击我的")

    '''关闭邀请入房通知'''

    def close_ivClose(self):
        if self.is_element_exist(PopUp.closeInvitInRoom[1]):
            self.click_element(PopUp.closeInvitInRoom, model="关闭邀请入房通知")
        else:
            pass

    '''关闭热门语言偏好'''

    def close_language(self):
        if self.is_element_exist(loc.txtSkip[1]):
            self.click_element(loc.txtSkip, model="点击跳过语言偏好设置")
        else:
            pass

    '''关闭开启直播气泡'''

    def close_tvTip(self):
        if self.is_element_exist(loc.tvTip[1]):
            self.click_element(loc.tvTip, model="点击开播气泡")
