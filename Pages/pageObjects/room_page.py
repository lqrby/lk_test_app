from re import M
from appium.webdriver.extensions.search_context import mobile
from attr import s
from Pages.pageObjects.Common_Buss import CommonBus
from Common.log import get_logger
import time, random
from TestDatas.IM import chatMessage
from Pages.pageLocators.pop_locators import PopUpLocator
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
        self.assert_true(roomloc.room_id,model="创建聊天室断言")
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
        self.exist_be_click(roomloc.close_ok)



    #聊天室列表
    def live_room_list(self):
        chat_room_list = self.get_elements(roomloc.chat_room_list)
        if len(chat_room_list) > 0:
            log.info("列表数据有{}条".format(len(chat_room_list)))
        else:
            log.info("暂无聊天室")
            self.save_webImgs(model="聊天室列表")
        self.check_goddess_Popup() #关闭女神引导弹窗
        return chat_room_list

    #进入聊天室内
    def enter_live_room(self,liveRoomList):
        if len(liveRoomList) > 0:
            room_number = random.randint(0,len(liveRoomList)-1)
            liveRoomList[room_number].click()
            self.wait_element_presence(roomloc.roomIdTv)
            self.assert_true(roomloc.roomIdTv,model="进入聊天室断言") #断言聊天室id
        else:
            self.save_webImgs(model="暂无聊天室")
            log.info("暂无聊天室")
            self.driver.close_app()
            self.driver.quit()


    
        
        
    '''
    功能:推荐聊天室
    '''
    def recommend_liveRoom(self):
        liveRoomList = self.live_room_list() #聊天室列表
        self.enter_live_room(liveRoomList) #随机进入聊天室
        if self.is_element_exist(roomloc.tv_queue): #队列
            log.info("进入了开黑聊天室")
            self.live_oom()
            self.click_rankingList(roomloc.ranking_list) #排行榜
            self.click_create_ranks() # 创建队伍 
            time.sleep(2)
            self.click_dissolution() # 解散队伍
            time.sleep(2)
            self.click_menu() #点击聊天室菜单
            self.close_room() #退出聊天室
        elif self.is_element_exist(roomloc.ranking_kuoLie): #扩列排行榜入口
            log.info("进入了扩列聊天室")
            self.live_oom()
            self.click_rankingList(roomloc.ranking_kuoLie) #扩列排行榜
            self.diamond_cash_back() #钻石返现-断言-返回
            self.click_menu() #点击聊天室菜单
            self.close_room(num=2) #退出聊天室
        elif self.is_element_exist(roomloc.head_picture): #头像
            log.info("进入了萌新接待聊天室")
            self.live_oom()
            self.click_menu() #点击聊天室菜单
            self.close_room() #退出聊天室
        elif self.is_element_exist(roomloc.receive_identifying): #领取
            log.info("进入了派对聊天室")
            self.live_oom()
            self.click_rankingList(roomloc.ranking_list) #排行榜
            self.click_receive() #领取按钮
            #幸运福袋
            # self.click_lucky_bag() #派对- 幸运福袋
            self.click_introduce() #点击玩法介绍，关闭玩法介绍（包括断言）
            self.click_menu() #点击聊天室菜单
            self.close_room() #退出聊天室
        else:
            log.info("迷路了，这是什么房间呀？？？")
            self.save_webImgs(model="未知聊天室截图")
            self.live_oom()
            self.click_menu() #点击聊天室菜单
            self.close_room() #退出聊天室
        return True
        


    
    '''
    点击未开播的用户
    功能:发现列表-查看用户资料用例
    '''
    def enter_notLiveRoom(self, number = 1):
        self.swipeDown()
        while number > 0:
            if self.is_element_exist(roomloc.tv_to_profile):
                self.click_element(roomloc.iv_close, model="关闭提升魅力弹窗")
            tv_desArr = self.get_elements(roomloc.tv_close)
            log.info("用户列表数据有{}条".format(len(tv_desArr)))
            self.close_back()
            if len(tv_desArr) > 0:
                for no_play in tv_desArr:
                    time.sleep(3)
                    no_play.click()
                    self.wait_element_presence(roomloc.tv_nick,model="资料tap-昵称")
                    self.assert_true(roomloc.tv_nick, model="资料tap-断言昵称") #资料tap-断言昵称
                    self.follow() #关注
                    self.click_more() #点击更多
                    self.cancel_follow() #取消关注
                    self.more_share() #断言分享更多
                    self.driver.keyevent(4) #返回
                    self.guardian() #守护者
                    time.sleep(2)
                    self.swipeUp() #向上滑动
                    time.sleep(1)
                    self.click_material() #资料tap
                    self.click_dynamic() #动态tap
                    self.click_exclusive_guard() #守护tap
                    self.click_exhibition_wall() #展墙tap
                    time.sleep(1)
                    self.login_Out() #退出登录
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
                # self.pop(PopUp.popList)
                log.info("向上滑动列表")
                self.swipeUp()
        return len(tv_desArr)
    
    
    '''
    附近的人--资料页用例
    '''
    def nearby_people_dataPage(self, num = 1):
        self.nearby_people() #附近的人tap
        return self.enter_notLiveRoom(number = num)
        
    '''
    附近的人---用户进入的聊天室用例
    '''
    def nearby_people_chatRoom(self, num = 1):
        self.nearby_people() #附近的人tap
        return self.enter_liveRoom(number = num)


    #附近的人tap
    def nearby_people(self):
        self.wait_element_clickable(roomloc.nearby_people,model="附近的人tap是否可点击")
        self.click_element(roomloc.nearby_people,model="点击附近的人tap")
        self.wait_element_presence(roomloc.rv) 


    #资料tap
    def click_material(self):
        self.wait_element_presence(roomloc.user_material,model="检查资料tap")
        self.click_element(roomloc.user_material,model="点击资料tap")
        self.wait_element_presence(roomloc.materialAssert,model="资料tap页元素")
        liKa_id = self.get_element(roomloc.liKa_id)
        self.assert_true(liKa_id)


    #动态tap
    def click_dynamic(self):
        self.wait_element_presence(roomloc.user_dynamic,model="检查动态tap")
        self.click_element(roomloc.user_dynamic,model="点击动态tap")
        self.wait_element_presence(roomloc.dynamic_tap_assert,model="动态tap页元素")
        dynamic_list = self.get_elements(roomloc.dynamic_list)
        self.assert_len(dynamic_list)


    #守护tap
    def click_exclusive_guard(self):
        self.wait_element_presence(roomloc.user_guard, model="检查守护tap")
        self.click_element(roomloc.user_guard, model="点击守护tap")
        self.wait_element_presence(roomloc.guard_tap_assert,model="守护tap页元素")
        self.assert_len(self.get_elements(roomloc.guard_list))
        
    
    #展墙tap
    def click_exhibition_wall(self):
        self.wait_element_presence(roomloc.War_wall,model="检查展墙tap")
        self.click_element(roomloc.War_wall,model="点击展墙tap")
        self.wait_element_presence(roomloc.materialAssert,model="展墙tap页元素")
        self.assert_len(self.get_elements(roomloc.War_wall_list)) #展墙断言
        if self.is_element_exist(roomloc.contribution):
            self.contribution() #贡献榜
        else:
            log.info("展墙tap---暂无贡献榜")
            self.save_webImgs(model="暂无贡献榜")
        self.gift_wall() #礼物展墙
        self.Dress_wall() #装扮展墙
        self.go_back() #返回列表页


    #守护者按钮
    def guardian(self):
        self.wait_element_clickable(roomloc.guardian, model="等待守护者显示")
        self.click_element(roomloc.guardian, model="点击守护者")
        time.sleep(1)
        if self.is_element_exist(roomloc.guardian_nickname):
            log.info("用户有守护者")
        else:
            log.info("该用户暂无守护者")
            self.save_webImgs(model="暂无守护者")
        self.go_back() #返回


    
    #展墙-贡献榜
    def contribution(self):
        self.wait_element_presence(roomloc.contribution, model="贡献榜")
        self.click_element(roomloc.contribution, model="点击贡献榜")
        self.diamond_list() #钻石榜
        time.sleep(1)
        self.swipeLeft() # 向左滑动
        time.sleep(1)
        self.Charm_list() #魅力榜
        self.swipeLeft() # 向左滑动
        time.sleep(1)
        self.guard_list() #守护榜
        self.go_back() #返回
        
        

    #左上角返回
    def go_back(self):
        self.wait_element_presence(roomloc.msg_backBtn, model="返回")
        self.click_element(roomloc.msg_backBtn, model="返回")
        time.sleep(1)

    #详情页返回
    def go_back_list(self):
        self.wait_element_presence(roomloc.backBtn, model="返回")
        self.click_element(roomloc.backBtn, model="返回")
        time.sleep(1)

    #展墙-钻石榜
    def diamond_list(self):
        # self.wait_element_presence(roomloc.masonry_list, model="钻石榜")
        # self.click_element(roomloc.masonry_list, model="钻石榜")
        if self.is_element_exist(roomloc.no_data):
            log.info("暂无数据")
            self.save_webImgs(model="钻石榜暂无数据")
        else:
            zs_list = self.get_elements(roomloc.masonry_list)
            self.assert_len(zs_list, dyj=1, model="钻石榜列表断言")
    
    
    #展墙-魅力榜
    def Charm_list(self):
        # self.wait_element_presence(roomloc.contributionList, model="魅力榜")
        # self.click_element(roomloc.masonry_list, model="魅力榜")
        if self.is_element_exist(roomloc.no_data):
            log.info("暂无数据")
            self.save_webImgs(model="魅力榜暂无数据")
        else:
            ml_list = self.get_elements(roomloc.masonry_list)
            print("ml_list====",len(ml_list))
            self.assert_len(ml_list, dyj=1, model="魅力榜列表断言")

    
    #展墙-守护榜
    def guard_list(self):
        # self.wait_element_presence(roomloc.contributionList, model="守护榜")
        # self.click_element(roomloc.masonry_list, model="守护榜")
        if self.is_element_exist(roomloc.no_data):
            log.info("暂无数据")
            self.save_webImgs(model="守护榜暂无数据")
        else:
            sh_list = self.get_elements(roomloc.masonry_list)
            self.assert_len(sh_list, dyj=1, model="守护榜列表断言")

    
    #====================礼物展墙================
    def gift_wall(self):
        self.wait_element_presence(roomloc.gift_wall, model="礼物展墙")  
        self.click_element(roomloc.gift_wall, model="礼物展墙")
        giftWallList = self.get_elements(roomloc.giftWallList)
        self.assert_len(giftWallList, dyj=1, model="礼物墙展墙列表断言")
        self.light_up() #点亮墙展礼物
        self.go_back()


    #====================装扮展墙================
    def Dress_wall(self):
        self.wait_element_presence(roomloc.decorate_wall, model="装扮展墙")  
        self.click_element(roomloc.decorate_wall, model="装扮展墙")
        Decorate_wall_list = self.get_elements(roomloc.Decorate_wall_list)
        self.assert_len(Decorate_wall_list, dyj=1, model="装扮墙展墙列表断言")
        self.go_back()

    
    #点亮墙展礼物
    def light_up(self, gift_number=2):
        j = 0
        while gift_number > 0:
            num = random.randint(0,4)
            if num > 0:
                self.swipeUp(t=1000,n=num)
            giftWallList = self.get_elements(roomloc.giftWallList)
            i = random.randint(0,len(giftWallList)-1)
            giftWallList[i].click()
            time.sleep(2)
            textStr = self.get_element(roomloc.Diamond_number_text).text
            number = "".join(list(filter(str.isdigit, textStr)))
            if int(number) > 50000:
                self.click_element(roomloc.cancel_btn,model="取消按钮")
                log.info("该礼物太贵了，换一个。")
                self.swipeDown_gift(t=1000,n=num)
            else:
                self.click_element(roomloc.close_ok, model="点亮按钮")
                time.sleep(2)
                j = j + 1
                log.info("=======点亮第{}次======".format(j))
                gift_number = gift_number - 1


    
    #礼物墙向上滑屏
    def swipeDown_gift(self, t=500, n=1):
        '''向下滑动屏幕'''
        time.sleep(0.5)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.43
        y2 = l['height'] * 0.93
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
    
    
    #关注
    def follow(self):
        if self.is_element_exist(roomloc.follow):
            self.click_element(roomloc.follow,model="点击关注")
            gz_toast = "关注成功"
            followSuccess = self.get_toast_msg(gz_toast, model="关注成功的toast")
            self.assert_in(gz_toast, followSuccess, model="关注用户") #断言关注
        else:
            pass

    #取消关注    
    def cancel_follow(self):
        if self.is_element_exist(roomloc.cancel_follow):
            time.sleep(1)
            self.click_element(roomloc.cancel_follow, model="点击取消关注")
            self.wait_element_presence(roomloc.Confirm_cancellation, model="等待确认按钮显示")
            self.click_element(roomloc.Confirm_cancellation, model="确认取消关注")
            cancelToast = "取消关注成功"
            toastMsg = self.get_toast_msg(cancelToast, model="取消关注成功的toast")  
            self.assert_in(cancelToast, toastMsg, model="取消关注") #取消关注断言
        else:
            pass

    
    #更多"..."
    def click_more(self):
        self.wait_element_clickable(roomloc.iv_more, model="更多") #更多
        self.click_element(roomloc.iv_more,model="点击更多")
        time.sleep(1)
    
    #断言更多分享长度
    def more_share(self):
        time.sleep(0.5)
        moreList = self.find_elements(roomloc.more_list) #更多list
        self.assert_len(moreList, dyj=7, model="更多列表断言")
        
    
    def send_message(self,msg_element,text_msg):
        self.wait_element_clickable(msg_element,model="检查消息按钮")
        self.click_element(msg_element,model="点击发消息按钮")
        self.wait_element_presence(roomloc.msg_input,model="消息输入框")
        self.input_text(roomloc.msg_input,text_msg,model="输入要发送的消息")
        self.wait_element_clickable(roomloc.send_message,model="发送按钮")
        self.click_element(roomloc.send_message,model="点击发送按钮")
        time.sleep(1)
        page_source_result = self.driver.page_source
        self.assert_in(text_msg,page_source_result,model="发送消息断言")
        self.driver.keyevent(4)

    
    #=======================================【房间】> 聊天室相关方法==============================================        

    #房间模块--->聊天室内操作（聊天室通用）
    def live_room(self):
        self.gift_entrance_top() #顶部礼物入口
        self.look_homeowner_data() #查看房主资料
        self.exist_be_click(roomloc.follow)#点击关注
        self.gift_entrance_bottom() # 底部礼物入口
        self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
        self.click_heat_value() # 房间用户及贵宾席
        self.click_blessing_bag() # 点击福袋
        self.click_wheat_lower() # 点击麦下  麦下取消功能
        self.click_game() #点击游戏并断言
        self.send_message(roomloc.iv_send_text,random.choice(chatMessage)) #发送消息并断言



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
            self.live_room() #聊天室内操作
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
            room_list[number].click()
            self.live_room() #聊天室内操作
            self.click_receive() #领取按钮
            time.sleep(1)
            self.click_menu() #点击聊天室菜单
            self.close_room(num=2) # 退出聊天室
            return True
        else:
            return False


    '''
    功能:进入扩列聊天室
    '''
    # def open_Expansion_room(self):
    #     self.swipeDown()
    #     self.driver.implicitly_wait(8)
    #     room_list = self.get_elements(roomloc.room_list_kaiHei)
    #     if len(room_list) > 0:
    #         number = random.randint(0, (len(room_list)-1))
    #         room_list[number].click()
    #         self.live_room() #聊天室内操作
    #         self.click_receive() #领取按钮
    #         time.sleep(1)
    #         self.click_menu() #点击聊天室菜单
    #         self.close_room(num=2) # 退出聊天室
    #         return True
    #     else:
    #         return False


    '''
    聊天室内菜单"..."
    '''
    def click_menu(self):
        self.wait_element_clickable(roomloc.room_menu, model="等待聊天室菜单可点击")
        self.click_element(roomloc.room_menu, model="点击聊天室菜单")#点击房间菜单


    #点击榜单
    def click_bangDan(self):
        self.wait_element_clickable(roomloc.room_module)
        self.click_element(roomloc.room_module, model="点击房间模块")#点击房间模块



    ###################################【房间】模块儿下的方法#############################################
    
    #点击房间[模块]
    def find_room(self):
        self.wait_element_clickable(roomloc.room_module)
        self.click_element(roomloc.room_module, model="点击房间模块")#点击房间模块

    #点击房间内的tap
    def room_tap(self, tap_element):
        self.wait_element_clickable(tap_element, model="检查tap")
        self.click_element(tap_element, model="点击tap") #点击tap



    #点击福袋
    def click_blessing_bag(self):
        self.wait_element_clickable(roomloc.lucky_bag_iv)
        self.click_element(roomloc.lucky_bag_iv, model="点击福袋")#点击福袋
        self.wait_eleVisible(roomloc.no_hair_message, model="等待显示‘不发送消息给好友’")
        self.assert_true(roomloc.no_hair_message) #福袋断言
        self.driver.keyevent(4)

    #派对-点击幸运福袋
    def click_lucky_bag(self):
        
        self.wait_element_clickable(roomloc.blessing_bag,model="福袋按钮")
        self.click_element(roomloc.blessing_bag, model="点击福袋按钮") #点击福袋按钮
        self.wait_eleVisible(roomloc.no_hair_message, model="等待显示‘不发送消息给好友’")
        self.assert_true(roomloc.no_hair_message) #福袋断言
        self.driver.keyevent(4)

    #点击扩列-钻石返现按钮   
    def diamond_cash_back(self):
        self.wait_element_clickable(roomloc.blessing_bag,model="钻石返现")
        self.click_element(roomloc.blessing_bag, model="点击钻石返现按钮") #钻石返现按钮
        self.assert_true(roomloc.cash_back_assert,model="钻石返现页面断言")
        self.go_back() #返回

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
            self.assert_in("领取成功", result, model="领取奖励断言")
            self.wait_element_presence(roomloc.play_instructions)
            self.click_element(roomloc.play_instructions, model="玩法说明按钮-可领取")
            time.sleep(2)
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
        self.wait_element_clickable(roomloc.open_black_recharge)
        self.click_element(roomloc.open_black_recharge)#点击礼物入口
  

    #开黑tap-礼物底部入口
    # def open_black_bottom(self):
    #     self.wait_element_clickable(roomloc.open_black_recharge)
    #     self.click_element(roomloc.open_black_recharge)#点击礼物入口
 
    #切换礼物tap
    def get_gift_tap(self):
        for i,tapBtn in enumerate(roomloc.gift_list):
            self.click_gift_tap(tapBtn) # 点击礼物tap
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
        self.assert_true(roomloc.personIdView) #用户资料断言（id）
        self.follow_ta() #关注
        self.chat() #聊天
        self.reward() #打赏，进入礼物页，点击资料再进入资料页
        self.ait_ta() #@ ta，然后返回，返回到了列表页
        

    #@ta
    def ait_ta(self):
        self.send_message(roomloc.reference,random.choice(chatMessage)) #@ta-发消息-断言
        

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

    

    #资料内点击返回
    def chat(self):
        self.wait_element_clickable(roomloc.msgBtn)
        self.click_element(roomloc.msgBtn,model="点击聊天") # 点击聊天
        self.go_back() #返回


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
    def click_rankingList(self,ranking_list):
        if self.is_element_exist(ranking_list):
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
            self.go_back() #返回
        

    #点击玩法介绍
    def click_introduce(self):
        time.sleep(2)
        if self.is_element_exist(roomloc.tv_introduce):
            self.click_element(roomloc.tv_introduce,model="点击玩法介绍")#点击玩法介绍  
            self.wait_element_presence(roomloc.tv_introduce_assert,model="玩法介绍内容")
            tv_introduce_assert = self.get_element(roomloc.tv_introduce_assert).text
            msg = ["一个秘密","性别女"] 
            self.click_introduce_assert(msg, tv_introduce_assert)
            self.click_element(roomloc.closeIv,model="关闭玩法介绍")#关闭玩法介绍
        else:
            pass
    

    #玩法介绍断言
    def click_introduce_assert(self,msg_assert_list,contain_text):
        mark = False
        for i in msg_assert_list:
            if i in contain_text:
                mark = True
                break
        try:
            assert mark == True
            log.info("玩法介绍===断言通过")
        except Exception as e:
            log.info("玩法介绍===断言错误")
            self.save_webImgs("玩法介绍断言错误截图")

    # #点击麦下
    def click_wheat_lower(self):
        # time.sleep(1)
        # self.click_wheatList()
        self.click_element(roomloc.layout_people,model="点击麦下") #点击麦下
        time.sleep(1)
        self.click_element(roomloc.layout_people,model="点击麦下") #点击麦下
        time.sleep(1)
        # self.click_wheatList()
    

    # 点击麦下用户列表
    def click_wheatList(self):
        if self.is_clickable(roomloc.iv_head_view):
            self.click_element(roomloc.iv_head_view,model="点击麦下收缩列表") #点击麦下收缩列表
            time.sleep(3)
            self.driver.keyevent(4)
        else:
            pass


    # 点击游戏
    def click_game(self):
        self.click_element(roomloc.iv_game,model="点击游戏") #点击游戏
        time.sleep(2)
        self.wait_element_presence(roomloc.game_assert,model="游戏列表")
        game_assert = self.get_elements(roomloc.game_assert)
        self.assert_len(game_assert,dyj=13, model="游戏列表断言")
        self.driver.keyevent(4)

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
        res = self.get_toast_exist("解散成功")
        self.assert_in("解散成功", res,model="解散队伍")
    
    
    
    #关闭女神开播引导弹窗
    def close_back(self):
        if self.is_element_exist(roomloc.close_back):
            self.click_element(roomloc.close_back,model="关闭女神开播引导弹窗") 
        else:
            pass
    

    '''
    附近动态流程
    '''
    def nearby_dynamics(self):
        self.nearby_dynamics_tap() #附近动态tap
        self.swipeDown() #刷新
        self.nearby_dynamics_list() #附近动态列表-进入动态详情
        self.spot_fabulous() #点赞
        self.click_follow() #关注
        self.click_more() #点击更多
        self.reportBtn() #举报
        self.assert_true(roomloc.commitBtn,model="举报断言") #举报断言
        self.go_back() #返回详情页
        self.go_back_list() #返回列表页



    #附近动态tap
    def nearby_dynamics_tap(self):
        self.wait_element_clickable(roomloc.tv_content,model="附近动态按钮是否可点击")
        self.click_element(roomloc.tv_content,model="点击附近动态tap")
        self.driver.implicitly_wait(8)
        self.wait_element_presence(roomloc.tv_nick,model="动态详情页的昵称")
        self.assert_true(roomloc.tv_nick,model="动态详情断言")


    #附近动态列表-进入动态详情
    def nearby_dynamics_list(self):
        nearby_dynamics_list = self.get_elements(roomloc.nearby_dynamics_list)   
        dt_num = random.randint(0,len(nearby_dynamics_list)-1) 
        nearby_dynamics_list[dt_num].click()




    #点赞
    def spot_fabulous(self):
        if self.is_clickable(roomloc.iv_prise):
            time.sleep(1)
            self.click_element(roomloc.iv_prise,model="点击点赞")
        else:
            log.info("已点过赞了")

    
    #关注
    def click_follow(self):
        if self.is_clickable(roomloc.follow):
            time.sleep(1)
            self.click_element(roomloc.follow,model="点击关注")
            gz_toast = "已关注"
            followSuccess = self.get_toast_msg(gz_toast, model="关注成功的toast")
            self.assert_in(gz_toast, followSuccess, model="关注用户") #断言关注
        else:
            pass

    #举报
    def reportBtn(self):
        self.wait_element_clickable(roomloc.reportBtn,model="举报按钮是否可点击")
        self.click_element(roomloc.reportBtn,model="点击举报按钮")
        time.sleep(1)
        