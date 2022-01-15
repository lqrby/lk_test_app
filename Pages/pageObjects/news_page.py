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
        self.replace_click(newsloc.tv_position,model="关注列表") #关注列表
        gzdy = self.assert_true(newsloc.editTextMessage,model="关注聊天页断言")
        if gzdy:
            time.sleep(1)
            self.roomPage.go_back()
        self.wait_click_element(newsloc.tv_title_two,model="粉饰tap")
        self.replace_click(newsloc.tv_position,model="粉丝列表") #粉丝列表
        fsdy = self.assert_true(newsloc.editTextMessage,model="粉丝聊天页断言")
        if fsdy:
            time.sleep(1)
            self.roomPage.go_back()
        self.wait_click_element(newsloc.tv_title_three,model="好友tap")
        self.replace_click(newsloc.tv_position,model="好友列表") #好友列表
        hydy = self.assert_true(newsloc.editTextMessage,model="好友聊天页断言")
        if hydy:
            time.sleep(1)
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
        
    #点击列表中的用户并检查用户状态
    def list_user_status(self,news_loc,model=None):
        followlist = self.public_list(news_loc,model=model) 
        if followlist and len(followlist) > 0:
            num = random.randint(0,len(followlist) - 1)
            followlist[num].click()
            part_text = "已被冻结"
            yesnodj = self.get_toast_exist(part_text,model="用户状态")
            if yesnodj and part_text in yesnodj:
                log.info("该用户已被冻结")
                return False
            else:
                return True
                 


    def replace_click(self, newsloc,model=None):
        for i in range(3):
            us = self.list_user_status(newsloc,model=model)
            if us == False:
                self.swipeDown()
                time.sleep(3)
            else:
                break
        time.sleep(5)