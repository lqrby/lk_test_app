from Common.basepage import BasePage
from Pages.pageLocators.pop_locators import PopUp
from Pages.pageLocators.reward_locators import RewardPageLocator as loc
from Pages.pageLocators.home_locators import HomePageLocator
from Common.log import get_logger

import time

'''直播打赏-页面操作行为'''
log = get_logger(logger_name="页面操作行为")


class RewardPage(BasePage):
    '''打赏-搜索固定up号进行进入直播间'''

    def enter_the_studio(self, up):
        if self.is_element_exist("探索", 3):
            self.click_element(HomePageLocator.click_hot)
        self.wait_eleVisible(loc.search)
        self.click_element(loc.search, model="点击主页搜索")

        self.wait_eleVisible(loc.input_up)
        self.input_text(loc.input_up, up, model="输入up号")

        self.click_element(loc.click_search, model="点击搜索")

        self.wait_eleVisible(loc.click_list)
        self.click_element(loc.click_list, model="点击用户")

        self.wait_eleVisible(loc.click_live)
        self.click_element(loc.click_live, model="点击进入直播间")
        time.sleep(2)
        return self

    '''打赏-进入直播间选择礼物进行打赏'''

    def give(self):
        if self.is_element_exist(PopUp.allowpop[1]):
            self.click_element(PopUp.allowpop)
        time.sleep(2)
        if self.is_element_exist(loc.popup_bubble[1]):
            self.click_element(loc.popup_bubble)
        self.click_element(loc.click_gift, model="点击进礼物")
        if self.is_element_exist(loc.popup_bubble[1]):
            self.click_element(loc.popup_bubble)
        gifts = self.get_elements(loc.gifts)
        self.click_element_byele(gifts[0], model="选择礼物")
        self.click_element(loc.click_give, model="点击赠送")
        return self

    '''打赏成功-获取断言的文本'''

    def get_the_text(self):
        self.wait_eleVisible(loc.get_text)
        return self.get_text(loc.get_text, model="刷礼物成功，获取文本")

    '''打赏多个礼物'''

    def Multiple_give(self):

        self.click_element(loc.click_gift, model="点击进礼物")
        gifts = self.get_elements(loc.gifts)
        self.click_element_byele(gifts[0], model="选择礼物")
        self.click_element(loc.llGiftNums, model="点击选择数量")
        self.click_element(loc.tvNum, model="选择礼物数量10")
        self.click_element(loc.click_give, model="点击赠送")
        return self

    '''连发打赏'''

    def Lianfa(self):
        self.click_element(loc.click_gift, model="点击进礼物")
        gifts = self.get_elements(loc.gifts)
        self.click_element_byele(gifts[0], model="选择礼物")
        self.click_element(loc.click_give, model="点击赠送")
        time.sleep(0.2)
        self.tap_by_coordinate((0.854, 0.964), times=5, model="点击连发")
        return self
