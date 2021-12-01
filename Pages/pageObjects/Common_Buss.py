from os import truncate
import time, random

from appium.webdriver.extensions.search_context import mobile
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException 
from Common.log import get_logger
from Pages.pageLocators.login_locators import LoginPageLocator
from Pages.pageLocators.home_locators import HomePageLocator as loc
from Pages.pageLocators.my_locators import MyLocators as my
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from appium.webdriver.common.touch_action import TouchAction 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.pageObjects.sign_pop_page import SignPopPage
from Pages.pageLocators.pop_locators import PopUpLocator

log = get_logger(logger_name="注册操作日志")


'''App页面公共可使用的方法'''


class CommonBus(BasePage):
    '''输入文本内容，跳转至某个页面'''
    def __init__(self, driver):
        super().__init__(driver)
        self.popPage = SignPopPage(driver)

    def switch_navigate(self, name):
        loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(name))
        self.wait_eleVisible(loc)
        self.click_element(loc)

    def navigate(self, id):
        loc = (MobileBy.ID, "{}".format(id))
        self.wait_eleVisible(loc)
        self.click_element(loc)

    
    def get_userStatus(self):
            log.info("===========检查用户登录状态========")
            self.close_page_popUp()
            if self.is_element_exist(loc.dating_module):
                self.close_page_popUp()
                return True
            else:
                log.info("用户未登录")
                return False    
        
    # 退出登录
    def login_Out(self):
        self.click_element(my.meBtn, model="点击我的") 
        time.sleep(2)
        self.popPage.check_goddess_Popup() #关闭女神引导弹窗
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
            # log.info("result======={}".format(result))
            assert result == True
            log.info("{}===断言通过,{} == {}".format(model,result,True))
            return False
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model=model)
            return True


    # 断言是否包含
    def assert_in(self, text, contain_text, model=None):
        try:
            assert text in contain_text
            log.info("{}===断言通过,{} 包含 {}".format(model,"contain_text",text))
            return True
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model=model)
            return False

    # 断言元素长度
    def assert_len(self, elements, dyj=0, model=None):
        try:
            assert len(elements) > dyj
            log.info("{}===断言通过,{} > {}".format(model,len(elements),dyj))
            return True
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model=model)
            return False


    # 断言文本长度
    def assert_text_len(self, text, dyj=0, model=None):
        try:
            assert len(text) > dyj
            log.info("断言通过,文本长度是:{}".format(len(text)))
            return True
        except Exception as e:
            log.info("断言错误,文本长度是:{}".format(len(text)))
            self.save_webImgs(model=model)
            return False

    


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
        self.wait_element_presence(slider_element,model="等待滑块按钮")
        seekBar = self.get_element(slider_element,model="获取滑块按钮").get_attribute("bounds")
        # print("seekBar===",seekBar,type(seekBar))
        e = self.get_coordinate(seekBar)
        start_X = e[0]+20
        TouchAction(self.driver).press(x=start_X, y=random.randint(e[1]+2,e[3]-2))\
            .wait(500).move_to(x=start_X + 100, y=random.randint(e[1]+2,e[3]-2))\
            .wait(500).move_to(x=start_X + 260, y=random.randint(e[1]+2,e[3]-2)).wait(500)\
            .move_to(x=start_X + 300, y=random.randint(e[1]+2,e[3]-2)).wait(500).release().perform()
        self.wait_element_presence(LoginPageLocator.codeInput,model="验证码输入框")

    
    # 列表长度及断言
    def public_list(self,list_loc,model,dyj=0):
        if self.is_element_exist(list_loc):
            avatars = self.get_elements(list_loc,model="获取{}".format(model))  
            self.assert_len(avatars,dyj=dyj,model="{}断言".format(model)) 
            return avatars
        else:
            log.info("{}暂无数据".format(model))    
            self.save_webImgs("{}暂无数据".format(model))
            return False
    
    '''切换tap'''
    def find_tap(self,find_element,location_element,find_model,location_model,t=500,loop=1):
        if self.is_element_exist(find_element):
            self.wait_click_element(find_element,find_model) 
        else:
            self.wait_element_presence(location_element,model="{}".format(location_model))
            gift_button = self.get_element(location_element,model="获取{}对象".format(location_model)).get_attribute("bounds")
            e = self.get_coordinate(gift_button)
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.8
            y1 = e[1]+20
            x2 = l['width'] * 0.2
            self.driver.swipe(x1, y1, x2, y1, t)
            if loop > 0:
                self.find_tap(find_element,location_element,find_model,location_model,t=t,loop=loop-1)

    #退出app，结束程序运行
    def exit_and_overRun(self):
        self.driver.close_app()
        self.driver.quit()