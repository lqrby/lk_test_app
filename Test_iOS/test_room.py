import pytest
from Common.log import get_logger
from Pages.iOS_pageObjects.streaming_page import StreamingPage
from Pages.iOS_pageObjects.room_page import RoomPage
from TsetDatas.iOS_Datas.roomData import *
from Pages.iOS_pageObjects.common_buss import CommonBus

log = get_logger(logger_name="直播间操作日志")

@pytest.mark.run(order=1)
class Test_Room:
    # 直播分享
    @pytest.mark.parametrize("case", user_name)
    def test_live_share(self, case, start_iOS):
        room_share = RoomPage(start_iOS)
        room_share.room_share()
        share_result = room_share.room_share_friend(case["u_name"])
        try:
            assert share_result == case["check"]
            log.info("分享好友")
        except AssertionError as a:
            log.exception("断言失败")
            self.hot.save_webImgs("分享好友_断言")
            raise a