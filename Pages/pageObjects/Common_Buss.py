import time
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
from Pages.pageLocators.streaming_locators import StreamingPageLocators
from Pages.pageLocators.pop_locators import PopUp
from Pages.pageLocators.login_locators import LoginPageLocator
from Pages.pageLocators.home_locators import HomePageLocator as loc
from Pages.pageLocators.my_locators import MyLocators as my
from Pages.pageLocators.room_locators import RoomPageLocator as RM
from selenium.webdriver.support.ui import WebDriverWait

log = get_logger(logger_name="注册操作日志")


'''App页面公共可使用的方法'''


class CommonBus(BasePage):
    '''输入文本内容，跳转至某个页面'''

    def switch_navigate(self, name):

        loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(name))
        self.wait_eleVisible(loc)
        self.click_element(loc)

    def navigate(self, id):
        loc = (MobileBy.ID, "{}".format(id))
        self.wait_eleVisible(loc)
        self.click_element(loc)

    # 开播后退出直播间
    def Get_out_of_the_studio(self):
        self.wait_eleVisible(StreamingPageLocators.quit_1, model="退出直播间")
        self.click_element(StreamingPageLocators.quit_1, model="退出直播间")

        self.wait_eleVisible(StreamingPageLocators.certain, model="确定退出")
        self.click_element(StreamingPageLocators.certain, model="确定退出")

        self.wait_eleVisible(StreamingPageLocators.certain, model="直播页关闭返回首页")
        self.click_element(StreamingPageLocators.certain, model="直播页关闭返回首页")

    # 运行完后退出App
    def quit_login(self):
        self.wait_eleVisible(HomePageLocator.click_me, model="点击我的")
        self.click_element(HomePageLocator.click_me, model="点击我的")

        self.wait_eleVisible(HomePageLocator.click_set, model="点击设置")
        self.click_element(HomePageLocator.click_set, model="点击设置")
        time.sleep(3)
        self.swipeUp()

        self.wait_eleVisible(HomePageLocator.click_quit, model="点击退出登录")
        self.click_element(HomePageLocator.click_quit, model="点击退出登录")

        self.wait_eleVisible(HomePageLocator.click_confirm, model="确定退出")
        self.click_element(HomePageLocator.click_confirm, model="确定退出")
        return self

    '''关闭游戏弹窗'''

    def gameinvit(self):
        if self.is_desplayed(HomePageLocator.closeGameInvit):
            self.click_element(HomePageLocator.closeGameInvit, model="关闭游戏弹窗")
        else:
            pass

    '''判断是否有隐私政策弹窗'''

    def privacy(self):
        if self.is_element_exist("感谢您使用Up直播"):
            self.click_element(HomePageLocator.dialog)
            self.click_element(HomePageLocator.txtOk)
            time.sleep(1)
        else:
            pass

    '''判断是否为游客'''

    def is_visitor(self):
        if self.is_desplayed(HomePageLocator.loginPop):
            self.click_element(HomePageLocator.loginPop)
        else:
            pass

    '''# 判断是否为可登录另一个账号页面'''

    def is_loginAnotherPage(self):
        if self.is_desplayed(HomePageLocator.loginAnother):
            self.click_element(HomePageLocator.loginAnother)
        else:
            pass

    '''登录状态下退出登录'''

    def is_login(self):
        if self.is_desplayed(HomePageLocator.click_me):
            try:
                # self.wait_eleVisible(HomePageLocator.click_me)
                self.click_element(HomePageLocator.click_me)
                self.wait_eleVisible(HomePageLocator.click_set)
                self.swipeUp()
                
                if self.get_text(HomePageLocator.click_set) == "设置":
                    self.click_element(HomePageLocator.click_set)
                    # self.click_element(HomePageLocator.logout)
                    self.wait_eleVisible(HomePageLocator.allowlogout)
                    self.click_element(HomePageLocator.allowlogout)
                    self.is_loginAnotherPage()
                elif self.get_text(HomePageLocator.logout) == "切换账号":
                    self.click_element(HomePageLocator.logout)
                else:
                    pass
            except Exception as e:
                log.info(e)
        elif self.is_element_exist("com.asiainno.uplive:id/txtLoginAnother"):
            self.is_loginAnotherPage()

    '''注册成功后，查看首页是否有临时广告'''

    def advertising(self):
        if self.is_desplayed(HomePageLocator.close_AD):
            self.click_element(HomePageLocator.close_AD, model="临时点击跳过广告")
        else:
            pass

    # 系统弹窗
    def systempop(self):
        if self.is_element_exist(PopUp.allowpop1[1]):
            self.click_element(PopUp.allowpop1, model="点击允许电话权限弹窗")
            time.sleep(1)
        else:
            pass

    # 允许定位弹窗
    def locatpop(self):
        if self.is_element_exist("允许定位"):
            self.click_element(PopUp.allowlocat)
            time.sleep(3)
            self.click_element(PopUp.onlyappallow)
        else:
            pass

    
    #检查是否有用户协议
    def check_agreement_one(self):
        log.info("检查用户协议弹窗按钮")
        time.sleep(2)
        try:
            agreementBtn = self.find_element(LoginPageLocator.agree)
        except NoSuchElementException:
            log.info("无用户协议弹窗按钮")
        else:
            agreementBtn.click()

    #检查是否有用户协议2
    def check_agreement_two(self):
        log.info("检查用户协议确认按钮")
        try:
            determineBtn = self.find_element(LoginPageLocator.determine)
        except NoSuchElementException:
            log.info("无用户协议确认按钮")
        else:
            determineBtn.click()

    def get_userStatus(self):
        try:
            log.info("===========检查用户在线状态========")
            self.check_error_popup()
            self.find_element(loc.dating_module)
            return True
        except NoSuchElementException:
            log.info("用户未登录")
            return False

    # 退出登录
    def login_Out(self):
        self.click_element(my.meBtn, model="点击我的")
        self.wait_element_clickable(my.setUpBtn, model="点击设置")
        self.click_element(my.setUpBtn)
        self.wait_element_clickable(my.logoutBtn, model="点击退出登录按钮")
        self.click_element(my.logoutBtn, model="点击退出登录按钮")
        self.wait_element_clickable(my.logoutOkBtn, model="点击确认退出按钮")
        self.click_element(my.logoutOkBtn, model="点击确认退出按钮")
        log.info("===========退出登录========")



    # 是否登录状态，已登录则退出登录
    def check_loggedIn_signOut(self):
        if self.is_element_exist(LoginPageLocator.agree):
            pass
        elif self.get_userStatus():
            log.info("===========用户是登录状态，开始退出========")
            self.click_element(my.meBtn, model="点击我的")
            self.wait_element_clickable(my.setUpBtn, model="点击设置")
            self.click_element(my.setUpBtn)
            self.wait_element_clickable(my.logoutBtn, model="点击退出登录按钮")
            self.click_element(my.logoutBtn, model="点击退出登录按钮")
            self.wait_element_clickable(my.logoutOkBtn, model="点击确认退出按钮")
            self.click_element(my.logoutOkBtn, model="点击确认退出按钮")
            log.info("===========退出登录========")
        else:
            pass



    #检查并关闭异常弹窗            
    def check_error_popup(self):
        self.exist_be_click(loc.iv_cancel)


    #检查并关闭未成年设置弹窗            
    def check_MinorSettings(self):
        time.sleep(2)
        self.exist_be_click(RM.btn_know)

    #检查关闭女神开播引导弹窗       
    def check_MinorSettings(self):
        self.exist_be_click(RM.close_back)
        
        

