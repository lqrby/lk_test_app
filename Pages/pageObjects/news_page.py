from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageLocators.square_locators import SquareLocators as squareloc
from Common.log import get_logger
import time, random
from Pages.pageObjects.sign_pop_page import SignPopPage
from Pages.pageLocators.news_locators import NewsLocators as newsloc
from Pages.pageLocators.home_locators import HomePageLocator as homeloc
from Pages.pageObjects.room_page import RoomPage

'''消息模块操作行为'''
log = get_logger(logger_name="消息操作日志")

class NewsPage(CommonBus):
    '''消息模块'''
    def __init__(self, driver):
        self.driver = driver
        self.popPage = SignPopPage(self.driver)
        self.roomPage = RoomPage(self.driver)
    
    '''
    通讯录
    '''
    def mail_list(self):
        self.wait_click_element(homeloc.message_moduke,model="消息模块")
        time.sleep(2)
        self.wait_click_element(newsloc.iv_msg_contact,model="通讯录按钮")
        result = self.public_list(newsloc.tv_position,model="关注列表") 
        if result:
            followlist = self.get_elements(newsloc.tv_position,model="关注列表元素")
            num = random.randint(0,len(followlist) - 1)
            followlist[num].click()
            time.sleep(5)
            self.assert_true(newsloc.buttonSendMessage,model="关注聊天页断言")
            self.roomPage.go_back()
        self.wait_click_element(newsloc.tv_title_two,model="粉饰tap")
        fs = self.public_list(newsloc.tv_position,model="粉丝列表")
        if fs:
            twolist = self.get_elements(newsloc.tv_position,model="粉丝列表元素")
            number = random.randint(0,len(twolist) - 1)
            twolist[number].click()
            self.assert_true(newsloc.buttonSendMessage,model="粉丝聊天页断言")
            self.roomPage.go_back()
        self.wait_click_element(newsloc.tv_title_three,model="好友tap")
        hylist = self.public_list(newsloc.tv_position,model="好友列表")
        if hylist:
            threelist = self.get_elements(newsloc.tv_position,model="好友列表元素")
            threenumber = random.randint(0,len(threelist) - 1)
            threelist[threenumber].click()
            self.assert_true(newsloc.buttonSendMessage,model="好友聊天页断言") 
            self.roomPage.go_back()
        self.wait_click_element(newsloc.iv_extra,model="添加好友按钮")
        self.assert_true(newsloc.et_input,model="搜索输入框断言") 
        page_source_result = self.driver.page_source
        self.assert_in("推荐聊天室",page_source_result,model="推荐聊天室标题")
        self.assert_in("附近在玩",page_source_result,model="附近在玩标题")
        self.roomPage.go_back()
        self.roomPage.go_back()
        time.sleep(2)
        return True
        
    