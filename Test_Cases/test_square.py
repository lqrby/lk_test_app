import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.square_page import SquarePage

log = get_logger(logger_name="设置操作日志")



@pytest.mark.run(order=4)
@allure.feature('广场模块')
class TestSquare:
    '''附近动态'''  
    @pytest.mark.success
    @allure.story('推荐动态')
    @allure.title('推荐动态测试用例')           
    def test_nearbyDynamics(self, startApp_keepUserData):
        log.info("*********************广场模块-推荐动态-测试用例*********************")
        square_page = SquarePage(startApp_keepUserData)
        nearby_dynamics = square_page.nearby_dynamics()
        with allure.step("查看推荐动态"):
            try:
                assert len(nearby_dynamics) > 0
                log.info("查看推荐动态断言成功")
            except AssertionError as a:
                log.error("查看推荐动态断言失败")
                raise
        


if __name__ == '__main__':
    pytest.main()
