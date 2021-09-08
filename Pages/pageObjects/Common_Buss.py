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
    
    # 断言是否为真
    def assert_true(self, assert_element):
        try:
            assert self.is_element_exist(assert_element) == True
        except Exception as e:
            log.info("创建团队断言错误")
            self.save_webImgs(model="创建团队断言错误")

    #检查并关闭异常弹窗            
    def check_error_popup(self):
        self.exist_be_click(loc.iv_cancel)


    #检查并关闭未成年设置弹窗            
    def check_MinorSettings(self):
        time.sleep(2)
        self.exist_be_click(RM.btn_know)

    #检查关闭女神开播引导弹窗       
    def check_goddess_Popup(self):
        self.exist_be_click(RM.close_back)
        
        

