import time

import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.reward_page import RewardPage

log = get_logger(logger_name="打赏操作日志")


@pytest.mark.run(order=5)
@allure.feature('直播间送礼测试用例')
class Test_reward:
    """打赏成功"""

    @pytest.mark.success
    @allure.story('单个礼物打赏测试用例')
    @allure.title('单个礼物打赏测试用例')
    def test_success_reward(self, startApp_keepUserData):
        reward_page = RewardPage(startApp_keepUserData)
        log.info("*********开播用例：打赏单个礼物成功*********")
        time.sleep(1)
        actual = reward_page.enter_the_studio("s1234").give().get_the_text()
        log.info(actual)
        with allure.step("打赏单个礼物成功"):
            try:
                assert "赠送了" in actual
                log.error("打赏成功")
            except AssertionError as a:
                log.error("断言失败")
                reward_page.save_webImgs("打赏-断言-截图")
                raise a
        log.info("*********开播用例：打赏多个礼物成功*********")
        time.sleep(1)
        actual = reward_page.Multiple_give().get_the_text()
        log.info(actual)
        with allure.step("打赏多个礼物成功"):
            try:
                assert "赠送了" in actual
                log.error("打赏成功")
            except AssertionError as a:
                log.error("断言失败")
                reward_page.save_webImgs("打赏多个-断言-截图")
                raise a
        log.info("*********开播用例：连发打赏礼物成功*********")
        time.sleep(1)
        actual = reward_page.Lianfa().get_the_text()
        log.info(actual)
        with allure.step("连发打赏礼物成功"):
            try:
                assert "赠送了" in actual
                log.error("打赏成功")
            except AssertionError as a:
                log.error("断言失败")
                reward_page.save_webImgs("连续打赏-断言-截图")
                raise a

if __name__ == '__main__':
    pytest.main()
