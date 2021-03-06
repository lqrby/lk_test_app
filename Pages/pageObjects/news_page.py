from operator import mod
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

    def list_assert(self,loc,model=None):
        if self.is_element_exist(loc,model=model):
            time.sleep(1)
            self.roomPage.go_back()
        elif self.is_element_exist(newsloc.invite_him_to_play,model="邀他玩"):
            self.driver.press_keycode(4)
            time.sleep(2)
            gzdy = self.assert_true(newsloc.editTextMessage,model="关注聊天页断言")
            if gzdy:
                time.sleep(1)
                self.roomPage.go_back()
            else:
                log.info("关注聊天页断言错误")
                self.save_webImgs("关注聊天页断言错误")
                self.driver.press_keycode(4)
        elif self.is_element_exist(newsloc.War_wall,model="展墙"):
            log.info("进入了用户资料页且断言成功")
            time.sleep(1)
            self.roomPage.go_back()
        else:
            log.info("迷路了不知道进哪里了")
            # self.switch_navigate("迷路了不知道进哪里了")
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)
            self.roomPage.go_back()

    
    '''
    通讯录
    '''
    def mail_list(self):
        self.wait_click_element(homeloc.message_moduke,model="消息模块")
        time.sleep(2)
        self.wait_click_element(newsloc.iv_msg_contact,model="通讯录按钮")
        self.view_user_homepage(newsloc.tv_position,model="关注列表") #关注列表
        
        self.wait_click_element(newsloc.tv_title_two,model="粉丝tap")
        self.view_user_homepage(newsloc.tv_position,model="粉丝列表") #粉丝列表
        
        self.wait_click_element(newsloc.tv_title_three,model="好友tap")
        self.view_user_homepage(newsloc.tv_position,model="好友列表") #好友列表

        self.wait_click_element(newsloc.iv_extra,model="添加好友按钮")
        time.sleep(2)
        self.assert_true(newsloc.et_input,model="搜索输入框断言") 
        page_source_result = self.driver.page_source
        # self.assert_in("推荐聊天室",page_source_result,model="推荐聊天室标题")
        self.assert_in("附近在玩",page_source_result,model="附近在玩标题")
        self.roomPage.go_back()
        time.sleep(2)
        self.roomPage.go_back()
        time.sleep(2)
        return True
        
    #点击列表中的用户并检查用户状态
    def view_user_homepage(self,news_loc,model=None):
        followlist = self.assert_len(news_loc,model=model) 
        mark = False
        if followlist and len(followlist) > 0:
            # for i in range(3):
            num = random.randint(0,len(followlist) - 1)
            log.info("{}中随机点击某一用户".format(model))
            followlist[num].click()
            part_text = "已被冻结"
            yesnodj = self.get_toast_exist(part_text,model="用户状态")
            if yesnodj and part_text in yesnodj:
                log.info("该用户已被冻结")
                self.swipeDown()
                time.sleep(3)
                self.view_user_homepage(news_loc,model = model)
            else:
                self.list_assert(newsloc.editTextMessage,model="关注用户聊天页断言")
                mark = True
                # break
            return mark
        else:
            return False
                 
