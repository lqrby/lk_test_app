'''
@File    :  my_page.py    
@Contact :  fangfang.song@asiainnovations.com

@Modify Time    2021/4/1 10:01 下午    
@Author  :  songfang  
@Version :  1.0
@Desciption : 
'''
import time

from Common.basepage import BasePage
from Pages.pageLocators.my_locators import MyLocators as loc


class MyPage(BasePage):

    '''进入设置'''
    def my(self):
        self.wait_eleVisible(loc.click_my, model="等待我的")
        self.click_element(loc.click_my, model="点击我的")
        return self

    '''返回'''
    def back(self):
        if self.is_element_exist(loc.back[1]):
            self.click_element(loc.back, "点击返回")
        if self.is_element_exist(loc.goback[1]):
            self.click_element(loc.goback, "点击返回")
        if self.is_element_exist(loc.CSback[1]):
            self.click_element(loc.CSback, "点击返回")

    '''进入个人资料编辑页'''
    def intoEdit(self):
        self.click_element(loc.sdVipCover, "点击用户头像")
        self.click_element(loc.edit, "点击编辑")
        title = self.get_text(loc.toolbar_title, "获取编辑页title")
        return title

    '''进入个人资料页'''
    def intoProfile(self):
        self.click_element(loc.sdVipCover, "点击头像")
        title = self.get_text(loc.layoutName, "获取昵称")
        return title

    '''进入钱包'''
    def intoMoneyBar(self):
        self.click_element(loc.txtWalletLabel, "点击钱包")
        title = self.get_text(loc.toolbar_title, "获取钱包页title")
        return title

    '''进入任务中心'''
    def intoTask(self):
        self.click_element(loc.layoutTaskCenter, "点击任务中心")
        title = self.get_text(loc.toolbar_title, "获取任务中心页title")
        return title

    '''进入我的消息'''
    def intoMessage(self):
        self.swipeUp(t=3000)
        self.click_element(loc.layoutProfileIM, "点击消息")
        title = self.get_text(loc.messagetitle, "获取消息页title")
        return title

    '''进入背包'''
    def intoBag(self):
        self.click_element(loc.layoutProfileBag, "点击背包")
        title = self.get_text(loc.toolbar_title, "获取背包title")
        return title

    '''进入商城'''
    def intoFerrari(self):
        self.click_element(loc.layoutProfileFerrari, "点击商城")
        title = self.get_text(loc.toolbar_title, "获取背包title")
        return title

    '''进入我的等级'''
    def intoGrade(self):
        self.click_element(loc.layoutProfileGrade, "点击我的等级")
        title = self.get_text(loc.toolbar_title, "获取我的等级页title")
        return title

    '''进入庄园'''
    def intoManor(self):
        self.click_element(loc.rlManor, "点击庄园")
        title = self.get_text(loc.toolbar_title, "获取庄园页title")
        return title

    '''进入尊享会员'''
    def intoMember(self):
        self.click_element(loc.layoutProfileMember, "点击尊享会员")
        title = self.get_text(loc.toolbar_title, "获取尊享会员页title")
        return title

    '''进入vip特权'''
    def intoVIPGrade(self):
        self.click_element(loc.layoutProfileVIPGrade, "点击vip特权")
        title = self.get_text(loc.toolbar_title, "获取vip特权页title")
        return title

    '''进入我的家族'''
    def intoFamily(self):
        self.click_element(loc.layoutProfileFamilyMine, "点击家族")
        title = self.get_text(loc.toolbar_title, "获取家族页title")
        return title

    '''进入真爱团'''
    def intoFans(self):
        self.click_element(loc.layoutProfileFansGroup, "点击粉丝团")
        title = self.get_text(loc.fanstitle, "获取粉丝团页title")
        return title

    '''进入我的直播'''
    def intoFLive(self):
        self.click_element(loc.layoutProfileLive, "点击我的直播")
        time.sleep(3)
        title = self.get_text(loc.toolbar_title, "获取我的直播页title")
        return title

    '''进入贡献榜'''
    def intoContribution(self):
        self.click_element(loc.layoutProfileContribution, "点击贡献榜")
        title = self.get_text(loc.toolbar_title, "获取自动回复页title")
        return title

    '''进入我的守护'''
    def intoGuardian(self):
        self.click_element(loc.layoutProfileGuardian, "点击守护")
        title = self.get_text(loc.toolbar_title, "获取守护页title")
        return title

    '''进入自动回复'''
    def intoResponse(self):
        self.click_element(loc.layoutProfileAutoResponse, "点击自动回复")
        title = self.get_text(loc.toolbar_title, "获取自动回复页title")
        return title

    '''进入谁看过我'''
    def intoFootPrint(self):
        self.click_element(loc.layoutProfileFootPrint, "点击谁看过我")
        title = self.get_text(loc.toolbar_title, "获取谁看过我页title")
        return title

    '''进入荣耀挑战赛'''
    def intoPkHistory(self):
        self.swipeUp(t=3000)
        self.click_element(loc.layoutPkHistory, "点击荣耀挑战赛")
        title = self.get_text(loc.pktitle, "获取荣耀挑战赛页title")
        return title

    '''进入我看过的'''
    def intoWatchHistory(self):
        self.swipeUp(t=3000)
        self.click_element(loc.layoutWatchHistory, "点击我看过的")
        title = self.get_text(loc.toolbar_title, "获取我看过的页title")
        return title

    '''进入官方客服'''
    def intoackRL(self):
        self.click_element(loc.feedbackRL, "点击官方客服")
        title = self.get_text(loc.toolbar_title, "获官方客服页title")
        return title

    '''进入帮助中心'''
    def intoHelpCenter(self):
        self.click_element(loc.layoutHelpCenter, "点击帮助中心")
        title = self.get_text(loc.toolbar_title, "获取帮助中心页title")
        return title

    '''进入联系我们'''
    def intoContactUs(self):
        self.click_element(loc.layoutContactUs, "点击联系我们")
        title = self.get_text(loc.toolbar_title, "获取联系我们页title")
        return title
