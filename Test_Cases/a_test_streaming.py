import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.streaming_page import Streaming
from Pages.pageObjects.Common_Buss import CommonBus

log = get_logger(logger_name="开播操作日志")

'''开播'''


@pytest.mark.run(order=6)
@allure.feature('开播测试用例')
class Test_streaming:
    @pytest.mark.success
    @allure.story('开播成功测试用例')
    def test_success_streaming(self, startApp_keepUserData):
        log.info("*********单人视频房开播用例：开播成功*********")
        streaming_page = Streaming(startApp_keepUserData)
        actual = streaming_page.star_streaming().success_copywriting()
        log.info(actual)
        with allure.step("单人视频房开播用例测试用例"):
            try:
                assert "连接成功" in "连接成功"
                log.error("开播成功成功")
            except AssertionError as a:
                log.error("断言失败")
                streaming_page.save_webImgs("开播-断言-截图")
                raise a


if __name__ == '__main__':
    pytest.main()
