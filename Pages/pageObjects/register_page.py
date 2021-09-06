from Common.basepage import BasePage
from Pages.pageLocators.register_loctaors import RegisterPageLocators as loc
from Pages.pageObjects.home_page import HomePage
from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
from Pages.pageObjects.Common_Buss import CommonBus

log = get_logger(logger_name="注册操作日志")
'''注册-页面操作行为'''


class RegisterPage(BasePage):
    '''注册-随机输入手机号操作行为'''

    def __init__(self, driver):
        super().__init__(driver)

        CommonBus(driver).gameinvit()
        # # 判断是否为游客
        # self.is_visitor()
        # 判断是否为可点击登录另一个账号页面
        CommonBus(driver).is_loginAnotherPage()
        # 是否为登录状态
        CommonBus(driver).is_login()

    def input_username(self, user):
        # self.click_element(loc.about_log, model="选择登录方式")
        self.wait_eleVisible(loc.phone, model="点击手机号登录")
        self.click_element(loc.phone, model="点击手机号登录")
        self.wait_eleVisible(loc.select_countries, model="选择国家")
        self.click_element(loc.select_countries, model="选择国家")

        self.wait_eleVisible(loc.input_countries, model="输入国家")
        self.input_text(loc.input_countries, "中国内地", model="输入中国内地")

        self.wait_element_clickable(loc.clice_China, model="等待元素可被点击")
        self.click_element(loc.clice_China, model="点击中国内地")

        self.wait_eleVisible(loc.phone_loc, model="输入手机号")
        self.input_text(loc.phone_loc, user, model="输入手机号")

        self.click_element(loc.clice_next, model="点击下一步")
        return self

    '''注册-输入验证码-密码'''

    def input_passwd(self, code, passwd):
        self.wait_eleVisible(loc.security_code, model="等待验证码可见在点击")
        self.input_text(loc.security_code, code, model="输入验证码")

        self.input_text(loc.passaw_loc, passwd, model="输入密码")

        self.click_element(loc.clice_next_1, model="点击确定")

        self.wait_eleVisible(loc.click_skip, model="查看跳过按钮可见")
        self.click_element(loc.click_skip, "点击跳过")

        self.Close_studio()

        self.skip()

        self.advertising()

        return HomePage(self.driver)

    '''进入直播间点击关闭'''

    def Close_studio(self):
        if self.is_desplayed(loc.exit_button):
            self.click_element(loc.exit_button, model="进入直播间点击关闭")
        else:
            pass

    '''关闭完点击跳过'''

    def skip(self):
        if self.is_desplayed(loc.skip):
            self.click_element(loc.skip, model="关注主播点击跳过")
        else:
            pass

    '''注册成功后，查看首页是否有临时广告'''

    def advertising(self):
        if self.is_desplayed(loc.close_AD):
            self.click_element(loc.close_AD, model="临时点击跳过广告")
        else:
            pass


