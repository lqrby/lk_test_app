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
    @allure.title('消息-通讯录测试用例')           
    def test_news(self, startApp_keepUserData):
        log.info("*********************消息-通讯录-测试用例*********************")
        news_page = NewsPage(startApp_keepUserData)
        mail_list = news_page.mail_list()
        with allure.step("查看用户主页"):
            try:
                assert mail_list == True
                log.info("查看用户主页资料断言成功")
            except AssertionError as a:
                log.error("查看用户主页资料断言失败")
                raise


    

if __name__ == '__main__':
    pytest.main()
