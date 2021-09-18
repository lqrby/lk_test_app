'''
Author: your name
Date: 2021-09-06 15:59:49
LastEditTime: 2021-09-18 13:26:20
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Test_Cases/a_test_IM.py
'''
import allure
import pytest
from Common.log import get_logger
from TestDatas.IM import sendsinglemessage, sendgroupmessage
from Pages.pageObjects.IM_page import IMPage

log = get_logger(logger_name="IM操作日志")


@pytest.mark.run(order=2)
@allure.feature('IM')
class Test_IM:
    """消息进入子模块查看是否正确"""

    @pytest.mark.success
    @allure.story('IM')
    @allure.title('IM')
    def test_IM(self, startApp_keepUserData):
        log.info("********************************IM-官方客服-测试用例**************************************************")
        IM_page = IMPage(startApp_keepUserData)
        actual = IM_page.IM().official_customer()
        log.info(actual)
        with allure.step("官方客服页面测试用例"):
            try:
                assert actual == "官方客服"
                log.error("官方客服测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                IM_page.save_webImgs("官方客服测试用例-断言-截图")
                raise a

        log.info("********************************IM-官方助手-测试用例**************************************************")
        actual = IM_page.official_assistant()
        with allure.step("官方助手页面测试用例"):
            try:
                assert actual in "官方助手"
                log.error("官方助手-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                IM_page.save_webImgs("官方助手-断言-截图")
                raise a

        log.info(
            "************************************IM-礼物助手-测试用例*****************************************************")
        actual = IM_page.gift_assistant()
        with allure.step("礼物助手页面测试用例"):
            try:
                assert actual in "礼物助手"
                log.error("礼物助手-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                IM_page.save_webImgs("礼物助手-断言-截图")
                raise a

        log.info("************************************IM-打招呼-测试用例*****************************************************")
        actual = IM_page.greet_sb()
        with allure.step("打招呼页面测试用例"):
            try:
                assert actual in "收到的招呼"
                log.error("打招呼-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                IM_page.save_webImgs("打招呼-断言-截图")
                raise a

    '''通讯录发送IM'''

    @pytest.mark.success
    @pytest.mark.parametrize("case", sendsinglemessage)
    @allure.story('address')
    @allure.title('address')
    def test_IM_address(self, case, startApp_keepUserData):
        log.info(
            "************************************IM-通讯录单聊-测试用例*****************************************************")
        IM_page = IMPage(startApp_keepUserData)
        actual = IM_page.IM().address_book(case["message"])
        with allure.step("通讯录单聊页面测试用例"):
            try:
                assert actual == case["expected"]
                log.error("IM-通讯录单聊-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                IM_page.save_webImgs("IM-通讯录单聊-断言-截图")
                raise a


if __name__ == '__main__':
    pytest.main()
