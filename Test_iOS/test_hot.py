import pytest
from Common.log import get_logger
from Pages.iOS_pageObjects.hot_page import HotPage
from TsetDatas.login import login_phone
from Pages.iOS_pageObjects.login_page import LoginPage
from Pages.iOS_pageObjects.env_page import EnvPage
from TsetDatas.iOS_Datas.hotData import *
from Pages.iOS_pageObjects.common_buss import CommonBus

log = get_logger(logger_name="热门操作日志")

@pytest.mark.run(order=1)
class Test_Hot:
    """正常登陆的测试用例--手机号登陆"""
    @pytest.mark.success
    @pytest.mark.parametrize("case", login_phone)
    def test_phone_login(self, case, start_iOS):
        log.info("*********热门用例：热门首页*********")
        """操作步骤：
            环境初始化
            1.登录
            2.热门断言
        """
        env = EnvPage(start_iOS)
        env.env_change("stage")

        login_page = LoginPage(start_iOS)
        login_page.login_check()
        result = login_page.login_iOS_phone(case["username"], case["password"])
        '''异常处理，预期结果与实际结果做对比，如果断言正确pass、如果断言失败或查找元素失败，自动截图保存路径到Outputs / screenshots'''
        try:
            assert result == case["check"]
            log.info("登录成功")
        except AssertionError as a:
            log.exception("断言失败")
            login_page.save_webImgs("登录success_断言")
            raise a

    # 热门首页
    @pytest.mark.parametrize("case", hot)
    def test_hot_home(self, case, start_iOS):
        self.hot = HotPage(start_iOS)
        result = self.hot.hot_home().success_title()
        try:
            assert result == case["hot_home"]
            log.info("热门首页")
        except AssertionError as a:
            log.exception("断言失败")
            self.hot.save_webImgs("热门首页_断言")
            raise a

    # 榜单用例
    @pytest.mark.parametrize("case", ranking)
    def test_hot_ranking(self, case, start_iOS):
        hot = HotPage(start_iOS)
        ranking_resule = hot.ranking()
        try:
            assert ranking_resule == case["ranking"]
            log.info("热门进入榜单")
        except AssertionError as a:
            log.exception("断言失败")
            hot.save_webImgs("榜单_断言")
            raise a

    # 搜索up号用例
    @pytest.mark.parametrize("case", user_name)
    def test_hot_search(self, case, start_iOS):
        hot = HotPage(start_iOS)
        search_resule = hot.search(case["u_name"])
        try:
            assert search_resule == case["u_name"]
            log.info("热门页点搜索")
        except AssertionError as a:
            log.exception("断言失败")
            hot.save_webImgs("搜索_断言")
            raise a

    # 进入IM页用例
    @pytest.mark.parametrize("case", message)
    def test_hot_message(self, case, start_iOS):
        hot = HotPage(start_iOS)
        message_resule = hot.message()
        try:
            assert message_resule == case["message"]
            log.info("热门页点击消息")
        except AssertionError as a:
            log.exception("断言失败")
            hot.save_webImgs("IM页_断言")
            raise a

    # 筛选用例
    @pytest.mark.parametrize("case", screen)
    def test_hot_screen(self, case, start_iOS):
        hot = HotPage(start_iOS)
        screen_resule = hot.screen()
        try:
            assert screen_resule[0] == case["screen"]
            assert screen_resule[1] == case["country"]
            log.info("热门国家筛选")
        except AssertionError as a:
            log.exception("断言失败")
            hot.save_webImgs("筛选_断言")
            raise a

    # 进入直播间
    @pytest.mark.parametrize("case", room)
    def test_hot_room(self, case, start_iOS):
        hot = HotPage(start_iOS)
        room_resule = hot.room()
        try:
            assert case["room"] in room_resule
            log.info("热门页点击直播间")
        except AssertionError as a:
            log.exception("断言失败")
            hot.save_webImgs("进入直播间_断言")
            raise a


if __name__ == '__main__':
    pytest.main()
