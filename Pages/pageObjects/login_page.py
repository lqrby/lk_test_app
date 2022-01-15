from logging import fatal
import time, random
from Common.log import get_logger
from Pages.pageLocators.login_locators import LoginPageLocator as loc
from Pages.pageObjects.Common_Buss import CommonBus
from testScript.db_util import MysqlDb
from Pages.pageObjects.sign_pop_page import SignPopPage


log = get_logger(logger_name="登录操作日志")


'''登录-页面操作行为'''


class LoginPage(CommonBus):

    def __init__(self, driver):
        super().__init__(driver)
        self.popPage = SignPopPage(driver)
    

    '''微信登录成功操作'''
    def login_byWechat_success(self,wxName,wxPassword):
        self.popPage.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.wdChatBtn, model="等待微信按钮元素可被点击")
        self.click_element(loc.wdChatBtn, model="点击微信按钮")
        # if self.is_element_exist(loc.microblog_authorizeBtn):
        #     self.exist_be_click(loc.microblog_authorizeBtn) #点击微信授权按钮（假如微博已登录）
        if self.is_element_exist(loc.wx_name,model="微信名称"):
            self.wait_element_presence(loc.wx_name, model="微信账号输入框")
            self.clear_input_text(loc.wx_name, model="清除微信账号输入框")
            self.input_text(loc.wx_name,wxName,model="输入微信账号")

            self.wait_element_presence(loc.wx_password, model="微信密码输入框")
            self.clear_input_text(loc.wx_password, model="清除微信密码输入框")
            self.input_text(loc.wx_password,wxPassword,model="输入微信密码")

            self.wait_element_clickable(loc.wxLoginBtn,"微信登录按钮")
            self.click_element(loc.wxLoginBtn,model="点击微信登录按钮")
            self.wait_element_clickable(loc.clickBtn,model="检查验证按钮")
            self.click_element(loc.clickBtn,model="点击验证按钮")
        return self.get_userStatus()


    '''微博登录成功操作'''
    def login_byWeiBo_success(self,wbName,wbPassword):
        self.popPage.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.microblogBtn, model="等待微博按钮元素可被点击")
        self.click_element(loc.microblogBtn, model="点击微博按钮")
        self.driver.implicitly_wait(8)
        if self.is_element_exist(loc.microblog_authorizeBtn,model="微博授权"):
            self.exist_be_click(loc.microblog_authorizeBtn) #点击微博授权按钮（假如微博已登录）
        elif self.is_element_exist(loc.wb_name,model="微博名称"):
            self.wait_element_presence(loc.wb_name, model="微博账号输入框")
            self.clear_input_text(loc.wb_name, model="清除微博账号输入框")
            self.input_text(loc.wb_name,wbName,model="输入微博账号")

            self.wait_element_presence(loc.wb_password, model="微博密码输入框")
            self.clear_input_text(loc.wb_password, model="清除微博密码输入框")
            self.input_text(loc.wb_password,wbPassword,model="输入微博密码")

            self.wait_element_clickable(loc.wb_loginBtn,model="微博登录按钮")
            self.click_element(loc.wb_loginBtn,model="点击微博登录按钮")
            self.wait_element_clickable(loc.clickBtn,model="检查验证按钮")
            self.click_element(loc.clickBtn,model="点击验证按钮")
        return self.get_userStatus()


    '''
    QQ登录成功操作
    1.未登录，先登录再授权
    2.已登录，直接授权
    '''
    def login_byQQ_success(self,qqName,qqPassword):
        self.popPage.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.qqBtn, model="等待qq元素可被点击")
        self.click_element(loc.qqBtn, model="点击qq按钮")
        self.driver.implicitly_wait(5)
        if self.is_element_exist(loc.fdsBtn,model="qq授权按钮"):
            self.exist_be_click(loc.fdsBtn) #点击qq授权按钮（假如qq已登录）
            # self.exist_be_click(loc.otherqqLoginBtn) #点击其它qq登录
        elif self.is_element_exist(loc.scan_authorization,model="扫描授权"):
            self.wait_element_presence(loc.qqInputNane, model="qq账号输入框")
            self.clear_input_text(loc.qqInputNane, model="清除qq账号输入框")
            self.input_text(loc.qqInputNane,qqName,model="输入qq账号")
            self.wait_element_presence(loc.qqInputPass, model="qq密码输入框")
            self.clear_input_text(loc.qqInputPass, model="清除qq密码输入框")
            self.input_text(loc.qqInputPass,qqPassword,model="输入qq密码")
            self.wait_element_clickable(loc.qqLoginBtn,"qq登录按钮")
            self.click_element(loc.qqLoginBtn,model="点击qq登录按钮")
            self.driver.implicitly_wait(8)
            self.exist_be_click(loc.fdsBtn) #点击qq授权按钮（假如qq已登录）
        return self.get_userStatus()

    

    '''错误的手机号密码登录'''
    def error_mobile_passWord(self, user, passwd,expected):
        self.popPage.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.phoneBtn, model="等待元素可被点击")
        self.click_element(loc.phoneBtn, model="点击手机号登录")
        self.wait_element_clickable(loc.nameAndPassBtn, model="等待元素可被点击")
        self.click_element(loc.nameAndPassBtn, model="点击账号密码登录")
        self.wait_element_presence(loc.username_type, model="等待元素显示")
        self.input_text(loc.username_type, user, model="输入手机号")
        self.input_text(loc.password_type, passwd, model="输入密码")
        checked = self.get_element(loc.cb_agreement,model="获取用户协议勾选状态").get_attribute("checked")
        if checked == "false":
            self.click_element(loc.cb_agreement,model="用户协议勾选框")
        self.click_element(loc.loginBtn, model="点击确定")
        toast = self.get_toast_exist(expected)
        if toast and expected in toast:
            self.save_webImgs(model="账号密码登录失败")
            log.info("XXXXX账号密码登录失败XXXXX")
            return True
        else:
            return False
        

        

    '''正确的手机号密码登录'''
    def login_mobile_passWord(self, user, passwd,expected):
        self.popPage.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.phoneBtn, model="等待元素可被点击")
        self.click_element(loc.phoneBtn, model="点击手机号登录")
        self.wait_element_clickable(loc.nameAndPassBtn, model="等待元素可被点击")
        self.click_element(loc.nameAndPassBtn, model="点击账号密码登录")
        self.wait_element_presence(loc.username_type, model="等待元素显示")
        self.input_text(loc.username_type, user, model="输入手机号")
        self.input_text(loc.password_type, passwd, model="输入密码")
        checked = self.get_element(loc.cb_agreement,model="获取用户协议勾选状态").get_attribute("checked")
        if checked == "false":
            self.click_element(loc.cb_agreement,model="用户协议勾选框")
        self.click_element(loc.loginBtn, model="点击确定")
        toast = self.get_toast_exist(expected)
        if toast and expected in toast:
            log.info("XXXXX账号密码登录失败XXXXX")
            self.save_webImgs(model="账号密码登录失败")
            return False
        # self.popPage.check_agreement_two()
        userStatus = self.get_userStatus()
        return userStatus


    '''
    手机号验证码登录注册
    '''
    def login_phone_code(self, phone):
        self.popPage.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.phoneBtn, model="等待元素可被点击")
        self.click_element(loc.phoneBtn, model="点击手机号登录")
        # self.exist_be_click(loc.otherPhoneBtn) #存在则点击其它手机号登录
        self.wait_eleVisible(loc.et_phone, model="等待手机号可输入")
        self.input_text(loc.et_phone, phone, model="输入手机号")
        sql = "select cnt from ourydc_app_sms where phone = {} order by insdt desc limit 1".format(phone)
        phoneNum = MysqlDb().query(sql)
        usedPhone = phoneNum[0]['cnt']
        log.info("旧验证码是======{}".format(usedPhone))
        self.click_element(loc.codeBtn, model="点击获取验证码")
        self.popPage.check_agreement_two()
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
            eleArr.append(self.get_element(ele,model="获取单个验证码对象"))
        for obj,i in zip(eleArr,phoneStr):
            obj.click()
            self.driver.press_keycode(int(i)+7)
        return self.get_userStatus()

    