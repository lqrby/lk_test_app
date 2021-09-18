'''
Author: your name
Date: 2021-09-06 15:59:49
LastEditTime: 2021-09-18 13:27:37
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Test_iOS/test_live.py
'''
import time
import pytest
from Common.log import get_logger
from Pages.iOS_pageObjects.streaming_page import StreamingPage
from Pages.iOS_pageObjects.room_page import RoomPage
from TestDatas.iOS_Datas.roomData import *
from Pages.iOS_pageObjects.common_buss import CommonBus

log = get_logger(logger_name="主播开播操作日志")

@pytest.mark.run(order=1)
class Test_Live:
    # 开启直播
    @pytest.mark.parametrize("case", live)
    def test_hot_home(self, case, start_iOS):
        Streaming = StreamingPage(start_iOS)
        result = Streaming.start_live()
        try:
            assert result == case["live"]
            log.info("开始直播")
        except AssertionError as a:
            log.exception("断言失败")
            self.hot.save_webImgs("直播_断言")
            raise a

    # 直播分享
    @pytest.mark.parametrize("case", user_name)
    def test_live_share(self, case, start_iOS):
        Streaming = StreamingPage(start_iOS)
        Streaming.live_share()
        room_share = RoomPage(start_iOS)
        share_result = room_share.room_share_friend(case["u_name"])
        try:
            assert share_result == case["check"]
            log.info("分享好友")
        except AssertionError as a:
            log.exception("断言失败")
            self.hot.save_webImgs("分享好友_断言")
            raise a