import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.set_page import SetPage

# from pytest import assume


log = get_logger(logger_name="设置操作日志")

'''设置'''


@pytest.mark.run(order=4)
@allure.feature('设置页面')
class Test_setting:
    @pytest.mark.success
    @allure.story('设置页面测试用例')
    @allure.title('设置页面测试用例')
    def test_setting(self, startApp_keepUserData):
        log.info("***********************************设置-账号绑定-测试用例**************************************")
        set_page = SetPage(startApp_keepUserData)
        actual_Account_binding = set_page.set().set_Account_binding()
        with allure.step("账号绑定页面测试用例"):
            try:
                assert actual_Account_binding == "账号绑定"
                log.error("账号绑定测试用例-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("查询账号绑定测试用例-断言-截图")
                raise a

        # log.info(
        #     "************************************设置-实名认证-测试用例*****************************************************")
        # actual_set_real_name = set_page.set_real_name("郭牛牛", "140430199999")
        # try:
        #     assert actual_set_real_name in "身份验证失败"
        #     log.error("身份验证失败-测试用例通过")
        # except AssertionError as a:
        #     log.error("断言失败")
        #     set_page.save_webImgs("身份验证失败-断言-截图")
        #     raise a

        log.info("*************************************设置-我的直播标签-测试用例******************************************")
        actual_my_live_tag = set_page.my_live_tag()
        with allure.step("我的直播标签页面测试用例"):
            try:
                assert actual_my_live_tag == "标签保存成功"
                log.error("保存标签-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("我的直播标签-断言-截图")
                raise a

        log.info("*************************************设置-黑名单-测试用例******************************************")
        actual_blacklist = set_page.blacklist()
        with allure.step("黑名单页面测试用例"):
            try:
                assert actual_blacklist == "暂无被拉黑用户"
                log.error("黑名单-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("黑名单-断言-截图")
                raise a

        log.info("*************************************设置-消息提醒-测试用例******************************************")
        actual_notificationSettingsRL = set_page.notificationSettingsRL()
        with allure.step("消息提醒页面测试用例"):
            try:
                assert actual_notificationSettingsRL is True
                log.error("消息提醒-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("消息提醒-断言-截图")
                raise a

        log.info("*************************************设置-隐私设置-测试用例******************************************")
        actual_privacy = set_page.privacy()
        with allure.step("隐私设置页面测试用例"):
            try:
                assert actual_privacy is True
                log.error("隐私设置-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("隐私设置-断言-截图")
                raise a

        log.info("*************************************设置-礼物设置-测试用例******************************************")
        actual_gift = set_page.gift()
        with allure.step("礼物设置页面测试用例"):
            try:
                assert actual_gift is True
                log.error("礼物设置-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("礼物设置-断言-截图")
                raise a

        log.info("*************************************设置-点击悬浮窗播放开关-测试用例******************************************")
        actual_floatWindowSwitch = set_page.floatWindowSwitch()
        with allure.step("点击悬浮窗播放开关测试用例"):
            try:
                assert actual_floatWindowSwitch is True
                log.error("点击悬浮窗播放开关-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("点击悬浮窗播放开关-断言-截图")
                raise a

        log.info("*************************************设置-点击直播性能优化开关-测试用例******************************************")
        actual_broadcastHardwareSwitch = set_page.broadcastHardwareSwitch()
        with allure.step("点击直播性能优化开关测试用例"):
            try:
                assert actual_broadcastHardwareSwitch is True
                log.error("点击直播性能优化开关-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("点击直播性能优化开关-断言-截图")
                raise a

        log.info("*************************************设置-关于Up直播-测试用例******************************************")
        actual_aboutRL = set_page.aboutRL()
        with allure.step("关于Up直播页面测试用例"):
            try:
                assert actual_aboutRL == "关于Up直播"
                log.error("关于Up直播-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                set_page.save_webImgs("关于Up直播-断言-截图")
                raise a


if __name__ == '__main__':
    pytest.main()
