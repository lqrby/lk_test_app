import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.hot_page import HotPage

log = get_logger(logger_name="热门操作日志")


@pytest.mark.run(order=1)
@allure.feature('热门首页')
class Test_Hot:

    @pytest.mark.ranking
    @allure.story('排行榜')
    @allure.title("排行榜")
    def test_ranking(self, startApp_keepUserData):
        hot_page = HotPage(startApp_keepUserData)

        log.info("***********************************热门排行榜测试用例-测试用例**************************************")

        actual_Ranking = hot_page.into_hot().ranking()
        with allure.step("Up风云榜"):
            try:
                assert actual_Ranking == "Up风云榜"
                log.error("热门排行榜测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门筛选测试用例-断言-截图")
                raise a

        log.info("***********************************热门排行榜主播榜单测试用例-测试用例**************************************")

        actual_hostrank = hot_page.hostrank()
        with allure.step("热门排行榜主播榜单测试用例"):
            try:
                assert int(actual_hostrank) > 0
                log.error("热门主播榜单测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门主播榜单测试用例-断言-截图")
                raise a

        log.info("***********************************热门排行榜财富总榜测试用例-测试用例**************************************")

        actual_moneytotalrank = hot_page.moneytotalrank()
        with allure.step("热门排行榜财富总榜测试用例"):
            try:
                assert int(actual_moneytotalrank) > 0
                log.error("热门排行榜财富总榜测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门排行榜财富总榜测试用例-断言-截图")
                raise a

        log.info("***********************************热门排行榜礼物星榜测试用例-测试用例**************************************")

        actual_starrank = hot_page.starrank()
        with allure.step("热门排行榜礼物星榜测试用例"):
            try:
                assert actual_starrank == "换个姿势重来一次"
                log.error("热门排行榜礼物星榜测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门排排行榜礼物星榜测试用例-断言-截图")
                raise a

        log.info("***********************************热门守护总榜查看测试用例-测试用例**************************************")

        actual_guardian = hot_page.guardian()
        with allure.step("热门守护总榜查看测试用例"):
            try:
                assert actual_guardian == True
                log.error("热门守护总榜查看测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门守护总榜查看测试用例-断言-截图")
                raise a

    @pytest.mark.message
    @allure.story('消息页面用例')
    @allure.title('消息页面用例')
    def test_message(self, startApp_keepUserData):
        hot_page = HotPage(startApp_keepUserData)
        log.info("***********************************热门进入消息页面测试用例-测试用例**************************************")
        actual_message = hot_page.into_hot().message()
        with allure.step("热门进入消息页面测试用例"):
            try:
                assert actual_message == "消息"
                log.error("热门进入消息页面测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门进入消息页面测试用例-断言-截图")
                raise a

    @pytest.mark.morepage
    @allure.story('筛选页面用例')
    @allure.title('筛选页面用例')
    def test_morepage(self, startApp_keepUserData):
        log.info("***********************************热门进入到筛选页面测试用例-测试用例**************************************")
        hot_page = HotPage(startApp_keepUserData)
        actual_morepage = hot_page.into_hot().morepage()
        with allure.step("热门进入到筛选页面测试用例"):
            try:
                assert actual_morepage is True
                log.error("热门进入到筛选页面测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门进入到筛选页面测试用例-断言-截图")
                raise a

        log.info("***********************************热门标签选择页面测试用例-测试用例**************************************")

        actual_showAllLabel = hot_page.showAllLabel()
        with allure.step("热门标签选择页面测试用例"):
            try:
                assert actual_showAllLabel == "Uplive"
                log.error("热门标签选择页面测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                hot_page.save_webImgs("热门标签选择页面测试用例-断言-截图")
                raise a


if __name__ == '__main__':
    pytest.main(['-s', './test_hot.py', '--alluredir', 'temp'])
