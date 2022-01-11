import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.news_page import NewsPage

log = get_logger(logger_name="设置操作日志")



@pytest.mark.run(order=7)
@allure.feature('消息模块')
class TestNews:
    '''消息---通讯录'''  
    @pytest.mark.success
    @allure.story('消息-通讯录')
    @allure.title('推荐动态测试用例')           
    def test_news(self, startApp_keepUserData):
        log.info("*********************广场模块-推荐动态-测试用例*********************")
        news_page = NewsPage(startApp_keepUserData)
        mail_list = news_page.mail_list()
        with allure.step("查看推荐动态"):
            try:
                assert mail_list == True
                log.info("查看推荐动态断言成功")
            except AssertionError as a:
                log.error("查看推荐动态断言失败")
                raise


    '''广场---关注'''  
    @pytest.mark.success
    @allure.story('广场-关注')
    @allure.title('广场关注测试用例')           
    def test_squareAttention(self, startApp_keepUserData):
        log.info("*********************广场模块-关注-测试用例*********************")
        square_page = NewsPage(startApp_keepUserData)
        nearby_dynamics = square_page.square_attention()
        with allure.step("查看我已关注用户的动态"):
            try:
                assert len(nearby_dynamics) > 0
                log.info("查看我已关注用户的动态断言成功")
            except AssertionError as a:
                log.error("查看我已关注用户的动态断言失败")
                raise
        


if __name__ == '__main__':
    pytest.main()