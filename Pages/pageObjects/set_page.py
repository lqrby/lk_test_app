from Common.basepage import BasePage
from Pages.pageLocators.set_locators import SetPageLocator as loc
import time

'''设置-页面操作行为'''


class SetPage(BasePage):
    ''''''
    '''进入设置'''

    def set(self):
        self.wait_eleVisible(loc.click_my, model="等待我的")
        self.click_element(loc.click_my, model="点击我的")

        self.click_element(loc.click_set, model="点击设置")
        return self

    '''进入二级模块返回操作'''

    def back_key(self):
        self.wait_eleVisible(loc.click_back, model="等待返回")
        self.click_element(loc.click_back, model="点击返回")
        return self

    '''账号绑定'''

    def set_Account_binding(self):
        self.wait_eleVisible(loc.click_Account_binding, model="等待账号绑定")
        self.click_element(loc.click_Account_binding, model="点击账号绑定")

        self.wait_eleVisible(loc.get_title, model="等待查看title")
        el = self.get_text(loc.get_title, model="获取账号绑定title")

        self.wait_eleVisible(loc.click_back, model="等待返回")
        self.click_element(loc.click_back, model="点击返回")
        time.sleep(4)

        return el

    '''实名认证'''

    def set_real_name(self, name, number):
        self.wait_eleVisible(loc.click_real_name, model="等待实名认证")
        self.click_element(loc.click_real_name, model="点击实名认证")

        self.input_text(loc.input_name, name, model="输入姓名")
        self.input_text(loc.input_number, number, model="输入身份证号")

        self.click_element(loc.click_authentication, model="点击认证身份")

        el = self.get_text(loc.get_text, model="获取错误的身份证信息")

        self.wait_eleVisible(loc.click_back, model="等待返回")
        self.click_element(loc.click_back, model="点击返回")

        self.wait_eleVisible(loc.click_back, model="等待返回")
        self.click_element(loc.click_back, model="点击返回")

        return el

    '''我的直播标签'''

    def my_live_tag(self):
        self.click_element(loc.click_lable, model="点击我的直播标签")

        self.click_element(loc.click_cute, model="点击乖巧可爱")

        self.click_element(loc.click_Sound_lovers, model="点击声音恋人")

        self.wait_eleVisible(loc.click_save, model="等待保存")
        self.click_element(loc.click_save, model="点击保存")

        el = self.get_toast()
        return el.text

    '''黑名单'''

    def blacklist(self):
        self.click_element(loc.click_blacklist, model="点击黑名单")

        el = self.get_text(loc.get_text_blacklist, model="获取黑名单信息做断言")

        self.click_element(loc.click_back, model="点击返回")

        return el

    '''消息提醒'''
    def notificationSettingsRL(self):
        self.click_element(loc.click_message, model="点击消息提醒")
        self.click_element(loc.click_host_to_push, model="点击主播推送消息")
        time.sleep(2)
        if self.is_element_exist(loc.click_No_disturbing[1]):
            self.click_element(loc.click_No_disturbing, model="点击消息免打扰")
        self.click_element(loc.click_dynamic, model="点击动态评论提箱")
        self.click_element(loc.click_user_to_chat)
        self.click_element(loc.click_invite, model="点击邀请入群提醒")
        self.click_element(loc.click_game, model="点击游戏消息提醒")
        self.click_element(loc.click_back, model="点击返回")
        return True

    '''隐私设置'''
    def privacy(self):
        self.swipeUp()
        self.click_element(loc.click_privacy, model="点击隐私设置")
        self.click_element(loc.click_facebook, model="点击查看Facebook好友")
        self.click_element(loc.click_distance, model="点击显示距离")
        self.click_element(loc.click_location, model="点击显示定位")
        self.click_element(loc.click_back, model="点击返回")
        return True

    '''礼物设置'''
    def gift(self):
        self.click_element(loc.click_gift, model="点击礼物设置")
        self.click_element(loc.click_direct_broadcasting, model="点击直播间公告开关")
        self.click_element(loc.click_effects, model="点击礼物特效开关")
        self.click_element(loc.click_back, model="点击返回")
        return True

    '''点击悬浮窗播放开关'''
    def floatWindowSwitch(self):
        self.click_element(loc.floatWindowSwitch, model="点击悬浮窗播放开关")
        return True

    '''点击直播性能优化开关'''
    def broadcastHardwareSwitch(self):
        self.click_element(loc.broadcastHardwareSwitch, model="点击启动直播性能优化")
        return True

    '''关于Up直播'''
    def aboutRL(self):
        self.click_element(loc.aboutRL, model="点击关于Up直播")
        time.sleep(1)
        toolbar_title = self.get_text(loc.toolbar_title, model="获取关于页title")
        self.click_element(loc.click_back, model="点击返回")
        return toolbar_title
