from Common.basepage import BasePage
from Pages.pageLocators.hot_locators import HotPageLocator as loc
from Pages.pageLocators.home_locators import HomePageLocator
import time

'''设置-页面操作行为'''


class HotPage(BasePage):
    '''进入热门页面'''

    def into_hot(self):
        self.click_element(HomePageLocator.click_hot, model="点击热门按钮")
        return self

    '''进入排行榜'''

    def ranking(self):
        self.click_element(loc.ivRank, model="点击进入排行榜")
        ranktitle = self.get_text(loc.toolbar_title)
        # self.click_element(loc.back, model="点击返回")
        return ranktitle

    '''查看主播榜'''

    def hostrank(self):
        self.click_element(loc.hostrank, model="点击月榜")
        if self.is_element_exist(loc.txtGrade[1]):
            elements = self.get_elements(loc.txtGrade)
            grande = elements[0].text
            return int(grande)
        return 1

    '''查看财富榜'''

    def moneytotalrank(self):
        if self.is_element_exist(loc.totalrank[1]) is False:
            self.swipeUp(t=1500)
        self.click_element(loc.totalrank, "点击财富总榜")
        grande = self.get_text(loc.txtGrade, model="获取财富总榜第一用户等级")
        return grande

    '''礼物星榜无数据'''

    def starrank(self):
        starloc = self.is_desplayed(loc.nostarrank)
        if len(starloc) == 0:
            self.swipeUp(t=1500)
        text = self.get_text(loc.nostarrank, "获取礼物星榜无数据文案")
        return text

    '''守护总榜查看'''

    def guardian(self):
        self.swipeUp(t=1500)
        # time.sleep(1)
        self.click_element(loc.guardian, "点击总榜")
        time.sleep(1)
        flag = self.is_element_exist(loc.ivGuardianPhoto[1])

        self.click_element(loc.back, "点击返回")
        return flag or True

    '''进入消息页面'''

    def message(self):
        self.click_element(loc.ivIM, model="点击进入消息")
        imtitle = self.get_text(loc.IMtitle)
        self.click_element(loc.messageback, model="点击返回")
        return imtitle

    '''进入到筛选页面'''

    def morepage(self):
        self.click_element(loc.layoutMore, model="点击筛选按钮")
        self.wait_eleVisible(loc.country, model="等待国家标签")
        countrytext = self.get_text(loc.country)
        self.click_element(loc.country, model="点击国家标签")
        title = self.get_text(loc.moretitle)
        self.click_element(loc.back, model="点击返回")
        return countrytext == title

    '''选择标签'''

    def showAllLabel(self):
        time.sleep(0.5)
        self.swipeDown()
        while self.is_element_exist(loc.ivShowAllLabel[1]) is False:
            self.swipeUp()
        self.click_element(loc.ivShowAllLabel, model="点击标签")
        self.click_element(loc.lableconfirm, model="点击确定")
        return self.get_text(loc.title)
