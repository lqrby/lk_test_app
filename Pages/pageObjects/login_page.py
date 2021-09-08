import time
from PIL import Image
from PIL import ImageGrab
from selenium.webdriver.support import wait
from Common.basepage import BasePage
from Pages.pageLocators.login_locators import LoginPageLocator as loc
from Pages.pageLocators.home_locators import HomePageLocator as home_loc
from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageObjects.home_page import HomePage
from testScript.db_util import MysqlDb
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions


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

    '''微信登录成功操作'''

    def login_bywechat_success(self):
        self.loginbywechat()
        return HomePage(self.driver)

    '''微博登录成功操作'''

    def login_byweibo_success(self):
        self.loginbyweibo()
        return HomePage(self.driver)

    '''QQ登录成功操作'''

    def login_byQQ_success(self):
        self.loginbyQQ()
        return HomePage(self.driver)

    '''手机号验证码录成功操作'''
    def login_phoneCode_success(self, phone):
        self.loginbyemail(phone)
        return HomePage(self.driver)


    
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

    # 验证码登录
    def login_phone_code(self, phone):
        self.check_agreement_one() #同意用户协议
        self.wait_element_clickable(loc.phoneBtn, model="等待元素可被点击")
        self.click_element(loc.phoneBtn, model="点击手机号登录")
        self.wait_eleVisible(loc.et_phone, model="等待手机号可输入")
        self.input_text(loc.et_phone, phone, model="输入手机号")
        self.click_element(loc.codeBtn, model="点击获取验证码")
        time.sleep(2)
        self.check_agreement_two()
        time.sleep(2)
        # self.wait_eleVisible(loc.maxPicture, model="等待元素显示")
        # # result = self.driver.page_source
        # self.get_element(loc.maxPicture)
        # bbox = maxPictureObj.get_attribute("bounds")
        # im = ImageGrab.grab(bbox)
        # a=im.transpose(Image.ROTATE_90)
        # self.drag_right() # 滑动验证码
        TouchAction(self.driver).press(x=258,y=1212).wait(1000).move_to(x=700,y=1212).wait(1000).wait(500).release().perform()
        # for i in range(100):
            # TouchAction(self.driver).press(x=250+i,y=1212).move_to(x=500+i,y=1212).release().perform()
        # ta = TouchActions(self.driver)
        # ta.tap_and_hold(xcoord=258,ycoord=1212)
        # ta.perform()
        # ta.move(xcoord=700,ycoord=1212)
        # ta.perform()
        # ta.release(xcoord=700,ycoord=1212)
        # ta.perform()
        # time.sleep(10)
            
            # time.sleep(2)
            # time.sleep(5)
            # ActionChains(self.driver).move_by_offset(xoffset=258,yoffset=1212).perform() #获取当前鼠标的位置
            # ActionChains(self.driver).click_and_hold().perform() #鼠标左键单击不松开
            # ActionChains(self.driver).drag_and_drop_by_offset(xoffset=600,yoffset=1212).perform() #鼠标左键单击不松开
        # ActionChains(self.driver).click_and_hold().perform()
        # ActionChains(self.driver).drag_and_drop_by_offset(x=700,y=1212).perform()
        # self.wait_element_presence(loc.verification_code)
        # sql = "select cnt from ourydc_app_sms where phone = '18810798467' order by insdt limit 1"
        # data = MysqlDb().query(sql) 
        # if data:
        #     code = data[0]["cnt"]
        #     for i,number in enumerate(code):
        #         self.input_text(loc.codeList[i],number) # 输入文本
        #         time.sleep(0.5)
        # else:
        #     self.save_webImgs("数据库查询验证码失败截图")
        # userStatus = self.get_userStatus()
        return False


    # 微信登录
    def loginbywechat(self):
        self.click_element(loc.chooseScience, model="点击选择环境")
        self.click_element(loc.Science, model="点击选择stage")
        self.click_element(loc.wechat, model="点击微信登录")
        return self

    # QQ登录
    def loginbyQQ(self):
        self.click_element(loc.chooseScience, model="点击选择环境")
        self.click_element(loc.Science, model="点击选择stage")
        self.click_element(loc.QQ, model="点击QQ登录")
        self.click_element(loc.QQfds, model="点击QQ授权")
        return self

    # 微博登录
    def loginbyweibo(self):
        self.click_element(loc.chooseScience, model="点击选择环境")
        self.click_element(loc.Science, model="点击选择stage")
        self.click_element(loc.weibo, model="点击微博登录")
        return self
