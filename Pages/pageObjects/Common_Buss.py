import time, random
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException 
from Common.log import get_logger
from Pages.pageLocators.pop_locators import PopUpLocator as poploc
from Pages.pageLocators.login_locators import LoginPageLocator
from Pages.pageLocators.home_locators import HomePageLocator as loc
from Pages.pageLocators.my_locators import MyLocators as my
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from appium.webdriver.common.touch_action import TouchAction 

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
            
            log.info("===========检查用户登录状态========")
            self.wait_element_presence(loc.dating_module)
            self.check_error_popup() #检查异常退出弹窗
            self.check_goddess_Popup() #检查房间引导弹窗
            # self.find_element(loc.dating_module)
            return True
        except NoSuchElementException:
            log.info("用户未登录")
            return False

    # 退出登录
    def login_Out(self):
        self.click_element(my.meBtn, model="点击我的") 
        time.sleep(2)
        self.check_goddess_Popup() #关闭女神引导弹窗
        if self.is_element_exist(my.setUpBtn) == False:
           self.swipeUp() 
        self.wait_element_clickable(my.setUpBtn, model="点击设置")
        self.click_element(my.setUpBtn, model="点击设置") 

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
            self.login_Out()
        else:
            pass
    
    # 断言是否为真
    def assert_true(self, assert_element, model=None):
        try:
            result = self.is_element_exist(assert_element)
            assert result == True
            log.info("{}===断言通过,{} == {}".format(model,result,True))
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model="{}断言错误".format(model))


    # 断言是否包含
    def assert_in(self, text, contain_text, model=None):
        try:
            assert text in contain_text
            log.info("{}===断言通过,{} 包含 {}".format(model,"contain_text",text))
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model="{}断言错误".format(model))

    # 断言长度
    def assert_len(self, elements, dyj=0, model=None):
        try:
            assert len(elements) > dyj
            log.info("{}===断言通过,{} > {}".format(model,len(elements),dyj))
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model="{}断言错误".format(model))


    #返回元素坐标
    def get_coordinate(self,bounds):
        b= bounds.replace("][",",")
        c = b.replace("]","")
        d = c.replace("[","")
        e = d.split(",")
        numList = []
        for i in e:
            numList.append(int(i))
        return numList
    

    #滑动滑块儿
    def drag_slider(self,slider_element):
        time.sleep(1)
        self.wait_element_presence(slider_element,model="滑块按钮")
        seekBar = self.get_element(slider_element).get_attribute("bounds")
        # print("seekBar===",seekBar,type(seekBar))
        e = self.get_coordinate(seekBar)
        start_X = e[0]+20
        TouchAction(self.driver).press(x=start_X, y=random.randint(e[1]+2,e[3]-2))\
            .wait(500).move_to(x=start_X + 100, y=random.randint(e[1]+2,e[3]-2))\
            .wait(500).move_to(x=start_X + 260, y=random.randint(e[1]+2,e[3]-2)).wait(500)\
            .move_to(x=start_X + 300, y=random.randint(e[1]+2,e[3]-2)).wait(500).release().perform()
        self.wait_element_presence(LoginPageLocator.codeInput)

    #检查并关闭异常弹窗            
    def check_error_popup(self):
        self.exist_be_click(poploc.iv_cancel)


    #检查并关闭未成年设置弹窗            
    def check_MinorSettings(self):
        time.sleep(2)
        self.exist_be_click(poploc.setting_minors)

    #检查关闭女神开播引导弹窗       
    def check_goddess_Popup(self):
        self.exist_be_click(poploc.close_back)
        
        

