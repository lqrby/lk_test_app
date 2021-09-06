from Pages.pageLocators.contacts_locators import Contacts as ConLoc
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as Mb
import random

'''选择某个好友，组建群聊'''


class Contacts(BasePage):
    ''''''
    '''点击好友列表中某一位好友'''

    def clickFriend(self, a):
        friendList = self.get_elements((Mb.XPATH, '//*[@resource-id="com.asiainno.uplive:id/recyclerCommon"]/android'
                                                  '.widget.LinearLayout'))
        if friendList.__len__() > 3:
            friendList[a].find_element(Mb.ID, "com.asiainno.uplive:id/txtName").click()

    '''选择群聊'''

    def clickGroup(self):
        self.wait_element_clickable(ConLoc.group)
        self.click_element(ConLoc.group, model="点击群聊")
        groupList = self.get_elements((Mb.XPATH, '//*[@resource-id="com.asiainno.uplive:id/recyclerView"]/android'
                                                 '.widget.RelativeLayout'))
        if groupList.__len__() > 0:
            randa = random.randint(0, groupList.__len__())
            groupList[randa].find_element(Mb.ID, "com.asiainno.uplive:id/name").click()
