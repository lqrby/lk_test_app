from Common.basepage import BasePage
from Common.log import get_logger
from Pages.iOS_pageLocators.hot_pageLocators import HotPageLocators as loc
from Pages.iOS_pageObjects.home_page import HomePage

log = get_logger(logger_name="热门操作日志")

class HotPage(BasePage):

    # 进入热门
    def hot_home(self):
        self.wait_eleVisible(loc.hot, model="等待热门")
        self.click_element(loc.hot, model="点击热门")
        return HomePage(self.driver)

    # 进入榜单
    def ranking(self):
        self.wait_eleVisible(loc.ranking, model="等待榜单")
        self.click_element(loc.ranking, model="点击榜单")
        self.wait_eleVisible(loc.ranking_title, model="等待榜单title")
        ranking_text = self.get_text(loc.ranking_title, model="获取榜单文本")
        self.wait_eleVisible(loc.arrowLeft, model="等待返回")
        self.click_element(loc.arrowLeft, model="点击返回")
        return ranking_text

    # 搜索up号
    def search(self, upName):
        self.wait_eleVisible(loc.search, model="等待搜索")
        self.click_element(loc.search, model="点击搜索")
        self.wait_eleVisible(loc.search_up, model="等待搜索栏")
        self.input_text(loc.search_up, upName, model="输入up号")
        self.click_element(loc.search_ok, model="确认搜索")
        search_result = self.get_text(loc.search_result, model="获取搜索结果文本")
        self.wait_eleVisible(loc.cancel, model="等待取消")
        self.click_element(loc.cancel, model="点击取消")
        return search_result

    # 消息
    def message(self):
        self.wait_eleVisible(loc.message, model="等待消息")
        self.click_element(loc.message, model="点击消息")
        message_tetle = self.get_text(loc.message_title, model="获取消息title文本")
        return message_tetle

    # 筛选country
    def screen(self):
        self.wait_eleVisible(loc.screen, model="等待筛选")
        self.click_element(loc.screen, model="点击筛选")
        screen_title = self.get_text(loc.screen_title, model="获取筛选title文本")
        self.wait_eleVisible(loc.TW, model="等待台湾")
        self.click_element(loc.TW, model="点击台湾")
        TW_title = self.get_text(loc.TW_title, model="获取台湾title文本")
        return screen_title, TW_title

    # 进入直播间
    def room(self):
        HomePage(self.driver).hot_check()
        self.scrollToView(loc.room)
        self.click_element(loc.room, model="点击直播间")
        self.swipeToView(loc.room_text)
        room_text = self.get_text(loc.room_state, model="获取聊天室连接成功文案")
        return room_text

    # 返回 	nav arrowLeft
    def arrowLeft(self):
        self.click_element(loc.arrowLeft, model="点击返回")
