from Common.basepage import BasePage
from Pages.pageObjects.Common_Buss import CommonBus
from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
import time, random

from Pages.pageLocators.pop_locators import PopUp
from Pages.pageLocators.home_locators import HomePageLocator as HL
from appium.webdriver.common.mobileby import MobileBy as Mb

log = get_logger(logger_name="首页操作日志")

'''首页-页面操作'''

class HomePage(CommonBus):
    
    #进入直播间
    def enter_liveRoom(self, number = 1):
        while number > 0:
            tv_plays = self.get_elements(HL.tv_play)
            log.info("列表数据有{}条".format(len(tv_plays)))
            if len(tv_plays) > 0:
                for no_play in tv_plays:
                    time.sleep(3)
                    no_play.click()
                    self.gift_entrance_top() #顶部礼物入口
                    self.look_homeowner_data() #查看房主资料
                    self.wait_eleVisible(HL.roomIdTv) # 断言用户资料
                    self.gift_entrance_bottom() # 底部礼物入口
                    self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
                    

                    # self.click_heat_value() # 房间用户及贵宾席
                    # self.exist_be_click(HL.follow)#点击关注
                    # self.click_introduce() #点击玩法介绍，关闭玩法介绍
                    # self.click_wheat_lower() # 点击麦下  麦下取消功能
                    # self.click_game() #点击游戏
                    self.driver.keyevent(4)
                    number = number - 1
                    if number == 0:
                        break
                if number > 0:
                    if self.is_element_exist(HL.no_more):
                        log.info("显示了没有更多")
                        number = 0
                        break
                    else:
                        log.info("向上滑动列表")
                        self.swipeUp()
            elif self.is_element_exist(HL.no_more):
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
            tv_desArr = self.get_elements(HL.tv_close)
            log.info("列表数据有{}条".format(len(tv_desArr)))
            if len(tv_desArr) > 0:
                for no_play in tv_desArr:
                    time.sleep(3)
                    no_play.click()
                    self.wait_eleVisible(HL.tv_nick)
                    time.sleep(random.randint(5,7))
                    self.driver.keyevent(4)
                    time.sleep(1)
                    number = number - 1
                    if number == 0:
                        break
                if number > 0:
                    if self.is_element_exist(HL.no_more):
                        log.info("显示了没有更多")
                        number = 0
                        break
                    else:
                        log.info("向上滑动列表")
                        self.swipeUp()
            elif self.is_element_exist(HL.no_more):
                log.info("没有更多")
                number = 0
                break
            else:
                log.info("向上滑动列表")
                self.swipeUp()
        return len(tv_desArr)
    
    
    #点击福袋
    def click_blessing_bag(self):
        self.wait_element_clickable(HL.lucky_bag_iv)
        self.click_element(HL.lucky_bag_iv)#点击福袋
        self.driver.keyevent(4)

    
    #礼物顶部入口
    def gift_entrance_top(self):
        self.wait_element_clickable(HL.masterAvatarView)
        self.click_element(HL.masterAvatarView)#点击礼物入口

    #礼物底部入口
    def gift_entrance_bottom(self):
        self.wait_element_clickable(HL.iv_first_recharge)
        self.click_element(HL.iv_first_recharge)#点击礼物入口
 
    #切换礼物tap
    def get_gift_tap(self):
        for i,tapBtn in enumerate(HL.gift_list):
            self.click_gift_tap(tapBtn) # 点击某个tap
            self.select_gift() # 选中某个礼物
            self.give_gifts() # 赠送礼物
            if i >= 2:
                break
        self.driver.press_keycode(4)
        time.sleep(2)

    
    #点击某个礼物tap
    def click_gift_tap(self,tapBtn):
        self.wait_element_clickable(tapBtn)
        self.click_element(tapBtn) #点击某个礼物tap

    #选中某个礼物
    def select_gift(self):
        time.sleep(2)
        giftPages = self.get_elements(HL.gift_pages) #某tap下当前页的所有礼物元素
        if giftPages.__len__() > 0:
            number = random.randint(0, giftPages.__len__())
            self.click_element(HL.get_gift(number))
            # giftPages[number].click()
            time.sleep(2)
            
    #赠送礼物
    def give_gifts(self):
        self.wait_element_clickable(HL.btn_send_gift)
        self.click_element(HL.btn_send_gift) #点击某个礼物tap

    #查看房主资料
    def look_homeowner_data(self):
        self.wait_element_clickable(HL.homeowner_data)
        self.click_element(HL.homeowner_data) #点击房主资料
        data = self.driver.page_source
        self.wait_element_presence(HL.personIdView)
        self.wait_element_presence(HL.nick) #昵称
        self.follow_ta() #关注
        self.chat() #聊天
        self.reward() #打赏，进入礼物页，点击资料再进入资料页
        self.ait_ta() #@ ta，然后返回，返回到了列表页
        self.driver.press_keycode(4)

    #@ta
    def ait_ta(self):
        self.wait_element_clickable(HL.reference)
        self.click_element(HL.reference) # 点击@ta
        self.driver.press_keycode(4)

    #资料内点击关注
    def follow_ta(self):
        self.wait_element_clickable(HL.attentionBtn)
        self.click_element(HL.attentionBtn) # 点击关注

    #资料内点击打赏
    def reward(self):
        self.wait_element_clickable(HL.sendBtn)
        self.click_element(HL.sendBtn) # 点击打赏
        self.wait_element_clickable(HL.homeowner_data)
        self.click_element(HL.homeowner_data) #点击房主资料

    #资料内点击聊天
    def chat(self):
        self.wait_element_clickable(HL.msgBtn)
        self.click_element(HL.msgBtn) # 点击聊天
        self.wait_element_clickable(HL.msg_backBtn)
        self.click_element(HL.msg_backBtn) # 点击返回


    # 点击房间热度值
    def click_heat_value(self):
        self.wait_element_clickable(HL.tv_heat)
        self.click_element(HL.tv_heat) #点击某个礼物tap
        time.sleep(2)
        self.wait_element_clickable(HL.heat_value)
        self.click_element(HL.heat_value) #在线列表
        time.sleep(2)
        self.wait_element_clickable(HL.vip_seat)
        self.click_element(HL.vip_seat) #贵宾席位列表
        self.driver.press_keycode(4)
        time.sleep(2)

    #点击排行榜
    def click_rankingList(self):
        self.wait_element_clickable(HL.ranking_list)
        self.click_element(HL.ranking_list) #点击排行榜
        time.sleep(2)
        self.wait_element_clickable(HL.contribution_list)
        self.click_element(HL.contribution_list) #点击贡献榜
        time.sleep(2)
        self.wait_element_clickable(HL.popularity_list)
        self.click_element(HL.popularity_list) #点击人气榜
        time.sleep(2)
        self.wait_element_clickable(HL.guardian_list)
        self.click_element(HL.guardian_list) #点击守护榜
        time.sleep(2)
        self.driver.press_keycode(4)
        time.sleep(2)

    #点击玩法介绍
    def click_introduce(self):
        time.sleep(2)
        self.click_element(HL.tv_introduce)#点击玩法介绍  
        time.sleep(1)
        result = self.driver.page_source
        assert "一" in result
        self.click_element(HL.closeIv)#关闭玩法介绍
    
    #点击麦下
    def click_wheat_lower(self):
        time.sleep(1)
        self.click_wheatList()
        self.click_element(HL.layout_people)#点击麦下
        time.sleep(1)
        self.click_wheatList()
    
    # 点击麦下用户列表
    def click_wheatList(self):
        if self.is_element_exist(HL.iv_head_view):
            self.click_element(HL.iv_head_view)#点击麦下收缩列表
            time.sleep(2)
            self.driver.keyevent(4)
        else:
            pass

    # 点击游戏
    def click_game(self):
        self.click_element(HL.iv_game)#点击游戏
        time.sleep(2)
            

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
