from Common.basepage import BasePage
from Pages.iOS_pageLocators.login_locators import LoginPageLocator as loc
from Pages.iOS_pageObjects.home_page import HomePage


"""登录-页面操作行为"""
class LoginPage(BasePage):
    def login_check(self):
        # 是否是游客模式 loc.guest_login[1]
        if self.is_element_exist("登录"):
            self.click_element(loc.guest_login, model="点击登录")
        # 是否是登录状态

    """成功登录操作行为"""
    def login_iOS_phone(self, user, passwd):
        self.wait_eleVisible(loc.phone, model="点击手机号登录")
        self.click_element(loc.phone, model="点击手机号登录")

        # self.wait_eleVisible(iOS_page.select_countries, model="选择国家")
        # self.click_element(iOS_page.select_countries, model="选择国家")
        #
        # self.wait_eleVisible(iOS_page.input_countries, model="输入国家")
        # self.input_text(iOS_page.input_countries, "中国内地", model="输入中国内地")
        #
        # self.wait_element_clickable(iOS_page.clice_China, model="等待元素可被点击")
        # self.click_element(iOS_page.clice_China, model="点击中国内地")

        self.wait_eleVisible(loc.phone_loc, model="输入手机号")
        self.input_text(loc.phone_loc, user, model="输入手机号")

        self.click_element(loc.clice_next, model="点击确定")

        self.wait_eleVisible(loc.passaw_loc, model="输入密码")
        self.input_text(loc.passaw_loc, passwd, model="输入密码")

        self.click_element(loc.clice_next_pwd, model="点击确定")

        login_text = self.isToastMessage(loc.login_text)
        # print(login_text)
        return login_text

    """手机号输入错误 / 获取错误的toast"""
    def error_toast(self):
        el = self.get_toast()
        return el.text
