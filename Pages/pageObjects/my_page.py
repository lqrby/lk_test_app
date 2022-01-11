import time,random
from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageLocators.my_locators import MyLocators as myloc
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from Pages.pageObjects.room_page import RoomPage
from Pages.pageObjects.square_page import SquarePage
from TestDatas.my import commentData,dynamicData
from Common.log import get_logger
log = get_logger(logger_name="首页操作日志")

class MyPage(CommonBus):

    def __init__(self,driver):
        self.driver = driver
        self.RoomPage = RoomPage(self.driver)
        self.SquarePage = SquarePage(self.driver)
    
    '''点击我的头像'''
    def click_head_portrait(self):
        self.wait_eleVisible(myloc.sdVipCover, model="等待我的头像")
        self.click_element(myloc.sdVipCover, model="点击我的头像")
        return self

    '''我的守护'''
    def my_guard(self):
        self.wait_eleVisible(myloc.protector_head, model="等待我的守护")
        self.click_element(myloc.protector_head, model="点击我的守护")
        if self.is_element_exist(roomloc.guardian_nickname):
            log.info("用户有守护者")
        else:
            log.info("该用户暂无守护者")
            self.save_webImgs(model="暂无守护者")
        self.RoomPage.go_back() #返回

    # 开播（开厅）入口（我的模块）
    def broadcasting_entrance(self):
        self.wait_element_presence(myloc.iv_open_room,model="等待开厅入口")
        self.click_element(myloc.iv_open_room,model="点击开厅入口")
        # self.assert_true(roomloc.entry_room,"开厅页面")
        self.RoomPage.go_back() #返回

    

    """
    查看我的资料流程
    """
    def view_my_profile(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.broadcasting_entrance() #开播入口及断言
        self.click_head_portrait() #点击我的头像
        self.RoomPage.my_information() #我的资料 
        return True


    '''修改昵称'''
    def updeta_nickname(self,nicknames):
        if self.is_clickable(myloc.v_nick,model="昵称"):
            #修改昵称
            self.wait_click_element(myloc.v_nick,model="昵称") #点击昵称
            nickname = random.choice(nicknames)
            self.wait_input_text(myloc.et_nick,nickname,model="昵称") #输入昵称
            self.click_element(myloc.tv_save,model="点击保存按钮")
            part_text = "保存成功"
            nickname_toast = self.get_toast_msg(part_text,model="保存昵称toast")
            if nickname_toast:
                log.info("toast===={}".format(nickname_toast))
                time.sleep(8)
                if self.is_clickable(myloc.v_nick,model="昵称"):
                    self.click_element(myloc.v_nick,model="点击昵称")
                    self.wait_element_presence(myloc.et_nick,model="等待昵称输入框")
                    nicknameText = self.get_text(myloc.et_nick,model="获取昵称文本")
                    if nicknameText == nickname:
                        log.info("修改昵称断言成功")
                        return True
                    else:
                        log.info("修改昵称断言失败")
                        self.save_webImgs("修改昵称断言失败")
                        return False
                else:
                    log.info("昵称审核中!")
                    self.save_webImgs("昵称审核中")
                    return False
                # self.wait_click_element(myloc.tv_cancel,model="取消按钮")
            else:
                log.info("toast===={}".format(nickname_toast))
                self.save_webImgs("保存昵称失败")
        else:
            self.save_webImgs("昵称审核中")
            return False


    '''修改签名'''
    def updeta_autograph(self,autographs):
        if self.is_clickable(myloc.v_describe,model="签名"):
            #修改签名
            self.wait_click_element(myloc.v_describe,model="我的签名")
            autograph = random.choice(autographs)
            self.wait_input_text(myloc.et_nick, autograph, model="我的签名")
            self.click_element(myloc.tv_save,model="点击保存按钮")
            part_text = "保存成功"
            autograph_toast = self.get_toast_msg(part_text,model="保存签名toast")
            if autograph_toast:
                log.info("toast===={}".format(autograph_toast))
                time.sleep(5)
                if self.is_clickable(myloc.v_describe,model="签名"):
                    self.click_element(myloc.v_describe,model="点击签名")
                    self.wait_element_presence(myloc.et_nick,model="等待签名输入框")
                    autographText = self.get_text(myloc.et_nick,model="获取签名文本")
                    if autographText == autograph:
                        log.info("修改签名断言成功")
                    else:
                        log.info("修改签名断言失败")
                        self.save_webImgs("修改签名断言失败")
                    self.wait_click_element(myloc.tv_cancel,model="取消按钮")
            else:
                log.info("toast===={}".format(autograph_toast))
                self.save_webImgs("保存签名失败")

    

    """
    编辑我的资料流程
    """
    def edit_my_profile(self,myProfileData):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.wait_click_element(myloc.iv_edit,model="编辑资料入口")
        self.updeta_nickname(myProfileData["nickname"]) #修改昵称
        # self.updeta_autograph(myProfileData["autograph"]) #修改签名
            # # self.RoomPage.go_back() #返回
        return True
 

    """
    我的好友流程+派对足迹
    """
    def myFriend_whoLookMe_partyFootprints(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.wait_click_element(myloc.v_user_friends,model="我的好友") 
        self.wait_click_element(myloc.tv_title_one,model="关注") 
        self.public_list(myloc.avatar,"关注",dyj=1)
        self.wait_click_element(myloc.tv_title_two,model="粉丝") 
        self.public_list(myloc.avatar,"粉丝",dyj=1)
        self.wait_click_element(myloc.tv_title_three,model="好友") 
        self.public_list(myloc.avatar,"好友",dyj=1)
        self.RoomPage.go_back()
        self.wait_click_element(myloc.v_look_me,model="谁看过我")
        self.public_list(myloc.iv_head,model="谁看过我列表")
        self.RoomPage.go_back()
        self.wait_click_element(myloc.v_footprint,model="派对足迹")
        self.public_list(myloc.iv_room_head,model="派对足迹")
        return True   



    '''我的动态'''
    def my_dynamic(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.wait_click_element(myloc.my_dynamic,model="我的动态")
        self.wait_click_element(myloc.btn_submit,model="发布动态")
        self.input_text(myloc.et_content,random.choice(dynamicData),model="输入发布动态内容")
        self.wait_click_element(myloc.iv_extra,model="发布")
        expected_text = "发送动态成功"
        Prompttext = self.get_toast_msg(expected_text,model="获取发布动态提示语")
        if expected_text in Prompttext:
            log.info("动态成功")
        else:
            log.exception("获取发布动态toast失败")
            self.save_webImgs("发布动态失败")
        self.swipeDown()
        time.sleep(2)
        dynamicList = self.public_list(myloc.my_dynamic_list,model="我的动态列表")
        if dynamicList:
            dt_num = random.randint(0,len(dynamicList)-1) 
            log.info("点击第{}个动态查看详情".format(dt_num + 1))
            dynamicList[dt_num].click()
            time.sleep(2)
            self.SquarePage.spot_fabulous() #点赞
            self.input_text(myloc.comment_input,text=random.choice(commentData),model="评论输入框")
            time.sleep(1)
            self.wait_click_element(myloc.sendButton,model="点击发送按钮")
            mark = "评论成功"
            msg = self.get_toast_msg(mark,model="获取发送消息后的toast消息")
            if mark in msg:
                log.info("评论动态成功")
                # self.RoomPage.go_back()
            else:
                log.exception("获取发送消息toast失败")
                self.save_webImgs("发送消息失败")
                # self.RoomPage.go_back()
            return self.delete_dynamic() #删除动态
        else:
            log.info("动态列表赞无数据")
            self.save_webImgs("动态列表赞无数据")
            return False
            
    def delete_dynamic(self):
        self.RoomPage.click_more() #点击更多
        self.wait_click_element(myloc.deleteButton,model="删除")
        deletemark = "删除成功"
        deletemsg = self.get_toast_msg(deletemark,model="获取删除动态后的toast消息")
        if deletemark in deletemsg:
            log.info("删除动态成功")
            # self.RoomPage.go_back()
            return True
        else:
            log.exception("获取删除动态toast失败")
            self.save_webImgs("删除动态失败")
            return False



    '''我的背包'''
    def my_knapsack(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        self.wait_click_element(myloc.my_knapsack,model="我的背包")
        self.public_list(myloc.all_gifts_list,model="我的全部礼物列表")
        self.wait_click_element(myloc.decorate_list, model="装饰")
        self.public_list(myloc.all_gifts_list,model="装饰列表")
        self.wait_click_element(myloc.prop_list, model="道具")
        self.public_list(myloc.all_gifts_list,model="道具列表")
        self.wait_click_element(myloc.gifts_list, model="礼物")
        giftsList = self.public_list(myloc.all_gifts_list,model="礼物列表")
        if giftsList:
            return True
        else:
            return False
        # sweetflower = self.public_list(myloc.sweet_flower,model="甜蜜小花列表")
        # if sweetflower:
        #     i = len(sweetflower)-1
        #     sweetflower[i].click() 
        #     self.wait_click_element(myloc.use_now, model="立即使用")
        #     self.wait_click_element(roomloc.masterAvatarView,model="顶部礼物入口")
        #     time.sleep(5)
        #     self.RoomPage.backpack_gift_reward() #背包礼物打赏
        #     self.driver.press_keycode(4)
        #     return self.RoomPage.exit_chat_room() #退出聊天室
        # else:
        #     log.info("礼物列表暂无甜蜜小花礼物")
        #     self.save_webImgs("礼物列表暂无甜蜜小花礼物")
        #     return False


    '''领奖、领取的方法'''
    def receive_rewards(self,loc,message,model):
        receive_an_awardList = self.get_elements(loc)
        number = len(receive_an_awardList) - 1
        self.click_element_byEle(receive_an_awardList[number],model="点击{}按钮".format(model))
        receive_an_award = self.get_toast_exist(message,model="{}toast")
        if receive_an_award and message in receive_an_award:
            log.info("{}奖励成功".format(model))
        else:
            log.info("{}失败".format(model))
            self.save_webImgs("{}失败".format(model))

    '''奖励中心'''
    def reward_center(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        self.wait_click_element(myloc.reward_center, model="点击奖励中心")
        time.sleep(2)
        if self.is_element_exist(myloc.sign_in,timeout=8):
            self.click_element(myloc.sign_in)
        time.sleep(3)
        if self.is_element_exist(myloc.sign_in,timeout=8):
            self.click_element(myloc.sign_in)
        time.sleep(2)
        if self.is_element_exist(myloc.receive_an_award):
            self.receive_rewards(myloc.receive_an_award,"领奖","领取奖励")
        else:
            log.info("暂无可领奖")
            self.save_webImgs("暂无可领奖")
        if self.is_element_exist(myloc.receive):
            self.wait_click_element(myloc.receive, model='领取按钮')
            self.wait_click_element(myloc.receive_ok,model="点击确定")
            return True
        else:
            self.swipeUp()
            if self.is_element_exist(myloc.receive):
                self.wait_click_element(myloc.receive, model='领取按钮')
                self.wait_click_element(myloc.receive_ok,model="点击确定")
                return True
            else:
                log.info("暂无可领取")
                self.save_webImgs(model="暂无可领取")
                return False

    '''活动中心'''    
    def activity_center(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        self.wait_click_element(myloc.activity_center,"活动中心")
        giftarr = self.public_list(myloc.onlineRecycle,model="已上线游戏列表",dyj=0)
        if giftarr:
            return True
        else:
            return False

    '''申请家族'''
    def application_family(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        self.wait_click_element(myloc.apply_family, model="申请家族",timeout=10)
        if self.public_list(myloc.application_family,model="申请家族列表",dyj=2):
            return True
        else:
            return False



    '''设置》账号安全'''
    def account_security(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        if self.is_element_exist(myloc.setUpBtn) == False:
           self.swipeUp()
        self.wait_click_element(myloc.setUpBtn, model="设置")
        self.wait_click_element(myloc.account_and_security, model="账号与安全")
        self.update_phone() # 修改手机号
        self.bind_official_account() # 绑定公众号   
        self.blacklist() # 黑名单
        return True

    # 修改手机号
    def update_phone(self):
        self.wait_click_element(myloc.layout_bind_phone, model="修改绑定手机")
        self.wait_click_element(myloc.changePhoneBtn, model="更换绑定手机号")
        self.assert_true(myloc.get_verification_code,model="更换绑定手机页面断言")
        self.RoomPage.go_back() #返回

    # 绑定公众号
    def bind_official_account(self):
        self.wait_click_element(myloc.bind_official_account, model="绑定公众号")
        time.sleep(3)
        # self.wait_element_presence(myloc.rl_root,"绑定公众号页面title")
        page_source = self.driver.page_source
        text = "关注公众号"
        self.assert_in(text, page_source, model="绑定公众号页面断言")
        self.RoomPage.go_back() #返回
        

    # 黑名单
    def blacklist(self):
        self.wait_click_element(myloc.layout_black_list, model="黑名单")
        if self.is_element_exist(myloc.blacklist_no_data):
            log.info("黑名单暂无数据")
            self.save_webImgs("暂无黑名单人员")
            self.RoomPage.go_back() #返回
        elif self.is_element_exist(myloc.blacklist_data):
            self.public_list(myloc.blacklist_data,model="黑名单列表")
            self.RoomPage.go_back() #返回
        else:
            log.error("黑名单页面异常")
            self.save_webImgs(model="黑名单页面异常")
            self.RoomPage.go_back() #返回

    # 输入密码
    def input_password(self):
        for i in range(1,5):
            self.driver.press_keycode(int(i)+7)
        if self.is_element_exist(myloc.confirm_password_input,timeout=1):
            self.wait_click_element(myloc.confirm_password_input, model="确认密码输入框")
            for i in range(1,5):
                self.driver.press_keycode(int(i)+7)
        self.wait_click_element(myloc.confirm_button, model="确定按钮")

    '''未成年保护模式'''
    def protection_of_minors(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        if self.is_element_exist(myloc.setUpBtn) == False:
           self.swipeUp()
        self.wait_click_element(myloc.setUpBtn, model="设置")
        text = ""
        state = self.is_element_exist(myloc.on_state)
        if state:
            text = self.get_text(myloc.on_state,model="开启状态")
        self.wait_click_element(myloc.protection_of_minors, model="未成年保护")
        if text == "未开启":
            self.wait_click_element(myloc.turn_on_protection, model="开启保护模式")
            self.input_password() # 输入密码
            self.wait_click_element(myloc.turn_off_protection, model="关闭保护模式")
            for i in range(1,5):
                self.driver.press_keycode(int(i)+7)
            self.wait_click_element(myloc.confirm_button, model="确定按钮")
            return True
        elif text == "已开启":
            self.wait_click_element(myloc.turn_off_protection, model="关闭保护模式")
            for i in range(1,5):
                self.driver.press_keycode(int(i)+7)
            self.wait_click_element(myloc.confirm_button, model="确定按钮")
            return True
        else:
            log.info("出问题啦！也不知道什么状态")
            self.save_webImgs("未成年保护不知道什么状态")
            return False

    # '''我的等级流程'''
    # def my_level(self):
    #     self.wait_click_element(myloc.meBtn, model="我的")
    #     self.wait_click_element(myloc.my_level,model="我的等级")
    #     '''H5页面'''



    '''设置-关于哩咔'''
    def about_lika(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        if self.is_element_exist(myloc.setUpBtn) == False:
           self.swipeUp()
        self.wait_click_element(myloc.setUpBtn, model="设置")
        self.wait_click_element(myloc.about_lika,model="关于哩咔")
        # self.check_version() #检查最新版本
        # self.page_assertion(myloc.layout_about,"客服邮箱",model="关于我们") #关于我们
        # self.page_assertion(myloc.layout_privacy,"平台经营者",model="隐私政策") #隐私政策
        self.help_center() 
        return True
        
    #检查更新
    def check_version(self):
        self.wait_click_element(myloc.checkVersion,model="检查更新")
        version = "当前已是最新版本"
        checkVersion = self.get_toast_msg(version,model="检查版本")
        if version in checkVersion:
            pass
        else:
            self.wait_click_element(myloc.update_later,model="稍后更新")
            log.info("点击稍后更新")


    #页面断言公共通用
    def page_assertion(self,pageloc,assertText,model=None):
        self.wait_click_element(pageloc,model=model)
        time.sleep(5)
        # log.info(self.driver.page_source)
        if assertText in self.driver.page_source:
            log.info("{}断言通过".format(model))
            self.RoomPage.go_back()
        else:
            log.info("{}断言错误".format(model))
            self.save_webImgs("{}断言失败".format(model))
            time.sleep(1)
            self.RoomPage.go_back()
    
    #帮助中心
    def help_center(self):
        self.wait_click_element(myloc.layout_helper,model="帮助中心")
        for itemLoc in myloc.problem_classification:
            self.wait_click_element(itemLoc[0],model=itemLoc[1])
            time.sleep(2)
            classification_list = self.get_elements(myloc.classification_list,model=itemLoc[1])
            number = random.randint(0,len(classification_list)-1)
            classification_list[number].click()
            time.sleep(2)
            if "未解决你的问题" in self.driver.page_source:
                # log.info("{}断言通过".format(model))
                self.RoomPage.go_back()
            else:
                log.info("{}断言错误".format(itemLoc[1]))
                self.save_webImgs("{}断言失败".format(itemLoc[1]))
                time.sleep(1)
                self.RoomPage.go_back()
            time.sleep(1)
            self.RoomPage.go_back()
            # contexts = self.driver.contexts
            # log.info("contexts========{}".format(contexts))
            # self.RoomPage.go_back()
        # contexts = self.driver.contexts
        # log.info("contexts========{}".format(contexts))
        # webview_name = ""
        # self.switch_webview()
        '''web页面'''

    
    #我的》商城
    def view_members(self):
        self.wait_click_element(myloc.meBtn, model="我的") 
        self.wait_click_element(myloc.iv_dress_store, model="商城") 
        time.sleep(3)
        self.assert_true(myloc.zuojia,model="座驾")
        time.sleep(1)
        self.assert_true(myloc.qipao,model="气泡")
        time.sleep(1)
        self.wait_click_element(myloc.vipzs, model="VIP专属")
        time.sleep(3)
        self.wait_click_element(myloc.dhjl, model="兑换记录")
        time.sleep(2)
        self.assert_true(myloc.xhjf, model="消耗积分")
        self.tap_by_coordinate([0.5,0.2])
        self.wait_click_element(myloc.shuoming, model="说明")
        time.sleep(2)
        source = self.driver.page_source
        time.sleep(1)
        text = "解释权归本平台所有"
        self.assert_in(text, source, model="说明断言")
        time.sleep(2)
        self.tap_by_coordinate([0.5,0.2])
        return True
        # self.driver.press_keycode(4)
        '''
        暂时生日墙有问题，金刚在处理，处理完即可完善用例
        '''
        # self.wait_click_element(myloc.jrsx, model="今日寿星")






        