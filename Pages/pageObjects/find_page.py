from Pages.pageObjects.home_page import HomePage
from Common.basepage import BasePage

from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
import time

from Pages.pageLocators.pop_locators import PopUp
from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageLocators.home_locators import HomePageLocator as HL

log = get_logger(logger_name="首页操作日志")

'''首页-页面操作'''


# class FindPage(CommonBus):
#     #进入直播间
#     def enter_liveRoom(self):

#         tv_plays = self.get_elements(HL.tv_play, number = 3)
#         if len(tv_plays) > 0:
            
#             for play in tv_plays:
#                 play.click()
#                 self.wait_eleVisible(HL.roomIdTv)
#                 number = number - 1
#                 if number == 0:
#                     break

#     #点击未开播的用户
#     def enter_liveRoom(self):
#         tv_desArr = self.get_elements(HL.des, number = 3)
#         if len(tv_desArr) > 0:
#             for no_play in tv_desArr:
#                 no_play.click()
#                 self.wait_eleVisible(HL.tv_nick)
#                 number = number - 1
#                 if number == 0:
#                     break




    








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
