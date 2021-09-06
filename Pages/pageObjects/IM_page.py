from Common.basepage import BasePage
from Pages.pageLocators.IM_locators import IMPageLocator as loc
import time
from appium.webdriver.common.mobileby import MobileBy as Mb

'''IM-页面操作行为'''


class IMPage(BasePage):
    ''''''
    '''进入消息模块'''

    def IM(self):
        self.wait_eleVisible(loc.click_my)
        self.click_element(loc.click_my, model="点击我的")

        self.click_element(loc.myMassage, model="点击我的消息")
        return self

    '''消息内返回操作'''

    def back_key(self):
        self.wait_eleVisible(loc.goBack, model="等待返回")
        self.click_element(loc.goBack, model="点击返回")
        return self

    '''官方客服'''

    def official_customer(self):
        self.wait_eleVisible(loc.officialCS,model="等待官方客服")
        self.click_element(loc.officialCS, model="点击官方客服")

        self.wait_eleVisible(loc.officialCS_text, model="等待查看title")
        el = self.get_text(loc.officialCS_text, model="获取客服文本")

        # self.back_key()
        self.wait_eleVisible(loc.goBack, model="等待返回")
        self.click_element(loc.goBack, model="点击返回")

        time.sleep(1)

        return el



    '''官方助手'''

    def official_assistant(self):
        self.wait_eleVisible(loc.officialHelper)
        self.click_element(loc.officialHelper, model="点击官方助手")

        self.wait_eleVisible(loc.officialHelper_title, model="等待查看title")
        el = self.get_text(loc.officialHelper_title, model="获取title")

        self.back_key()

        time.sleep(1)

        return el

    '''礼物助手'''

    def gift_assistant(self):
        self.click_element(loc.giftHelper, model="点击礼物助手")

        self.wait_eleVisible(loc.giftHelper_title, model="等待查看title")
        el = self.get_text(loc.giftHelper_title, model="获取title")

        self.back_key()

        time.sleep(1)

        return el

    '''打招呼'''

    def greet_sb(self):
        self.click_element(loc.greet , model="点击礼物助手")

        self.wait_eleVisible(loc.greet_title, model="等待查看title")
        el = self.get_text(loc.greet_title, model="获取title")

        self.wait_eleVisible(loc.goBack_1, model="等待返回")
        self.click_element(loc.goBack_1, model="点击返回")

        time.sleep(1)

        return el


    '''通讯录'''

    def address_book(self,sendText):
        self.click_element(loc.contacts , model="点击通讯录")

        self.clickFriend(2)

        self.input_text(loc.etinput, sendText, model="输入内容")

        self.click_element(loc.send, model="点击发送")

        el=self.get_text(loc.Successful_text,model="获取IM发送成功的文本")


        time.sleep(3)

        return el

    def clickFriend(self, a):
        friendList = self.get_elements((Mb.XPATH, '//*[@resource-id="com.asiainno.uplive:id/recyclerCommon"]/android'
                                                  '.widget.LinearLayout'))
        if friendList.__len__() > 3:
            friendList[a].find_element(Mb.ID, "com.asiainno.uplive:id/txtName").click()
