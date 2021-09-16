import time, random
from PIL import Image
from PIL import ImageGrab
# from Common.basepage import BasePage
from Common.log import get_logger
from Pages.pageLocators.login_locators import LoginPageLocator as loc
# from Pages.pageLocators.home_locators import HomePageLocator as home_loc
from Pages.pageObjects.Common_Buss import CommonBus
# from Pages.pageObjects.home_page import HomePage
from testScript.db_util import MysqlDb

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.touch_actions import TouchActions

log = get_logger(logger_name="登录操作日志")


'''登录-页面操作行为'''


class LoginPage(CommonBus):

    def __init__(self, driver):
        # # 判断游戏弹窗
        # CommonBus(driver).gameinvit()
        # # # 判断是否为游客
        # CommonBus(driver).is_visitor()
        # 判断是否为可点击登录另一个账号页面
        # CommonBus(driver).is_loginAnotherPage()
        # # 是否为登录状态
        super().__init__(driver)
        # CommonBus(driver).is_login()

    # '''手机号成功登录操作行为'''
    # def login_bymobile_success(self, user, passwd):
    #     self.loginbymobile(user, passwd)
    #     return HomePage(self.driver)

    # '''微信登录成功操作'''

    # def login_bywechat_success(self):
    #     self.loginbywechat()
    #     return HomePage(self.driver)

    # '''微博登录成功操作'''

    # def login_byweibo_success(self):
    #     self.loginbyweibo()
    #     return HomePage(self.driver)

    # '''QQ登录成功操作'''

    # def login_byQQ_success(self):
    #     self.loginbyQQ()
    #     return HomePage(self.driver)

    # '''手机号验证码录成功操作'''
    # def login_phoneCode_success(self, phone):
    #     self.loginbyemail(phone)
    #     return HomePage(self.driver)


    
    '''手机号输入错误 / 获取错误的toast'''

    def error_toast(self):
        el = self.get_toast()
        return el.text

    # 手机号密码登录
    def login_mobile_passWord(self, user, passwd):
        self.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.phoneBtn, model="等待元素可被点击")
        self.click_element(loc.phoneBtn, model="点击手机号登录")
        self.wait_element_clickable(loc.nameAndPassBtn, model="等待元素可被点击")
        self.click_element(loc.nameAndPassBtn, model="点击账号密码登录")
        self.wait_element_presence(loc.username_type, model="等待元素显示")
        self.input_text(loc.username_type, user, model="输入手机号")
        self.input_text(loc.password_type, passwd, model="输入密码")
        self.click_element(loc.loginBtn, model="点击确定")
        self.check_agreement_two()
        userStatus = self.get_userStatus()
        return userStatus


    '''
    手机号验证码登录注册
    '''
    def login_phone_code(self, phone):
        self.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.phoneBtn, model="等待元素可被点击")
        self.click_element(loc.phoneBtn, model="点击手机号登录")
        # self.exist_be_click(loc.otherPhoneBtn) #存在则点击其它手机号登录
        self.wait_eleVisible(loc.et_phone, model="等待手机号可输入")
        self.input_text(loc.et_phone, phone, model="输入手机号")
        print("手机号是====={}".format(phone))
        sql = "select cnt from ourydc_app_sms where phone = {} order by insdt desc limit 1".format(phone)
        # print("sql===={}".format(sql))
        phoneNum = MysqlDb().query(sql)
        usedPhone = phoneNum[0]['cnt']
        print("旧验证码是======{}".format(usedPhone))
        self.click_element(loc.codeBtn, model="点击获取验证码")
        self.check_agreement_two()
        self.driver.implicitly_wait(8)
        self.drag_slider(loc.seekBar) #拖动滑块儿
        self.wait_eleVisible(loc.input_one, model="等待显示验证码输入框")
        time.sleep(3)
        phoneStr = ""
        for i in range(10):
            log.info("第{}次获取验证码".format(i+1))
            phoneNumber = MysqlDb().query(sql)
            if phoneNumber[0]['cnt'] != usedPhone:
                phoneStr = str(phoneNumber[0]['cnt'])
                log.info("新验证码是===={}".format(phoneStr))
                break
            else:
                time.sleep(4)
        eleArr = []
        for ele in loc.codeList:
            eleArr.append(self.get_element(ele))
        for obj,i in zip(eleArr,phoneStr):
            obj.click()
            self.driver.press_keycode(int(i)+7)
        self.driver.implicitly_wait(5)
        return self.get_userStatus()

    