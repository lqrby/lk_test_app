import time, random
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from Common.log import get_logger
from Pages.pageLocators.login_locators import LoginPageLocator
from Pages.pageLocators.home_locators import HomePageLocator as loc
from Pages.pageLocators.my_locators import MyLocators as my
from appium.webdriver.common.touch_action import TouchAction 
from Pages.pageObjects.sign_pop_page import SignPopPage

log = get_logger(logger_name="公共模块操作日志")


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
            if self.is_element_exist(loc.dating_module,model="交友tap"):
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
        if self.is_element_exist(my.setUpBtn,model="设置按钮元素") == False:
           self.swipeUp() 

        self.wait_click_element(my.setUpBtn, model="点击设置")

        self.wait_click_element(my.logoutBtn, model="点击退出登录按钮")

        self.wait_click_element(my.logoutOkBtn, model="点击确认退出按钮")
        
        log.info("===========退出登录========")



    # 是否登录状态，已登录则退出登录
    def check_loggedIn_signOut(self):
        if self.is_element_exist(LoginPageLocator.agree,model="同意按钮元素"):
            pass
        elif self.get_userStatus():
            log.info("===========用户是登录状态，开始退出========")
            self.login_Out()
        else:
            pass
    
    # 断言是否为真
    def assert_true(self, assert_loc, model=None):
        try:
            result = self.is_element_exist(assert_loc,model=model)
            # log.info("result======={}".format(result))
            assert result == True
            log.info("{}===断言通过,{} == {}".format(model,result,True))
            return True
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model=model)
            return False


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
    def assert_len(self, list_loc, dyj=0, model=None):
        try:
            if self.is_element_exist(list_loc,model=model):
                avatars = self.get_elements(list_loc,model="获取{}元素".format(model))
                assert len(avatars) > dyj
                log.info("{}===断言通过,{} > {}".format(model,len(avatars),dyj))
                return avatars
            else:
                log.info("元素不存在：{}".format(list_loc))
                self.save_webImgs(model=model)
                return False
        except Exception as e:
            log.info("{}断言错误".format(model))
            self.save_webImgs(model=model)
            return False
            
    # 断言元素长度
    def assert_equal(self, dy_loc, dyj=0, model=None):
        try:
            self.wait_element_presence(dy_loc,model=model)
            yslist = self.get_elements(dy_loc,model=model)
            assert len(yslist) == dyj
            log.info("{}===断言通过,{} == {}".format(model,len(yslist),dyj))
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

    
    '''切换tap'''
    def find_tap(self,find_element,location_element,find_model,location_model,t=500,loop=1):
        if self.is_element_exist(find_element,model=find_model):
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

    
    