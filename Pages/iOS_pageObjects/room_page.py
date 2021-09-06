from Common.basepage import BasePage
from Common.log import get_logger
from Pages.iOS_pageLocators.room_locators import RoomLocators as loc
from Pages.iOS_pageObjects.home_page import HomePage

log = get_logger(logger_name="直播间操作日志")

class RoomPage(BasePage):
    # 聊天
    def room_chat(self, chat_text):
        # 点击聊天按钮
        self.wait_eleVisible(loc.room_chat, model="等待点击聊天")
        self.click_element(loc.room_chat, model="点击聊天")
        # 发送消息
        self.wait_eleVisible(loc.room_chat_in, model="等待输入")
        self.input_text(loc.room_chat_in, chat_text, model="输入内容")
        self.wait_eleVisible(loc.room_chat_send, "等待发送")
        self.click_element(loc.room_chat_send, model="点击发送")
        self.swipeToView(chat_text)
        room_text = self.get_text(loc.room_state, model="获取聊天室连接成功文案")
        return room_text

    # 直播间分享
    def room_share(self):
        # 点击分享
        self.wait_eleVisible(loc.room_share, model="等待分享")
        self.click_element(loc.room_share, model="点击分享")
        return self

    def room_share_friend(self, friend_name):
        # 分享好友
        self.wait_eleVisible(loc.room_share_friend, model="等到分享的好友")
        self.click_element(loc.room_share_friend, model="点击分享的好友")
        self.wait_eleVisible(loc.room_share_in, model="等待输入好友名字")
        self.input_text(loc.room_share_in, friend_name, model="输入好友名字")
        self.wait_eleVisible(loc.room_share_who, model="等待选择好友")
        self.click_element(loc.room_share_who, model="点击好友")
        self.click_element(loc.room_share_who, model="点击好友")
        self.wait_eleVisible(loc.room_share_next, model="等待确认")
        self.click_element(loc.room_share_next, model="点击确认")
        text = self.isToastMessage(loc.share_friend_ck)
        return text

