from Pages.pageObjects.Common_Buss import CommonBus
from Common.log import get_logger
import time, random
from TestDatas.IM import chatMessage
from Pages.pageObjects.sign_pop_page import SignPopPage
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from Pages.pageLocators.home_locators import HomePageLocator as homeloc


log = get_logger(logger_name="首页操作日志")

'''首页-页面操作'''

class RoomPage(CommonBus):
    def __init__(self, driver):
        self.driver = driver
        self.popPage = SignPopPage(self.driver)
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
        if self.entry_room(): #点击确认创建房间按钮
            if self.is_element_exist(roomloc.layout_room_info_top) or self.is_element_exist(roomloc.ignore1):
                log.info("创建小窝聊天室断言成功")
                self.exit_chat_room() #退出聊天室
                return True
            else:
                log.info("创建小窝聊天室断言失败")
                self.save_webImgs(model="创建小窝聊天室")
        else:
            return False

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
        if self.entry_room(): #点击确认创建房间按钮
            self.assert_true(roomloc.ignore1,model="创建房间id")
            self.exit_chat_room() #退出聊天室
            return True
        else:
            return False


    #===================================开小窝/萌新接待房间子方法======================================     
    #创建聊天室入口
    def menuIv(self):
        self.wait_element_clickable(roomloc.menuIv)
        self.click_element(roomloc.menuIv, model="点击创建聊天室入口按钮")

    #选择房间类型
    def room_type(self,num=1):
        self.wait_element_presence(roomloc.room_type,model="房间类型")
        room = self.find_elements(roomloc.room_type)
        room[num].click()

    #选择房间标签
    def room_label(self):
        self.wait_element_presence(roomloc.room_label,model="房间标签")
        roomLabels = self.find_elements(roomloc.room_label)
        labelNum = random.randint(0,(len(roomLabels)-1))
        roomLabels[labelNum].click()
        
    #选择房间话题
    def room_name(self):
        roomName = "创建房间-{}".format(int(time.time()))
        self.wait_element_presence(roomloc.room_name,model="房间话题")
        self.clear_input_text(roomloc.room_name, model="清除输入框默认文本")
        self.input_text(roomloc.room_name, roomName, model="输入房间话题")

    #选择房间座位数
    def room_seat(self):
        self.wait_element_presence(roomloc.room_seat,model="房间座位")
        roomSeats = self.find_elements(roomloc.room_seat)
        seatNum = random.randint(0,(len(roomSeats)-1))
        roomSeats[seatNum].click()
        
    #点击确认创建房间按钮
    def entry_room(self):
        self.wait_element_clickable(roomloc.entry_room,model="创建房间按钮")
        self.click_element(roomloc.entry_room, model="点击确认创建房间按钮")
        message = "需官方授权可开启"
        message_toast = self.get_toast_exist(message,model='获取toast')
        if message in message_toast:
            log.info("toast======={}".format(message_toast))
            self.save_webImgs(model="创建聊天室失败截图")
            return False
        else:
            return True


    #房间菜单按钮
    def room_menu(self):
        self.wait_element_clickable(roomloc.room_menu,timeout=4,model="等待房间菜单")
        self.click_element(roomloc.room_menu, model="点击房间菜单")
        
    #退出聊天室
    def close_room(self):
        if self.is_element_exist(roomloc.exit_room,timeout=3,model="退出房间"):
            self.click_element(roomloc.exit_room,model="点击退出房间")
            res = self.is_element_exist(roomloc.give_up_reward,timeout=3,model="放弃奖励元素")
            if res:
                return self.click_element(roomloc.give_up_reward,model="点击放弃奖励")
            else:
                return True
        elif self.is_element_exist(roomloc.close_room,timeout=3,model="关闭房间元素"):
            self.click_element(roomloc.close_room,model="点击关闭房间")
            if self.is_element_exist(roomloc.close_ok,model="确定按钮"):
                return self.click_element(roomloc.close_ok,model="点击确定")
            else:
                return True
            

    #退出聊天室
    def exit_chat_room(self):
        self.room_menu()
        res = self.close_room()
        return res


    #聊天室列表
    def live_room_list(self,room_list_elements):
        roomList = False
        if self.is_element_exist(room_list_elements,model="聊天室列表元素是否存在"):
            roomList = self.get_elements(room_list_elements,model="获取聊天室列表")
        else:
            log.info("暂无聊天室")
            self.save_webImgs(model="暂无聊天室")
        self.popPage.check_goddess_Popup() #关闭女神引导弹窗
        return roomList
    

    #进入聊天室内
    def enter_live_room(self,liveRoomList):
        if len(liveRoomList) > 0:
            room_number = random.randint(0,len(liveRoomList)-1)
            liveRoomList[room_number].click()
            if self.is_element_exist(roomloc.room_text,timeout=3,poll_frequency=0.3,model="房间密码"):
                log.info("能到这里吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？")
                self.click_element(roomloc.closeRoomText,model="关闭聊天室输入密码框")
                log.info("该聊天室有密码，无法进入")
                self.save_webImgs(model="聊天室有密码")
                return False
            self.popPage.check_put_away() #收起聊天室邀请加入队伍的页面
            self.assert_true(roomloc.roomIdTv,model="聊天室id") #断言聊天室id
            return True
        else:
            self.save_webImgs(model="暂无聊天室")
            log.info("暂无聊天室")
            return False

    '''
    功能:临时测试聊天室
    '''
    # def testrecommend_liveRoom(self):
    #     self.find_room() #点击房间模块
    #     blackTap = self.room_tap(roomloc.recommend_tap,model="推荐tap") #点击推荐tap
    #     if blackTap == False:
    #         return {"result":True,"message":"暂无推荐tap"}
    #     # self.swipeUp(n=3)
    #     res = self.is_element_exist(roomloc.chat_room_list,model='聊天室列表')
    #     if res == False:
    #         log.info("推荐列表暂无房间可进入")
    #         self.save_webImgs(model="推荐列表暂无房间可进入")
    #         return {"result":False,"message":"推荐列表暂无房间可进入"}
        
    #     liveRoomList = self.live_room_list(roomloc.chat_room_list) #聊天室列表
    #     # print("liveRoomList=====",liveRoomList)
    #     self.enter_live_room(liveRoomList) #随机进入聊天室
    #     self.bottom_more()
    #     # self.liveRoom() #聊天室内操作
    #     # self.click_game() #点击游戏并断言
    #     # self.enter_the_game(roomloc.jbtq,roomloc.taoquan_btn,model="金币套圈") #进入金币套圈游戏并断言
    #     # time.sleep(2)
    #     # self.enter_the_game(roomloc.trap,roomloc.taoquan_btn,model="套圈圈") #进入套圈圈游戏并断言
    #     # time.sleep(2)
    #     # self.enter_the_game(roomloc.Koi_blind_box,roomloc.purchase_btn,model="锦鲤盲盒") #进入锦鲤盲盒游戏并断言
    #     # time.sleep(2)
    #     # self.enter_the_game(roomloc.jungle_hunt,roomloc.hemp_rope,click_num=1,model="丛林狩猎") #进入丛林狩猎游戏并断言
    #     return {"result":True}

    '''
    功能:推荐聊天室
    '''
    def recommend_liveRoom(self):
        self.find_room() #点击房间模块
        blackTap = self.room_tap(roomloc.recommend_tap,model="推荐tap") #点击推荐tap
        if blackTap == False:
            return {"result":True,"message":"暂无推荐tap"}
        res = self.is_element_exist(roomloc.chat_room_list,model="房间列表")
        if res == False:
            log.info("推荐列表暂无房间可进入")
            self.save_webImgs(model="推荐列表暂无房间可进入")
            return {"result":False,"message":"推荐列表暂无房间可进入"}
        liveRoomList = self.live_room_list(roomloc.chat_room_list) #聊天室列表
        self.enter_live_room(liveRoomList) #随机进入聊天室
        self.liveRoom() #聊天室内操作
        return {"result":True}

    '''
    发现列表进入用户所在的聊天室
    '''
    def enter_liveRoom(self):
        # 在聊天室的用户
        self.wait_click_element(homeloc.dating_module)#点击交友模块
        self.wait_click_element(homeloc.tv_content_fx)#点击发现tap
        time.sleep(2)
        self.close_page_popUp()
        self.swipeDown()
        time.sleep(3)
        playList = self.live_room_list(roomloc.tv_play) 
        if playList:
            self.enter_live_room(playList) #随机进入聊天室
            self.liveRoom()
            return True
        else:
            return False

    def liveRoom(self):
        self.live_room() #关注、游戏、发消息、礼物入口
        if self.is_element_exist(roomloc.ranking_list,timeout=5,model="排行榜"): #是否有排行榜
            self.click_rankingList(roomloc.ranking_list) #排行榜
        self.createRanks_and_dissolution() #创建队伍并解散队伍
        # self.click_receive() #领取按钮
        #幸运福袋
        self.click_introduce() #点击玩法介绍，关闭玩法介绍（包括断言）
        self.bottom_more() #聊天室内更多相关操作流程
        return self.exit_chat_room() #退出聊天室
        

    '''
    点击未开播的用户
    功能:发现列表-查看用户资料用例
    '''
    def enter_notLiveRoom(self):
        self.wait_click_element(homeloc.dating_module,model="点击交友模块")
        time.sleep(2)
        self.close_page_popUp()
        self.swipeDown()
        self.wait_element_presence(roomloc.cc_layout,model="用户列表")
        return self.user_homePage(roomloc.tv_close)
        
    
    #资料页操作
    def user_homePage(self,element_list,element_arr=None):
        tv_desArr = self.get_list(element_list,model="获取用户列表元素")
        if tv_desArr and len(tv_desArr) > 0:
            return self.view_user_profile(tv_desArr)
        elif element_arr != None:
            layout_info_arr = self.get_list(element_arr,model="获取用户列表元素2")
            if layout_info_arr and len(layout_info_arr) > 0:
                return self.view_user_profile(layout_info_arr)
        elif self.is_element_exist(roomloc.no_more,model="没有更多") == False:
            log.info("当前页暂无进入聊天室用户，上拉加载")
            self.swipeUp()
            return self.user_homePage(element_list)
        elif self.is_element_exist(roomloc.no_data,model="暂无数据"):
            self.save_webImgs(model="列表暂无数据截图")
            log.info("列表暂无数据")    
            return False
        else:
            self.save_webImgs(model="列表暂无用户进入聊天室")
            log.info("列表暂无用户进入聊天室")    
            return False
    
    
    def view_user_profile(self,resultList): #查看用户资料
        log.info("用户列表有{}条数据".format(len(resultList)))
        no_play = random.choice(resultList)
        no_play.click()
        self.wait_element_presence(roomloc.tv_nick,model="用户昵称")
        self.assert_true(roomloc.tv_nick, model="断言用户昵称") #资料tap-断言昵称
        self.follow() #关注
        self.click_more() #点击更多
        self.more_share() #断言分享更多
        self.cancel_follow() #取消关注
        self.guardian() #守护者
        self.swipeUp() #向上滑动
        time.sleep(1)
        self.click_material() #资料tap
        self.click_dynamic() #动态tap
        self.click_exclusive_guard() #守护tap
        self.click_exhibition_wall() #展墙tap
        self.login_Out() #退出登录
        return True

        
    def my_information(self): #查看我的资料
        self.wait_element_presence(roomloc.tv_nick_name,model="我的昵称")
        self.assert_true(roomloc.tv_nick_name, model="断言我的昵称") #资料tap-断言昵称
        self.guardian() #守护者
        self.swipeUp() #向上滑动
        time.sleep(1)
        self.click_material() #资料tap
        self.click_dynamic() #动态tap
        self.click_exclusive_guard() #守护tap
        self.click_exhibition_wall() #展墙tap
        # self.login_Out() #退出登录
        return True
    
    
    '''
    附近的人--资料页用例
    '''
    def nearby_people_dataPage(self):
        self.wait_click_element(homeloc.dating_module,model="点击交友模块")
        self.nearby_people() #附近的人tap
        self.close_page_popUp()
        self.swipeDown()
        self.wait_element_presence(roomloc.tv_close,model="用户列表")
        return self.user_homePage(roomloc.tv_close)
        
    '''
    附近的人---用户进入的聊天室用例
    '''
    def nearby_people_chatRoom(self):
        self.wait_click_element(homeloc.dating_module,model="点击交友模块")
        self.nearby_people() #附近的人tap
        return self.enter_liveRoom()


    #附近的人tap
    def nearby_people(self):
        self.wait_element_clickable(roomloc.nearby_people,model="附近的人tap是否可点击")
        self.click_element(roomloc.nearby_people,model="点击附近的人tap")
        # self.wait_element_presence(roomloc.rv) 
        if self.is_element_exist(roomloc.tv_close,model="用户未进入聊天室元素"):
            log.info("附近的人列表断言通过")
        else:
            log.info("附近的人列表暂无数据")
            self.save_webImgs(model="附近的人列表暂无数据")


    #资料tap
    def click_material(self):
        self.wait_element_presence(roomloc.user_material,model="检查资料tap")
        self.click_element(roomloc.user_material,model="点击资料tap")
        self.swipeUp()
        self.wait_element_presence(roomloc.liKa_id,model="用户哩咔id")
        lk_id = self.get_element(roomloc.liKa_id,model="哩咔id").get_attribute("text")
        log.info("哩咔ID:{}".format(lk_id))
        self.assert_true(roomloc.liKa_id, model="资料tap断言-哩咔id")


    #动态tap
    def click_dynamic(self):
        self.wait_element_presence(roomloc.user_dynamic,model="动态tap")
        self.click_element(roomloc.user_dynamic,model="点击动态tap")
        if self.is_element_exist(roomloc.dynamic_list,timeout=3,model="动态列表"):
            self.assert_len(roomloc.dynamic_list, model="断言动态tap列表")
        elif self.is_element_exist(roomloc.no_data,timeout=3,model="是否暂无动态元素"):
            log.info("该用户暂无动态")
            self.save_webImgs(model="暂无动态")
        


    #守护tap
    def click_exclusive_guard(self):
        self.wait_element_presence(roomloc.user_guard, model="检查守护tap")
        self.click_element(roomloc.user_guard, model="点击守护tap")
        if self.is_element_exist(roomloc.guard_list,model="用户守护"):
            self.assert_len(roomloc.guard_list,model="断言守护列表")
        else:
            log.info("暂无守护tap")
            self.save_webImgs(model="暂无守护tap")
        
    
    #展墙tap
    def click_exhibition_wall(self):
        self.wait_element_presence(roomloc.War_wall,model="检查展墙tap")
        self.click_element(roomloc.War_wall,model="点击展墙tap")
        self.assert_true(roomloc.War_wall_list,model="展墙tap页断言")
        if self.is_element_exist(roomloc.contribution,model="贡献榜"):
            self.contribution() #贡献榜
        else:
            log.info("用户隐藏了贡献榜")
            self.save_webImgs(model="用户隐藏了贡献榜")
        if self.is_element_exist(roomloc.gift_wall,model="礼物展墙"):
            self.gift_wall() #礼物展墙
        else:
            log.info("用户隐藏了礼物展墙")
            self.save_webImgs(model="用户隐藏了礼物展墙")
        self.Dress_wall() #装扮展墙
        self.go_back() #返回列表页


    #守护者按钮
    def guardian(self):
        if self.is_element_exist(roomloc.guardian,model="守护者"):
            self.click_element(roomloc.guardian, model="点击守护者")
            if self.is_element_exist(roomloc.guardian_nickname,model="守护者昵称"):
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
        time.sleep(1)
        if self.is_element_exist(roomloc.msg_backBtn,model="聊天返回"):
            self.click_element(roomloc.msg_backBtn, model="返回")
        elif self.is_element_exist(roomloc.backBtn,model="详情页返回"):
            self.click_element(roomloc.backBtn, model="返回")
        else:
            log.info("没有查找到返回元素")
            self.save_webImgs(model="没有查找到返回元素")
            self.driver.press_keycode(4)


    #详情页返回
    def go_back_list(self):
        self.wait_element_presence(roomloc.backBtn, model="返回")
        self.click_element(roomloc.backBtn, model="返回")
        time.sleep(1)

    #展墙-钻石榜
    def diamond_list(self):
        if self.is_element_exist(roomloc.masonry_list,model="钻石榜列表"):
            zs_list = self.get_elements(roomloc.masonry_list,model="获取钻石榜列表")
            self.assert_len(roomloc.masonry_list, dyj=0, model="断言钻石榜列表")
        else:
            log.info("暂无数据")
            self.save_webImgs(model="钻石榜暂无数据")
    
    #展墙-魅力榜
    def Charm_list(self):
        if self.is_element_exist(roomloc.masonry_list,model="魅力榜列表"):
            self.assert_len(roomloc.masonry_list, dyj=0, model="断言魅力榜列表")
        else:
            log.info("暂无数据")
            self.save_webImgs(model="魅力榜暂无数据")

    #展墙-守护榜
    def guard_list(self):
        if self.is_element_exist(roomloc.no_data,model="有无数据"):
            log.info("守护榜暂无数据")
            self.save_webImgs(model="守护榜暂无数据")
        else:
            self.assert_len(roomloc.masonry_list, dyj=0, model="断言守护榜列表")

    
    #====================礼物展墙================
    def gift_wall(self):
        self.wait_click_element(roomloc.gift_wall, model="礼物展墙") #点击礼物展墙
        giftwaill = self.is_element_exist(roomloc.giftWallList,model="礼物展墙") #礼物展墙列表是否存在
        if giftwaill:
            bool = self.assert_len(roomloc.giftWallList, dyj=0, model="断言礼物展墙列表")
            if bool:
                # self.light_up() #点亮墙展礼物
                log.info("展墙列表有点亮的礼物")
                self.go_back()
            else:
                log.info("展墙列表没有点亮的礼物")
                self.driver.press_keycode(4)
                self.go_back()
        else:
            log.info("礼物展墙暂无点亮的礼物")
            self.save_webImgs(model="礼物展墙暂无点亮的礼物")
            self.driver.press_keycode(4)
            time.sleep(2)
            self.go_back()
            if self.is_element_exist(roomloc.War_wall_list,model="展墙断言"):
                pass
            else:
                log.info("见鬼了")
                self.go_back()

    #====================装扮展墙================
    def Dress_wall(self):
        self.wait_element_presence(roomloc.decorate_wall, model="装扮展墙")  
        self.click_element(roomloc.decorate_wall, model="点击装扮展墙")
        self.wait_element_presence(roomloc.Decorate_wall_list,model="装扮展墙列表")
        self.assert_len(roomloc.Decorate_wall_list, dyj=1, model="断言装扮展墙列表")
        self.go_back()

    
    #点亮墙展礼物
    def light_up(self, gift_number=2):
        j = 0
        while gift_number > 0:
            num = random.randint(0,4)
            if num > 0:
                self.swipeUp(t=1000,n=num)
            giftWallList = self.get_elements(roomloc.giftWallList,model="获取展墙礼物列表")
            i = random.randint(0,len(giftWallList)-1)
            giftWallList[i].click() #点击打赏
            time.sleep(2)
            textStr = self.get_element(roomloc.Diamond_number_text,model="获取弹窗中的文本").text  #确定弹窗中text
            log.info("文本内容:{}".format(textStr))
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
        if self.is_element_exist(roomloc.follow,model="关注"):
            self.click_element(roomloc.follow,model="点击关注")
            # gz_toast = "关注成功"
            # followSuccess = self.get_toast_msg(gz_toast, model="关注成功的toast")
            # self.assert_in(gz_toast, followSuccess, model="关注用户") #断言关注
            self.assert_true(roomloc.follow, model="断言关注用户") #断言关注
        else:
            pass

    #取消关注    
    def cancel_follow(self):
        if self.is_element_exist(roomloc.cancel_follow,model="取消关注"):
            time.sleep(1)
            self.click_element(roomloc.cancel_follow, model="点击取消关注")
            self.wait_element_presence(roomloc.Confirm_cancellation, model="确认按钮显示")
            self.click_element(roomloc.Confirm_cancellation, model="确认取消关注")
            # cancelToast = "取消关注成功"
            # toastMsg = self.get_toast_msg(cancelToast, model="取消关注成功的toast")  
            # self.assert_in(cancelToast, toastMsg, model="取消关注") #取消关注断言
            self.assert_true(roomloc.cancel_follow,model="断言取消关注")
        else:
            self.driver.press_keycode(4)

    
    #更多"..."
    def click_more(self):
        self.wait_element_clickable(roomloc.iv_more, model="更多") #更多
        self.click_element(roomloc.iv_more,model="点击更多")
        
    
    #断言更多分享长度
    def more_share(self):
        if self.is_element_exist(roomloc.gv_list,model="更多列表"):
            self.assert_len(roomloc.gv_list, dyj=7, model="断言更多列表")
        else:
            log.info("分享更多列表错误")
            self.save_webImgs(model="分享更多列表错误")
        
    
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
        self.driver.press_keycode(4)

    
    #=======================================【房间】> 聊天室相关方法==============================================        

    #房间模块--->聊天室内操作（聊天室通用）
    def live_room(self):
        if self.is_element_exist(roomloc.all_mode,timeout=3,model="全部模式"):
            self.driver.press_keycode(4)
        self.exist_be_click(roomloc.follow,model="关注")#点击关注
        self.gift_entrance_top() #顶部礼物入口》查看房主资料》关注，@她，聊天，金币打赏，背包小花打赏等
        self.gift_entrance_bottom() # 底部礼物入口》切换礼物tap，选中礼物，赠送礼物,返回，房间用户及贵宾席
        self.click_game() #点击游戏并断言
        self.send_message(roomloc.iv_send_text,random.choice(chatMessage)) #发送消息并断言


    '''
    功能:进入开黑聊天室
    '''
    def open_black_room(self):
        self.find_room() #点击房间模块
        blackTap = self.room_tap(roomloc.open_black_tap,model="开黑tap") #点击开黑tap
        if blackTap == False:
            return {"result":True,"message":"暂无开黑tap"}
        self.popPage.check_MinorSettings() #检测未成年弹框
        self.swipeDown()
        log.info("刷新列表")
        room_list =self.get_list(roomloc.chat_room_list,model="开黑聊天室列表") #房间列表
        number = random.randint(0, (len(room_list)-1))
        if len(number) > 0:
            room_list[number].click()
            self.live_room() #聊天室内操作
            time.sleep(2)
            self.createRanks_and_dissolution() #创建队伍并解散队伍
            exit_res = self.exit_chat_room() #退出聊天室
            return {"result":exit_res,"message":exit_res}
        else:
            return {"result":False,"message":'开黑列表为空'}
        

    '''
    功能:进入派对聊天室
    '''
    def open_party_room(self):
        self.find_room() #点击房间模块
        blackTap = self.room_tap(roomloc.party_tap,model="派对聊天室") #点击派对tap
        if blackTap == False:
            return {"result":True,"message":"暂无开黑tap"}
        self.swipeDown()
        res = self.is_element_exist(roomloc.chat_room_list,model="聊天室列表")
        if res:
            room_list =self.get_list(roomloc.chat_room_list,model="派对聊天室列表") #房间列表
            number = random.randint(0,(len(room_list)-1))
            room_list[number].click()
            self.live_room() #聊天室内公共操作方法
            self.click_receive() #领取按钮
            time.sleep(1)
            exit_res = self.exit_chat_room() #退出聊天室
            return {"result":exit_res}
        else:
            log.info("派对列表暂无可进入的房间")
            self.save_webImgs(model="派对列表暂无可进入的房间")
            return {"result":False,"message":"派对列表暂无可进入的房间"}

    '''
    功能:关注-进入聊天室
    '''
    def follow_room(self):
        self.find_room() #点击房间模块
        blackTap = self.room_tap(roomloc.follow_tap,model="关注聊天室") #点击关注tap
        if blackTap == False:
            return {"result":True,"message":"暂无关注tap"}
        self.swipeDown()
        res = self.is_element_exist(roomloc.chat_room_list,model="聊天室列表")
        if res:
            room_list =self.get_list(roomloc.chat_room_list,model="关注聊天室列表") #房间列表
            number = random.randint(0,(len(room_list)-1))
            room_list[number].click()
            self.live_room() #聊天室内公共操作方法
            self.click_receive() #领取按钮
            time.sleep(1)
            exit_res = self.exit_chat_room() #退出聊天室
            return {"result":exit_res}
        else:
            log.info("关注列表暂无可进入的房间")
            self.save_webImgs(model="关注列表暂无可进入的房间")
            return {"result":False,"message":"关注列表暂无可进入的房间"}
        

    '''
    功能:进入扩列聊天室
    '''
    def open_Expansion_room(self):
        self.swipeDown()
        if self.is_element_exist(roomloc.chat_room_list,model="聊天室列表") == False:
            log.info("扩列列表暂无可进入的房间")
            self.save_webImgs(model="扩列列表暂无可进入的房间")
            return False
        room_list =self.get_list(roomloc.chat_room_list,model="扩列聊天室列表") #房间列表
        if room_list and len(room_list) > 0:
            number = random.randint(0, (len(room_list)-1))
            room_list[number].click()
            time.sleep(1)
            self.live_room() #聊天室内操作
            self.click_receive() #领取按钮
            time.sleep(1)
            exit_res = self.exit_chat_room() #退出聊天室
            return exit_res
        else:
            return False

    def get_list(self, list_element,model=None):
        if self.is_element_exist(list_element,model=model):
            list_elements = self.get_elements(list_element,model="获取{}元素".format(model))
            return list_elements
        else:
            return False
        


    #点击榜单
    def click_bangDan(self):
        self.wait_element_clickable(roomloc.room_module)
        self.click_element(roomloc.room_module, model="点击房间模块")#点击房间模块



    ###################################【房间】模块儿下的方法#############################################
    
    #点击房间[模块]
    def find_room(self):
        self.wait_element_clickable(roomloc.room_module,model="房间模块")
        self.click_element(roomloc.room_module, model="点击房间模块")#点击房间模块
            

    #点击房间模块的*tap
    def room_tap(self, tap_element,model=None):
        if self.is_element_exist(tap_element, model=model):
            self.click_element(tap_element, model=model) #点击tap
            return True
        else:
            log.info("暂无{}".format(model))
            self.save_webImgs(model="暂无{}".format(model))
            return False

    #点击福袋
    def click_blessing_bag(self):
        self.wait_element_clickable(roomloc.lucky_bag_iv)
        self.click_element(roomloc.lucky_bag_iv, model="点击福袋")#点击福袋
        self.wait_eleVisible(roomloc.no_hair_message, model="等待显示‘不发送消息给好友’")
        self.assert_true(roomloc.no_hair_message) #福袋断言
        self.driver.press_keycode(4)


    #点击扩列-钻石返现按钮   
    def diamond_cash_back(self):
        self.wait_element_clickable(roomloc.Lucky_bag,model="钻石返现")
        self.click_element(roomloc.Lucky_bag, model="点击钻石返现按钮") #钻石返现按钮
        self.assert_true(roomloc.cash_back_assert,model="钻石返现页面断言")
        self.go_back() #返回

    # 领取入口
    def click_receive(self):
        if self.is_element_exist(roomloc.receive,model="签到领取"):
            self.wait_click_element(roomloc.receive, model="领取按钮")
            self.wait_eleVisible(roomloc.for_her, model="等待显示为ta点亮tap")
            self.assert_true(roomloc.for_her,model="为ta点亮tap") #断言
            self.wait_click_element(roomloc.sign_in, model="气泡签到或领取")
            self.wait_click_element(roomloc.receiveBtn, model="领取按钮")
            result = self.get_toast_exist(message='领取成功')
            self.assert_in("领取成功", result, model="领取奖励断言")
            self.wait_click_element(roomloc.play_instructions,model="玩法说明")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
        elif self.is_element_exist(roomloc.count_down_receive,model="倒计时"):
            self.click_element(roomloc.count_down_receive, model="点击领取倒计时按钮")
            self.wait_click_element(roomloc.play_instructions,model="玩法说明")
            time.sleep(2)
            wfsm_source = self.driver.page_source
            text_wfsm = "每日收取全部奖励连续3/5/7天时当天奖励翻倍"
            self.assert_in(text_wfsm,wfsm_source,model="断言玩法说明")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
        else:
            log.info("该聊天室无领取按钮")
            self.save_webImgs(model="该聊天室无领取按钮")
            
        
    #抽奖tap
    def click_luck_draw(self):
        self.wait_element_clickable(roomloc.luck_draw)
        self.click_element(roomloc.luck_draw, model="点击抽奖tap")
        '''
        后续写H5脚本
        '''
    #礼物顶部入口
    def gift_entrance_top(self):
        masterAvatarView = ""
        if self.is_element_exist(roomloc.masterAvatarView,model="打赏礼物入口"):
            masterAvatarView = self.wait_element_presence(roomloc.masterAvatarView,timeout=5,model="顶部送礼物入口")
        else:
            masterAvatarView = self.wait_element_presence(roomloc.v_empty_avatar,timeout=5,model="顶部送礼物入口")
        if masterAvatarView:
            self.click_element(roomloc.masterAvatarView,model="点击顶部送礼物入口")#点击礼物入口
            self.gold_reward() #选中金币礼物，赠送金币礼物
            self.backpack_gift_reward() #背包礼物打赏
            self.look_homeowner_data() #查看房主资料
            return True
        else:
            return False

    #推荐tap-礼物底部入口
    def gift_entrance_bottom(self):
        self.wait_element_presence(roomloc.open_black_recharge, model="底部送礼物入口")
        self.click_element(roomloc.open_black_recharge, model="点击底部送礼物入口")#点击礼物入口
        time.sleep(2)
        self.driver.press_keycode(4)
        # self.get_gift_tap() #切换礼物tap，选中礼物，赠送礼物,返回
        # self.click_heat_value() # 房间用户及贵宾席

    #背包礼物打赏
    def backpack_gift_reward(self):
        self.find_tap(roomloc.knapsack_button, roomloc.gift_button,"背包tap","礼物tap")
        backpack_gift = self.assert_len(roomloc.backpack_gift,model="背包礼物列表")
        if backpack_gift:
            time.sleep(5)
            i = len(backpack_gift)-1
            backpack_gift[i].click()
            self.wait_click_element(roomloc.btn_send_gift,model="赠送") #点击赠送
        else:
            log.info("背包列表暂无礼物")
            self.save_webImgs(model="背包列表暂无礼物")
        # self.driver.press_keycode(4)

    #金币打赏
    def gold_reward(self):
        self.find_tap(roomloc.goldCoins_button,roomloc.gift_button,"金币tap","礼物tap")
        # self.wait_click_element(roomloc.closeRoomText,model="关闭绘制图案")
        #先判断金币是否大于等于2
        self.wait_element_presence(roomloc.goldCoins_balance,timeout=4,model="等待金币余额")
        text = self.get_element_attribute(roomloc.goldCoins_balance,"text",model="获取金币余额元素")
        text = text.replace("W","")
        log.info("金币余额是：{}".format(text))
        number = int(text)
        if number >= 2:
            self.wait_element_presence(roomloc.goldCoins_list,model="金币礼物列表加载")
            goldCoinsList = self.get_elements(roomloc.goldCoins_list,model="获取金币礼物列表元素")
            goldCoinsList[0].click()
            self.click_element(roomloc.btn_send_gift,model="点击赠送按钮")
            # self.driver.press_keycode(4)
        else:
            log.info("金币不足，无法金币打赏")
            self.save_webImgs(model="金币不足")
            self.driver.press_keycode(4)
            

    #切换礼物tap
    def get_gift_tap(self):
        for i,tapBtn in enumerate(roomloc.gift_list):
            self.click_gift_tap(tapBtn) # 点击礼物tap
            self.select_gift() # 选中某个礼物
            # self.give_gifts() # 赠送礼物
            if i >= 2:
                break
        self.driver.press_keycode(4)
        time.sleep(1)

    #点击礼物tap
    def click_gift_tap(self,tapBtn):
        self.wait_element_clickable(tapBtn, model="等待元素显示")
        self.click_element(tapBtn,model="点击礼物tap") #点击礼物tap
        self.wait_element_presence(roomloc.gift_pages,model="等待礼物列表显示")


    #选中某个礼物
    def select_gift(self):
        giftPages = self.get_elements(roomloc.gift_pages,model="当前tap下的礼物列表") #某tap下当前页的所有礼物元素
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
        self.assert_true(roomloc.personIdView,model='断言个人id') #用户资料断言（id）
        self.follow_ta() #关注
        self.chat() #聊天
        self.reward() #打赏，进入礼物页，点击资料再进入资料页
        self.ait_ta() #@ ta，然后返回，返回到了列表页
        

    #@ta
    def ait_ta(self):
        self.send_message(roomloc.reference,random.choice(chatMessage)) #@ta-发消息-断言
        

    #资料内点击关注
    def follow_ta(self):
        if self.is_clickable(roomloc.attentionBtn,model="关注"):
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
        self.assert_user_list(model="用户在线列表")
        time.sleep(2)
        self.wait_element_clickable(roomloc.vip_seat)
        self.click_element(roomloc.vip_seat,model="点击贵宾席位") #贵宾席位列表
        self.assert_user_list(model="贵宾席位列表暂无数据")
        self.driver.press_keycode(4)
        time.sleep(2)
    
    def assert_user_list(self,model=None):
        self.wait_element_presence(roomloc.user_list,model=model)
        self.assert_len(roomloc.user_list,model=model)

    #点击排行榜
    def click_rankingList(self,ranking_list):
        result = self.is_element_exist(ranking_list,model="暂无排行榜")
        if result:
            log.info("点击排行榜======{}".format(result))
            self.wait_click_element(roomloc.ranking_list,model="点击排行榜")
            self.rankingList_assert(roomloc.day_week_month_assert,model="贡献榜-日榜") #断言
            self.wait_click_element(roomloc.tv_title_week, model="贡献榜-周榜")
            self.rankingList_assert(roomloc.day_week_month_assert,model="贡献榜-周榜") #断言
            self.wait_click_element(roomloc.tv_title_yue, model="贡献榜-月榜")
            self.rankingList_assert(roomloc.day_week_month_assert,model="贡献榜-月榜") #断言
            self.wait_click_element(roomloc.popularity_list, model="人气榜-日榜")
            self.rankingList_assert(roomloc.day_week_month_assert,model="人气榜-日榜") #断言
            self.wait_click_element(roomloc.tv_title_week, model="人气榜-周榜")
            self.rankingList_assert(roomloc.day_week_month_assert,model="人气榜-周榜") #断言
            self.wait_click_element(roomloc.tv_title_yue, model="人气榜-月榜")
            self.rankingList_assert(roomloc.day_week_month_assert,model="人气榜-月榜") #断言
            self.wait_click_element(roomloc.guardian_list, model="守护榜")
            self.rankingList_assert(roomloc.day_week_month_assert2,model="守护榜") #断言
            self.go_back() #返回
        else:
            log.info("暂无排行榜")
            self.save_webImgs(model="暂无排行榜")


    #排行榜断言    
    def rankingList_assert(self,element,model):
        ranking_ele = self.is_element_exist(element,model=model)
        # log.info("result====={}".format(ranking_ele))
        if ranking_ele:
            self.assert_len(element,model=model)
        elif self.is_element_exist(roomloc.no_data,model="暂无数据元素"):
            log.info("==========暂无{}========".format(model))
            self.save_webImgs(model=model)
        else:
            log.info("=========={}异常========".format(model))
            self.save_webImgs(model=model)
    #点击玩法介绍
    def click_introduce(self):
        if self.is_element_exist(roomloc.tv_introduce,model="玩法介绍"):
            self.click_element(roomloc.tv_introduce,model="点击玩法介绍")#点击玩法介绍  
            self.wait_element_presence(roomloc.tv_introduce_assert,model="玩法介绍内容")
            tv_introduce_assert = self.get_element(roomloc.tv_introduce_assert,model="获取玩法介绍文本对象").text
            self.assert_text_len(tv_introduce_assert, model="玩法介绍断言")
            self.click_element(roomloc.closeIv,model="关闭玩法介绍")#关闭玩法介绍
        else:
            log.info("无玩法介绍")
            self.save_webImgs(model="无玩法介绍")
    

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
            self.save_webImgs(model="玩法介绍")

    # #点击麦下
    def click_wheat_lower(self):
        self.click_element(roomloc.layout_people,model="点击麦下") #点击麦下
        time.sleep(1)
        self.click_element(roomloc.layout_people,model="点击麦下") #点击麦下
        time.sleep(1)
    

    # 点击麦下用户列表
    def click_wheatList(self):
        if self.is_clickable(roomloc.iv_head_view,model="麦下列表"):
            self.click_element(roomloc.iv_head_view,model="点击麦下收缩列表") #点击麦下收缩列表
            time.sleep(3)
            self.driver.press_keycode(4)
        else:
            pass

    #进入游戏并断言
    def enter_the_game(self,click_loc,assert_str,click_num=0,model=None):
        self.wait_click_element(roomloc.iv_game,model="游戏入口图标") #点击游戏
        self.wait_element_presence(roomloc.game_assert,model="等待游戏列表")
        self.wait_click_element(click_loc,model=model) #点击要进入的游戏元素
        time.sleep(8)
        while click_num > 0:
            self.tap_by_coordinate([0.5,0.6],model="点击蒙层")
            time.sleep(1)
            click_num = click_num - 1
        # self.is_element_exist(assert_loc,model="断言进入游戏")
        time.sleep(8)
        # self.assert_true(assert_loc,model="{}游戏断言".format(model))
        self.getContent_and_assert(assert_str,model="断言{}".format(model))
        self.driver.press_keycode(4)
    # 点击游戏
    def click_game(self):
        if self.is_element_exist(roomloc.iv_game,timeout=5,model="游戏入口图标"):
            self.click_element(roomloc.iv_game,model="点击游戏入口图标") #点击游戏
            self.wait_element_presence(roomloc.game_assert,model="等待游戏列表")
            time.sleep(5)
            self.assert_len(roomloc.game_assert,dyj=4, model="断言游戏列表")
            time.sleep(2)
            self.driver.press_keycode(4)
            # self.enter_the_game(roomloc.jbtq,roomloc.taoquan_btn,model="金币套圈") #进入金币套圈游戏并断言
            # time.sleep(2)
            self.enter_the_game(roomloc.trap,"套圈圈",model="套圈圈") #进入套圈圈游戏并断言
            # time.sleep(2)
            # self.enter_the_game(roomloc.Koi_blind_box,roomloc.purchase_btn,model="锦鲤盲盒") #进入锦鲤盲盒游戏并断言
            time.sleep(2)
            self.enter_the_game(roomloc.jungle_hunt,"尼龙绳",click_num=1,model="丛林狩猎") #进入丛林狩猎游戏并断言

        else:
            log.info("无游戏入口")
            self.save_webImgs(model="无游戏入口")
        

    # 开黑tay-聊天室-创建队伍
    def click_create_ranks(self):
        if self.is_element_exist(roomloc.tv_disband,timeout=1,model="解散"):
            self.click_dissolution()
        if self.is_element_exist(roomloc.tv_create,timeout=1,model="创建队伍按钮"):
            self.click_element(roomloc.tv_create,model="点击创建队伍") #点击创建队伍
            self.wait_element_clickable(roomloc.spinner_mode, model="检查模式下拉选择框")
            # self.click_element(roomloc.spinner_mode,model="点击下拉选择框") #点击模式下拉选择框
            self.input_text(roomloc.et_desc, "能歌善舞。", model="输入要求")
            xsList = self.get_elements(roomloc.rv_reward,model="获取悬赏列表元素") # 获取悬赏list元素
            xsList[0].click() # 点击某悬赏
            self.click_element(roomloc.btn_create, model="点击创建团队确定按钮")  #点击创建团队确定按钮
            mark = self.assert_true(roomloc.create_assert,model='断言创建队伍') #断言创建团队是否成功
            self.exist_be_click(roomloc.mantle, model="蒙层元素，有则点击，无则pass")
            return mark
        else:
            log.info("该房间无创建队伍按钮")
            self.save_webImgs(model = "无创建队伍按钮")
            return False
        

    # 解散队伍
    def click_dissolution(self):
        self.wait_element_presence(roomloc.tv_disband, model="解散按钮")
        self.click_element(roomloc.tv_disband, model="点击解散按钮")
        res = self.get_toast_exist("解散成功",model="获取toast值")
        self.assert_in("解散成功", res,model="解散队伍")
        
    def createRanks_and_dissolution(self):
        if self.click_create_ranks():
            time.sleep(3)
            self.click_dissolution()
        else:
            pass
    
    
    #关闭女神开播引导弹窗
    def close_back(self):
        if self.is_element_exist(roomloc.close_back,model="聊天室关闭按钮"):
            self.click_element(roomloc.close_back,model="关闭女神开播引导弹窗") 
        else:
            pass
    
    #聊天室底部更多中的游戏、红包、任务等相关操作流程
    def bottom_more(self):
        self.more_geme() #游戏惩罚规则
        self.more_red_envelope() #红包
        self.click_task() #任务
    #游戏规则
    def more_geme(self):
        self.wait_click_element(roomloc.iv_more,model="更多")
        if self.is_element_exist(roomloc.gd_game,model="游戏"):
            self.click_element(roomloc.gd_game,model="点击游戏")
            time.sleep(3)
            self.assert_true(roomloc.game_ymbb,model="断言一毛不拔")
            time.sleep(2)
            self.assert_true(roomloc.game_ybzj,model="断言一本正经")
            time.sleep(2)
            # self.wait_click_element(roomloc.gig_adventure,model="大冒险tap")
            # self.assert_true(roomloc.wash_and_sing,model="断言边刷牙边唱歌")
            # time.sleep(2)
            # self.assert_true(roomloc.water_reading,model="断言含一口水读绕口令")
            # time.sleep(1)
            self.go_back()
        else:
            log.info("暂无【游戏】》真心话大冒险")
            self.save_webImgs(model="无【游戏】》真心话大冒险")
            time.sleep(1)
            self.driver.press_keycode(4)


    #红包
    def more_red_envelope(self):
        self.wait_click_element(roomloc.iv_more,model="更多")
        self.wait_click_element(roomloc.red_envelope,model="红包")
        time.sleep(2)
        self.assert_true(roomloc.total_amount,model="断言总金额")
        time.sleep(2)
        self.assert_true(roomloc.count_down,model="断言倒计时")
        time.sleep(2)
        self.wait_click_element(roomloc.diamond_red_envelope,model="钻石红包")
        time.sleep(2)
        self.assert_true(roomloc.total_amount,model="断言总金额")
        time.sleep(2)
        self.assert_true(roomloc.btn_send,model="断言发送按钮")
        time.sleep(2)
        self.driver.press_keycode(4)


    #任务
    def click_task(self):
        self.wait_click_element(roomloc.iv_more,model="更多")
        self.wait_click_element(roomloc.task,model="任务")
        time.sleep(2) 
        self.assert_true(roomloc.daily_login,model="日常任务")
        time.sleep(2) 
        self.assert_true(roomloc.gold_coin_lucky_draw,model="金币抽奖")
        time.sleep(2) 
        if self.is_element_exist(roomloc.receive_button,model="领取按钮是否存在"):
            claim_list = self.get_elements(roomloc.receive_button,model="存在，获取可领取数量")
            log.info("点击领取按钮")
            claim_list[0].click()
            lj_text = "领取成功"
            lqjl = self.get_toast_msg(lj_text,model="获取奖励领取toast")
            if lj_text in lqjl:
                log.info("领取任务奖励成功===={}".format(lqjl))
            else:
                log.info("领取任务奖励失败===={}".format(lqjl))
                self.save_webImgs(model="领取任务奖励失败")
        else:
            log.info("暂无可领取奖励")
            self.save_webImgs(model="暂无可领取奖励按钮")
        self.wait_click_element(roomloc.task_description,model="点击任务说明")
        time.sleep(2)
        rwsm = self.driver.page_source
        textsrt = "完成每日任务可获得活跃度"
        if textsrt in rwsm:
            log.info("任务说明断言成功")
        else:
            log.info("任务说明断言失败")
            self.save_webImgs(model="任务说明错误")
        if self.is_element_exist(roomloc.closeRoomText,model="关闭按钮"):
            self.wait_click_element(roomloc.closeRoomText,model="点击关闭按钮")
        if self.is_element_exist(roomloc.collectable,model="可领取奖励"):
            klqjlsl = self.get_elements(roomloc.collectable,model="可领取奖励数量")
            klqjlsl[0].click()
            lqjl_text = "已领取"
            ljtoast = self.get_toast_msg(lj_text,model="获取领奖toast")
            if lqjl_text in ljtoast:
                log.info("领奖成功======{}".format(ljtoast))
            else:
                log.info("领奖失败==={}".format(ljtoast))
                self.save_webImgs("领奖失败")
        time.sleep(2)        
        self.driver.press_keycode(4)
        time.sleep(2) 


    