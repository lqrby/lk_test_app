from Common.basepage import BasePage
from Common.log import get_logger
from Pages.iOS_pageLocators.streaming_locators import StreamingLocators as loc


log = get_logger(logger_name="热门操作日志")

class StreamingPage(BasePage):
    # 开启直播
    def start_live(self):
        self.wait_eleVisible(loc.streaming, model='等待开播')
        self.click_element(loc.streaming, model='点击开播按钮')

        self.wait_eleVisible(loc.Begintolive, model="等待开始直播")
        self.click_element(loc.Begintolive, model="点击开始直播")

        self.swipeToView(loc.text)
        live_text = self.get_text(loc.accesstocopy, model="获取开播成功文本")
        return live_text

    # 直播分享
    def live_share(self):
        self.wait_eleVisible(loc.room_pop, model='等待更多')
        self.click_element(loc.room_pop, model='点击更多')
        self.tap_by_coordinate(loc.share, model="点击分享")

