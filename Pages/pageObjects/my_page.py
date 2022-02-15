import time,random

from appium.webdriver.extensions.search_context import mobile
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
    
    

    '''我的守护'''
    def my_guard(self):
        self.wait_click_element(myloc.protector_head, model="点击我的守护")
        if self.is_element_exist(roomloc.guardian_nickname,model="守护者昵称"):
            log.info("用户有守护者")
        else:
            log.info("该用户暂无守护者")
            self.save_webImgs(model="暂无守护者")
        self.RoomPage.go_back() #返回

    # 开播（开厅）入口（我的模块）
    def broadcasting_entrance(self):
        self.wait_click_element(myloc.iv_open_room,model="点击开厅入口")
        # self.assert_true(roomloc.entry_room,"开厅页面")
        self.RoomPage.go_back() #返回

    

    """
    查看我的资料流程
    """
    def view_my_profile(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.broadcasting_entrance() #开播入口及断言
        self.wait_click_element(myloc.sdVipCover, model="点击我的头像")
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
        if self.is_element_exist(myloc.sign_in,timeout=8,model="立即签到"):
            self.click_element(myloc.sign_in,model="立即签到")
        time.sleep(3)
        if self.is_element_exist(myloc.sign_in,timeout=8,model="放入背包"):
            self.click_element(myloc.sign_in,model="放入背包")
        time.sleep(2)
        if self.is_element_exist(myloc.receive_an_award,model="领奖按钮"):
            self.receive_rewards(myloc.receive_an_award,"领奖","领取奖励")
        else:
            log.info("暂无可领奖")
            self.save_webImgs("暂无可领奖")
        if self.is_element_exist(myloc.receive,model="领取"):
            self.wait_click_element(myloc.receive, model='领取按钮')
            self.wait_click_element(myloc.receive_ok,model="点击确定")
            return True
        else:
            self.swipeUp()
            if self.is_element_exist(myloc.receive,model="领取"):
                self.wait_click_element(myloc.receive, model='领取按钮')
                self.wait_click_element(myloc.receive_ok,model="点击确定")
                return True
            else:
                log.info("暂无可领取")
                self.save_webImgs(model="暂无可领取")
                return True

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
        self.wait_click_element(myloc.apply_family, model="申请家族")
        time.sleep(8)
        if self.public_list(myloc.application_family,model="申请家族列表",dyj=2):
            return True
        else:
            return False



    '''设置》账号安全'''
    def account_security(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        if self.is_element_exist(myloc.setUpBtn,model="设置") == False:
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
        time.sleep(8)
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
        elif self.is_element_exist(myloc.blacklist_data,model="黑名单页面元素"):
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
        if self.is_element_exist(myloc.confirm_password_input,timeout=1,model="确认密码输入框"):
            self.wait_click_element(myloc.confirm_password_input, model="确认密码输入框")
            for i in range(1,5):
                self.driver.press_keycode(int(i)+7)
        self.wait_click_element(myloc.confirm_button, model="确定按钮")

    '''未成年保护模式'''
    def protection_of_minors(self):
        self.wait_click_element(myloc.meBtn, model="我的")
        if self.is_element_exist(myloc.setUpBtn,model="设置按钮") == False:
           self.swipeUp()
        self.wait_click_element(myloc.setUpBtn, model="设置")
        text = ""
        state = self.is_element_exist(myloc.on_state,model="开启状态")
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
        if self.is_element_exist(myloc.setUpBtn,model="设置按钮") == False:
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
    def shopping_mall(self):
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


    '''
    我的》收入流程
    '''
    def income(self):
        self.wait_click_element(myloc.meBtn, model="我的") 
        self.wait_click_element(myloc.my_income, model="收入") 
        time.sleep(5)
        self.baby_currency_exchange(myloc.exchange_diamonds,model="宝宝币") #宝宝币兑换
        self.withdrawal() #提现相关
        self.wait_click_element(myloc.yxbtap, model="点击游戏币tap")
        self.baby_currency_exchange(myloc.charm_value_exchange,model="游戏币") #游戏币兑换
        self.wait_click_element(myloc.mlztap, model="点击魅力值tap")
        self.baby_currency_exchange(myloc.charm_value_exchange,model="魅力值") #魅力值兑换
        return True 
        
        
    #宝宝币、游戏币、魅力值兑换
    def baby_currency_exchange(self,loc,model=None):
        num = self.wait_getTextValue(myloc.bbbNumber,"{}数量".format(model))
        log.info("数量是==============================={}".format(num))
        
            
        if int(num) > 1:
            time.sleep(5)
            self.wait_click_element(loc, model="兑换按钮")
            time.sleep(3)
            if model=="魅力值":
                self.input_text(myloc.et_input, 2, model="输入{}兑换数量".format(model))
                time.sleep(1)
            else:
                self.input_text(myloc.et_input, 1, model="输入{}兑换数量".format(model))
                time.sleep(1)
            self.assert_true(myloc.all_exchange,model="全部兑换")
            self.wait_click_element(myloc.tv_shift_to, model="确认兑换")
            if model=="宝宝币":
                self.wait_click_element(myloc.tv_confirm, model="再次确定按钮")
            else:
                self.wait_click_element(myloc.tv_sure, model="点击确定按钮")
            if model=="魅力值":
                text = "兑换成功"
            else:
                text = "成功兑换"
            bbbstr = self.get_toast_msg(text,model="{}兑换toast".format(model))
            if bbbstr and text in bbbstr:
                log.info("{}兑换成功===={}".format(model,bbbstr))
            else:
                log.info("{}兑换异常===={}".format(model,bbbstr))
        else:
            log.info("{}数量为空".format(model))
            self.save_webImgs("{}钱包空荡荡".format(model))
        time.sleep(2)
        self.wait_click_element(myloc.exchange_instructions, model="兑换说明") 
        time.sleep(8)
        sourceText = self.driver.page_source
        text1 = "什么是{}".format(model)
        self.assert_in(text1, sourceText, model="兑换说明断言")
        time.sleep(1)
        self.driver.press_keycode(4)
        time.sleep(2)
        
        
    
    #提现
    def withdrawal(self):
        self.wait_click_element(myloc.btn_withdraw, model="提现") 
        time.sleep(8)
        self.wait_click_element(myloc.withdrawal, model="提现") 
        time.sleep(5)
        self.assert_true(myloc.card_no,model="身份证号码")
        time.sleep(1)
        self.assert_true(myloc.deposit_bank,model="开户银行")
        time.sleep(1)
        self.assert_true(myloc.nex_setp,model="下一步")
        time.sleep(1)
        self.wait_click_element(myloc.service_agreement, model="服务协议") 
        self.wait_click_element(myloc.jsxy, model="费用结算协议") 
        time.sleep(4)
        resText = self.driver.page_source
        text = "哈尔滨米娱信息"
        self.assert_in(text, resText, model="费用结算协议断言")
        self.RoomPage.go_back()
        time.sleep(2)
        self.assert_true(myloc.zyxy,model="自由协议")
        self.wait_click_element(myloc.zyxy, model="自由协议")
        time.sleep(4)
        zyzyText = self.driver.page_source
        restext = "为维护您的自身权益"
        self.assert_in(restext, zyzyText, model="自由协议断言")
        self.RoomPage.go_back()
        time.sleep(2)
        self.assert_true(myloc.zyxy,model="自由协议")
        self.RoomPage.go_back()
        time.sleep(2)
        self.assert_true(myloc.card_no,model="提现信息完善页面-身份证号断言")
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)
        self.wait_click_element(myloc.Withdrawal_record, model="提现记录")
        time.sleep(3)
        if self.is_element_exist(myloc.record_list,model="提现记录列表"):
            txList = self.get_elements(myloc.record_list,model="提现记录列表元素")
            sznum = random.randint(0,len(txList)-1)
            time.sleep(3)
            txList[sznum].click()
            time.sleep(3)
            result = self.get_text(myloc.tv_withdraw_status,model="获取兑换状态")
            self.assert_in("兑换钻石成功",result,model="兑换断言")
            time.sleep(2)
            self.assert_true(myloc.layout_withdraw_actual,model="断言兑换钻石数量")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(3)
            self.driver.press_keycode(4)

        else:
            log.info("提现记录列表数据为空")
            self.save_webImgs("提现记录列表暂无数据")

    #游戏币相关操作
    def game_currency(self,loc_ele,model=None):
        self.wait_click_element(loc_ele, model="{}tap按钮".format(model))
        time.sleep(5)
        yxbres = self.assert_true(myloc.bbbNumber,model="{}余额".format(model))
        return yxbres
        


    '''
    会员页面操作流程
    '''
    def member(self):
        self.wait_click_element(myloc.meBtn, model="我的") 
        self.wait_click_element(myloc.iv_vip, model="会员") 
        time.sleep(4)
        self.assert_true(myloc.hybs,model="断言会员专属")
        time.sleep(1)
        self.assert_true(myloc.zszb,model="断言专属装扮")
        time.sleep(1)
        return self.renew_now()#立即续费方法



    #立即续费方法
    def renew_now(self):
        self.wait_click_element(myloc.ndzsbs, model="立即续费") 
        self.assert_equal(myloc.gear,dyj=4,model="断言充值档位")
        time.sleep(1)
        self.wait_click_element(myloc.morePayWayLay, model="更多支付") 
        time.sleep(1)
        self.assert_true(myloc.payWayLay,model="支付宝选项断言")
        time.sleep(2)
        self.wait_click_element(myloc.give, model="赠送") 
        time.sleep(1)
        self.wait_click_element(myloc.gift_friends, model="赠送好友") 
        time.sleep(3)
        friends = self.get_elements(myloc.select_friends,model="获取好友列表")
        number = random.randint(0,len(friends)-1)
        friends[number].click()
        self.wait_click_element(myloc.confirmOK, model="确定")
        time.sleep(1)
        senduid = self.get_text(myloc.sendIdTv,model="用户id号码")
        if senduid and len(senduid) > 3:
            log.info("选择的用户哩咔ID是:{}".format(senduid))
            self.wait_click_element(myloc.payment, model="支付")
            self.wait_click_element(myloc.tv_cancel, model="再考虑下")
            time.sleep(2)
        else:
            log.info("选择赠送好友失败==={}".format(senduid))
            self.save_webImgs("赠送好友失败")
            self.driver.press_keycode(4)
        self.wait_click_element(myloc.membership_agreement, model="哩咔会员协议")
        time.sleep(4)
        lkhyxy = self.driver.page_source
        part_text = "会员资格以月为单位计算"
        if part_text in lkhyxy:
            log.info("哩咔会员断言成功===包含:{}".format(part_text))
        else:
            log.info("哩咔会员断言失败===未包含:{}".format(part_text))
            self.save_webImgs("哩咔会员协议")
        self.RoomPage.go_back()
        self.assert_true(myloc.weixin,model="断言微信支付选项")
        self.RoomPage.go_back()
        self.assert_true(myloc.hybs,model="断言会员专属")
        time.sleep(1)
        if self.is_element_exist(myloc.xnf, model="续年费元素是否存在"):
            self.wait_click_element(myloc.xnf, model="续年费,更优惠")
        elif self.is_element_exist(myloc.knf, model="开年费元素是否存在"):
            self.wait_click_element(myloc.knf, model="开年费,更优惠")
        self.assert_equal(myloc.gear,dyj=4,model="充值档位断言2")
        self.RoomPage.go_back()
        time.sleep(3)
        return self.assert_true(myloc.zszb,model="断言专属装扮")
        


    '''我的-充值流程'''
    def recharge(self):
        self.wait_click_element(myloc.meBtn, model="我的") 
        self.wait_click_element(myloc.iv_recharge, model="充值") 
        time.sleep(4)
        if self.is_element_exist(myloc.scth_title,model="首充特惠"):
            self.RoomPage.go_back()
        #默认钻石tap
        time.sleep(4)
        self.balance_quantity(myloc.diamond_quantity,model="钻石数量")
        time.sleep(2)
        self.assert_true(myloc.layout_pay_wechat,model="微信支付选项")
        time.sleep(2)
        self.assert_true(myloc.layout_pay_alipay,model="支付宝选项")
        time.sleep(2)
        self.assert_equal(myloc.recharge_gear,dyj=6,model="断言充值档位列表")
        #开具发票
        # self.wait_click_element(myloc.invoice, model="开具发票")
        # time.sleep(3)
        # self.assert_true(myloc.duty_paragraph,model="断言公司税号")
        # #开票记录
        # self.wait_click_element(myloc.invoicing_record, model="开票记录")
        #点击开票说明
        # self.wait_click_element(myloc.billing_description, model="开票说明")
        # time.sleep(5)
        # kpsmText = self.driver.page_source
        # kpsm_ext = "将电子发票推送至您的邮箱"
        # self.assert_in(kpsm_ext, kpsmText, model="断言开票说明")
        #开票说明-在线客服
        self.wait_click_element(myloc.online_service2,model="在线客服")
        if self.is_element_exist(myloc.kefu_nick,model="客服昵称"):
            kf_list = self.get_elements(myloc.kefu_nick,model="客服列表")
            kf_num = random.randint(0,len(kf_list)-1)
            kf_list[kf_num].click()
            time.sleep(5)
            if self.is_element_exist(myloc.tv_desc,model="聊天页-心动"):
                self.driver.press_keycode(4)
                time.sleep(1)
            if self.is_element_exist(myloc.interactive_games,model="点此处邀她玩"):
                self.driver.press_keycode(4)
                time.sleep(1)
            self.assert_true(myloc.editTextMessage,model="断言聊天输入框")
            self.RoomPage.go_back() #返回客服列表
            time.sleep(2)
            self.RoomPage.go_back() #返回开具说明
            time.sleep(2)
            self.driver.press_keycode(4) #返回开具发票
            time.sleep(4)
            self.driver.press_keycode(4) #返回钻石tap页
        else:
            log.info("暂无客服")
            self.save_webImgs("暂无客服")

        self.wait_click_element(myloc.Withdrawal_record, model="查看明细")
        self.details_view(myloc.tv_money,model="充值记录") #查看明细-充值记录列表相关操作
        self.screen(7)
        self.wait_click_element(myloc.tv_title_two, model="消费tap") 
        self.details_view(myloc.tv_money,model="消费记录") #查看明细-消费记录列表相关操作
        self.screen(5)
        self.RoomPage.go_back()
        #宝石tap操作
        self.wait_click_element(myloc.gemstone, model="点击宝石tap") 
        self.balance_quantity(myloc.diamond_quantity,model="宝石数量")
        self.assert_equal(myloc.recharge_gear,dyj=9,model="断言充值档位列表")
        #宝石-在线客服
        self.contact_customer_service(myloc.online_service,model="在线客服")
        #宝石-查看明细
        self.wait_click_element(myloc.Withdrawal_record, model="查看明细")
        #默认收入tap
        self.details_view(myloc.tv_money,model="收入记录") #宝石tap-查看明细-收入记录列表相关操作
        self.screen(6)
        self.wait_click_element(myloc.tv_title_two, model="消费tap") 
        self.details_view(myloc.tv_money,model="消费记录") #宝石tap-查看明细-消费记录列表相关操作
        self.screen(5)
        self.RoomPage.go_back()
        #金币tap操作
        self.wait_click_element(myloc.gold_coins, model="点击金币tap")
        self.balance_quantity(myloc.itv_gold,model="金币数量")
        if self.assert_len(myloc.tv_count,dyj=0,model="金币收入支出记录列表"):
            self.wait_click_element(myloc.tv_see_all,model="查看全部")
            self.details_view(myloc.tv_count,model="获取金币记录")
            self.wait_click_element(myloc.use_gold_coins, model="使用金币tap")
            self.details_view(myloc.tv_count,model="使用金币记录")
            self.RoomPage.go_back()
        else:
            log.info("金币收入支出暂无记录")
            self.save_webImgs("金币收入支出暂无记录")
        self.wait_click_element(myloc.Withdrawal_record, model="兑换记录")
        self.details_view(myloc.tv_count,model="获取金币记录")
        self.wait_click_element(myloc.use_gold_coins, model="使用金币tap")
        self.details_view(myloc.tv_count,model="使用金币记录")
        self.RoomPage.go_back()
        #赚取金币按钮
        self.click_element(myloc.btn_get_gold,model="赚取金币按钮")
        text = "每日签到"
        if self.is_element_exist(myloc.sign_in,model="签到"):
            self.click_element(myloc.sign_in,model="点击立即签到按钮")
            self.click_element(myloc.sign_in,model="点击放入背包按钮")
        text_res = self.get_text(myloc.mrqd_title,model="每日签到")
        return self.assert_in(text,text_res,model="断言每日签到是否存在")
        


    #钻石tap-查看明细相关操作
    def details_view(self,loc,model=None):
        if self.is_element_exist(loc,model=model):
            tvtimes = self.find_elements(loc)
            self.assert_len(tvtimes,model="断言{}列表".format(model))
        else:
            log.info("暂无{}".format(model))
            self.save_webImgs("暂无{}".format(model))
        
    #余额数量
    def balance_quantity(self,loc,model=None):
        if self.assert_true(loc,model="等待{}元素".format(model)) == False:
            return False
        diamondNum = self.get_text(loc,model="获取{}".format(model))
        if int(diamondNum) > 0:
            pass
        else:
            log.info("没有{}，穷的叮当响".format(model))
            self.save_webImgs("暂无{}".format(model))    


    #进入聊天页通用方法
    def contact_customer_service(self,loc,model=None):
        self.wait_click_element(loc, model="点击{}".format(model))
        # self.assert_equal(myloc.tvxzs_title,dyj=11,model="小助手问题列表")
        self.assert_true(myloc.editTextMessage,model="断言聊天输入框")
        self.RoomPage.go_back()
        


    def screen(self,num):
        self.wait_click_element(myloc.iv_extra, model="筛选按钮") 
        self.assert_equal(myloc.tv_content,dyj=num,model="筛选选项断言")
        self.wait_click_element(myloc.tv_cancel, model="取消按钮") 



    '''我的等级测试流程'''
    def my_level(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        time.sleep(2)
        if self.is_element_exist(myloc.my_level, model="我的等级"):
            self.wait_click_element(myloc.my_level, model="点击我的等级") 
            time.sleep(5)
            self.assert_true(myloc.free_barrage,model="断言免费弹幕")
            time.sleep(3)
            self.assert_true(myloc.free_barrage,model="断言榜单隐身")
            self.wait_click_element(myloc.anchor_level, model="点击主播等级tap") 
            time.sleep(2)
            self.assert_true(myloc.begin_to_show,model="开播")
            time.sleep(2)
            self.assert_true(myloc.wish,model="心愿")
            time.sleep(2)
            self.assert_true(myloc.zhujianPK,model="PK")
            self.wait_click_element(myloc.rank, model="点击爵位等级tap") 
            time.sleep(2)
            self.assert_true(myloc.count,model="伯爵")
            time.sleep(2)
            self.wait_click_element(myloc.explain,model="点击说明tap")
            time.sleep(3)
            sm_Text = self.driver.page_source
            vip_ext = "VIP等级是根据用户在应用内的消费金额计算"
            self.assert_in(vip_ext, sm_Text, model="断言vip等级说明")
            time.sleep(2)
            self.wait_click_element(myloc.anchor_level, model="点击主播等级tap")
            time.sleep(3)
            zhubo_Text = self.driver.page_source
            zb_ext = "主播等级是根据主播经验计算的"
            self.assert_in(zb_ext, zhubo_Text, model="断言等级说明")
            time.sleep(2)
            self.wait_click_element(myloc.rank, model="点击爵位等级tap")
            time.sleep(3)
            juewei_Text = self.driver.page_source
            jw_ext = "购买爵位自动返还一定金额的钻石"
            self.assert_in(jw_ext, juewei_Text, model="断言vip等级说明")
            time.sleep(1)
            return True
            
        else:
            log.info("暂未显示我的等级")
            self.save_webImgs("暂未显示我的等级")
            return True
