import time,random
from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageLocators.my_locators import MyLocators as myloc
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from Pages.pageObjects.room_page import RoomPage
from Common.log import get_logger
log = get_logger(logger_name="首页操作日志")

class MyPage(CommonBus):

    def __init__(self,driver):
        self.driver = driver
        self.RoomPage = RoomPage(self.driver)

    
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

    def audit_status(self,loc,model):
        mark = self.is_clickable(loc)
        if mark == False:
            log.info(model)
            self.save_webImgs(model)
            return False
        else:
            return True

    # 修改昵称
    def updeta_nickname(self,nicknames):
        if self.audit_status(myloc.v_nick,"昵称审核中"):
            #修改昵称
            self.wait_click_element(myloc.v_nick,model="昵称") #点击昵称
            nickname = random.choice(nicknames)
            self.wait_input_text(myloc.et_nick,nickname,model="昵称") #输入昵称
            self.click_element(myloc.tv_save,model="点击保存按钮")
            part_text = "保存成功"
            nickname_toast = self.get_toast_msg(part_text,model="保存昵称toast")
            if nickname_toast:
                log.info("toast===={}".format(nickname_toast))
                time.sleep(5)
                if self.audit_status(myloc.v_nick,"昵称审核中"):
                    self.click_element(myloc.v_nick,model="点击昵称")
                    self.wait_element_presence(myloc.et_nick,model="等待昵称输入框")
                    nicknameText = self.get_text(myloc.et_nick,model="获取昵称文本")
                    if nicknameText == nickname:
                        log.info("修改昵称断言成功")
                    else:
                        log.info("修改昵称断言失败")
                        self.save_webImgs("修改昵称断言失败")
                    self.wait_click_element(myloc.tv_cancel,model="取消按钮")
            else:
                log.info("toast===={}".format(nickname_toast))
                self.save_webImgs("保存昵称失败")

    def updeta_autograph(self,autographs):
        if self.audit_status(myloc.v_describe,"签名审核中"):
            #修改签名
            self.wait_click_element(myloc.v_describe,"我的签名")
            autograph = random.choice(autographs)
            self.wait_input_text(myloc.et_nick, autograph, "我的签名")
            self.click_element(myloc.tv_save,"点击保存按钮")
            part_text = "保存成功"
            autograph_toast = self.get_toast_msg(part_text,model="保存签名toast")
            if autograph_toast:
                log.info("toast===={}".format(autograph_toast))
                time.sleep(5)
                if self.audit_status(myloc.v_describe,"签名审核中"):
                    self.click_element(myloc.v_describe,"点击签名")
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
        self.updeta_autograph(myProfileData["autograph"]) #修改签名
            # # self.RoomPage.go_back() #返回
        return True




    
    
        

    """
    我的好友流程+派对足迹
    """
    def myFriend_whoLookMe_partyFootprints(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.wait_click_element(myloc.v_user_friends,"我的好友") 
        self.wait_click_element(myloc.tv_title_one,"关注") 
        self.public_list(myloc.avatar,"关注",dyj=1)
        self.wait_click_element(myloc.tv_title_two,"粉丝") 
        self.public_list(myloc.avatar,"粉丝",dyj=1)
        self.wait_click_element(myloc.tv_title_three,"好友") 
        self.public_list(myloc.avatar,"好友",dyj=1)
        self.RoomPage.go_back()
        self.public_list(myloc.v_look_me,myloc.iv_head,"谁看过我")
        self.RoomPage.go_back()
        self.public_list(myloc.v_footprint,myloc.iv_room_head,"派对足迹")
        return True   



    

    '''我的动态'''
    def my_dynamic(self):
        self.wait_click_element(myloc.meBtn, model="点击我的")
        self.wait_click_element(myloc.my_dynamic,model="我的动态")
        dynamicList = self.public_list(myloc.my_dynamic_list,model="我的动态列表")
        if dynamicList:
            dt_num = random.randint(0,len(dynamicList)-1) 
            log.info("点击第{}个动态查看详情".format(dt_num + 1))
            dynamicList[dt_num].click()
            if self.is_element_exist(myloc.tv_read_count):
                return True
            else:
                return False


    # '''进入任务中心'''
    # def intoTask(self):
    #     self.click_element(myloc.layoutTaskCenter, "点击任务中心")
    #     title = self.get_text(myloc.toolbar_title, "获取任务中心页title")
    #     return title

    # '''进入我的消息'''
    # def intoMessage(self):
    #     self.swipeUp(t=3000)
    #     self.click_element(myloc.layoutProfileIM, "点击消息")
    #     title = self.get_text(myloc.messagetitle, "获取消息页title")
    #     return title

    # '''进入背包'''
    # def intoBag(self):
    #     self.click_element(myloc.layoutProfileBag, "点击背包")
    #     title = self.get_text(myloc.toolbar_title, "获取背包title")
    #     return title

    # '''进入商城'''
    # def intoFerrari(self):
    #     self.click_element(myloc.layoutProfileFerrari, "点击商城")
    #     title = self.get_text(myloc.toolbar_title, "获取背包title")
    #     return title

    # '''进入我的等级'''
    # def intoGrade(self):
    #     self.click_element(myloc.layoutProfileGrade, "点击我的等级")
    #     title = self.get_text(myloc.toolbar_title, "获取我的等级页title")
    #     return title

    # '''进入庄园'''
    # def intoManor(self):
    #     self.click_element(myloc.rlManor, "点击庄园")
    #     title = self.get_text(myloc.toolbar_title, "获取庄园页title")
    #     return title

    # '''进入尊享会员'''
    # def intoMember(self):
    #     self.click_element(myloc.layoutProfileMember, "点击尊享会员")
    #     title = self.get_text(loc.toolbar_title, "获取尊享会员页title")
    #     return title

    # '''进入vip特权'''
    # def intoVIPGrade(self):
    #     self.click_element(loc.layoutProfileVIPGrade, "点击vip特权")
    #     title = self.get_text(loc.toolbar_title, "获取vip特权页title")
    #     return title

    # '''进入我的家族'''
    # def intoFamily(self):
    #     self.click_element(loc.layoutProfileFamilyMine, "点击家族")
    #     title = self.get_text(loc.toolbar_title, "获取家族页title")
    #     return title

    # '''进入真爱团'''
    # def intoFans(self):
    #     self.click_element(loc.layoutProfileFansGroup, "点击粉丝团")
    #     title = self.get_text(loc.fanstitle, "获取粉丝团页title")
    #     return title

    # '''进入我的直播'''
    # def intoFLive(self):
    #     self.click_element(loc.layoutProfileLive, "点击我的直播")
    #     time.sleep(3)
    #     title = self.get_text(loc.toolbar_title, "获取我的直播页title")
    #     return title

    # '''进入贡献榜'''
    # def intoContribution(self):
    #     self.click_element(loc.layoutProfileContribution, "点击贡献榜")
    #     title = self.get_text(loc.toolbar_title, "获取自动回复页title")
    #     return title

    # '''进入我的守护'''
    # def intoGuardian(self):
    #     self.click_element(loc.layoutProfileGuardian, "点击守护")
    #     title = self.get_text(loc.toolbar_title, "获取守护页title")
    #     return title

    # '''进入自动回复'''
    # def intoResponse(self):
    #     self.click_element(loc.layoutProfileAutoResponse, "点击自动回复")
    #     title = self.get_text(loc.toolbar_title, "获取自动回复页title")
    #     return title

    # '''进入谁看过我'''
    # def intoFootPrint(self):
    #     self.click_element(loc.layoutProfileFootPrint, "点击谁看过我")
    #     title = self.get_text(loc.toolbar_title, "获取谁看过我页title")
    #     return title

    # '''进入荣耀挑战赛'''
    # def intoPkHistory(self):
    #     self.swipeUp(t=3000)
    #     self.click_element(loc.layoutPkHistory, "点击荣耀挑战赛")
    #     title = self.get_text(loc.pktitle, "获取荣耀挑战赛页title")
    #     return title

    # '''进入我看过的'''
    # def intoWatchHistory(self):
    #     self.swipeUp(t=3000)
    #     self.click_element(loc.layoutWatchHistory, "点击我看过的")
    #     title = self.get_text(loc.toolbar_title, "获取我看过的页title")
    #     return title

    # '''进入官方客服'''
    # def intoackRL(self):
    #     self.click_element(loc.feedbackRL, "点击官方客服")
    #     title = self.get_text(loc.toolbar_title, "获官方客服页title")
    #     return title

    # '''进入帮助中心'''
    # def intoHelpCenter(self):
    #     self.click_element(loc.layoutHelpCenter, "点击帮助中心")
    #     title = self.get_text(loc.toolbar_title, "获取帮助中心页title")
    #     return title

    # '''进入联系我们'''
    # def intoContactUs(self):
    #     self.click_element(loc.layoutContactUs, "点击联系我们")
    #     title = self.get_text(loc.toolbar_title, "获取联系我们页title")
    #     return title
